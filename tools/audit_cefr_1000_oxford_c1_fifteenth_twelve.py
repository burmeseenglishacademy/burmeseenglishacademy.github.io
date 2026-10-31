#!/usr/bin/env python3
"""Fail-closed Oxford C1 fifteenth research packet audit; staging only.

All twelve new exact word/POS pairs are ABSENT from two inspected Oxford core lists.
Absence is NOT CEFR classification; dictionary pages are sense leads only.
No automatic independent linguistic approval, listening, device or launch claim.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = "draft/CEFR-1000-OXFORD-C1-FIFTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-11-01.json"
PACKET_BLOB = "9151e40e7b43fac43f4ef6b1f9f0e64e678885e5"
SHORTLIST = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
HISTORICAL = "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json"
HISTORICAL_BLOB = "7eaf88b9ed7687b26ccde713262f10fb209743a8"
WORDS = ("embellish","endemic","enigma","ephemeral","exacerbate","exonerate",
         "fallacy","fervent","galvanize","incongruous","introspection","juxtapose")
DICTIONARY = ("embellish","endemic","exonerate","juxtapose")
PROPOSALS = ("embellish","endemic","exonerate","juxtapose")
PDF3 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
DATE = "2026-11-01"
STATUS = "C1_FIFTEENTH_TWELVE_ALL_CORE_LIST_UNLISTED_FOUR_DIRECT_DICTIONARY_SENSE_LEADS_ALL_HELD"
LEVELS = ("A1","A2","B1","B2","C1")

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load():
    for path, expected in ((PATH,PACKET_BLOB),(SHORTLIST,SHORTLIST_BLOB),
                           (HISTORICAL,HISTORICAL_BLOB)):
        require(sha(path) == expected, "Historical or immutable Git blob changed: "+path)
    return [json.loads((ROOT / p).read_text(encoding="utf8"))
            for p in (PATH, SHORTLIST, HISTORICAL)]

def audit(packet, shortlist, historical, reference):
    require(packet == reference, "Pinned source research packet was tampered")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == STATUS and packet.get("observed_on") == DATE
            and packet.get("shortlist_blob_sha") == SHORTLIST_BLOB,
            "Wrong project, source, observation date or status")
    require(packet.get("record_count") == 12
            and packet.get("counts_by_level") == {x:(12 if x=="C1" else 0) for x in LEVELS}
            and packet.get("publisher_reference_level_counts") ==
                {**{x:0 for x in LEVELS},"UNLISTED":12}
            and packet.get("direct_dictionary_sense_leads") == 4,
            "Publisher research count drift")
    require(packet.get("independently_approved_count") == 0
            and packet.get("independent_human_review_receipts") == []
            and packet.get("audio_real_listening_signoffs") == []
            and packet.get("release_approved") is False,
            "Fabricated independent review, audio or release evidence")
    entries = shortlist.get("entries")
    require(isinstance(entries,list) and len(entries)==1000
            and shortlist.get("counts_by_level") == {x:200 for x in LEVELS}
            and shortlist.get("independently_approved_by_level") == {x:0 for x in LEVELS},
            "Shortlist level count or independent approval changed")
    require(len({r["word"] for r in entries}) == 1000,
            "Duplicated shortlist headwords")
    by_word = {r["word"]:r for r in entries}
    rows = packet.get("records")
    require(isinstance(rows,list) and tuple(r.get("word") for r in rows) == WORDS,
            "Wrong C1 word set, order or count")
    for row in rows:
        word = row["word"]
        entry = by_word[word]
        require(entry["level"] == row.get("level") == "C1"
                and entry["part_of_speech"] == row.get("part_of_speech"),
                "Draft POS/level changed: "+word)
        require(row.get("shortlist_snapshot") ==
                {"english_definition":entry["english_definition"],
                 "myanmar_meaning":entry["burmese_meaning"],
                 "example_sentence":entry["example_sentence"]},
                "Frozen English/Myanmar/example altered: "+word)
        prov = {"source_path":entry["source_path"],
                "source_index":entry["source_index"],
                "source_blob_sha":entry["source_blob_sha"]}
        require(row.get("shortlist_provenance") == prov
                and prov["source_path"] == HISTORICAL
                and prov["source_blob_sha"] == HISTORICAL_BLOB,
                "Historical source provenance changed: "+word)
        idx = prov["source_index"]
        originals = historical.get("entries")
        require(type(idx) is int and 0 <= idx < len(originals),
                "Historical source index invalid: "+word)
        old = originals[idx]
        require(old.get("word") == word
                and old.get("part_of_speech") == entry["part_of_speech"]
                and old.get("level",old.get("proposed_level")) == "C1"
                and all(old[k] == entry[k] for k in
                        ("english_definition","burmese_meaning","example_sentence")),
                "Historical Git source row mismatch: "+word)
        pub = row.get("publisher_source")
        require(pub == {"publisher":"Oxford University Press",
                "title":"The Oxford 3000 and Oxford 5000 by CEFR level (both inspected)",
                "url":PDF3,"additional_inspected_url":PDF5,"observed_on":DATE,
                "pdf_page":None,"extracted_line":None,"source_excerpt":None,
                "source_cefr_level":None,
                "evidence_scope":"NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL",
                "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Invented publisher CEFR level, PDF locator or source: "+word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None
                and "independent HUMAN" in row.get("independent_reviewer_task","")
                and len(row.get("editorial_risk","")) > 75,
                "False human approval or missing exact-sense risk: "+word)
        d = row.get("dictionary_sense_lead")
        if word in DICTIONARY:
            require(isinstance(d,dict) and d.get("observed_on") == DATE
                    and d.get("url","").startswith("https://www.oxfordlearnersdictionaries.com/definition/english/")
                    and d.get("sense_number") == (2 if word == "embellish" else 1)
                    and d.get("access") == "DIRECT_OFFICIAL_PUBLISHER_DICTIONARY_WEB_TEXT"
                    and d.get("evidence_scope") == "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and len(d.get("sense_summary","")) > 80,
                    "Forged Oxford dictionary lead: "+word)
        else:
            require(d is None,"Invented dictionary access: "+word)
        p = row.get("editorial_rewrite_candidate")
        if word in PROPOSALS:
            require(isinstance(p,dict)
                    and p.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and all(len(p.get(k,""))>20 for k in
                        ("english_definition","myanmar_meaning","example_sentence")),
                    "Invalid unapproved bilingual proposal: "+word)
        else:
            require(p is None,"Invented rewrite proposal: "+word)
    return {"C1":{"written":200,"independently_approved":0,
                  "new_core_list_absence_observations":12,
                  "new_direct_dictionary_sense_leads":4},
            "release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist, historical):
    cases=[]
    for i,word in enumerate(WORDS):
        for label,fn in [
            ("word",lambda r:r.update(word="fake")),
            ("pos",lambda r:r.update(part_of_speech="noun" if r["part_of_speech"]!="noun" else "verb")),
            ("english",lambda r:r["shortlist_snapshot"].update(english_definition="forged")),
            ("myanmar",lambda r:r["shortlist_snapshot"].update(myanmar_meaning="အတု")),
            ("example",lambda r:r["shortlist_snapshot"].update(example_sentence="fake")),
            ("index",lambda r:r["shortlist_provenance"].update(source_index=999)),
            ("blob",lambda r:r["shortlist_provenance"].update(source_blob_sha="0"*40)),
            ("source",lambda r:r["publisher_source"].update(url="https://example.invalid")),
            ("cefr",lambda r:r["publisher_source"].update(source_cefr_level="C1")),
            ("locator",lambda r:r["publisher_source"].update(pdf_page=1)),
            ("risk",lambda r:r.update(editorial_risk="")),
            ("approval",lambda r:r.update(release_approved=True)),
            ("review",lambda r:r.update(independently_reviewed=True)),
            ("receipt",lambda r:r.update(independent_reviewer_receipt={"fake":True})),
        ]:
            cases.append((i,label,fn))
    for i,label,fn in cases:
        altered=copy.deepcopy(packet)
        fn(altered["records"][i])
        try: audit(altered,shortlist,historical,packet)
        except ValueError: continue
        raise AssertionError("Forged research accepted: "+WORDS[i]+"/"+label)
    n=len(cases)
    for word in DICTIONARY:
        i=WORDS.index(word)
        for fn in (lambda r:r.update(dictionary_sense_lead=None),
                   lambda r:r["dictionary_sense_lead"].update(sense_summary="forged")):
            altered=copy.deepcopy(packet);fn(altered["records"][i])
            try: audit(altered,shortlist,historical,packet)
            except ValueError: n+=1;continue
            raise AssertionError("Forged dictionary sense accepted: "+word)
    for word in PROPOSALS:
        i=WORDS.index(word)
        altered=copy.deepcopy(packet)
        altered["records"][i]["editorial_rewrite_candidate"]["review_status"]="INDEPENDENTLY_APPROVED"
        try: audit(altered,shortlist,historical,packet)
        except ValueError: n+=1;continue
        raise AssertionError("Forged Myanmar approval accepted: "+word)
    for fn in (lambda p:p.update(release_approved=True),
               lambda p:p.update(independently_approved_count=12),
               lambda p:p["records"].pop(),
               lambda p:p.update(record_count=1000),
               lambda p:p.update(audio_real_listening_signoffs=[{"fake":True}])):
        altered=copy.deepcopy(packet);fn(altered)
        try: audit(altered,shortlist,historical,packet)
        except ValueError: n+=1;continue
        raise AssertionError("Forged packet status accepted")
    return n

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    packet,shortlist,historical=load()
    report=audit(packet,shortlist,historical,packet)
    if args.self_test:
        n=self_test(packet,shortlist,historical)
        print("PASS: rejected %d/%d forged C1 research/approval mutations" % (n,n))
    print(json.dumps(report if args.level in ("C1","ALL") else
                     {args.level:{"written":200,"independently_approved":0},
                      "release":"BLOCKED_STAGING_ONLY"},sort_keys=True))

if __name__=="__main__":
    main()
