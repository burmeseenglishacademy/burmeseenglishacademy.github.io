#!/usr/bin/env python3
"""Staging-only Cambridge-indexed B1 sense-conflict packet integrity auditor.

This validates frozen-source fidelity and rejects invented approvals. Publisher
search-index snippets are NOT directly opened pages or independent human review.
No production write, approval, listening or deployment operation occurs here.
"""
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-B1-EIGHT-FOUNDATIONAL-CAMBRIDGE-INDEXED-SENSE-TRIAGE-2026-11-02.json"
FROZEN_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "independent": ("B2", "adjective NOT INFLUENCED", "LEVEL_CONFLICT", "https://dictionary.cambridge.org/dictionary/english/independent"),
    "weekend": ("A1", "noun Saturday and Sunday", "LEVEL_CONFLICT", "https://dictionary.cambridge.org/dictionary/english/weekend"),
    "cash": ("A2", "learner-English noun COINS", "LEVEL_CONFLICT", "https://dictionary.cambridge.org/dictionary/learner-english/cash"),
    "effort": ("B1", "noun physical or mental energy", "INDEX_ALIGNMENT_LEAD", "https://dictionary.cambridge.org/dictionary/english/effort"),
    "civil": ("C1", "adjective ORDINARY", "LEVEL_AND_EXAMPLE_SENSE_CONFLICT", "https://dictionary.cambridge.org/dictionary/english/civil"),
    "ship": ("A2", "noun BOAT", "LEVEL_CONFLICT", "https://dictionary.cambridge.org/dictionary/english/ship"),
    "operation": ("C1", "noun WORK", "LEVEL_AND_COUNTABILITY_CONFLICT", "https://dictionary.cambridge.org/dictionary/english/operation"),
    "analysis": ("B2", "noun detailed examination", "LEVEL_CONFLICT", "https://dictionary.cambridge.org/dictionary/english/analysis"),
}
FALSE_FLAGS = ("independently_reviewed", "release_approved", "headword_george_listened",
               "headword_emma_listened", "example_george_listened",
               "example_emma_listened", "physical_iphone_safari_tested")


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def load():
    raw = SHORTLIST.read_bytes()
    if git_blob_sha(raw) != FROZEN_SHA:
        raise ValueError("Frozen shortlist blob changed")
    return json.loads(PACKET.read_text(encoding="utf-8")), json.loads(raw)


def validate(packet, shortlist, level="ALL"):
    errors = []
    def require(condition, reason):
        if not condition:
            errors.append(reason)

    require(level in (*LEVELS, "ALL"), "unknown CEFR level")
    require(packet.get("schema") == 1, "packet schema")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    require(packet.get("created_on") == "2026-11-02", "observation date")
    require(packet.get("status") == "INDEXED_CAMBRIDGE_EXACT_SENSE_TRIAGE_HUMAN_REVIEW_REQUIRED", "research status")
    require(packet.get("frozen_shortlist_blob_sha") == FROZEN_SHA, "shortlist hash")
    limitations = packet.get("source_access_limitations")
    require(isinstance(limitations, str) and all(t in limitations for t in
            ("search-index", "HTTP 403", "not direct", "not independent")), "publisher access caveat")
    require(packet.get("count") == 8 and packet.get("level") == "B1", "eight B1 cards")
    require(packet.get("conflict_count") == 7 and packet.get("alignment_count") == 1, "conflict totals")
    require(packet.get("production_deployed") is False, "no production claim")
    for k in ("headword_audio_listening_signoffs", "example_audio_listening_signoffs",
              "physical_iphone_safari_signoffs"):
        require(type(packet.get(k)) is int and packet[k] == 0, "no fabricated signoff " + k)
    expected_counts = {k: 200 for k in LEVELS}
    require(packet.get("first_pass_written_by_level") == expected_counts, "first-pass counts")
    require(packet.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "approval counts")
    source = shortlist.get("entries", [])
    require(len(source) == 1000, "exactly 1000 source records")
    require(shortlist.get("counts_by_level") == expected_counts, "source level totals")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "source approval totals")
    require(Counter(e.get("level") for e in source) == Counter(expected_counts), "200 entries per level")
    require(len({e.get("word", "").casefold() for e in source}) == 1000, "global unique headwords")
    for e in source:
        require(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english", "reviewed_burmese", "reviewed_example",
                         "reviewed_level", "reviewed_pronunciation")), "source held " + str(e.get("word")))
    index = {e["word"]: e for e in source}
    rows = packet.get("records")
    if not isinstance(rows, list):
        return errors + ["records must be a list"]
    require(len(rows) == 8, "eight records required")
    seen = set()
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"record {i} not object")
            continue
        word = row.get("word")
        require(word in EXPECTED, f"record {i} unknown headword")
        require(word not in seen, f"record {i} duplicate headword")
        seen.add(word)
        if word not in EXPECTED or word not in index:
            continue
        frozen = index[word]
        cefr, heading, status, url = EXPECTED[word]
        require(row.get("level") == "B1" == frozen["level"], word + " frozen level")
        require(row.get("part_of_speech") == frozen["part_of_speech"], word + " frozen POS")
        snap = row.get("shortlist_snapshot")
        require(isinstance(snap, dict), word + " frozen snapshot object")
        if isinstance(snap, dict):
            for k, source_key in (("english_definition", "english_definition"),
                                  ("burmese_meaning", "burmese_meaning"),
                                  ("example_sentence", "example_sentence")):
                require(snap.get(k) == frozen[source_key], word + " frozen " + k)
        provenance = row.get("shortlist_provenance")
        require(isinstance(provenance, dict), word + " provenance object")
        if isinstance(provenance, dict):
            for k in ("source_path", "source_index", "source_blob_sha"):
                require(provenance.get(k) == frozen[k], word + " source " + k)
        observed = row.get("publisher_observation")
        require(isinstance(observed, dict), word + " publisher object")
        if isinstance(observed, dict):
            expected = {
                "publisher": "Cambridge Dictionary", "source_url": url,
                "observed_on": "2026-11-02",
                "access": "SEARCH_INDEX_VISIBLE_DIRECT_OPEN_403",
                "evidence_scope": "PUBLISHER_INDEXED_EXACT_SENSE_CEFR_LEAD_NOT_DIRECT_OR_INDEPENDENT",
                "sense_heading": heading, "indexed_cefr": cefr,
            }
            for k, value in expected.items():
                require(observed.get(k) == value, word + " publisher " + k)
        require(row.get("triage_status") == status, word + " conflict type")
        note = row.get("editorial_note")
        require(isinstance(note, str) and len(note.strip()) >= 70, word + " meaningful triage note")
        alt = row.get("unapproved_teaching_alternative")
        require(isinstance(alt, dict), word + " unapproved alternative")
        if isinstance(alt, dict):
            for k in ("english_definition", "burmese_meaning", "example_sentence"):
                require(isinstance(alt.get(k), str) and len(alt[k].strip()) >= 12,
                        word + " alternative " + k)
            require(word in str(alt.get("example_sentence", "")).casefold(),
                    word + " alternative example headword")
        task = row.get("independent_reviewer_task")
        require(isinstance(task, str) and all(x in task for x in
                ("Independently", "George", "Emma", "HEADWORD", "EXAMPLE")),
                word + " actual reviewer task")
        require(row.get("editorial_hold") is True, word + " editorial hold")
        require(all(row.get(k) is False for k in FALSE_FLAGS), word + " no false approval/listening")
        require(row.get("independent_reviewer_receipt") is None, word + " no reviewer receipt")
    require(seen == set(EXPECTED), "all eight headwords represented")
    if level != "ALL":
        require(level in LEVELS, "known level")
        require(sum(1 for row in rows if row.get("level") == level) == (8 if level == "B1" else 0),
                "level-specific subset")
    return errors


def self_test(packet, shortlist):
    baseline = validate(packet, shortlist)
    if baseline:
        raise AssertionError("baseline: " + "; ".join(baseline[:10]))
    total = 0
    for i, row in enumerate(packet["records"]):
        mutations = [
            (("word",), "fake-headword"), (("level",), "C1"),
            (("part_of_speech",), "fake-POS"),
            (("shortlist_snapshot", "english_definition"), "forged"),
            (("shortlist_snapshot", "burmese_meaning"), "အတု"),
            (("shortlist_snapshot", "example_sentence"), "fake example"),
            (("shortlist_provenance", "source_path"), "fake.json"),
            (("shortlist_provenance", "source_index"), -1),
            (("shortlist_provenance", "source_blob_sha"), "0" * 40),
            (("publisher_observation", "source_url"), "https://example.org/not-publisher"),
            (("publisher_observation", "observed_on"), "2099-01-01"),
            (("publisher_observation", "access"), "DIRECT_PUBLISHER_PAGE"),
            (("publisher_observation", "evidence_scope"), "INDEPENDENT_APPROVAL"),
            (("publisher_observation", "sense_heading"), "different sense"),
            (("publisher_observation", "indexed_cefr"), "C2"),
            (("triage_status",), "APPROVED"),
            (("editorial_note",), "No conflict"),
            (("unapproved_teaching_alternative", "example_sentence"), "No word here."),
            (("independent_reviewer_task",), "Reviewed"),
            (("editorial_hold",), False), (("independently_reviewed",), True),
            (("release_approved",), True), (("headword_george_listened",), True),
            (("headword_emma_listened",), True), (("example_george_listened",), True),
            (("example_emma_listened",), True),
            (("physical_iphone_safari_tested",), True),
            (("independent_reviewer_receipt",), {"reviewer": "fake"}),
        ]
        for path, replacement in mutations:
            bad = copy.deepcopy(packet)
            obj = bad["records"][i]
            for key in path[:-1]:
                obj = obj[key]
            obj[path[-1]] = replacement
            if not validate(bad, shortlist):
                raise AssertionError(f"forgery accepted: {row['word']} {path}")
            total += 1
    for k, replacement in (
        ("status", "APPROVED"), ("frozen_shortlist_blob_sha", "0" * 40),
        ("source_access_limitations", "Publisher directly verified"),
        ("conflict_count", 0), ("count", 7),
        ("independently_approved_by_level", {"B1": 8}),
        ("headword_audio_listening_signoffs", 8),
        ("example_audio_listening_signoffs", 8),
        ("physical_iphone_safari_signoffs", 1),
        ("production_deployed", True),
    ):
        bad = copy.deepcopy(packet)
        bad[k] = replacement
        if not validate(bad, shortlist):
            raise AssertionError("forged top-level claim accepted: " + k)
        total += 1
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist = load()
    errors = validate(packet, shortlist, args.level)
    if errors:
        print("FAIL: " + "; ".join(errors[:30]))
        return 1
    print(f"PASS: eight held B1 research cards, 7 publisher-indexed conflicts, 1 alignment; "
          f"level={args.level}; 1000 held; 0 independent approvals; no audio/iPhone/deployment evidence")
    if args.self_test:
        total = self_test(packet, shortlist)
        print(f"PASS: {total}/{total} synthetic adversarial mutations rejected (mock only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
