#!/usr/bin/env python3
"""Fail-closed, staging-only audit of five held B1 exact-sense research cards.

Mechanical source/provenance checks are NOT independent language review,
pronunciation listening, device testing or deployment approval.
"""
import argparse
import collections
import copy
import datetime
import hashlib
import json
import pathlib
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B1-FIVE-DEMAND-SUPPLY-FEATURE-APPLY-AUTHORITY-SENSE-TRIAGE-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_BLOB = "156f61c533e13e243f64dd8470a1cde9d85242af"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_BLOB = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
EXPECTED = {
    "demand": ("noun", 381, "demand_1", "182-190", "B2",
               "B1_VS_INDEXED_B2_EXACT_SENSE"),
    "supply": ("noun", 605, "supply_1", "109-115,165-203", None,
               "COUNTABILITY_AND_MATERIAL_VS_QUANTITY_GLOSS"),
    "feature": ("noun", 690, "feature_1", "103-117,156-160", None,
                "TECHNICAL_FUNCTION_VS_GENERAL_CHARACTERISTIC"),
    "apply": ("verb", 693, "apply", "110-128,133-155", "B1",
              "B1_INDEXED_ALIGNMENT_CONTROL_GRAMMAR"),
    "authority": ("noun", 694, "authority", "108-116,150-159,181-187", "B2",
                  "B1_VS_INDEXED_B2_POWER_SENSE"),
}
FROZEN_KEYS = ("word", "level", "part_of_speech", "english_definition",
               "burmese_meaning", "example_sentence", "source_path",
               "source_index", "source_blob_sha", "editorial_hold",
               *FLAGS, "status")


def fail(message):
    raise ValueError(message)


def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_hold(entry, label):
    if entry.get("editorial_hold") is not True:
        fail(label + ": editorial hold lost")
    for key in FLAGS:
        if entry.get(key) is not False:
            fail(label + ": forged or missing review flag " + key)
    if entry.get("independently_approved", False) is not False:
        fail(label + ": independent approval forged")


def validate(packet, shortlist, source):
    if packet.get("schema") != 1 or packet.get("created_on") != "2026-11-02":
        fail("research schema/date mismatch")
    if (packet.get("branch") != "cefr-5000-bilingual-qa-staging"
            or packet.get("scope") != "USER_APPROVED_1000_TOTAL_NOT_5000"
            or packet.get("release_status") != "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"):
        fail("scope or release status mismatch")
    if packet.get("shortlist_path") != "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json":
        fail("shortlist path mismatch")
    if packet.get("shortlist_blob_sha") != SHORTLIST_BLOB:
        fail("shortlist provenance mismatch")
    limits = packet.get("source_limitations", "")
    if not all(t in limits for t in ("HTTP 403", "search-index", "unapproved", "not establish")):
        fail("source limitations absent or weakened")
    targets = {x: 200 for x in LEVELS}
    zeros = {x: 0 for x in LEVELS}
    if (packet.get("counts_by_level") != targets
            or packet.get("independently_approved_by_level") != zeros):
        fail("research packet quotas or approval totals changed")
    if (shortlist.get("counts_by_level") != targets
            or shortlist.get("independently_approved_by_level") != zeros
            or len(shortlist.get("entries", [])) != 1000):
        fail("frozen shortlist quota/approval mismatch")
    counted = collections.Counter(x.get("level") for x in shortlist["entries"])
    if dict(counted) != targets:
        fail("frozen per-level count mismatch")
    heads = [x.get("word", "").casefold() for x in shortlist["entries"]]
    if len(set(heads)) != 1000:
        fail("frozen headword deduplication failed")
    by_word = {x["word"]: x for x in shortlist["entries"] if x.get("level") == "B1"}
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 5 or packet.get("research_record_count") != 5:
        fail("wrong record count")
    if {r.get("word") for r in records} != set(EXPECTED):
        fail("wrong/duplicated research headwords")
    for r in records:
        word = r["word"]
        pos, index, slug, lines, badge, risk = EXPECTED[word]
        if r.get("level") != "B1" or r.get("part_of_speech") != pos:
            fail(word + ": POS/level mismatch")
        original = r.get("frozen_original")
        if not isinstance(original, dict) or original != by_word[word]:
            fail(word + ": frozen bilingual/source record changed")
        if (original.get("source_path") != "draft/A2-C1-EDITORIAL-STARTER.json"
                or original.get("source_blob_sha") != SOURCE_BLOB
                or original.get("source_index") != index):
            fail(word + ": historical source provenance changed")
        historical = source["entries"][index]
        for key in ("word", "level", "part_of_speech", "english_definition",
                    "burmese_meaning", "example_sentence"):
            if original.get(key) != historical.get(key):
                fail(word + ": historical " + key + " changed")
        check_hold(original, word + " original")
        check_hold(r, word + " research")
        if r.get("proposed_alternative_unapproved") is not True:
            fail(word + ": proposed content not marked unapproved")
        for field in ("proposed_english_definition", "proposed_myanmar_meaning",
                      "proposed_original_example", "evidence_note"):
            if not isinstance(r.get(field), str) or len(r[field].strip()) < 22:
                fail(word + ": missing substantive " + field)
        if not any("\u1000" <= c <= "\u109f" for c in r["proposed_myanmar_meaning"]):
            fail(word + ": Myanmar script missing")
        if word.casefold() not in r["proposed_original_example"].casefold():
            fail(word + ": original example does not demonstrate headword")
        if r.get("risk_category") != risk or r.get("observed_on") != "2026-11-02":
            fail(word + ": research category/date changed")
        ox = r.get("oxford_direct")
        if not isinstance(ox, dict):
            fail(word + ": Oxford observation missing")
        if (ox.get("url") != "https://www.oxfordlearnersdictionaries.com/definition/english/" + slug
                or ox.get("lines") != lines or ox.get("access") != "DIRECT_PAGE_OPENED"
                or ox.get("purpose") != "SENSE_AND_GRAMMAR_NOT_CEFR_SIGNOFF"
                or len(str(ox.get("scope", ""))) < 30):
            fail(word + ": Oxford source locator/access changed")
        cam = r.get("cambridge_indexed")
        if not isinstance(cam, dict):
            fail(word + ": Cambridge indexed evidence missing")
        if (cam.get("url") != "https://dictionary.cambridge.org/dictionary/english/" + word
                or cam.get("access") != "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"
                or cam.get("observed_cefr_badge") != badge
                or len(str(cam.get("observed_sense", ""))) < 25):
            fail(word + ": Cambridge indexed badge/access misrepresented")
    return {"scope": "STAGING_RESEARCH_ONLY", "level": "B1", "source_bound_records": 5,
            "indexed_B2_conflicts": 2, "indexed_B1_alignment_control": 1,
            "unlabelled_exact_sense": 2, "independently_approved": 0,
            "real_listening_signoffs": 0, "release": "BLOCKED_STAGING_ONLY"}


def self_test(packet, shortlist, source):
    validate(packet, shortlist, source)
    attempts = 0
    for i in range(5):
        edits = [
            ("level", "C1"), ("part_of_speech", "adjective"),
            ("observed_on", "2026-11-03"),
            ("risk_category", "INDEPENDENTLY_VERIFIED"),
            ("editorial_hold", False), ("independently_approved", True),
            ("proposed_alternative_unapproved", False),
            ("reviewed_english", True), ("reviewed_burmese", True),
            ("reviewed_example", True), ("reviewed_level", True),
            ("reviewed_pronunciation", True), ("release_approved", True),
            ("proposed_myanmar_meaning", "English only"),
            ("proposed_original_example", "There is a problem."),
            ("evidence_note", "fake"),
        ]
        for key, value in edits:
            altered = copy.deepcopy(packet)
            altered["records"][i][key] = value
            try:
                validate(altered, shortlist, source)
            except (ValueError, KeyError, IndexError, TypeError):
                attempts += 1
            else:
                fail("self-test accepted forged " + packet["records"][i]["word"] + ":" + key)
        for group, key, value in [
            ("oxford_direct", "url", "https://example.com/word"),
            ("oxford_direct", "lines", "999-999"),
            ("oxford_direct", "access", "INDEX_ONLY"),
            ("oxford_direct", "purpose", "INDEPENDENT_CEFR_SIGNOFF"),
            ("cambridge_indexed", "url", "https://example.com/word"),
            ("cambridge_indexed", "access", "DIRECT_PUBLISHER_DICTIONARY_PAGE"),
            ("cambridge_indexed", "observed_cefr_badge", "C1"),
            ("frozen_original", "source_index", 0),
            ("frozen_original", "english_definition", "forged"),
            ("frozen_original", "burmese_meaning", "forged"),
            ("frozen_original", "example_sentence", "forged"),
            ("frozen_original", "reviewed_level", True),
        ]:
            altered = copy.deepcopy(packet)
            altered["records"][i][group][key] = value
            try:
                validate(altered, shortlist, source)
            except (ValueError, KeyError, IndexError, TypeError):
                attempts += 1
            else:
                fail("self-test accepted forged nested field " + group + ":" + key)
    for key, value in [("release_status", "APPROVED"), ("source_limitations", "Verified"),
                       ("counts_by_level", {x: 201 for x in LEVELS}),
                       ("independently_approved_by_level", {x: 200 for x in LEVELS}),
                       ("research_record_count", 6), ("shortlist_blob_sha", "0" * 40)]:
        altered = copy.deepcopy(packet)
        altered[key] = value
        try:
            validate(altered, shortlist, source)
        except (ValueError, KeyError, IndexError, TypeError):
            attempts += 1
        else:
            fail("self-test accepted forged packet field " + key)
    return attempts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    for path, expected in ((PACKET, PACKET_BLOB), (SHORTLIST, SHORTLIST_BLOB),
                           (SOURCE, SOURCE_BLOB)):
        if git_blob_sha(path) != expected:
            fail("pinned Git blob changed: " + str(path.relative_to(ROOT)))
    packet, shortlist, source = map(load, (PACKET, SHORTLIST, SOURCE))
    result = validate(packet, shortlist, source)
    result["level_lane"] = args.level
    if args.self_test:
        result["synthetic_forged_mutations_rejected"] = self_test(packet, shortlist, source)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
