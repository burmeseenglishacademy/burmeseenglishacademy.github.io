#!/usr/bin/env python3
"""Fail-closed CEFR-1000 inventory / approval gate. Staging only; no writes."""
import argparse
import json
import sys
import unicodedata
from collections import Counter
from pathlib import Path

LEVELS = ("A1", "A2", "B1", "B2", "C1")
REVIEW_FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation")
def normalized(word):
    return unicodedata.normalize("NFKC", word).casefold().strip()

def audit(path):
    errors = []
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("shortlist root must be an object")
    if type(obj.get("schema")) is not int or obj["schema"] != 1:
        errors.append("unsupported shortlist schema")
    if obj.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("provisional release_status missing or altered")
    for field, expected in (("scope_target", 200), ("counts_by_level", 200), ("independently_approved_by_level", 0)):
        metadata = obj.get(field)
        if not isinstance(metadata, dict) or set(metadata) != set(LEVELS):
            errors.append(f"{field}: must contain exactly A1, A2, B1, B2, C1")
        elif any(type(metadata[level]) is not int or metadata[level] != expected for level in LEVELS):
            errors.append(f"{field}: expected {expected} for every level")
    stages = obj.get("stages")
    if not isinstance(stages, dict) or stages.get("production") != "UNMODIFIED":
        errors.append("production preservation stage missing or altered")
    expected_stages = {
        "english_definitions": "FIRST_PASS_UNVERIFIED",
        "myanmar_meanings": "FIRST_PASS_UNVERIFIED",
        "original_examples": "FIRST_PASS_UNVERIFIED",
        "independent_source_evidence": "NOT_OBSERVED",
        "audio": "NOT_GENERATED_FOR_FINAL_SHORTLIST_NOT_LISTENED",
    }
    for field, expected in expected_stages.items():
        if not isinstance(stages, dict) or stages.get(field) != expected:
            errors.append(f"stage {field}: provisional gate missing or altered")
    entries = obj.get("entries")
    if not isinstance(entries, list):
        raise ValueError("entries must be a list")
    counts = Counter()
    seen = {}
    approved = Counter()
    for idx, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {idx}: not an object")
            continue
        level, word = entry.get("level"), entry.get("word")
        if not isinstance(level, str) or level not in LEVELS:
            errors.append(f"entry {idx}: invalid level {level!r}")
            continue
        counts[level] += 1
        if not isinstance(word, str) or not word.strip():
            errors.append(f"entry {idx}: missing word")
            continue
        key = normalized(word)
        if key in seen:
            errors.append(f"entry {idx}: duplicate normalized headword {word!r}, first at {seen[key]}; needs independent sense adjudication")
        else:
            seen[key] = idx
        for field in ("part_of_speech", "english_definition", "burmese_meaning", "example_sentence", "source_path", "source_blob_sha"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append(f"entry {idx}: missing {field}")
        source_path = entry.get("source_path")
        if isinstance(source_path, str) and source_path.strip():
            parts = source_path.replace(chr(92), "/").split("/")
            if (not source_path.startswith("draft/") or
                    any(part in ("", ".", "..") for part in parts) or
                    any(ord(char) < 32 or ord(char) == 127 for char in source_path)):
                errors.append(f"entry {idx}: unsafe source_path")
        for field in ("word", "english_definition", "burmese_meaning", "example_sentence"):
            value = entry.get(field)
            if isinstance(value, str) and any(
                    (ord(char) < 32 and char not in "\n\t") or ord(char) == 127
                    for char in value):
                errors.append(f"entry {idx}: control characters in {field}")
        sha = entry.get("source_blob_sha")
        if isinstance(sha, str) and (len(sha) != 40 or any(c not in "0123456789abcdefABCDEF" for c in sha)):
            errors.append(f"entry {idx}: invalid source_blob_sha")
        if type(entry.get("source_index")) is not int or entry["source_index"] < 0:
            errors.append(f"entry {idx}: invalid source_index")
        for field in (*REVIEW_FIELDS, "release_approved", "editorial_hold"):
            if type(entry.get(field)) is not bool:
                errors.append(f"entry {idx}: {field} must be an explicit JSON boolean")
        if entry.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            errors.append(f"entry {idx}: provisional status missing or altered")
        flags = [entry.get(k) is True for k in REVIEW_FIELDS]
        if entry.get("release_approved") is True:
            approved[level] += 1
            # A provisional boolean can NEVER establish independent approval.
            errors.append(f"entry {idx}: release_approved flag is insufficient without independently signed, digest-bound evidence")
        if any(flags):
            errors.append(f"entry {idx}: bare review flag(s) cannot establish independent signoff")
        if entry.get("editorial_hold") is not True:
            errors.append(f"entry {idx}: editorial hold removed from provisional source")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: expected 200 entries, found {counts[level]}")
    if len(entries) != 1000:
        errors.append(f"expected 1000 entries, found {len(entries)}")
    print("Provisional written counts: " + ", ".join(f"{k}={counts[k]}" for k in LEVELS))
    print("Independently verified approvals: UNPROVEN (bare flags never count)")
    print("Audio listening, physical iPhone, current-SHA CI, hosting and deployment: UNVERIFIED")
    print(f"Structural findings: {len(errors)}")
    for item in errors[:100]:
        print("BLOCK:", item)
    if len(errors) > 100:
        print(f"... {len(errors)-100} further findings")
    print("RELEASE BLOCKED: provisional inventory is not an approved release manifest")
    return 1

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("shortlist", nargs="?", default="draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    args = p.parse_args()
    try:
        sys.exit(audit(args.shortlist))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("RELEASE BLOCKED:", exc, file=sys.stderr)
        sys.exit(2)
