#!/usr/bin/env python3
"""Staging-only, fail-closed integrity audit for six C1 Oxford/Cambridge research cards.

Publisher observations are not independent human review. Cambridge C2 index leads
cannot be silently relabelled C1; no approval, audio or deployment occurs here.
"""
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-METICULOUS-SCRUTINIZE-DIRECT-OXFORD-CAMBRIDGE-C2-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
FROZEN_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
RESEARCH_SHA = "58b6ac1822a6eb19b9127396dea7dcdc32eeccf5"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "meticulous": ("C2", "C2_CONFLICT", "88-114", "/məˈtɪkjələs/"),
    "mitigate": (None, "UNSUBSTANTIATED_C1", "88-124", "/ˈmɪtɪɡeɪt/"),
    "nuanced": (None, "UNSUBSTANTIATED_C1", "88-107", "/ˈnjuːɑːnst/"),
    "pragmatic": ("C2", "C2_CONFLICT", "88-123", "/præɡˈmætɪk/"),
    "precedent": ("C2", "C2_CONFLICT", "88-155", "/ˈpresɪdənt/"),
    "scrutinize": (None, "UNSUBSTANTIATED_C1", "88-125", "/ˈskruːtənaɪz/"),
}
FALSE_FLAGS = ("independently_reviewed", "release_approved", "headword_george_listened",
               "headword_emma_listened", "example_george_listened",
               "example_emma_listened", "physical_iphone_safari_tested")


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load():
    frozen = SHORTLIST.read_bytes()
    research = PACKET.read_bytes()
    if git_blob_sha(frozen) != FROZEN_SHA:
        raise ValueError("Frozen shortlist blob changed")
    if git_blob_sha(research) != RESEARCH_SHA:
        raise ValueError("Research packet blob changed: source/provenance re-review required")
    return json.loads(research), json.loads(frozen)


def validate(packet, shortlist, level="ALL"):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    require(level in (*LEVELS, "ALL"), "invalid level")
    require(packet.get("schema") == 1, "schema")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    require(packet.get("created_on") == "2026-11-02", "observation date")
    require(packet.get("status") == "DIRECT_OXFORD_AND_INDEXED_CAMBRIDGE_C1_SENSE_TRIAGE_HUMAN_REVIEW_REQUIRED", "research status")
    require(packet.get("frozen_shortlist_blob_sha") == FROZEN_SHA, "shortlist SHA")
    caveat = packet.get("source_access_limitations", "")
    require(isinstance(caveat, str) and all(s in caveat for s in
            ("directly opened", "search-index", "HTTP 403", "not direct", "not independent", "topic c2")),
            "publisher-access and footer caveat")
    require(packet.get("count") == 6 and packet.get("level") == "C1", "six C1 records")
    require(packet.get("indexed_c2_conflicts") == 3 and packet.get("unsubstantiated_c1") == 3,
            "three indexed C2 conflicts and three unsubstantiated C1 placements")
    require(packet.get("first_pass_written_by_level") == dict.fromkeys(LEVELS, 200), "first pass counts")
    require(packet.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "independent approvals")
    require(packet.get("production_deployed") is False, "no production claim")
    for field in ("headword_audio_listening_signoffs", "example_audio_listening_signoffs",
                  "physical_iphone_safari_signoffs"):
        require(type(packet.get(field)) is int and packet[field] == 0, "no fabricated " + field)

    source = shortlist.get("entries", [])
    require(len(source) == 1000, "exactly 1000 shortlist rows")
    require(Counter(row.get("level") for row in source) == Counter(dict.fromkeys(LEVELS, 200)),
            "exactly 200 entries per level")
    require(len({str(row.get("word", "")).casefold() for row in source}) == 1000, "global deduplication")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "source independent approvals remain zero")
    for row in source:
        require(row.get("editorial_hold") is True and row.get("release_approved") is False
                and all(row.get(f) is False for f in
                        ("reviewed_english", "reviewed_burmese", "reviewed_example",
                         "reviewed_level", "reviewed_pronunciation")),
                "shortlist entry remains held: " + str(row.get("word")))
    index = {row["word"]: row for row in source}
    rows = packet.get("records")
    if not isinstance(rows, list):
        return errors + ["records must be a list"]
    require(len(rows) == 6, "six records")
    seen = set()
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append("record not object " + str(i))
            continue
        word = row.get("word")
        require(word in EXPECTED, "unexpected headword " + str(word))
        require(word not in seen, "duplicate headword " + str(word))
        seen.add(word)
        if word not in EXPECTED or word not in index:
            continue
        frozen = index[word]
        cefr, status, lines, ipa = EXPECTED[word]
        require(row.get("level") == frozen.get("level") == "C1", word + " level")
        require(row.get("part_of_speech") == frozen.get("part_of_speech"), word + " POS")
        snap = row.get("shortlist_snapshot")
        require(isinstance(snap, dict), word + " snapshot")
        if isinstance(snap, dict):
            for field in ("english_definition", "burmese_meaning", "example_sentence"):
                require(snap.get(field) == frozen.get(field), word + " frozen " + field)
        prov = row.get("shortlist_provenance")
        require(isinstance(prov, dict), word + " provenance")
        if isinstance(prov, dict):
            for field in ("source_path", "source_index", "source_blob_sha"):
                require(prov.get(field) == frozen.get(field), word + " provenance " + field)
        ox = row.get("oxford_observation")
        require(isinstance(ox, dict), word + " Oxford object")
        if isinstance(ox, dict):
            for field, value in {
                "publisher": "Oxford Advanced Learner's Dictionary",
                "source_url": "https://www.oxfordlearnersdictionaries.com/definition/english/" + word,
                "observed_on": "2026-11-02",
                "access": "DIRECT_PUBLISHER_PAGE_OPENED",
                "source_line_range": lines, "uk_ipa": ipa,
                "exact_sense_c1_badge_observed": False,
            }.items():
                require(ox.get(field) == value, word + " Oxford " + field)
            require(isinstance(ox.get("observed_sense_paraphrase"), str)
                    and len(ox["observed_sense_paraphrase"]) > 55, word + " sense observation")
        cam = row.get("cambridge_observation")
        require(isinstance(cam, dict), word + " Cambridge object")
        if isinstance(cam, dict):
            for field, value in {
                "publisher": "Cambridge Dictionary",
                "source_url": "https://dictionary.cambridge.org/dictionary/english/" + word,
                "observed_on": "2026-11-02",
                "access": "PUBLISHER_SEARCH_INDEX_VISIBLE_DIRECT_OPEN_403",
                "evidence_scope": "INDEXED_CEFR_LEAD_NOT_DIRECT_OR_INDEPENDENT",
                "indexed_cefr": cefr,
            }.items():
                require(cam.get(field) == value, word + " Cambridge " + field)
        require(row.get("triage_status") == status, word + " triage status")
        require(isinstance(row.get("editorial_note"), str)
                and len(row["editorial_note"]) > 100, word + " editorial explanation")
        alt = row.get("unapproved_teaching_alternative")
        require(isinstance(alt, dict), word + " unapproved alternative")
        if isinstance(alt, dict):
            for field in ("english_definition", "burmese_meaning", "example_sentence"):
                require(isinstance(alt.get(field), str) and len(alt[field]) > 12,
                        word + " alternative " + field)
            require(word in str(alt.get("example_sentence", "")).casefold(),
                    word + " example headword")
        task = row.get("independent_reviewer_task")
        require(isinstance(task, str) and all(s in task for s in
                ("Independently", "George", "Emma", "HEADWORD", "EXAMPLE", "iPhone")),
                word + " independent reviewer task")
        require(row.get("editorial_hold") is True, word + " hold")
        require(all(row.get(f) is False for f in FALSE_FLAGS), word + " false approval/listening")
        require(row.get("independent_reviewer_receipt") is None, word + " reviewer receipt")
    require(seen == set(EXPECTED), "all six headwords covered")
    if level != "ALL":
        require(sum(1 for r in rows if r.get("level") == level) == (6 if level == "C1" else 0),
                "level-specific subset")
    return errors


def self_test(packet, shortlist):
    if validate(packet, shortlist):
        raise AssertionError("baseline failed: " + "; ".join(validate(packet, shortlist)[:8]))
    total = 0
    for i, row in enumerate(packet["records"]):
        mutations = [
            (("word",), "fake"), (("level",), "B2"), (("part_of_speech",), "fake"),
            (("shortlist_snapshot", "english_definition"), "forged"),
            (("shortlist_snapshot", "burmese_meaning"), "အတု"),
            (("shortlist_snapshot", "example_sentence"), "forged"),
            (("shortlist_provenance", "source_path"), "fake.json"),
            (("shortlist_provenance", "source_index"), -1),
            (("shortlist_provenance", "source_blob_sha"), "0" * 40),
            (("oxford_observation", "source_url"), "https://example.org/fake"),
            (("oxford_observation", "observed_on"), "2099-01-01"),
            (("oxford_observation", "access"), "NOT_OPENED"),
            (("oxford_observation", "source_line_range"), "0-0"),
            (("oxford_observation", "uk_ipa"), "wrong"),
            (("oxford_observation", "exact_sense_c1_badge_observed"), True),
            (("cambridge_observation", "source_url"), "https://example.org/fake"),
            (("cambridge_observation", "access"), "DIRECT_OPENED"),
            (("cambridge_observation", "evidence_scope"), "INDEPENDENT_REVIEW"),
            (("cambridge_observation", "indexed_cefr"), "A1" if row["cambridge_observation"]["indexed_cefr"] is None else "C1"),
            (("triage_status",), "APPROVED"),
            (("editorial_note",), "none"),
            (("unapproved_teaching_alternative", "example_sentence"), "No headword here."),
            (("independent_reviewer_task",), "approved"),
            (("editorial_hold",), False), (("independently_reviewed",), True),
            (("release_approved",), True), (("headword_george_listened",), True),
            (("headword_emma_listened",), True), (("example_george_listened",), True),
            (("example_emma_listened",), True),
            (("physical_iphone_safari_tested",), True),
            (("independent_reviewer_receipt",), {"reviewer": "forged"}),
        ]
        for path, replacement in mutations:
            bad = copy.deepcopy(packet)
            obj = bad["records"][i]
            for field in path[:-1]:
                obj = obj[field]
            obj[path[-1]] = replacement
            if not validate(bad, shortlist):
                raise AssertionError("forged mutation accepted: " + row["word"] + " " + str(path))
            total += 1
    for field, replacement in (
        ("status", "APPROVED"), ("count", 5), ("indexed_c2_conflicts", 0),
        ("unsubstantiated_c1", 0), ("frozen_shortlist_blob_sha", "0" * 40),
        ("source_access_limitations", "direct and independent"),
        ("independently_approved_by_level", {"C1": 6}),
        ("headword_audio_listening_signoffs", 6),
        ("example_audio_listening_signoffs", 6),
        ("physical_iphone_safari_signoffs", 1), ("production_deployed", True),
    ):
        bad = copy.deepcopy(packet)
        bad[field] = replacement
        if not validate(bad, shortlist):
            raise AssertionError("forged top-level claim accepted: " + field)
        total += 1
    return total


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    packet, shortlist = load()
    errors = validate(packet, shortlist, args.level)
    if errors:
        print("FAIL: " + "; ".join(errors[:25]))
        return 1
    print(f"PASS: six C1 held research cards; 3 Cambridge-indexed C2 conflicts, "
          f"3 unsubstantiated C1 placements; level={args.level}; "
          "0 independent approvals, no listening/iPhone/production evidence")
    if args.self_test:
        count = self_test(packet, shortlist)
        print(f"PASS: {count}/{count} synthetic adversarial mutations rejected (mock only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
