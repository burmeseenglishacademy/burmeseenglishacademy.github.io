#!/usr/bin/env python3
"""Fail-closed staging audit: six Cambridge-indexed C1 exact-sense research leads.
Search-index evidence is NOT human CEFR approval, direct-page verification or listening.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-CAMBRIDGE-MANUFACTURER-COASTAL-DISABILITY-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_SHA = "b6d6abcf79fdd9273f27fba49b6f1eb817e74b70"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
EXPECTED = {
    "manufacturer": (457, "noun", "B2", "C1_VS_INDEXED_B2_MANUFACTURING_COMPANY"),
    "coastal": (729, "adjective", "B2", "C1_VS_INDEXED_B2_NEAR_SEA"),
    "disability": (456, "noun", "B2", "C1_VS_INDEXED_B2_CONDITION"),
    "permit": (569, "noun", "C1", "C1_INDEXED_NOUN_ALIGNMENT_HETERONYM"),
    "transaction": (458, "noun", "C1", "C1_INDEXED_COMMERCE_ALIGNMENT"),
    "probability": (660, "noun", "C1", "C1_INDEXED_LIKELIHOOD_ALIGNMENT"),
}

def sha(path):
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\\0" + b).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def require(condition, msg):
    if not condition:
        raise ValueError(msg)

def held(card, label):
    require(card.get("editorial_hold") is True, label + ": hold missing")
    require(card.get("independently_approved", False) is False, label + ": forged approval")
    for f in FLAGS:
        require(card.get(f) is False, label + ": forged review flag " + f)

def validate(packet, shortlist, source):
    targets = {level: 200 for level in LEVELS}
    zeros = {level: 0 for level in LEVELS}
    require(packet.get("schema") == 1 and packet.get("created_on") == "2026-11-02", "schema/date")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_NOT_5000", "scope")
    require(packet.get("branch") == "cefr-5000-bilingual-qa-staging", "branch")
    require(packet.get("release_status") == "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH", "release status")
    require(packet.get("shortlist_path") == "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json", "shortlist path")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "shortlist provenance")
    require(packet.get("counts_by_level") == targets and packet.get("independently_approved_by_level") == zeros, "packet quotas/approvals")
    require(shortlist.get("counts_by_level") == targets and shortlist.get("independently_approved_by_level") == zeros, "shortlist quotas/approvals")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000 and dict(collections.Counter(x.get("level") for x in entries)) == targets, "1000 exact quota")
    require(len(set(x.get("word", "").casefold() for x in entries)) == 1000, "duplicate headword")
    require(all(x.get("editorial_hold") is True and all(x.get(f) is False for f in FLAGS) for x in entries), "shortlist review hold")
    limits = packet.get("source_limitations", "")
    require(all(x in limits for x in ("search-index", "HTTP 403", "not independently", "unapproved", "no audio")), "publisher access limitations")
    require(packet.get("research_record_count") == 6 and packet.get("conflict_count") == 3 and packet.get("alignment_control_count") == 3, "research totals")
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == 6, "records count")
    require(set(x.get("word") for x in records) == set(EXPECTED), "duplicate/unknown word")
    source_entries = source.get("entries", [])
    require(len(source_entries) > 729, "historical source missing")
    byword = {x["word"]: x for x in entries}
    for r in records:
        w = r["word"]
        index, pos, badge, risk = EXPECTED[w]
        require(r.get("level") == "C1" and r.get("part_of_speech") == pos, w + ": POS/level")
        require(r.get("source_index") == index and r.get("source_blob_sha") == SOURCE_SHA, w + ": source locator")
        original = r.get("frozen_original")
        require(original == byword[w], w + ": frozen card mismatch")
        held(original, w + " original")
        require(source_entries[index].get("word") == w, w + ": historical source word")
        for f in ("word", "level", "part_of_speech", "english_definition", "burmese_meaning", "example_sentence"):
            require(source_entries[index].get(f) == original.get(f), w + ": historical bilingual drift " + f)
        held(r, w + " research")
        require(r.get("status") == "RESEARCH_LEAD_NOT_HUMAN_REVIEWED", w + ": status")
        require(r.get("review_needed") == [
            "English exact-sense and grammar", "fluent Myanmar meaning",
            "original example naturalness", "independent source-backed CEFR level",
            "British George/Emma headword and example audio listening"], w + ": review tasks")
        pub = r.get("cambridge")
        require(isinstance(pub, dict), w + ": publisher evidence")
        require(pub.get("publisher") == "Cambridge Dictionary, Advanced Learner's Dictionary", w + ": publisher")
        require(pub.get("url") == "https://dictionary.cambridge.org/dictionary/english/" + w, w + ": publisher URL")
        require(urlparse(pub["url"]).hostname == "dictionary.cambridge.org", w + ": source host")
        require(pub.get("observed_on") == "2026-11-02", w + ": observation date")
        require(pub.get("access") == "SEARCH_INDEX_SNIPPET_ONLY_DIRECT_PAGE_HTTP_403", w + ": forged direct access")
        require(pub.get("indexed_cefr") == badge and pub.get("indexed_pos") == pos, w + ": indexed POS/level")
        require(pub.get("exact_sense_risk") == risk, w + ": exact-sense risk")
        require(isinstance(pub.get("editorial_observation"), str) and len(pub["editorial_observation"]) > 70, w + ": observation")
        alt = r.get("unapproved_teaching_alternative")
        require(isinstance(alt, dict), w + ": alternatives")
        for field in ("english_definition", "burmese_meaning", "example_sentence"):
            require(isinstance(alt.get(field), str) and len(alt[field].strip()) > 12, w + ": alternative " + field)
        require(w in alt["example_sentence"].lower(), w + ": example does not illustrate headword")
    return True

def self_test(packet, shortlist, source):
    tested = 0
    for i, record in enumerate(packet["records"]):
        for field, value in (
            ("level", "B2"), ("part_of_speech", "verb"), ("source_index", -1),
            ("source_blob_sha", "forged"), ("editorial_hold", False),
            ("independently_approved", True), ("status", "APPROVED"),
            ("review_needed", []), ("frozen_original", {}),
        ):
            candidate = copy.deepcopy(packet)
            candidate["records"][i][field] = value
            expect_reject(candidate, shortlist, source)
            tested += 1
        for field, value in (
            ("url", "https://evil.example/word"),
            ("access", "DIRECT_PUBLISHER_VERIFIED"),
            ("indexed_cefr", "C2"),
            ("editorial_observation", ""),
        ):
            candidate = copy.deepcopy(packet)
            candidate["records"][i]["cambridge"][field] = value
            expect_reject(candidate, shortlist, source)
            tested += 1
        candidate = copy.deepcopy(packet)
        candidate["records"][i]["unapproved_teaching_alternative"]["example_sentence"] = "This example omits the target."
        expect_reject(candidate, shortlist, source)
        tested += 1
    for field, value in (
        ("scope", "CEFR_5000"), ("branch", "main"), ("release_status", "PUBLISHED"),
        ("source_limitations", ""), ("independently_approved_by_level", {x:200 for x in LEVELS}),
        ("conflict_count", 0), ("research_record_count", 5),
    ):
        candidate = copy.deepcopy(packet)
        candidate[field] = value
        expect_reject(candidate, shortlist, source)
        tested += 1
    candidate = copy.deepcopy(packet)
    candidate["records"][1] = copy.deepcopy(candidate["records"][0])
    expect_reject(candidate, shortlist, source)
    tested += 1
    altered = copy.deepcopy(shortlist)
    altered["entries"][0]["release_approved"] = True
    expect_reject(packet, altered, source)
    tested += 1
    altered = copy.deepcopy(shortlist)
    altered["entries"][0]["word"] = altered["entries"][1]["word"]
    expect_reject(packet, altered, source)
    tested += 1
    print(f"PASS: {tested}/{tested} synthetic negative mutations rejected; no human approval implied")

def expect_reject(packet, shortlist, source):
    try:
        validate(packet, shortlist, source)
    except (ValueError, KeyError, TypeError, IndexError):
        return
    raise AssertionError("Fail-open: synthetic forgery accepted")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    require(sha(PACKET) == PACKET_SHA, "packet Git blob integrity")
    require(sha(SHORTLIST) == SHORTLIST_SHA, "shortlist Git blob integrity")
    require(sha(SOURCE) == SOURCE_SHA, "historical source Git blob integrity")
    packet, shortlist, source = load(PACKET), load(SHORTLIST), load(SOURCE)
    validate(packet, shortlist, source)
    print(f"PASS: six held C1 Cambridge indexed leads; {args.level}; 3 B2 conflicts, 3 C1 controls; zero independent approvals")
    if args.self_test:
        self_test(packet, shortlist, source)

if __name__ == "__main__":
    main()
