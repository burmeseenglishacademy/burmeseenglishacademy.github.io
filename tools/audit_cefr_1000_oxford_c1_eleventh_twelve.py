#!/usr/bin/env python3
"""Fail-closed C1 eleventh Oxford source/sense research audit. NEVER human approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-C1-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "df1846febb375e1ca1a899131e4087acb9e70cc2"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF_BASE = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_"
EXPECTED = (
    ("harassment","C1",5000,5,1277,"harassment n."),
    ("commentary","C1",5000,4,924,"commentary n."),
    ("classification","C1",5000,4,906,"classification n."),
    ("congressional","C1",5000,4,961,"congressional adj."),
    ("partially","C1",5000,6,1559,"partially adv."),
    ("precedent","C1",5000,6,1593,"precedent n."),
    ("socialist","C1",5000,7,1790,"socialist adj."),
    ("solely","C1",5000,7,1792,"solely adv."),
    ("striking","C1",5000,7,1833,"striking adj."),
    ("acknowledge","B2",3000,10,2601,"acknowledge v."),
    ("adopt","B2",3000,10,2608,"adopt v."),
    ("qualify","B1",3000,9,2344,"qualify v."),
)
LEAD_URLS = {
    "qualify": "https://www.oxfordlearnersdictionaries.com/definition/english/qualify",
    "precedent": "https://www.oxfordlearnersdictionaries.com/definition/english/precedent",
    "commentary": "https://www.oxfordlearnersdictionaries.com/definition/english/commentary",
    "harassment": "https://www.oxfordlearnersdictionaries.com/definition/english/harassment",
}

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def blob_sha(path):
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def audit(packet=None, verify_blob=True):
    if verify_blob:
        require(blob_sha(PACKET) == PACKET_BLOB, "Immutable publisher packet blob changed")
    require(blob_sha(SHORTLIST) == SHORTLIST_BLOB, "Frozen shortlist blob changed")
    data = packet if packet is not None else json.loads(PACKET.read_text("utf8"))
    original = json.loads(SHORTLIST.read_text("utf8"))
    by_word = {r["word"]: r for r in original["entries"]}
    require(original["counts_by_level"] == {x:200 for x in ("A1","A2","B1","B2","C1")},
            "Approved 200-per-level quota changed")
    require(original["independently_approved_by_level"] == {x:0 for x in ("A1","A2","B1","B2","C1")},
            "False independent approvals in shortlist")
    require(data.get("schema") == 1 and data.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and data.get("status") == "C1_ELEVENTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
            and data.get("observed_on") == "2026-10-30"
            and data.get("shortlist_blob_sha") == SHORTLIST_BLOB
            and data.get("record_count") == 12
            and data.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":0,"C1":12}
            and data.get("publisher_reference_level_counts") == {"B1":1,"B2":2,"C1":9}
            and data.get("word_pos_discrepancies") == 3,
            "Scope, source totals, observation date or publisher counts drift")
    require(data.get("independently_approved_count") == 0
            and data.get("independent_human_review_receipts") == []
            and data.get("audio_real_listening_signoffs") == []
            and data.get("release_approved") is False,
            "Fabricated approval or listening evidence")
    records = data.get("records")
    require(isinstance(records,list) and len(records)==12, "Twelve research records required")
    require([r.get("word") for r in records] == [e[0] for e in EXPECTED],
            "Research words or order changed")
    for r,(word,level,list_id,page,line,excerpt) in zip(records,EXPECTED):
        original_row = by_word[word]
        require(r.get("level") == "C1" and r.get("part_of_speech") == original_row["part_of_speech"],
                "Frozen level or POS mismatch: "+word)
        require(r.get("shortlist_snapshot") == {
            "english_definition":original_row["english_definition"],
            "myanmar_meaning":original_row["burmese_meaning"],
            "example_sentence":original_row["example_sentence"]},
            "English/Myanmar/example snapshot drift: "+word)
        require(r.get("shortlist_provenance") == {
            "source_path":original_row["source_path"],
            "source_index":original_row["source_index"],
            "source_blob_sha":original_row["source_blob_sha"]},
            "Historical Git provenance drift: "+word)
        pub = r.get("publisher_source")
        require(isinstance(pub,dict) and pub == {
            "publisher":"Oxford University Press",
            "title":f"The Oxford {list_id} by CEFR level",
            "url":f"{PDF_BASE}{list_id}_by_CEFR_level.pdf",
            "observed_on":"2026-10-30",
            "pdf_page":page,
            "extracted_line":line,
            "source_excerpt":excerpt,
            "source_cefr_level":level,
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
            "Publisher level, PDF locator or exact source excerpt drift: "+word)
        require(isinstance(r.get("editorial_risk"),str) and len(r["editorial_risk"])>35
                and isinstance(r.get("independent_reviewer_task"),str)
                and "Independent human" in r["independent_reviewer_task"]
                and r.get("editorial_hold") is True
                and r.get("independently_reviewed") is False
                and r.get("release_approved") is False
                and r.get("independent_reviewer_receipt") is None,
                "Missing editorial hold or fabricated human review: "+word)
    leads = data.get("direct_dictionary_sense_leads")
    require(isinstance(leads,list) and len(leads)==4
            and {r.get("word"):r.get("url") for r in leads} == LEAD_URLS,
            "Four directly opened publisher dictionary leads required")
    for r in leads:
        require(r.get("observed_on")=="2026-10-30"
                and r.get("scope")=="DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"
                and type(r.get("sense_number")) is int and r["sense_number"]>0
                and isinstance(r.get("lines"),list) and len(r["lines"])==2
                and all(type(n) is int and n>0 for n in r["lines"])
                and r["lines"][0] < r["lines"][1]
                and isinstance(r.get("interpretation"),str) and len(r["interpretation"])>35
                and r.get("part_of_speech")==by_word[r["word"]]["part_of_speech"],
                "Direct sense observation incomplete or forged")
    proposals = data.get("unapproved_editorial_suggestions")
    require(isinstance(proposals,list) and len(proposals)==4
            and {r.get("word") for r in proposals}==set(LEAD_URLS),
            "Four distinct held bilingual proposals required")
    for r in proposals:
        require(r.get("status")=="EDITORIAL_PROPOSAL_NOT_INDEPENDENTLY_REVIEWED"
                and isinstance(r.get("proposed_myanmar"),str)
                and any("\u1000" <= ch <= "\u109f" for ch in r["proposed_myanmar"])
                and isinstance(r.get("proposed_example"),str)
                and len(r["proposed_example"])>25,
                "False proposal approval or missing bilingual/example content")
    return {"direct_oxford_word_pos":12,"publisher_levels":{"B1":1,"B2":2,"C1":9},
            "dictionary_sense_leads":4,"independently_approved":0}

def self_test():
    base = json.loads(PACKET.read_text("utf8"))
    count=0
    def reject(label,change):
        nonlocal count
        altered=copy.deepcopy(base)
        change(altered)
        try:
            audit(altered,verify_blob=False)
        except ValueError:
            count+=1
            return
        raise AssertionError("Forged evidence accepted: "+label)
    for i in range(12):
        reject("publisher CEFR",lambda d,i=i:d["records"][i]["publisher_source"].update(source_cefr_level="C2"))
        reject("publisher line",lambda d,i=i:d["records"][i]["publisher_source"].update(extracted_line=0))
        reject("publisher access",lambda d,i=i:d["records"][i]["publisher_source"].update(access="SEARCH_SNIPPET"))
        reject("publisher excerpt",lambda d,i=i:d["records"][i]["publisher_source"].update(source_excerpt="invented"))
        reject("Myanmar snapshot",lambda d,i=i:d["records"][i]["shortlist_snapshot"].update(myanmar_meaning="အမှား"))
        reject("English snapshot",lambda d,i=i:d["records"][i]["shortlist_snapshot"].update(english_definition="wrong"))
        reject("example snapshot",lambda d,i=i:d["records"][i]["shortlist_snapshot"].update(example_sentence="Wrong."))
        reject("source index",lambda d,i=i:d["records"][i]["shortlist_provenance"].update(source_index=-1))
        reject("human review",lambda d,i=i:d["records"][i].update(independently_reviewed=True))
        reject("release",lambda d,i=i:d["records"][i].update(release_approved=True))
    reject("independent count",lambda d:d.update(independently_approved_count=12))
    reject("fake listening",lambda d:d.update(audio_real_listening_signoffs=[{"fake":True}]))
    reject("fake dictionary lead",lambda d:d["direct_dictionary_sense_leads"][0].update(scope="INDEPENDENT_APPROVED"))
    reject("fake proposal",lambda d:d["unapproved_editorial_suggestions"][0].update(status="APPROVED"))
    return count

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=("A1","A2","B1","B2","C1","ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    report=audit()
    print("PASS: C1 eleventh twelve source-bound Oxford word/POS leads, 4 dictionary sense leads, 0 independent approvals; level",args.level,report)
    if args.self_test:
        print("PASS:",self_test(),"/",124,"adversarial publisher, bilingual, provenance and signoff mutations rejected")
if __name__=="__main__":
    main()
