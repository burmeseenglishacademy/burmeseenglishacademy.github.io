#!/usr/bin/env python3
"""Staging-only source-bound audit for six held A2 exact-sense research leads.

This validates mechanical provenance and absence of fabricated approvals.
Publisher-index CEFR snippets and our bilingual alternatives are NOT independent
human review. No release, audio generation, or deployment occurs here.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_PATH = ROOT / "draft/CEFR-1000-A2-SIX-WORLD-LIFE-PUBLIC-DATA-POLICE-UNIVERSITY-CAMBRIDGE-OXFORD-2026-11-03.json"
SHORTLIST_PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE_PATH = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_SHA = "46178f8017b0c2c5ad511cb833565009d0c79e76"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
TARGETS = {k: 200 for k in ("A1", "A2", "B1", "B2", "C1")}
# Frozen source index, publisher-index CEFR label, and interpretation scope.
EXPECTED = {
    "world": (7, "A1", "LOWER_LEVEL_SAME_SENSE_A1_LEAD", "world"),
    "life": (8, "A1", "DIFFERENT_SENSE_A1_NO_EXACT_MATCH", "life"),
    "public": (185, "B1", "HIGHER_LEVEL_SAME_SENSE_B1_LEAD", "public_2"),
    "data": (363, "B2", "HIGHER_LEVEL_SAME_SENSE_B2_LEAD", "data"),
    "police": (432, "A2", "ALIGNED_A2_LEAD", "police_1"),
    "university": (427, "A1", "LOWER_LEVEL_SAME_SENSE_A1_LEAD", "university"),
}
FROZEN = ("english_definition", "burmese_meaning", "example_sentence",
          "source_path", "source_index", "source_blob_sha")
ORIGINAL = ("word", "level", "part_of_speech", "english_definition",
            "burmese_meaning", "example_sentence")
FALSE = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")


def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(packet, shortlist, source):
    problems = []
    def require(ok, message):
        if not ok:
            problems.append(message)

    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_NOT_5000", "scope")
    require(packet.get("release_status") == "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH", "release status")
    require(packet.get("observed_on") == "2026-11-03", "observation date")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "shortlist provenance")
    require(packet.get("counts_by_level") == TARGETS, "packet quotas")
    require(packet.get("independently_approved_by_level") == dict.fromkeys(TARGETS, 0), "packet zero approval")
    require("403" in packet.get("source_access_limitations", ""), "Cambridge access limitation")
    require(shortlist.get("counts_by_level") == TARGETS, "frozen quotas")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(TARGETS, 0), "frozen zero approval")
    require(shortlist.get("release_status") == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH", "frozen release hold")
    rows = shortlist.get("entries", [])
    require(len(rows) == 1000, "exact 1000")
    require(collections.Counter(x.get("level") for x in rows) == collections.Counter(TARGETS), "per-level 200")
    require(len({x.get("word", "").casefold() for x in rows}) == 1000, "global headword uniqueness")
    require(all(x.get("editorial_hold") is True and all(x.get(k) is False for k in FALSE) for x in rows), "frozen independent holds")
    by_word = {x.get("word"): x for x in rows}
    cards = packet.get("entries", [])
    require(isinstance(cards, list) and len(cards) == 6, "six research cards")
    require({x.get("word") for x in cards} == set(EXPECTED), "six named words")
    original = source.get("entries", [])
    for card in cards:
        word = card.get("word")
        if word not in EXPECTED or word not in by_word:
            continue
        index, cefr, scope, oxford_slug = EXPECTED[word]
        frozen = by_word[word]
        frozen_copy = card.get("frozen", {})
        observed = card.get("source", {})
        require(card.get("level") == "A2" and card.get("part_of_speech") == frozen.get("part_of_speech"), word + " POS/level")
        require(all(frozen_copy.get(k) == frozen.get(k) for k in FROZEN), word + " frozen bilingual/provenance")
        require(frozen_copy.get("source_index") == index, word + " source index")
        require(frozen_copy.get("source_path") == "draft/A2-C1-EDITORIAL-STARTER.json", word + " historical path")
        require(frozen_copy.get("source_blob_sha") == SOURCE_SHA, word + " historical blob")
        require(index < len(original) and all(original[index].get(k) == frozen.get(k) for k in ORIGINAL), word + " historical source record")
        require(observed.get("oxford_url") == "https://www.oxfordlearnersdictionaries.com/definition/english/" + oxford_slug, word + " Oxford headword path")
        require(observed.get("cambridge_url") == "https://dictionary.cambridge.org/dictionary/english/" + word, word + " Cambridge headword path")
        require(observed.get("oxford_access") == "DIRECT_PUBLISHER_PAGE", word + " Oxford access")
        require(observed.get("cambridge_access") == "PUBLISHER_SEARCH_INDEX_ONLY_DIRECT_403", word + " Cambridge index limitation")
        require(observed.get("cambridge_level") == cefr and observed.get("cefr_scope") == scope, word + " exact-sense classification")
        require(observed.get("observed_on") == "2026-11-03", word + " source observation date")
        require(isinstance(observed.get("oxford_lines"), str) and "-" in observed["oxford_lines"], word + " Oxford line locator")
        require(isinstance(card.get("editorial_risk"), str) and len(card["editorial_risk"]) > 70, word + " editorial risk")
        alternative = card.get("proposed_alternative", {})
        require(all(isinstance(alternative.get(k), str) and len(alternative[k]) > 10 for k in ("english_definition", "burmese_meaning", "example_sentence")), word + " teaching alternative")
        require(any("\u1000" <= c <= "\u109f" for c in alternative.get("burmese_meaning", "")), word + " Myanmar script")
        require(word in alternative.get("example_sentence", "").casefold(), word + " example sense anchor")
        require(card.get("proposed_alternative_unapproved") is True and card.get("editorial_hold") is True, word + " editorial hold")
        require(all(card.get(k) is False for k in FALSE), word + " fabricated approval")
    return problems


def self_test(packet, shortlist, source):
    count = 0
    for i in range(6):
        for path, forged in (
            (("word",), "invented"), (("level",), "C1"),
            (("part_of_speech",), "adverb"), (("frozen", "english_definition"), "WRONG"),
            (("frozen", "burmese_meaning"), "WRONG"), (("frozen", "example_sentence"), "WRONG"),
            (("frozen", "source_index"), 0), (("frozen", "source_blob_sha"), "WRONG"),
            (("source", "cambridge_level"), "C1"), (("source", "cefr_scope"), "INDEPENDENTLY_APPROVED"),
            (("source", "cambridge_access"), "DIRECT_PUBLISHER_PAGE"),
            (("source", "cambridge_url"), "https://dictionary.cambridge.org/dictionary/english/banana"),
            (("source", "oxford_url"), "https://www.oxfordlearnersdictionaries.com/definition/english/banana"),
            (("source", "observed_on"), "2099-01-01"),
            (("editorial_hold",), False), (("proposed_alternative_unapproved",), False),
            (("reviewed_english",), True), (("reviewed_burmese",), True),
            (("reviewed_example",), True), (("reviewed_level",), True),
            (("reviewed_pronunciation",), True), (("release_approved",), True),
        ):
            changed = copy.deepcopy(packet)
            node = changed["entries"][i]
            for k in path[:-1]:
                node = node[k]
            node[path[-1]] = forged
            if not validate(changed, shortlist, source):
                raise AssertionError("forgery accepted: %s %s" % (i, path))
            count += 1
    for key, value in (("scope", "SUPERSEDED_5000"),
                       ("release_status", "READY"),
                       ("observed_on", "2099-01-01"),
                       ("independently_approved_by_level", dict.fromkeys(TARGETS, 200)),
                       ("counts_by_level", dict.fromkeys(TARGETS, 100))):
        changed = copy.deepcopy(packet)
        changed[key] = value
        if not validate(changed, shortlist, source):
            raise AssertionError("forged global metadata accepted: " + key)
        count += 1
    print("PASS: %d/%d synthetic source, bilingual, CEFR, reviewer and release forgeries rejected; NOT independent review" % (count, count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*TARGETS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    assert blob_sha(PACKET_PATH) == PACKET_SHA, "research packet changed"
    assert blob_sha(SHORTLIST_PATH) == SHORTLIST_SHA, "frozen shortlist changed"
    assert blob_sha(SOURCE_PATH) == SOURCE_SHA, "historical source changed"
    packet, shortlist, source = read(PACKET_PATH), read(SHORTLIST_PATH), read(SOURCE_PATH)
    problems = validate(packet, shortlist, source)
    if problems:
        raise SystemExit("FAIL: " + "; ".join(problems[:25]))
    print("PASS: six held A2 source-bound Oxford/Cambridge-index sense cards; five quotas 200; independent approval 0; lane=" + args.level)
    if args.self_test:
        self_test(packet, shortlist, source)


if __name__ == "__main__":
    main()
