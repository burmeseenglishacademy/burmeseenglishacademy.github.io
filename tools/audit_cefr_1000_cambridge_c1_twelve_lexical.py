#!/usr/bin/env python3
"""Fail-closed staging audit: twelve Cambridge C1 lexical sense leads.

Publisher search-index text is NOT an independently reviewed CEFR sense badge.
This auditor cannot approve content, audio, iPhone QA or deployment.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-C1-TWELVE-INDEXED-LEXICAL-SENSE-TRIAGE-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "9cd5b7a4d3b50474ce9079f05c218572c35f3d9a"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
TARGET = {level: 200 for level in LEVELS}
ZERO = {level: 0 for level in LEVELS}
RISKS = {
    "ambivalence": "MIXED_FEELINGS_VS_UNCERTAINTY",
    "anachronism": "HISTORICAL_MISPLACEMENT_VS_OBSOLETE",
    "antipathy": "STRONG_DISLIKE_AND_PREPOSITION",
    "arbitrate": "ARBITRATION_DECISION_VS_MEDIATION",
    "belligerent": "HOSTILE_PERSON_VS_WARRING_STATE",
    "benevolent": "KIND_PERSON_VS_CHARITABLE_ORGANISATION",
    "brevity": "CONCISENESS_VS_SHORT_DURATION",
    "circumspect": "CAUTION_VS_TIMIDITY",
    "coercion": "FORCE_VS_ORDINARY_PERSUASION",
    "conundrum": "DIFFICULT_PROBLEM_VS_RIDDLE",
    "corroborate": "SUPPORTING_EVIDENCE_VS_ABSOLUTE_PROOF",
    "credence": "UNCOUNTABLE_CREDENCE_VS_CREDIBILITY",
}

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

def git_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def validate(packet, shortlist, baseline):
    require(packet.get("schema") == 1
            and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == "C1_TWELVE_CAMBRIDGE_INDEXED_LEXICAL_SENSE_TRIAGE_EDITORIAL_HOLD"
            and packet.get("observed_on") == "2026-10-31", "Scope/date/status drift")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_BLOB, "Shortlist binding drift")
    require(packet.get("record_count") == 12 and isinstance(packet.get("records"), list)
            and len(packet["records"]) == 12, "Cardinality drift")
    require(packet.get("first_pass_written_by_level") == TARGET
            and packet.get("independently_approved_by_level") == ZERO,
            "Fabricated counts or independent approval")
    require(packet.get("publisher_cefr_badges_observed_in_extract") == 0,
            "Fabricated CEFR badge")
    limitations = packet.get("source_access_limitations", "")
    require("HTTP 403" in limitations and "NOT a verified claim" in limitations
            and "not direct Oxford" in limitations, "Source limitations suppressed")
    require(packet.get("release_approved") is False
            and packet.get("independent_human_review_receipts") == []
            and packet.get("audio_listening_receipts") == [],
            "False signoff or audio claim")
    require(shortlist.get("counts_by_level") == TARGET
            and shortlist.get("independently_approved_by_level") == ZERO,
            "Frozen shortlist counts/approvals changed")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Shortlist cardinality drift")
    for level in LEVELS:
        require(sum(e.get("level") == level for e in entries) == 200,
                "Level quota changed: " + level)
    require(len({e.get("word", "").casefold() for e in entries}) == 1000,
            "Duplicate headword in provisional shortlist")
    lookup = {e["word"]: e for e in entries}
    rows = packet["records"]
    require({r.get("word") for r in rows} == set(RISKS), "Wrong or duplicate headwords")
    frozen = {r["word"]: r for r in baseline["records"]}
    for row in rows:
        word = row["word"]
        source = lookup[word]
        pub = row.get("publisher_source", {})
        require(row.get("level") == source["level"] == "C1"
                and row.get("part_of_speech") == source["part_of_speech"],
                "Level/POS mismatch: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": source["english_definition"],
            "myanmar_meaning": source["burmese_meaning"],
            "example_sentence": source["example_sentence"],
        }, "Original bilingual/example mismatch: " + word)
        require(row.get("shortlist_provenance") == {
            k: source[k] for k in ("source_path", "source_index", "source_blob_sha")
        }, "Historical provenance mismatch: " + word)
        require(pub.get("publisher") == "Cambridge University Press"
                and pub.get("url") == "https://dictionary.cambridge.org/dictionary/english/" + word
                and pub.get("observed_on") == "2026-10-31"
                and pub.get("access") == "PUBLIC_SEARCH_INDEX_EXTRACT_DIRECT_PAGE_403_ON_SAMPLED_URLS"
                and pub.get("evidence_scope") == "LEXICAL_SENSE_AND_GRAMMAR_RESEARCH_LEAD_NOT_INDEPENDENT_REVIEW"
                and pub.get("cefr_badge_in_observed_extract") is None,
                "Publisher source or CEFR badge misrepresented: " + word)
        require(pub.get("source_summary") == frozen[word]["publisher_source"]["source_summary"],
                "Publisher summary changed: " + word)
        require(row.get("editorial_risk") == RISKS[word], "Risk erased: " + word)
        candidate = row.get("unapproved_rewrite_candidate", {})
        require(candidate == frozen[word]["unapproved_rewrite_candidate"]
                and candidate.get("status") == "UNAPPROVED_ASSISTANT_PROPOSAL"
                and bool(candidate.get("myanmar_meaning"))
                and bool(candidate.get("original_example")),
                "Bilingual candidate drift or false approval: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "Forged reviewer signoff: " + word)
    return {"scope": "STAGING_ONLY", "lexical_sense_leads": 12,
            "observed_cefr_badges": 0, "direct_oxford_coverage_increment": 0,
            "first_pass_written_by_level": TARGET,
            "independently_approved_by_level": ZERO,
            "release": "BLOCKED_INDEPENDENT_EXACT_SENSE_CEFR_EVIDENCE_MISSING"}

def self_test(packet, shortlist):
    rejected = 0
    def must_reject(forged):
        nonlocal rejected
        try:
            validate(forged, shortlist, packet)
        except (ValueError, TypeError, KeyError):
            rejected += 1
        else:
            raise AssertionError("Adversarial mutation unexpectedly accepted")
    for i, row in enumerate(packet["records"]):
        for field, value in [
            ("word", "fakeword"), ("level", "B2"), ("part_of_speech", "adverb"),
            ("editorial_risk", "NO_RISK"), ("editorial_hold", False),
            ("independently_reviewed", True), ("release_approved", True),
            ("independent_reviewer_receipt", {"reviewer": "AI", "result": "PASS"}),
        ]:
            fake = copy.deepcopy(packet)
            fake["records"][i][field] = value
            must_reject(fake)
        for field, value in [
            ("url", "https://example.com/fake"),
            ("publisher", "Unverified"),
            ("observed_on", "2025-01-01"),
            ("access", "DIRECT_LIVE_PUBLISHER_PAGE"),
            ("evidence_scope", "INDEPENDENT_EXACT_SENSE_CEFR_APPROVED"),
            ("cefr_badge_in_observed_extract", "C1"),
            ("source_summary", "False publisher observation"),
        ]:
            fake = copy.deepcopy(packet)
            fake["records"][i]["publisher_source"][field] = value
            must_reject(fake)
        for field, value in [
            ("english_definition", "Changed definition"),
            ("myanmar_meaning", "အတည်ပြုပြီး"),
            ("example_sentence", "Changed example."),
        ]:
            fake = copy.deepcopy(packet)
            fake["records"][i]["shortlist_snapshot"][field] = value
            must_reject(fake)
        for field, value in [
            ("source_path", "draft/forged.json"),
            ("source_index", -1),
            ("source_blob_sha", "0" * 40),
        ]:
            fake = copy.deepcopy(packet)
            fake["records"][i]["shortlist_provenance"][field] = value
            must_reject(fake)
        fake = copy.deepcopy(packet)
        fake["records"][i]["unapproved_rewrite_candidate"]["status"] = "APPROVED"
        must_reject(fake)
    for field, value in [
        ("release_approved", True),
        ("independent_human_review_receipts", [{"reviewer": "AI"}]),
        ("audio_listening_receipts", [{"voice": "George", "listened": True}]),
        ("publisher_cefr_badges_observed_in_extract", 12),
        ("source_access_limitations", "Fully verified"),
        ("record_count", 1000),
        ("independently_approved_by_level", {**ZERO, "C1": 12}),
    ]:
        fake = copy.deepcopy(packet)
        fake[field] = value
        must_reject(fake)
    return rejected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    require(git_blob(PACKET) == PACKET_BLOB, "Source packet blob SHA changed")
    require(git_blob(SHORTLIST) == SHORTLIST_BLOB, "Frozen shortlist blob SHA changed")
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf8"))
    result = validate(packet, shortlist, packet)
    result["level_lane"] = args.level
    if args.self_test:
        result["forged_mutations_rejected"] = self_test(packet, shortlist)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
