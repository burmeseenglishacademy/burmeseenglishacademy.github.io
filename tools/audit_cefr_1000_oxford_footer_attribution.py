#!/usr/bin/env python3
"""Fail closed on five Oxford dictionary footer misattributions (staging only).

The Oxford page footer advertises site-wide Word of the Day "applicable" (C1),
not the requested headword. Directly rechecked 2026-10-31. This auditor binds
the correction to immutable old packets and the held shortlist; it does NOT
claim to re-fetch live pages, verify exact-sense CEFR, or sign off human review.
"""
import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORRECTION = "draft/CEFR-1000-OXFORD-FOOTER-WORD-OF-DAY-FIVE-CORRECTION-2026-10-31.json"
SHORTLIST = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE_LIST = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
EXPECTED = {
    "historic": ("adjective", "B1", "historic", (165, 169)),
    "graduate": ("verb", "B1", "graduate_2", (241, 245)),
    "appointment": ("noun", "B1", "appointment", (250, 254)),
    "contemporary": ("adjective", "B2", "contemporary_1", (181, 185)),
    "raw": ("adjective", "B2", "raw_1", (236, 240)),
}
ORIGINAL_PACKETS = {
    "historic": "draft/CEFR-1000-OXFORD-B2-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json",
    **{w: "draft/CEFR-1000-OXFORD-B2-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
       for w in ("graduate", "appointment", "contemporary", "raw")},
}

def check(test, reason):
    if not test:
        raise ValueError(reason)

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def audit(correction, originals, shortlist):
    check(correction.get("schema") == 1 and correction.get("scope") == "CEFR_1000_STAGING_ONLY"
          and correction.get("observed_on") == "2026-10-31"
          and correction.get("status") == "FIVE_FALSE_OXFORD_C1_FOOTER_CONFLICTS_CORRECTED_NO_INDEPENDENT_APPROVAL"
          and correction.get("count") == 5 and correction.get("independently_approved_count") == 0
          and correction.get("production_deployed") is False,
          "Correction must remain staging-only and unapproved")
    check(correction.get("source_list_url") == SOURCE_LIST
          and correction.get("original_shortlist_blob_sha") == "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
          "Source list or frozen shortlist provenance changed")
    rows = correction.get("records")
    check(isinstance(rows, list) and len(rows) == 5
          and {r.get("word") for r in rows} == set(EXPECTED),
          "Expected exactly five distinct corrected headwords")
    entries = {e["word"]: e for e in shortlist["entries"]}
    check(len(shortlist["entries"]) == 1000
          and shortlist["independently_approved_by_level"] == dict.fromkeys(("A1", "A2", "B1", "B2", "C1"), 0),
          "Shortlist changed or has forged approvals")
    for row in rows:
        word = row["word"]
        pos, level, url_tail, old_lines = EXPECTED[word]
        oldpath = ORIGINAL_PACKETS[word]
        check(row.get("part_of_speech") == pos and row.get("original_packet") == oldpath
              and row.get("original_pdf_word_pos_level") == level,
              "Correction target or original publisher level changed: " + word)
        claim = row.get("original_misattributed_footer", {})
        check(claim.get("claimed_level") == "C1"
              and claim.get("claimed_page_text_lines") == list(old_lines)
              and claim.get("original_claim") == "UNRESOLVED_PUBLISHER_SURFACE_CONFLICT_INDEPENDENT_SENSE_REVIEW_REQUIRED",
              "Historical false claim not bound to original: " + word)
        page = row.get("publisher_page_recheck", {})
        check(page.get("url") == "https://www.oxfordlearnersdictionaries.com/definition/english/" + url_tail
              and page.get("observed_on") == "2026-10-31"
              and page.get("actual_footer_headword") == "applicable"
              and page.get("actual_footer_part_of_speech") == "adjective"
              and page.get("actual_footer_level") == "C1"
              and page.get("footer_context") == "WORD_OF_THE_DAY_SITEWIDE_WIDGET_NOT_TARGET_HEADWORD"
              and page.get("evidence_scope") == "DIRECT_PAGE_CONTEXT_CORRECTS_FALSE_FOOTER_ATTRIBUTION_NOT_EXACT_SENSE_CEFR",
              "Word-of-the-Day footer attribution falsified: " + word)
        context = page.get("context_page_text_lines")
        sense = page.get("sense_page_text_lines")
        check(isinstance(context, list) and len(context) == 2 and all(type(x) is int for x in context)
              and context[0] < old_lines[0] <= old_lines[1] < context[1]
              and isinstance(sense, list) and len(sense) == 2
              and all(type(x) is int for x in sense) and 80 <= sense[0] <= sense[1] < context[0],
              "Invalid source-page context or sense locators: " + word)
        check(row.get("correction") == "RETRACT_C1_TARGET_WORD_FOOTER_CLAIM_PDF_WORD_POS_LABEL_RETAINS_ITS_LIMITED_SCOPE"
              and row.get("independent_exact_sense_review") == "NOT_DONE"
              and row.get("editorial_hold") is True and row.get("independently_approved") is False,
              "Correction must never masquerade as independent signoff: " + word)
        old = next((r for r in originals[oldpath]["records"] if r.get("word") == word), None)
        check(old is not None and old.get("part_of_speech") == pos
              and old.get("publisher_source", {}).get("source_cefr_level") == level
              and old.get("publisher_source", {}).get("url") == SOURCE_LIST
              and old.get("publisher_surface_conflict", {}).get("dictionary_footer_label") == "C1"
              and old.get("publisher_surface_conflict", {}).get("page_text_line_start") == old_lines[0]
              and old.get("publisher_surface_conflict", {}).get("page_text_line_end") == old_lines[1]
              and old.get("dictionary_sense_lead", {}).get("url") == page["url"],
              "Historical packet not bound to correction: " + word)
        entry = entries[word]
        check(entry["level"] == "B2" and entry["part_of_speech"] == pos
              and entry["editorial_hold"] is True and entry["release_approved"] is False
              and all(entry.get("reviewed_" + f) is False for f in
                      ("english", "burmese", "example", "level", "pronunciation"))
              and old["shortlist_snapshot"]["english_definition"] == entry["english_definition"]
              and old["shortlist_snapshot"]["myanmar_meaning"] == entry["burmese_meaning"]
              and old["shortlist_snapshot"]["example_sentence"] == entry["example_sentence"],
              "Frozen held bilingual draft or review flags drifted: " + word)
    return {"corrected_false_footer_claims": 5, "actual_footer_word": "applicable",
            "independent_approvals": 0, "release": "BLOCKED_STAGING_ONLY"}

def self_test(correction, originals, shortlist):
    rejected = 0
    def reject(modifier):
        nonlocal rejected
        candidate = copy.deepcopy(correction)
        modifier(candidate)
        try:
            audit(candidate, originals, shortlist)
        except (ValueError, KeyError, TypeError):
            rejected += 1
        else:
            raise AssertionError("Forged footer attribution or approval was accepted")
    for i in range(5):
        for field, value in (
            ("actual_footer_headword", "historic"),
            ("actual_footer_level", "B2"),
            ("footer_context", "TARGET_HEADWORD_CEFR_LABEL"),
            ("observed_on", "2026-10-29"),
            ("url", "https://example.com/fake"),
            ("evidence_scope", "INDEPENDENT_CEFR_SIGNOFF"),
        ):
            reject(lambda p, i=i, field=field, value=value:
                   p["records"][i]["publisher_page_recheck"].__setitem__(field, value))
        reject(lambda p, i=i: p["records"][i].__setitem__("independently_approved", True))
        reject(lambda p, i=i: p["records"][i].__setitem__("editorial_hold", False))
        reject(lambda p, i=i: p["records"][i].__setitem__("original_pdf_word_pos_level", "C1"))
        reject(lambda p, i=i: p["records"][i]["original_misattributed_footer"].__setitem__("claimed_level", "B1"))
    reject(lambda p: p.__setitem__("production_deployed", True))
    reject(lambda p: p.__setitem__("independently_approved_count", 5))
    reject(lambda p: p["records"].pop())
    return rejected

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("A1", "A2", "B1", "B2", "C1", "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    correction = read(CORRECTION)
    originals = {p: read(p) for p in set(ORIGINAL_PACKETS.values())}
    shortlist = read(SHORTLIST)
    result = audit(correction, originals, shortlist)
    if args.self_test:
        result["forged_mutations_rejected"] = self_test(correction, originals, shortlist)
    result["lane"] = args.level
    print(json.dumps(result, sort_keys=True))
