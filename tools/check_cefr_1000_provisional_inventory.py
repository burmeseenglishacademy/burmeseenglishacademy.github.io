#!/usr/bin/env python3
"""Fail-closed CEFR-1000 provisional inventory guard; never grants release approval.

Usage: python3 tools/check_cefr_1000_provisional_inventory.py
This guard deliberately checks draft integrity only, NOT independent signoff.
"""
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("word", "level", "part_of_speech", "english_definition",
          "burmese_meaning", "example_sentence", "source_path",
          "source_index", "source_blob_sha")
REVIEW_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                "reviewed_level", "reviewed_pronunciation", "release_approved")

def check(data):
    errors = []
    if not isinstance(data, dict):
        return ["Root must be an object"]
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"]
    if len(entries) != 1000:
        errors.append(f"Expected 1000 entries, got {len(entries)}")
    counts = Counter()
    seen = {}
    for index, entry in enumerate(entries):
        label = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: not an object")
            continue
        for field in FIELDS:
            value = entry.get(field)
            if isinstance(value, str):
                if not value.strip():
                    errors.append(f"{label}: empty {field}")
            elif field == "source_index" and type(value) is int and value >= 0:
                pass
            else:
                errors.append(f"{label}: invalid/missing {field}")
        level = entry.get("level")
        if level not in LEVELS:
            errors.append(f"{label}: invalid level {level!r}")
        else:
            counts[level] += 1
        word = entry.get("word")
        if isinstance(word, str):
            normalized = " ".join(word.casefold().split())
            if normalized in seen:
                errors.append(f"{label}: duplicate headword {word!r} also at {seen[normalized]}")
            seen[normalized] = index
        if entry.get("editorial_hold") is not True:
            errors.append(f"{label}: provisional entry must remain on editorial hold")
        for flag in REVIEW_FLAGS:
            if entry.get(flag) is not False:
                errors.append(f"{label}: {flag} must be explicitly false in provisional inventory")
        sha = entry.get("source_blob_sha")
        if not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            errors.append(f"{label}: invalid historical blob SHA")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: expected 200, got {counts[level]}")
        if data.get("counts_by_level", {}).get(level) != 200:
            errors.append(f"{level}: declared count not 200")
        if data.get("independently_approved_by_level", {}).get(level) != 0:
            errors.append(f"{level}: provisional independent approvals must remain zero")
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("Provisional release_status altered")
    if data.get("stages", {}).get("production") != "UNMODIFIED":
        errors.append("Provisional production status altered")
    return errors

def main():
    try:
        data = json.loads(PATH.read_text(encoding="utf-8"))
        errors = check(data)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors = [f"Unable to read inventory: {exc}"]
    for error in errors:
        print("FAIL:", error)
    if errors:
        print(f"BLOCKED: {len(errors)} inventory integrity failure(s); no release permission")
        return 1
    print("PASS: provisional 1000 inventory structure and zero-approval hold only.")
    print("RELEASE BLOCKED: independent review, audio listening, iPhone and deployment not verified.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
