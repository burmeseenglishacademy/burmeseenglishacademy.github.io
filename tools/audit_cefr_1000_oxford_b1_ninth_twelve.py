#!/usr/bin/env python3
"""Staging-only, immutable Oxford B1 ninth-twelve source and bilingual hold auditor.

Direct publisher observations are not independent exact-sense CEFR approval.
The packet's Git blob SHA freezes every observation, source URL, original
Myanmar/example snapshot, editorial risk, and absence of human receipts.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB_SHA = "70099e29caf35365981cef20122a9ccf621c431d"
SHORT_BLOB_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
EXPECTED = [["protection","B2",12,3105,"protection n."],["receive","A2",6,1530,"receive v."],["speech","A2",6,1647,"speech n."],["traffic","A1",4,816,"traffic n."],["demand","B2",11,2774,"demand n., v."],["investment","B2",11,2957,"investment n."],["structure","A2",7,1669,"structure n."],["appear","A2",4,950,"appear v."],["exchange","B1",8,2034,"exchange n., v."],["powerful","B1",9,2307,"powerful adj."],["partner","A1",3,575,"partner n."],["solution","A2",6,1640,"solution n."]]
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def need(ok, why):
    if not ok:
        raise ValueError(why)

def git_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()

def audit(packet, shortlist):
    raw = PACKET.read_bytes()
    need(git_sha(raw) == PACKET_BLOB_SHA, "B1 ninth publisher packet changed")
    need(git_sha(SHORT.read_bytes()) == SHORT_BLOB_SHA, "Frozen shortlist changed")
    need(packet == json.loads(raw.decode("utf-8")), "Publisher or bilingual packet mutated")
    need(packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("record_count") == 12
         and packet.get("word_pos_discrepancies") == 10
         and packet.get("direct_dictionary_sense_leads") == 4
         and packet.get("independently_approved_count") == 0,
         "Source/review scope or totals drift")
    need(packet.get("publisher_reference_level_counts") == {"A1":2,"A2":5,"B1":2,"B2":3},
         "Oxford classification totals drift")
    need(shortlist.get("counts_by_level") == {x:200 for x in LEVELS}
         and shortlist.get("independently_approved_by_level") == {x:0 for x in LEVELS},
         "Approved quotas or human signoffs drift")
    entries = shortlist.get("entries")
    need(isinstance(entries, list) and len(entries) == 1000
         and len({r["word"] for r in entries}) == 1000,
         "Shortlist must have exactly 1000 distinct held words")
    by_word = {r["word"]: r for r in entries}
    rows = packet.get("records")
    need(isinstance(rows, list) and len(rows) == len(EXPECTED), "Record count drift")
    for row, (word, cefr, page, line, excerpt) in zip(rows, EXPECTED):
        source = by_word.get(word)
        need(source is not None and source.get("level") == "B1"
             and row.get("word") == word and row.get("level") == "B1"
             and row.get("part_of_speech") == source.get("part_of_speech"),
             "Wrong B1 headword or part of speech: " + word)
        need(row.get("shortlist_snapshot") == {
             "english_definition": source["english_definition"],
             "myanmar_meaning": source["burmese_meaning"],
             "example_sentence": source["example_sentence"]},
             "English/Myanmar/example drift: " + word)
        need(row.get("shortlist_provenance") == {k:source[k] for k in
             ("source_path","source_index","source_blob_sha")},
             "Historical source provenance drift: " + word)
        p = row.get("publisher_source", {})
        need(p.get("publisher") == "Oxford University Press"
             and p.get("url") == SOURCE_URL and p.get("observed_on") == "2026-10-30"
             and p.get("pdf_page") == page and p.get("extracted_line") == line
             and p.get("source_excerpt") == excerpt and p.get("source_cefr_level") == cefr
             and p.get("access") == "DIRECT_OFFICIAL_PDF_WEB_TEXT"
             and p.get("evidence_scope") == "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "Publisher source/locator or CEFR word-POS evidence drift: " + word)
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
             and row.get("release_approved") is False and row.get("independent_reviewer_receipt") is None
             and source.get("editorial_hold") is True and source.get("release_approved") is False,
             "Forged independent review or release approval: " + word)
        need(isinstance(row.get("editorial_risk"), str) and len(row["editorial_risk"]) > 35
             and "Independent human reviewer" in row.get("independent_reviewer_task", ""),
             "Missing human exact-sense review task: " + word)
        lead = row.get("dictionary_sense_lead")
        if word in ("protection", "demand", "investment", "exchange"):
            need(isinstance(lead, dict)
                 and lead.get("url", "").startswith("https://www.oxfordlearnersdictionaries.com/definition/english/" + word)
                 and lead.get("observed_on") == "2026-10-30"
                 and lead.get("evidence_scope") == "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF",
                 "Direct dictionary sense lead changed: " + word)
            need(row.get("editorial_rewrite_candidate", {}).get("status")
                 == "UNAPPROVED_EDITORIAL_PROPOSAL_NOT_APPLIED",
                 "Bilingual rewrite was falsely approved: " + word)
        else:
            need(lead is None and row.get("editorial_rewrite_candidate") is None,
                 "Unobserved dictionary or invented rewrite: " + word)
    return {"written":200,"independently_approved":0,"word_pos_observations":12,
            "publisher_lower":7,"publisher_higher":3,"word_pos_match_unverified":2,
            "direct_dictionary_sense_leads":4,"release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    tests = []
    for index in range(12):
        for name, mut in (
            ("word", lambda r: r.update(word="forged")),
            ("level", lambda r: r.update(level="C1")),
            ("pos", lambda r: r.update(part_of_speech="forged")),
            ("source-cefr", lambda r: r["publisher_source"].update(source_cefr_level="C1" if index != 0 else "A1")),
            ("source-line", lambda r: r["publisher_source"].update(extracted_line=-1)),
            ("source-url", lambda r: r["publisher_source"].update(url="https://example.org/forged.pdf")),
            ("Myanmar", lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အမှား")),
            ("English", lambda r: r["shortlist_snapshot"].update(english_definition="forged")),
            ("example", lambda r: r["shortlist_snapshot"].update(example_sentence="forged")),
            ("provenance", lambda r: r["shortlist_provenance"].update(source_index=-1)),
            ("fake-review", lambda r: r.update(independently_reviewed=True)),
            ("fake-approval", lambda r: r.update(release_approved=True)),
            ("fake-listening", lambda r: r.update(independent_reviewer_receipt={"heard":True})),
        ):
            mutated = copy.deepcopy(packet)
            mut(mutated["records"][index])
            tests.append((name, mutated))
    for name, mutated in tests:
        try:
            audit(mutated, shortlist)
        except ValueError:
            continue
        raise AssertionError("Forged B1 source/translation/signoff accepted: " + name)
    return len(tests)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args=p.parse_args()
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist=json.loads(SHORT.read_text(encoding="utf-8"))
    result=audit(packet, shortlist)
    if args.self_test:
        n=self_test(packet, shortlist)
        print(f"PASS: rejected {n}/{n} B1 ninth forged source/bilingual/reviewer mutations")
    print(json.dumps({"level":args.level, **result},sort_keys=True))

if __name__ == "__main__":
    main()
