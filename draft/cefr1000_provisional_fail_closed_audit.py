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
        if level not in LEVELS:
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
        if not isinstance(entry.get("source_index"), int) or isinstance(entry.get("source_index"), bool):
            errors.append(f"entry {idx}: invalid source_index")
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
