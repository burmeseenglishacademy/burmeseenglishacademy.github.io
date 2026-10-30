#!/usr/bin/env python3
"""Fail-closed B1 eleventh Oxford word/POS research auditor. Not human signoff."""
import argparse, copy, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/"draft/CEFR-1000-OXFORD-B1-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT=ROOT/"draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA="dc2522c508de0a6fe0404b243f68a3bb925921a6"
SHORT_SHA="475e68ae17ab97bd937e73e5ce4794e0dcd76551"
BASE="https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/"
LEVELS=("A1","A2","B1","B2","C1")
EXPECTED=[
("foundation","B2",2,265,"foundation n.",5000),
("gain","B2",11,2886,"gain v., n.",3000),
("influence","B1",8,2148,"influence n., v.",3000),
("improve","A1",2,393,"improve v.",3000),
("prevent","A2",6,1495,"prevent v.",3000),
("advantage","A2",4,920,"advantage n.",3000),
("aware","B1",7,1837,"aware adj.",3000),
("decide","A1",1,198,"decide v.",3000),
("progress","A2",6,1506,"progress n.",3000),
("concept","B2",10,2711,"concept n.",3000),
("academic","B1",7,1784,"academic adj.",3000),
("accurate","B2",10,2599,"accurate adj.",3000)]
LEADS={
"foundation":("https://www.oxfordlearnersdictionaries.com/definition/english/foundation",4,170,180),
"gain":("https://www.oxfordlearnersdictionaries.com/definition/english/gain_1",3,181,192),
"influence":("https://www.oxfordlearnersdictionaries.com/definition/english/influence_2",1,112,128),
"concept":("https://www.oxfordlearnersdictionaries.com/definition/english/concept",1,119,145)}
def need(ok,why):
    if not ok: raise ValueError(why)
def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+bytes([0])+b).hexdigest()
def audit(packet,shortlist):
    need(blob(PACKET)==PACKET_SHA and blob(SHORT)==SHORT_SHA,"Frozen research/shortlist Git blob drift")
    need(packet.get("schema")==1 and packet.get("scope")=="CEFR_1000_TOTAL_STAGING_ONLY"
        and packet.get("status")=="B1_ELEVENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
        and packet.get("observed_on")=="2026-10-30"
        and packet.get("shortlist_blob_sha")==SHORT_SHA
        and packet.get("record_count")==12
        and packet.get("counts_by_level")==dict(zip(LEVELS,(0,0,12,0,0)))
        and packet.get("publisher_reference_level_counts")=={"A1":2,"A2":3,"B1":3,"B2":4}
        and packet.get("word_pos_discrepancies")==9
        and packet.get("direct_dictionary_sense_leads")==4
        and packet.get("independently_approved_count")==0,"Packet scope/counts/approval drift")
    need(shortlist.get("counts_by_level")==dict.fromkeys(LEVELS,200)
        and shortlist.get("independently_approved_by_level")==dict.fromkeys(LEVELS,0)
        and len(shortlist.get("entries",[]))==1000,"Shortlist 200-per-level/approval drift")
    byword={e["word"]:e for e in shortlist["entries"]}
    need(len(byword)==1000,"Duplicate shortlist headword")
    rows=packet.get("records")
    need(isinstance(rows,list) and len(rows)==12,"Incomplete Oxford records")
    for row,(word,cefr,page,line,excerpt,source) in zip(rows,EXPECTED):
        e=byword.get(word)
        need(e is not None and e["level"]=="B1" and row.get("word")==word
             and row.get("level")=="B1" and row.get("part_of_speech")==e["part_of_speech"],"Word/POS drift: "+word)
        need(row.get("shortlist_snapshot")=={
             "english_definition":e["english_definition"],"myanmar_meaning":e["burmese_meaning"],
             "example_sentence":e["example_sentence"]},"Bilingual/example snapshot drift: "+word)
        need(row.get("shortlist_provenance")=={
             k:e[k] for k in ("source_path","source_index","source_blob_sha")},"Historical provenance drift: "+word)
        need(row.get("publisher_source")=={
             "publisher":"Oxford University Press",
             "title":f"The Oxford {source} by CEFR level",
             "url":BASE+f"The_Oxford_{source}_by_CEFR_level.pdf",
             "observed_on":"2026-10-30","pdf_page":page,"extracted_line":line,
             "source_excerpt":excerpt,"source_cefr_level":cefr,
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"Publisher evidence drift: "+word)
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
             and row.get("release_approved") is False and row.get("independent_reviewer_receipt") is None
             and e.get("editorial_hold") is True and e.get("release_approved") is False,
             "Fabricated human approval: "+word)
        need(isinstance(row.get("editorial_risk"),str) and len(row["editorial_risk"])>40
             and "Independent human reviewer" in row.get("independent_reviewer_task",""),
             "Missing sense risk/reviewer task: "+word)
        lead=row.get("dictionary_sense_lead")
        candidate=row.get("editorial_rewrite_candidate")
        if word in LEADS:
            u,s,a,b=LEADS[word]
            need(isinstance(lead,dict) and lead.get("url")==u and lead.get("sense_number")==s
                 and lead.get("page_text_line_start")==a and lead.get("page_text_line_end")==b
                 and lead.get("observed_on")=="2026-10-30"
                 and lead.get("evidence_scope")=="DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"
                 and len(lead.get("editorial_interpretation",""))>35,"Dictionary lead drift: "+word)
            need(isinstance(candidate,dict)
                 and candidate.get("status")=="UNAPPROVED_EDITORIAL_PROPOSAL_NOT_APPLIED"
                 and len(candidate.get("myanmar_meaning",""))>10
                 and len(candidate.get("original_example_sentence",""))>25,
                 "Editorial alternative drift: "+word)
        else:
            need(lead is None and candidate is None,"Fabricated dictionary lead: "+word)
    return {"written":200,"independently_approved":0,"publisher_observations":12,
            "publisher_higher":4,"publisher_lower":5,"word_pos_match_unverified":3,
            "direct_dictionary_sense_leads":4,"release":"BLOCKED_STAGING_ONLY"}
def self_test(packet,shortlist):
    tests=[]
    for i in range(12):
        mutations=[
          ("word",lambda r:r.update(word="fabricated")),
          ("level",lambda r:r.update(level="C1")),
          ("pos",lambda r:r.update(part_of_speech="fabricated")),
          ("publisher-level",lambda r:r["publisher_source"].update(source_cefr_level="C1")),
          ("publisher-url",lambda r:r["publisher_source"].update(url="https://example.org/fake.pdf")),
          ("publisher-title",lambda r:r["publisher_source"].update(title="Invented Oxford")),
          ("publisher-date",lambda r:r["publisher_source"].update(observed_on="1900-01-01")),
          ("publisher-page",lambda r:r["publisher_source"].update(pdf_page=0)),
          ("publisher-line",lambda r:r["publisher_source"].update(extracted_line=-1)),
          ("publisher-excerpt",lambda r:r["publisher_source"].update(source_excerpt="fake")),
          ("english",lambda r:r["shortlist_snapshot"].update(english_definition="fake")),
          ("myanmar",lambda r:r["shortlist_snapshot"].update(myanmar_meaning="အမှား")),
          ("example",lambda r:r["shortlist_snapshot"].update(example_sentence="fake")),
          ("source-index",lambda r:r["shortlist_provenance"].update(source_index=-1)),
          ("source-blob",lambda r:r["shortlist_provenance"].update(source_blob_sha="fake")),
          ("hold",lambda r:r.update(editorial_hold=False)),
          ("review",lambda r:r.update(independently_reviewed=True)),
          ("approved",lambda r:r.update(release_approved=True)),
          ("receipt",lambda r:r.update(independent_reviewer_receipt={"fake":True})),
          ("risk",lambda r:r.update(editorial_risk=""))]
        if packet["records"][i]["dictionary_sense_lead"] is not None:
            mutations += [
                ("dictionary-url",lambda r:r["dictionary_sense_lead"].update(url="https://example.org")),
                ("dictionary-sense",lambda r:r["dictionary_sense_lead"].update(sense_number=999)),
                ("dictionary-line",lambda r:r["dictionary_sense_lead"].update(page_text_line_start=-1)),
                ("candidate-approval",lambda r:r["editorial_rewrite_candidate"].update(status="APPROVED"))]
        for name,mut in mutations:
            altered=copy.deepcopy(packet)
            mut(altered["records"][i])
            tests.append((name,altered))
    for name,altered in tests:
        try: audit(altered,shortlist)
        except ValueError: continue
        raise AssertionError("Forged B1 eleventh evidence accepted: "+name)
    return len(tests)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    packet=json.loads(PACKET.read_text("utf-8"))
    shortlist=json.loads(SHORT.read_text("utf-8"))
    result=audit(packet,shortlist)
    if args.self_test:
        n=self_test(packet,shortlist)
        print(f"PASS: rejected {n}/{n} B1 eleventh adversarial publisher, bilingual, provenance and approval mutations")
    print(json.dumps({"level":args.level,**result},sort_keys=True))
if __name__=="__main__": main()
