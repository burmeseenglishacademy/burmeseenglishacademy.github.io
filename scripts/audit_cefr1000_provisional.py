#!/usr/bin/env python3
"""Fail-closed provisional CEFR-1000 audit; NEVER grants editorial approval.

Run: python3 scripts/audit_cefr1000_provisional.py
Exit 0 means the *provisional inventory* has expected structure and remains held.
It does NOT mean release-ready. The release manifest must use separate gates.
"""
import json
import pathlib
import sys
import unicodedata
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("word", "level", "part_of_speech", "english_definition",
          "burmese_meaning", "example_sentence", "source_path",
          "source_index", "source_blob_sha")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")

def audit(data):
    errors = []
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("provisional release status changed: inspect manually")
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries is not an array"], {}
    if len(entries) != 1000:
        errors.append(f"expected 1000 provisional entries, found {len(entries)}")
    counts = Counter()
    seen = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {index} not an object")
            continue
        level = entry.get("level")
        counts[level] += 1
        for field in FIELDS:
            value = entry.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                errors.append(f"entry {index} missing {field}")
        word = entry.get("word")
        if isinstance(word, str) and word.strip():
            key = unicodedata.normalize("NFKC", word).casefold().strip()
            if key in seen:
                errors.append(f"duplicate headword {word!r} at {seen[key]} and {index}; inspect senses")
            else:
                seen[key] = index
        if entry.get("editorial_hold") is not True:
            errors.append(f"entry {index} not explicitly on editorial hold")
        for flag in FLAGS:
            if entry.get(flag) is not False:
                errors.append(f"entry {index} {flag} is not explicitly false")
        if entry.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            errors.append(f"entry {index} status changed")
        source_index = entry.get("source_index")
        if not isinstance(source_index, int) or isinstance(source_index, bool) or source_index < 0:
            errors.append(f"entry {index} invalid source_index")
        sha = entry.get("source_blob_sha")
        if not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha.lower()):
            errors.append(f"entry {index} invalid provenance SHA")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: expected 200, found {counts[level]}")
        if data.get("counts_by_level", {}).get(level) != counts[level]:
            errors.append(f"{level}: declared count differs from entries")
        if data.get("independently_approved_by_level", {}).get(level) != 0:
            errors.append(f"{level}: provisional independent approval count must be zero")
    if set(counts) != set(LEVELS):
        errors.append(f"unexpected level(s): {sorted(map(str, set(counts) - set(LEVELS)))}")
    if data.get("scope_target") != {level: 200 for level in LEVELS}:
        errors.append("scope target changed")
    return errors, {level: counts[level] for level in LEVELS}

def main():
    try:
        data = json.loads(PATH.read_text(encoding="utf-8"))
        errors, counts = audit(data)
    except (OSError, ValueError, TypeError) as exc:
        print(f"FAIL: unable to audit provisional inventory: {exc}", file=sys.stderr)
        return 1
    print("Provisional counts:", counts)
    if errors:
        for error in errors[:100]:
            print("FAIL:", error, file=sys.stderr)
        print(f"{len(errors)} total errors", file=sys.stderr)
        return 1
    print("PASS: provisional structure and editorial holds only; NOT release approval")
    return 0

if __name__ == "__main__":
    sys.exit(main())
