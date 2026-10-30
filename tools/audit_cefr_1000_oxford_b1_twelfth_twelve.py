#!/usr/bin/env python3
"""Fail-closed B1 twelfth Oxford publisher research; NO independent review or deployment."""
import argparse, copy, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/"draft/CEFR-1000-OXFORD-B1-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORT=ROOT/"draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA="c2ecb9827a7cbd679d4f4debba55f3bafbcb9cc4"
SHORT_SHA="475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS=("A1","A2","B1","B2","C1")
EXPECTED=[["achieve","A2",4,915,"achieve v.","3000"],["afford","B1",7,1796,"afford v.","3000"],["category","B1",7,1878,"category n.","3000"],["relevant","B2",12,3131,"relevant adj.","3000"],["fresh","A2",5,1235,"fresh adj.","3000"],["scale","B2",12,3162,"scale n.","3000"],["score","A2",6,1587,"score v., n.","3000"],["smart","B1",9,2446,"smart adj.","3000"],["throw","A2",7,1705,"throw v.","3000"],["wedding","A2",7,1757,"wedding n.","3000"],["feature","A2",5,1204,"feature n.","3000"],["target","A2",7,1690,"target n.","3000"]]
BASE="https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/"
LEADS={"afford":["https://www.oxfordlearnersdictionaries.com/definition/english/afford",1,112,125],"fresh":["https://www.oxfordlearnersdictionaries.com/definition/english/fresh_1",1,108,125],"scale":["https://www.oxfordlearnersdictionaries.com/definition/english/scale_1",1,106,119],"target":["https://www.oxfordlearnersdictionaries.com/definition/english/target_1",1,105,115]}
def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+bytes([0])+b).hexdigest()
def need(ok,msg):
    if not ok: raise ValueError(msg)
def audit(doc=None,shortlist=None):
    need(blob(PACKET)==PACKET_SHA and blob(SHORT)==SHORT_SHA,"Frozen packet/shortlist Git blob changed")
    truth=json.loads(PACKET.read_text("utf-8"))
    p=doc if doc is not None else truth
    need(p==truth,"Source packet changed or fabricated signoff")
    s=shortlist if shortlist is not None else json.loads(SHORT.read_text("utf-8"))
    need(s.get("counts_by_level")==dict.fromkeys(LEVELS,200) and s.get("independently_approved_by_level")==dict.fromkeys(LEVELS,0) and len(s.get("entries",[]))==1000,"Shortlist count/approval drift")
    by={e["word"]:e for e in s["entries"]}
    need(len(by)==1000,"Duplicate shortlist headword")
    need(p.get("schema")==1 and p.get("scope")=="CEFR_1000_TOTAL_STAGING_ONLY" and p.get("status")=="B1_TWELFTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD" and p.get("observed_on")=="2026-10-31" and p.get("shortlist_blob_sha")==SHORT_SHA and p.get("record_count")==12 and p.get("counts_by_level")==dict(zip(LEVELS,(0,0,12,0,0))) and p.get("publisher_reference_level_counts")=={"A2":7,"B1":3,"B2":2} and p.get("word_pos_discrepancies")==9 and p.get("direct_dictionary_sense_leads")==4 and p.get("independently_approved_count")==0,"Research metadata drift")
    need("NOT independent exact-sense" in p.get("source_limitations","") or "NOT independent exact-sense" in p.get("source_limitations","").replace("NOT independent exact-sense CEFR classification","NOT independent exact-sense"),"Publisher limitation removed")
    rows=p.get("records")
    need(isinstance(rows,list) and len(rows)==12,"Twelve source records required")
    for row,(word,cefr,page,line,excerpt,docname) in zip(rows,EXPECTED):
        e=by.get(word)
        need(e is not None and e.get("level")=="B1" and row.get("word")==word and row.get("level")=="B1" and row.get("part_of_speech")==e.get("part_of_speech"),"Headword/POS mismatch: "+word)
        need(row.get("shortlist_snapshot")=={k:e[k] for k in ("english_definition","myanmar_meaning","example_sentence")},"Bilingual/example snapshot mismatch: "+word)
        need(row.get("shortlist_provenance")=={k:e[k] for k in ("source_path","source_index","source_blob_sha")},"Historical Git provenance mismatch: "+word)
        need(row.get("publisher_source")=={"publisher":"Oxford University Press","title":"The Oxford "+docname+" by CEFR level","url":BASE+"The_Oxford_"+docname+"_by_CEFR_level.pdf","observed_on":"2026-10-31","pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,"source_cefr_level":cefr,"evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"Publisher evidence mismatch: "+word)
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False and row.get("release_approved") is False and row.get("independent_reviewer_receipt") is None and e.get("editorial_hold") is True and e.get("release_approved") is False,"Forged independent review: "+word)
        need(len(row.get("editorial_risk",""))>40 and "Independent human editor" in row.get("independent_reviewer_task",""),"Sense risk/reviewer handoff absent: "+word)
        lead=row.get("dictionary_sense_lead")
        candidate=row.get("editorial_rewrite_candidate")
        if word in LEADS:
            url,sense,start,end=LEADS[word]
            need(isinstance(lead,dict) and lead.get("url")==url and lead.get("sense_number")==sense and lead.get("page_text_line_start")==start and lead.get("page_text_line_end")==end and lead.get("observed_on")=="2026-10-31" and lead.get("evidence_scope")=="DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF" and len(lead.get("editorial_interpretation",""))>40,"Dictionary sense lead mismatch: "+word)
            need(isinstance(candidate,dict) and candidate.get("status")=="UNAPPROVED_EDITORIAL_PROPOSAL_NOT_APPLIED" and len(candidate.get("myanmar_meaning",""))>10 and len(candidate.get("original_example_sentence",""))>20,"Unapproved alternative mismatch: "+word)
        else:
            need(lead is None and candidate is None,"Invented dictionary sense lead: "+word)
    return True
def self_test():
    original=json.loads(PACKET.read_text("utf-8"))
    changes=[
        (("publisher_source","source_cefr_level"),"C1"),
        (("publisher_source","url"),"https://example.invalid/forged.pdf"),
        (("publisher_source","observed_on"),"2026-11-01"),
        (("publisher_source","pdf_page"),999),
        (("publisher_source","extracted_line"),9999),
        (("publisher_source","source_excerpt"),"fabricated entry"),
        (("publisher_source","evidence_scope"),"INDEPENDENT_EXACT_SENSE_APPROVAL"),
        (("shortlist_snapshot","burmese_meaning"),"အမှား"),
        (("shortlist_snapshot","example_sentence"),"Forged example."),
        (("shortlist_provenance","source_blob_sha"),"0"*40),
        (("editorial_risk",),"No risk"),
        (("independently_reviewed",),True),
        (("release_approved",),True),
        (("editorial_hold",),False),
        (("independent_reviewer_receipt",),{"reviewer":"bot"}),
    ]
    n=0
    for i in range(12):
        for path,value in changes:
            forged=copy.deepcopy(original)
            obj=forged["records"][i]
            for key in path[:-1]: obj=obj[key]
            obj[path[-1]]=value
            try: audit(forged)
            except ValueError: n+=1; continue
            raise AssertionError("Forged source/review accepted: "+str((i,path)))
    return n
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    audit()
    n=self_test() if args.self_test else 0
    if args.self_test: print(f"PASS: {n}/{n} forged publisher, bilingual, provenance and independent-review mutations rejected")
    print(f"PASS: {args.level} 12 B1 draft Oxford word/POS observations; 7 A2, 3 B1, 2 B2; four direct sense leads; 0 independent approvals; NO DEPLOY")
if __name__=="__main__": main()
