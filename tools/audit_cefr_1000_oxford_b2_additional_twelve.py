#!/usr/bin/env python3
"""Fail-closed integrity audit for 12 additional B2-draft Oxford word/POS leads.
This audits provenance and editorial holds, NOT independently verified exact senses.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-ADDITIONAL-TWELVE-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED = {
    "relief": ("B2", 12, 3132, "relief n.", "RELIEF_EMOTION_VS_ASSISTANCE"),
    "shame": ("B2", 12, 3185, "shame n.", "SHAME_EMOTION_VS_DISGRACE"),
    "somewhat": ("B2", 12, 3204, "somewhat adv.", "DEGREE_ADVERB_MYANMAR_NATURALNESS"),
    "surely": ("B1", 10, 2487, "surely adv.", "LOWER_OXFORD_B1_EPISTEMIC_USAGE"),
    "absolute": ("B2", 10, 2594, "absolute adj.", "ABSOLUTE_SILENCE_COLLOCATION"),
    "incident": ("B2", 11, 2932, "incident n.", "INCIDENT_SAFETY_REPORT_CONTEXT"),
    "quit": ("B1", 9, 2346, "quit v.", "LOWER_OXFORD_B1_LEAVE_JOB_SENSE"),
    "widely": ("B2", 12, 3307, "widely adv.", "WIDELY_USED_COLLOCATION"),
    "worldwide": ("B1", 10, 2582, "worldwide adj., adv.", "LOWER_OXFORD_B1_ADVERB_SENSE"),
    "anniversary": ("B2", 10, 2622, "anniversary n.", "ANNIVERSARY_YEARLY_RECURRENCE"),
    "attractive": ("A2", 4, 967, "attractive adj.", "LOWER_OXFORD_A2_DESIGN_APPEAL"),
    "broad": ("B2", 10, 2668, "broad adj.", "BROAD_ABSTRACT_SCOPE"),
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def require(condition, message):
    if not condition:
        raise ValueError(message)

def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

def audit(packet, shortlist, sha, level="ALL"):
    require(sha == SHORTLIST_SHA, "Shortlist blob changed; rebind source evidence")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Packet scope drift")
    require(packet.get("status") == "B2_ADDITIONAL_TWELVE_DIRECT_OXFORD_WORD_POS_LEADS_EDITORIAL_HOLD", "Packet status drift")
    require(packet.get("observed_on") == "2026-10-28" and packet.get("shortlist_blob_sha") == sha, "Packet observation provenance drift")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 12, "Wrong record count")
    require(packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}, "Packet level counts drift")
    require(type(packet.get("word_pos_discrepancies")) is int and packet["word_pos_discrepancies"] == 4, "Conflict count drift")
    require(type(packet.get("independently_approved_count")) is int and packet["independently_approved_count"] == 0, "Fake approvals")
    require("NOT independently verified" in packet.get("source_limitations", ""), "Publisher scope caveat missing")
    require(shortlist.get("scope_target") == {k:200 for k in LEVELS}, "Scope is not 1000")
    require(shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}, "Independent approval misreported")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Shortlist length drift")
    require({k:sum(e.get("level")==k for e in entries) for k in LEVELS} == {k:200 for k in LEVELS}, "Per-level count drift")
    require(len({e.get("word","").casefold() for e in entries}) == 1000, "Duplicate cross-level headword")
    index = {(e.get("word"),e.get("level")):e for e in entries}
    records = packet.get("records")
    require(isinstance(records,list) and len(records)==12, "Missing observations")
    require(len({r.get("word") for r in records if isinstance(r,dict)})==12, "Duplicate observation")
    require({r.get("word") for r in records} == set(EXPECTED), "Unexpected observed word")
    for rec in records:
        word = rec["word"]
        e = index.get((word,"B2"))
        require(e is not None and rec.get("level") == "B2", word+" not B2-bound")
        require(rec.get("part_of_speech") == e.get("part_of_speech"), word+" POS changed")
        require(rec.get("shortlist_snapshot") == {
            "english_definition":e["english_definition"],
            "myanmar_meaning":e["burmese_meaning"],
            "example_sentence":e["example_sentence"]
        }, word+" bilingual/example source drift")
        require(rec.get("shortlist_provenance") == {
            "source_path":e["source_path"],
            "source_index":e["source_index"],
            "source_blob_sha":e["source_blob_sha"]
        }, word+" Git source provenance drift")
        cefr,page,line,excerpt,risk = EXPECTED[word]
        require(rec.get("publisher_source") == {
            "publisher":"Oxford University Press",
            "title":"The Oxford 3000 by CEFR level",
            "url":URL,
            "observed_on":"2026-10-28",
            "pdf_page":page,
            "extracted_line":line,
            "source_excerpt":excerpt,
            "source_cefr_level":cefr,
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"
        }, word+" Oxford observation drift")
        require(rec.get("editorial_risk") == risk, word+" editorial risk drift")
        task = rec.get("independent_reviewer_task")
        require(isinstance(task,str) and "Human-independent reviewer:" in task and "content-bound review receipt" in task, word+" independent task missing")
        require(rec.get("editorial_hold") is True and e.get("editorial_hold") is True, word+" hold removed")
        require(rec.get("independently_reviewed") is False and rec.get("release_approved") is False and rec.get("independent_reviewer_receipt") is None, word+" fabricated signoff")
        require(all(e.get(k) is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation","release_approved")), word+" shortlist signoff changed")
    return sum(EXPECTED[w][0] != "B2" for w in EXPECTED)

def negative_tests(packet, shortlist, sha):
    cases = [
        ("word",lambda p:p["records"][0].__setitem__("word","fabricated")),
        ("level",lambda p:p["records"][0].__setitem__("level","C1")),
        ("pos",lambda p:p["records"][0].__setitem__("part_of_speech","verb")),
        ("english",lambda p:p["records"][0]["shortlist_snapshot"].__setitem__("english_definition","fake")),
        ("myanmar",lambda p:p["records"][0]["shortlist_snapshot"].__setitem__("myanmar_meaning","fake")),
        ("example",lambda p:p["records"][0]["shortlist_snapshot"].__setitem__("example_sentence","fake")),
        ("source-path",lambda p:p["records"][0]["shortlist_provenance"].__setitem__("source_path","fake")),
        ("source-index",lambda p:p["records"][0]["shortlist_provenance"].__setitem__("source_index",-1)),
        ("source-blob",lambda p:p["records"][0]["shortlist_provenance"].__setitem__("source_blob_sha","fake")),
        ("publisher-url",lambda p:p["records"][0]["publisher_source"].__setitem__("url","https://example.com")),
        ("publisher-date",lambda p:p["records"][0]["publisher_source"].__setitem__("observed_on","2026-01-01")),
        ("publisher-page",lambda p:p["records"][0]["publisher_source"].__setitem__("pdf_page",0)),
        ("publisher-line",lambda p:p["records"][0]["publisher_source"].__setitem__("extracted_line",0)),
        ("publisher-excerpt",lambda p:p["records"][0]["publisher_source"].__setitem__("source_excerpt","fake n.")),
        ("publisher-level",lambda p:p["records"][0]["publisher_source"].__setitem__("source_cefr_level","C1")),
        ("scope",lambda p:p["records"][0]["publisher_source"].__setitem__("evidence_scope","INDEPENDENT_APPROVAL")),
        ("risk",lambda p:p["records"][0].__setitem__("editorial_risk","NONE")),
        ("hold",lambda p:p["records"][0].__setitem__("editorial_hold",False)),
        ("approval",lambda p:p["records"][0].__setitem__("release_approved",True)),
        ("review",lambda p:p["records"][0].__setitem__("independently_reviewed",True)),
        ("receipt",lambda p:p["records"][0].__setitem__("independent_reviewer_receipt",{"approved":True})),
        ("duplicate",lambda p:p["records"].__setitem__(1,copy.deepcopy(p["records"][0]))),
        ("counts",lambda p:p.__setitem__("word_pos_discrepancies",0)),
        ("task",lambda p:p["records"][0].__setitem__("independent_reviewer_task","self approved"))
    ]
    rejected=0
    for label,mutate in cases:
        forged=copy.deepcopy(packet)
        mutate(forged)
        try:
            audit(forged,shortlist,sha)
        except (ValueError,KeyError,TypeError):
            rejected+=1
        else:
            raise AssertionError("Fail-open negative mutation: "+label)
    return rejected,len(cases)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    data=SHORTLIST.read_bytes()
    sha=blob_sha(data)
    shortlist=json.loads(data)
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    conflicts=audit(packet,shortlist,sha,args.level)
    print(f"Oxford B2 additional twelve: PASS level={args.level}; 12 publisher word/POS observations, {conflicts} lower-level discrepancies, zero independent approvals")
    if args.self_test:
        rejected,total=negative_tests(packet,shortlist,sha)
        print(f"Oxford B2 additional twelve: {rejected}/{total} forged-source/false-approval negative mutations rejected")

if __name__=="__main__":
    main()
