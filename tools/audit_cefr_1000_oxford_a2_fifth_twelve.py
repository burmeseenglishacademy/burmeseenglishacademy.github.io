#!/usr/bin/env python3
"""Fail-closed Oxford A2 fifth-twelve research integrity audit, never an approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-FIFTH-TWELVE-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
OBS = json.loads(r'''[["history","A1",2,369,"history n.","HISTORY_A1_VS_A2_AND_PAST_EVENTS_VS_ACADEMIC_SUBJECT","Oxford lists the noun at A1, while draft A2 describes historical events. Check teaching rationale for the precise sense, Myanmar phrasing and example; independent human source-backed exact-sense review required."],["university","A1",4,837,"university n.","UNIVERSITY_A1_VS_A2_AND_BRITISH_AT_UNIVERSITY","Oxford lists university n. at A1. Review the British idiom 'at university' in the example and distinguish an institution from university education; independent human bilingual and exact-sense CEFR signoff required."],["air","A1",1,23,"air n.","AIR_A1_VS_A2_ATMOSPHERE_VS_MANNER","Oxford lists air n. at A1. Draft means breathable atmospheric gases, not an air of confidence or an aircraft journey; verify Myanmar and original example independently."],["probably","A1",3,622,"probably adv.","PROBABLY_A1_VS_A2_LIKELIHOOD_NOT_CERTAINTY","Oxford lists probably adv. at A1. Confirm probability rather than certainty and improve natural Myanmar adverb wording if necessary; independent exact-sense review required."],["future","A1",2,322,"future n.","FUTURE_A1_VS_A2_NOUN_NOT_ADJECTIVE","Oxford lists future n. at A1. Confirm the time-after-present noun sense and distinguish adjective uses; independent reviewer to verify CEFR, Myanmar and example."],["police","A1",3,606,"police n.","POLICE_A1_VS_A2_COLLECTIVE_PLURAL_NOUN","Oxford gives police n. at A1; draft marks plural noun. British collective grammar 'the police are/asked' is relevant. Verify accurate Myanmar institutional meaning and grammar independently."],["reason","A1",3,643,"reason n.","REASON_A1_VS_A2_CAUSE_VS_EXPLANATION","Oxford lists reason n. at A1. Distinguish cause from an explanation or justification and independently verify the draft example and Myanmar nuance."],["within","B1",10,2579,"within prep.","WITHIN_B1_VS_A2_TIME_LIMIT_AND_SPACE","Oxford lists within prep. at B1, higher than A2 draft. In 'within two days' distinguish deadline before the end of two days from 'in two days'; independently review Myanmar temporal meaning and exact-sense CEFR."],["able","A2",4,910,"able adj.","ABLE_A2_MATCH_BE_ABLE_TO_CONSTRUCTION","Oxford lists able adj. at A2. Check the 'be able to + infinitive' construction and difference between skill, opportunity and permission; human exact-sense review required."],["single","A2",6,1618,"single adj., n.","SINGLE_A2_MATCH_ROOM_AMBIGUITY_AND_UNMARRIED_SENSE","Oxford lists single adj., n. at A2. Draft 'single room' could refer to accommodation for one person rather than only one room; disambiguate this from unmarried and noun senses."],["large","A1",2,425,"large adj.","LARGE_A1_VS_A2_SIZE_AND_QUANTITY","Oxford lists large adj. at A1. Check physical size versus amount, and whether Myanmar wording suits the example; independent source-backed sense review required."],["possible","A1",3,611,"possible adj.","POSSIBLE_A1_VS_A2_FEASIBILITY_AND_PROBABILITY","Oxford lists possible adj. at A1. Draft focuses on feasibility ('possible to change') rather than probability; verify natural Myanmar and exact-sense evidence independently."]]''')
LEVELS = ("A1","A2","B1","B2","C1")
RECORD_KEYS = {"word","level","part_of_speech","shortlist_snapshot","shortlist_provenance",
               "publisher_source","editorial_risk","independent_reviewer_task",
               "editorial_hold","independently_reviewed","release_approved",
               "independent_reviewer_receipt"}
SOURCE_KEYS = {"publisher","title","url","observed_on","pdf_page","extracted_line",
               "source_excerpt","source_cefr_level","evidence_scope","access"}

def require(ok, why):
    if not ok:
        raise ValueError(why)

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()

def audit(packet, shortlist):
    require(git_blob(SHORTLIST) == SHORTLIST_SHA, "Frozen shortlist blob drift")
    require(shortlist.get("counts_by_level") == dict.fromkeys(LEVELS,200)
            and shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS,0),
            "Shortlist scope/approval drift")
    entries = shortlist.get("entries")
    require(isinstance(entries,list) and len(entries)==1000
            and len({e["word"].casefold() for e in entries})==1000,
            "Shortlist must be 1000 deduplicated words")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in ("reviewed_english","reviewed_burmese",
                    "reviewed_example","reviewed_level","reviewed_pronunciation"))
                for e in entries), "Fake shortlist review")
    require(set(packet)=={"schema","scope","status","observed_on","shortlist_blob_sha",
            "record_count","counts_by_level","publisher_reference_level_counts",
            "word_pos_discrepancies","independently_approved_count","source_limitations","records"},
            "Unexpected packet fields")
    require(packet["schema"]==1 and packet["scope"]=="CEFR_1000_TOTAL_STAGING_ONLY"
            and packet["status"]=="A2_FIFTH_TWELVE_OXFORD_WORD_POS_EDITORIAL_HOLD"
            and packet["observed_on"]=="2026-10-29"
            and packet["shortlist_blob_sha"]==SHORTLIST_SHA,
            "Scope/status/provenance mismatch")
    require(packet["record_count"]==12
            and packet["counts_by_level"]=={"A1":0,"A2":12,"B1":0,"B2":0,"C1":0}
            and packet["publisher_reference_level_counts"]=={"A1":9,"A2":2,"B1":1}
            and packet["word_pos_discrepancies"]==10
            and packet["independently_approved_count"]==0,
            "Counts or fake approval")
    require("never exact-sense" in packet["source_limitations"].lower(),
            "Missing source limitations")
    rows=packet["records"]
    require(isinstance(rows,list) and len(rows)==12
            and [r.get("word") for r in rows]==[x[0] for x in OBS],
            "Wrong source observation order/count")
    byword={e["word"]:e for e in entries}
    for row,(word,source_level,page,line,excerpt,risk,task) in zip(rows,OBS):
        entry=byword[word]
        require(set(row)==RECORD_KEYS and row["word"]==word
                and row["level"]==entry["level"]=="A2"
                and row["part_of_speech"]==entry["part_of_speech"],
                "Headword/level/POS drift "+word)
        require(row["shortlist_snapshot"]==
                {"english_definition":entry["english_definition"],
                 "myanmar_meaning":entry["burmese_meaning"],
                 "example_sentence":entry["example_sentence"]},
                "English/Myanmar/example drift "+word)
        require(row["shortlist_provenance"]==
                {k:entry[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical source provenance drift "+word)
        require(set(row["publisher_source"])==SOURCE_KEYS
                and row["publisher_source"]==
                {"publisher":"Oxford University Press",
                 "title":"The Oxford 3000 by CEFR level",
                 "url":URL,"observed_on":"2026-10-29","pdf_page":page,
                 "extracted_line":line,"source_excerpt":excerpt,
                 "source_cefr_level":source_level,
                 "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                 "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Forged Oxford source/locator "+word)
        require(row["editorial_risk"]==risk and row["independent_reviewer_task"]==task,
                "Editorial risk/task drift "+word)
        require(row["editorial_hold"] is True and row["independently_reviewed"] is False
                and row["release_approved"] is False
                and row["independent_reviewer_receipt"] is None,
                "Forged human review "+word)
    return {"draft_level":"A2","observations":12,"publisher_A1":9,
            "publisher_A2":2,"publisher_B1":1,"independent_approvals":0,
            "release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    changes=[
      ("word",lambda r:r.update(word="forged")),
      ("draft level",lambda r:r.update(level="B1")),
      ("POS",lambda r:r.update(part_of_speech="forged")),
      ("English",lambda r:r["shortlist_snapshot"].update(english_definition="fake")),
      ("Myanmar",lambda r:r["shortlist_snapshot"].update(myanmar_meaning="မှား")),
      ("example",lambda r:r["shortlist_snapshot"].update(example_sentence="fake")),
      ("source path",lambda r:r["shortlist_provenance"].update(source_path="fake")),
      ("source index",lambda r:r["shortlist_provenance"].update(source_index=-1)),
      ("source blob",lambda r:r["shortlist_provenance"].update(source_blob_sha="0"*40)),
      ("publisher",lambda r:r["publisher_source"].update(publisher="fake")),
      ("title",lambda r:r["publisher_source"].update(title="fake")),
      ("URL",lambda r:r["publisher_source"].update(url="https://example.invalid")),
      ("date",lambda r:r["publisher_source"].update(observed_on="2099-01-01")),
      ("page",lambda r:r["publisher_source"].update(pdf_page=0)),
      ("line",lambda r:r["publisher_source"].update(extracted_line=-1)),
      ("excerpt",lambda r:r["publisher_source"].update(source_excerpt="fake")),
      ("Oxford level",lambda r:r["publisher_source"].update(source_cefr_level="C2")),
      ("evidence scope",lambda r:r["publisher_source"].update(evidence_scope="APPROVED")),
      ("access",lambda r:r["publisher_source"].update(access="SECONDHAND")),
      ("risk",lambda r:r.update(editorial_risk="fake")),
      ("task",lambda r:r.update(independent_reviewer_task="Approved")),
      ("hold",lambda r:r.update(editorial_hold=False)),
      ("review",lambda r:r.update(independently_reviewed=True)),
      ("approval",lambda r:r.update(release_approved=True)),
      ("receipt",lambda r:r.update(independent_reviewer_receipt={"fake":True}))
    ]
    rejected=0
    for i in range(12):
        for label,mutate in changes:
            p=copy.deepcopy(packet)
            mutate(p["records"][i])
            try:
                audit(p,shortlist)
            except ValueError:
                rejected+=1
                continue
            raise AssertionError("Forged "+label+" passed "+OBS[i][0])
    for label,mutate in [
      ("record count",lambda p:p.update(record_count=13)),
      ("source counts",lambda p:p.update(publisher_reference_level_counts={"A1":8,"A2":3,"B1":1})),
      ("approval count",lambda p:p.update(independently_approved_count=1)),
      ("status",lambda p:p.update(status="APPROVED")),
      ("shortlist SHA",lambda p:p.update(shortlist_blob_sha="0"*40)),
      ("source limitations",lambda p:p.update(source_limitations="All approved"))
    ]:
        p=copy.deepcopy(packet)
        mutate(p)
        try:
            audit(p,shortlist)
        except ValueError:
            rejected+=1
            continue
        raise AssertionError("Forged packet "+label+" passed")
    return rejected

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    p.add_argument("--self-test",action="store_true")
    args=p.parse_args()
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist=json.loads(SHORTLIST.read_text(encoding="utf-8"))
    result=audit(packet,shortlist)
    if args.self_test:
        n=self_test(packet,shortlist)
        print(f"PASS: {n}/{n} forged Oxford, bilingual, provenance and human-review mutations rejected")
    print(json.dumps(result if args.level in ("A2","ALL") else
                     {"draft_level":args.level,"observations":0,"independent_approvals":0},
                     sort_keys=True))

if __name__=="__main__":
    main()
