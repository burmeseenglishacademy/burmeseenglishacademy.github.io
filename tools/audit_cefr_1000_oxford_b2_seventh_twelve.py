#!/usr/bin/env python3
"""Fail-closed seventh B2 Oxford evidence audit; research is not independent approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-SEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF3000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
LEVELS = ("A1","A2","B1","B2","C1")
EXPECTED = json.loads(r'''[["speaker","A2",6,1645,"speaker n.","A person giving a lecture, not an electronic loudspeaker; check guest-speaker context and Burmese distinction."],["percentage","B1",9,2273,"percentage n.","Percentage of returns versus percentage-point change; Myanmar rendering must not confuse percentage with per cent."],["household","B2",11,2914,"household n.","One household may include non-relatives; avoid equating it with only a nuclear family."],["occur","B1",9,2247,"occur v.","Occurrence of power cuts is a happen sense; distinguish occur to someone (idea) and check Myanmar verb collocation."],["alongside","C1",3,766,"alongside prep.","The building example uses physically next to, not working together with; publisher dictionary badge conflicts with PDF C1."],["anxiety","B2",1,31,"anxiety n.","Anxiety as ordinary worry versus clinical anxiety disorder; do not imply a diagnosis in Myanmar."],["charity","A2",4,1038,"charity n.","Example refers to an organization, not charitable kindness or donations in general; dictionary badge conflicts with PDF A2."],["discovery","A2",5,1134,"discovery n.","The act/result of discovering; clarify how the scientific finding changed understanding and natural Myanmar phrasing."],["formal","A2",5,1231,"formal adj.","A formal complaint means made through official procedures, not necessarily a polite or formal tone."],["formula","C1",5,1229,"formula n.","Mathematical rule in example, not chemical formula, recipe or method for success; dictionary badge conflicts with PDF C1."],["innocent","B1",8,2152,"innocent adj.","Not guilty in legal context, not naive/harmless; avoid equating acquittal with proof of factual innocence."],["mystery","B1",9,2225,"mystery n.","An unexplained cause, not necessarily a detective-fiction genre or a deliberate secret."]]''')
LEADS = json.loads(r'''[{"word":"alongside","url":"https://www.oxfordlearnersdictionaries.com/definition/english/alongside_2","observed_on":"2026-10-30","entry_pos":"preposition","sense_number":1,"sense_summary":"physically next to / at the side of","example_alignment":"The new building stands alongside the old library.","dictionary_excerpt_locator":"lines 88-114","dictionary_badge_observation":"Oxford 3000 B2 badge shown at lines 140-144, conflicting with Oxford 5000 PDF C1 preposition entry","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"formula","url":"https://www.oxfordlearnersdictionaries.com/definition/english/formula","observed_on":"2026-10-30","entry_pos":"noun","sense_number":1,"sense_summary":"mathematical symbols representing a rule or law","example_alignment":"The engineer used a formula to calculate the area.","dictionary_excerpt_locator":"lines 88-123","dictionary_badge_observation":"Oxford 3000 B2 badge shown at lines 214-218, conflicting with Oxford 5000 PDF C1 noun entry","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"charity","url":"https://www.oxfordlearnersdictionaries.com/definition/english/charity","observed_on":"2026-10-30","entry_pos":"noun","sense_number":1,"sense_summary":"an organisation helping people in need","example_alignment":"The charity provides meals for older residents.","dictionary_excerpt_locator":"lines 88-117","dictionary_badge_observation":"Oxford 3000 B2 badge shown at lines 223-227, conflicting with Oxford 3000 PDF A2 noun entry","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"percentage","url":"https://www.oxfordlearnersdictionaries.com/definition/english/percentage","observed_on":"2026-10-30","entry_pos":"noun","sense_number":1,"sense_summary":"number, amount or rate expressed out of one hundred","example_alignment":"The percentage of returned products fell this month.","dictionary_excerpt_locator":"lines 88-128","dictionary_badge_observation":"Maths and measurement B1 topic label at line 128 aligns with Oxford 3000 PDF B1 noun entry; topic label is not an exact-sense CEFR signoff","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"}]''')
TASK = "Independent human reviewer must verify the intended exact sense against dated publisher dictionary evidence, publisher CEFR classification conflicts, English definition, fluent Myanmar meaning, original example grammar, British pronunciation, provenance, and content-bound independent signoff. Word/POS lists and automated checks are not independent exact-sense CEFR approval."

def need(test, reason):
    if not test:
        raise ValueError(reason)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(blob == SHORT_SHA, "Frozen shortlist blob drift")
    need(shortlist.get("counts_by_level") == {k:200 for k in LEVELS}
         and shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}
         and len(shortlist.get("entries", [])) == 1000, "Shortlist scope or approval drift")
    by_word = {e["word"]:e for e in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist headwords")
    for entry in shortlist["entries"]:
        need(entry.get("editorial_hold") is True
             and entry.get("release_approved") is False
             and all(entry.get("reviewed_"+x) is False for x in
                     ("english","burmese","example","level","pronunciation")),
             "Unapproved shortlist status drift")
    need(packet.get("schema") == 1
         and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status") == "B2_SEVENTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet.get("observed_on") == "2026-10-30"
         and packet.get("shortlist_blob_sha") == SHORT_SHA
         and packet.get("record_count") == 12
         and packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}
         and packet.get("publisher_reference_level_counts") == {"A2":4,"B1":4,"B2":2,"C1":2}
         and packet.get("word_pos_discrepancies") == 10
         and packet.get("independently_approved_count") == 0
         and packet.get("release_approved") is False
         and packet.get("independent_human_review_receipts") == []
         and packet.get("audio_real_listening_signoffs") == [],
         "Publisher evidence metadata, fake approval or release drift")
    need(isinstance(packet.get("source_limitations"), str)
         and "not exact-sense CEFR" in packet["source_limitations"]
         and "conflict" in packet["source_limitations"], "Evidence limitations erased")
    need(len(packet.get("records", [])) == 12, "Evidence record count drift")
    for row, (word, cefr, page, line, excerpt, risk) in zip(packet["records"], EXPECTED):
        original = by_word[word]
        need(row.get("word") == word and row.get("level") == "B2"
             and row.get("part_of_speech") == original["part_of_speech"],
             "Word/level/POS drift")
        need(row.get("shortlist_snapshot") == {
             "english_definition": original["english_definition"],
             "myanmar_meaning": original["burmese_meaning"],
             "example_sentence": original["example_sentence"]}, "Bilingual/example snapshot drift")
        need(row.get("shortlist_provenance") == {k:original[k] for k in
             ("source_path","source_index","source_blob_sha")}, "Git source provenance drift")
        need(row.get("publisher_source") == {
             "publisher":"Oxford University Press",
             "title":"The Oxford 5000 by CEFR level" if cefr in ("B2","C1") and word in ("anxiety","alongside","formula") else "The Oxford 3000 by CEFR level",
             "url": PDF5000 if word in ("anxiety","alongside","formula") else PDF3000,
             "observed_on":"2026-10-30",
             "pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,
             "source_cefr_level":cefr,
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher locator/source drift")
        need(row.get("editorial_risk") == risk
             and row.get("independent_reviewer_task") == TASK,
             "Reviewer task or risk drift")
        need(row.get("editorial_hold") is True
             and row.get("independently_reviewed") is False
             and row.get("release_approved") is False
             and row.get("independent_reviewer_receipt") is None,
             "Fabricated independent signoff")
    need(packet.get("direct_dictionary_sense_leads") == LEADS,
         "Dictionary sense or publisher-badge conflict erased")
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS,"ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORT.read_text(encoding="utf-8"))
    audit(packet, shortlist)
    rejected = 0
    if args.self_test:
        mutations = [
            ("word","fabricated"),("level","C1"),("part_of_speech","fabricated"),
            ("shortlist_snapshot",{"english_definition":"fabricated"}),
            ("shortlist_provenance",{"source_blob_sha":"0"*40}),
            ("publisher_source",{"source_cefr_level":"fabricated"}),
            ("editorial_risk","fabricated"),
            ("independent_reviewer_task","fabricated"),
            ("editorial_hold",False),("independently_reviewed",True),
            ("release_approved",True),
            ("independent_reviewer_receipt",{"reviewer":"fabricated"})
        ]
        for i in range(12):
            for field, value in mutations:
                forged = copy.deepcopy(packet)
                need(forged["records"][i][field] != value,
                     "Ineffective mutation: %s/%s" % (i,field))
                forged["records"][i][field] = value
                try:
                    audit(forged, shortlist)
                except (ValueError, KeyError, TypeError):
                    rejected += 1
                else:
                    raise AssertionError("Forged evidence accepted: %s/%s" % (i,field))
        for i in range(4):
            for field, value in [
                ("sense_number",99),("sense_summary","fabricated"),
                ("example_alignment","fabricated"),
                ("dictionary_badge_observation","fabricated"),
                ("verification_scope","INDEPENDENT_APPROVED"),
                ("url","https://invalid.example")]:
                forged = copy.deepcopy(packet)
                need(forged["direct_dictionary_sense_leads"][i][field] != value,
                     "Ineffective dictionary mutation")
                forged["direct_dictionary_sense_leads"][i][field] = value
                try:
                    audit(forged, shortlist)
                except (ValueError, KeyError, TypeError):
                    rejected += 1
                else:
                    raise AssertionError("Forged dictionary lead accepted")
        for field, value in [
            ("record_count",11),("word_pos_discrepancies",0),
            ("publisher_reference_level_counts",{"B2":12}),
            ("observed_on","2026-10-29"),
            ("independently_approved_count",1),
            ("shortlist_blob_sha","0"*40),
            ("source_limitations","publisher verified exact sense"),
            ("independent_human_review_receipts",[{"reviewer":"fabricated"}]),
            ("audio_real_listening_signoffs",[{"listener":"fabricated"}]),
            ("release_approved",True)]:
            forged = copy.deepcopy(packet)
            need(forged[field] != value, "Ineffective metadata mutation")
            forged[field] = value
            try:
                audit(forged, shortlist)
            except (ValueError, KeyError, TypeError):
                rejected += 1
            else:
                raise AssertionError("Forged metadata accepted")
        need(rejected == 178, "Mutation rejection count drift")
        print("PASS: rejected 178/178 forged source, bilingual, dictionary and approval mutations")
    print(json.dumps({"level":args.level,"observations":12,
                      "publisher_levels":{"A2":4,"B1":4,"B2":2,"C1":2},
                      "independent_approvals":0,
                      "adversarial_mutations_rejected":rejected,
                      "status":"PASS_STRUCTURE_STAGING_ONLY_NO_DEPLOY"},sort_keys=True))

if __name__ == "__main__":
    main()
