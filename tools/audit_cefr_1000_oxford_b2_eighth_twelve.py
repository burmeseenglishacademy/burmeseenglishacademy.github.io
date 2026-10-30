#!/usr/bin/env python3
"""Fail-closed B2 eighth Oxford publisher evidence audit; NEVER an independent review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-EIGHTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''[["convention","B2",1,130,"convention n.","The example uses a professional gathering; do not conflate this sense with a social custom or an international treaty."],["equivalent","B2",1,216,"equivalent n., adj.","Draft is adjective: qualifications comparable in value or standard, not the separate noun entry; confirm intended comparison and fluent Myanmar."],["universal","B2",3,672,"universal adj.","A concern shared across people, not a claim that every single person has identical access or circumstances."],["infrastructure","B2",2,332,"infrastructure n.","Physical and organisational public systems; Myanmar should include utilities/services as well as buildings."],["recognition","B2",2,515,"recognition n.","Public appreciation for research, not visual identification or formal legal recognition; distinguish Myanmar senses."],["mechanism","B2",2,390,"mechanism n.","Abstract process explaining operation, not necessarily a physical machine mechanism; confirm technical Burmese collocation."],["acquisition","C1",3,727,"acquisition n.","Business takeover in example, not acquiring a language or a single purchased object; B2 draft versus Oxford C1 word/POS needs independent decision."],["outstanding","B2",2,442,"outstanding adj.","Draft means excellent service, not an unpaid invoice or unfinished task; preserve sense in Myanmar."],["primarily","B2",2,480,"primarily adv.","Mainly intended for new employees; do not imply exclusive eligibility, and verify adverb placement."],["circuit","B2",1,92,"circuit n.","Electrical closed path, not race track, legal circuit or tour; check electrical technical precision in Myanmar."],["healthcare","B2",2,299,"healthcare n.","Medical services and systems, not only one hospital or treatment; Myanmar compound fluency needs human review."],["membership","B2",2,393,"membership n.","Status/benefits of belonging to an organisation; distinguish membership fee, membership list and member count."]]''')
LEADS = json.loads(r'''[{"word":"convention","url":"https://www.oxfordlearnersdictionaries.com/definition/english/convention","observed_on":"2026-10-30","entry_pos":"noun","sense_number":2,"sense_summary":"large professional or political meeting; distinct from social custom and treaty senses","example_alignment":"The annual convention attracted teachers from many countries.","dictionary_excerpt_locator":"lines 148-179","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"equivalent","url":"https://www.oxfordlearnersdictionaries.com/definition/english/equivalent_2","observed_on":"2026-10-30","entry_pos":"adjective","sense_number":1,"sense_summary":"equal in value, amount, meaning or importance; adjective distinct from noun entry","example_alignment":"The two qualifications are considered equivalent.","dictionary_excerpt_locator":"lines 88-123","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"acquisition","url":"https://www.oxfordlearnersdictionaries.com/definition/english/acquisition","observed_on":"2026-10-30","entry_pos":"noun","sense_number":3,"sense_summary":"purchase of a company, business asset or land; distinct from skill acquisition","example_alignment":"The acquisition of the smaller firm took six months.","dictionary_excerpt_locator":"lines 136-150","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"},{"word":"outstanding","url":"https://www.oxfordlearnersdictionaries.com/definition/english/outstanding","observed_on":"2026-10-30","entry_pos":"adjective","sense_number":1,"sense_summary":"extremely good or excellent; distinct from unpaid/unfinished sense 2","example_alignment":"The team received an award for outstanding service.","dictionary_excerpt_locator":"lines 105-129 and 142-151","verification_scope":"DIRECT_DICTIONARY_SENSE_DESCRIPTION_NOT_INDEPENDENT_CEFR_APPROVAL"}]''')
TASK = "Independent human reviewer must inspect dated exact-sense publisher evidence, resolve any CEFR/POS conflicts, verify English definition, fluent Myanmar meaning, original example grammar, British pronunciation, historical provenance and content-bound independent signoff. Automated word/POS checks do not approve the entry."

def need(ok, reason):
    if not ok:
        raise ValueError(reason)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
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
         and packet.get("status") == "B2_EIGHTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet.get("observed_on") == "2026-10-30"
         and packet.get("shortlist_blob_sha") == SHORT_SHA
         and packet.get("record_count") == 12
         and packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}
         and packet.get("publisher_reference_level_counts") == {"B2":11,"C1":1}
         and packet.get("word_pos_discrepancies") == 1
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
    for row, (word, cefr, page, line, excerpt, risk) in zip(rows, EXPECTED):
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
             "title":"The Oxford 5000 by CEFR level",
             "url":PDF,"observed_on":"2026-10-30","pdf_page":page,
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
            "new_word_pos_observations":12,"publisher_B2":11,
            "publisher_C1":1,"direct_dictionary_sense_leads":4,
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
            ("word","forged"),("level","C1"),("part_of_speech","verb"),
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
                           ("observed_on","2026-10-29"),("entry_pos","verb"),
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
        print("PASS: rejected %d/%d eighth B2 publisher, bilingual and signoff mutations" % (n,n))
    else:
        report = audit(packet,shortlist)
    if args.level in ("B2","ALL"):
        print(json.dumps(report,ensure_ascii=False,sort_keys=True))
    else:
        print(json.dumps({"level":args.level,"B2_research_only":True,
                          "release":"BLOCKED_STAGING_ONLY"},sort_keys=True))

if __name__ == "__main__":
    main()
