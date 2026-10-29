#!/usr/bin/env python3
"""Fail-closed B1 fifth-twelve Oxford word/POS evidence audit, staging only."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-FIFTH-TWELVE-2026-10-29.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
EXPECTED = [
    ("block","B1",7,1857,"block n., v."),
    ("equipment","A2",5,1172,"equipment n."),
    ("nation","B1",9,2228,"nation n."),
    ("otherwise","B2",12,3048,"otherwise adv."),
    ("purpose","A2",6,1515,"purpose n."),
    ("responsible","B1",9,2387,"responsible adj."),
    ("theory","B1",10,2504,"theory n."),
    ("agency","B2",10,2612,"agency n."),
    ("avoid","A2",4,973,"avoid v."),
    ("coast","A2",4,1058,"coast n."),
    ("economy","B1",8,2000,"economy n."),
    ("environment","A2",5,1171,"environment n."),
]
LEVELS = ("A1","A2","B1","B2","C1")

def need(condition, why):
    if not condition:
        raise ValueError(why)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()
    need(blob == SHORT_SHA, "Frozen shortlist blob changed")
    need(shortlist["counts_by_level"] == {k:200 for k in LEVELS}
         and shortlist["independently_approved_by_level"] == {k:0 for k in LEVELS}
         and len(shortlist["entries"]) == 1000, "Frozen scope/approval changed")
    need(packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet["status"] == "B1_FIFTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet["observed_on"] == "2026-10-29"
         and packet["shortlist_blob_sha"] == SHORT_SHA, "Packet source/status drift")
    need(packet["record_count"] == 12 and len(packet["records"]) == 12
         and packet["counts_by_level"] == {"A1":0,"A2":0,"B1":12,"B2":0,"C1":0}
         and packet["publisher_reference_level_counts"] == {"A1":0,"A2":5,"B1":5,"B2":2,"C1":0}
         and packet["word_pos_discrepancies"] == 7
         and packet["independently_approved_count"] == 0, "Count/approval drift")
    by_word = {e["word"]:e for e in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist word")
    for row, (word, source_level, page, line, excerpt) in zip(packet["records"], EXPECTED):
        need(row["word"] == word, "Word/order drift")
        original = by_word[word]
        need(row["level"] == original["level"] == "B1"
             and row["part_of_speech"] == original["part_of_speech"], "POS/level drift")
        need(row["shortlist_snapshot"] == {k:original[k] for k in
             ("english_definition","burmese_meaning","example_sentence")}, "English/Myanmar/example changed")
        need(row["shortlist_provenance"] == {k:original[k] for k in
             ("source_path","source_index","source_blob_sha")}, "Historical Git provenance changed")
        need(row["publisher_source"] == {
             "publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level",
             "url":URL,"observed_on":"2026-10-29","pdf_page":page,"extracted_line":line,
             "source_excerpt":excerpt,"source_cefr_level":source_level,
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher source altered")
        need(row["editorial_hold"] is True and row["independently_reviewed"] is False
             and row["release_approved"] is False and row["independent_reviewer_receipt"] is None,
             "Fabricated reviewer approval")
        need(isinstance(row["editorial_risk"],str) and len(row["editorial_risk"]) > 12
             and "Independent human" in row["independent_reviewer_task"], "Missing reviewer task")
    return True

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    packet=json.loads(PACKET.read_text("utf8"))
    shortlist=json.loads(SHORT.read_text("utf8"))
    audit(packet,shortlist)
    print("PASS: 12 B1-draft publisher observations (5 A2, 5 B1, 2 B2), zero independent approval")
    if args.self_test:
        rejected=0
        for index in range(12):
            for field,value in (
                ("word","fake"),("level","C1"),("part_of_speech","fake"),
                ("shortlist_snapshot",{"english_definition":"fake"}),
                ("shortlist_provenance",{"source_blob_sha":"0"*40}),
                ("publisher_source",{"source_cefr_level":"B1"}),
                ("editorial_hold",False),("independently_reviewed",True),
                ("release_approved",True),("independent_reviewer_receipt",{"reviewer_id":"fake"})):
                forged=copy.deepcopy(packet)
                forged["records"][index][field]=value
                try:
                    audit(forged,shortlist)
                except (ValueError,KeyError,TypeError):
                    rejected+=1
                else:
                    raise AssertionError("Forged evidence or review passed")
        need(rejected==120,"Mutation count drift")
        print("PASS: rejected 120/120 publisher, bilingual, provenance and false-review mutations")
if __name__=="__main__":
    main()
