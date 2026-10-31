#!/usr/bin/env python3
"""Fail-closed B1 thirteenth Oxford evidence audit. Never grants human approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "325a0f83eb841beca98c7ced5ffef1f23c35e3f6"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = (
    ("village", "A1", 4, 849, "village n."),
    ("apply", "A2", 4, 952, "apply v."),
    ("authority", "B1", 7, 1834, "authority n."),
    ("method", "A2", 6, 1395, "method n."),
    ("healthy", "A1", 2, 358, "healthy adj."),
    ("option", "A2", 6, 1437, "option n."),
    ("trouble", "A2", 7, 1726, "trouble n."),
    ("apart", "B1", 7, 1819, "apart adv."),
    ("gift", "A2", 5, 1247, "gift n."),
    ("require", "B1", 9, 2382, "require v."),
    ("wood", "A2", 7, 1770, "wood n."),
    ("background", "A2", 4, 977, "background n."),
)
SENSES = {
    "apply": (1, 110, 129),
    "authority": (2, 150, 160),
    "apart": (1, 107, 112),
    "background": (1, 106, 134),
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet=None, shortlist=None):
    require(git_blob_sha(PACKET) == PACKET_SHA, "Publisher evidence packet blob changed")
    require(git_blob_sha(SHORTLIST) == SHORTLIST_SHA, "Frozen shortlist blob changed")
    p = packet if packet is not None else json.loads(PACKET.read_text(encoding="utf-8"))
    s = shortlist if shortlist is not None else json.loads(SHORTLIST.read_text(encoding="utf-8"))
    require(len(s.get("entries", [])) == 1000, "Expected exactly 1000 first-pass rows")
    require(s.get("counts_by_level") == dict.fromkeys(LEVELS, 200), "200 per level required")
    require(s.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Independent approvals cannot be manufactured")
    by_word = {x["word"]: x for x in s["entries"]}
    require(len(by_word) == 1000, "Duplicate shortlist headwords")
    require(all(x.get("editorial_hold") is True and x.get("release_approved") is False
                and all(x.get(k) is False for k in (
                    "reviewed_english", "reviewed_burmese", "reviewed_example",
                    "reviewed_level", "reviewed_pronunciation")) for x in s["entries"]),
            "Unverified shortlist signoff drift")
    require(p.get("schema") == 1 and p.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and p.get("status") == "B1_THIRTEENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and p.get("observed_on") == "2026-10-31"
            and p.get("shortlist_blob_sha") == SHORTLIST_SHA
            and p.get("record_count") == 12
            and p.get("counts_by_level") == {"A1":0,"A2":0,"B1":12,"B2":0,"C1":0}
            and p.get("publisher_reference_level_counts") == {"A1":2,"A2":7,"B1":3,"B2":0,"C1":0}
            and p.get("word_pos_discrepancies") == 9
            and p.get("direct_dictionary_sense_leads") == 4
            and p.get("independently_approved_count") == 0
            and "not independent exact-sense cefr approval" in p.get("source_limitations","").lower(),
            "Staging evidence scope, counts or limitations changed")
    rows = p.get("records")
    require(isinstance(rows,list) and len(rows)==12, "Twelve source-bound records required")
    for row,(word,cefr,page,line,excerpt) in zip(rows,EXPECTED):
        e=by_word[word]
        require(e["level"]=="B1" and row.get("word")==word and row.get("level")=="B1"
                and row.get("part_of_speech")==e["part_of_speech"],
                "Word, level or POS mismatch: "+word)
        require(row.get("shortlist_snapshot")=={
                    "english_definition":e["english_definition"],
                    "myanmar_meaning":e["burmese_meaning"],
                    "example_sentence":e["example_sentence"]},
                "Bilingual/grammar source snapshot changed: "+word)
        require(row.get("shortlist_provenance")=={
                    k:e[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical Git provenance changed: "+word)
        require(row.get("publisher_source")=={
                    "publisher":"Oxford University Press",
                    "title":"The Oxford 3000 by CEFR level",
                    "url":PDF,
                    "observed_on":"2026-10-31",
                    "pdf_page":page,
                    "extracted_line":line,
                    "source_excerpt":excerpt,
                    "source_cefr_level":cefr,
                    "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                    "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Source CEFR, locator or provenance mismatch: "+word)
        require(len(row.get("editorial_risk",""))>=45
                and "Independent human editor" in row.get("independent_reviewer_task",""),
                "Missing human exact-sense and bilingual review instruction: "+word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "False review or release signoff: "+word)
        lead=row.get("dictionary_sense_lead")
        proposal=row.get("editorial_rewrite_candidate")
        if word in SENSES:
            sense,first,last=SENSES[word]
            require(isinstance(lead,dict)
                    and lead.get("url")==f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
                    and lead.get("sense_number")==sense
                    and lead.get("page_text_line_start")==first
                    and lead.get("page_text_line_end")==last
                    and lead.get("observed_on")=="2026-10-31"
                    and lead.get("evidence_scope")=="DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and len(lead.get("sense_summary",""))>35,
                    "Dictionary sense attribution invalid: "+word)
            require(isinstance(proposal,dict)
                    and len(proposal.get("myanmar_meaning",""))>=10
                    and len(proposal.get("original_example",""))>=20
                    and proposal.get("review_status")=="UNAPPROVED_EDITORIAL_PROPOSAL",
                    "Self-authored alternative cannot be approved: "+word)
        else:
            require(lead is None and proposal is None,
                    "Unobserved dictionary sense or rewrite claimed: "+word)
    return True

def self_test():
    truth=json.loads(PACKET.read_text(encoding="utf-8"))
    tests=0
    for i in range(12):
        for path,value in (
            (("word",),"forged"),
            (("publisher_source","source_cefr_level"),"C1"),
            (("publisher_source","pdf_page"),99),
            (("publisher_source","extracted_line"),-1),
            (("publisher_source","source_excerpt"),"forged source"),
            (("shortlist_snapshot","myanmar_meaning"),"fabricated"),
            (("shortlist_provenance","source_blob_sha"),"forged"),
            (("editorial_hold",),False),
            (("independently_reviewed",),True),
            (("release_approved",),True),
            (("independent_reviewer_receipt",),{"fake":"yes"}),
        ):
            mutated=copy.deepcopy(truth)
            target=mutated["records"][i]
            for k in path[:-1]: target=target[k]
            target[path[-1]]=value
            try: audit(mutated)
            except (ValueError,KeyError,TypeError): tests+=1
            else: raise AssertionError("Forged publisher or signoff mutation escaped")
        if truth["records"][i].get("dictionary_sense_lead"):
            for path,value in (
                (("dictionary_sense_lead","sense_number"),99),
                (("dictionary_sense_lead","url"),"https://invalid.example/"),
                (("editorial_rewrite_candidate","review_status"),"APPROVED"),
            ):
                mutated=copy.deepcopy(truth)
                target=mutated["records"][i]
                for k in path[:-1]:target=target[k]
                target[path[-1]]=value
                try: audit(mutated)
                except (ValueError,KeyError,TypeError):tests+=1
                else:raise AssertionError("Forged sense or proposal mutation escaped")
    print(f"PASS: {tests}/{tests} B1 thirteenth adversarial source, Myanmar, provenance and false-signoff mutations rejected")
    return tests

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=[*LEVELS,"ALL"],default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    audit()
    if args.self_test:self_test()
    print(f"PASS: B1 thirteenth source-bound staging audit ({args.level}); 12 word/POS observations, four sense leads, 0 independently approved; NEVER DEPLOY")

if __name__=="__main__":
    main()
