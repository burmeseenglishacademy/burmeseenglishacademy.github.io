#!/usr/bin/env python3
"""Third twelve A1 Oxford word/POS source observations; not human review or approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-THIRD-TWELVE-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE_URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
EXPECTED = {
    "goodbye": (2, 333, "goodbye exclam./n."),
    "thank": (3, 779, "thank v."),
    "water": (4, 861, "water n."),
    "food": (2, 302, "food n."),
    "home": (2, 372, "home n., adv."),
    "family": (2, 268, "family n., adj."),
    "mother": (2, 497, "mother n."),
    "father": (2, 276, "father n."),
    "school": (3, 669, "school n."),
    "teacher": (3, 767, "teacher n."),
    "student": (3, 745, "student n."),
    "book": (1, 96, "book n."),
}
EXPECTED_RISKS = {
    "goodbye": "EXCLAMATION_VS_NOUN_SCOPE",
    "thank": "STILTED_ORIGINAL_EXAMPLE",
    "water": "OVER_NARROW_ENGLISH_DEFINITION",
    "food": "COLLECTIVE_UNCOUNTABLE_USAGE",
    "home": "HOME_NOUN_ADVERB_EXAMPLE_MISMATCH",
    "family": "FAMILY_NOUN_VS_ADJECTIVE_SCOPE",
    "mother": "PARENT_KINSHIP_REGISTER",
    "father": "PARENT_KINSHIP_REGISTER",
    "school": "INSTITUTION_VS_BUILDING_SENSE",
    "teacher": "GENDER_NEUTRAL_OCCUPATION",
    "student": "STUDENT_SCOPE_AND_GENDER",
    "book": "BOOK_NOUN_VS_VERB_SCOPE",
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet, shortlist, actual_blob):
    require(actual_blob == SHORTLIST_BLOB, "Original shortlist blob drift")
    require(packet.get("schema") == 1, "Wrong packet schema")
    require(packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Scope drift")
    require(packet.get("status") == "A1_THIRD_TWELVE_DIRECT_OXFORD_WORD_POS_LEADS_EDITORIAL_HOLD", "Status drift")
    require(packet.get("observed_on") == "2026-10-28", "Observation date drift")
    require(packet.get("shortlist_blob_sha") == actual_blob, "Packet shortlist SHA drift")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 12, "Wrong record count")
    require(packet.get("counts_by_level") == {"A1": 12, "A2": 0, "B1": 0, "B2": 0, "C1": 0}, "Level counts drift")
    require(type(packet.get("independently_approved_count")) is int and packet["independently_approved_count"] == 0, "False independent approval count")
    require("NOT independently verified" in packet.get("source_limitations", ""), "Source limitations removed")
    require(shortlist.get("scope_target") == {x: 200 for x in ("A1", "A2", "B1", "B2", "C1")}, "Shortlist target changed")
    require(shortlist.get("independently_approved_by_level") == {x: 0 for x in ("A1", "A2", "B1", "B2", "C1")}, "Shortlist approval changed")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Not exactly 1000 provisional entries")
    counts = {x: sum(e.get("level") == x for e in entries) for x in ("A1", "A2", "B1", "B2", "C1")}
    require(counts == {x: 200 for x in counts}, "Not 200 per level")
    indexed = {(e["word"], e["level"]): e for e in entries}
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == 12, "Not 12 observations")
    require({r.get("word") for r in records if isinstance(r, dict)} == set(EXPECTED), "Missing, extra or duplicate word")
    for r in records:
        word = r["word"]
        e = indexed.get((word, "A1"))
        require(e is not None and r.get("level") == "A1", "Unbound A1 word")
        require(r.get("part_of_speech") == e.get("part_of_speech"), word + " POS snapshot drift")
        require(r.get("shortlist_snapshot") == {
            "english_definition": e["english_definition"],
            "myanmar_meaning": e["burmese_meaning"],
            "example_sentence": e["example_sentence"],
        }, word + " bilingual/example drift")
        require(r.get("shortlist_provenance") == {
            "source_path": e["source_path"],
            "source_index": e["source_index"],
            "source_blob_sha": e["source_blob_sha"],
        }, word + " source provenance drift")
        page, line, excerpt = EXPECTED[word]
        require(r.get("publisher_source") == {
            "publisher": "Oxford University Press",
            "title": "The Oxford 3000 by CEFR level",
            "url": SOURCE_URL,
            "observed_on": "2026-10-28",
            "pdf_page": page,
            "extracted_line": line,
            "source_excerpt": excerpt,
            "source_cefr_level": "A1",
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT",
        }, word + " publisher source observation drift")
        require(r.get("editorial_risk") == EXPECTED_RISKS[word], word + " editorial risk drift")
        require(isinstance(r.get("independent_reviewer_task"), str) and "Require separate dated human exact-sense CEFR" in r["independent_reviewer_task"], word + " missing independent review task")
        require(r.get("editorial_hold") is True and e.get("editorial_hold") is True, word + " not on hold")
        require(r.get("independently_reviewed") is False and r.get("release_approved") is False, word + " false review")
        require(r.get("independent_reviewer_receipt") is None, word + " invented review receipt")
        require(all(e.get(flag) is False for flag in (
            "reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level",
            "reviewed_pronunciation", "release_approved")), word + " shortlist approval drift")
    return counts

def negative_tests(packet, shortlist, sha):
    mutations = [
        ("word", lambda p: p["records"][0].__setitem__("word", "not-the")),
        ("level", lambda p: p["records"][0].__setitem__("level", "B2")),
        ("pos", lambda p: p["records"][0].__setitem__("part_of_speech", "noun")),
        ("source-url", lambda p: p["records"][0]["publisher_source"].__setitem__("url", "https://example.com/fake")),
        ("source-date", lambda p: p["records"][0]["publisher_source"].__setitem__("observed_on", "2026-10-27")),
        ("source-page", lambda p: p["records"][0]["publisher_source"].__setitem__("pdf_page", 99)),
        ("source-line", lambda p: p["records"][0]["publisher_source"].__setitem__("extracted_line", 123)),
        ("source-excerpt", lambda p: p["records"][0]["publisher_source"].__setitem__("source_excerpt", "the n.")),
        ("source-cefr", lambda p: p["records"][0]["publisher_source"].__setitem__("source_cefr_level", "B2")),
        ("source-scope", lambda p: p["records"][0]["publisher_source"].__setitem__("evidence_scope", "EXACT_SENSE")),
        ("source-access", lambda p: p["records"][0]["publisher_source"].__setitem__("access", "HUMAN_VERIFIED")),
        ("english", lambda p: p["records"][0]["shortlist_snapshot"].__setitem__("english_definition", "altered")),
        ("myanmar", lambda p: p["records"][0]["shortlist_snapshot"].__setitem__("myanmar_meaning", "အတည်ပြုပြီး")),
        ("example", lambda p: p["records"][0]["shortlist_snapshot"].__setitem__("example_sentence", "changed")),
        ("source-index", lambda p: p["records"][0]["shortlist_provenance"].__setitem__("source_index", 900)),
        ("source-blob", lambda p: p["records"][0]["shortlist_provenance"].__setitem__("source_blob_sha", "0"*40)),
        ("risk", lambda p: p["records"][0].__setitem__("editorial_risk", "")),
        ("risk-substitution", lambda p: p["records"][0].__setitem__("editorial_risk", "MISLEADING_SUBSTITUTE")),
        ("task", lambda p: p["records"][0].__setitem__("independent_reviewer_task", "approved")),
        ("hold", lambda p: p["records"][0].__setitem__("editorial_hold", False)),
        ("review", lambda p: p["records"][0].__setitem__("independently_reviewed", True)),
        ("approval", lambda p: p["records"][0].__setitem__("release_approved", True)),
        ("receipt", lambda p: p["records"][0].__setitem__("independent_reviewer_receipt", {"reviewer_id": "fake"})),
        ("home-risk", lambda p: next(r for r in p["records"] if r["word"] == "home").__setitem__("editorial_risk", "NO_MISMATCH")),
        ("count", lambda p: p.__setitem__("record_count", 13)),
        ("packet-sha", lambda p: p.__setitem__("shortlist_blob_sha", "0"*40)),
        ("duplicate", lambda p: p["records"].__setitem__(1, copy.deepcopy(p["records"][0]))),
        ("source-limits", lambda p: p.__setitem__("source_limitations", "fully verified")),
    ]
    for name, mutate in mutations:
        altered = copy.deepcopy(packet)
        mutate(altered)
        try:
            audit(altered, shortlist, sha)
        except (ValueError, KeyError, TypeError, AttributeError):
            continue
        raise AssertionError("FAIL: accepted forged source/review mutation: " + name)
    return len(mutations)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=["A1", "A2", "B1", "B2", "C1", "ALL"], default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    data = SHORTLIST.read_bytes()
    shortlist = json.loads(data)
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    sha = blob_sha(data)
    counts = audit(packet, shortlist, sha)
    negative = negative_tests(packet, shortlist, sha) if args.self_test else 0
    observed = 12 if args.level in ("A1", "ALL") else 0
    report = {
        "scope": "STAGING_ONLY_NO_DEPLOYMENT",
        "level": args.level,
        "first_pass_written": 1000 if args.level == "ALL" else counts[args.level],
        "direct_oxford_word_pos_observations_in_this_packet": observed,
        "independently_approved": 0,
        "negative_mutations_rejected": negative,
        "not_exact_sense_review": True,
        "release_blocked": True,
        "shortlist_blob_sha": sha,
    }
    path = ROOT / ("cefr-1000-oxford-a1-third-twelve-" + args.level + ".json")
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf8")
    print(json.dumps(report, sort_keys=True))

if __name__ == "__main__":
    main()
