#!/usr/bin/env python3
"""Fail-closed staging auditor for nine Cambridge C1 indexed sense leads.

Public search-index observations are NOT direct dictionary-page inspection,
independent review, final CEFR proof, audio listening, or publication approval.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-C1-NINE-INDEXED-SENSE-AND-POS-TRIAGE-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "7d5efd10b8f988ebf19fc240358087bad6a16d11"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "naval": ("C2", "ADJECTIVE_SAME_SENSE_HIGHER_THAN_C1"),
    "noble": ("C1", "ADJECTIVE_MORAL_SENSE_MATCH_LEAD"),
    "treasury": (None, "UNLABELLED_GOVERNMENT_DEPARTMENT_CAPITALIZATION"),
    "ethics": ("C2", "C2_STUDY_SENSE_VS_DRAFT_PRINCIPLES"),
    "manufacturer": ("B2", "NOUN_SAME_SENSE_LOWER_THAN_C1"),
    "veteran": ("C2", "PUBLISHER_NOUN_NOT_DRAFT_ADJECTIVE"),
    "legally": ("B2", "ADVERB_SAME_SENSE_LOWER_THAN_C1"),
    "destiny": ("C1", "COUNTABLE_FUTURE_VS_UNCOUNTABLE_FATE"),
    "census": (None, "UNLABELLED_COUNTABLE_OFFICIAL_POPULATION_COUNT"),
}
TARGET = {level: 200 for level in LEVELS}
ZERO = {level: 0 for level in LEVELS}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def validate(packet, shortlist, baseline):
    require(packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Wrong project scope")
    require(packet.get("schema") == 1 and packet.get("observed_on") == "2026-10-31",
            "Wrong schema or observation date")
    require(packet.get("status") == "C1_NINE_CAMBRIDGE_INDEXED_SENSE_TRIAGE_EDITORIAL_HOLD",
            "Incorrect staging status")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_BLOB, "Frozen shortlist provenance drift")
    require(packet.get("first_pass_written_by_level") == TARGET, "First-pass count drift")
    require(packet.get("independently_approved_by_level") == ZERO, "Forged approvals")
    require(packet.get("publisher_cefr_leads") == {"C1": 2, "B2": 2, "C2": 3, "UNLABELLED": 2},
            "Publisher indexed level counts drift")
    require(packet.get("pos_mismatch_records") == ["veteran"], "Noun/adjective POS mismatch suppressed")
    require("HTTP 403" in packet.get("source_access_limitations", "")
            and "not Oxford observations" in packet["source_access_limitations"],
            "Indexed-only source limitations suppressed")
    require(packet.get("release_approved") is False
            and packet.get("independent_human_review_receipts") == []
            and packet.get("audio_listening_receipts") == [], "False independent review/audio approval")
    require(shortlist.get("counts_by_level") == TARGET
            and shortlist.get("independently_approved_by_level") == ZERO,
            "Frozen shortlist scope or approval drift")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000,
            "Frozen shortlist must have 1000 entries")
    by_word = {x["word"]: x for x in entries}
    require(len(by_word) == 1000, "Duplicate provisional headwords")
    rows = packet.get("records")
    require(isinstance(rows, list) and len(rows) == 9
            and packet.get("record_count") == 9, "Wrong indexed source packet cardinality")
    require({r.get("word") for r in rows} == set(EXPECTED), "Wrong or repeated source headwords")
    frozen = {r["word"]: r for r in baseline["records"]}
    for row in rows:
        word = row["word"]
        source = by_word[word]
        pub = row.get("publisher_source", {})
        require(row.get("level") == source["level"] == "C1"
                and row.get("part_of_speech") == source["part_of_speech"],
                "Shortlist level/POS drift: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": source["english_definition"],
            "myanmar_meaning": source["burmese_meaning"],
            "example_sentence": source["example_sentence"],
        }, "Frozen bilingual/example snapshot drift: " + word)
        require(row.get("shortlist_provenance") == {
            k: source[k] for k in ("source_path", "source_index", "source_blob_sha")
        }, "Historical Git source provenance drift: " + word)
        require(pub.get("publisher") == "Cambridge University Press"
                and pub.get("observed_on") == "2026-10-31"
                and pub.get("access") == "PUBLIC_SEARCH_INDEX_CACHED_DIRECT_PAGE_403"
                and pub.get("evidence_scope") == "PUBLISHER_INDEXED_SENSE_LEAD_NOT_HUMAN_REVIEW",
                "Indexed evidence misrepresented as direct publisher inspection: " + word)
        require(pub.get("source_cefr_level") == EXPECTED[word][0]
                and row.get("editorial_risk") == EXPECTED[word][1],
                "Publisher sense/POS conflict or level drift: " + word)
        require(pub.get("url") == frozen[word]["publisher_source"]["url"]
                and pub.get("source_summary") == frozen[word]["publisher_source"]["source_summary"],
                "Source URL or indexed observation modified: " + word)
        require(row.get("unapproved_rewrite_candidate") == frozen[word]["unapproved_rewrite_candidate"]
                and row["unapproved_rewrite_candidate"].get("status") == "UNAPPROVED_ASSISTANT_PROPOSAL",
                "Bilingual/example candidate changed or falsely approved: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "Forged independent review: " + word)
    return {"scope": "STAGING_ONLY", "C1_indexed_sense_leads": 9,
            "indexed_C1": 2, "indexed_B2": 2, "indexed_C2": 3,
            "indexed_unlabelled": 2, "publisher_pos_mismatch": ["veteran"],
            "independently_approved_by_level": ZERO, "direct_oxford_coverage_increment": 0,
            "release": "BLOCKED_NOT_INDEPENDENTLY_REVIEWED"}


def self_test(packet, shortlist):
    mutations = 0
    for index in range(9):
        for field, value in [
            ("word", "fabricated"), ("level", "B2"),
            ("part_of_speech", "noun" if packet["records"][index]["part_of_speech"] != "noun" else "adjective"),
            ("editorial_risk", "NO_RISK"), ("editorial_hold", False),
            ("independently_reviewed", True), ("release_approved", True),
            ("independent_reviewer_receipt", {"reviewer_id": "AI", "result": "PASS"}),
        ]:
            forged = copy.deepcopy(packet)
            forged["records"][index][field] = value
            try:
                validate(forged, shortlist, packet)
            except (ValueError, KeyError, TypeError):
                mutations += 1
            else:
                raise AssertionError("Forged " + field + " accepted")
        for key, value in [
            ("source_cefr_level", "A1"), ("access", "DIRECT_PUBLISHER_DICTIONARY_PAGE"),
            ("evidence_scope", "PUBLISHER_EXACT_SENSE_CEFR_LABEL"),
            ("url", "https://example.com/forged/word"),
            ("source_summary", "Unsubstantiated automatic approval"),
        ]:
            forged = copy.deepcopy(packet)
            forged["records"][index]["publisher_source"][key] = value
            try:
                validate(forged, shortlist, packet)
            except (ValueError, KeyError, TypeError):
                mutations += 1
            else:
                raise AssertionError("Forged publisher " + key + " accepted")
        for key, value in [
            ("english_definition", "Fabricated English definition"),
            ("myanmar_meaning", "အတည်ပြုပြီး"),
            ("example_sentence", "Fake example."),
        ]:
            forged = copy.deepcopy(packet)
            forged["records"][index]["shortlist_snapshot"][key] = value
            try:
                validate(forged, shortlist, packet)
            except (ValueError, KeyError, TypeError):
                mutations += 1
            else:
                raise AssertionError("Forged bilingual " + key + " accepted")
    for field, value in [
        ("release_approved", True),
        ("independent_human_review_receipts", [{"reviewer_id": "AI", "result": "PASS"}]),
        ("audio_listening_receipts", [{"voice": "George", "result": "PASS"}]),
        ("publisher_cefr_leads", {"C1": 9}),
        ("pos_mismatch_records", []),
    ]:
        forged = copy.deepcopy(packet)
        forged[field] = value
        try:
            validate(forged, shortlist, packet)
        except (ValueError, KeyError, TypeError):
            mutations += 1
        else:
            raise AssertionError("Forged global " + field + " accepted")
    return mutations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    require(git_blob(PACKET) == PACKET_BLOB, "Source packet Git blob SHA mismatch")
    require(git_blob(SHORTLIST) == SHORTLIST_BLOB, "Frozen shortlist Git blob SHA mismatch")
    packet = json.loads(PACKET.read_text("utf8"))
    shortlist = json.loads(SHORTLIST.read_text("utf8"))
    result = validate(packet, shortlist, packet)
    result["level_lane"] = args.level
    if args.self_test:
        result["forged_mutations_rejected"] = self_test(packet, shortlist)
    output = ROOT / ("cefr-1000-cambridge-c1-nine-" + args.level + ".json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
