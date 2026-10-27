#!/usr/bin/env python3
"""Validate direct publisher-PDF spotcheck provenance and provisional hold integrity.

This is deterministic data-integrity QA, NOT independent lexical/CEFR/Burmese
approval. An official Oxford word/POS/level listing is not an exact-sense proof.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPOT = ROOT / "draft/CEFR-1000-OXFORD-DIRECT-PDF-SPOTCHECK-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
URL = ("https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/"
       "oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
LEVELS = ("A1", "A2", "B1", "B2", "C1")
INDEX = {level: i for i, level in enumerate(LEVELS)}
STATUS = "OFFICIAL_PUBLISHER_PDF_SPOTCHECK_NOT_INDEPENDENT_REVIEW_DO_NOT_PUBLISH"


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def validate(document, shortlist, raw_shortlist, level="ALL"):
    errors = []
    rows = document.get("records", [])
    selected = [r for r in rows if level == "ALL" or r.get("shortlist_level") == level]
    originals = {r.get("word"): r for r in shortlist.get("entries", [])}
    if document.get("status") != STATUS or document.get("source_url") != URL:
        errors.append("official source provenance or staging-only status missing")
    if document.get("observed_on") != "2026-10-27":
        errors.append("source observation date altered without a new direct review")
    if document.get("shortlist_source_blob_sha") != blob_sha(raw_shortlist):
        errors.append("source shortlist changed; direct spotcheck must be rechecked")
    if len(rows) != 23 or document.get("record_count") != len(rows):
        errors.append("expected exactly 23 directly observed source records")
    if len({r.get("word") for r in rows}) != len(rows):
        errors.append("duplicate direct source headword")
    if document.get("level_mismatch_count") != sum(
        r.get("shortlist_level") != r.get("official_oxford3000_level") for r in rows
    ):
        errors.append("level mismatch aggregate inaccurate")
    if len(shortlist.get("entries", [])) != 1000:
        errors.append("shortlist must retain exactly 1000 entries")
    for row in selected:
        word = row.get("word")
        src = originals.get(word)
        if src is None:
            errors.append(f"{word}: not in shortlist")
            continue
        for from_key, to_key in (
            ("shortlist_level", "level"),
            ("shortlist_part_of_speech", "part_of_speech"),
            ("shortlist_definition", "english_definition"),
            ("shortlist_burmese", "burmese_meaning"),
            ("shortlist_example", "example_sentence"),
        ):
            if row.get(from_key) != src.get(to_key):
                errors.append(f"{word}: {from_key} drift from source shortlist")
        if row.get("shortlist_level") not in INDEX or row.get("official_oxford3000_level") not in INDEX:
            errors.append(f"{word}: unknown CEFR level")
            continue
        if row.get("level_difference") != (
            INDEX[row["shortlist_level"]] - INDEX[row["official_oxford3000_level"]]
        ):
            errors.append(f"{word}: incorrect CEFR distance")
        if row.get("word_and_pos_level_match") is not (
            row["shortlist_level"] == row["official_oxford3000_level"]
        ):
            errors.append(f"{word}: incorrect matching classification")
        if row.get("official_pdf_page", 0) < 1 or row.get("official_pdf_extracted_line", -1) < 0:
            errors.append(f"{word}: missing PDF page/line evidence")
        if not row.get("official_oxford3000_pos") or not row.get("editorial_issue"):
            errors.append(f"{word}: missing POS or editorial review task")
        if (row.get("exact_sense_checked_by_independent_reviewer") is not False
                or row.get("myanmar_meaning_independently_verified") is not False
                or row.get("example_independently_verified") is not False
                or row.get("independent_review_receipt") is not None
                or row.get("review_status") != "EDITORIAL_HOLD_SOURCE_SPOTCHECK_ONLY"):
            errors.append(f"{word}: unsupported independent approval claim")
        if src.get("editorial_hold") is not True or src.get("release_approved") is not False:
            errors.append(f"{word}: source shortlist editorial hold was bypassed")
    return errors, {
        "level": level, "source": URL, "observation_date": document.get("observed_on"),
        "direct_official_pdf_spotchecks": len(selected),
        "level_mismatch_candidates": sum(
            r.get("shortlist_level") != r.get("official_oxford3000_level") for r in selected
        ),
        "independent_approvals": 0,
        "status": "STAGING_HOLD_NO_PUBLICATION",
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    document = json.loads(SPOT.read_text("utf-8"))
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    errors, result = validate(document, shortlist, raw, args.level)
    if args.self_test:
        tampered = copy.deepcopy(document)
        tampered["records"][0]["exact_sense_checked_by_independent_reviewer"] = True
        if not validate(tampered, shortlist, raw, "ALL")[0]:
            errors.append("self-test failed to reject fake independent review")
        tampered = copy.deepcopy(document)
        tampered["records"][0]["shortlist_level"] = "C1"
        if not validate(tampered, shortlist, raw, "ALL")[0]:
            errors.append("self-test failed to reject level tampering")
        tampered = copy.deepcopy(document)
        tampered["source_url"] = "https://example.invalid"
        if not validate(tampered, shortlist, raw, "ALL")[0]:
            errors.append("self-test failed to reject provenance tampering")
        result["negative_tests"] = "PASS" if not errors else "FAIL"
    result["errors"] = errors
    output = ROOT / f"cefr-1000-oxford-direct-spotcheck-{args.level}.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\\n", "utf-8")
    print(json.dumps(result, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
