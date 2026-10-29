#!/usr/bin/env python3
"""Fail-closed staging-only integrity audit of 12 direct Oxford C1-draft word/POS leads.

This pins independently observed publisher PDF line excerpts and the original
shortlist snapshots. It is NOT exact-sense review, translation approval, listening
evidence, or a deployment gate that can authorise release.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-C1-SIXTH-TWELVE-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
U3 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
U5 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
# Directly checked official publisher PDF observations on 2026-10-29:
# word, Oxford word/POS CEFR, one-based PDF page, zero-based extracted line,
# verbatim short excerpt, editorial risk and review task. NOT exact-sense CEFR.
OBS = json.loads(r'''[["popularity","B2",12,3077,"popularity n.","POPULARITY_LOWER_B2_VS_C1_DRAFT","Confirm common noun popularity is Oxford B2 word/POS, not C1; seek exact-sense teaching rationale. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["sacred","C1",7,1737,"sacred adj.","SACRED_RELIGIOUS_VS_NONRELIGIOUS_SPECIAL","Distinguish religious holiness from metaphorically sacred personal traditions; check Myanmar register. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["spy","C1",7,1813,"spy n.","SPY_PERSON_VS_SPY_VERB","Check noun person secretly gathering information, not the verb; distinguish country and organisation. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["suspension","C1",7,1874,"suspension n.","SUSPENSION_TEMPORARY_STOP_VS_HANGING_OR_VEHICLE","Distinguish temporary interruption from suspension as hanging or vehicle component. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["terrorism","B2",3,633,"terrorism n.","TERRORISM_LOWER_B2_AND_NEUTRAL_DEFINITION","Oxford B2 word/POS vs draft C1; independently verify neutral, accurate definition and example. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["upgrade","C1",8,1956,"upgrade v., n.","UPGRADE_VERB_VS_NOUN_AND_REPLACE_VS_IMPROVE","Distinguish verb from noun; improving need not require replacement; review over-narrow English definition. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["warrant","C1",8,1993,"warrant n., v.","WARRANT_LEGAL_DOCUMENT_VS_JUSTIFY_VERB","Confirm noun legal authorization rather than verb justify; verify natural legal Myanmar wording. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["asset","B2",1,37,"asset n.","ASSET_LOWER_B2_AND_PERSON_VS_PROPERTY","Oxford B2 word/POS vs draft C1; English definition combines valuable property and useful person; example uses person sense. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["burden","C1",4,867,"burden n.","BURDEN_FIGURATIVE_RESPONSIBILITY_VS_PHYSICAL_LOAD","Check figurative responsibility/cost versus literal heavy load; fluent Myanmar. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["charter","C1",4,895,"charter n.","CHARTER_FOUNDING_DOCUMENT_VS_RENTAL","Distinguish organisation constitution from chartered transport/rental. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["civilian","C1",4,903,"civilian n., adj.","CIVILIAN_NOUN_VS_ADJECTIVE_EXAMPLE_MISMATCH","CRITICAL: shortlist labels noun, but example 'civilian families' uses adjective. Independent correction required before approval. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."],["coalition","C1",4,911,"coalition n.","COALITION_POLITICAL_ALLIANCE_VS_GENERIC_COOPERATION","Distinguish political coalition from general collaboration; review Burmese nuance. Independent human must check exact sense, source-backed CEFR, English/Myanmar, original example and real British audio; attach dated content-bound evidence."]]''')
RECORD_KEYS = {"word","level","part_of_speech","shortlist_snapshot","shortlist_provenance",
               "publisher_source","editorial_risk","independent_reviewer_task",
               "editorial_hold","independently_reviewed","release_approved",
               "independent_reviewer_receipt"}
SOURCE_KEYS = {"publisher","title","url","observed_on","pdf_page","extracted_line",
               "source_excerpt","source_cefr_level","evidence_scope","access"}
LEVELS = ("A1","A2","B1","B2","C1")

def require(test, message):
    if not test:
        raise ValueError(message)

def git_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()

def audit(packet, shortlist):
    require(git_blob(SHORTLIST) == SHORTLIST_SHA, "shortlist Git blob changed")
    require(shortlist.get("counts_by_level") == dict.fromkeys(LEVELS,200)
            and shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS,0),
            "shortlist scope or approvals changed")
    entries = shortlist.get("entries")
    require(isinstance(entries,list) and len(entries)==1000, "shortlist not 1000")
    require(len({e.get("word","").casefold() for e in entries})==1000,
            "duplicate shortlist headwords")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in ("reviewed_english","reviewed_burmese",
                    "reviewed_example","reviewed_level","reviewed_pronunciation"))
                for e in entries), "shortlist has fake approvals")
    require(packet.get("schema")==1 and packet.get("scope")=="CEFR_1000_TOTAL_STAGING_ONLY",
            "packet scope/schema")
    require(packet.get("status")=="C1_SIXTH_TWELVE_OXFORD_WORD_POS_EDITORIAL_HOLD"
            and packet.get("observed_on")=="2026-10-29", "packet status/date")
    require(packet.get("shortlist_blob_sha")==SHORTLIST_SHA, "packet shortlist SHA")
    require(packet.get("record_count")==12
            and packet.get("counts_by_level")=={"A1":0,"A2":0,"B1":0,"B2":0,"C1":12}
            and packet.get("publisher_reference_level_counts")=={"B2":3,"C1":9}
            and packet.get("word_pos_discrepancies")==3
            and packet.get("independently_approved_count")==0,
            "counts or fabricated approval")
    require(isinstance(packet.get("source_limitations"),str)
            and "never exact-sense" in packet["source_limitations"].lower(),
            "publisher limitations absent")
    records = packet.get("records")
    require(isinstance(records,list) and len(records)==12
            and [r.get("word") for r in records]==[r[0] for r in OBS],
            "wrong 12 words or duplicate records")
    by_word = {e["word"]:e for e in entries}
    for r,(word,source_level,page,line,excerpt,risk,task) in zip(records,OBS):
        e=by_word[word]
        require(set(r)==RECORD_KEYS and r["word"]==word
                and r["level"]=="C1" and e["level"]=="C1"
                and r["part_of_speech"]==e["part_of_speech"], "word/POS drift: "+word)
        require(r["shortlist_snapshot"]==
                {"english_definition":e["english_definition"],
                 "myanmar_meaning":e["burmese_meaning"],
                 "example_sentence":e["example_sentence"]}, "bilingual/example drift: "+word)
        require(r["shortlist_provenance"]==
                {k:e[k] for k in ("source_path","source_index","source_blob_sha")},
                "historical Git provenance drift: "+word)
        pub=r["publisher_source"]
        require(set(pub)==SOURCE_KEYS and pub==
                {"publisher":"Oxford University Press",
                 "title":"The Oxford "+("3000" if word=="popularity" else "5000")+" by CEFR level",
                 "url":U3 if word=="popularity" else U5,
                 "observed_on":"2026-10-29","pdf_page":page,
                 "extracted_line":line,"source_excerpt":excerpt,
                 "source_cefr_level":source_level,
                 "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                 "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "publisher PDF source drift: "+word)
        require(r["editorial_risk"]==risk and r["independent_reviewer_task"]==task,
                "review task/risk drift: "+word)
        require(r["editorial_hold"] is True and r["independently_reviewed"] is False
                and r["release_approved"] is False
                and r["independent_reviewer_receipt"] is None,
                "fake review/approval: "+word)
    return {"level":"C1","observations":12,"publisher_B2":3,"publisher_C1":9,
            "independently_approved":0,"status":"STAGING_ONLY"}

def self_test(packet,shortlist):
    changes = [
        ("word",lambda r:r.update(word="counterfeit")),
        ("level",lambda r:r.update(level="B2")),
        ("pos",lambda r:r.update(part_of_speech="noun" if r["part_of_speech"]=="verb" else "verb")),
        ("English",lambda r:r["shortlist_snapshot"].update(english_definition="Fabricated")),
        ("Myanmar",lambda r:r["shortlist_snapshot"].update(myanmar_meaning="မှားနေသည်")),
        ("example",lambda r:r["shortlist_snapshot"].update(example_sentence="Fabricated.")),
        ("source path",lambda r:r["shortlist_provenance"].update(source_path="fake.json")),
        ("source index",lambda r:r["shortlist_provenance"].update(source_index=-1)),
        ("source blob",lambda r:r["shortlist_provenance"].update(source_blob_sha="0"*40)),
        ("publisher URL",lambda r:r["publisher_source"].update(url="https://example.invalid/fake")),
        ("publisher identity",lambda r:r["publisher_source"].update(publisher="Unknown")),
        ("source date",lambda r:r["publisher_source"].update(observed_on="2026-10-30")),
        ("source page",lambda r:r["publisher_source"].update(pdf_page=r["publisher_source"]["pdf_page"]+100)),
        ("source line",lambda r:r["publisher_source"].update(extracted_line=-1)),
        ("source quote",lambda r:r["publisher_source"].update(source_excerpt="fake adj.")),
        ("source level",lambda r:r["publisher_source"].update(source_cefr_level="A1")),
        ("source scope",lambda r:r["publisher_source"].update(evidence_scope="EXACT_SENSE")),
        ("access",lambda r:r["publisher_source"].update(access="SEARCH_SNIPPET")),
        ("risk",lambda r:r.update(editorial_risk="none")),
        ("review task",lambda r:r.update(independent_reviewer_task="Approved")),
        ("hold",lambda r:r.update(editorial_hold=False)),
        ("reviewed",lambda r:r.update(independently_reviewed=True)),
        ("approved",lambda r:r.update(release_approved=True)),
        ("receipt",lambda r:r.update(independent_reviewer_receipt={"reviewer":"bot"})),
    ]
    count=0
    for i in range(12):
        for name,mutate in changes:
            test=copy.deepcopy(packet)
            mutate(test["records"][i])
            try:
                audit(test,shortlist)
            except ValueError:
                count+=1
                continue
            raise AssertionError("Forged "+name+" accepted for "+OBS[i][0])
    for name,mutate in [
        ("count",lambda p:p.update(record_count=13)),
        ("B2 count",lambda p:p.update(publisher_reference_level_counts={"B2":2,"C1":10})),
        ("approval count",lambda p:p.update(independently_approved_count=1)),
        ("packet status",lambda p:p.update(status="APPROVED")),
        ("shortlist SHA",lambda p:p.update(shortlist_blob_sha="0"*40)),
    ]:
        test=copy.deepcopy(packet)
        mutate(test)
        try:
            audit(test,shortlist)
        except ValueError:
            count+=1
            continue
        raise AssertionError("Forged packet "+name+" accepted")
    return count

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    packet=json.loads(PACKET.read_text(encoding="utf8"))
    shortlist=json.loads(SHORTLIST.read_text(encoding="utf8"))
    result=audit(packet,shortlist)
    if args.self_test:
        n=self_test(packet,shortlist)
        print(f"PASS: {n}/{n} forged source, bilingual, provenance and approval mutations rejected")
    print(json.dumps(result if args.level in ("C1","ALL") else
                     {"level":args.level,"observations":0,"independently_approved":0},
                     sort_keys=True))

if __name__=="__main__":
    main()
