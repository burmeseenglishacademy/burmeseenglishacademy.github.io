#!/usr/bin/env python3
"""Staging-only source-bound lexical-slot/sense research auditor.

Publisher pages and bilingual alternatives are research leads, NOT independent
human approvals. A morphological resemblance does not prove duplicate lexemes.
This script never modifies shortlist, release evidence, audio or production.
"""
import argparse
import collections
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-SIX-DERIVED-NOUNS-CROSSLEVEL-LEXICAL-SLOTS-2026-11-03.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_SHA = "6afcd5d3544b0c21e5334090dd6235d0415df0ca"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
TARGETS = {k: 200 for k in ("A1", "A2", "B1", "B2", "C1")}
FIELDS = ("english_definition", "burmese_meaning", "example_sentence",
          "source_path", "source_index", "source_blob_sha")
ORIGINAL = ("word", "level", "part_of_speech", "english_definition",
            "burmese_meaning", "example_sentence")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
# (level, historical index, related word, related level, related POS,
#  morphological relation, Cambridge indexed CEFR, evidence interpretation,
#  Oxford URL slug)
EXPECTED = {
    "training": ("A2", 603, "train", "A1", "noun",
                 "DERIVED_NOUN_DISTINCT_FROM_TRAIN_TRANSPORT_NOUN", "B1",
                 "HIGHER_SAME_SENSE_CONFLICT", "training"),
    "building": ("A2", 672, "build", "A2", "verb",
                 "LEXICALISED_COUNT_NOUN_VS_VERB_ING_FORM", "A2",
                 "ALIGNED_SAME_SENSE_LEAD", "building"),
    "reporting": ("B2", 143, "report", "A2", "noun",
                  "LEXICALISED_UNCOUNTABLE_NEWS_NOUN_VS_REPORT_NOUN", None,
                  "UNLABELLED_NOT_CEFR_PROOF", "reporting"),
    "engineer": ("B2", 397, "engine", "B1", "noun",
                 "DERIVED_PROFESSION_NOUN_NOT_INFLECTION_OF_ENGINE", None,
                 "UNLABELLED_NOT_CEFR_PROOF", "engineer_1"),
    "speaker": ("B2", 852, "speak", "A1", "verb",
                "DERIVED_AGENT_NOUN_NOT_INFLECTION_OF_SPEAK", "B1",
                "LOWER_SAME_SENSE_CONFLICT", "speaker"),
    "news": ("A2", 511, "new", "A1", "adjective",
             "LEXICALISED_UNCOUNTABLE_NOUN_NOT_PRODUCTIVE_PLURAL", "A2",
             "ALIGNED_SAME_SENSE_LEAD", "news"),
}


def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(packet, shortlist, historical):
    issues = []
    def require(condition, reason):
        if not condition:
            issues.append(reason)
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_NOT_5000", "scope")
    require(packet.get("release_status") == "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH", "release hold")
    require(packet.get("observed_on") == "2026-11-03", "observation date")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "frozen source SHA")
    require(packet.get("counts_by_level") == TARGETS, "packet quotas")
    require(packet.get("independently_approved_by_level") == dict.fromkeys(TARGETS, 0), "packet zero approval")
    require("403" in packet.get("method", ""), "Cambridge direct-access limitation")
    require(shortlist.get("release_status") == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH", "shortlist release hold")
    require(shortlist.get("counts_by_level") == TARGETS, "shortlist quotas")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(TARGETS, 0), "shortlist zero approval")
    rows = shortlist.get("entries", [])
    require(isinstance(rows, list) and len(rows) == 1000, "exactly 1000")
    require(collections.Counter(x.get("level") for x in rows) == collections.Counter(TARGETS), "five 200-entry levels")
    require(len({x.get("word", "").casefold() for x in rows}) == 1000, "global headword uniqueness")
    require(all(x.get("editorial_hold") is True and all(x.get(k) is False for k in FLAGS)
                for x in rows), "no false shortlist approvals")
    lookup = {x.get("word"): x for x in rows}
    cards = packet.get("entries", [])
    require(isinstance(cards, list) and len(cards) == 6, "six cards")
    require({x.get("word") for x in cards} == set(EXPECTED), "six exact headwords")
    original = historical.get("entries", [])
    for card in cards:
        word = card.get("word")
        if word not in EXPECTED or word not in lookup:
            continue
        level, index, base, base_level, base_pos, relation, cefr, scope, slug = EXPECTED[word]
        row, paired = lookup[word], lookup.get(base, {})
        frozen, morph, source = card.get("frozen", {}), card.get("morphology", {}), card.get("source", {})
        require(card.get("level") == level and card.get("part_of_speech") == "noun", word + " level/POS")
        require(all(frozen.get(k) == row.get(k) for k in FIELDS), word + " frozen text and provenance")
        require(frozen.get("source_path") == "draft/A2-C1-EDITORIAL-STARTER.json"
                and frozen.get("source_index") == index and frozen.get("source_blob_sha") == SOURCE_SHA,
                word + " historical source locator")
        require(index < len(original) and all(original[index].get(k) == row.get(k) for k in ORIGINAL),
                word + " historical source content")
        require(morph.get("related_word") == base and morph.get("related_level") == base_level
                and morph.get("related_pos") == base_pos and morph.get("classification") == relation
                and morph.get("not_automatically_duplicate") is True,
                word + " morphological distinction")
        require(paired.get("level") == base_level and paired.get("part_of_speech") == base_pos,
                word + " paired shortlist source")
        require(source.get("oxford_url") ==
                "https://www.oxfordlearnersdictionaries.com/definition/english/" + slug,
                word + " Oxford exact headword URL")
        require(source.get("cambridge_url") ==
                "https://dictionary.cambridge.org/dictionary/english/" + word,
                word + " Cambridge exact headword URL")
        require(source.get("oxford_access") == "DIRECT_PUBLISHER_PAGE"
                and source.get("cambridge_access") == "PUBLISHER_SEARCH_INDEX_ONLY_DIRECT_403",
                word + " publisher access honesty")
        require(source.get("cambridge_level") == cefr and source.get("cefr_scope") == scope,
                word + " indexed CEFR scope")
        require(source.get("oxford_topic_labels_are_not_headword_cefr") is True,
                word + " Oxford topic is not headword CEFR")
        require(source.get("observed_on") == "2026-11-03"
                and re.fullmatch(r"[0-9]+-[0-9]+", str(source.get("oxford_lines", ""))),
                word + " dated source line locator")
        require(isinstance(card.get("editorial_risk"), str) and len(card["editorial_risk"]) > 90,
                word + " substantive editorial risk")
        proposal = card.get("proposed_alternative", {})
        require(all(isinstance(proposal.get(k), str) and len(proposal[k]) > 12
                    for k in ("english_definition", "burmese_meaning", "example_sentence")),
                word + " original bilingual proposal")
        require(any("\u1000" <= c <= "\u109f" for c in proposal.get("burmese_meaning", "")),
                word + " fluent Myanmar draft present")
        require(word in re.findall(r"[a-z]+(?:[-'][a-z]+)*",
                                   proposal.get("example_sentence", "").casefold()),
                word + " example word/sense anchor")
        require(card.get("proposed_alternative_unapproved") is True
                and card.get("editorial_hold") is True
                and all(card.get(k) is False for k in FLAGS),
                word + " independent reviewer/audio/release hold")
    return issues


def self_test(packet, shortlist, historical):
    mutations = 0
    for index in range(6):
        for path, bad in (
            (("word",), "fake"), (("level",), "C1"),
            (("part_of_speech",), "verb"),
            (("frozen", "english_definition"), "FAKE"),
            (("frozen", "burmese_meaning"), "FAKE"),
            (("frozen", "example_sentence"), "FAKE"),
            (("frozen", "source_index"), -1),
            (("frozen", "source_blob_sha"), "FAKE"),
            (("morphology", "related_word"), "fake"),
            (("morphology", "classification"), "SAME_LEMMA_APPROVED"),
            (("morphology", "not_automatically_duplicate"), False),
            (("source", "cambridge_level"), "C2"),
            (("source", "cefr_scope"), "INDEPENDENT_CEFR_APPROVED"),
            (("source", "oxford_access"), "PUBLISHER_SEARCH_INDEX_ONLY"),
            (("source", "cambridge_access"), "DIRECT_PUBLISHER_PAGE"),
            (("source", "oxford_topic_labels_are_not_headword_cefr"), False),
            (("source", "oxford_url"), "https://www.oxfordlearnersdictionaries.com/definition/english/banana"),
            (("source", "cambridge_url"), "https://dictionary.cambridge.org/dictionary/english/banana"),
            (("source", "observed_on"), "2099-01-01"),
            (("editorial_hold",), False),
            (("proposed_alternative_unapproved",), False),
            (("reviewed_english",), True), (("reviewed_burmese",), True),
            (("reviewed_example",), True), (("reviewed_level",), True),
            (("reviewed_pronunciation",), True), (("release_approved",), True),
        ):
            changed = copy.deepcopy(packet)
            node = changed["entries"][index]
            for key in path[:-1]:
                node = node[key]
            node[path[-1]] = bad
            if not validate(changed, shortlist, historical):
                raise AssertionError("FAIL OPEN: %s %s" % (index, path))
            mutations += 1
    for field, bad in (
        ("scope", "SUPERSEDED_5000"), ("release_status", "READY"),
        ("observed_on", "2099-01-01"),
        ("counts_by_level", dict.fromkeys(TARGETS, 100)),
        ("independently_approved_by_level", dict.fromkeys(TARGETS, 200)),
        ("shortlist_blob_sha", "fake"),
    ):
        changed = copy.deepcopy(packet)
        changed[field] = bad
        if not validate(changed, shortlist, historical):
            raise AssertionError("FAIL OPEN global " + field)
        mutations += 1
    print("PASS: %d/%d synthetic provenance, lexical-sense, CEFR, Myanmar, reviewer and release forgeries rejected; no independent review" % (mutations, mutations))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*TARGETS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    for path, sha in ((PACKET, PACKET_SHA), (SHORTLIST, SHORTLIST_SHA), (SOURCE, SOURCE_SHA)):
        if git_blob_sha(path) != sha:
            raise SystemExit("BLOCK: frozen Git blob SHA changed: " + str(path))
    packet, shortlist, historical = read(PACKET), read(SHORTLIST), read(SOURCE)
    problems = validate(packet, shortlist, historical)
    if problems:
        for issue in problems[:30]:
            print("BLOCK:", issue)
        raise SystemExit("FAIL: %d source/sense/review integrity defects" % len(problems))
    if args.self_test:
        self_test(packet, shortlist, historical)
    print("PASS: %s six source-bound derived-noun research cards; A1/A2/B1/B2/C1 200 each, 0 independently approved; staging only" % args.level)


if __name__ == "__main__":
    main()
