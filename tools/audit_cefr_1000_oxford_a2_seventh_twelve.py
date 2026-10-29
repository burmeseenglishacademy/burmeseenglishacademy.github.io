#!/usr/bin/env python3
"""Fail-closed Oxford A2 seventh twelve publisher and sense-lead integrity check.

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
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-SEVENTH-TWELVE-AND-THREE-DIRECT-SENSE-LEADS-2026-10-30.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORT_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
META = json.loads(r'''{"schema":1,"scope":"CEFR_1000_TOTAL_STAGING_ONLY","status":"A2_SEVENTH_TWELVE_DIRECT_OXFORD_WORD_POS_THREE_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD","observed_on":"2026-10-30","shortlist_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551","record_count":12,"counts_by_level":{"A1":0,"A2":12,"B1":0,"B2":0,"C1":0},"publisher_reference_level_counts":{"A1":4,"A2":7,"B1":1},"word_pos_discrepancies":5,"direct_dictionary_sense_leads":3,"independently_approved_count":0,"source_limitations":"Oxford 3000 PDF and three Oxford dictionary pages directly inspected 2026-10-30. PDF records are publisher word/POS observations, not independent exact-sense CEFR labels. Topic tags and examples are editorial leads only. Frozen shortlist, review tasks and production assets unchanged."}''')
ANCHORS = json.loads(r'''[{"word":"post","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":612,"source_excerpt":"post n., v.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Online message is distinct from physical mail, job post, upright post and posting verb. Oxford dictionary labels internet topic a2; word/POS A1 is not an exact-sense A1 approval.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/post_2","page_text_line_start":190,"page_text_line_end":227,"editorial_interpretation":"Oxford noun sense 4 is an online message or blog post; page tags internet topic a2, distinct from the word/POS A1 list label. The two are not interchangeable CEFR approvals.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"social","level":"A2","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1635,"source_excerpt":"social adj.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"A social event is interpersonal/recreational, not social media or society-wide policy; Myanmar လူမှုဆက်ဆံရေး requires natural context.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"death","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1109,"source_excerpt":"death n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Sensitive end-of-life noun; distinguish death, dying and fatality; ensure respectful original example and Myanmar phrasing.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"guy","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1260,"source_excerpt":"guy n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Informal person/man; gender-neutral use varies; front-desk reference and Myanmar လူတစ်ယောက် should be reviewed.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"true","level":"A2","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":822,"source_excerpt":"true adj.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"A1 word/POS versus provisional A2; factual truth distinct from loyalty or authenticity; retain level conflict pending human review.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"along","level":"A2","part_of_speech":"preposition","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":936,"source_excerpt":"along prep., adv.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft preposition along the river is movement following its length; distinguish adverb and alongside/static sense.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"matter","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":6,"extracted_line":1387,"source_excerpt":"matter n., v.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft noun denotes an issue needing attention, not physical substance or the verb matter; avoid overgeneralizing Myanmar ကိစ္စ.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"pretty","level":"A2","part_of_speech":"adverb","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":620,"source_excerpt":"pretty adj., adv.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft adverb means fairly/quite, not attractive adjective or very/intensifier sense; dictionary direct adverb entry distinguishes these meanings.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/pretty_1","page_text_line_start":88,"page_text_line_end":136,"editorial_interpretation":"Oxford adverb sense 1 denotes fairly/to some extent and sense 2 denotes very. The draft 'pretty clear' may be scalar/ambiguous and needs human exact-sense and Myanmar check.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"bit","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":4,"extracted_line":999,"source_excerpt":"bit n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"A bit of sugar is small amount, not a computing bit or the past tense of bite; natural Myanmar quantity/measure needs review.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"hit","level":"A2","part_of_speech":"verb","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":5,"extracted_line":1281,"source_excerpt":"hit v., n.","source_cefr_level":"A2","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft ball-hit-window impact is transitive physical contact, not strike a person, success, or noun hit; grammar and Myanmar need review.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"past","level":"A2","part_of_speech":"noun","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":3,"extracted_line":578,"source_excerpt":"past adj., n., prep.","source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Draft noun past is previous time, not past adjective or preposition; publisher A1 conflicts with provisional A2.","dictionary_sense_lead":null,"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."},{"word":"due","level":"A2","part_of_speech":"adjective","publisher_source":{"publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level","url":"https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf","observed_on":"2026-10-30","pdf_page":8,"extracted_line":1994,"source_excerpt":"due adj.","source_cefr_level":"B1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE","access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},"editorial_risk":"Expected arrival in ten minutes, not caused-by due to, overdue payment or owing; publisher B1 conflicts with provisional A2.","dictionary_sense_lead":{"url":"https://www.oxfordlearnersdictionaries.com/definition/english/due_1","page_text_line_start":149,"page_text_line_end":165,"editorial_interpretation":"Oxford expected/arranged sense includes transport due in five minutes; owed/payable sense is separate. This page does not independently certify draft A2 exact-sense CEFR.","observed_on":"2026-10-30","evidence_scope":"DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"},"independent_reviewer_task":"Independent human must verify exact sense and source-backed CEFR teaching level, English definition, fluent Myanmar, example grammar, British pronunciation, historical provenance and content-bound signoff. Publisher word/POS or topic labels are not independent approval."}]''')
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
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

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
                for r in packet["records"]) == 5, "Level conflicts not retained")
    require(sum(r["dictionary_sense_lead"] is not None for r in packet["records"]) == 3,
            "Direct dictionary lead count drift")
    return {"level": "A2", "publisher_word_pos_observations": 12,
            "word_pos_level_conflicts": 5, "dictionary_sense_leads": 3,
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
