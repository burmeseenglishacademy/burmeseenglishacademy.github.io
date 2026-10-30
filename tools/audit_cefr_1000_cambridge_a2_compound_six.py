#!/usr/bin/env python3
"""Fail-closed staging-only Cambridge A2 compound source-snapshot auditor.

Web search-index observations are NOT direct page fetches, independent human
reviews, Oxford PDF observations, final audio listening, or CEFR approvals.
"""
import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-A2-COMPOUND-SIX-SENSE-TRIAGE-2026-10-30.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED_RECORDS = json.loads(r'''[{"word":"raincoat","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"A coat made to keep rain from soaking your clothes.","myanmar_meaning":"မိုးရေမစိုစေရန် ဝတ်ဆင်သော မိုးကာအင်္ကျီ","example_sentence":"I packed a raincoat because the forecast warned of heavy rain."},"shortlist_provenance":{"source_path":"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json","source_index":0,"source_blob_sha":"da7df62123acfac89a0acedad4652ec499c7ed3d"},"publisher_source":{"publisher":"Cambridge University Press","dictionary":"Cambridge Advanced Learner's Dictionary & Thesaurus","url":"https://dictionary.cambridge.org/dictionary/english/raincoat","observed_on":"2026-10-30","retrieval_method":"WEB_SEARCH_INDEX_RESULT_PAGE_OPEN_RETURNED_403","index_section":"Meaning of raincoat in English","visible_cefr_badge":"A2","source_excerpt_summary":"Cambridge Advanced Learner's Dictionary raincoat noun C with A2 badge; coat protecting wearer from rain","source_evidence_scope":"DICTIONARY_EXACT_SENSE_LEAD_NOT_INDEPENDENT_REVIEW","publisher_cefr_level_is_not_inferred_from_missing_badge":true},"editorial_risk":"Physical rain-protective coat; not the wider category of waterproof outerwear.","unapproved_myanmar_proposal":"မိုးရေမစိုအောင် ကာကွယ်ပေးသော မိုးကာအင်္ကျီ","unapproved_original_example_proposal":"She took a raincoat because it might rain later.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"lunchbox","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"A small container used to carry food for a midday meal.","myanmar_meaning":"နေ့လယ်စာ ထည့်ယူသွားရန် အသုံးပြုသော ထမင်းဘူး","example_sentence":"She put a sandwich and an apple in her lunchbox before school."},"shortlist_provenance":{"source_path":"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json","source_index":1,"source_blob_sha":"da7df62123acfac89a0acedad4652ec499c7ed3d"},"publisher_source":{"publisher":"Cambridge University Press","dictionary":"Cambridge Advanced Learner's Dictionary & Thesaurus","url":"https://dictionary.cambridge.org/dictionary/english/lunchbox","observed_on":"2026-10-30","retrieval_method":"WEB_SEARCH_INDEX_RESULT_PAGE_OPEN_RETURNED_403","index_section":"Meaning of lunchbox in English","visible_cefr_badge":null,"source_excerpt_summary":"Cambridge Advanced Learner's Dictionary lunchbox noun C; container for carrying lunch; no visible CEFR badge in retrieved snippet","source_evidence_scope":"DICTIONARY_EXACT_SENSE_LEAD_NOT_INDEPENDENT_REVIEW","publisher_cefr_level_is_not_inferred_from_missing_badge":true},"editorial_risk":"Lunch container rather than the food inside; absence of badge is NOT a CEFR level.","unapproved_myanmar_proposal":"နေ့လယ်စာ ထည့်ယူသွားရန် သုံးသော ထမင်းဘူး","unapproved_original_example_proposal":"He packed his lunchbox before leaving for school.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"toothache","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"Pain in a tooth or in the area around a tooth.","myanmar_meaning":"သွားတစ်ချောင်း သို့မဟုတ် သွားပတ်ဝန်းကျင်တွင် ဖြစ်သော သွားကိုက်ဝေဒနာ","example_sentence":"He missed football practice because his toothache became worse."},"shortlist_provenance":{"source_path":"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json","source_index":2,"source_blob_sha":"da7df62123acfac89a0acedad4652ec499c7ed3d"},"publisher_source":{"publisher":"Cambridge University Press","dictionary":"Cambridge Advanced Learner's Dictionary & Thesaurus","url":"https://dictionary.cambridge.org/dictionary/english/toothache","observed_on":"2026-10-30","retrieval_method":"WEB_SEARCH_INDEX_RESULT_PAGE_OPEN_RETURNED_403","index_section":"Meaning of toothache in English","visible_cefr_badge":"A2","source_excerpt_summary":"Cambridge Advanced Learner's Dictionary toothache noun C or U with A2 badge; pain related to a tooth","source_evidence_scope":"DICTIONARY_EXACT_SENSE_LEAD_NOT_INDEPENDENT_REVIEW","publisher_cefr_level_is_not_inferred_from_missing_badge":true},"editorial_risk":"Countability C or U; compare have toothache / have a toothache; British usage and example grammar.","unapproved_myanmar_proposal":"သွားကိုက်ဝေဒနာ","unapproved_original_example_proposal":"She went to the dentist because she had toothache.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"sunscreen","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"A cream or lotion that protects skin from sunlight.","myanmar_meaning":"နေရောင်ခြည်ဒဏ်မှ အရေပြားကို ကာကွယ်ပေးသော လိမ်းဆေး","example_sentence":"Apply sunscreen before spending the afternoon at the beach."},"shortlist_provenance":{"source_path":"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json","source_index":3,"source_blob_sha":"da7df62123acfac89a0acedad4652ec499c7ed3d"},"publisher_source":{"publisher":"Cambridge University Press","dictionary":"Cambridge Advanced Learner's Dictionary & Thesaurus","url":"https://dictionary.cambridge.org/dictionary/english/sunscreen","observed_on":"2026-10-30","retrieval_method":"WEB_SEARCH_INDEX_RESULT_PAGE_OPEN_RETURNED_403","index_section":"Meaning of sunscreen in English","visible_cefr_badge":null,"source_excerpt_summary":"Cambridge Advanced Learner's Dictionary sunscreen; protective skin substance; no visible CEFR badge in retrieved snippet","source_evidence_scope":"DICTIONARY_EXACT_SENSE_LEAD_NOT_INDEPENDENT_REVIEW","publisher_cefr_level_is_not_inferred_from_missing_badge":true},"editorial_risk":"Cream/lotion against UV exposure, not general sun avoidance; uncountable mass noun.","unapproved_myanmar_proposal":"နေရောင်ခြည်၏ ခရမ်းလွန်ရောင်ခြည်ဒဏ်မှ အရေပြားကို ကာကွယ်ပေးသော လိမ်းဆေး","unapproved_original_example_proposal":"Apply sunscreen before going outside in strong sunlight.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"shoelace","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"A thin cord used to fasten a shoe.","myanmar_meaning":"ဖိနပ်ကို ချည်တင်းစေရန် အသုံးပြုသော ဖိနပ်ကြိုး","example_sentence":"Tie your shoelace before you run across the playground."},"shortlist_provenance":{"source_path":"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json","source_index":0,"source_blob_sha":"228c772697e4879f6b8a30f85709d188a1df266c"},"publisher_source":{"publisher":"Cambridge University Press","dictionary":"Cambridge Advanced Learner's Dictionary & Thesaurus","url":"https://dictionary.cambridge.org/dictionary/english/shoelace","observed_on":"2026-10-30","retrieval_method":"WEB_SEARCH_INDEX_RESULT_PAGE_OPEN_RETURNED_403","index_section":"Meaning of shoelace in English","visible_cefr_badge":null,"source_excerpt_summary":"Cambridge Advanced Learner's Dictionary shoelace noun C usually plural; thin cord to fasten shoes; no visible CEFR badge in retrieved snippet","source_evidence_scope":"DICTIONARY_EXACT_SENSE_LEAD_NOT_INDEPENDENT_REVIEW","publisher_cefr_level_is_not_inferred_from_missing_badge":true},"editorial_risk":"Usually plural when referring to a pair of shoes; distinguish shoelace from shoestring figurative sense.","unapproved_myanmar_proposal":"ဖိနပ်ကို ချည်နှောင်ရန် အသုံးပြုသော ဖိနပ်ကြိုး","unapproved_original_example_proposal":"Tie your shoelaces before you start running.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null},{"word":"bookshelf","level":"A2","part_of_speech":"noun","shortlist_snapshot":{"english_definition":"A shelf used for storing or displaying books.","myanmar_meaning":"စာအုပ်များ တင်ထားရန် ပြုလုပ်ထားသော စာအုပ်စင်","example_sentence":"I put the new dictionary on the highest bookshelf."},"shortlist_provenance":{"source_path":"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json","source_index":1,"source_blob_sha":"228c772697e4879f6b8a30f85709d188a1df266c"},"publisher_source":{"publisher":"Cambridge University Press","dictionary":"Cambridge Advanced Learner's Dictionary & Thesaurus","url":"https://dictionary.cambridge.org/dictionary/english/bookshelf","observed_on":"2026-10-30","retrieval_method":"WEB_SEARCH_INDEX_RESULT_PAGE_OPEN_RETURNED_403","index_section":"Meaning of bookshelf in English","visible_cefr_badge":"A2","source_excerpt_summary":"Cambridge Advanced Learner's Dictionary bookshelf noun C with A2 badge; shelf for books; plural bookshelves","source_evidence_scope":"DICTIONARY_EXACT_SENSE_LEAD_NOT_INDEPENDENT_REVIEW","publisher_cefr_level_is_not_inferred_from_missing_badge":true},"editorial_risk":"Plural irregular bookshelves; bookshelf versus freestanding bookcase; original highest bookshelf may be awkward context.","unapproved_myanmar_proposal":"စာအုပ်များ တင်ထားရန် အသုံးပြုသော စင်","unapproved_original_example_proposal":"I put the new dictionary on the top bookshelf.","editorial_hold":true,"independently_reviewed":false,"release_approved":false,"independent_reviewer_receipt":null}]''')
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED_KEYS = {
    "schema": 1,
    "scope": "CEFR_1000_TOTAL_STAGING_ONLY",
    "status": "A2_COMPOUND_SIX_CAMBRIDGE_INDEX_SENSE_TRIAGE_EDITORIAL_HOLD",
    "observed_on": "2026-10-30",
    "shortlist_blob_sha": SHORTLIST_SHA,
    "record_count": 6,
    "counts_by_level": {"A1": 0, "A2": 6, "B1": 0, "B2": 0, "C1": 0},
    "visible_cambridge_cefr_badge_counts": {"A2": 3, "NOT_VISIBLE": 3},
    "independently_approved_count": 0,
    "independent_human_review_receipts": [],
    "audio_real_listening_signoffs": 0,
    "release_approved": False,
}
REVIEW_FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation", "release_approved")

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def audit(packet, shortlist):
    require(isinstance(packet, dict), "packet must be object")
    require(set(packet) == set(EXPECTED_KEYS) | {"source_limitations", "independent_reviewer_task", "records"},
            "packet schema must not add or omit fields")
    for k, v in EXPECTED_KEYS.items():
        require(packet.get(k) == v, "packet metadata mismatch: " + k)
    require("403" in packet["source_limitations"] and "NOT" in packet["source_limitations"],
            "retrieval limits must remain explicit")
    require("Human-independent" in packet["independent_reviewer_task"],
            "independent reviewer requirement missing")
    require(packet.get("records") == EXPECTED_RECORDS,
            "six Cambridge observations, source limitations, original bilingual snapshots and holds are immutable")
    require(shortlist.get("release_status") == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
            "shortlist release status changed")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "independent approvals may not be invented")
    require(len(shortlist.get("entries", [])) == 1000, "shortlist count changed")
    byword = {(r.get("level"), r.get("word")): r for r in shortlist["entries"]}
    for row in EXPECTED_RECORDS:
        original = byword.get(("A2", row["word"]))
        require(original is not None, "shortlist word missing")
        require(original.get("part_of_speech") == row["part_of_speech"], "POS changed")
        for k, v in row["shortlist_snapshot"].items():
            require(original.get(k) == v, "shortlist bilingual/example snapshot changed: " + row["word"] + " field=" + k + " actual=" + repr(original.get(k)) + " expected=" + repr(v))
        for k, v in row["shortlist_provenance"].items():
            require(original.get(k) == v, "historical Git provenance changed: " + row["word"])
        require(original.get("editorial_hold") is True, "editorial hold removed")
        require(all(original.get(k) is False for k in REVIEW_FIELDS), "unapproved review flag changed")
    require([r["publisher_source"]["visible_cefr_badge"] for r in EXPECTED_RECORDS]
            == ["A2", None, "A2", None, None, "A2"], "missing badges cannot be inferred")
    return True

def negative_tests(packet, shortlist):
    count = 0
    def reject(p, s):
        nonlocal count
        try:
            audit(p, s)
        except (ValueError, TypeError, KeyError):
            count += 1
        else:
            raise AssertionError("forged evidence or review state accepted")
    for key in EXPECTED_KEYS:
        p = copy.deepcopy(packet)
        p[key] = "FORGED"
        reject(p, shortlist)
    for field in ("source_limitations", "independent_reviewer_task"):
        p = copy.deepcopy(packet)
        p[field] = ""
        reject(p, shortlist)
    for i, row in enumerate(EXPECTED_RECORDS):
        for key in ("word", "level", "part_of_speech", "editorial_hold",
                    "independently_reviewed", "release_approved", "independent_reviewer_receipt",
                    "editorial_risk", "unapproved_myanmar_proposal", "unapproved_original_example_proposal"):
            p = copy.deepcopy(packet)
            p["records"][i][key] = "FORGED"
            reject(p, shortlist)
        for obj, fields in (("shortlist_snapshot", ("english_definition", "myanmar_meaning", "example_sentence")),
                            ("shortlist_provenance", ("source_path", "source_index", "source_blob_sha")),
                            ("publisher_source", ("publisher", "dictionary", "url", "observed_on", "retrieval_method",
                                                  "index_section", "visible_cefr_badge", "source_excerpt_summary",
                                                  "source_evidence_scope", "publisher_cefr_level_is_not_inferred_from_missing_badge"))):
            for key in fields:
                p = copy.deepcopy(packet)
                p["records"][i][obj][key] = "FORGED"
                reject(p, shortlist)
    for key in ("english_definition", "myanmar_meaning", "example_sentence", "source_blob_sha",
                "editorial_hold", "reviewed_burmese", "release_approved"):
        s = copy.deepcopy(shortlist)
        entry = next(x for x in s["entries"] if x["word"] == "raincoat" and x["level"] == "A2")
        entry[key] = "FORGED" if key not in ("editorial_hold", "reviewed_burmese", "release_approved") else False if key=="editorial_hold" else True
        reject(packet, s)
    for key in ("release_status", "independently_approved_by_level"):
        s = copy.deepcopy(shortlist)
        s[key] = "APPROVED"
        reject(packet, s)
    return count

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    audit(packet, shortlist)
    print("Cambridge A2 compound six: source-bound index snippets; 3 A2 badges, 3 unlabeled; 0 independently approved; staging hold")
    if args.self_test:
        count = negative_tests(packet, shortlist)
        print(f"Rejected {count}/{count} forged evidence, Myanmar, provenance and human-approval mutations")

if __name__ == "__main__":
    main()
