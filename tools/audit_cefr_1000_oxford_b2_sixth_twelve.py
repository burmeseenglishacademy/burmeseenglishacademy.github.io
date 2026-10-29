#!/usr/bin/env python3
"""Fail-closed sixth B2 Oxford publisher word/POS packet audit; never independent approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-SIXTH-TWELVE-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''[["extensive",1,238,"extensive adj.","Distinguish broad geographical coverage from severe/large-scale damage; check Myanmar modifier in the storm example."],["formation",2,260,"formation n.","Committee formation is an establishment process; distinguish military formation and rock formation senses."],["partnership",2,455,"partnership n.","Check business/institutional cooperation versus legal business-partner entity and fluent Myanmar collocation."],["principal",2,481,"principal adj.","Ensure adjective main/primary is not confused with school principal noun; verify pronunciation and example."],["steam",3,597,"steam n.","Distinguish steam from visible condensed water droplets; review Burmese rendering of vapour rising from soup."],["commander",1,106,"commander n.","Military commander versus non-military commanding role; check register and contextual translation."],["monthly",2,401,"monthly adj.","Example uses adjective before meeting; distinguish monthly adverb and monthly publication noun."],["barely",1,52,"barely adv.","Barely hear means almost unable to hear, not a low-volume description; review Myanmar adverb naturalness."],["psychological",2,495,"psychological adj.","Mind/emotion sense versus experimental psychology; avoid medical claims from the stress example."],["overcome",2,443,"overcome v.","Problem/fear overcoming sense; distinguish physical overcoming and passive overcome by emotion."],["highway",2,304,"highway n.","Check international highway versus British motorway distinctions; avoid equating all highways with motorways."],["jury",2,358,"jury n.","Legal fact-finding jury versus competition judging panel; ensure Myanmar gloss does not imply a professional judge."]]''')
TASK = "Independent human reviewer must confirm exact intended sense and CEFR teaching suitability using a dated publisher dictionary sense URL, fluent Myanmar meaning, English definition, original example grammar, British pronunciation, source provenance and content-bound signoff. Oxford PDF word/POS label alone is not exact-sense CEFR or independent approval."

def need(ok, why):
    if not ok:
        raise ValueError(why)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
    need(blob == SHORT_SHA, "Frozen shortlist Git blob drift")
    need(shortlist.get("counts_by_level") == {k: 200 for k in LEVELS}
         and shortlist.get("independently_approved_by_level") == {k: 0 for k in LEVELS}
         and len(shortlist.get("entries", [])) == 1000, "Scope or approval drift")
    need(packet.get("schema") == 1
         and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status") == "B2_SIXTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet.get("observed_on") == "2026-10-30"
         and packet.get("shortlist_blob_sha") == SHORT_SHA, "Packet status/source drift")
    need(packet.get("record_count") == 12 and len(packet.get("records", [])) == 12
         and packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}
         and packet.get("publisher_reference_level_counts") == {"B2":12}
         and packet.get("word_pos_discrepancies") == 0
         and packet.get("independently_approved_count") == 0, "Packet count or fake approval")
    need(isinstance(packet.get("source_limitations"), str)
         and "not exact-sense CEFR" in packet["source_limitations"], "Publisher evidence scope lost")
    by_word = {e["word"]: e for e in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist headwords")
    for row, (word, page, line, excerpt, risk) in zip(packet["records"], EXPECTED):
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
             "title":"The Oxford 5000 by CEFR level",
             "url":URL, "observed_on":"2026-10-30", "pdf_page":page,
             "extracted_line":line, "source_excerpt":excerpt,
             "source_cefr_level":"B2",
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher evidence altered")
        need(row.get("editorial_risk") == risk and row.get("independent_reviewer_task") == TASK,
             "Editorial risk/reviewer task altered")
        need(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
             and row.get("release_approved") is False
             and row.get("independent_reviewer_receipt") is None, "Fabricated human signoff")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS,"ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORT.read_text(encoding="utf8"))
    audit(packet, shortlist)
    rejected = 0
    if args.self_test:
        mutations = [
            ("word", "fabricated"), ("level", "C1"),
            ("part_of_speech", "fabricated"),
            ("shortlist_snapshot", {"english_definition":"fabricated"}),
            ("shortlist_provenance", {"source_blob_sha":"0"*40}),
            ("publisher_source", {"source_cefr_level":"C1"}),
            ("editorial_risk", "fabricated"),
            ("independent_reviewer_task", "fabricated"),
            ("editorial_hold", False),
            ("independently_reviewed", True),
            ("release_approved", True),
            ("independent_reviewer_receipt", {"reviewer":"fabricated"}),
        ]
        for i in range(12):
            for field, value in mutations:
                forged = copy.deepcopy(packet)
                need(forged["records"][i][field] != value,
                     "Ineffective adversarial mutation: %s/%s" % (i, field))
                forged["records"][i][field] = value
                try:
                    audit(forged, shortlist)
                except (ValueError, KeyError, TypeError):
                    rejected += 1
                else:
                    raise AssertionError("Forged source/bilingual/review accepted: %s/%s" % (i,field))
        for field, value in [
            ("record_count",11), ("independently_approved_count",1),
            ("word_pos_discrepancies",1),
            ("publisher_reference_level_counts",{"B2":11}),
            ("observed_on","2026-10-29"), ("shortlist_blob_sha","0"*40),
            ("source_limitations","publisher verified exact sense"),
        ]:
            forged = copy.deepcopy(packet)
            need(forged[field] != value, "Ineffective packet mutation: " + field)
            forged[field] = value
            try:
                audit(forged, shortlist)
            except (ValueError, KeyError, TypeError):
                rejected += 1
            else:
                raise AssertionError("Forged packet metadata accepted: " + field)
        need(rejected == 151, "Adversarial mutation count drift")
        print("PASS: rejected 151/151 forged source, translation, provenance and approval mutations")
    print(json.dumps({"level":args.level,"publisher_word_pos_observations":12,
                      "publisher_B2":12,"independent_approvals":0,
                      "adversarial_mutations_rejected":rejected,
                      "status":"PASS_STRUCTURE_STAGING_ONLY_NO_DEPLOY"},sort_keys=True))

if __name__ == "__main__":
    main()
