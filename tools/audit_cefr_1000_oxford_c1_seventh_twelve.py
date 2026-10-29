#!/usr/bin/env python3
"""Fail-closed staging-only C1 Oxford PDF + direct-dictionary evidence auditor.
No human review, listening, iPhone test, or release permission is conferred.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SHORTLIST=ROOT/"draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET=ROOT/"draft/CEFR-1000-OXFORD-C1-SEVENTH-TWELVE-2026-10-30.json"
FROZEN="475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL="https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
OBS=json.loads(r'''[["controversial","B2",1,127,"controversial adj.","C1_DRAFT_VS_OXFORD_B2_WORD_POS","Oxford lists the ordinary adjective at B2. Independent reviewer must establish a genuinely distinct C1 sense or replace/retier; verify fluent Myanmar and original example. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["legendary","C1",6,1401,"legendary adj.","LEGENDARY_FAMOUS_VS_MYTHICAL","Distinguish celebrated real-world person from a person in legend; Myanmar ဒဏ္ဍာရီလာ may misleadingly suggest mythical rather than very famous. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["regulatory","C1",7,1684,"regulatory adj.","REGULATORY_RULES_VS_REGULATOR","Check adjective regulatory vs noun regulator; verify formal industry collocation and Myanmar ထိန်းကြပ်ရေး. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["integration","C1",5,1354,"integration n.","INTEGRATION_TECHNICAL_VS_SOCIAL","Draft technical system integration differs from social integration; verify exact sense and Burmese technical register. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["legitimate","C1",6,1405,"legitimate adj.","LEGITIMATE_LEGAL_VS_REASONABLE","Definition combines lawful and justified/reasonable senses; example legitimate reason selects justified, not necessarily lawful. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["advocate","C1",3,743,"advocate n., v.","ADVOCATE_VERB_VS_NOUN","Check verb support/recommend vs noun person; verify transitive advocate stricter controls and Myanmar တိုက်တွန်းသည်. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["custody","C1",4,1032,"custody n.","CUSTODY_CHILD_CARE_VS_DETENTION","Definition combines child custody and police detention; example is child custody. Require one precise teachable sense and natural child-custody collocation. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["excess","C1",5,1185,"excess n., adj.","EXCESS_NOUN_VS_ADJECTIVE_EXAMPLE_CRITICAL","CRITICAL: draft labels noun but 'the excess material' uses adjective excess; Oxford directly distinguishes noun and adjective. Rewrite example only after independent review. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["operational","C1",6,1533,"operational adj.","OPERATIONAL_FUNCTIONING_VS_OPERATIONS","Differentiate operational 'relating to operations' from 'ready for use'; review warehouse example and Myanmar. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["syndrome","C1",7,1882,"syndrome n.","SYNDROME_MEDICAL_VS_NONMEDICAL","Check syndrome clinical symptom cluster versus metaphorical pattern; ensure medically precise Myanmar without diagnosis claims. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["fluid","C1",5,1225,"fluid n.","FLUID_LIQUID_VS_GAS","Definition includes liquid and gas, while brake fluid is a liquid; verify physical meaning, uncountability and fluent Myanmar. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."],["amateur","C1",3,768,"amateur adj., n.","AMATEUR_NOUN_VS_ADJECTIVE_EXAMPLE_CRITICAL","CRITICAL: draft labels noun but 'amateur photographer' is adjectival; Oxford directly documents this adjective use and a separate noun sense. Independent human reviewer must confirm exact-sense CEFR, English definition, natural Myanmar, original example grammar, British pronunciation, source URL/observation date and a content-bound signoff; retain hold until independently verified."]]''')
DIRECT_LEADS=json.loads(r'''[{"word":"excess","noun_url":"https://www.oxfordlearnersdictionaries.com/definition/english/excess_1","noun_lines":"88-110","adjective_url":"https://www.oxfordlearnersdictionaries.com/definition/english/excess_2","adjective_lines":"88-110","observed_on":"2026-10-30","finding":"Draft example 'the excess material' uses attributive adjective excess, not the proposed noun.","dictionary_badge_conflict":"The directly accessed Oxford dictionary page displays an Oxford 3000 B2 badge, while direct search of the official Oxford 3000 CEFR PDF found no matching headword and the Oxford 5000 PDF lists the word/POS under C1. Treat as an unresolved publisher display/list discrepancy, NOT independent exact-sense CEFR evidence.","oxford3000_pdf_checked_url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","badge_observed_on":"2026-10-30"},{"word":"amateur","noun_url":"https://www.oxfordlearnersdictionaries.com/definition/english/amateur_2","noun_lines":"88-116","adjective_url":"https://www.oxfordlearnersdictionaries.com/definition/english/amateur_1","adjective_lines":"88-116","observed_on":"2026-10-30","finding":"Draft example 'The amateur photographer...' uses attributive adjective, not proposed noun.","dictionary_badge_conflict":"The directly accessed Oxford dictionary page displays an Oxford 3000 B2 badge, while direct search of the official Oxford 3000 CEFR PDF found no matching headword and the Oxford 5000 PDF lists the word/POS under C1. Treat as an unresolved publisher display/list discrepancy, NOT independent exact-sense CEFR evidence.","oxford3000_pdf_checked_url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","badge_observed_on":"2026-10-30"}]''')
RECORD_KEYS={"word","level","part_of_speech","shortlist_snapshot","shortlist_provenance",
             "publisher_source","editorial_risk","independent_reviewer_task",
             "editorial_hold","independently_reviewed","release_approved","independent_reviewer_receipt"}
PUB_KEYS={"publisher","title","url","observed_on","pdf_page","extracted_line",
          "source_excerpt","source_cefr_level","evidence_scope","access"}
LEVELS=("A1","A2","B1","B2","C1")

def require(test,reason):
    if not test: raise ValueError(reason)

def blob_sha(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def audit(p,s):
    require(blob_sha(SHORTLIST)==FROZEN,"Frozen shortlist blob drift")
    require(s.get("counts_by_level")==dict.fromkeys(LEVELS,200) and
            s.get("independently_approved_by_level")==dict.fromkeys(LEVELS,0),
            "Wrong scope or fabricated approvals")
    es=s.get("entries")
    require(isinstance(es,list) and len(es)==1000,"Exactly 1000 required")
    require(len({e.get("word","").casefold() for e in es})==1000,"Duplicate headwords")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in ("reviewed_english","reviewed_burmese",
                  "reviewed_example","reviewed_level","reviewed_pronunciation")) for e in es),
            "Shortlist editorial approval drift")
    require(p.get("schema")==1 and p.get("scope")=="CEFR_1000_TOTAL_STAGING_ONLY" and
            p.get("status")=="C1_SEVENTH_TWELVE_OXFORD_WORD_POS_EDITORIAL_HOLD" and
            p.get("observed_on")=="2026-10-30" and p.get("shortlist_blob_sha")==FROZEN,
            "Packet identity, scope, date or frozen source changed")
    require(p.get("record_count")==12 and p.get("counts_by_level")==
            {"A1":0,"A2":0,"B1":0,"B2":0,"C1":12} and
            p.get("publisher_reference_level_counts")=={"B2":1,"C1":11} and
            p.get("word_pos_discrepancies")==1 and
            p.get("independently_approved_count")==0,"Packet counts or approval drift")
    require("never exact-sense" in p.get("source_limitations","").lower(),
            "Evidence limitation missing")
    require(p.get("direct_dictionary_sense_leads")==DIRECT_LEADS,
            "Direct Oxford dictionary sense-lead evidence changed")
    rows=p.get("records")
    require(isinstance(rows,list) and len(rows)==12 and
            [r.get("word") for r in rows]==[o[0] for o in OBS],
            "Wrong C1 words or duplicate observations")
    by_word={e["word"]:e for e in es}
    for r,(word,level,page,line,excerpt,risk,task) in zip(rows,OBS):
        e=by_word[word]
        require(set(r)==RECORD_KEYS and r["level"]==e["level"]=="C1" and
                r["part_of_speech"]==e["part_of_speech"],"Headword/POS mismatch "+word)
        require(r["shortlist_snapshot"]==
                {"english_definition":e["english_definition"],
                 "myanmar_meaning":e["burmese_meaning"],
                 "example_sentence":e["example_sentence"]},
                "Frozen bilingual/example snapshot drift "+word)
        require(r["shortlist_provenance"]==
                {k:e[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical Git provenance drift "+word)
        require(set(r["publisher_source"])==PUB_KEYS and r["publisher_source"]==
                {"publisher":"Oxford University Press",
                 "title":"The Oxford 5000 by CEFR level",
                 "url":URL,"observed_on":"2026-10-30",
                 "pdf_page":page,"extracted_line":line,
                 "source_excerpt":excerpt,"source_cefr_level":level,
                 "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                 "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Source/PDF locator or CEFR label drift "+word)
        require(r["editorial_risk"]==risk and r["independent_reviewer_task"]==task,
                "Review risk/task drift "+word)
        require(r["editorial_hold"] is True and
                r["independently_reviewed"] is False and
                r["release_approved"] is False and
                r["independent_reviewer_receipt"] is None,
                "Fabricated independent review/approval "+word)
    return {"level":"C1","written":200,"new_source_observations":12,
            "publisher_B2":1,"publisher_C1":11,"independently_approved":0,
            "real_audio_listening_receipts":0,"release":"BLOCKED_STAGING_ONLY"}

def self_test(p,s):
    mutations=[
        ("word",lambda r:r.update(word="FAKE")),
        ("level",lambda r:r.update(level="B2")),
        ("part_of_speech",lambda r:r.update(part_of_speech="forged")),
        ("English",lambda r:r["shortlist_snapshot"].update(english_definition="forged")),
        ("Myanmar",lambda r:r["shortlist_snapshot"].update(myanmar_meaning="မှား")),
        ("example",lambda r:r["shortlist_snapshot"].update(example_sentence="forged")),
        ("source_path",lambda r:r["shortlist_provenance"].update(source_path="forged")),
        ("source_index",lambda r:r["shortlist_provenance"].update(source_index=-1)),
        ("source_blob",lambda r:r["shortlist_provenance"].update(source_blob_sha="0"*40)),
        ("publisher",lambda r:r["publisher_source"].update(publisher="forged")),
        ("title",lambda r:r["publisher_source"].update(title="forged")),
        ("URL",lambda r:r["publisher_source"].update(url="https://invalid.example")),
        ("observed_on",lambda r:r["publisher_source"].update(observed_on="1900-01-01")),
        ("page",lambda r:r["publisher_source"].update(pdf_page=999)),
        ("line",lambda r:r["publisher_source"].update(extracted_line=-1)),
        ("excerpt",lambda r:r["publisher_source"].update(source_excerpt="forged")),
        ("CEFR",lambda r:r["publisher_source"].update(source_cefr_level="A1")),
        ("scope",lambda r:r["publisher_source"].update(evidence_scope="EXACT_SENSE_APPROVED")),
        ("access",lambda r:r["publisher_source"].update(access="SEARCH_SNIPPET")),
        ("editorial_risk",lambda r:r.update(editorial_risk="forged")),
        ("review_task",lambda r:r.update(independent_reviewer_task="approved")),
        ("hold",lambda r:r.update(editorial_hold=False)),
        ("reviewed",lambda r:r.update(independently_reviewed=True)),
        ("approved",lambda r:r.update(release_approved=True)),
        ("receipt",lambda r:r.update(independent_reviewer_receipt={"reviewer":"fake"})),
    ]
    n=0
    for i in range(12):
        for label,mut in mutations:
            t=copy.deepcopy(p)
            before=json.dumps(t["records"][i],ensure_ascii=False,sort_keys=True)
            mut(t["records"][i])
            after=json.dumps(t["records"][i],ensure_ascii=False,sort_keys=True)
            require(before!=after,"Ineffective negative test: "+label)
            try: audit(t,s)
            except ValueError: n+=1
            else: raise AssertionError("Forged "+label+" accepted on "+OBS[i][0])
    packet_mutations=[
        ("record count",lambda t:t.update(record_count=11)),
        ("source counts",lambda t:t["publisher_reference_level_counts"].update(C1=12)),
        ("fake independent count",lambda t:t.update(independently_approved_count=1)),
        ("fake date",lambda t:t.update(observed_on="1900-01-01")),
        ("sense lead forgery",lambda t:t["direct_dictionary_sense_leads"][0].update(finding="approved")),
        ("remove record",lambda t:t["records"].pop()),
    ]
    for label,mut in packet_mutations:
        t=copy.deepcopy(p)
        before=json.dumps(t,ensure_ascii=False,sort_keys=True)
        mut(t)
        require(before!=json.dumps(t,ensure_ascii=False,sort_keys=True),"Ineffective "+label)
        try: audit(t,s)
        except ValueError: n+=1
        else: raise AssertionError("Forged packet "+label+" accepted")
    require(n==12*len(mutations)+len(packet_mutations),"Negative test count drift")
    return n

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    p=json.loads(PACKET.read_text(encoding="utf-8"))
    s=json.loads(SHORTLIST.read_text(encoding="utf-8"))
    result=audit(p,s)
    if args.self_test:
        n=self_test(p,s)
        print("PASS: %d/%d seventh C1 adversarial mutations rejected"%(n,n))
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    main()
