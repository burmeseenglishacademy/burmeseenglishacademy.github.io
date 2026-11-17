#!/usr/bin/env python3
"""CEFR-1000 production release preflight. Fail closed; never deploys.

Separate from provisional intake checks. A structurally valid shortlist is NOT
an approved release manifest. Evidence must be external to the intake files.
"""
import argparse
import collections
import json
from pathlib import Path
import sys

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("english", "myanmar", "example", "exact_sense_cefr", "pronunciation")
VOICES = ("george", "emma")
KINDS = ("headword", "example")

def audit(root):
    errors = []
    manifest_path = root / "release/cefr1000-approved-manifest.json"
    evidence_path = root / "release/cefr1000-independent-evidence.json"
    qa_path = root / "release/cefr1000-release-qa.json"
    for path in (manifest_path, evidence_path, qa_path):
        if not path.is_file():
            errors.append(f"missing independent release artifact: {path.relative_to(root)}")
    if errors:
        return errors
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"invalid release evidence: {exc}"]
    entries = manifest.get("entries")
    reviews = evidence.get("reviews")
    if not isinstance(entries, list) or not isinstance(reviews, list):
        return ["manifest entries and independent reviews must be arrays"]
    if len(entries) != 1000 or len(reviews) != 1000:
        errors.append("exactly 1000 manifest entries and 1000 independent reviews required")
    counts = collections.Counter()
    keys = set()
    review_by_id = {}
    for r in reviews:
        if not isinstance(r, dict) or not isinstance(r.get("entry_id"), str):
            errors.append("invalid independent review record")
            continue
        if r["entry_id"] in review_by_id:
            errors.append(f"duplicate review: {r['entry_id']}")
        review_by_id[r["entry_id"]] = r
    for i, e in enumerate(entries):
        if not isinstance(e, dict):
            errors.append(f"entry {i}: not an object")
            continue
        level, word, pos, sense = (e.get(k) for k in ("level", "word", "part_of_speech", "sense_id"))
        counts[level] += 1
        key = tuple(str(v).casefold().strip() for v in (word, pos, sense))
        if not all(key) or key in keys:
            errors.append(f"entry {i}: missing or duplicate word/POS/sense")
        keys.add(key)
        entry_id = e.get("entry_id")
        if not isinstance(entry_id, str) or not entry_id.strip():
            errors.append(f"entry {i}: missing stable entry_id")
            continue
        r = review_by_id.get(entry_id)
        if not r:
            errors.append(f"entry {i}: independent review missing")
            continue
        for field in FIELDS:
            check = r.get(field)
            if not isinstance(check, dict) or check.get("decision") != "approved" or not all(
                isinstance(check.get(k), str) and check[k].strip()
                for k in ("reviewer_id", "signed_at", "source_url", "observed_on")
            ):
                errors.append(f"{entry_id}: {field} independent evidence/signoff missing")
        audio = e.get("audio")
        for voice in VOICES:
            for kind in KINDS:
                record = audio.get(voice, {}).get(kind) if isinstance(audio, dict) else None
                if not isinstance(record, dict) or not all(
                    isinstance(record.get(k), str) and record[k].strip()
                    for k in ("asset_path", "sha256", "listened_by", "listened_at")
                ):
                    errors.append(f"{entry_id}: {voice} {kind} audio/listening evidence missing")
    if counts != collections.Counter({level: 200 for level in LEVELS}):
        errors.append(f"incorrect level counts: {dict(counts)}")
    if len(review_by_id) != len(entries):
        errors.append("review ID set does not match manifest entries")
    for gate in ("desktop_browser", "mobile_browser", "physical_iphone_safari",
                 "github_pages_limits", "production_deployment", "production_assets_preserved",
                 "privacy_protection"):
        record = qa.get(gate)
        if not isinstance(record, dict) or record.get("passed") is not True or not all(
            isinstance(record.get(k), str) and record[k].strip()
            for k in ("evidence_url", "verified_by", "verified_at")
        ):
            errors.append(f"release QA gate not evidenced: {gate}")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = audit(args.root.resolve())
    except (OSError, ValueError, TypeError) as exc:
        errors = [f"unreadable release evidence: {exc}"]
    if errors:
        for error in errors[:35]:
            print("RELEASE BLOCKED:", error, file=sys.stderr)
        print(f"RELEASE BLOCKED: {len(errors)} failed gate(s); no deployment performed", file=sys.stderr)
        return 1
    print("Preflight evidence schema passed; independently verify authenticity before any deployment.")
    print("No deployment performed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
