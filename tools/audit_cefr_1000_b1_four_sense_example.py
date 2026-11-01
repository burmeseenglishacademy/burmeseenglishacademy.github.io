#!/usr/bin/env python3
"""Fail-closed structural audit for four held B1 exact-sense research cards.

Research-only: publisher search-index labels are NOT independent CEFR signoff.
Never converts provisional entries into release approvals.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B1-FOUR-DIRECT-OXFORD-SENSE-EXAMPLE-TRIAGE-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "50a0bf7e10b0698b6d61adea503173a4bfae1ab1"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
COUNTS = {level: 200 for level in LEVELS}
ZEROS = {level: 0 for level in LEVELS}
WORDS = ("direct", "notice", "operation", "civil")
EXPECTED = {
    "direct": ("DEFINITION_EXAMPLE_EXACT_SENSE_MISMATCH", "direct_2", "133-159", ("C1", "B1")),
    "notice": ("PUBLISHER_INDEXED_A2_VS_FROZEN_B1", "notice_2", "105-137", ("A2", "B1")),
    "operation": ("BUSINESS_SENSE_AND_GRAMMATICAL_NUMBER_AMBIGUITY", "operation", "215-275", ("C1", "C1")),
    "civil": ("CIVIL_RIGHTS_COLLOCATION_VS_NONMILITARY_GLOSS", "civil", "105-125", ()),
}
SOURCE_LIMITATIONS = ("Oxford Advanced Learner's Dictionary pages were directly opened for sense and grammar. "
    "Cambridge exact-sense labels were observed in public indexed publisher results; direct Cambridge requests returned HTTP 403. "
    "Oxford topic CEFR tags are not word/sense CEFR evidence. Neither research nor suggested Myanmar/examples "
    "constitutes independent human approval.")
ORIGINAL_FIELDS = (
    "word", "level", "part_of_speech", "english_definition", "burmese_meaning",
    "example_sentence", "source_path", "source_index", "source_blob_sha",
    "editorial_hold", "reviewed_english", "reviewed_burmese", "reviewed_example",
    "reviewed_level", "reviewed_pronunciation", "release_approved", "status",
)
FALSE_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
               "reviewed_level", "reviewed_pronunciation", "release_approved")


def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def validate(packet, shortlist):
    errors = []
    def need(condition, label):
        if not condition:
            errors.append(label)
    need(packet.get("schema") == 1, "packet schema")
    need(packet.get("branch") == "cefr-5000-bilingual-qa-staging", "staging branch")
    need(packet.get("scope") == "USER_APPROVED_1000_TOTAL_NOT_5000", "scope")
    need(packet.get("release_status") == "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH", "release hold")
    need(packet.get("created_on") == "2026-11-02", "observation date")
    need(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "shortlist provenance")
    need(packet.get("shortlist_path") == "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json", "shortlist path")
    need(packet.get("source_limitations") == SOURCE_LIMITATIONS, "source access disclosure")
    need(packet.get("counts_by_level") == COUNTS, "written quotas")
    need(packet.get("independently_approved_by_level") == ZEROS, "independent approval quota")
    need(packet.get("research_record_count") == 4, "record count")
    need(shortlist.get("counts_by_level") == COUNTS, "frozen counts")
    need(shortlist.get("independently_approved_by_level") == ZEROS, "frozen approvals")
    entries = shortlist.get("entries", [])
    need(isinstance(entries, list) and len(entries) == 1000, "exactly 1000 frozen entries")
    if not isinstance(entries, list):
        entries = []
    heads = [str(x.get("word", "")).casefold() for x in entries if isinstance(x, dict)]
    need(len(heads) == len(set(heads)) == 1000, "deduplicated frozen headwords")
    for level in LEVELS:
        need(sum(x.get("level") == level for x in entries if isinstance(x, dict)) == 200, "frozen level " + level)
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("invalid frozen entry")
            continue
        need(entry.get("editorial_hold") is True, "frozen editorial hold")
        for flag in FALSE_FLAGS:
            need(entry.get(flag) is False, "frozen " + flag)
    rows = packet.get("records", [])
    need(isinstance(rows, list) and len(rows) == 4, "four research rows")
    if not isinstance(rows, list):
        return errors
    need([x.get("word") for x in rows if isinstance(x, dict)] == list(WORDS), "record identities and order")
    for row in rows:
        if not isinstance(row, dict):
            errors.append("invalid row")
            continue
        word = row.get("word", "")
        if word not in EXPECTED:
            errors.append("unexpected word " + str(word))
            continue
        risk, slug, lines, cefr = EXPECTED[word]
        original = next((x for x in entries if x.get("word") == word and x.get("level") == "B1"), None)
        need(original is not None, word + " missing frozen original")
        if original:
            snapshot = {k: original[k] for k in ORIGINAL_FIELDS if k in original}
            need(row.get("frozen_original") == snapshot, word + " frozen bilingual/provenance snapshot")
        need(row.get("level") == "B1" and row.get("part_of_speech") == (original or {}).get("part_of_speech"), word + " POS")
        need(row.get("observed_on") == "2026-11-02", word + " observed date")
        need(row.get("risk_category") == risk, word + " risk")
        need(len(str(row.get("evidence_note", "")).strip()) >= 80, word + " explanatory evidence")
        ox = row.get("oxford_direct") or {}
        need(ox.get("url") == "https://www.oxfordlearnersdictionaries.com/definition/english/" + slug, word + " Oxford URL")
        need(ox.get("lines") == lines, word + " Oxford source line locator")
        need(ox.get("access") == "DIRECT_PAGE_OPENED", word + " direct Oxford observation")
        need(ox.get("purpose") == "SENSE_AND_GRAMMAR_NOT_INDEPENDENT_CEFR", word + " Oxford limitation")
        need(len(str(ox.get("scope", "")).strip()) >= 30, word + " exact sense")
        cam = row.get("cambridge_indexed")
        if word == "civil":
            need(cam is None, "civil cannot gain invented publisher CEFR label")
        else:
            need(isinstance(cam, dict), word + " indexed publisher")
            cam = cam or {}
            need(cam.get("url") == "https://dictionary.cambridge.org/dictionary/english/" + word, word + " Cambridge URL")
            need(cam.get("access") == "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403", word + " Cambridge access")
            labels = cam.get("observed_labels") or []
            need([x.get("level") for x in labels] == list(cefr), word + " indexed exact-sense levels")
            need(len(labels) == len(cefr) and all(len(str(x.get("sense", ""))) >= 15 for x in labels), word + " indexed senses")
        need(row.get("editorial_hold") is True, word + " hold")
        need(row.get("independently_approved") is False, word + " independent approval")
        need(row.get("proposed_alternative_unapproved") is True, word + " alternative hold")
        for flag in FALSE_FLAGS:
            need(row.get(flag) is False, word + " " + flag)
        for field in ("proposed_english_definition", "proposed_myanmar_meaning", "proposed_original_example"):
            need(len(str(row.get(field, "")).strip()) >= 20, word + " " + field)
        need(row.get("proposed_original_example") != (original or {}).get("example_sentence"), word + " distinct original example")
    return errors


def self_test(packet, shortlist):
    mutations = []
    for i, row in enumerate(packet["records"]):
        for field, value in (
            ("word", "forged"), ("level", "C1"), ("observed_on", "2025-01-01"),
            ("risk_category", ""), ("evidence_note", ""),
            ("editorial_hold", False), ("independently_approved", True),
            ("reviewed_burmese", True), ("reviewed_level", True),
            ("release_approved", True), ("proposed_alternative_unapproved", False),
            ("proposed_myanmar_meaning", ""), ("proposed_original_example", ""),
        ):
            def mutate(d, i=i, field=field, value=value):
                d["records"][i][field] = value
            mutations.append((row["word"] + "/" + field, mutate))
        for field, value in (
            ("english_definition", "forged"), ("burmese_meaning", "forged"),
            ("example_sentence", "forged"), ("source_index", -1),
            ("source_blob_sha", "0000"), ("reviewed_english", True),
        ):
            def mutate(d, i=i, field=field, value=value):
                d["records"][i]["frozen_original"][field] = value
            mutations.append((row["word"] + "/original/" + field, mutate))
        for field, value in (
            ("url", "https://example.org/forged"), ("access", "INDEPENDENT_VERIFIED"),
            ("lines", "0-0"), ("purpose", "INDEPENDENT_CEFR"),
        ):
            def mutate(d, i=i, field=field, value=value):
                d["records"][i]["oxford_direct"][field] = value
            mutations.append((row["word"] + "/oxford/" + field, mutate))
        if row["cambridge_indexed"] is not None:
            for field, value in (("access", "DIRECT_VERIFIED"), ("url", "https://example.org")):
                def mutate(d, i=i, field=field, value=value):
                    d["records"][i]["cambridge_indexed"][field] = value
                mutations.append((row["word"] + "/cambridge/" + field, mutate))
            def fake_level(d, i=i):
                d["records"][i]["cambridge_indexed"]["observed_labels"][0]["level"] = "A1"
            mutations.append((row["word"] + "/forged_level", fake_level))
        else:
            def invent_level(d, i=i):
                d["records"][i]["cambridge_indexed"] = {"access": "DIRECT_VERIFIED", "observed_labels": [{"level": "B1"}]}
            mutations.append((row["word"] + "/invented_cefr", invent_level))
    for field, value in (
        ("scope", "5000"), ("release_status", "APPROVED"), ("source_limitations", ""),
        ("shortlist_blob_sha", "0000"), ("research_record_count", 5),
        ("branch", "main"), ("created_on", "2026-11-01"),
    ):
        def mutate(d, field=field, value=value):
            d[field] = value
        mutations.append(("packet/" + field, mutate))
    for label, mutate in mutations:
        sample = copy.deepcopy(packet)
        mutate(sample)
        if not validate(sample, shortlist):
            raise AssertionError("adversarial mutation accepted: " + label)
    print(f"PASS: {len(mutations)}/{len(mutations)} synthetic source, bilingual, provenance and forged-approval mutations rejected")
    return len(mutations)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if git_blob_sha(PACKET) != PACKET_SHA:
        raise SystemExit("FAIL: source research packet Git blob SHA differs from pinned baseline")
    if git_blob_sha(SHORTLIST) != SHORTLIST_SHA:
        raise SystemExit("FAIL: frozen shortlist Git blob SHA changed")
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    errors = validate(packet, shortlist)
    if errors:
        raise SystemExit("FAIL: " + "; ".join(sorted(set(errors))[:30]))
    selected = [x for x in packet["records"] if args.level in ("ALL", x["level"])]
    print(f"PASS: {args.level}: {len(selected)} held source-bound B1 cards; 0 independently approved; no audio or human signoff claimed")
    if args.self_test:
        self_test(packet, shortlist)


if __name__ == "__main__":
    main()
