#!/usr/bin/env python3
"""Fail-closed B2 fifth-twelve Oxford PDF word/POS audit; NOT independent sense review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-FIFTH-TWELVE-2026-10-29.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL3000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
URL5000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
TASK = "Independent human reviewer must confirm the exact intended sense and CEFR teaching suitability using a dated dictionary sense URL, fluent Myanmar meaning, English definition, original example grammar and source provenance; word/POS-only Oxford list is not independent sense approval."
EXPECTED = json.loads(r'''[["breath","B2",10,2666,"breath n.",3000,"Noun breath versus verb breathe; breathing air, not metaphorical relief."],["brief","B2",10,2667,"brief adj.",3000,"Short duration adjective versus noun legal brief; intended temporal sense."],["conduct","B2",10,2714,"conduct v., n.",3000,"Verb organising/carrying out versus directing music or conducting electricity."],["decade","B1",8,1961,"decade n.",3000,"B1 publisher word/POS label conflicts with provisional B2; ordinary ten-year sense."],["external","B2",11,2844,"external adj.",3000,"Physical outside versus outside an organisation; definition may conflate senses."],["fantasy","B2",1,244,"fantasy n.",5000,"Imagined situation versus literary genre; example must express intended sense."],["grab","B2",11,2892,"grab v.",3000,"Sudden physical taking versus metaphorical grabbing attention."],["immediate","B1",8,2134,"immediate adj.",3000,"B1 publisher label conflicts with B2; without delay versus closest relationship."],["introduction","A2",5,1315,"introduction n.",3000,"A2 publisher label conflicts with B2; opening section versus introducing people."],["presidential","C1",6,1609,"presidential adj.",5000,"C1 publisher word/POS label conflicts with B2; political-office sense requires independent CEFR review."],["recognize","A2",6,1535,"recognize v.",3000,"A2 publisher label conflicts with B2; identification from familiarity versus formal recognition; US/UK spelling."],["regularly","B1",9,2360,"regularly adv.",3000,"B1 publisher label conflicts with B2; repeated frequency versus uniformity."]]''')

def need(ok, why):
    if not ok:
        raise ValueError(why)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
    need(blob == SHORT_SHA, "Frozen shortlist Git blob drift")
    need(shortlist.get("counts_by_level") == {k:200 for k in LEVELS}
         and shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}
         and len(shortlist.get("entries", [])) == 1000, "Scope or approval drift")
    need(packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status") == "B2_FIFTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet.get("observed_on") == "2026-10-29"
         and packet.get("shortlist_blob_sha") == SHORT_SHA, "Packet status/source drift")
    need(packet.get("record_count") == 12 and len(packet.get("records", [])) == 12
         and packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}
         and packet.get("publisher_reference_level_counts") == {"A1":0,"A2":2,"B1":3,"B2":6,"C1":1}
         and packet.get("word_pos_discrepancies") == 6
         and packet.get("lower_level_observations") == 5
         and packet.get("higher_level_observations") == 1
         and packet.get("independently_approved_count") == 0, "Packet counts or fake approval")
    by_word = {e["word"]:e for e in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist headwords")
    for row, (word, source_level, page, line, excerpt, pdf, risk) in zip(packet["records"], EXPECTED):
        need(row.get("word") == word and row.get("level") == "B2", "Word/level drift")
        original = by_word[word]
        need(row.get("part_of_speech") == original["part_of_speech"], "POS drift")
        need(row.get("shortlist_snapshot") == {
             "english_definition": original["english_definition"],
             "myanmar_meaning": original["burmese_meaning"],
             "example_sentence": original["example_sentence"]}, "English/Myanmar/example drift")
        need(row.get("shortlist_provenance") == {k:original[k] for k in
             ("source_path","source_index","source_blob_sha")}, "Historical Git provenance drift")
        need(row.get("publisher_source") == {
             "publisher":"Oxford University Press",
             "title":"The Oxford %s by CEFR level" % pdf,
             "url":URL3000 if pdf == 3000 else URL5000,
             "observed_on":"2026-10-29", "pdf_page":page,
             "extracted_line":line, "source_excerpt":excerpt,
             "source_cefr_level":source_level,
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher evidence altered")
        need(row.get("editorial_risk") == risk and row.get("independent_reviewer_task") == TASK,
             "Editorial risk/reviewer task altered")
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
             and row.get("release_approved") is False
             and row.get("independent_reviewer_receipt") is None, "Fabricated human signoff")
    return True

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS,"ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORT.read_text(encoding="utf8"))
    audit(packet, shortlist)
    print("PASS: 12 B2 draft publisher word/POS observations (5 lower, 6 match, 1 higher), zero independent approvals")
    if args.self_test:
        rejected = 0
        for i in range(12):
            for field, value in [
                ("word","fake"),("level","C1"),("part_of_speech","fake"),
                ("shortlist_snapshot",{"english_definition":"fake"}),
                ("shortlist_provenance",{"source_blob_sha":"0"*40}),
                ("publisher_source",{"source_cefr_level":"B2"}),
                ("editorial_risk","fake"),("editorial_hold",False),
                ("independently_reviewed",True),("release_approved",True),
                ("independent_reviewer_receipt",{"fake":"approval"})
            ]:
                forged = copy.deepcopy(packet)
                forged["records"][i][field] = value
                try:
                    audit(forged, shortlist)
                except (ValueError,KeyError,TypeError):
                    rejected += 1
                else:
                    raise AssertionError("Forged source, bilingual or review data passed: %s %s" % (i,field))
        need(rejected == 132, "Mutation count drift")
        print("PASS: rejected 132/132 forged publisher, bilingual, provenance and review mutations")

if __name__ == "__main__":
    main()
