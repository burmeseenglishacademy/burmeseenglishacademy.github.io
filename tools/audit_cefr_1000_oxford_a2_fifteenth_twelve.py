#!/usr/bin/env python3
"""Fail-closed Oxford A2 fifteenth 12 word/POS and four direct sense leads; NEVER approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A1","A2","B1","B2","C1")
PACKET_PATH = "draft/CEFR-1000-OXFORD-A2-FIFTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORTLIST_PATH = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "6714b6f6612855aa75a82d1f3f0013cfd5c133e1"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
EXPECTED = json.loads(r'''[["similar","A1",3,697,"similar adj."],["common","A1",1,164,"common adj."],["likely","A2",5,1362,"likely adj."],["fine","A1",2,290,"fine adj."],["couple","A2",4,1088,"couple n."],["online","A1",3,552,"online adj., adv."],["return","A1",3,651,"return v., n."],["wish","A2",7,1769,"wish v., n."],["finally","A2",5,1213,"finally adv."],["guess","A1",2,342,"guess v., n."],["gold","A2",5,1250,"gold n., adj."],["middle","A2",6,1396,"middle n., adj."]]''')
SENSES = json.loads(r'''{"fine":["https://www.oxfordlearnersdictionaries.com/definition/english/fine_1",3,178,185],"couple":["https://www.oxfordlearnersdictionaries.com/definition/english/couple_1",2,103,126],"online":["https://www.oxfordlearnersdictionaries.com/definition/english/online_2",1,88,119],"wish":["https://www.oxfordlearnersdictionaries.com/definition/english/wish_1",1,114,129]}''')
ROOT_KEYS = {"schema","scope","status","observed_on","shortlist_blob_sha","record_count","counts_by_level","publisher_reference_level_counts","word_pos_discrepancies","direct_dictionary_sense_leads","independently_approved_count","source_limitations","records"}
ROW_KEYS = {"word","level","part_of_speech","shortlist_snapshot","shortlist_provenance","publisher_source","editorial_risk","independent_reviewer_task","editorial_hold","independently_reviewed","release_approved","independent_reviewer_receipt"}
SOURCE_KEYS = {"publisher","title","url","observed_on","pdf_page","extracted_line","source_excerpt","source_cefr_level","evidence_scope","access"}
SENSE_KEYS = {"url","sense_number","page_text_line_start","page_text_line_end","observed_on","evidence_scope","sense_summary"}
CANDIDATE_KEYS = {"myanmar_meaning","original_example","review_status"}

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def audit(packet, shortlist):
    require(set(packet) == ROOT_KEYS, "Packet root schema drift")
    require(packet["schema"] == 1 and packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet["status"] == "A2_FIFTEENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and packet["observed_on"] == "2026-10-31" and packet["shortlist_blob_sha"] == SHORTLIST_SHA,
            "Scope, status, observation date or shortlist binding drift")
    require(packet["record_count"] == 12
            and packet["counts_by_level"] == dict(zip(LEVELS,(0,12,0,0,0)))
            and packet["publisher_reference_level_counts"] == dict(zip(LEVELS,(6,6,0,0,0)))
            and packet["word_pos_discrepancies"] == 6
            and packet["direct_dictionary_sense_leads"] == 4
            and packet["independently_approved_count"] == 0
            and "not independent exact-sense cefr approval" in packet["source_limitations"].lower()
            and "fine weather example" in packet["source_limitations"].lower()
            and "word of the day" in packet["source_limitations"].lower(),
            "Source totals or scope disclaimers changed")
    require(shortlist.get("release_status") == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH"
            and shortlist.get("counts_by_level") == dict.fromkeys(LEVELS,200)
            and shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS,0),
            "Frozen 1000 release status or independent approval drift")
    entries = shortlist.get("entries")
    require(isinstance(entries,list) and len(entries) == 1000, "Exactly 1000 entries required")
    byword = {r["word"]:r for r in entries}
    require(len(byword) == 1000 and all(
        r.get("editorial_hold") is True and r.get("release_approved") is False
        and all(r.get(k) is False for k in
            ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation"))
        for r in entries), "Frozen shortlist duplication or fabricated independent review")
    records = packet.get("records")
    require(isinstance(records,list) and len(records) == 12, "Packet row count drift")
    seen = set()
    for row, expected in zip(records,EXPECTED):
        word, source_level, page, line, excerpt = expected
        require(set(row) == ROW_KEYS | ({"dictionary_sense_lead","editorial_rewrite_candidate"} if word in SENSES else set()),
                "Row schema or unauthorized signoff field drift: " + word)
        require(row["word"] == word and word not in seen and row["level"] == "A2", "Word order/level/duplicate drift")
        seen.add(word)
        s = byword[word]
        require(s["level"] == "A2" and row["part_of_speech"] == s["part_of_speech"], "Draft POS drift: " + word)
        require(row["shortlist_snapshot"] == {"english_definition":s["english_definition"],
                 "myanmar_meaning":s["burmese_meaning"],"example_sentence":s["example_sentence"]},
                "Original English/Myanmar/example changed: " + word)
        require(row["shortlist_provenance"] == {k:s[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical source provenance changed: " + word)
        p = row["publisher_source"]
        require(set(p) == SOURCE_KEYS and p == {
            "publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level",
            "url":PDF,"observed_on":"2026-10-31","pdf_page":page,"extracted_line":line,
            "source_excerpt":excerpt,"source_cefr_level":source_level,
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
            "Publisher evidence attribution/CEFR/POS/page/line changed: " + word)
        require(isinstance(row["editorial_risk"],str) and len(row["editorial_risk"]) > 25
                and "independent" in row["independent_reviewer_task"].lower()
                and "not independent approval" in row["independent_reviewer_task"].lower()
                and row["editorial_hold"] is True and row["independently_reviewed"] is False
                and row["release_approved"] is False and row["independent_reviewer_receipt"] is None,
                "Missing editorial risk or forged independent signoff: " + word)
        if word in SENSES:
            lead = row["dictionary_sense_lead"]
            url,num,start,end = SENSES[word]
            require(set(lead) == SENSE_KEYS and lead["url"] == url and lead["sense_number"] == num
                    and lead["page_text_line_start"] == start and lead["page_text_line_end"] == end
                    and lead["observed_on"] == "2026-10-31"
                    and lead["evidence_scope"] == "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and isinstance(lead["sense_summary"],str) and len(lead["sense_summary"]) > 35,
                    "Dictionary exact-sense lead drift: " + word)
            proposal = row["editorial_rewrite_candidate"]
            require(set(proposal) == CANDIDATE_KEYS and proposal["review_status"] == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and isinstance(proposal["myanmar_meaning"],str) and len(proposal["myanmar_meaning"]) > 15
                    and isinstance(proposal["original_example"],str) and len(proposal["original_example"]) > 25,
                    "Myanmar/original example proposal lost or promoted: " + word)
    require(seen == {r[0] for r in EXPECTED}, "Unobserved word or duplicate")
    return {"scope":"STAGING_ONLY_PUBLISHER_WORD_POS_NOT_INDEPENDENT_EXACT_SENSE_APPROVAL",
            "draft_level":"A2","observed":len(records),"source_reference_levels":packet["publisher_reference_level_counts"],
            "publisher_word_pos_discrepancies":6,"dictionary_sense_leads":4,
            "first_pass_written":200,"independently_approved":0,
            "george_emma_listening_signoffs":0,"release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    baseline = audit(packet,shortlist)
    cases = 0
    for i,row in enumerate(packet["records"]):
        edits = [
            lambda r: r["publisher_source"].update(source_cefr_level="C1" if r["publisher_source"]["source_cefr_level"] != "C1" else "A1"),
            lambda r: r["publisher_source"].update(source_excerpt="forged publisher line"),
            lambda r: r["publisher_source"].update(extracted_line=-1),
            lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အတု"),
            lambda r: r["shortlist_snapshot"].update(example_sentence="forged example"),
            lambda r: r["shortlist_provenance"].update(source_index=-1),
            lambda r: r.update(independently_reviewed=True),
            lambda r: r.update(release_approved=True),
            lambda r: r.update(independent_reviewer_receipt={"fake":"signed"}),
            lambda r: r.update(editorial_hold=False),
        ]
        if row["word"] in SENSES:
            edits += [
                lambda r: r["dictionary_sense_lead"].update(sense_number=999),
                lambda r: r["dictionary_sense_lead"].update(evidence_scope="INDEPENDENT_APPROVED"),
                lambda r: r["editorial_rewrite_candidate"].update(review_status="APPROVED"),
                lambda r: r["editorial_rewrite_candidate"].update(myanmar_meaning=""),
            ]
        for edit in edits:
            forged = copy.deepcopy(packet)
            edit(forged["records"][i])
            try:
                audit(forged,shortlist)
            except ValueError:
                cases += 1
                continue
            raise AssertionError("Forged evidence/review mutation passed: " + row["word"])
    for edit in [
        lambda p:p.update(independently_approved_count=1),
        lambda p:p.update(record_count=11),
        lambda p:p["records"].pop(),
        lambda p:p["records"].reverse(),
        lambda p:p.update(source_limitations="Independent CEFR approved"),
    ]:
        forged=copy.deepcopy(packet)
        edit(forged)
        try:
            audit(forged,shortlist)
        except ValueError:
            cases += 1
            continue
        raise AssertionError("Forged packet scope passed")
    return baseline,cases

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    packet_path=ROOT/PACKET_PATH
    shortlist_path=ROOT/SHORTLIST_PATH
    require(blob_sha(packet_path)==PACKET_SHA,"Pinned Oxford source packet blob changed")
    require(blob_sha(shortlist_path)==SHORTLIST_SHA,"Pinned shortlist blob changed")
    packet=json.loads(packet_path.read_text(encoding="utf-8"))
    shortlist=json.loads(shortlist_path.read_text(encoding="utf-8"))
    if args.self_test:
        report,n=self_test(packet,shortlist)
        print("PASS: rejected %d/%d forged Oxford source, bilingual, sense and independent-review mutations"%(n,n))
    else:
        report=audit(packet,shortlist)
    if args.level != "ALL":
        print(json.dumps({args.level:{"written":200,"new_source_observations":12 if args.level=="A2" else 0,
                               "independently_approved":0},"release":"BLOCKED_STAGING_ONLY"},sort_keys=True))
    else:
        print(json.dumps(report,sort_keys=True))

if __name__=="__main__":
    main()
