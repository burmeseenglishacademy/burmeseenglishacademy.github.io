#!/usr/bin/env python3
"""Fail-closed staging-only audit of eight B1 exact-sense research leads.

Oxford pages were directly inspected for dictionary senses. Cambridge CEFR
labels were indexed publisher-page leads with direct HTTP 403, NOT human review.
Neither this audit nor its adversarial tests approves any CEFR card or audio.
"""
import argparse
import copy
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET_PATH = ROOT / "draft/CEFR-1000-B1-EIGHT-CAMBRIDGE-INDEXED-EXACT-SENSE-TRIAGE-2026-11-02.json"
SHORTLIST_PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "8e71b2acc0ae4c347053ce8039b916e675c1d9eb"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("analysis", "impact", "independent", "primary", "ship", "cash", "fan", "male")
PUBLISHER_LEVELS = ("B2", "B2", "B2", "B2", "A2", "A2", "B1", "B1")
OXFORD_URLS = (
    "https://www.oxfordlearnersdictionaries.com/definition/english/analysis",
    "https://www.oxfordlearnersdictionaries.com/definition/english/impact_1",
    "https://www.oxfordlearnersdictionaries.com/definition/english/independent_1",
    "https://www.oxfordlearnersdictionaries.com/definition/english/primary_1",
    "https://www.oxfordlearnersdictionaries.com/definition/english/ship_1",
    "https://www.oxfordlearnersdictionaries.com/definition/english/cash_1",
    "https://www.oxfordlearnersdictionaries.com/definition/english/fan_1",
    "https://www.oxfordlearnersdictionaries.com/definition/english/male_1",
)
OXFORD_LINES = ("119-138", "103-120", "174-188", "115-123",
                "105-129", "103-116", "171-178", "105-138")
CAMBRIDGE_URLS = (
    "https://dictionary.cambridge.org/dictionary/english/analysis",
    "https://dictionary.cambridge.org/dictionary/english/impact",
    "https://dictionary.cambridge.org/dictionary/learner-english/independent",
    "https://dictionary.cambridge.org/dictionary/learner-english/primary",
    "https://dictionary.cambridge.org/dictionary/english/ship",
    "https://dictionary.cambridge.org/dictionary/learner-english/cash",
    "https://dictionary.cambridge.org/dictionary/english/fan",
    "https://dictionary.cambridge.org/dictionary/learner-english/male",
)
FROZEN_FIELDS = ("word", "level", "part_of_speech", "english_definition",
                 "burmese_meaning", "example_sentence", "source_path",
                 "source_index", "source_blob_sha", "editorial_hold",
                 "reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation", "release_approved")
FALSE_FLAGS = ("independently_approved", "reviewed_english", "reviewed_burmese",
               "reviewed_example", "reviewed_level", "reviewed_pronunciation",
               "release_approved")

def blob_sha(path):
    return subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                          check=True, capture_output=True, text=True).stdout.strip()

def validate(packet, shortlist, baseline=None):
    errors = []
    if not isinstance(packet, dict) or not isinstance(shortlist, dict):
        return ["root JSON must contain objects"]
    expected_counts = dict.fromkeys(LEVELS, 200)
    expected_zero = dict.fromkeys(LEVELS, 0)
    for key, expected in (
        ("schema", 1), ("created_on", "2026-11-02"),
        ("branch", "cefr-5000-bilingual-qa-staging"),
        ("scope", "USER_APPROVED_1000_TOTAL_NOT_5000"),
        ("release_status", "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"),
        ("shortlist_blob_sha", SHORTLIST_SHA),
        ("counts_by_level", expected_counts),
        ("independently_approved_by_level", expected_zero),
        ("research_record_count", 8), ("cross_level_conflict_count", 6),
        ("indexed_alignment_control_count", 2),
    ):
        if packet.get(key) != expected:
            errors.append("packet metadata " + key)
    limitations = str(packet.get("source_limitations", ""))
    if not all(x in limitations for x in ("HTTP 403", "not independent human review",
                                         "not word/sense CEFR approvals")):
        errors.append("publisher access and review limitations missing")
    frozen = shortlist.get("entries")
    if not isinstance(frozen, list) or len(frozen) != 1000:
        return errors + ["shortlist must have 1000 entries"]
    if shortlist.get("counts_by_level") != expected_counts:
        errors.append("frozen shortlist level quotas changed")
    if shortlist.get("independently_approved_by_level") != expected_zero:
        errors.append("frozen shortlist approval counts changed")
    if any(not isinstance(e, dict) or e.get("editorial_hold") is not True or
           any(e.get(k) is not False for k in FALSE_FLAGS[1:]) for e in frozen):
        errors.append("frozen shortlist unheld or forged approval")
    if len(set(str(e.get("word", "")).casefold() for e in frozen if isinstance(e, dict))) != 1000:
        errors.append("shortlist duplicate headwords")
    by_word = {e.get("word"): e for e in frozen if isinstance(e, dict)}
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != 8:
        return errors + ["eight source-bound records required"]
    for i, word in enumerate(WORDS):
        row = rows[i]
        if not isinstance(row, dict):
            errors.append(word + " row must be object")
            continue
        original = by_word.get(word)
        if original is None or original.get("level") != "B1":
            errors.append(word + " not in frozen B1")
            continue
        if row.get("word") != word or row.get("level") != "B1" or row.get("part_of_speech") != original.get("part_of_speech"):
            errors.append(word + " headword/POS mismatch")
        if row.get("frozen_original") != {k: original.get(k) for k in FROZEN_FIELDS}:
            errors.append(word + " frozen bilingual/example/provenance changed")
        ox = row.get("oxford_direct")
        ca = row.get("cambridge_indexed")
        if not isinstance(ox, dict) or ox != {
            "url": OXFORD_URLS[i], "lines": OXFORD_LINES[i],
            "access": "DIRECT_PAGE_OPENED",
            "scope": "DICTIONARY_SENSE_AND_GRAMMAR_NOT_INDEPENDENT_CEFR"
        }:
            errors.append(word + " Oxford source receipt mismatch")
        if not isinstance(ca, dict) or ca.get("url") != CAMBRIDGE_URLS[i] or ca.get("level") != PUBLISHER_LEVELS[i] or ca.get("access") != "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403":
            errors.append(word + " Cambridge indexed source receipt mismatch")
        if not isinstance(ca, dict) or not isinstance(ca.get("sense_paraphrase"), str) or not ca["sense_paraphrase"].strip():
            errors.append(word + " indexed exact-sense paraphrase missing")
        expected_disposition = ("CROSS_LEVEL_EXACT_SENSE_HUMAN_ADJUDICATION_REQUIRED"
                                if i < 6 else "INDEXED_SENSE_ALIGNMENT_CONTROL_NOT_APPROVAL")
        if row.get("disposition") != expected_disposition:
            errors.append(word + " review disposition changed")
        if row.get("observed_on") != "2026-11-02":
            errors.append(word + " observation date missing")
        if row.get("editorial_hold") is not True or row.get("proposed_alternative_unapproved") is not True:
            errors.append(word + " editorial hold missing")
        if any(row.get(k) is not False for k in FALSE_FLAGS):
            errors.append(word + " forged review or release approval")
        for field in ("evidence_note", "proposed_myanmar_meaning",
                      "proposed_original_example", "sense_review_risk"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(word + " missing " + field)
        if not re.search(r"[\u1000-\u109f]", str(row.get("proposed_myanmar_meaning", ""))):
            errors.append(word + " Myanmar characters missing")
        if not re.search(r"\b" + re.escape(word) + r"\b", str(row.get("proposed_original_example", "")).casefold()):
            errors.append(word + " headword absent from proposed example")
        if baseline is not None and row != baseline["records"][i]:
            errors.append(word + " pinned evidence snapshot changed")
    if baseline is not None and packet != baseline:
        errors.append("pinned research packet mutated")
    return errors

def self_test(packet, shortlist):
    cases = (
        ("word", "fake"), ("level", "C1"), ("part_of_speech", "verb"),
        ("observed_on", "2099-01-01"), ("disposition", "APPROVED"),
        ("evidence_note", ""), ("proposed_myanmar_meaning", "English only"),
        ("proposed_original_example", "Nothing relevant here."),
        ("sense_review_risk", ""), ("editorial_hold", False),
        ("proposed_alternative_unapproved", False),
        ("independently_approved", True), ("reviewed_english", True),
        ("reviewed_burmese", True), ("reviewed_example", True),
        ("reviewed_level", True), ("reviewed_pronunciation", True),
        ("release_approved", True),
    )
    n = 0
    for i, word in enumerate(WORDS):
        for field, value in cases:
            trial = copy.deepcopy(packet)
            trial["records"][i][field] = value
            if not validate(trial, shortlist, packet):
                raise AssertionError("forged " + word + "/" + field + " escaped")
            n += 1
        for group, field, value in (
            ("oxford_direct", "url", "https://example.invalid/fake"),
            ("oxford_direct", "lines", "999-999"),
            ("oxford_direct", "access", "INDEPENDENTLY_APPROVED"),
            ("cambridge_indexed", "url", "https://example.invalid/fake"),
            ("cambridge_indexed", "level", "A1"),
            ("cambridge_indexed", "access", "DIRECT_VERIFIED"),
            ("cambridge_indexed", "sense_paraphrase", ""),
            ("frozen_original", "source_blob_sha", "0" * 40),
        ):
            trial = copy.deepcopy(packet)
            trial["records"][i][group][field] = value
            if not validate(trial, shortlist, packet):
                raise AssertionError("forged " + word + "/" + group + "." + field + " escaped")
            n += 1
    for field, value in (
        ("scope", "SUPERSEDED_5000"), ("release_status", "READY_TO_PUBLISH"),
        ("shortlist_blob_sha", "0" * 40), ("cross_level_conflict_count", 0),
        ("independently_approved_by_level", dict.fromkeys(LEVELS, 200)),
        ("source_limitations", "all sources independently verified"),
    ):
        trial = copy.deepcopy(packet)
        trial[field] = value
        if not validate(trial, shortlist, packet):
            raise AssertionError("forged packet metadata escaped: " + field)
        n += 1
    print("PASS: rejected %d/%d synthetic source, bilingual, provenance and approval mutations" % (n, n))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if blob_sha(PACKET_PATH) != PACKET_SHA or blob_sha(SHORTLIST_PATH) != SHORTLIST_SHA:
        raise SystemExit("BLOCK: pinned Git blob SHA changed; independent research reconciliation required")
    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST_PATH.read_text(encoding="utf-8"))
    problems = validate(packet, shortlist)
    if problems:
        raise SystemExit("BLOCK: " + "; ".join(problems[:25]))
    if args.self_test:
        self_test(packet, shortlist)
    selected = [x["word"] for x in packet["records"]
                if args.level == "ALL" or x["level"] == args.level]
    print("PASS research integrity only: level=%s held=%d words=%s independent_approvals=0" %
          (args.level, len(selected), ",".join(selected)))
    print("RELEASE BLOCKED: indexed CEFR leads are not independent English/Myanmar/example/sense approvals")

if __name__ == "__main__":
    main()
