#!/usr/bin/env python3
"""Fail-closed integrity audit for SIX UNAPPROVED replacement research candidates.

Oxford's CEFR word/POS list and dictionary senses are source leads, NOT
independent exact-sense, Myanmar, example or pronunciation approvals.
This script does not change the frozen shortlist or production.
"""
import argparse
import copy
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET_PATH = ROOT / "draft/CEFR-1000-SIX-INFLECTION-SLOT-REPLACEMENT-CANDIDATES-2026-11-02.json"
SHORTLIST_PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "e2a3545e05f5f61c1c2f3c1bb734d8a73d33cc72"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
PAIRS = (("is", "afraid", "A1", "adjective", 17),
         ("are", "angry", "A1", "adjective", 31),
         ("does", "answer", "A1", "noun", 34),
         ("did", "airport", "A1", "noun", 25),
         ("better", "ability", "A2", "noun", 920),
         ("worst", "achievement", "B1", "noun", 1803))
PDF_URL = ("https://www.oxfordlearnersdictionaries.com/external/pdf/"
           "wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
DICT_URLS = {
    "afraid": "https://www.oxfordlearnersdictionaries.com/definition/english/afraid",
    "angry": "https://www.oxfordlearnersdictionaries.com/definition/english/angry",
    "answer": "https://www.oxfordlearnersdictionaries.com/definition/english/answer_1",
    "airport": "https://www.oxfordlearnersdictionaries.com/definition/english/airport",
    "ability": "https://www.oxfordlearnersdictionaries.com/definition/english/ability_1",
    "achievement": "https://www.oxfordlearnersdictionaries.com/definition/english/achievement",
}
FROZEN_FIELDS = ("word", "level", "part_of_speech", "english_definition",
                 "burmese_meaning", "example_sentence", "source_path",
                 "source_index", "source_blob_sha", "editorial_hold",
                 "reviewed_english", "reviewed_burmese", "reviewed_example",
                 "reviewed_level", "reviewed_pronunciation", "release_approved")
FALSE_FLAGS = ("independently_approved", "reviewed_english", "reviewed_burmese",
               "reviewed_example", "reviewed_level", "reviewed_pronunciation",
               "release_approved")
EVIDENCE_SCOPE = ("DIRECT_OXFORD_WORD_POS_CEFR_LIST_PLUS_DIRECT_DICTIONARY_"
                  "SENSE_NOT_INDEPENDENT_SIGNOFF")

def git_blob(path):
    return subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                          capture_output=True, check=True, text=True).stdout.strip()

def validate(packet, shortlist, baseline=None):
    errors = []
    if not isinstance(packet, dict) or not isinstance(shortlist, dict):
        return ["packet/shortlist root must be JSON objects"]
    expected_counts = dict.fromkeys(LEVELS, 200)
    expected_zero = dict.fromkeys(LEVELS, 0)
    for field, value in (
        ("schema", 1), ("created_on", "2026-11-02"),
        ("branch", "cefr-5000-bilingual-qa-staging"),
        ("scope", "USER_APPROVED_1000_TOTAL_NOT_5000"),
        ("release_status", "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"),
        ("shortlist_blob_sha", SHORTLIST_SHA),
        ("counts_by_level", expected_counts),
        ("independently_approved_by_level", expected_zero),
        ("held_nonindependent_form_count", 6), ("candidate_count", 6),
    ):
        if packet.get(field) != value:
            errors.append("packet " + field)
    if "not independently" not in str(packet.get("source_limitations", "")).lower():
        errors.append("source limitations do not preserve independent-review warning")
    frozen = shortlist.get("entries")
    if not isinstance(frozen, list) or len(frozen) != 1000:
        return errors + ["frozen shortlist must contain 1000 records"]
    if shortlist.get("counts_by_level") != expected_counts:
        errors.append("frozen per-level quotas changed")
    if shortlist.get("independently_approved_by_level") != expected_zero:
        errors.append("frozen approvals changed")
    if any(not isinstance(x, dict) or x.get("editorial_hold") is not True or
           any(x.get(flag) is not False for flag in
               ("reviewed_english", "reviewed_burmese", "reviewed_example",
                "reviewed_level", "reviewed_pronunciation", "release_approved"))
           for x in frozen):
        errors.append("frozen shortlist has forged approval or unheld record")
    words = [x.get("word", "").casefold() for x in frozen if isinstance(x, dict)]
    if len(set(words)) != 1000:
        errors.append("frozen headwords not unique")
    by_word = {x["word"]: x for x in frozen if isinstance(x, dict)}
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != 6:
        return errors + ["candidate packet cardinality"]
    for idx, (held, candidate, level, pos, pdf_line) in enumerate(PAIRS):
        row = rows[idx]
        if not isinstance(row, dict):
            errors.append("candidate row not object"); continue
        original = by_word.get(held)
        if original is None or original.get("level") != level:
            errors.append(held + " original missing or wrong level")
            continue
        if row.get("held_word") != held or row.get("candidate_word") != candidate:
            errors.append(held + " slot/candidate mismatch")
        if row.get("candidate_level") != level or row.get("candidate_pos") != pos:
            errors.append(candidate + " CEFR/POS mismatch")
        if candidate in words:
            errors.append(candidate + " already exists in frozen 1000")
        if row.get("held_original") != {k: original.get(k) for k in FROZEN_FIELDS}:
            errors.append(held + " frozen English/Myanmar/example/provenance mismatch")
        if row.get("publisher_wordlist_url") != PDF_URL or row.get("publisher_wordlist_line") != pdf_line:
            errors.append(candidate + " publisher PDF evidence mismatch")
        if row.get("publisher_dictionary_url") != DICT_URLS[candidate]:
            errors.append(candidate + " publisher dictionary URL mismatch")
        if not re.fullmatch(r"[0-9]+-[0-9]+", str(row.get("publisher_dictionary_lines", ""))):
            errors.append(candidate + " dictionary line locator absent")
        if row.get("observed_on") != "2026-11-02" or row.get("source_evidence_scope") != EVIDENCE_SCOPE:
            errors.append(candidate + " observation/evidence scope mismatch")
        if row.get("editorial_hold") is not True or row.get("proposed_alternative_unapproved") is not True:
            errors.append(candidate + " editorial hold missing")
        if any(row.get(k) is not False for k in FALSE_FLAGS):
            errors.append(candidate + " forged independent approval")
        for field in ("proposed_english_definition", "proposed_myanmar_meaning",
                      "proposed_original_example", "sense_review_risk"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                errors.append(candidate + " missing " + field)
        if not re.search(r"[\u1000-\u109f]", str(row.get("proposed_myanmar_meaning", ""))):
            errors.append(candidate + " Myanmar gloss missing")
        if not re.search(r"\b" + re.escape(candidate) + r"\b",
                         str(row.get("proposed_original_example", "")).casefold()):
            errors.append(candidate + " candidate missing from example")
        if baseline is not None and row != baseline["records"][idx]:
            errors.append(candidate + " pinned source packet altered")
    if baseline is not None and packet != baseline:
        errors.append("pinned packet differs from baseline")
    return errors

def self_test(packet, shortlist):
    cases = (
        ("held_word", "fake"), ("candidate_word", "fake"),
        ("candidate_level", "C1"), ("candidate_pos", "verb"),
        ("publisher_wordlist_url", "https://example.invalid/fake.pdf"),
        ("publisher_wordlist_line", 9999),
        ("publisher_dictionary_url", "https://example.invalid/fake"),
        ("publisher_dictionary_lines", "unknown"),
        ("observed_on", "2099-01-01"),
        ("source_evidence_scope", "INDEPENDENTLY_APPROVED"),
        ("proposed_english_definition", ""),
        ("proposed_myanmar_meaning", "not Myanmar"),
        ("proposed_original_example", "No matching word."),
        ("sense_review_risk", ""),
        ("editorial_hold", False), ("proposed_alternative_unapproved", False),
        ("independently_approved", True), ("reviewed_english", True),
        ("reviewed_burmese", True), ("reviewed_example", True),
        ("reviewed_level", True), ("reviewed_pronunciation", True),
        ("release_approved", True),
    )
    count = 0
    for i in range(6):
        for field, value in cases:
            mutated = copy.deepcopy(packet)
            mutated["records"][i][field] = value
            if not validate(mutated, shortlist, packet):
                raise AssertionError("mutation escaped: " + PAIRS[i][1] + " " + field)
            count += 1
        mutated = copy.deepcopy(packet)
        mutated["records"][i]["held_original"]["source_blob_sha"] = "0" * 40
        if not validate(mutated, shortlist, packet):
            raise AssertionError("frozen provenance mutation escaped")
        count += 1
    for field, value in (
        ("scope", "SUPERSEDED_5000"), ("release_status", "READY"),
        ("shortlist_blob_sha", "0" * 40),
        ("independently_approved_by_level", dict.fromkeys(LEVELS, 200)),
        ("source_limitations", "approved"), ("candidate_count", 5000),
    ):
        mutated = copy.deepcopy(packet)
        mutated[field] = value
        if not validate(mutated, shortlist, packet):
            raise AssertionError("root mutation escaped: " + field)
        count += 1
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if git_blob(PACKET_PATH) != PACKET_SHA or git_blob(SHORTLIST_PATH) != SHORTLIST_SHA:
        raise SystemExit("FAIL: frozen packet or shortlist Git blob mismatch")
    packet = json.loads(PACKET_PATH.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST_PATH.read_text(encoding="utf8"))
    problems = validate(packet, shortlist)
    if problems:
        raise SystemExit("FAIL: " + "; ".join(problems[:30]))
    subset = [x for x in packet["records"]
              if args.level == "ALL" or x["candidate_level"] == args.level]
    expected = {"A1": 4, "A2": 1, "B1": 1, "B2": 0, "C1": 0, "ALL": 6}
    if len(subset) != expected[args.level]:
        raise SystemExit("FAIL: level-specific candidate quota mismatch")
    print("PASS: %s Oxford-backed UNAPPROVED candidate records, %s lane; 0 independent approvals" %
          (len(subset), args.level))
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: %s/%s forged-research mutations rejected (synthetic only)" % (n, n))

if __name__ == "__main__":
    main()
