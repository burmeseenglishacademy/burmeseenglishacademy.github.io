#!/usr/bin/env python3
"""Conservative CEFR-1000 editorial triage; never grants approval or changes source."""
import argparse
import json
import pathlib
import re
import unicodedata
from collections import Counter, defaultdict

LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {level: 200 for level in LEVELS}

def normalize(value):
    return unicodedata.normalize("NFKC", value).casefold().strip()

def audit(data):
    errors, warnings = [], []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"], []
    if len(entries) != 1000:
        errors.append(f"expected 1000 records, found {len(entries)}")
    counts = Counter()
    headwords = defaultdict(list)
    senses = defaultdict(list)
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {index}: not an object")
            continue
        level = entry.get("level")
        if level not in LEVELS:
            errors.append(f"entry {index}: invalid level {level!r}")
        else:
            counts[level] += 1
        word, pos, definition = (entry.get(k) for k in ("word", "part_of_speech", "english_definition"))
        for field in ("word", "part_of_speech", "english_definition", "burmese_meaning", "example_sentence"):
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"entry {index}: empty or invalid {field}")
        if not all(isinstance(x, str) and x.strip() for x in (word, pos, definition)):
            continue
        key = normalize(word)
        headwords[key].append((index, level, word))
        senses[(key, normalize(pos), normalize(definition))].append((index, level))
        if word != word.strip():
            warnings.append(f"entry {index}: headword has surrounding whitespace")
        if word == "i":
            warnings.append(f"entry {index}: English first-person pronoun must be capitalised I")
        if re.search(r"\b(?:wordnet|wikidata|wikipedia)\b", str(entry.get("source_path", "")), re.I):
            warnings.append(f"entry {index}: historical lexical source needs independent CEFR evidence")
        if entry.get("release_approved") is not False or entry.get("editorial_hold") is not True:
            errors.append(f"entry {index}: provisional hold/approval invariant violated")
        for flag in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation"):
            if entry.get(flag) is not False:
                errors.append(f"entry {index}: {flag} must remain false in provisional shortlist")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: expected 200 entries, found {counts[level]}")
    for key, records in headwords.items():
        if len(records) > 1:
            errors.append(f"duplicate normalised headword {key!r}: {records}")
    for key, records in senses.items():
        if len(records) > 1:
            errors.append(f"duplicate exact normalised sense {key!r}: {records}")
    if data.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        errors.append("provisional shortlist claims independent approval")
    if data.get("counts_by_level") != EXPECTED:
        errors.append("declared level counts mismatch")
    return errors, warnings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shortlist", default="draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    args = parser.parse_args()
    data = json.loads(pathlib.Path(args.shortlist).read_text(encoding="utf-8"))
    errors, warnings = audit(data)
    for item in warnings:
        print("EDITORIAL WARNING:", item)
    for item in errors:
        print("BLOCK:", item)
    print(f"Provisional triage: {len(errors)} structural blocks; {len(warnings)} editorial warnings; independent approvals NOT assessed")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
