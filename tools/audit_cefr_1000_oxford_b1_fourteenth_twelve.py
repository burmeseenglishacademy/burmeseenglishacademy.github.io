#!/usr/bin/env python3
"""Fail-closed source/provenance audit: 12 B1 draft Oxford observations, NOT approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_PATH = "draft/CEFR-1000-OXFORD-B1-FOURTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORTLIST_PATH = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "9b8b9780bd77d3356b83c88d32979a1378be0f66"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''[["brand","B1",7,1863,"brand n., v."],["cent","A1",1,135,"cent n."],["count","A2",4,1087,"count v."],["fourth","A1",2,311,"fourth number"],["mental","B1",9,2212,"mental adj."],["mostly","A2",6,1405,"mostly adv."],["owner","A2",6,1446,"owner n."],["previously","B1",9,2318,"previously adv."],["realize","A2",6,1529,"realize v."],["click","B1",7,1899,"click v., n."],["faith","B2",11,2849,"faith n."],["fashion","A2",5,1201,"fashion n."]]''')
SENSES = json.loads(r'''{"brand":["https://www.oxfordlearnersdictionaries.com/definition/english/brand_1",1,105,124],"fourth":["https://www.oxfordlearnersdictionaries.com/definition/english/fourth_1",1,88,113],"realize":["https://www.oxfordlearnersdictionaries.com/definition/english/realize",1,107,132],"faith":["https://www.oxfordlearnersdictionaries.com/definition/english/faith_1",1,105,114]}''')
ROOT_KEYS = {"schema","scope","status","observed_on","shortlist_blob_sha","record_count","counts_by_level","publisher_reference_level_counts","word_pos_discrepancies","direct_dictionary_sense_leads","independently_approved_count","source_limitations","records"}
ROW_KEYS = {"word","level","part_of_speech","shortlist_snapshot","shortlist_provenance","publisher_source","editorial_risk","independent_reviewer_task","editorial_hold","independently_reviewed","release_approved","independent_reviewer_receipt"}
SOURCE_KEYS = {"publisher","title","url","observed_on","pdf_page","extracted_line","source_excerpt","source_cefr_level","evidence_scope","access"}
SENSE_KEYS = {"url","sense_number","page_text_line_start","page_text_line_end","observed_on","evidence_scope","sense_summary"}
CANDIDATE_KEYS = {"myanmar_meaning","original_example","review_status"}

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def audit(packet, shortlist):
    require(set(packet) == ROOT_KEYS, "Unexpected or missing packet root field")
    require(packet["schema"] == 1 and packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet["status"] == "B1_FOURTEENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and packet["observed_on"] == "2026-10-31" and packet["shortlist_blob_sha"] == SHORTLIST_SHA,
            "Research packet scope/date/source changed")
    require(packet["record_count"] == 12
            and packet["counts_by_level"] == dict(zip(LEVELS, (0,0,12,0,0)))
            and packet["publisher_reference_level_counts"] == dict(zip(LEVELS, (2,5,4,1,0)))
            and packet["word_pos_discrepancies"] == 8
            and packet["direct_dictionary_sense_leads"] == 4
            and packet["independently_approved_count"] == 0
            and "not independent exact-sense cefr approval" in packet["source_limitations"].lower()
            and "ordinal number" in packet["source_limitations"].lower(),
            "Source count, disclaimer or no-approval gate changed")
    require(len(shortlist["entries"]) == 1000
            and shortlist["counts_by_level"] == dict.fromkeys(LEVELS,200)
            and shortlist["independently_approved_by_level"] == dict.fromkeys(LEVELS,0)
            and shortlist["release_status"] == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
            "Frozen 1000 and zero approval contract changed")
    byword = {r["word"]:r for r in shortlist["entries"]}
    require(len(byword) == 1000 and all(
            r.get("editorial_hold") is True and r.get("release_approved") is False
            and all(r.get(k) is False for k in
                ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation"))
            for r in shortlist["entries"]), "Shortlist duplicate/forged approval")
    rows=packet["records"]
    require(isinstance(rows,list) and len(rows)==12 and len({r["word"] for r in rows})==12,
            "Twelve distinct source observations required")
    for row,(word,cefr,page,line,excerpt) in zip(rows,EXPECTED):
        require(set(row)==ROW_KEYS | ({"dictionary_sense_lead","editorial_rewrite_candidate"} if word in SENSES else set()),
                "Record keys drift for "+word)
        original=byword[word]
        require(original["level"]=="B1" and row["word"]==word and row["level"]=="B1"
                and row["part_of_speech"]==original["part_of_speech"], "Word/POS drift for "+word)
        require(row["shortlist_snapshot"] == {
                "english_definition":original["english_definition"],
                "myanmar_meaning":original["burmese_meaning"],
                "example_sentence":original["example_sentence"]}, "Bilingual/example drift for "+word)
        require(row["shortlist_provenance"] == {k:original[k] for k in
                ("source_path","source_index","source_blob_sha")}, "Historical Git provenance drift for "+word)
        require(row["publisher_source"] == {
                "publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level",
                "url":PDF,"observed_on":"2026-10-31","pdf_page":page,
                "extracted_line":line,"source_excerpt":excerpt,"source_cefr_level":cefr,
                "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher word/POS/source locator drift for "+word)
        require(row["editorial_hold"] is True and row["independently_reviewed"] is False
                and row["release_approved"] is False and row["independent_reviewer_receipt"] is None
                and isinstance(row["editorial_risk"],str) and len(row["editorial_risk"])>30
                and isinstance(row["independent_reviewer_task"],str)
                and "Independent human" in row["independent_reviewer_task"],
                "Editorial hold or human-review contract drift for "+word)
        if word=="fourth":
            require(original["part_of_speech"]=="ordinal adjective"
                    and excerpt=="fourth number" and "POS" in row["editorial_risk"],
                    "Fourth ordinal-number vs adjective conflict was hidden")
        if word in SENSES:
            url,num,start,end=SENSES[word]
            lead=row["dictionary_sense_lead"]
            require(set(lead)==SENSE_KEYS and lead["url"]==url
                    and lead["sense_number"]==num and lead["page_text_line_start"]==start
                    and lead["page_text_line_end"]==end and lead["observed_on"]=="2026-10-31"
                    and lead["evidence_scope"]=="DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and isinstance(lead["sense_summary"],str) and len(lead["sense_summary"])>40,
                    "Direct dictionary sense locator drift for "+word)
            cand=row["editorial_rewrite_candidate"]
            require(set(cand)==CANDIDATE_KEYS
                    and cand["review_status"]=="UNAPPROVED_EDITORIAL_PROPOSAL"
                    and isinstance(cand["myanmar_meaning"],str) and len(cand["myanmar_meaning"])>12
                    and isinstance(cand["original_example"],str)
                    and len(cand["original_example"])>25
                    and (word.lower() in cand["original_example"].lower()
                         or (word=="realize" and "realise" in cand["original_example"].lower())),
                    "Unapproved Myanmar/example proposal corrupted for "+word)
    return {"observed_B1":12,"publisher_levels":packet["publisher_reference_level_counts"],
            "word_pos_discrepancies":8,"sense_leads":4,"independently_approved":0,
            "release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    cases=0
    for i,row in enumerate(packet["records"]):
        def reject(mut, label):
            nonlocal cases
            changed=copy.deepcopy(packet)
            mut(changed["records"][i])
            try:
                audit(changed,shortlist)
            except (ValueError,KeyError,TypeError,IndexError):
                cases+=1
            else:
                raise AssertionError("Forged "+label+" accepted for "+row["word"])
        for key,value in (
            ("word","forged"),("level","C1"),("part_of_speech","forged"),
            ("editorial_hold",False),("independently_reviewed",True),
            ("release_approved",True),("independent_reviewer_receipt",{"forged":True}),
            ("editorial_risk",""),("independent_reviewer_task","self approved"),
            ("unknown_field","fake")):
            reject(lambda r,k=key,v=value:r.update({k:v}),key)
        for key,value in (
            ("url","https://example.invalid"),("publisher","Unknown"),
            ("source_cefr_level","C1"),("pdf_page",0),("extracted_line",-1),
            ("source_excerpt","forged n."),("observed_on","2026-11-01"),
            ("evidence_scope","INDEPENDENT_CEFR_APPROVED")):
            reject(lambda r,k=key,v=value:r["publisher_source"].update({k:v}),"source "+key)
        for key,value in (
            ("english_definition","Forged English"),("myanmar_meaning","အမှား"),
            ("example_sentence","Forged example")):
            reject(lambda r,k=key,v=value:r["shortlist_snapshot"].update({k:v}),"snapshot "+key)
        for key,value in (("source_path","draft/fake.json"),("source_index",-1),
                          ("source_blob_sha","0"*40)):
            reject(lambda r,k=key,v=value:r["shortlist_provenance"].update({k:v}),"provenance "+key)
        if row["word"] in SENSES:
            for key,value in (("url","https://example.invalid"),("sense_number",999),
                    ("page_text_line_start",0),("page_text_line_end",0),
                    ("evidence_scope","APPROVED"),("sense_summary","")):
                reject(lambda r,k=key,v=value:r["dictionary_sense_lead"].update({k:v}),"sense "+key)
            for key,value in (("myanmar_meaning",""),("original_example","fake"),
                    ("review_status","APPROVED")):
                reject(lambda r,k=key,v=value:r["editorial_rewrite_candidate"].update({k:v}),"proposal "+key)
    for mut in (
        lambda p:p.update(independently_approved_count=1),
        lambda p:p.update(word_pos_discrepancies=0),
        lambda p:p.update(publisher_reference_level_counts=dict.fromkeys(LEVELS,0)),
        lambda p:p.update(source_limitations="independently approved"),
        lambda p:p["records"].reverse()):
        changed=copy.deepcopy(packet)
        mut(changed)
        try:
            audit(changed,shortlist)
        except (ValueError,KeyError,TypeError,IndexError):
            cases+=1
        else:
            raise AssertionError("Forged packet-level mutation accepted")
    for mut in (
        lambda s:s["entries"][0].update(release_approved=True),
        lambda s:s["entries"][0].update(reviewed_english=True),
        lambda s:s["entries"][0].update(word=s["entries"][1]["word"]),
        lambda s:s["independently_approved_by_level"].update(B1=1)):
        changed=copy.deepcopy(shortlist)
        mut(changed)
        try:
            audit(packet,changed)
        except (ValueError,KeyError,TypeError,IndexError):
            cases+=1
        else:
            raise AssertionError("Forged frozen-shortlist mutation accepted")
    return cases

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=LEVELS+("ALL",),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    require(git_blob_sha(ROOT/PACKET_PATH)==PACKET_SHA, "Pinned Oxford research packet blob changed")
    require(git_blob_sha(ROOT/SHORTLIST_PATH)==SHORTLIST_SHA, "Frozen shortlist blob changed")
    packet=json.loads((ROOT/PACKET_PATH).read_text(encoding="utf-8"))
    shortlist=json.loads((ROOT/SHORTLIST_PATH).read_text(encoding="utf-8"))
    result=audit(packet,shortlist)
    if args.self_test:
        result["forged_mutations_rejected"]=self_test(packet,shortlist)
    result["requested_level"]=args.level
    result["records_for_requested_level"]=12 if args.level in ("B1","ALL") else 0
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    main()
