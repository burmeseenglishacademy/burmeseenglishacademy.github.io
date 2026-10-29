#!/usr/bin/env python3
"""Fail-closed B1 seventh Oxford word/POS + six direct dictionary sense leads. STAGING ONLY."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-SEVENTH-TWELVE-AND-SIX-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED_META = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"B1_SEVENTH_TWELVE_DIRECT_OXFORD_WORD_POS_AND_SIX_SENSE_LEADS_EDITORIAL_HOLD","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":0,"A2":0,"B1":12,"B2":0,"C1":0},"publisher_reference_level_counts":{"A1":1,"A2":6,"B1":1,"B2":4},"word_pos_discrepancies":11,"direct_dictionary_sense_leads":6,"independently_approved_count":0,"source_limitations":"Oxford official PDF directly inspected 2026-10-30; word/POS labels only, not exact-sense CEFR, independent human English/Myanmar/example verification or real George/Emma audio listening. Six directly opened Oxford dictionary pages provide editorial sense leads only. All twelve remain editorial holds."}''')
EXPECTED_ANCHORS = json.loads(r'''[{"word":"queen","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1519,"source_excerpt":"queen n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Female sovereign in draft, not wife of a king, chess piece, playing card or queen bee; Myanmar 'ဘုရင်မ' may be context-ambiguous.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/queen","observed_on":"2026-10-30","page_text_line_start":106,"page_text_line_end":151,"editorial_interpretation":"Female ruler sense is distinct from queen consort; draft example 'addressed the nation' suggests reigning sovereign.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"heat","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1268,"source_excerpt":"heat n., v.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft noun refers to hot weather sensation, not physical heat energy, a heating appliance or verb; Myanmar 'အပူရှိန်' should be checked.","dictionary_sense_lead":null},{"word":"truly","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":12,"extracted_line":3267,"source_excerpt":"truly adv.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft example 'I truly appreciate your help' expresses sincere feeling; distinguish emphasis on quality or objective truth. Publisher B2 word/POS differs from draft B1.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/truly","observed_on":"2026-10-30","page_text_line_start":116,"page_text_line_end":140,"editorial_interpretation":"Dictionary separates sincere feeling from intensity and accurate-description senses; first sense aligns with draft.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"mission","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":11,"extracted_line":3007,"source_excerpt":"mission n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft rescue team's mission is a formally assigned important task; avoid translating as religious mission or general goal. Publisher B2 versus draft B1.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/mission","observed_on":"2026-10-30","page_text_line_start":106,"page_text_line_end":127,"editorial_interpretation":"Oxford's official important-task/assigned-job sense includes rescue missions; distinguish institutional mission or religious purpose.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"mass","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":11,"extracted_line":2991,"source_excerpt":"mass n., adj.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft 'A mass of clouds' uses large grouped quantity, not physical mass/weight or mass adjective; check countability and natural Myanmar gloss.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/mass_1","observed_on":"2026-10-30","page_text_line_start":107,"page_text_line_end":160,"editorial_interpretation":"Oxford distinguishes shapeless mass, a large quantity, and a grouped number; draft collocation needs sense-specific Myanmar.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"hall","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1263,"source_excerpt":"hall n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft large event room; distinguish entrance hall, corridor, town hall or institutional building; check 'ခန်းမ' context.","dictionary_sense_lead":null},{"word":"cell","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":10,"extracted_line":2685,"source_excerpt":"cell n.","source_cefr_level":"B2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft biological cell, not prison cell, spreadsheet cell, electrical cell or American cell phone; Myanmar 'သက်ရှိဆဲလ်' may be appropriate.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/cell","observed_on":"2026-10-30","page_text_line_start":105,"page_text_line_end":188,"editorial_interpretation":"Oxford explicitly distinguishes biological cell from prison, electrical and spreadsheet senses; draft matches biology.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"catch","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":1030,"source_excerpt":"catch v.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft physically intercepting a thrown ball, not catching illness, transport, attention or discovering wrongdoing; Myanmar 'ဖမ်းယူသည်' needs sports context.","dictionary_sense_lead":null},{"word":"sick","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":696,"source_excerpt":"sick adj.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft feeling ill is consistent with common illness sense; distinguish British 'be sick' meaning vomit and American 'sick' as ill.","dictionary_sense_lead":null},{"word":"touch","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":7,"extracted_line":1711,"source_excerpt":"touch v.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft physical hand contact with wet paint, not emotional impact or 'get in touch'; clarify polite imperative.","dictionary_sense_lead":null},{"word":"separate","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1598,"source_excerpt":"separate adj.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft distinct boxes, not verb 'to separate' or 'separate from'; Myanmar 'သီးခြားဖြစ်သော' contextual accuracy needed.","dictionary_sense_lead":null},{"word":"remain","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":9,"extracted_line":2372,"source_excerpt":"remain v.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft 'Please remain seated' is linking-verb continued-state sense; distinguish remaining quantity/existence. Oxford labels B1 word/POS, not independent sense approval.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/remain","observed_on":"2026-10-30","page_text_line_start":103,"page_text_line_end":163,"editorial_interpretation":"Oxford marks remain as relatively formal and normally non-progressive; 'remain seated' matches linking-verb state sense.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}}]''')
TASK = "Independent human reviewer must verify intended exact sense and CEFR suitability with dated publisher dictionary evidence, fluent Myanmar translation, original example grammar, British pronunciation and content-bound receipt; no publisher word/POS observation constitutes independent signoff."

def need(ok, reason):
    if not ok:
        raise ValueError(reason)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(blob == SHORT_SHA, "Frozen shortlist blob changed")
    need(shortlist.get("counts_by_level") == {k: 200 for k in LEVELS}
         and shortlist.get("independently_approved_by_level") == {k: 0 for k in LEVELS}
         and len(shortlist.get("entries", [])) == 1000, "Scope or approval drift")
    need({k:v for k,v in packet.items() if k != "records"} == EXPECTED_META,
         "Packet metadata/source scope/approval drift")
    need(len(packet.get("records", [])) == 12, "Record count drift")
    by_word = {e["word"]:e for e in shortlist["entries"]}
    need(len(by_word) == 1000, "Duplicate shortlist headwords")
    need(all(e["editorial_hold"] is True and e["release_approved"] is False
             and all(e.get("reviewed_"+k) is False for k in
                     ("english","burmese","example","level","pronunciation"))
             for e in shortlist["entries"]), "Shortlist has fabricated review")
    for row, anchor in zip(packet["records"], EXPECTED_ANCHORS):
        word = anchor["word"]
        need(word in by_word and by_word[word]["level"] == "B1", "Wrong shortlist word")
        e = by_word[word]
        expected = {
            "word":word, "level":"B1", "part_of_speech":e["part_of_speech"],
            "shortlist_snapshot":{
                "english_definition":e["english_definition"],
                "myanmar_meaning":e["burmese_meaning"],
                "example_sentence":e["example_sentence"]},
            "shortlist_provenance":{k:e[k] for k in
                ("source_path","source_index","source_blob_sha")},
            "publisher_source":anchor["publisher_source"],
            "editorial_risk":anchor["editorial_risk"],
            "dictionary_sense_lead":anchor["dictionary_sense_lead"],
            "independent_reviewer_task":TASK,
            "editorial_hold":True, "independently_reviewed":False,
            "release_approved":False, "independent_reviewer_receipt":None}
        need(row == expected, "Publisher, Myanmar, grammar, provenance or signoff mutation: "+word)
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
        edits = [
            ("word","fabricated"), ("level","C1"),
            ("part_of_speech","fabricated"),
            ("shortlist_snapshot",{"english_definition":"fabricated"}),
            ("shortlist_provenance",{"source_blob_sha":"0"*40}),
            ("publisher_source",{"source_cefr_level":"C1"}),
            ("editorial_risk","fabricated"),
            ("dictionary_sense_lead",{"url":"https://invalid.example"}),
            ("independent_reviewer_task","fabricated"),
            ("editorial_hold",False), ("independently_reviewed",True),
            ("release_approved",True),
            ("independent_reviewer_receipt",{"reviewer":"fabricated"}),
            ("fake_extra_field",True)]
        for i in range(12):
            for field,value in edits:
                forged = copy.deepcopy(packet)
                need(forged["records"][i].get(field) != value,
                     "Ineffective adversarial mutation: %s/%s"%(i,field))
                forged["records"][i][field] = value
                try:
                    audit(forged, shortlist)
                except (ValueError, KeyError, TypeError):
                    rejected += 1
                else:
                    raise AssertionError("Forged evidence accepted: %s/%s"%(i,field))
        for field,value in [
            ("record_count",11), ("independently_approved_count",1),
            ("word_pos_discrepancies",10),
            ("publisher_reference_level_counts",{"B1":12}),
            ("direct_dictionary_sense_leads",5),
            ("observed_on","2026-10-29"),
            ("shortlist_blob_sha","0"*40),
            ("source_limitations","independently approved"),
            ("fake_extra_field",True)]:
            forged = copy.deepcopy(packet)
            need(forged.get(field) != value, "Ineffective metadata mutation: "+field)
            forged[field] = value
            try:
                audit(forged, shortlist)
            except (ValueError, KeyError, TypeError):
                rejected += 1
            else:
                raise AssertionError("Forged packet metadata accepted: "+field)
        need(rejected == 177, "Adversarial count drift")
        print("PASS: rejected 177/177 forged Oxford source, sense, Myanmar, provenance and fake reviewer mutations")
    print(json.dumps({"level":args.level,"publisher_word_pos_observations":12,
                      "publisher_A1":1,"publisher_A2":6,"publisher_B1":1,"publisher_B2":4,
                      "direct_dictionary_sense_leads":6,
                      "independent_approvals":0,"adversarial_mutations_rejected":rejected,
                      "status":"PASS_STRUCTURE_STAGING_ONLY_NO_DEPLOY"},sort_keys=True))

if __name__ == "__main__":
    main()
