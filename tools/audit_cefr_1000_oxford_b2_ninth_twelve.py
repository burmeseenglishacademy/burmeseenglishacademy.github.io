#!/usr/bin/env python3
"""Fail-closed B2 ninth Oxford publisher evidence audit; NEVER an independent review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF3000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''[["shipping","C1",7,1771,"shipping n.","5000","The example concerns freight transport and a carrier's arrival confirmation, not romantic pairing or merely ships as a group."],["therapy","B2",12,3251,"therapy n.","3000","Physical rehabilitation treatment, not psychotherapy alone; distinguish treatment method and clinical advice."],["witness","B2",12,3313,"witness n., v.","3000","Noun eyewitness at a crossing, not legal testimony as a verb or a formal signing witness."],["aim","B1",7,1803,"aim v., n.","3000","Verb intend to reduce errors, not point a weapon; Oxford B1 word/POS conflicts with draft B2."],["clinical","C1",4,908,"clinical adj.","5000","Medical training/patient-care sense, not emotionally detached or plain appearance; Oxford C1 conflicts with draft B2."],["defeat","B2",11,2765,"defeat v., n.","3000","Verb win against a team, not a noun loss or overcoming an abstract difficulty."],["democracy","B2",1,158,"democracy n.","5000","Political system with elected representation; distinguish a particular democratic country from a system of government."],["suspect","B2",12,3239,"suspect v., n.","3000","Verb believe without proof, not a person under suspicion (noun); the technician's faulty-cable hypothesis remains uncertain."],["trend","B1",10,2527,"trend n.","3000","Noun general direction of change, not a short-lived fashion; Oxford B1 conflicts with provisional B2."],["wealth","B2",12,3301,"wealth n.","3000","Money/property assets, not a figurative abundance of ideas; consider natural Myanmar distinction from income."],["document","A2",5,1139,"document n.","3000","Noun electronic/written record, not verb document an event; Oxford A2 conflicts with provisional B2."],["employee","A2",5,1162,"employee n.","3000","Paid worker under an employer, not self-employed contractor or employer; Oxford A2 conflicts with provisional B2."]]''')
LEADS = json.loads(r'''[{"word":"shipping","url":"https://www.oxfordlearnersdictionaries.com/definition/english/shipping","observed_on":"2026-10-30","entry_pos":"noun","sense_number":2,"sense_summary":"transporting people or goods by ship or another means; distinct from collective ships and informal romantic-pairing sense","example_alignment":"The shipping company confirmed the container's arrival.","dictionary_excerpt_locator":"lines 120-130; contrast senses 1 and 3 at 107-117 and 131-134","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"clinical","url":"https://www.oxfordlearnersdictionaries.com/definition/english/clinical","observed_on":"2026-10-30","entry_pos":"adjective","sense_number":1,"sense_summary":"patient examination and treatment, especially clinical training; separate cold-detached and bare-room senses","example_alignment":"The students gained clinical experience at the hospital.","dictionary_excerpt_locator":"lines 103-110; contrast senses 2 and 3 at 122-133","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"aim","url":"https://www.oxfordlearnersdictionaries.com/definition/english/aim_1","observed_on":"2026-10-30","entry_pos":"verb","sense_number":1,"sense_summary":"try or plan to achieve an outcome; aim to plus infinitive; not point a weapon","example_alignment":"We aim to reduce delivery errors this month.","dictionary_excerpt_locator":"lines 112-128; contrast weapon sense 4 at 170-176","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"witness","url":"https://www.oxfordlearnersdictionaries.com/definition/english/witness_1","observed_on":"2026-10-30","entry_pos":"noun","sense_number":1,"sense_summary":"person who saw an event and can describe it, distinct from a witness giving evidence in court","example_alignment":"A witness described what happened at the crossing.","dictionary_excerpt_locator":"lines 105-127; contrast court sense 2 at 151-161","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"}]''')
TASK = "Independent human reviewer must inspect dated exact-sense publisher evidence, resolve any CEFR/POS conflicts, verify English definition, fluent Myanmar meaning, original example grammar, British pronunciation, historical provenance and content-bound independent signoff. Automated word/POS checks do not approve the entry."

def need(ok, reason):
    if not ok:
        raise ValueError(reason)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(sha == SHORT_SHA, "Frozen shortlist Git blob drift")
    need(shortlist.get("counts_by_level") == {k: 200 for k in LEVELS}
         and shortlist.get("independently_approved_by_level") == {k: 0 for k in LEVELS}
         and len(shortlist.get("entries", [])) == 1000, "Scope or approvals drift")
    by_word = {e["word"]: e for e in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist headwords")
    need(all(e.get("editorial_hold") is True and e.get("release_approved") is False
             and all(e.get("reviewed_" + k) is False for k in
                     ("english", "burmese", "example", "level", "pronunciation"))
             for e in shortlist["entries"]), "Shortlist false review/approval")
    need(set(packet) == {"schema","scope","status","observed_on","shortlist_blob_sha",
         "record_count","counts_by_level","publisher_reference_level_counts",
         "word_pos_discrepancies","independently_approved_count","source_limitations",
         "records","direct_dictionary_sense_leads","independent_human_review_receipts",
         "audio_real_listening_signoffs","release_approved"}, "Unexpected packet keys")
    need(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status") == "B2_NINTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet.get("observed_on") == "2026-10-30"
         and packet.get("shortlist_blob_sha") == SHORT_SHA
         and packet.get("record_count") == 12
         and packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}
         and packet.get("publisher_reference_level_counts") == {"A2":2,"B1":2,"B2":6,"C1":2}
         and packet.get("word_pos_discrepancies") == 6
         and packet.get("independently_approved_count") == 0
         and packet.get("independent_human_review_receipts") == []
         and packet.get("audio_real_listening_signoffs") == []
         and packet.get("release_approved") is False,
         "Packet metadata, scope or forged approval")
    need(isinstance(packet.get("source_limitations"), str)
         and "not exact-sense CEFR approvals" in packet["source_limitations"]
         and "No frozen shortlist edits" in packet["source_limitations"],
         "Publisher evidence limitations erased")
    rows = packet.get("records")
    need(isinstance(rows, list) and len(rows) == 12, "Wrong record count")
    need(len({x.get("word") for x in rows}) == 12, "Duplicate batch headwords")
    for row, (word, cefr, page, line, excerpt, list_name, risk) in zip(rows, EXPECTED):
        src = by_word[word]
        need(set(row) == {"word","level","part_of_speech","shortlist_snapshot",
             "shortlist_provenance","publisher_source","editorial_risk",
             "independent_reviewer_task","editorial_hold","independently_reviewed",
             "release_approved","independent_reviewer_receipt"}, "Unexpected record keys")
        need(row.get("word") == word and row.get("level") == "B2"
             and row.get("part_of_speech") == src["part_of_speech"],
             "Word, POS or level drift")
        need(row.get("shortlist_snapshot") == {
             "english_definition": src["english_definition"],
             "myanmar_meaning": src["burmese_meaning"],
             "example_sentence": src["example_sentence"]}, "English/Myanmar/example drift")
        need(row.get("shortlist_provenance") == {
             k: src[k] for k in ("source_path","source_index","source_blob_sha")},
             "Historical Git provenance drift")
        need(row.get("publisher_source") == {
             "publisher":"Oxford University Press",
             "title":"The Oxford " + list_name + " by CEFR level",
             "url":PDF3000 if list_name == "3000" else PDF5000,"observed_on":"2026-10-30","pdf_page":page,
             "extracted_line":line,"source_excerpt":excerpt,
             "source_cefr_level":cefr,
             "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
             "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher evidence drift")
        need(row.get("editorial_risk") == risk and
             row.get("independent_reviewer_task") == TASK,
             "Sense-risk or independent reviewer task drift")
        need(row.get("editorial_hold") is True
             and row.get("independently_reviewed") is False
             and row.get("release_approved") is False
             and row.get("independent_reviewer_receipt") is None,
             "Fabricated independent review")
    need(packet.get("direct_dictionary_sense_leads") == LEADS,
         "Direct dictionary sense evidence/locator drift")
    return {"scope":"STAGING_ONLY_NOT_INDEPENDENT_APPROVAL",
            "B2_first_pass_written":200,"B2_independently_approved":0,
            "new_word_pos_observations":12,"publisher_A2":2,
            "publisher_B1":2,"publisher_B2":6,"publisher_C1":2,"direct_dictionary_sense_leads":4,
            "real_audio_listening_signoffs":0,"release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    baseline = audit(packet, shortlist)
    mutations = []
    for key, value in [
        ("scope","CEFR_5000"),("status","APPROVED"),
        ("observed_on","2026-10-29"),("shortlist_blob_sha","fake"),
        ("record_count",11),("counts_by_level",{"B2":12}),
        ("publisher_reference_level_counts",{"B2":12}),
        ("word_pos_discrepancies",0),("independently_approved_count",1),
        ("source_limitations","approved"),("independent_human_review_receipts",[{"fake":True}]),
        ("audio_real_listening_signoffs",[{"fake":True}]),("release_approved",True)]:
        mutations.append(("metadata " + key, lambda p,k=key,v=value: p.__setitem__(k,v)))
    mutations.append(("missing record",lambda p: p["records"].pop()))
    mutations.append(("duplicate record",lambda p: p["records"].__setitem__(1,copy.deepcopy(p["records"][0]))))
    for i in range(12):
        for key, value in [
            ("word","forged"),("level","C1"),("part_of_speech","FORGED_POS"),
            ("editorial_risk","forged"),("independent_reviewer_task","self-approved"),
            ("editorial_hold",False),("independently_reviewed",True),
            ("release_approved",True),("independent_reviewer_receipt",{"fake":True})]:
            mutations.append((str(i)+":"+key,lambda p,i=i,k=key,v=value: p["records"][i].__setitem__(k,v)))
        for key, value in [("english_definition","forged"),("myanmar_meaning","forged"),
                           ("example_sentence","forged")]:
            mutations.append((str(i)+":snapshot:"+key,lambda p,i=i,k=key,v=value:
                              p["records"][i]["shortlist_snapshot"].__setitem__(k,v)))
        for key, value in [("source_path","forged"),("source_index",-1),
                           ("source_blob_sha","forged")]:
            mutations.append((str(i)+":provenance:"+key,lambda p,i=i,k=key,v=value:
                              p["records"][i]["shortlist_provenance"].__setitem__(k,v)))
        for key, value in [("publisher","forged"),("title","forged"),
                           ("url","https://example.com/fake.pdf"),
                           ("observed_on","2026-10-29"),("pdf_page",0),
                           ("extracted_line",-1),("source_excerpt","forged"),
                           ("source_cefr_level","A1"),("evidence_scope","EXACT_SENSE_APPROVED"),
                           ("access","NOT_DIRECT")]:
            mutations.append((str(i)+":publisher:"+key,lambda p,i=i,k=key,v=value:
                              p["records"][i]["publisher_source"].__setitem__(k,v)))
    for i in range(4):
        for key, value in [("word","forged"),("url","https://example.com/fake"),
                           ("observed_on","2026-10-29"),("entry_pos","FORGED_POS"),
                           ("sense_number",999),("sense_summary","forged"),
                           ("example_alignment","forged"),("dictionary_excerpt_locator","forged"),
                           ("verification_scope","INDEPENDENT_APPROVAL")]:
            mutations.append((str(i)+":lead:"+key,lambda p,i=i,k=key,v=value:
                              p["direct_dictionary_sense_leads"][i].__setitem__(k,v)))
    for label, change in mutations:
        forged = copy.deepcopy(packet)
        change(forged)
        need(forged != packet, "Ineffective negative test: " + label)
        try:
            audit(forged, shortlist)
        except ValueError:
            continue
        raise AssertionError("Forged source or fake approval accepted: " + label)
    return baseline, len(mutations)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORT.read_text(encoding="utf-8"))
    if args.self_test:
        report, n = self_test(packet,shortlist)
        print("PASS: rejected %d/%d ninth B2 publisher, bilingual and signoff mutations" % (n,n))
    else:
        report = audit(packet,shortlist)
    if args.level in ("B2","ALL"):
        print(json.dumps(report,ensure_ascii=False,sort_keys=True))
    else:
        print(json.dumps({"level":args.level,"B2_research_only":True,
                          "release":"BLOCKED_STAGING_ONLY"},sort_keys=True))

if __name__ == "__main__":
    main()
