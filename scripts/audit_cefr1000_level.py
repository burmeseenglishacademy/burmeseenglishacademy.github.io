#!/usr/bin/env python3
"""Staging-only CEFR-1000 per-level structural audit. Never grants release approval."""
import argparse
import json
import pathlib
import sys
import unicodedata
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def check_level(data, level):
    errors = []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries must be an array"]
    selected = [e for e in entries if isinstance(e, dict) and e.get("level") == level]
    if len(selected) != 200:
        errors.append(f"{level}: expected 200, found {len(selected)}")
    seen = set()
    for idx, e in enumerate(selected):
        word = e.get("word")
        if not isinstance(word, str) or not word.strip():
            errors.append(f"{level} item {idx}: missing headword")
            continue
        key = unicodedata.normalize("NFKC", word).casefold().strip()
        if key in seen:
            errors.append(f"{level}: duplicate headword {word!r}")
        seen.add(key)
        for field in ("english_definition", "burmese_meaning", "example_sentence",
                      "part_of_speech", "source_path", "source_blob_sha"):
            if not isinstance(e.get(field), str) or not e[field].strip():
                errors.append(f"{level} {word!r}: missing {field}")
        if e.get("editorial_hold") is not True or e.get("release_approved") is not False:
            errors.append(f"{level} {word!r}: provisional hold violated")
        for field in ("reviewed_english", "reviewed_burmese", "reviewed_example",
                      "reviewed_level", "reviewed_pronunciation"):
            if e.get(field) is not False:
                errors.append(f"{level} {word!r}: {field} must be false")
    if data.get("independently_approved_by_level", {}).get(level) != 0:
        errors.append(f"{level}: independent approvals must remain zero")
    if data.get("counts_by_level", {}).get(level) != 200:
        errors.append(f"{level}: declared count must be 200")
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("release status must remain provisional")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", required=True, choices=LEVELS)
    args = parser.parse_args()
    try:
        data = json.loads(SHORTLIST.read_text(encoding="utf-8"))
        errors = check_level(data, args.level)
    except (OSError, ValueError, TypeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    if errors:
        return 1
    print(f"PASS: {args.level} provisional structural checks only; NOT independently reviewed or release-ready")
    return 0

if __name__ == "__main__":
    sys.exit(main())
