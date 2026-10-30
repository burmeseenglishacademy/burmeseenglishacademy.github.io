#!/usr/bin/env python3
"""Fail-closed Oxford A2 eighth twelve publisher and sense-lead integrity check.

STAGING ONLY. Direct PDF word/POS evidence and dictionary sense observations are
not independently reviewed exact-sense CEFR approvals. No deployment or edits.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-EIGHTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
META = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"A2_EIGHTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":0,"A2":12,"B1":0,"B2":0,"C1":0},"publisher_reference_level_counts":{"A1":7,"A2":4,"B1":1},"word_pos_discrepancies":8,"direct_dictionary_sense_leads":4,"independently_approved_count":0,"source_limitations":"Direct Oxford 3000 CEFR PDF and four Oxford dictionary noun pages inspected 2026-10-30. Seven A1 and one B1 publisher word/POS classifications conflict with provisional A2; exact-sense CEFR and fluent Myanmar remain independently unverified. Four dictionary pages are source leads only. No human review, audio listening, device QA or deployment; shortlist and reviewer tasks remain frozen."}''')
ANCHORS = json.loads(r'''[{"word":"plan","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":599,"source_excerpt":"plan n., v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft intended arrangement for a Saturday visit; distinguish an intention from a detailed plan and noun from plan verb.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/plan_1","observed_on":"2026-10-30","page_text_line_start":106,"page_text_line_end":190,"editorial_interpretation":"Oxford noun sense 1 intention and sense 2 arranged steps; a planned museum visit is a plausible simple intention, not a technical drawing.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"available","level":"A2","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":971,"source_excerpt":"available adj.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Meeting room availability means free to use at a time, not a product being in stock; confirm natural Myanmar temporal wording.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"chance","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":1036,"source_excerpt":"chance n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft opportunity to join a school team; distinguish opportunity from probability of selection and avoid translating solely as luck.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/chance_1","observed_on":"2026-10-30","page_text_line_start":165,"page_text_line_end":178,"editorial_interpretation":"Oxford countable sense 2 is an opportunity to do something, matching chance to join; sense 1 instead concerns probability.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"experience","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1185,"source_excerpt":"experience n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Uncountable job-acquired skill, not a countable event; review experience working versus experience of/in working and Myanmar register.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/experience_1","observed_on":"2026-10-30","page_text_line_start":105,"page_text_line_end":129,"editorial_interpretation":"Oxford uncountable sense 1 is knowledge/skill gained from work; countable sense 3 means an event and is not intended.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"example","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":2,"extracted_line":256,"source_excerpt":"example n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Illustrative example, not a moral example to follow; draft meaning and grammar require independent check.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"price","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":621,"source_excerpt":"price n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Retail price for one notebook, distinct from wider cost or value; clarify currency context without inventing local price.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"account","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":7,"extracted_line":1787,"source_excerpt":"account n.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Bank savings account, not a social-media account, bill or narrative. Publisher B1 noun conflicts with provisional A2 and needs exact-sense rationale.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/account_1","observed_on":"2026-10-30","page_text_line_start":105,"page_text_line_end":120,"editorial_interpretation":"Oxford noun sense 1 is a bank arrangement for keeping/using money; savings account is directly supported, distinct from narrative or online accounts.","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"include","level":"A2","part_of_speech":"verb","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":2,"extracted_line":395,"source_excerpt":"include v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Form field inclusion versus general membership; Myanmar causative ပါဝင်စေသည် may be less natural than ထည့်သွင်းဖော်ပြပါ for contact details.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"report","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":648,"source_excerpt":"report n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"School written assignment, not a news broadcast or verb to report; Oxford word/POS A1 does not prove A2 pedagogical sense.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"clear","level":"A2","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":1049,"source_excerpt":"clear adj.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft definition mixes easy to understand and easy to see; example only tests understandable instructions. Human reviewer should narrow exact sense.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"cost","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":1,"extracted_line":175,"source_excerpt":"cost n., v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Ticket expense inclusive of lunch, not cost verb; distinguish cost from price and Myanmar ကုန်ကျစရိတ်.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"project","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":626,"source_excerpt":"project n.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"School class assignment about water saving, not construction or business project; A1 word/POS listing is not independent exact-sense review.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, original example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."}]''')
FIELDS = frozenset(("word", "level", "part_of_speech", "shortlist_snapshot",
    "shortlist_provenance", "publisher_source", "editorial_risk",
    "dictionary_sense_lead", "independent_reviewer_task", "editorial_hold",
    "independently_reviewed", "release_approved", "independent_reviewer_receipt"))

def require(test, why):
    if not test:
        raise ValueError(why)

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet, shortlist):
    require(set(packet) == set(META) | {"records"}, "Packet schema/key drift")
    require({k: packet[k] for k in META} == META, "Packet metadata/source scope drift")
    require(git_blob_sha(SHORT) == SHORT_BLOB, "Frozen shortlist Git blob drift")
    require(shortlist["counts_by_level"] == {k: 200 for k in LEVELS}, "Not 200 per level")
    require(shortlist["independently_approved_by_level"] == {k: 0 for k in LEVELS},
            "Independent approvals must not be fabricated")
    entries = shortlist["entries"]
    require(len(entries) == 1000 and len({x["word"].casefold() for x in entries}) == 1000,
            "Shortlist count or duplicate headwords")
    by_key = {(e["level"], e["word"]): e for e in entries}
    require(len(packet["records"]) == len(ANCHORS) == 12, "Wrong research count")
    require(len({r["word"] for r in packet["records"]}) == 12, "Duplicate research word")
    for row, anchor in zip(packet["records"], ANCHORS):
        word = anchor["word"]
        require(set(row) == FIELDS, "Unexpected research record field: " + word)
        for key, value in anchor.items():
            require(row[key] == value, "Tampered publisher/source/editorial anchor: " + word + "/" + key)
        entry = by_key.get(("A2", word))
        require(entry is not None and row["level"] == "A2", "Not in frozen A2: " + word)
        require(row["shortlist_snapshot"] == {
            "english_definition": entry["english_definition"],
            "myanmar_meaning": entry["burmese_meaning"],
            "example_sentence": entry["example_sentence"]},
            "Bilingual or example snapshot drift: " + word)
        require(row["shortlist_provenance"] == {
            "source_path": entry["source_path"],
            "source_index": entry["source_index"],
            "source_blob_sha": entry["source_blob_sha"]},
            "Historical Git provenance drift: " + word)
        require(entry["editorial_hold"] is True and entry["release_approved"] is False
                and all(entry.get("reviewed_" + k) is False for k in
                        ("english", "burmese", "example", "level", "pronunciation")),
                "Frozen entry approval flags changed: " + word)
        require(row["editorial_hold"] is True and row["independently_reviewed"] is False
                and row["release_approved"] is False and row["independent_reviewer_receipt"] is None,
                "False human review or release approval: " + word)
        pub = row["publisher_source"]
        require(pub["source_cefr_level"] in LEVELS and pub["source_excerpt"].split()[0] == word,
                "Source word/POS locator mismatch: " + word)
        require(pub["evidence_scope"] == "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                "Publisher word/POS promoted to exact-sense CEFR: " + word)
        lead = row["dictionary_sense_lead"]
        if lead is not None:
            require(lead["evidence_scope"] == "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"
                    and lead["url"].startswith("https://www.oxfordlearnersdictionaries.com/definition/english/"),
                    "Dictionary lead promoted to approval: " + word)
    require(collections.Counter(r["publisher_source"]["source_cefr_level"]
                                for r in packet["records"]) ==
            collections.Counter(META["publisher_reference_level_counts"]),
            "Publisher CEFR label distribution drift")
    require(sum(r["publisher_source"]["source_cefr_level"] != "A2"
                for r in packet["records"]) == 8, "Level conflicts not retained")
    require(sum(r["dictionary_sense_lead"] is not None for r in packet["records"]) == 4,
            "Direct dictionary lead count drift")
    return {"level": "A2", "publisher_word_pos_observations": 12,
            "word_pos_level_conflicts": 8, "dictionary_sense_leads": 4,
            "independent_approvals": 0, "release": "BLOCKED_STAGING_ONLY"}

def flipped(value):
    if value is None:
        return {"forged": True}
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if isinstance(value, str):
        return value + " [tampered]"
    if isinstance(value, dict):
        return {**value, "forged": True}
    raise AssertionError("Unhandled mutation type")

def self_test(packet, shortlist):
    count = 0
    def reject(mutated, reason):
        nonlocal count
        require(mutated != packet, "Ineffective adversarial mutation: " + reason)
        try:
            audit(mutated, shortlist)
        except (ValueError, KeyError, TypeError, AssertionError):
            count += 1
            return
        raise AssertionError("FORGED evidence accepted: " + reason)
    for i, row in enumerate(packet["records"]):
        for key in FIELDS:
            test = copy.deepcopy(packet)
            test["records"][i][key] = flipped(row[key])
            reject(test, row["word"] + "/" + key)
        for section in ("publisher_source", "shortlist_snapshot", "shortlist_provenance"):
            for key, value in row[section].items():
                test = copy.deepcopy(packet)
                test["records"][i][section][key] = flipped(value)
                reject(test, row["word"] + "/" + section + "/" + key)
        if row["dictionary_sense_lead"]:
            for key, value in row["dictionary_sense_lead"].items():
                test = copy.deepcopy(packet)
                test["records"][i]["dictionary_sense_lead"][key] = flipped(value)
                reject(test, row["word"] + "/dictionary_sense_lead/" + key)
    for key, value in META.items():
        test = copy.deepcopy(packet)
        test[key] = flipped(value)
        reject(test, "meta/" + key)
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist = read(PACKET), read(SHORT)
    result = audit(packet, shortlist)
    if args.self_test:
        result["adversarial_mutations_rejected"] = self_test(packet, shortlist)
    result["requested_lane"] = args.level
    result["lane_observations"] = 12 if args.level in ("A2", "ALL") else 0
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
