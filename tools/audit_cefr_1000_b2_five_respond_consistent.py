#!/usr/bin/env python3
"""Fail-closed STAGING-ONLY Cambridge B2 five-sense provenance audit.

Publisher-index observations are NOT independent English/Myanmar/CEFR reviews.
Never modifies production, shortlist, review tasks, audio or approval evidence.
"""
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B2-FIVE-RESPOND-CONDUCT-CONSISTENT-ESTABLISH-OCCUR-CAMBRIDGE-2026-11-03.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
HISTORICAL = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_SHA = "6812a2bbbc716459142dbc1ca9c7942a23ad807a"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
HISTORICAL_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
TARGETS = {x: 200 for x in ("A1", "A2", "B1", "B2", "C1")}
WORDS = {
    "respond": ("B2", "ALIGNED_SAME_SENSE_LEAD", 236, "learner-english/respond"),
    "conduct": ("B2", "ALIGNED_SAME_SENSE_LEAD", 250, "english/conduct"),
    "consistent": ("C2", "HIGHER_SAME_SENSE_CONFLICT", 452, "english/consistent"),
    "establish": ("B2", "ALIGNED_WITH_SCOPE_CAVEAT", 625, "english/establish"),
    "occur": ("B2", "ALIGNED_SAME_SENSE_LEAD", 906, "english/occur"),
}
FROZEN = ("english_definition", "burmese_meaning", "example_sentence",
          "source_path", "source_index", "source_blob_sha")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
ORIGINAL = ("word", "level", "part_of_speech", "english_definition",
            "burmese_meaning", "example_sentence")

def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def audit(packet, shortlist, historical):
    errors = []
    def check(condition, name):
        if not condition:
            errors.append(name)
    check(packet.get("scope") == "USER_APPROVED_1000_TOTAL_NOT_5000", "scope")
    check(packet.get("release_status") == "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH", "hold")
    check(packet.get("observed_on") == "2026-11-03", "observation date")
    check(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "shortlist provenance")
    check(packet.get("counts_by_level") == TARGETS, "packet quotas")
    check(packet.get("independently_approved_by_level") == dict.fromkeys(TARGETS, 0), "packet approvals")
    check("HTTP 403" in packet.get("method", ""), "publisher access limitation")
    check("not human-independent signoff" in packet.get("method", ""), "no human signoff claim")
    check(shortlist.get("release_status") == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH", "shortlist hold")
    check(shortlist.get("counts_by_level") == TARGETS, "shortlist quotas")
    check(shortlist.get("independently_approved_by_level") == dict.fromkeys(TARGETS, 0), "shortlist approvals")
    rows = shortlist.get("entries", [])
    check(len(rows) == 1000, "exactly 1000 provisional entries")
    check(collections.Counter(x.get("level") for x in rows) == collections.Counter(TARGETS), "200 per level")
    check(len({x.get("word", "").casefold() for x in rows}) == 1000, "global unique written headwords")
    check(all(x.get("editorial_hold") is True and all(x.get(k) is False for k in FLAGS) for x in rows), "shortlist approval flags")
    lookup = {x["word"]: x for x in rows}
    cards = packet.get("entries", [])
    check(len(cards) == len(WORDS) and {x.get("word") for x in cards} == set(WORDS), "exact five cards")
    check(len(historical.get("entries", [])) > 906, "historical source length")
    for card in cards:
        word = card.get("word")
        if word not in WORDS or word not in lookup:
            continue
        indexed, scope, index, suffix = WORDS[word]
        original = lookup[word]
        source = historical["entries"][index]
        check(card.get("level") == "B2" and card.get("part_of_speech") == original["part_of_speech"], word + " lexical slot")
        check(card.get("frozen") == {k: original[k] for k in FROZEN}, word + " frozen original")
        check(all(source.get(k) == original.get(k) for k in ORIGINAL), word + " historical record")
        check(original.get("source_path") == "draft/A2-C1-EDITORIAL-STARTER.json" and original.get("source_index") == index and original.get("source_blob_sha") == HISTORICAL_SHA, word + " historical provenance")
        s = card.get("source", {})
        check(s.get("publisher") == "Cambridge University Press", word + " publisher")
        check(s.get("publisher_url", "").startswith("https://dictionary.cambridge.org/") and s.get("publisher_url", "").endswith(suffix), word + " publisher URL")
        check(s.get("access") == "PUBLISHER_SEARCH_INDEX_ONLY_DIRECT_PAGE_HTTP_403", word + " index-only access")
        check(s.get("observed_on") == "2026-11-03", word + " observation")
        check(s.get("indexed_level") == indexed and s.get("cefr_scope") == scope, word + " CEFR-sense evidence")
        check(s.get("independent_exact_sense_verification") is False, word + " independent-source signoff")
        check(bool(s.get("indexed_sense")) and bool(s.get("british_ipa_lead")), word + " sense/IPA lead")
        check(bool(card.get("editorial_risk")) and "Cambridge" in card.get("editorial_risk", ""), word + " risk")
        alternative = card.get("proposed_alternative", {})
        check(all(isinstance(alternative.get(k), str) and alternative[k].strip() for k in ("english_definition", "burmese_meaning", "example_sentence")), word + " bilingual alternatives")
        check(card.get("proposed_alternative_unapproved") is True and card.get("editorial_hold") is True, word + " hold")
        check(all(card.get(k) is False for k in FLAGS), word + " reviewer/approval flags")
    return errors

def main():
    for path, expected in ((PACKET, PACKET_SHA), (SHORTLIST, SHORTLIST_SHA), (HISTORICAL, HISTORICAL_SHA)):
        assert blob_sha(path) == expected, "Git blob SHA mismatch: " + str(path)
    packet, shortlist, historical = map(load, (PACKET, SHORTLIST, HISTORICAL))
    problems = audit(packet, shortlist, historical)
    assert not problems, "Source-bound audit failed: " + "; ".join(problems)
    mutations = 0
    for i, card in enumerate(packet["entries"]):
        for field, value in (
            ("release_approved", True), ("reviewed_english", True),
            ("reviewed_burmese", True), ("reviewed_example", True),
            ("reviewed_level", True), ("reviewed_pronunciation", True),
            ("editorial_hold", False), ("proposed_alternative_unapproved", False)
        ):
            tampered = copy.deepcopy(packet)
            tampered["entries"][i][field] = value
            assert audit(tampered, shortlist, historical), "forged flag accepted: " + field
            mutations += 1
        for key, value in (("indexed_level", "A1"), ("cefr_scope", "INDEPENDENTLY_APPROVED"),
                           ("access", "DIRECT_PUBLISHER_VERIFIED"), ("independent_exact_sense_verification", True),
                           ("publisher_url", "https://untrusted.example/"), ("observed_on", "2020-01-01")):
            tampered = copy.deepcopy(packet)
            tampered["entries"][i]["source"][key] = value
            assert audit(tampered, shortlist, historical), "forged source accepted: " + key
            mutations += 1
        tampered = copy.deepcopy(packet)
        tampered["entries"][i]["frozen"]["burmese_meaning"] = "UNVERIFIED_REPLACEMENT"
        assert audit(tampered, shortlist, historical), "forged Burmese accepted"
        mutations += 1
    for level in TARGETS:
        tampered = copy.deepcopy(packet)
        tampered["independently_approved_by_level"][level] = 1
        assert audit(tampered, shortlist, historical), "forged level approval accepted"
        mutations += 1
    print(f"PASS: five source-bound B2 cards held; {mutations}/{mutations} synthetic forgeries rejected; 1000 provisional, 0 approved; NO DEPLOY")

if __name__ == "__main__":
    main()
