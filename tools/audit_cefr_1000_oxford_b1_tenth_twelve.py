#!/usr/bin/env python3
"""B1 tenth source-bound Oxford PDF/sense research integrity; no human approval."""
import argparse, copy, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/"draft/CEFR-1000-OXFORD-B1-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT=ROOT/"draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA="1b045c2edb8cad47c9ae0d407fdaafb052bc309c"
SHORT_SHA="475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_URL="https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS=("A1","A2","B1","B2","C1")
EXPECTED=[["traditional","A2",7,1720,"traditional adj."],["worry","A2",7,1774,"worry v."],["benefit","B1",7,1854,"benefit v."],["budget","B2",10,2670,"budget n."],["generation","B1",8,2091,"generation n."],["therefore","B1",10,2505,"therefore adv."],["division","B2",11,2797,"division n."],["actual","B2",10,2603,"actual adj."],["northern","B1",9,2240,"northern adj."],["screen","A2",6,1588,"screen n."],["engine","A2",5,1167,"engine n."],["critical","B2",10,2746,"critical adj."]]
LEADS={"benefit":["https://www.oxfordlearnersdictionaries.com/definition/english/benefit_2",1,114,118],"budget":["https://www.oxfordlearnersdictionaries.com/definition/english/budget_1",1,103,119],"generation":["https://www.oxfordlearnersdictionaries.com/definition/english/generation",1,103,120],"critical":["https://www.oxfordlearnersdictionaries.com/definition/english/critical",2,141,151]}

def need(condition, reason):
    if not condition: raise ValueError(reason)

def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+bytes([0])+b).hexdigest()

def audit(packet, shortlist):
    need(blob(PACKET)==PACKET_SHA and blob(SHORT)==SHORT_SHA, "Frozen packet/shortlist blob changed")
    need(packet.get("schema")==1 and packet.get("scope")=="CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status")=="B1_TENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
         and packet.get("observed_on")=="2026-10-30" and packet.get("shortlist_blob_sha")==SHORT_SHA
         and packet.get("record_count")==12 and packet.get("counts_by_level")=={"A1":0,"A2":0,"B1":12,"B2":0,"C1":0}
         and packet.get("publisher_reference_level_counts")=={"A2":4,"B1":4,"B2":4}
         and packet.get("word_pos_discrepancies")==8 and packet.get("direct_dictionary_sense_leads")==4
         and packet.get("independently_approved_count")==0, "Source counts/scope/approval drift")
    need(shortlist.get("counts_by_level")==dict.fromkeys(LEVELS,200)
         and shortlist.get("independently_approved_by_level")==dict.fromkeys(LEVELS,0)
         and len(shortlist.get("entries",[]))==1000, "Frozen 200-per-level quota or false approval")
    byword={r["word"]:r for r in shortlist["entries"]}
    need(len(byword)==1000, "Duplicate shortlist headword")
    rows=packet.get("records")
    need(isinstance(rows,list) and len(rows)==12, "Missing source observations")
    for row,(word,cefr,page,line,excerpt) in zip(rows,EXPECTED):
        source=byword.get(word)
        need(source is not None and source["level"]=="B1"
             and row.get("word")==word and row.get("level")=="B1"
             and row.get("part_of_speech")==source["part_of_speech"], "Word/POS mismatch: "+word)
        need(row.get("shortlist_snapshot")=={"english_definition":source["english_definition"],
             "myanmar_meaning":source["burmese_meaning"],"example_sentence":source["example_sentence"]},
             "Frozen bilingual/example snapshot changed: "+word)
        need(row.get("shortlist_provenance")=={k:source[k] for k in
             ("source_path","source_index","source_blob_sha")}, "Historical Git provenance changed: "+word)
        need(row.get("publisher_source")=={"publisher":"Oxford University Press",
             "title":"The Oxford 3000 by CEFR level","url":SOURCE_URL,"observed_on":"2026-10-30",
             "pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,
             "source_cefr_level":cefr,"evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher PDF evidence changed: "+word)
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
             and row.get("release_approved") is False and row.get("independent_reviewer_receipt") is None
             and source["editorial_hold"] is True and source["release_approved"] is False,
             "Forged review, listening or release receipt: "+word)
        need(isinstance(row.get("editorial_risk"),str) and len(row["editorial_risk"])>40
             and "Independent human reviewer" in row.get("independent_reviewer_task",""),
             "Missing exact-sense human review task: "+word)
        lead=row.get("dictionary_sense_lead")
        suggestion=row.get("editorial_rewrite_candidate")
        if word in LEADS:
            u,s,a,b=LEADS[word]
            need(isinstance(lead,dict) and lead.get("url")==u and lead.get("sense_number")==s
                 and lead.get("page_text_line_start")==a and lead.get("page_text_line_end")==b
                 and lead.get("observed_on")=="2026-10-30"
                 and lead.get("evidence_scope")=="DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"
                 and len(lead.get("editorial_interpretation",""))>35,
                 "Direct dictionary sense lead changed: "+word)
            need(isinstance(suggestion,dict)
                 and suggestion.get("status")=="UNAPPROVED_EDITORIAL_PROPOSAL_NOT_APPLIED"
                 and len(suggestion.get("myanmar_meaning",""))>10
                 and len(suggestion.get("original_example_sentence",""))>25,
                 "Unapproved Myanmar/example alternative changed: "+word)
        else:
            need(lead is None and suggestion is None, "Invented dictionary evidence: "+word)
    return {"written":200,"independently_approved":0,"word_pos_observations":12,
            "publisher_lower":4,"publisher_higher":4,"word_pos_match_unverified":4,
            "direct_dictionary_sense_leads":4,"release":"BLOCKED_STAGING_ONLY"}

def self_test(packet,shortlist):
    tests=[]
    for i in range(12):
        cases=(
            ("word",lambda r:r.update(word="forged")),
            ("draft-level",lambda r:r.update(level="C1")),
            ("pos",lambda r:r.update(part_of_speech="forged")),
            ("source-level",lambda r:r["publisher_source"].update(source_cefr_level="C1")),
            ("source-page",lambda r:r["publisher_source"].update(pdf_page=0)),
            ("source-line",lambda r:r["publisher_source"].update(extracted_line=-1)),
            ("source-excerpt",lambda r:r["publisher_source"].update(source_excerpt="forged")),
            ("source-url",lambda r:r["publisher_source"].update(url="https://example.org/fake.pdf")),
            ("source-date",lambda r:r["publisher_source"].update(observed_on="1900-01-01")),
            ("English",lambda r:r["shortlist_snapshot"].update(english_definition="forged")),
            ("Myanmar",lambda r:r["shortlist_snapshot"].update(myanmar_meaning="အမှား")),
            ("example",lambda r:r["shortlist_snapshot"].update(example_sentence="forged")),
            ("provenance",lambda r:r["shortlist_provenance"].update(source_index=-1)),
            ("hold",lambda r:r.update(editorial_hold=False)),
            ("review",lambda r:r.update(independently_reviewed=True)),
            ("approval",lambda r:r.update(release_approved=True)),
            ("fake-receipt",lambda r:r.update(independent_reviewer_receipt={"fake":True})),
            ("risk",lambda r:r.update(editorial_risk="")),
        )
        for name,mut in cases:
            test=copy.deepcopy(packet)
            mut(test["records"][i])
            tests.append((name,test))
    for name,test in tests:
        try: audit(test,shortlist)
        except ValueError: continue
        raise AssertionError("Forged B1 tenth source/bilingual/review accepted: "+name)
    return len(tests)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    packet=json.loads(PACKET.read_text("utf8"))
    shortlist=json.loads(SHORT.read_text("utf8"))
    report=audit(packet,shortlist)
    if args.self_test:
        n=self_test(packet,shortlist)
        print(f"PASS: rejected {n}/{n} B1 tenth adversarial evidence/bilingual/reviewer mutations")
    print(json.dumps({"level":args.level,**report},sort_keys=True))
if __name__=="__main__": main()
