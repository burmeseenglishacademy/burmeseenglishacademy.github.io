#!/usr/bin/env python3
"""Fail-closed mechanical audit of six held C1 Oxford/Cambridge research cards.
Publisher evidence and synthetic tests are NOT independent linguistic, audio or device approval.
"""
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json"
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-CONJECTURE-DISSONANCE-DIRECT-OXFORD-2026-11-03.json"
HASHES = {
    SHORT: "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
    SOURCE: "da7df62123acfac89a0acedad4652ec499c7ed3d",
    PACKET: "a2f35cb7de46c4239dea2c90be2fe5fb70810a48",
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("conjecture", "conscientious", "culpability", "disparage",
         "disproportionate", "dissonance")
EXPECTED = {k: 200 for k in LEVELS}
ZERO = {k: 0 for k in LEVELS}
FALSE_FLAGS = ("independently_reviewed", "release_approved",
               "george_headword_listened", "emma_headword_listened",
               "george_example_listened", "emma_example_listened",
               "physical_iphone_safari_tested")
FIELDS = ("english_definition", "burmese_meaning", "example_sentence")
REQUIRED_OBS = ("source_url", "source_line_range", "source_sense_summary",
                "uk_ipa_lead", "cambridge_publisher_url", "exact_sense_cefr_label")

def blob_hash(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load():
    for path, expected in HASHES.items():
        if blob_hash(path) != expected:
            raise ValueError("BLOCK: frozen Git blob mismatch " + str(path))
    return tuple(json.loads(p.read_text(encoding="utf-8"))
                 for p in (PACKET, SHORT, SOURCE))

def validate(packet, shortlist, source, level="ALL"):
    errors = []
    def check(ok, message):
        if not ok:
            errors.append(message)
    check(level in (*LEVELS, "ALL"), "unknown lane")
    entries = shortlist.get("entries", [])
    check(isinstance(entries, list) and len(entries) == 1000, "1000 frozen entries")
    if not isinstance(entries, list):
        return errors
    check(Counter(x.get("level") for x in entries) == Counter(EXPECTED),
          "five 200-word quotas")
    check(len({str(x.get("word", "")).casefold() for x in entries}) == 1000,
          "global written-form uniqueness")
    check(shortlist.get("independently_approved_by_level") == ZERO,
          "frozen independent approvals")
    for e in entries:
        check(e.get("editorial_hold") is True and all(
            e.get(k) is False for k in ("reviewed_english", "reviewed_burmese",
            "reviewed_example", "reviewed_level", "reviewed_pronunciation",
            "release_approved")), "false frozen signoff " + str(e.get("word")))
    check(packet.get("schema") == 1, "packet schema")
    check(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY", "scope")
    check(packet.get("observed_on") == "2026-11-03", "date")
    check(packet.get("status") == "C1_SIX_DIRECT_OXFORD_SENSE_AND_CAMBRIDGE_INDEXED_C1_TRIAGE_HUMAN_REVIEW_REQUIRED", "hold status")
    check(packet.get("frozen_shortlist_blob_sha") == HASHES[SHORT], "shortlist binding")
    check(packet.get("written_by_level") == EXPECTED, "written totals")
    check(packet.get("independently_approved_by_level") == ZERO, "false approvals")
    check(packet.get("production_deployed") is False, "false deployment")
    for key in ("audio_listening_signoffs", "physical_iphone_safari_signoffs"):
        check(type(packet.get(key)) is int and packet[key] == 0, "false signoff " + key)
    limitation = packet.get("source_limitations", "")
    check(all(s in limitation for s in ("403", "TOPIC", "not independent", "hold"))
          or ("403" in limitation and "TOPIC" in limitation and "not independent" in limitation.lower()),
          "publisher access/CEFR honesty")
    records = packet.get("records", [])
    check(isinstance(records, list) and len(records) == 6, "six research cards")
    if not isinstance(records, list):
        return errors
    check(tuple(r.get("word") for r in records) == WORDS, "ordered exact word set")
    original = {e["word"]: e for e in entries}
    source_entries = source.get("entries", [])
    for r in records:
        w = r.get("word")
        if w not in original:
            errors.append("unknown headword " + str(w))
            continue
        e = original[w]
        check(r.get("level") == "C1" and r.get("part_of_speech") == e.get("part_of_speech"),
              "word POS/level " + w)
        check(r.get("frozen_snapshot") == {k: e.get(k) for k in FIELDS},
              "frozen bilingual/example drift " + w)
        p = r.get("provenance", {})
        check(p == {k: e.get(k) for k in ("source_path", "source_index", "source_blob_sha")},
              "source provenance " + w)
        idx = e.get("source_index")
        check(isinstance(idx, int) and 0 <= idx < len(source_entries), "historical index " + w)
        if isinstance(idx, int) and 0 <= idx < len(source_entries):
            old = source_entries[idx]
            check(old.get("word") == w and old.get("proposed_level") == "C1" and
                  all(old.get(k) == e.get(k) for k in FIELDS),
                  "historical source mismatch " + w)
        o = r.get("publisher_observation", {})
        check(o.get("publisher") == "Oxford Advanced Learner's Dictionary", "publisher " + w)
        check(o.get("source_url") == "https://www.oxfordlearnersdictionaries.com/definition/english/" +
              ("conjecture_1" if w == "conjecture" else w), "publisher URL " + w)
        check(urlparse(o.get("cambridge_publisher_url", "")).netloc == "dictionary.cambridge.org"
              and o.get("cambridge_publisher_url", "").endswith("/" + w), "Cambridge URL " + w)
        check(o.get("observed_on") == "2026-11-03" and
              o.get("access") == "DIRECT_OXFORD_PUBLISHER_PAGE_OPENED" and
              o.get("cambridge_access") == "PUBLISHER_OWNED_SEARCH_INDEX_ONLY_DIRECT_PAGE_403",
              "source access honesty " + w)
        check(all(isinstance(o.get(k), str) and len(o[k]) >= 5 for k in REQUIRED_OBS),
              "source metadata " + w)
        expected_cefr = ("CAMBRIDGE_INDEXED_C1_NOT_INDEPENDENT" if w == "conscientious"
                         else "NOT_ESTABLISHED")
        check(o.get("exact_sense_cefr_label") == expected_cefr and
              o.get("independently_verified") is False, "false CEFR evidence " + w)
        alt = r.get("unapproved_teaching_alternative", {})
        check(all(isinstance(alt.get(k), str) and len(alt[k].strip()) > 15 for k in FIELDS),
              "missing bilingual alternatives " + w)
        check(w in alt.get("example_sentence", "").lower(), "alternative example lemma " + w)
        check(isinstance(r.get("risk"), str) and len(r["risk"]) > 18, "missing risk " + w)
        check("Independent human" in r.get("independent_review_task", ""),
              "independent reviewer handoff " + w)
        check(r.get("editorial_hold") is True and
              all(r.get(k) is False for k in FALSE_FLAGS), "false approval/audio/iPhone " + w)
    return errors

def negative_tests(packet, shortlist, source):
    total = 0
    mutations = [
        ("scope", "FIVE_THOUSAND"),
        ("status", "APPROVED"),
        ("observed_on", "2027-01-01"),
        ("independently_approved_by_level", {**ZERO, "C1": 1}),
        ("audio_listening_signoffs", 1),
        ("physical_iphone_safari_signoffs", 1),
        ("production_deployed", True),
    ]
    for key, value in mutations:
        x = copy.deepcopy(packet); x[key] = value
        if not validate(x, shortlist, source):
            raise AssertionError("forgery accepted " + key)
        total += 1
    for i in range(6):
        for key, value in (
            ("editorial_hold", False), ("independently_reviewed", True),
            ("release_approved", True), ("george_headword_listened", True),
            ("emma_example_listened", True), ("physical_iphone_safari_tested", True),
        ):
            x = copy.deepcopy(packet); x["records"][i][key] = value
            if not validate(x, shortlist, source):
                raise AssertionError("forged receipt accepted " + key)
            total += 1
        for key, value in (
            ("source_url", "https://fake.example.com/word"),
            ("cambridge_access", "DIRECT_FULL_PAGE_VERIFIED"),
            ("exact_sense_cefr_label", "C1_HUMAN_APPROVED"),
            ("observed_on", "2027-01-01"),
        ):
            x = copy.deepcopy(packet); x["records"][i]["publisher_observation"][key] = value
            if not validate(x, shortlist, source):
                raise AssertionError("forged source accepted " + key)
            total += 1
        x = copy.deepcopy(packet); x["records"][i]["frozen_snapshot"]["burmese_meaning"] = "fake"
        if not validate(x, shortlist, source):
            raise AssertionError("forged Burmese accepted")
        total += 1
    x = copy.deepcopy(shortlist); x["entries"][0]["release_approved"] = True
    if not validate(packet, x, source):
        raise AssertionError("frozen release flag accepted")
    total += 1
    x = copy.deepcopy(source); x["entries"][28]["english_definition"] = "fake"
    if not validate(packet, shortlist, x):
        raise AssertionError("historical source drift accepted")
    total += 1
    print("PASS: " + str(total) + "/" + str(total) +
          " synthetic source, Myanmar, CEFR, review, listening, iPhone and release forgeries rejected")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    try:
        packet, shortlist, source = load()
        issues = validate(packet, shortlist, source, args.level)
        if issues:
            for issue in issues[:20]:
                print("BLOCK:", issue)
            return 1
        if args.self_test:
            negative_tests(packet, shortlist, source)
        print("PASS: six held C1 publisher-source cards structurally consistent; " +
              "200 first-pass/0 independently approved per level; RELEASE BLOCKED")
        return 0
    except (ValueError, AssertionError, OSError, json.JSONDecodeError) as exc:
        print("BLOCK:", exc)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
