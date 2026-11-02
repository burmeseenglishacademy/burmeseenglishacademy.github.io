#!/usr/bin/env python3
"""Fail-closed, staging-only Cambridge-indexed B2 six-card evidence integrity check.

Search-index evidence is NOT a direct Cambridge page open or independent
human English, Myanmar, example, pronunciation, CEFR or listening signoff.
No manifest approval, main-branch write, or deployment occurs here.
"""
import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET = ROOT / "draft/CEFR-1000-B2-SIX-SINGER-STEAM-COMMANDER-EXACT-WISE-MONTHLY-INDEXED-2026-11-02.json"
FROZEN_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "singer": ("A2", "LEVEL_CONFLICT", "noun [C], person who sings"),
    "steam": ("B2", "INDEX_ALIGNMENT_LEAD", "noun [U], hot gas produced when water boils"),
    "commander": ("C2", "LEVEL_AND_SENSE_SCOPE_CONFLICT", "noun [C], officer in charge of a military operation or naval rank"),
    "exact": ("B1", "LEVEL_CONFLICT", "adjective ACCURATE, completely correct in every detail"),
    "wise": ("B2", "INDEX_ALIGNMENT_LEAD", "adjective, good judgment based on experience"),
    "monthly": ("B1", "LEVEL_CONFLICT", "adjective/adverb, happening or produced once a month"),
}
FALSE_FLAGS = ("independently_reviewed", "release_approved",
               "headword_george_listened", "headword_emma_listened",
               "example_george_listened", "example_emma_listened",
               "physical_iphone_safari_tested")
ROW_KEYS = {"word", "level", "part_of_speech", "shortlist_snapshot",
            "shortlist_provenance", "publisher_observation", "triage_status",
            "editorial_note", "unapproved_teaching_alternative",
            "independent_reviewer_task", "editorial_hold", *FALSE_FLAGS}
PUB_KEYS = {"publisher", "source_url", "observed_on", "access",
            "evidence_scope", "indexed_cefr", "indexed_part_of_speech_and_sense",
            "uk_ipa", "observation_paraphrase", "exact_sense_independently_verified"}

def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

def load():
    raw, original = SHORTLIST.read_bytes(), SOURCE.read_bytes()
    if blob_sha(raw) != FROZEN_SHA or blob_sha(original) != SOURCE_SHA:
        raise ValueError("Frozen shortlist or historical original source blob changed")
    return (json.loads(PACKET.read_text(encoding="utf-8")),
            json.loads(raw), json.loads(original))

def validate(packet, shortlist, original, level="ALL"):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)

    require(level in (*LEVELS, "ALL"), "invalid lane")
    require(packet.get("schema") == 1, "schema")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    require(packet.get("created_on") == "2026-11-02", "observation date")
    require(packet.get("status") == "INDEXED_CAMBRIDGE_B2_SIX_EXACT_SENSE_TRIAGE_HUMAN_REVIEW_REQUIRED", "research status")
    require(packet.get("frozen_shortlist_blob_sha") == FROZEN_SHA, "frozen hash")
    caveat = packet.get("source_access_limitations", "")
    require(isinstance(caveat, str) and all(x in caveat for x in
            ("search-index", "HTTP 403", "not direct", "not independent")), "source access honesty")
    require(packet.get("count") == 6 and packet.get("level") == "B2", "six B2 research cards")
    require(packet.get("conflict_count") == 4 and packet.get("alignment_count") == 2, "conflict totals")
    require(packet.get("production_deployed") is False, "no production claim")
    for key in ("headword_audio_listening_signoffs", "example_audio_listening_signoffs",
                "physical_iphone_safari_signoffs"):
        require(type(packet.get(key)) is int and packet[key] == 0, "false signoff " + key)
    counts = {k: 200 for k in LEVELS}
    require(packet.get("first_pass_written_by_level") == counts, "written totals")
    require(packet.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "approved totals")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000, "exactly 1000 frozen entries")
    require(Counter(e.get("level") for e in entries) == Counter(counts), "200 each level")
    require(shortlist.get("counts_by_level") == counts, "shortlist declared totals")
    require(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0), "shortlist independent totals")
    require(len({e.get("word", "").casefold() for e in entries}) == 1000, "global headword deduplication")
    for e in entries:
        require(e.get("editorial_hold") is True and e.get("release_approved") is False and
                all(e.get(k) is False for k in ("reviewed_english", "reviewed_burmese",
                    "reviewed_example", "reviewed_level", "reviewed_pronunciation")),
                "frozen held status " + str(e.get("word")))
    index = {e["word"]: e for e in entries}
    rows = packet.get("records")
    if not isinstance(rows, list):
        return errors + ["records not list"]
    require(len(rows) == 6, "six records")
    seen = set()
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"row {i} not object")
            continue
        word = row.get("word")
        require(set(row) == ROW_KEYS, f"row {i} missing/extra fields (including forged approval receipts)")
        require(word in EXPECTED, f"row {i} unknown word")
        require(word not in seen, f"row {i} duplicate")
        seen.add(word)
        if word not in EXPECTED or word not in index:
            continue
        frozen = index[word]
        cefr, status, heading = EXPECTED[word]
        require(row.get("level") == "B2" == frozen["level"], word + " frozen level")
        require(row.get("part_of_speech") == frozen["part_of_speech"], word + " POS")
        snapshot = row.get("shortlist_snapshot", {})
        require(isinstance(snapshot, dict) and snapshot ==
                {k: frozen[k] for k in ("english_definition", "burmese_meaning", "example_sentence")},
                word + " frozen English/Myanmar/example")
        provenance = row.get("shortlist_provenance", {})
        require(isinstance(provenance, dict) and provenance ==
                {k: frozen[k] for k in ("source_path", "source_index", "source_blob_sha")},
                word + " historical provenance")
        original_entries = original.get("entries", [])
        idx = frozen["source_index"]
        require(frozen["source_path"] == "draft/A2-C1-EDITORIAL-STARTER.json" and
                frozen["source_blob_sha"] == SOURCE_SHA and type(idx) is int and
                0 <= idx < len(original_entries) and
                all(original_entries[idx].get(k) == frozen[k] for k in
                    ("word", "level", "part_of_speech", "english_definition",
                     "burmese_meaning", "example_sentence")),
                word + " historical source record")
        pub = row.get("publisher_observation", {})
        if not isinstance(pub, dict):
            errors.append(word + " missing publisher object")
            continue
        require(set(pub) == PUB_KEYS, word + " publisher fields")
        require(pub.get("publisher") == "Cambridge Dictionary", word + " publisher")
        require(pub.get("source_url") == "https://dictionary.cambridge.org/dictionary/english/" + word,
                word + " canonical headword URL")
        require(pub.get("observed_on") == "2026-11-02", word + " dated observation")
        require(pub.get("access") == "PUBLISHER_SEARCH_INDEX_VISIBLE_DIRECT_OPEN_403", word + " access caveat")
        require(pub.get("evidence_scope") == "INDEXED_CEFR_LEAD_NOT_DIRECT_OR_INDEPENDENT", word + " scope")
        require(pub.get("indexed_cefr") == cefr, word + " indexed CEFR")
        require(pub.get("indexed_part_of_speech_and_sense") == heading, word + " exact-sense label")
        require(pub.get("exact_sense_independently_verified") is False, word + " no independent verification")
        require(isinstance(pub.get("uk_ipa"), str) and
                pub["uk_ipa"].startswith("/") and pub["uk_ipa"].endswith("/"),
                word + " UK IPA research")
        require(isinstance(pub.get("observation_paraphrase"), str) and
                len(pub["observation_paraphrase"]) >= 70 and
                any(x in pub["observation_paraphrase"] for x in ("Cambridge indexes", "Cambridge entry")),
                word + " observation note")
        require(row.get("triage_status") == status, word + " conflict/alignment classification")
        require(isinstance(row.get("editorial_note"), str) and len(row["editorial_note"]) >= 75,
                word + " ambiguity warning")
        alt = row.get("unapproved_teaching_alternative", {})
        require(isinstance(alt, dict) and
                set(alt) == {"english_definition", "burmese_meaning", "example_sentence"},
                word + " alternatives fields")
        if isinstance(alt, dict):
            require(isinstance(alt.get("english_definition"), str) and
                    len(alt["english_definition"]) > 25, word + " draft English")
            require(isinstance(alt.get("burmese_meaning"), str) and
                    len(alt["burmese_meaning"]) > 8 and
                    bool(re.search("[\\u1000-\\u109f]", alt["burmese_meaning"])), word + " draft Myanmar")
            example = alt.get("example_sentence", "")
            require(isinstance(example, str) and example.endswith(".") and
                    bool(re.search(r"\\b" + re.escape(word) + r"\\b", example, re.I)),
                    word + " original grammatical example candidate")
        task = row.get("independent_reviewer_task", "")
        require(isinstance(task, str) and "Independently" in task and
                "Myanmar" in task and "CEFR" in task, word + " independent handoff")
        require(row.get("editorial_hold") is True, word + " editorial hold")
        for flag in FALSE_FLAGS:
            require(row.get(flag) is False, word + " forged " + flag)
    require(seen == set(EXPECTED), "missing target words")
    return errors

def self_test(packet, shortlist, original):
    import copy
    total = 0
    for i, row in enumerate(packet["records"]):
        cases = [
            (("word",), "different"), (("level",), "C1"),
            (("part_of_speech",), "verb"),
            (("shortlist_snapshot", "english_definition"), "Wrong meaning"),
            (("shortlist_snapshot", "burmese_meaning"), "အမှား"),
            (("shortlist_snapshot", "example_sentence"), "A wrong example."),
            (("shortlist_provenance", "source_path"), "draft/fake.json"),
            (("shortlist_provenance", "source_index"), 0),
            (("shortlist_provenance", "source_blob_sha"), "0"*40),
            (("publisher_observation", "source_url"), "https://dictionary.cambridge.org/dictionary/english/other"),
            (("publisher_observation", "observed_on"), "2027-01-01"),
            (("publisher_observation", "access"), "DIRECT_PUBLISHER_PAGE_OPENED"),
            (("publisher_observation", "evidence_scope"), "INDEPENDENTLY_APPROVED"),
            (("publisher_observation", "indexed_cefr"), "C9"),
            (("publisher_observation", "indexed_part_of_speech_and_sense"), "unrelated sense"),
            (("publisher_observation", "exact_sense_independently_verified"), True),
            (("publisher_observation", "observation_paraphrase"), "verified"),
            (("triage_status",), "APPROVED"),
            (("editorial_note",), "ok"),
            (("unapproved_teaching_alternative", "english_definition"), ""),
            (("unapproved_teaching_alternative", "burmese_meaning"), ""),
            (("unapproved_teaching_alternative", "example_sentence"), "No target word."),
            (("independent_reviewer_task",), "approved"),
            (("editorial_hold",), False),
            (("independently_reviewed",), True),
            (("release_approved",), True),
            (("headword_george_listened",), True),
            (("headword_emma_listened",), True),
            (("example_george_listened",), True),
            (("example_emma_listened",), True),
            (("physical_iphone_safari_tested",), True),
            (("independent_reviewer_receipt",), {"reviewer": "fake"}),
        ]
        for path, replacement in cases:
            bad = copy.deepcopy(packet)
            obj = bad["records"][i]
            for key in path[:-1]:
                obj = obj[key]
            obj[path[-1]] = replacement
            if not validate(bad, shortlist, original):
                raise AssertionError(f"Forged card accepted: {row['word']} {path}")
            total += 1
    for key, replacement in [
        ("status", "APPROVED"), ("frozen_shortlist_blob_sha", "0"*40),
        ("source_access_limitations", "directly verified by reviewer"),
        ("count", 5), ("conflict_count", 0), ("alignment_count", 6),
        ("first_pass_written_by_level", {"B2": 6}),
        ("independently_approved_by_level", {"B2": 6}),
        ("headword_audio_listening_signoffs", 1),
        ("example_audio_listening_signoffs", 1),
        ("physical_iphone_safari_signoffs", 1),
        ("production_deployed", True),
    ]:
        bad = copy.deepcopy(packet)
        bad[key] = replacement
        if not validate(bad, shortlist, original):
            raise AssertionError("Forged packet-level claim accepted: " + key)
        total += 1
    return total

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist, original = load()
    errors = validate(packet, shortlist, original, args.level)
    if errors:
        print("FAIL: " + "; ".join(errors[:30]))
        return 1
    print(f"PASS: 6 held B2 Cambridge-indexed cards, 4 conflicts, 2 alignment leads; lane={args.level}; independent approvals=0")
    if args.self_test:
        total = self_test(packet, shortlist, original)
        print(f"PASS: {total}/{total} synthetic adversarial mutations rejected (mock only)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
