#!/usr/bin/env python3
"""Fail-closed CEFR-1000 editorial preflight. Structural checks are NOT approval."""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path

LEVELS = ("A1", "A2", "B1", "B2", "C1")
REVIEW_FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation")
REQUIRED = ("word", "level", "part_of_speech", "english_definition",
            "burmese_meaning", "example_sentence", "source_path",
            "source_index", "source_blob_sha")
def run(path, release=False):
    problems = []
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise ValueError("entries must be a list")
    counts = Counter()
    seen = set()
    global_headwords = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            problems.append(f"entry {index}: not an object")
            continue
        level = entry.get("level")
        if not isinstance(level, str) or level not in LEVELS:
            problems.append(f"entry {index}: invalid level {level!r}")
        else:
            counts[level] += 1
        for field in REQUIRED:
            value = entry.get(field)
            if field not in ("source_index",) and (not isinstance(value, str) or not value.strip()):
                problems.append(f"entry {index}: {field} must be nonempty text")
        if not isinstance(entry.get("word"), str) or not entry["word"].strip():
            problems.append(f"entry {index}: word must be nonempty text")
        if not isinstance(entry.get("part_of_speech"), str) or not entry["part_of_speech"].strip():
            problems.append(f"entry {index}: part_of_speech must be nonempty text")
        if type(entry.get("source_index")) is not int or entry["source_index"] < 0:
            problems.append(f"entry {index}: source_index must be a nonnegative integer")
        sha = entry.get("source_blob_sha")
        if not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdefABCDEF" for c in sha):
            problems.append(f"entry {index}: source_blob_sha must be a 40-character Git blob SHA")
        word = entry.get("word")
        if isinstance(word, str) and isinstance(level, str):
            key = (level, word.strip().casefold(), str(entry.get("part_of_speech", "")).strip().casefold())
            if key in seen:
                problems.append(f"entry {index}: duplicate level/headword/POS {key}")
            seen.add(key)
            canonical = word.strip().casefold()
            previous = global_headwords.get(canonical)
            if previous is not None:
                problems.append(f"entry {index}: headword {word!r} already allocated at entry {previous}; cross-level or same-level lexical duplication requires sense adjudication")
            else:
                global_headwords[canonical] = index
        if type(entry.get("editorial_hold")) is not bool:
            problems.append(f"entry {index}: editorial_hold must be an explicit boolean")
        if not release and entry.get("editorial_hold") is not True:
            problems.append(f"entry {index}: provisional entry must remain on editorial hold")
        if not release and (entry.get("release_approved") is True or any(entry.get(f) is True for f in REVIEW_FIELDS)):
            problems.append(f"entry {index}: provisional inventory cannot claim independent approval or completed review")
        for field in REVIEW_FIELDS + ("release_approved",):
            if type(entry.get(field)) is not bool:
                problems.append(f"entry {index}: {field} must be an explicit boolean")
        if release:
            if entry.get("editorial_hold") is not False:
                problems.append(f"entry {index}: editorial hold not cleared")
            if not all(entry.get(f) is True for f in REVIEW_FIELDS) or entry.get("release_approved") is not True:
                problems.append(f"entry {index}: independent review not complete")
            for field in ("source_english", "source_burmese", "source_level"):
                if not isinstance(entry.get(field), str) or not entry[field].strip():
                    problems.append(f"entry {index}: missing review source {field}")
    # a/an are pronunciation-conditioned variants of one indefinite article.
    # A human editor must resolve the lexical-unit count before release.
    if "a" in global_headwords and "an" in global_headwords:
        problems.append("lexical-unit conflict: a/an count as separate headwords; independent editorial adjudication required")
    for level in LEVELS:
        if counts[level] != 200:
            problems.append(f"{level}: expected 200 entries, found {counts[level]}")
    if len(entries) != 1000:
        problems.append(f"expected 1000 entries, found {len(entries)}")
    if data.get("counts_by_level") != {level: 200 for level in LEVELS}:
        problems.append("declared counts_by_level inconsistent")
    if release:
        if data.get("independently_approved_by_level") != {level: 200 for level in LEVELS}:
            problems.append("independent approvals not 200 per level")
        # A manifest alone can never prove independent identity, real listening,
        # physical iPhone QA, hosting or deployment. External signed evidence is
        # required; this script deliberately never reports release readiness.
        problems.append("release blocked: independently authenticated review, audio listening, physical iPhone, hosting and deployment evidence not verified")
    print(json.dumps({"mode": "release" if release else "structural",
                      "counts": {k: counts[k] for k in LEVELS},
                      "errors": len(problems), "details": problems[:60]},
                     ensure_ascii=False, indent=2))
    return 1 if problems else 0

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("manifest", nargs="?", default="draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    p.add_argument("--release", action="store_true", help="always fails closed without external evidence")
    a = p.parse_args()
    try:
        sys.exit(run(a.manifest, a.release))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"preflight failed closed: {exc}", file=sys.stderr)
        sys.exit(2)
