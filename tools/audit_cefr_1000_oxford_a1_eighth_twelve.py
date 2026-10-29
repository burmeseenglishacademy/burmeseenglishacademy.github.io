#!/usr/bin/env python3
"""Fail-closed, publisher-locator-bound A1 temporal and family word/POS evidence.

Source word/POS CEFR levels are NOT independent exact-sense, Myanmar, example,
real listening, or publication approval. This auditor never changes production.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-EIGHTH-TWELVE-2026-10-29.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = (
    ("today", "A1", 3, 805, "today adv., n."),
    ("tomorrow", "A1", 3, 809, "tomorrow adv., n."),
    ("yesterday", "A1", 4, 903, "yesterday adv., n."),
    ("morning", "A1", 2, 495, "morning n."),
    ("afternoon", "A1", 1, 18, "afternoon n."),
    ("evening", "A1", 1, 248, "evening n."),
    ("night", "A1", 2, 522, "night n."),
    ("week", "A1", 4, 868, "week n."),
    ("month", "A1", 2, 493, "month n."),
    ("minute", "A1", 2, 485, "minute1 n."),
    ("hour", "A1", 2, 379, "hour n."),
    ("brother", "A1", 1, 110, "brother n."),
)
RISKS = {"today":"A1_EIGHTH_TWELVE_TODAY_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","tomorrow":"A1_EIGHTH_TWELVE_TOMORROW_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","yesterday":"A1_EIGHTH_TWELVE_YESTERDAY_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","morning":"A1_EIGHTH_TWELVE_MORNING_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","afternoon":"A1_EIGHTH_TWELVE_AFTERNOON_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","evening":"A1_EIGHTH_TWELVE_EVENING_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","night":"A1_EIGHTH_TWELVE_NIGHT_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","week":"A1_EIGHTH_TWELVE_WEEK_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","month":"A1_EIGHTH_TWELVE_MONTH_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","minute":"A1_EIGHTH_TWELVE_MINUTE_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","hour":"A1_EIGHTH_TWELVE_HOUR_WORD_POS_AND_EXAMPLE_SENSE_REVIEW","brother":"A1_EIGHTH_TWELVE_BROTHER_WORD_POS_AND_EXAMPLE_SENSE_REVIEW"}
TASKS = {"today":"Independent human reviewer: Today is Monday uses today as a nominal subject, although the provisional part of speech says adverb; require a sense/POS-aligned original example or independently reviewed POS amendment. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","tomorrow":"Independent human reviewer: Distinguish adverbial tomorrow in the example from nominal tomorrow; verify Myanmar time reference and example naturalness. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","yesterday":"Independent human reviewer: Yesterday was Sunday uses yesterday nominally as a subject while draft POS says adverb; require independent grammar and example correction. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","morning":"Independent human reviewer: Distinguish morning as a noun from the temporal adverbial phrase in the morning; check fluent Myanmar and natural example. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","afternoon":"Independent human reviewer: Check afternoon time span and preposition in the afternoon; keep it distinct from evening. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","evening":"Independent human reviewer: Check evening versus night and the time expression in the evening in both languages. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","night":"Independent human reviewer: Check night as a time period, not an adjective; verify sleep at night collocation. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","week":"Independent human reviewer: Review a week as rate/frequency construction and distinguish seven-day period from calendar week. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","month":"Independent human reviewer: Review next month without a preposition and the relative-time Myanmar translation. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","minute":"Independent human reviewer: Oxford minute1 is the time-unit noun, not the unrelated adjective meaning tiny; verify sixty-second sense. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","hour":"Independent human reviewer: Check hour noun, one hour duration, and an hour article in alternative examples. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval.","brother":"Independent human reviewer: Check brother as male sibling, Myanmar kinship nuance and natural singular example. Verify exact publisher-backed sense/CEFR, fluent Myanmar, example grammar and original wording; Oxford word/POS level alone is not independent approval."}
PRIOR = ["A1-TWELVE-DIRECT-PDF-2026-10-28","A1-SECOND-TWELVE-2026-10-28","A1-THIRD-TWELVE-2026-10-28","A1-FOURTH-TWENTYFOUR-2026-10-29","A1-FIFTH-TWENTYFOUR-2026-10-29","A1-SIXTH-TWENTYFOUR-2026-10-29","A1-SEVENTH-TWELVE-2026-10-29"]

def need(test, message):
    if not test:
        raise ValueError(message)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(sha == SHORT_SHA, "Frozen shortlist Git blob drift")
    need(len(shortlist["entries"]) == 1000 and
         shortlist["counts_by_level"] == {x: 200 for x in LEVELS} and
         shortlist["independently_approved_by_level"] == {x: 0 for x in LEVELS},
         "Frozen scope or approval drift")
    need(packet["schema"] == 1 and packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet["status"] == "A1_EIGHTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet["observed_on"] == "2026-10-29"
         and packet["shortlist_blob_sha"] == SHORT_SHA, "Packet scope/provenance drift")
    need(packet["record_count"] == len(packet["records"]) == 12
         and packet["counts_by_level"] == {"A1":12,"A2":0,"B1":0,"B2":0,"C1":0}
         and packet["publisher_reference_level_counts"] == {"A1":12,"A2":0,"B1":0,"B2":0,"C1":0}
         and packet["word_pos_discrepancies"] == 0
         and packet["independently_approved_count"] == 0, "Counts or approvals forged")
    need(packet["source_limitations"] == "Direct Oxford University Press official Oxford 3000 PDF word/POS observations on 2026-10-29, one-based PDF pages and zero-based extracted lines. All 12 publisher A1 word/POS observations remain exact-sense and example/POS unverified. In particular today/yesterday nominal-subject examples conflict with provisional adverb labels. No independent linguistic approval, real listening, physical device QA or production publication.",
         "Source limitations removed or altered")
    by_word = {x["word"]: x for x in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate frozen headword")
    words = [x[0] for x in EXPECTED]
    need(len(set(words)) == 12, "Repeated expected word")
    for suffix in PRIOR:
        old = json.loads((ROOT / ("draft/CEFR-1000-OXFORD-" + suffix + ".json")).read_text("utf-8"))
        need(not set(words).intersection(x["word"] for x in old["records"]),
             "New packet repeats an earlier A1 source observation")
    for row, (word, source_level, page, line, excerpt) in zip(packet["records"], EXPECTED):
        need(row["word"] == word, "Wrong word/order")
        src = by_word[word]
        need(row["level"] == src["level"] == "A1"
             and row["part_of_speech"] == src["part_of_speech"], "Wrong draft POS/level")
        need(row["shortlist_snapshot"] == {
            "english_definition": src["english_definition"],
            "myanmar_meaning": src["burmese_meaning"],
            "example_sentence": src["example_sentence"]}, "English/Myanmar/example snapshot drift")
        need(row["shortlist_provenance"] == {
            k: src[k] for k in ("source_path", "source_index", "source_blob_sha")},
            "Historical Git provenance drift")
        need(row["publisher_source"] == {
            "publisher": "Oxford University Press",
            "title": "The Oxford 3000 by CEFR level",
            "url": URL, "observed_on": "2026-10-29",
            "pdf_page": page, "extracted_line": line,
            "source_excerpt": excerpt, "source_cefr_level": source_level,
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Oxford source excerpt/locator drift")
        need(row["editorial_risk"] == RISKS[word]
             and row["independent_reviewer_task"] == TASKS[word],
             "Exact-sense editorial task changed or removed")
        need(row["editorial_hold"] is True
             and row["independently_reviewed"] is False
             and row["release_approved"] is False
             and row["independent_reviewer_receipt"] is None,
             "False human signoff or release approval")
    return True

def self_test(packet, shortlist):
    rejected = 0
    for i in range(12):
        for field, fake in (
            ("word", "forged"),
            ("level", "C1"),
            ("part_of_speech", "forged"),
            ("shortlist_snapshot", {"english_definition": "forged"}),
            ("shortlist_provenance", {"source_blob_sha": "0" * 40}),
            ("publisher_source", {"source_cefr_level": "C1"}),
            ("editorial_risk", "FORGED_RISK"),
            ("independent_reviewer_task", "FORGED_TASK"),
            ("editorial_hold", False),
            ("independently_reviewed", True),
            ("release_approved", True),
            ("independent_reviewer_receipt", {"reviewer": "fake"}),
        ):
            changed = copy.deepcopy(packet)
            changed["records"][i][field] = fake
            try:
                audit(changed, shortlist)
            except (ValueError, KeyError, TypeError):
                rejected += 1
            else:
                raise AssertionError("Forged source, Myanmar, task or approval accepted")
    need(rejected == 144, "Negative mutation test count drift")
    return rejected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text("utf-8"))
    shortlist = json.loads(SHORT.read_text("utf-8"))
    audit(packet, shortlist)
    print("PASS: 12 new A1 Oxford word/POS observations; zero independent approvals")
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: rejected %d/%d forged A1 source, Myanmar, example and reviewer mutations" % (n, n))

if __name__ == "__main__":
    main()
