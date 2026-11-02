#!/usr/bin/env python3
"""Fail-closed documentary integrity for six B1 Cambridge-indexed sense leads.

Search-indexed publisher evidence is research only. No human CEFR, English,
Myanmar, example, George/Emma listening, physical iPhone or release approval.
"""
import argparse
import copy
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B1-SIX-FIGHTING-GROW-CAMBRIDGE-INDEXED-SENSE-2026-11-03.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "cd7ce40c5c72e3d4773a1de8e7cff86f21724ec2"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("fighting", "damage", "directly", "disease", "doubt", "grow")
INDEXES = (433, 436, 437, 438, 439, 440)
PUBLISHER_LEVELS = ("B2", "B1", "B1", "B1", "B1", "A2")
CONFLICTS = ("B1_VS_B2_EXACT_NOUN", "NONE_ALIGNMENT_LEAD",
             "NONE_ALIGNMENT_LEAD", "NONE_ALIGNMENT_LEAD",
             "NONE_ALIGNMENT_LEAD", "B1_VS_A2_EXACT_VERB")
FALSE_FLAGS = ("independent_english_approved", "independent_myanmar_approved",
               "independent_example_approved", "independent_cefr_approved",
               "release_approved")
FROZEN_FIELDS = ("word", "level", "part_of_speech", "english_definition",
                 "burmese_meaning", "example_sentence", "source_path",
                 "source_index", "source_blob_sha")


def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def validate(packet, shortlist):
    issues = []
    targets = {level: 200 for level in LEVELS}
    zero = {level: 0 for level in LEVELS}
    if not isinstance(packet, dict) or not isinstance(shortlist, dict):
        return ["root objects required"]
    for key, value in (
        ("schema", 1), ("created_on", "2026-11-03"),
        ("branch", "cefr-5000-bilingual-qa-staging"),
        ("scope", "USER_APPROVED_1000_TOTAL_NOT_5000"),
        ("release_status", "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"),
        ("shortlist_blob_sha", SHORTLIST_SHA),
        ("counts_by_level", targets), ("independently_approved_by_level", zero),
    ):
        if packet.get(key) != value:
            issues.append("packet " + key)
    if ("not independently approved" not in
            str(packet.get("source_limitations", "")).casefold()):
        issues.append("source limitation honesty")
    if shortlist.get("counts_by_level") != targets or shortlist.get(
            "independently_approved_by_level") != zero:
        issues.append("frozen quotas or approvals")
    frozen = shortlist.get("entries")
    if not isinstance(frozen, list) or len(frozen) != 1000:
        return issues + ["1000 frozen records required"]
    counts = {level: sum(e.get("level") == level for e in frozen
                         if isinstance(e, dict)) for level in LEVELS}
    if counts != targets:
        issues.append("actual per-level quotas")
    if len({e.get("word") for e in frozen if isinstance(e, dict)}) != 1000:
        issues.append("duplicate headwords")
    if any(not isinstance(e, dict) or e.get("editorial_hold") is not True
           or any(e.get(k) is not False for k in
                  ("reviewed_english", "reviewed_burmese", "reviewed_example",
                   "reviewed_level", "reviewed_pronunciation", "release_approved"))
           for e in frozen):
        issues.append("shortlist forged approval")
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 6:
        return issues + ["exactly six indexed research rows required"]
    for n, (word, index, level, conflict) in enumerate(
            zip(WORDS, INDEXES, PUBLISHER_LEVELS, CONFLICTS)):
        row = records[n]
        if not isinstance(row, dict):
            issues.append("nonobject research row")
            continue
        original = frozen[index]
        if (row.get("word") != word or row.get("level") != "B1"
                or row.get("shortlist_index") != index
                or row.get("part_of_speech") != original.get("part_of_speech")):
            issues.append(word + " identity/POS/level")
        for source, frozen_field in (
                ("frozen_english_definition", "english_definition"),
                ("frozen_burmese_meaning", "burmese_meaning"),
                ("frozen_example_sentence", "example_sentence"),
                ("source_path", "source_path"),
                ("source_index", "source_index"),
                ("source_blob_sha", "source_blob_sha")):
            if row.get(source) != original.get(frozen_field):
                issues.append(word + " frozen " + source)
        if row.get("publisher_url") != (
                "https://dictionary.cambridge.org/dictionary/english/" + word):
            issues.append(word + " publisher URL")
        if row.get("publisher_indexed_cefr") != level or row.get(
                "conflict_type") != conflict:
            issues.append(word + " CEFR conflict honesty")
        if (row.get("observed_on") != "2026-11-03"
                or row.get("evidence_access") !=
                "PUBLISHER_OWNED_SEARCH_INDEX_RESULT_NOT_INDEPENDENT_REVIEW"
                or row.get("exact_sense_observation_scope") !=
                "INDEXED_PUBLISHER_SENSE_LEAD_ONLY"):
            issues.append(word + " source access/scope/date")
        if any(row.get(flag) is not False for flag in FALSE_FLAGS):
            issues.append(word + " forged independent approval")
        if not all(isinstance(row.get(field), str) and len(row[field].strip()) > 8
                   for field in ("publisher_sense_paraphrase", "finding",
                                 "publisher_indexed_pos")):
            issues.append(word + " missing sense provenance")
        alt = row.get("unapproved_teaching_alternative")
        if not isinstance(alt, dict) or not all(
                isinstance(alt.get(k), str) and len(alt[k].strip()) > 8
                for k in ("english_definition", "burmese_meaning",
                          "original_example")):
            issues.append(word + " missing teaching draft")
        elif not any("\u1000" <= ch <= "\u109f" for ch in alt["burmese_meaning"]):
            issues.append(word + " Myanmar script missing")
    return issues


def self_test(packet, shortlist):
    n = 0
    def must_reject(p, s):
        nonlocal n
        problems = validate(p, s)
        if not problems:
            raise AssertionError("forged evidence unexpectedly accepted")
        n += 1
    for field in FALSE_FLAGS:
        for i in range(6):
            p = copy.deepcopy(packet)
            p["records"][i][field] = True
            must_reject(p, shortlist)
    for i in range(6):
        for field, value in (
                ("publisher_indexed_cefr", "C1"),
                ("publisher_url", "https://dictionary.cambridge.org/dictionary/english/banana"),
                ("observed_on", "2099-01-01"),
                ("evidence_access", "DIRECT_PUBLISHER_DICTIONARY_PAGE"),
                ("exact_sense_observation_scope", "INDEPENDENT_EXACT_SENSE"),
                ("frozen_example_sentence", "A forged sentence."),
                ("conflict_type", "NONE_ALIGNMENT_LEAD" if i in (0, 5) else "B1_VS_A2_EXACT_VERB"),
        ):
            p = copy.deepcopy(packet)
            p["records"][i][field] = value
            must_reject(p, shortlist)
    for field, value in (
            ("release_status", "APPROVED"),
            ("independently_approved_by_level", dict.fromkeys(LEVELS, 200)),
            ("source_limitations", "Independent review complete"),
    ):
        p = copy.deepcopy(packet)
        p[field] = value
        must_reject(p, shortlist)
    for field, value in (("reviewed_level", True), ("editorial_hold", False)):
        s = copy.deepcopy(shortlist)
        s["entries"][433][field] = value
        must_reject(packet, s)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if blob_sha(PACKET) != PACKET_SHA or blob_sha(SHORTLIST) != SHORTLIST_SHA:
        raise SystemExit("BLOCK: frozen packet or shortlist blob changed")
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf8"))
    issues = validate(packet, shortlist)
    if issues:
        raise SystemExit("BLOCK: " + "; ".join(issues[:25]))
    selected = 6 if args.level in ("B1", "ALL") else 0
    print("PASS: %s held B1 indexed-sense research records in %s lane; 0 independently approved" % (selected, args.level))
    if args.self_test:
        count = self_test(packet, shortlist)
        print("PASS: %s/%s synthetic research and approval forgeries rejected" % (count, count))


if __name__ == "__main__":
    main()
