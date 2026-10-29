#!/usr/bin/env python3
"""Fail-closed audit for twelve additional official Oxford B1-draft word/POS observations.

Publisher word/POS lists are not exact-sense CEFR, English/Myanmar, original-example,
independent-human or listening approval. Staging only; never writes production.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-SIXTH-TWELVE-2026-10-29.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = (
    ("flight", "A1", 2, 297, "flight n."),
    ("primary", "B1", 9, 2320, "primary adj."),
    ("activity", "A1", 1, 9, "activity n."),
    ("application", "B1", 7, 1821, "application n."),
    ("complex", "B1", 7, 1919, "complex adj."),
    ("condition", "A2", 4, 1072, "condition n."),
    ("freedom", "B2", 11, 2877, "freedom n."),
    ("interview", "A1", 2, 401, "interview n., v."),
    ("location", "B1", 8, 2197, "location n."),
    ("accept", "A2", 4, 912, "accept v."),
    ("attempt", "B2", 10, 2645, "attempt n., v."),
    ("distance", "A2", 5, 1137, "distance n."),
)
PRIOR = (
    "B1-TWELVE-DIRECT-PDF-2026-10-28",
    "B1-LOWER-LEVEL-TWELVE-2026-10-28",
    "B1-MIXED-TWELVE-2026-10-28",
    "B1-FOURTH-TWENTYFOUR-2026-10-29",
    "B1-FIFTH-TWELVE-2026-10-29",
)

def need(condition, why):
    if not condition:
        raise ValueError(why)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()
    need(sha == SHORT_SHA, "Frozen shortlist blob drift")
    need(shortlist["counts_by_level"] == {x: 200 for x in LEVELS}
         and shortlist["independently_approved_by_level"] == {x: 0 for x in LEVELS}
         and len(shortlist["entries"]) == 1000, "Scope or independent approvals changed")
    need(packet["schema"] == 1 and packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet["status"] == "B1_SIXTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet["observed_on"] == "2026-10-29"
         and packet["shortlist_blob_sha"] == SHORT_SHA, "Packet scope/source changed")
    need(packet["record_count"] == len(packet["records"]) == 12
         and packet["counts_by_level"] == {"A1":0,"A2":0,"B1":12,"B2":0,"C1":0}
         and packet["publisher_reference_level_counts"] == {"A1":3,"A2":3,"B1":4,"B2":2,"C1":0}
         and packet["word_pos_discrepancies"] == 8
         and packet["independently_approved_count"] == 0, "Counts or approval drift")
    by_word = {r["word"]: r for r in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist headword")
    words = [x[0] for x in EXPECTED]
    need(len(set(words)) == 12, "Repeated expected headword")
    for suffix in PRIOR:
        older = json.loads((ROOT / ("draft/CEFR-1000-OXFORD-" + suffix + ".json")).read_text("utf8"))
        need(not set(words).intersection(r["word"] for r in older["records"]),
             "New source packet repeats earlier B1 observation")
    for row, (word, source_level, page, line, excerpt) in zip(packet["records"], EXPECTED):
        need(row["word"] == word, "Headword or row order changed")
        source = by_word[word]
        need(row["level"] == source["level"] == "B1"
             and row["part_of_speech"] == source["part_of_speech"], "Draft level/POS changed")
        need(row["shortlist_snapshot"] == {
             "english_definition": source["english_definition"],
             "myanmar_meaning": source["burmese_meaning"],
             "example_sentence": source["example_sentence"]}, "Bilingual/example source drift")
        need(row["shortlist_provenance"] == {k:source[k] for k in
             ("source_path", "source_index", "source_blob_sha")}, "Historical provenance changed")
        need(row["publisher_source"] == {
             "publisher":"Oxford University Press",
             "title":"The Oxford 3000 by CEFR level",
             "url":URL, "observed_on":"2026-10-29",
             "pdf_page":page, "extracted_line":line,
             "source_excerpt":excerpt, "source_cefr_level":source_level,
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Oxford publisher excerpt/locator drift")
        need(row["editorial_hold"] is True and row["independently_reviewed"] is False
             and row["release_approved"] is False
             and row["independent_reviewer_receipt"] is None, "Forged human review/approval")
        need(isinstance(row["editorial_risk"], str) and len(row["editorial_risk"]) > 12
             and isinstance(row["independent_reviewer_task"], str)
             and "Independent human" in row["independent_reviewer_task"],
             "Missing exact-sense human review task")
    return True

def self_test(packet, shortlist):
    rejected = 0
    for index in range(12):
        for field, value in (
            ("word", "forged"),
            ("level", "C1"),
            ("part_of_speech", "forged"),
            ("shortlist_snapshot", {"english_definition":"forged"}),
            ("shortlist_provenance", {"source_blob_sha":"0"*40}),
            ("publisher_source", {"source_cefr_level":"B1"}),
            ("editorial_risk", ""),
            ("independent_reviewer_task", "forged"),
            ("editorial_hold", False),
            ("independently_reviewed", True),
            ("release_approved", True),
            ("independent_reviewer_receipt", {"reviewer":"fake"}),
        ):
            tampered = copy.deepcopy(packet)
            tampered["records"][index][field] = value
            try:
                audit(tampered, shortlist)
            except (ValueError, KeyError, TypeError):
                rejected += 1
            else:
                raise AssertionError("Tampered publisher/translation/approval accepted")
    need(rejected == 144, "Mutation test count drift")
    return rejected

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    packet = json.loads(PACKET.read_text("utf8"))
    shortlist = json.loads(SHORT.read_text("utf8"))
    audit(packet, shortlist)
    print("PASS: 12 distinct B1-draft Oxford word/POS observations: A1=3 A2=3 B1=4 B2=2; independent approvals=0")
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: rejected %d/%d forged publisher, Myanmar, provenance and reviewer mutations" % (n,n))

if __name__ == "__main__":
    main()
