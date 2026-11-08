#!/usr/bin/env python3
"""Staging-only CEFR-1000 structural checks; no editorial approval is inferred."""
import argparse, collections, json, pathlib, sys

LEVELS = ("A1", "A2", "B1", "B2", "C1")
ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
REVIEW_FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation", "release_approved")
SOURCE_FIELDS = ("source_english", "source_burmese", "source_level")

def check(level, release):
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    entries = data["entries"]
    errors = []
    if data.get("scope_target") != {k: 200 for k in LEVELS}:
        errors.append("scope_target is not 200 for every CEFR level")
    if len(entries) != 1000:
        errors.append(f"expected 1000 entries, got {len(entries)}")
    counts = collections.Counter(e.get("level") for e in entries)
    for k in LEVELS:
        if counts[k] != 200:
            errors.append(f"{k}: expected 200, got {counts[k]}")
    if set(counts) != set(LEVELS):
        errors.append("unknown CEFR levels present")
    if data.get("counts_by_level") != {k: counts[k] for k in LEVELS}:
        errors.append("declared counts_by_level does not match inventory")
    selected = [(i, e) for i, e in enumerate(entries) if e.get("level") == level]
    seen = set()
    for i, e in selected:
        word = e.get("word")
        if not isinstance(word, str) or not word.strip():
            errors.append(f"entry {i}: missing headword")
            continue
        identity = (word.casefold().strip(), str(e.get("part_of_speech", "")).casefold().strip())
        if identity in seen:
            errors.append(f"entry {i}: repeated headword/POS {identity}")
        seen.add(identity)
        for field in ("english_definition", "burmese_meaning", "example_sentence", "source_path", "source_blob_sha"):
            if not isinstance(e.get(field), str) or not e[field].strip():
                errors.append(f"entry {i}: missing {field}")
        if not isinstance(e.get("source_index"), int) or e["source_index"] < 0:
            errors.append(f"entry {i}: invalid source_index")
        if release:
            if e.get("editorial_hold") is not False or any(e.get(k) is not True for k in REVIEW_FIELDS):
                errors.append(f"entry {i}: independent editorial signoff incomplete")
            for field in SOURCE_FIELDS:
                if not isinstance(e.get(field), str) or not e[field].strip():
                    errors.append(f"entry {i}: missing source-backed {field}")
    if release:
        # External evidence must be checked separately: this script cannot verify
        # independent reviewer identity, real listening, physical iPhone or deployment.
        errors.append("release blocked: external independent review, audio listening, device, hosting and deployment attestations not machine-verified")
    return errors, len(selected)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--level", required=True, choices=LEVELS)
    p.add_argument("--release", action="store_true", help="Fail closed until external evidence gates are implemented")
    a = p.parse_args()
    errors, count = check(a.level, a.release)
    print(f"{a.level}: {count} provisional entries; mode={'release' if a.release else 'structural'}; errors={len(errors)}")
    for error in errors[:50]:
        print("ERROR:", error, file=sys.stderr)
    if len(errors) > 50:
        print(f"... {len(errors)-50} additional errors", file=sys.stderr)
    sys.exit(1 if errors else 0)
