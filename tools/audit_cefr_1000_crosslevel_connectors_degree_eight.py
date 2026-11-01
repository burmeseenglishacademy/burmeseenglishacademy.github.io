#!/usr/bin/env python3
"""Fail-closed audit of eight *unapproved* Cambridge-indexed sense triage records.

The packet is editorial research, not a human-independent review ledger.
Source indexing is not proof of publisher page access or a final CEFR decision.
"""
import argparse
import copy
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CROSSLEVEL-CONNECTORS-AND-DEGREE-EIGHT-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "60c46bed558aa3d9f345817e546c4f9dad0b3e01"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("apparently", "critical", "rather", "fine", "otherwise",
         "however", "therefore", "quite")
PUBLISHER_LEVELS = ("B2", "B2", "B1", "B1", "B1", "A2", "B1", None)
EXPECTED_LEVELS = ("B1", "B1", "A2", "A2", "B1", "A2", "B1", "A2")
EXPECTED_POS = ("adverb", "adjective", "adverb", "adjective",
                "conjunction", "adverb", "adverb", "adverb")
SOURCE_URLS = (
    "https://dictionary.cambridge.org/dictionary/english/apparently",
    "https://dictionary.cambridge.org/dictionary/english/critical",
    "https://dictionary.cambridge.org/dictionary/english/rather",
    "https://dictionary.cambridge.org/dictionary/english/fine",
    "https://dictionary.cambridge.org/dictionary/english/otherwise",
    "https://dictionary.cambridge.org/us/dictionary/learner-english/however",
    "https://dictionary.cambridge.org/dictionary/english/therefore",
    "https://dictionary.cambridge.org/grammar/british-grammar/quite",
)
ORIGINAL_FIELDS = ("word", "level", "part_of_speech", "english_definition",
                   "burmese_meaning", "example_sentence", "source_path",
                   "source_index", "source_blob_sha")
FALSE_FLAGS = ("independently_approved", "reviewed_english",
               "reviewed_burmese", "reviewed_example", "reviewed_level",
               "release_approved")
EXPECTED_SOURCE_TYPE = "PUBLIC_SEARCH_INDEXED_PUBLISHER_PAGE_NOT_INDEPENDENTLY_REVIEWED"
EXPECTED_SOURCE_LIMITATIONS = "Publisher pages accessed via public search indexing; some direct requests returned HTTP 403. Treat publisher labels as indexed evidence leads, never as independent exact-sense human signoff. Cambridge grammar page for quite supplies no CEFR rating."

def git_blob(path):
    return subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                          check=True, capture_output=True, text=True).stdout.strip()

def validate(packet, shortlist, baseline=None):
    errors = []
    if not isinstance(packet, dict) or not isinstance(shortlist, dict):
        return ["packet/shortlist root must be objects"]
    for key, value in (
        ("schema", 1), ("created_on", "2026-11-02"),
        ("scope", "USER_APPROVED_1000_TOTAL_NOT_5000"),
        ("branch", "cefr-5000-bilingual-qa-staging"),
        ("shortlist_blob_sha", SHORTLIST_SHA),
        ("release_status", "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"),
        ("counts_by_level", dict.fromkeys(LEVELS, 200)),
        ("independently_approved_by_level", dict.fromkeys(LEVELS, 0)),
    ):
        if packet.get(key) != value: errors.append("packet " + key)
    if packet.get("source_limitations") != EXPECTED_SOURCE_LIMITATIONS:
        errors.append("missing source-access limitation")
    frozen = shortlist.get("entries")
    rows = packet.get("records")
    if not isinstance(frozen, list) or len(frozen) != 1000:
        return errors + ["shortlist cardinality"]
    if shortlist.get("counts_by_level") != dict.fromkeys(LEVELS, 200):
        errors.append("shortlist levels")
    if shortlist.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        errors.append("shortlist independent approvals")
    if any(not isinstance(x, dict) or x.get("release_approved") or
           any(x.get(k) for k in ("reviewed_english", "reviewed_burmese",
                                  "reviewed_example", "reviewed_level"))
           for x in frozen):
        errors.append("shortlist false approval")
    if not isinstance(rows, list) or len(rows) != len(WORDS):
        return errors + ["packet cardinality"]
    by_word = {x["word"]: x for x in frozen}
    for idx, (word, row) in enumerate(zip(WORDS, rows)):
        if not isinstance(row, dict):
            errors.append(word + " non-object"); continue
        original = by_word.get(word)
        if original is None:
            errors.append(word + " not in frozen shortlist"); continue
        if row.get("word") != word or row.get("level") != EXPECTED_LEVELS[idx]:
            errors.append(word + " identity/level")
        for field in ORIGINAL_FIELDS:
            if row.get(field) != original.get(field):
                errors.append(word + " frozen " + field)
        if row.get("publisher_level") != PUBLISHER_LEVELS[idx]:
            errors.append(word + " publisher label")
        if row.get("publisher_pos") != EXPECTED_POS[idx]:
            errors.append(word + " publisher POS")
        if row.get("url") != SOURCE_URLS[idx]:
            errors.append(word + " source URL")
        if row.get("observed_on") != "2026-11-02":
            errors.append(word + " observation date")
        if row.get("publisher_evidence_type") != EXPECTED_SOURCE_TYPE:
            errors.append(word + " evidence access misrepresented")
        if row.get("editorial_hold") is not True or row.get("proposed_alternative_unapproved") is not True:
            errors.append(word + " editorial hold")
        if any(row.get(k) is not False for k in FALSE_FLAGS):
            errors.append(word + " false review or approval")
        for field in ("sense", "source_heading", "risk", "proposed_burmese",
                      "proposed_example", "priority"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(word + " missing " + field)
        if not re.search("[\u1000-\u109f]", str(row.get("proposed_burmese", ""))):
            errors.append(word + " Myanmar absent")
        if not re.search(r"\b" + re.escape(word) + r"\b",
                         str(row.get("proposed_example", "")).lower()):
            errors.append(word + " example lemma absent")
        if baseline is not None and row != baseline["records"][idx]:
            errors.append(word + " research baseline changed")
    if baseline is not None and packet != baseline:
        errors.append("frozen research packet changed")
    return errors

def self_test(packet, shortlist):
    tested = 0
    mutations = (
        ("level", "C1"), ("publisher_level", "C1"),
        ("publisher_pos", "noun"), ("url", "https://example.org/dictionary"),
        ("observed_on", "2026-11-03"),
        ("publisher_evidence_type", "DIRECT_PUBLISHER_PAGE_OPENED"),
        ("source_blob_sha", "0" * 40),
        ("burmese_meaning", "အမှား"),
        ("english_definition", "False."),
        ("example_sentence", "Wrong."),
        ("proposed_burmese", "not Myanmar"),
        ("proposed_example", "No matching token."),
        ("editorial_hold", False), ("independently_approved", True),
        ("reviewed_english", True), ("reviewed_burmese", True),
        ("reviewed_example", True), ("reviewed_level", True),
        ("release_approved", True), ("proposed_alternative_unapproved", False),
    )
    for i in range(len(WORDS)):
        for key, value in mutations:
            bad = copy.deepcopy(packet)
            bad["records"][i][key] = value
            if not validate(bad, shortlist, packet):
                raise AssertionError("mutation escaped: %s %s" % (WORDS[i], key))
            tested += 1
    for key, value in (
        ("scope", "CEFR_5000"), ("shortlist_blob_sha", "0" * 40),
        ("release_status", "APPROVED"),
        ("source_limitations", "Direct publisher page opened and independently approved."),
        ("source_limitations", ""),
        ("independently_approved_by_level", dict.fromkeys(LEVELS, 200)),
    ):
        bad = copy.deepcopy(packet); bad[key] = value
        if not validate(bad, shortlist, packet):
            raise AssertionError("root mutation escaped: " + key)
        tested += 1
    return tested

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if git_blob(PACKET) != PACKET_SHA or git_blob(SHORTLIST) != SHORTLIST_SHA:
        raise SystemExit("FAIL: research or frozen shortlist blob differs from pinned baseline")
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    errors = validate(packet, shortlist)
    if errors:
        raise SystemExit("FAIL: " + "; ".join(errors[:30]))
    subset = [x for x in packet["records"] if args.level == "ALL" or x["level"] == args.level]
    expected = {"A1":0, "A2":4, "B1":4, "B2":0, "C1":0, "ALL":8}[args.level]
    if len(subset) != expected:
        raise SystemExit("FAIL: level-specific record count")
    print("PASS: %s indexed publisher research records, 0 independent approvals, %s lane" %
          (len(subset), args.level))
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: %d/%d synthetic forged-evidence mutations rejected" % (n, n))

if __name__ == "__main__":
    main()
