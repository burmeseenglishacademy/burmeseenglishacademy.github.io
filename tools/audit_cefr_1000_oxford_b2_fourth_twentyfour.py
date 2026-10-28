#!/usr/bin/env python3
"""Fail-closed audit of 24 Oxford B2-draft word/POS research observations.
This verifies data integrity and provenance only. It does NOT independently
verify publisher semantics, human review, audio, device QA, or publication.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-FOURTH-TWENTYFOUR-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''{"resistance":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":7,"extracted_line":1711,"source_excerpt":"resistance n.","source_cefr_level":"C1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"C1_OPPOSITION_VS_ELECTRICAL_RESISTANCE"},"retail":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":3,"extracted_line":534,"source_excerpt":"retail n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"RETAIL_BUSINESS_VS_RETAIL_ADJECTIVE"},"calm":{"pos":"adjective","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":7,"extracted_line":1871,"source_excerpt":"calm adj., v., n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"LOWER_B1_CALM_ADJECTIVE_VS_B2"},"client":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":7,"extracted_line":1900,"source_excerpt":"client n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"LOWER_B1_PROFESSIONAL_CUSTOMER_SENSE"},"expansion":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":1,"extracted_line":233,"source_excerpt":"expansion n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"EXPANSION_PHYSICAL_VS_BUSINESS"},"empire":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":1,"extracted_line":210,"source_excerpt":"empire n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"EMPIRE_POLITICAL_VS_BUSINESS_METAPHOR"},"significantly":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":12,"extracted_line":3195,"source_excerpt":"significantly adv.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"SIGNIFICANTLY_QUANTITY_VS_IMPORTANCE"},"reporting":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":3,"extracted_line":528,"source_excerpt":"reporting n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"REPORTING_JOURNALISM_VS_WORKPLACE_REPORTS"},"closely":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":10,"extracted_line":2698,"source_excerpt":"closely adv.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"CLOSELY_ATTENTION_VS_PROXIMITY"},"constantly":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":10,"extracted_line":2723,"source_excerpt":"constantly adv.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"CONSTANTLY_FREQUENTLY_VS_UNINTERRUPTED"},"contest":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":10,"extracted_line":2727,"source_excerpt":"contest n., v.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"CONTEST_NOUN_COMPETITION_VS_VERB_DISPUTE"},"hardly":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":8,"extracted_line":2111,"source_excerpt":"hardly adv.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"LOWER_B1_BARELY_VS_HARD_ADVERB"},"motor":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":11,"extracted_line":3014,"source_excerpt":"motor n., adj.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"MOTOR_NOUN_VS_ADJECTIVE"},"officially":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 and Oxford 5000 by CEFR level (both inspected)","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","observed_on":"2026-10-29","pdf_page":null,"extracted_line":null,"source_excerpt":null,"source_cefr_level":null,"evidence_scope":"NO_MATCH_IN_TWO_INSPECTED_CORE_LIST_PDFS_NOT_PROOF_OF_CEFR","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"NO_EXACT_WORD_POS_IN_INSPECTED_OXFORD_CORE_PDFS"},"portion":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":2,"extracted_line":470,"source_excerpt":"portion n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"PORTION_FOOD_VS_GENERAL_PART"},"peak":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":6,"extracted_line":1568,"source_excerpt":"peak n.","source_cefr_level":"C1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"HIGHER_C1_PEAK_MAXIMUM_VS_MOUNTAIN_SUMMIT"},"reform":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":7,"extracted_line":1677,"source_excerpt":"reform n., v.","source_cefr_level":"C1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"HIGHER_C1_SYSTEM_REFORM_NOUN"},"retirement":{"pos":"noun","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":3,"extracted_line":535,"source_excerpt":"retirement n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"RETIREMENT_ACT_VS_POST_WORK_PERIOD"},"solar":{"pos":"adjective","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":12,"extracted_line":3203,"source_excerpt":"solar adj.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"SOLAR_ENERGY_VS_ASTRONOMY"},"somehow":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":3,"extracted_line":576,"source_excerpt":"somehow adv.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"SOMEHOW_UNKNOWN_METHOD_VS_DESPITE_DIFFICULTY"},"ultimate":{"pos":"adjective","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":3,"extracted_line":663,"source_excerpt":"ultimate adj.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"ULTIMATE_FINAL_VS_MOST_IMPORTANT"},"unknown":{"pos":"adjective","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":12,"extracted_line":3277,"source_excerpt":"unknown adj.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"UNKNOWN_CAUSE_VS_UNIDENTIFIED_PERSON"},"automatically":{"pos":"adverb","pub":{"publisher":"Oxford University Press","title":"The Oxford 5000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":1,"extracted_line":46,"source_excerpt":"automatically adv.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"AUTOMATICALLY_MACHINE_VS_UNCONSCIOUSLY"},"blind":{"pos":"adjective","pub":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","additional_inspected_url":null,"observed_on":"2026-10-29","pdf_page":10,"extracted_line":2662,"source_excerpt":"blind adj.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"risk":"BLIND_VISUAL_DISABILITY_VS_FIGURATIVE"}}''')
ALLOWED_RECORD_FIELDS = {"word", "level", "part_of_speech", "shortlist_snapshot",
    "shortlist_provenance", "publisher_source", "editorial_risk",
    "independent_reviewer_task", "editorial_hold", "independently_reviewed",
    "release_approved", "independent_reviewer_receipt"}

def require(ok, why):
    if not ok:
        raise ValueError(why)

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

def audit(packet, shortlist, sha, level="ALL"):
    require(sha == SHORTLIST_SHA, "Frozen shortlist Git blob mismatch")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Scope drift")
    require(packet.get("status") == "B2_FOURTH_TWENTYFOUR_OXFORD_CORE_LIST_EDITORIAL_HOLD", "Status drift")
    require(packet.get("observed_on") == "2026-10-29" and packet.get("shortlist_blob_sha") == sha, "Observation provenance drift")
    for field, val in {"record_count":24, "word_pos_discrepancies":7,
                       "lower_level_observations":3, "higher_level_observations":3,
                       "not_found_in_inspected_core_lists":1,
                       "independently_approved_count":0}.items():
        require(type(packet.get(field)) is int and packet[field] == val, "Packet count drift: "+field)
    require(packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":24,"C1":0}, "Packet level counts drift")
    require("does NOT prove" in packet.get("source_limitations",""), "Absence caveat removed")
    require(shortlist.get("scope_target") == {k:200 for k in LEVELS}, "Target changed")
    require(shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}, "Fabricated independent approvals")
    entries = shortlist.get("entries")
    require(isinstance(entries,list) and len(entries)==1000, "Shortlist count drift")
    require({k:sum(e.get("level")==k for e in entries) for k in LEVELS} == {k:200 for k in LEVELS}, "Level balance drift")
    require(len({e.get("word","").casefold() for e in entries})==1000, "Duplicate headwords")
    lookup = {(e.get("word"),e.get("level")):e for e in entries}
    records = packet.get("records")
    require(isinstance(records,list) and len(records)==24, "Missing records")
    require(all(isinstance(r,dict) for r in records), "Malformed record")
    require({r.get("word") for r in records}==set(EXPECTED), "Missing/extra/duplicate word")
    require(len({r.get("word") for r in records})==24, "Duplicate word")
    for rec in records:
        word = rec["word"]
        e = lookup.get((word,"B2"))
        require(e is not None, word+" missing from B2")
        require(set(rec)==ALLOWED_RECORD_FIELDS, word+" hidden/unknown review field")
        require(rec.get("level")=="B2" and rec.get("part_of_speech")==e.get("part_of_speech")==EXPECTED[word]["pos"], word+" POS/level drift")
        require(rec.get("shortlist_snapshot")=={
            "english_definition":e["english_definition"],
            "myanmar_meaning":e["burmese_meaning"],
            "example_sentence":e["example_sentence"]}, word+" bilingual/example snapshot drift")
        provenance = {"source_path":e["source_path"],"source_index":e["source_index"],
                      "source_blob_sha":e["source_blob_sha"]}
        require(rec.get("shortlist_provenance")==provenance, word+" source provenance drift")
        require(e.get("source_path")=="draft/A2-C1-EDITORIAL-STARTER.json", word+" unexpected source path")
        source_bytes = (ROOT / e["source_path"]).read_bytes()
        require(git_blob_sha(source_bytes)==e["source_blob_sha"], word+" source Git blob drift")
        source = json.loads(source_bytes)["entries"][e["source_index"]]
        require(all(source.get(k)==e.get(k) for k in
                    ("word","part_of_speech","english_definition","burmese_meaning","example_sentence")), word+" original source drift")
        require(rec.get("publisher_source")==EXPECTED[word]["pub"], word+" publisher metadata/locator drift")
        require(rec.get("editorial_risk")==EXPECTED[word]["risk"], word+" risk tag drift")
        task=rec.get("independent_reviewer_task")
        require(isinstance(task,str) and word in task and "Human-independent reviewer:" in task
                and "content hash" in task and "reviewer identity" in task, word+" independent task missing")
        require(rec.get("editorial_hold") is True and rec.get("independently_reviewed") is False
                and rec.get("release_approved") is False and rec.get("independent_reviewer_receipt") is None,
                word+" fake approval")
        require(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),
                word+" shortlist hold flags changed")
    return sum(EXPECTED[w]["pub"]["source_cefr_level"] != "B2" for w in EXPECTED)

def negative_tests(packet,shortlist,sha):
    cases=[]
    for i,r in enumerate(packet["records"]):
        for name,mutate in (
            ("english",lambda x: x["shortlist_snapshot"].__setitem__("english_definition","FORGED")),
            ("myanmar",lambda x: x["shortlist_snapshot"].__setitem__("myanmar_meaning","FORGED")),
            ("example",lambda x: x["shortlist_snapshot"].__setitem__("example_sentence","FORGED")),
            ("url",lambda x: x["publisher_source"].__setitem__("url","https://example.org/forged")),
            ("line",lambda x: x["publisher_source"].__setitem__("extracted_line",999999)),
            ("level",lambda x: x["publisher_source"].__setitem__("source_cefr_level","A1")),
            ("risk",lambda x: x.__setitem__("editorial_risk","UNFLAGGED")),
            ("approval",lambda x: x.__setitem__("release_approved",True)),
            ("receipt",lambda x: x.__setitem__("independent_reviewer_receipt",{"result":"PASS"})),
            ("hidden",lambda x: x.__setitem__("reviewed_by","AI"))):
            p=copy.deepcopy(packet)
            mutate(p["records"][i])
            cases.append((name+"-"+r["word"],p,shortlist,sha))
    for field,value in (
        ("record_count",25),("word_pos_discrepancies",0),
        ("lower_level_observations",0),("higher_level_observations",0),
        ("not_found_in_inspected_core_lists",0),("independently_approved_count",1),
        ("status","APPROVED"),("observed_on","2099-01-01")):
        p=copy.deepcopy(packet);p[field]=value;cases.append(("meta-"+field,p,shortlist,sha))
    bad=copy.deepcopy(shortlist);bad["independently_approved_by_level"]["B2"]=1
    cases.append(("fake-shortlist-approval",packet,bad,sha))
    rejected=0
    for label,p,s,h in cases:
        try:
            audit(p,s,h)
        except (ValueError,KeyError,TypeError,IndexError):
            rejected+=1
        else:
            raise AssertionError("FAIL OPEN: "+label)
    return rejected,len(cases)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    raw=SHORTLIST.read_bytes()
    shortlist=json.loads(raw)
    packet=json.loads(PACKET.read_text("utf8"))
    issues=audit(packet,shortlist,git_blob_sha(raw),args.level)
    print(f"Oxford B2 fourth 24: PASS level={args.level}; 24 direct source-list observations, {issues} mismatches/unlisted, 0 independent approvals")
    if args.self_test:
        rejected,total=negative_tests(packet,shortlist,git_blob_sha(raw))
        print(f"Oxford B2 fourth 24: {rejected}/{total} forged-source, bilingual, and fake-review mutations rejected")

if __name__=="__main__":
    main()
