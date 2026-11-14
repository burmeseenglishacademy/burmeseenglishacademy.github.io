#!/usr/bin/env python3
"""Read-only editorial triage for the approved CEFR-1000 *provisional* inventory.

Heuristics nominate human-review questions, never establish CEFR level,
lexical correctness, duplicate senses, or independent approval.
"""
import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("source_english", "source_burmese", "source_level")
REVIEW = ("reviewed_english", "reviewed_burmese", "reviewed_example",
          "reviewed_level", "reviewed_pronunciation", "release_approved")
def norm(word):
    return unicodedata.normalize("NFKC", word).casefold().strip()

def triage(data):
    entries = data.get("entries")
    if not isinstance(entries, list) or len(entries) != 1000:
        raise ValueError("Expected precisely 1000 provisional entries")
    by_level = defaultdict(list)
    for idx, row in enumerate(entries):
        if not isinstance(row, dict) or row.get("level") not in LEVELS:
            raise ValueError(f"Malformed level or entry at {idx}")
        by_level[row["level"]].append((idx, row))
        if row.get("editorial_hold") is not True or any(row.get(f) is not False for f in REVIEW):
            raise ValueError(f"Unexpected review/approval state at {idx}: stop triage")
    if any(len(by_level[level]) != 200 for level in LEVELS):
        raise ValueError("Exactly 200 entries per level required")
    occurrences = defaultdict(list)
    for level in LEVELS:
        for idx, row in by_level[level]:
            word = row.get("word")
            if not isinstance(word, str) or not word.strip():
                raise ValueError(f"Missing word at {idx}")
            occurrences[norm(word)].append((idx, level, row))
    risks = []
    def add(idx, row, code, question, related=None):
        risks.append({"index": idx, "level": row["level"], "word": row["word"],
                      "risk_code": code, "review_question": question,
                      "related_indices": related or [],
                      "source_path": row.get("source_path"),
                      "source_index": row.get("source_index"),
                      "source_blob_sha": row.get("source_blob_sha"),
                      "independent_review": "NOT_PERFORMED"})
    for level in LEVELS:
        for idx, row in by_level[level]:
            word = row["word"]
            if any(not isinstance(row.get(f), str) or not row[f].strip() for f in FIELDS):
                add(idx, row, "MISSING_EXTERNAL_EVIDENCE",
                    "Obtain dated, URL-backed exact-sense English/Myanmar/CEFR evidence; source path alone is not external verification.")
            if word == "i":
                add(idx, row, "ORTHOGRAPHY_CAPITALIZATION",
                    "Check canonical first-person pronoun I and preserve lowercase only in casefold matching.")
            if norm(word) in {"a", "an"}:
                add(idx, row, "ARTICLE_ALLOMORPH",
                    "Adjudicate whether a/an are one article sense occupying one slot; check following sound rather than letter.")
            if re.search(r"[^\w\s'-]", word, re.UNICODE):
                add(idx, row, "PUNCTUATION_OR_SYMBOL",
                    "Check whether punctuation is lexical, a noncanonical form, or a named-entity artefact.")
            if any(ch.isdigit() for ch in word):
                add(idx, row, "DIGIT_IN_HEADWORD",
                    "Verify this is a lexical headword, not an identifier or historical source artefact.")
            if word != word.strip() or "  " in word:
                add(idx, row, "WHITESPACE_NORMALIZATION",
                    "Normalize display text without silently changing lexical identity.")
    for key, items in occurrences.items():
        if len(items) > 1:
            for idx, level, row in items:
                add(idx, row, "NORMALIZED_HEADWORD_COLLISION",
                    "Compare POS, exact senses and levels; do not assume same spelling means same sense.",
                    [other_idx for other_idx, _, _ in items if other_idx != idx])
    return {"release_decision": "BLOCKED_STAGING_ONLY",
            "basis": "HEURISTIC_TRIAGE_NOT_INDEPENDENT_REVIEW",
            "scope": {level: len(by_level[level]) for level in LEVELS},
            "independently_approved": {level: 0 for level in LEVELS},
            "risk_counts": {code: sum(r["risk_code"] == code for r in risks)
                            for code in sorted({r["risk_code"] for r in risks})},
            "risks": risks}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    parser.add_argument("--output", help="Optional local JSON output; never writes inventory")
    args = parser.parse_args()
    result = triage(json.loads(Path(args.input).read_text(encoding="utf-8")))
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)

if __name__ == "__main__":
    main()
