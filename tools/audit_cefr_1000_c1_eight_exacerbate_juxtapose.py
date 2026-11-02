#!/usr/bin/env python3
"""Staging-only Oxford sense evidence audit; NEVER independent CEFR or listening approval."""
import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
UPSTREAM = ROOT / "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json"
PACKET = ROOT / "draft/CEFR-1000-C1-EIGHT-DIRECT-OXFORD-EXACERBATE-JUXTAPOSE-SENSE-2026-11-02.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
UPSTREAM_SHA = "7eaf88b9ed7687b26ccde713262f10fb209743a8"
PACKET_SHA = "42c917ecb01d27ea510f0507c7c714bb723262a1"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "exacerbate": ("exacerbate", "111-114", "verb", "/ɪɡˈzæsəbeɪt/"),
    "exonerate": ("exonerate", "111-114", "verb", "/ɪɡˈzɒnəreɪt/"),
    "fallacy": ("fallacy", "105-116", "noun", "/ˈfæləsi/"),
    "fervent": ("fervent", "101-107", "adjective", "/ˈfɜːvənt/"),
    "galvanize": ("galvanize_1", "101-122", "verb", "/ˈɡælvənaɪz/"),
    "incongruous": ("incongruous", "95-106", "adjective", "/ɪnˈkɒŋɡruəs/"),
    "introspection": ("introspection", "95-107", "noun", "/ˌɪntrəˈspekʃn/"),
    "juxtapose": ("juxtapose", "101-112", "verb", "/ˌdʒʌkstəˈpəʊz/"),
}
FALSE_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
               "reviewed_level", "reviewed_pronunciation", "release_approved")
REVIEW_FLAGS = ("english", "myanmar", "example", "cefr", "pronunciation",
                "audio_listened", "iphone_tested", "release_approved")


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def read_pinned(path, expected_sha):
    raw = path.read_bytes()
    assert blob_sha(raw) == expected_sha, f"Changed frozen source: {path}"
    return json.loads(raw)


def validate(packet, shortlist, upstream):
    assert packet["scope"] == "USER_APPROVED_CEFR_1000_STAGING_ONLY"
    assert packet["release_status"] == "RESEARCH_ONLY_ALL_EIGHT_HELD"
    assert packet["branch"] == "cefr-5000-bilingual-qa-staging"
    assert packet["observed_on"] == "2026-11-02"
    assert packet["shortlist_blob_sha"] == SHORT_SHA
    assert packet["upstream_source_blob_sha"] == UPSTREAM_SHA
    assert packet["target_counts"] == dict.fromkeys(LEVELS, 200)
    assert packet["independently_approved_counts"] == dict.fromkeys(LEVELS, 0)
    assert "not independent" in packet["review_policy"].lower()
    entries = shortlist["entries"]
    assert len(entries) == 1000
    assert Counter(e["level"] for e in entries) == Counter(dict.fromkeys(LEVELS, 200))
    assert len({e["word"].casefold() for e in entries}) == 1000
    assert all(e["editorial_hold"] is True and
               all(e[k] is False for k in FALSE_FLAGS) for e in entries)
    byword = {e["word"]: e for e in entries}
    assert len(packet["records"]) == 8
    assert [r["word"] for r in packet["records"]] == list(EXPECTED)
    assert all(r["level"] == "C1" for r in packet["records"])
    for record in packet["records"]:
        word = record["word"]
        suffix, lines, pos, ipa = EXPECTED[word]
        frozen = byword[word]
        assert record["part_of_speech"] == pos == frozen["part_of_speech"]
        assert record["frozen_first_pass"] == {
            "english_definition": frozen["english_definition"],
            "burmese_meaning": frozen["burmese_meaning"],
            "example_sentence": frozen["example_sentence"],
        }, word
        provenance = record["historical_provenance"]
        assert provenance == {k: frozen[k] for k in
            ("source_path", "source_index", "source_blob_sha")} | {
            "shortlist_blob_sha": SHORT_SHA}, word
        assert provenance["source_blob_sha"] == UPSTREAM_SHA
        original = upstream["entries"][provenance["source_index"]]
        assert original["word"] == word
        assert all(original[k] == frozen[k] for k in
                   ("english_definition", "burmese_meaning", "example_sentence"))
        source = record["source_observation"]
        assert source["publisher"] == "Oxford University Press"
        assert source["source_url"] == (
            "https://www.oxfordlearnersdictionaries.com/definition/english/" + suffix)
        assert source["observed_on"] == "2026-11-02"
        assert source["access"] == "DIRECT_PUBLISHER_ENTRY_OPENED"
        assert source["observed_line_range"] == lines
        assert source["uk_ipa"] == ipa
        assert source["part_of_speech"] == pos
        assert source["exact_sense_cefr_badge_observed"] is None
        assert "no C1 exact-sense CEFR classification" in source["source_limitations"]
        assert len(source["exact_sense_summary_paraphrase"]) >= 35
        assert len(source["caution"]) >= 20
        assert len(record["editorial_risk"]) >= 35
        proposal = record["unapproved_teaching_alternative"]
        assert proposal["approval_status"] == "UNAPPROVED_EDITORIAL_PROPOSAL"
        assert all(isinstance(proposal[k], str) and len(proposal[k].strip()) > 25
                   for k in ("english_definition", "burmese_meaning",
                             "original_example_sentence"))
        assert record["independent_review"] == dict.fromkeys(REVIEW_FLAGS, False)
    return True


def adversarial_tests(packet, shortlist, upstream):
    count = 0
    for i, record in enumerate(packet["records"]):
        cases = [
            ("frozen_first_pass", "english_definition", "forged definition"),
            ("frozen_first_pass", "burmese_meaning", "forged Myanmar"),
            ("frozen_first_pass", "example_sentence", "forged example"),
            ("historical_provenance", "source_path", "draft/fake.json"),
            ("historical_provenance", "source_index", 0),
            ("historical_provenance", "source_blob_sha", "0" * 40),
            ("source_observation", "source_url", "https://www.oxfordlearnersdictionaries.com/blog/" + record["word"]),
            ("source_observation", "access", "SEARCH_INDEX_ONLY"),
            ("source_observation", "exact_sense_cefr_badge_observed", "C1"),
            ("source_observation", "observed_line_range", "999-1000"),
            ("source_observation", "uk_ipa", "/fake/"),
            ("source_observation", "observed_on", "2025-01-01"),
            ("source_observation", "source_limitations", "independently approved C1"),
            ("unapproved_teaching_alternative", "approval_status", "APPROVED"),
            ("unapproved_teaching_alternative", "burmese_meaning", ""),
            ("independent_review", "english", True),
            ("independent_review", "cefr", True),
            ("independent_review", "audio_listened", True),
            ("independent_review", "iphone_tested", True),
            ("independent_review", "release_approved", True),
        ]
        for section, field, replacement in cases:
            bad = copy.deepcopy(packet)
            bad["records"][i][section][field] = replacement
            try:
                validate(bad, shortlist, upstream)
            except (AssertionError, KeyError, IndexError, TypeError):
                count += 1
            else:
                raise AssertionError(f"Accepted forged {record['word']} {section}.{field}")
        for field, replacement in (("word", "exonerate" if i != 1 else "exacerbate"),
                                   ("level", "B2"), ("part_of_speech", "noun" if record["part_of_speech"] != "noun" else "verb")):
            bad = copy.deepcopy(packet)
            bad["records"][i][field] = replacement
            try:
                validate(bad, shortlist, upstream)
            except (AssertionError, KeyError, IndexError, TypeError):
                count += 1
            else:
                raise AssertionError(f"Accepted forged {record['word']} {field}")
    assert count == 8 * 23
    print(f"PASS: {count}/{count} synthetic forgeries rejected (NOT independent human review)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    shortlist = read_pinned(SHORT, SHORT_SHA)
    upstream = read_pinned(UPSTREAM, UPSTREAM_SHA)
    packet = read_pinned(PACKET, PACKET_SHA)
    validate(packet, shortlist, upstream)
    print(f"PASS {args.level}: eight held Oxford C1 exact-sense observations; "
          "200 written / 0 independently approved per level; no release")
    if args.self_test:
        adversarial_tests(packet, shortlist, upstream)


if __name__ == "__main__":
    main()
