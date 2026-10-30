#!/usr/bin/env python3
"""Fail-closed Oxford B1 eighth 12 word/POS and four dictionary sense leads. Staging only."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-EIGHTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-30.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED_META = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"B1_EIGHTH_TWELVE_DIRECT_OXFORD_WORD_POS_AND_FOUR_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":0,"A2":0,"B1":12,"B2":0,"C1":0},"publisher_reference_level_counts":{"A1":2,"A2":3,"B1":7},"word_pos_discrepancies":5,"direct_dictionary_sense_leads":4,"independently_approved_count":0,"source_limitations":"Oxford 3000 official CEFR PDF directly inspected on 2026-10-30. Publisher labels are word/POS and homograph specific, not independent exact-sense CEFR verification. Four directly opened dictionary pages are editorial sense leads only; lie2 PDF B1 versus dictionary B2 badge unresolved. No human independent review, real audio listening, device testing or publication."}''')
EXPECTED_ANCHORS = json.loads(r'''[{"word":"channel","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":7,"extracted_line":1887,"source_excerpt":"channel n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Television channel sense, not river/waterway, communication medium or English Channel; Myanmar 'ရုပ်မြင်သံကြားလိုင်း' is specific.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/channel_1","observed_on":"2026-10-30","page_text_line_start":103,"page_text_line_end":154,"editorial_interpretation":"Dictionary TV/radio section distinguishes TV station from other channel senses; the draft documentary example uses TV channel.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"fat","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":2,"extracted_line":275,"source_excerpt":"fat adj.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft adjective describes a cat's body size, not high-fat food, fat noun or insult directed at a person; avoid potentially stigmatising human examples.","dictionary_sense_lead":null},{"word":"royal","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":9,"extracted_line":2401,"source_excerpt":"royal adj.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft 'royal palace' describes monarchy, not a proper name; Myanmar translation 'တော်ဝင်မိသားစုနှင့် သက်ဆိုင်သော' is narrower than some royal institutional contexts.","dictionary_sense_lead":null},{"word":"serve","part_of_speech":"verb","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1601,"source_excerpt":"serve v.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft means provide breakfast, not serve in the military, legal notice or a sporting turn; review Myanmar naturalness and the 7 o'clock time expression.","dictionary_sense_lead":null},{"word":"wonderful","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":889,"source_excerpt":"wonderful adj.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft is positive evaluation of an evening; Myanmar 'ကြည်နူးဖွယ်ကောင်းသော' can add an emotional nuance not required by every use.","dictionary_sense_lead":null},{"word":"bottom","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":1008,"source_excerpt":"bottom n., adj.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft noun means lowest part inside a bag, not buttocks, bottom adjective, financial low point or underside; Myanmar 'အောက်ခြေ' requires container context.","dictionary_sense_lead":null},{"word":"lie","part_of_speech":"verb","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":8,"extracted_line":2186,"source_excerpt":"lie2 (tell a lie) v., n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"CRITICAL HOMOGRAPH: draft means knowingly say something false (lie2, lied/lied), NOT A1 lie1 'recline' (lay/lain). The dictionary's Oxford 3000 B2 badge for lie2 conflicts with PDF B1; independent sense-specific CEFR reconciliation required.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/lie2_1","observed_on":"2026-10-30","page_text_line_start":88,"page_text_line_end":122,"editorial_interpretation":"Direct lie2 dictionary confirms false-statement verb, past lied/lied, and lie about something; page displays Oxford 3000 B2 while PDF labels lie2 B1. Contrast lie1 /definition/english/lie1_1 (recline, lay/lain).","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"square","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":7,"extracted_line":1651,"source_excerpt":"square adj., n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft noun is four equal sides with right angles, not town square, number squared or adjective; Myanmar 'စတုရန်းပုံ' aligns with shape but needs exact-sense review.","dictionary_sense_lead":null},{"word":"surface","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":10,"extracted_line":2488,"source_excerpt":"surface n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft means the top/outside of a table, not earth/water surface, mathematical surface or verb; Myanmar 'မျက်နှာပြင်' is context-sensitive.","dictionary_sense_lead":null},{"word":"supply","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":9,"extracted_line":2485,"source_excerpt":"supply n., v.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft noun is available quantity of clean water, not plural emergency supplies or act of providing; Myanmar 'ထောက်ပံ့ပစ္စည်း' can incorrectly imply goods rather than an available amount.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/supply_1","observed_on":"2026-10-30","page_text_line_start":109,"page_text_line_end":133,"editorial_interpretation":"Dictionary first countable sense concerns amount available, including clean water supply; distinguish plural supplies and uncountable act of provision.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"waste","part_of_speech":"verb","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":10,"extracted_line":2564,"source_excerpt":"waste n., v., adj.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft transitive verb means use water unnecessarily, not discarded waste noun or waste adjective; Myanmar 'ဖြုန်းတီးသည်' fits the resource sense, but exact context needs independent review.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/waste_2","observed_on":"2026-10-30","page_text_line_start":112,"page_text_line_end":122,"editorial_interpretation":"Dictionary verb first sense is using more than necessary or useful; draft water example fits this, not waste as refuse.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"}},{"word":"strength","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":9,"extracted_line":2472,"source_excerpt":"strength n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft physical muscular power, not structural material strength, moral courage, competitive advantage or numerical intensity; Myanmar 'ခွန်အား' is broad.","dictionary_sense_lead":null}]''')
EXPECTED_TASK = "Independent human reviewer must verify exact sense and CEFR suitability, English definition, fluent Myanmar meaning, original example grammar, source-backed word/POS and dictionary distinctions, and British pronunciation. Human signoff must be content-bound; source observation and assistant analysis are not independent review."

def require(test, message):
    if not test:
        raise ValueError(message)

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def audit(packet, shortlist):
    require(isinstance(packet, dict) and isinstance(shortlist, dict), "Invalid JSON root")
    require(set(packet) == set(EXPECTED_META) | {"records"}, "Unexpected packet fields")
    for key, value in EXPECTED_META.items():
        require(packet.get(key) == value, "Packet metadata drift: " + key)
    require(blob_sha(SHORTLIST) == EXPECTED_META["shortlist_blob_sha"],
            "Frozen shortlist Git blob has changed")
    require(shortlist.get("release_status") ==
            "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
            "Shortlist release status changed")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Shortlist count drift")
    require(shortlist.get("counts_by_level") == {x: 200 for x in LEVELS},
            "Not exactly 200 per CEFR level")
    require(shortlist.get("independently_approved_by_level") == {x: 0 for x in LEVELS},
            "Independent approvals must not be manufactured")
    require(isinstance(packet.get("records"), list) and len(packet["records"]) == 12,
            "Expected twelve records")
    require([r.get("word") for r in packet["records"]] ==
            [a["word"] for a in EXPECTED_ANCHORS], "Record order/identity drift")
    by_key = {(r.get("level"), r.get("word")): r for r in entries}
    require(len(by_key) == 1000, "Duplicate shortlist level/word key")
    source_paths = set()
    for row, anchor in zip(packet["records"], EXPECTED_ANCHORS):
        word = anchor["word"]
        require(isinstance(row, dict), "Invalid record " + word)
        require(set(row) == {"word", "level", "part_of_speech", "shortlist_snapshot",
                            "shortlist_provenance", "publisher_source", "editorial_risk",
                            "dictionary_sense_lead", "independent_reviewer_task",
                            "editorial_hold", "independently_reviewed", "release_approved",
                            "independent_reviewer_receipt"}, "Record field drift: " + word)
        require(row["level"] == "B1" and row["word"] == word
                and row["part_of_speech"] == anchor["part_of_speech"],
                "Draft identity/POS drift: " + word)
        source = by_key.get(("B1", word))
        require(source is not None, "Missing shortlist entry: " + word)
        require(row["shortlist_snapshot"] == {
            "english_definition": source["english_definition"],
            "myanmar_meaning": source["burmese_meaning"],
            "example_sentence": source["example_sentence"]},
            "Bilingual/grammar source snapshot mismatch: " + word)
        require(row["shortlist_provenance"] == {
            "source_path": source["source_path"],
            "source_index": source["source_index"],
            "source_blob_sha": source["source_blob_sha"]},
            "Historical Git provenance mismatch: " + word)
        source_paths.add(source["source_path"])
        require(row["publisher_source"] == anchor["publisher_source"],
                "Publisher URL/date/page/line/excerpt/level/POS drift: " + word)
        require(row["editorial_risk"] == anchor["editorial_risk"],
                "Editorial risk drift: " + word)
        require(row["dictionary_sense_lead"] == anchor["dictionary_sense_lead"],
                "Direct dictionary sense locator drift: " + word)
        require(row["independent_reviewer_task"] == EXPECTED_TASK,
                "Reviewer task drift: " + word)
        require(row["editorial_hold"] is True
                and row["independently_reviewed"] is False
                and row["release_approved"] is False
                and row["independent_reviewer_receipt"] is None,
                "Manufactured review/approval: " + word)
        require(source["editorial_hold"] is True and source["release_approved"] is False
                and all(source.get("reviewed_" + k) is False for k in
                        ("english", "burmese", "example", "level", "pronunciation")),
                "Frozen shortlist approval drift: " + word)
    for name in source_paths:
        source_file = ROOT / name
        require(source_file.is_file(), "Missing original editorial source: " + name)
        for row in packet["records"]:
            if row["shortlist_provenance"]["source_path"] == name:
                require(blob_sha(source_file) == row["shortlist_provenance"]["source_blob_sha"],
                        "Original source Git blob mismatch: " + name)
    counts = {level: sum(r["publisher_source"]["source_cefr_level"] == level
                         for r in packet["records"]) for level in ("A1", "A2", "B1")}
    require(counts == {"A1": 2, "A2": 3, "B1": 7}, "Publisher level count drift")
    require(sum(bool(r["dictionary_sense_lead"]) for r in packet["records"]) == 4,
            "Direct dictionary leads count drift")
    require(sum(r["publisher_source"]["source_cefr_level"] != "B1"
                for r in packet["records"]) == 5, "Cross-level discrepancy drift")
    return {"records": 12, "publisher_word_pos": counts,
            "direct_dictionary_leads": 4, "independent_approvals": 0,
            "release": "BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    audit(packet, shortlist)
    cases = 0
    def negative(label, fn):
        nonlocal cases
        mutated = copy.deepcopy(packet)
        fn(mutated)
        require(mutated != packet, "Ineffective negative mutation: " + label)
        try:
            audit(mutated, shortlist)
        except (ValueError, TypeError, KeyError, AttributeError):
            cases += 1
        else:
            raise ValueError("Forged data accepted: " + label)
    for key, val in EXPECTED_META.items():
        negative("meta " + key, lambda x, k=key: x.__setitem__(k, "FORGED"))
    negative("remove packet record", lambda x: x["records"].pop())
    negative("swap packet records", lambda x: x["records"].reverse())
    for i, anchor in enumerate(EXPECTED_ANCHORS):
        for field in ("word", "level", "part_of_speech", "editorial_risk",
                      "independent_reviewer_task", "shortlist_snapshot",
                      "shortlist_provenance", "publisher_source", "dictionary_sense_lead",
                      "editorial_hold", "independently_reviewed", "release_approved",
                      "independent_reviewer_receipt"):
            negative(anchor["word"] + " " + field,
                     lambda x, j=i, k=field: x["records"][j].__setitem__(k, "FORGED"))
        for key in anchor["publisher_source"]:
            negative(anchor["word"] + " publisher " + key,
                     lambda x, j=i, k=key: x["records"][j]["publisher_source"].__setitem__(k, "FORGED"))
        for key in ("english_definition", "myanmar_meaning", "example_sentence"):
            negative(anchor["word"] + " snapshot " + key,
                     lambda x, j=i, k=key: x["records"][j]["shortlist_snapshot"].__setitem__(k, "FORGED"))
        for key in ("source_path", "source_index", "source_blob_sha"):
            negative(anchor["word"] + " provenance " + key,
                     lambda x, j=i, k=key: x["records"][j]["shortlist_provenance"].__setitem__(k, "FORGED"))
        if anchor["dictionary_sense_lead"]:
            for key in anchor["dictionary_sense_lead"]:
                negative(anchor["word"] + " sense " + key,
                         lambda x, j=i, k=key: x["records"][j]["dictionary_sense_lead"].__setitem__(k, "FORGED"))
    return cases

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    summary = audit(packet, shortlist)
    print(json.dumps({"lane": args.level, **summary}, ensure_ascii=False, sort_keys=True))
    if args.self_test:
        print("Rejected %d/%d adversarial packet mutations" %
              (self_test(packet, shortlist), self_test_count(packet)))
def self_test_count(packet):
    return len(EXPECTED_META) + 2 + len(packet["records"]) * (13 + 10 + 3 + 3) + sum(
        len(a["dictionary_sense_lead"]) for a in EXPECTED_ANCHORS if a["dictionary_sense_lead"])

if __name__ == "__main__":
    main()
