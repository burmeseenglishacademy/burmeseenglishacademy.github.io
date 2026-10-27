#!/usr/bin/env python3
"""Fail-closed structural audit of 27 directly observed Oxford 3000/5000 word/POS lines.

This is evidence-integrity checking only, NOT independent sense, English, Myanmar,
example, CEFR, pronunciation or real-device signoff. Never deploy from this script.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-SECOND-DIRECT-PDF-BATCH-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
RANK = {v: i for i, v in enumerate(LEVELS)}
STATUS = "DIRECT_OXFORD_3000_5000_SOURCE_TRIAGE_STAGING_HOLD_NO_RELEASE"
ROW_STATUS = "DIRECT_PDF_WORD_POS_TRIAGE_ONLY_NOT_APPROVED"
URL_PREFIX = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/"
URLS = {
    "3000": URL_PREFIX + "The_Oxford_3000_by_CEFR_level.pdf",
    "5000": URL_PREFIX + "The_Oxford_5000_by_CEFR_level.pdf",
}
# Frozen direct observations: word -> (edition, publisher level, POS, 1-based page, 0-based PDF extracted line).
# This only pins what was observed; the validator does not independently fetch the PDF.
OBSERVED = {
    "world": ("3000", "A1", "noun", 4, 893),
    "company": ("3000", "A1", "noun", 1, 165),
    "job": ("3000", "A1", "noun", 2, 410),
    "future": ("3000", "A1", "noun", 2, 322),
    "group": ("3000", "A1", "noun", 2, 340),
    "life": ("3000", "A1", "noun", 2, 439),
    "machine": ("3000", "A1", "noun", 2, 457),
    "trip": ("3000", "A1", "noun", 4, 820),
    "advice": ("3000", "A1", "noun", 1, 15),
    "explain": ("3000", "A1", "verb", 2, 261),
    "grow": ("3000", "A1", "verb", 2, 341),
    "rich": ("3000", "A1", "adjective", 3, 653),
    "prepare": ("3000", "A1", "verb", 3, 618),
    "print": ("3000", "B2", "noun", 12, 3092),
    "hide": ("3000", "A2", "verb", 5, 1275),
    "anniversary": ("3000", "B2", "noun", 10, 2622),
    "asset": ("5000", "B2", "noun", 1, 37),
    "racism": ("5000", "B2", "noun", 2, 503),
    "consistently": ("5000", "B2", "adverb", 1, 121),
    "diverse": ("5000", "B2", "adjective", 1, 185),
    "evaluation": ("5000", "B2", "noun", 1, 222),
    "interpretation": ("5000", "B2", "noun", 2, 348),
    "neutral": ("5000", "B2", "adjective", 2, 419),
    "terrorism": ("5000", "B2", "noun", 3, 633),
    "controversial": ("5000", "B2", "adjective", 1, 127),
    "dominant": ("5000", "B2", "adjective", 1, 188),
    "integrity": ("5000", "C1", "noun", 5, 1355),
}
EXPECTED_COUNTS = {"A1": 0, "A2": 6, "B1": 6, "B2": 4, "C1": 11}
DRAFT_FIELDS = {
    "shortlist_level": "level",
    "shortlist_pos": "part_of_speech",
    "shortlist_english_definition": "english_definition",
    "shortlist_myanmar_meaning": "burmese_meaning",
    "shortlist_example": "example_sentence",
}


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def validate(packet, shortlist, raw_shortlist, level="ALL"):
    errors = []
    rows = packet.get("records", [])
    entries = shortlist.get("entries", [])
    originals = {r.get("word"): r for r in entries}
    if packet.get("schema") != 1 or packet.get("status") != STATUS:
        errors.append("staging-only source packet status/schema altered")
    if packet.get("observed_on") != "2026-10-27" or packet.get("source_urls") != URLS:
        errors.append("publisher provenance/date altered")
    if packet.get("shortlist_blob_sha") != git_blob_sha(raw_shortlist):
        errors.append("shortlist source blob changed: observations require reinspection")
    if len(entries) != 1000 or {k: sum(x.get("level") == k for x in entries) for k in LEVELS} != dict.fromkeys(LEVELS, 200):
        errors.append("provisional 200-per-level source no longer matches approved scope")
    if len(rows) != 27 or packet.get("record_count") != 27:
        errors.append("direct observations must remain exactly 27")
    if len({r.get("word") for r in rows}) != len(rows) or {r.get("word") for r in rows} != set(OBSERVED):
        errors.append("observed word set duplicate, added or missing")
    counts = {k: sum(r.get("shortlist_level") == k for r in rows) for k in LEVELS}
    if counts != EXPECTED_COUNTS or packet.get("per_shortlist_level") != EXPECTED_COUNTS:
        errors.append("per-level source observation counts changed")
    if packet.get("independently_approved_count") != 0:
        errors.append("unsupported independent approval aggregate")
    if packet.get("word_pos_level_discrepancy_count") != sum(r.get("word_pos_level_match") is False for r in rows):
        errors.append("source discrepancy aggregate inaccurate")
    for r in rows:
        word = r.get("word")
        if word not in OBSERVED:
            continue
        original = originals.get(word)
        if not original:
            errors.append(f"{word}: missing original")
            continue
        edition, src_level, src_pos, page, line = OBSERVED[word]
        expected = {
            "source_title": f"The Oxford {edition} by CEFR level",
            "source_url": URLS[edition],
            "source_publisher": "Oxford University Press",
            "source_observed_on": "2026-10-27",
            "source_pdf_page": page,
            "source_extracted_line": line,
            "source_listed_pos": src_pos,
            "source_listed_level": src_level,
            "level_distance": RANK[original["level"]] - RANK[src_level],
            "word_pos_level_match": original["level"] == src_level,
        }
        for k, v in expected.items():
            if r.get(k) != v:
                errors.append(f"{word}: publisher observation {k} drift")
        for packet_field, shortlist_field in DRAFT_FIELDS.items():
            if r.get(packet_field) != original.get(shortlist_field):
                errors.append(f"{word}: source draft {packet_field} drift")
        if not r.get("editorial_review_issue") or not r.get("source_access") or not r.get("source_scope"):
            errors.append(f"{word}: incomplete provenance or editorial issue")
        for field in ("independent_english_review", "independent_myanmar_review",
                      "independent_example_review", "independent_cefr_sense_review",
                      "release_approved"):
            if r.get(field) is not False:
                errors.append(f"{word}: unsupported approval field {field}")
        if (r.get("independent_reviewer_receipt") is not None
                or r.get("editorial_hold") is not True
                or r.get("status") != ROW_STATUS
                or original.get("editorial_hold") is not True
                or original.get("release_approved") is not False):
            errors.append(f"{word}: editorial hold or independent receipt tampered")
    selected = [r for r in rows if level == "ALL" or r.get("shortlist_level") == level]
    report = {
        "level": level,
        "observed_on": packet.get("observed_on"),
        "publisher_pdf_word_pos_observations": len(selected),
        "publisher_level_discrepancies": sum(r.get("word_pos_level_match") is False for r in selected),
        "independently_approved": 0,
        "status": "STAGING_HOLD_NOT_SENSE_VERIFIED_NOT_RELEASE_READY",
        "errors": errors,
    }
    return errors, report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text("utf-8"))
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    errors, report = validate(packet, shortlist, raw, args.level)
    if args.self_test:
        changes = [
            lambda p: p["records"][0].update({"independent_english_review": True}),
            lambda p: p["records"][0].update({"source_extracted_line": 9999}),
            lambda p: p["records"][0].update({"source_listed_level": "C1"}),
            lambda p: p["records"][0].update({"source_url": "https://example.invalid"}),
            lambda p: p["records"].append(copy.deepcopy(p["records"][0])),
            lambda p: p.update({"independently_approved_count": 1}),
        ]
        for i, change in enumerate(changes):
            altered = copy.deepcopy(packet)
            change(altered)
            if not validate(altered, shortlist, raw, "ALL")[0]:
                errors.append(f"negative test {i} accepted forged source/review evidence")
        report["negative_tests"] = "PASS" if not errors else "FAIL"
    report["errors"] = errors
    out = ROOT / f"cefr-1000-oxford-second-batch-{args.level}.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\\n", "utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
