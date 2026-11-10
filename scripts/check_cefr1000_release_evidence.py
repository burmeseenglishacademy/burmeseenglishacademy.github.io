#!/usr/bin/env python3
"""Fail-closed CEFR-1000 release evidence gate. This does not perform reviews.

A future release requires a separate, externally supplied evidence JSON document.
Missing evidence, unsigned/self-reviewed claims, missing files and incomplete gates
always fail. Do not wire a passing provisional audit to publication.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import unicodedata
from collections import Counter

LEVELS = ("A1", "A2", "B1", "B2", "C1")
REVIEW_DOMAINS = ("english", "myanmar", "example", "cefr", "pronunciation")
VOICES = ("george", "emma")
KINDS = ("headword", "example")
GLOBAL_GATES = ("browser_regression", "mobile_regression", "physical_iphone_safari",
                "github_pages_hosting", "production_deployment", "production_assets_preserved",
                "privacy_review", "lessons_54_preserved", "ielts_1000_preserved")
ROOT = Path(__file__).resolve().parents[1]

def valid_attestation(record, *, require_url=True):
    if not isinstance(record, dict):
        return False
    for key in ("reviewer_id", "reviewed_at", "evidence_url", "content_sha256"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            return False
    if record.get("independent") is not True or record.get("self_evaluation") is not False:
        return False
    if require_url and not record["evidence_url"].startswith(("https://", "http://")):
        return False
    sha = record["content_sha256"].lower()
    return len(sha) == 64 and all(c in "0123456789abcdef" for c in sha)

def reviewed_content_sha256(entry, domain):
    """Bind an attestation to the exact reviewed field, not a free-floating digest.

    Domain payload is versioned and canonical: JSON with sorted keys, UTF-8,
    compact separators, and no ASCII escaping. Any editorial change invalidates
    the old attestation. This is structural binding, NOT proof of reviewer identity.
    """
    fields = {
        "english": "english_definition",
        "myanmar": "burmese_meaning",
        "example": "example_sentence",
        "cefr": "level",
        "pronunciation": "word",
    }
    field = fields[domain]
    payload = {"schema": 1, "domain": domain, "word": entry["word"],
               "part_of_speech": entry["part_of_speech"],
               "sense_id": entry["sense_id"], "value": entry[field]}
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()

def audit(manifest, evidence, root=ROOT):
    errors = []
    if not isinstance(manifest, dict):
        return ["approved manifest must be a JSON object"]
    entries = manifest.get("entries")
    if not isinstance(entries, list) or len(entries) != 1000:
        return ["approved manifest must contain exactly 1000 entries"]
    if manifest.get("counts_by_level") != {level: 200 for level in LEVELS}:
        errors.append("approved manifest level counts must equal 200 each")
    counts = Counter()
    seen = set()
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            errors.append(f"entry {i} invalid")
            continue
        level, word, sense = e.get("level"), e.get("word"), e.get("sense_id")
        if not isinstance(level, str) or level not in LEVELS:
            errors.append(f"entry {i}: invalid CEFR level type/value")
            continue
        counts[level] += 1
        if not all(isinstance(v, str) and v.strip() for v in (word, sense)):
            errors.append(f"entry {i}: invalid level/headword/sense")
            continue
        key = (unicodedata.normalize("NFKC", word).casefold().strip(),
               unicodedata.normalize("NFKC", sense).casefold().strip())
        if key in seen:
            errors.append(f"entry {i}: duplicate normalized headword/sense")
        seen.add(key)
        for field in ("english_definition", "burmese_meaning", "example_sentence", "part_of_speech"):
            if not isinstance(e.get(field), str) or not e[field].strip():
                errors.append(f"entry {i}: missing {field}")
        reviews = e.get("independent_reviews", {})
        for domain in REVIEW_DOMAINS:
            r = reviews.get(domain) if isinstance(reviews, dict) else None
            if not valid_attestation(r):
                errors.append(f"entry {i}: independent {domain} review evidence absent/invalid")
            else:
                if r["reviewer_id"] == e.get("author_id"):
                    errors.append(f"entry {i}: {domain} reviewer equals author")
                if not all(isinstance(e.get(k), str) and e[k].strip()
                           for k in ("word", "part_of_speech", "sense_id",
                                     {"english": "english_definition",
                                      "myanmar": "burmese_meaning",
                                      "example": "example_sentence",
                                      "cefr": "level",
                                      "pronunciation": "word"}[domain])):
                    errors.append(f"entry {i}: {domain} review cannot bind incomplete content")
                elif r["content_sha256"].lower() != reviewed_content_sha256(e, domain):
                    errors.append(f"entry {i}: {domain} review content hash mismatch")
        audio = e.get("audio", {})
        for voice in VOICES:
            for kind in KINDS:
                voice_audio = audio.get(voice) if isinstance(audio, dict) else None
                item = voice_audio.get(kind) if isinstance(voice_audio, dict) else None
                if not isinstance(item, dict) or not isinstance(item.get("path"), str):
                    errors.append(f"entry {i}: {voice}/{kind} audio path missing")
                    continue
                if not item["path"].strip():
                    errors.append(f"entry {i}: {voice}/{kind} empty audio path")
                    continue
                path = (root / item["path"]).resolve()
                if not path.is_relative_to(root.resolve()) or not path.is_file():
                    errors.append(f"entry {i}: {voice}/{kind} audio file missing/unsafe")
                    continue
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                if digest != item.get("sha256"):
                    errors.append(f"entry {i}: {voice}/{kind} audio hash mismatch")
                if not valid_attestation(item.get("listening_signoff")):
                    errors.append(f"entry {i}: {voice}/{kind} real listening signoff missing")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: expected 200, found {counts[level]}")
    gates = evidence.get("gates", {}) if isinstance(evidence, dict) else {}
    for gate in GLOBAL_GATES:
        record = gates.get(gate) if isinstance(gates, dict) else None
        if not valid_attestation(record) or record.get("passed") is not True:
            errors.append(f"global gate {gate} missing or unverified")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="draft/CEFR-1000-APPROVED-MANIFEST.json")
    parser.add_argument("--evidence", default="draft/CEFR-1000-RELEASE-EVIDENCE.json")
    args = parser.parse_args()
    try:
        manifest = json.loads((ROOT / args.manifest).read_text(encoding="utf-8"))
        evidence = json.loads((ROOT / args.evidence).read_text(encoding="utf-8"))
        errors = audit(manifest, evidence)
    except (OSError, ValueError, TypeError) as exc:
        print(f"BLOCKED: evidence missing or malformed: {exc}", file=sys.stderr)
        return 1
    for issue in errors[:50]:
        print("BLOCKED:", issue, file=sys.stderr)
    if errors:
        print(f"BLOCKED: {len(errors)} unmet requirements; no release approval", file=sys.stderr)
        return 1
    print("Evidence schema checks passed; human provenance and live deployment must still be independently verified.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
