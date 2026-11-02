#!/usr/bin/env python3
"""Fail-closed staging audit of six A2 household-object sense research cards.
A successful run is mechanical evidence only, never human, audio or device approval.
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
PACKET = ROOT / "draft/CEFR-1000-A2-SIX-HOUSEHOLD-OBJECTS-OXFORD-CAMBRIDGE-SENSE-2026-11-03.json"
SOURCES = {
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json": "228c772697e4879f6b8a30f85709d188a1df266c",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json": "96d54ddb6fdc204e8cbea45e8c97a6c98fb17b11",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json": "6a10ae41eb41370a9a5b74d907fa395bb43e18d8",
}
PINNED = {SHORT: "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
          PACKET: "39cf277a9f100e6233eebf8d2b5a674917ca9b98",
          **{ROOT / path: sha for path, sha in SOURCES.items()}}
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("doormat", "shoebox", "saucepan", "washcloth", "greenhouse", "wheelbarrow")
QUOTA = {level: 200 for level in LEVELS}
ZERO = {level: 0 for level in LEVELS}
FIELDS = ("english_definition", "burmese_meaning", "example_sentence")
FALSE_FLAGS = ("independently_reviewed", "release_approved", "george_headword_listened",
               "emma_headword_listened", "george_example_listened",
               "emma_example_listened", "physical_iphone_safari_tested")
URLS = {
    "doormat": "https://www.oxfordlearnersdictionaries.com/definition/english/doormat",
    "shoebox": "https://www.oxfordlearnersdictionaries.com/us/definition/english/shoebox",
    "saucepan": "https://www.oxfordlearnersdictionaries.com/us/definition/english/saucepan",
    "washcloth": "https://www.oxfordlearnersdictionaries.com/us/definition/english/washcloth",
    "greenhouse": "https://www.oxfordlearnersdictionaries.com/definition/english/greenhouse",
    "wheelbarrow": "https://www.oxfordlearnersdictionaries.com/definition/english/wheelbarrow",
}
CAMBRIDGE = {
    "doormat": "doormat", "shoebox": "shoe-box", "saucepan": "saucepan",
    "washcloth": "washcloth", "greenhouse": "greenhouse", "wheelbarrow": "wheelbarrow",
}

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

def load():
    for path, sha in PINNED.items():
        if git_blob(path) != sha:
            raise ValueError("BLOCK: frozen Git blob changed: " + str(path))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORT.read_text(encoding="utf-8"))
    sources = {name: json.loads((ROOT / name).read_text(encoding="utf-8"))
               for name in SOURCES}
    return packet, shortlist, sources

def validate(packet, shortlist, sources, level="ALL"):
    errors = []
    def check(test, message):
        if not test:
            errors.append(message)
    check(level in (*LEVELS, "ALL"), "unknown CEFR lane")
    entries = shortlist.get("entries", [])
    if not isinstance(entries, list):
        return ["frozen shortlist is not a list"]
    check(len(entries) == 1000, "exactly 1000 provisional records")
    check(Counter(x.get("level") for x in entries) == Counter(QUOTA), "five 200 quotas")
    check(len({str(x.get("word", "")).casefold() for x in entries}) == 1000,
          "global written-form deduplication")
    check(shortlist.get("independently_approved_by_level") == ZERO,
          "zero independent approvals in frozen shortlist")
    for e in entries:
        check(e.get("editorial_hold") is True and all(e.get(k) is False for k in
              ("reviewed_english", "reviewed_burmese", "reviewed_example",
               "reviewed_level", "reviewed_pronunciation", "release_approved")),
              "frozen reviewer signoff forgery " + str(e.get("word")))
    check(packet.get("schema") == 1, "packet schema")
    check(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY",
          "1000-word scope")
    check(packet.get("status") == "A2_SIX_DIRECT_OXFORD_CAMBRIDGE_INDEXED_HUMAN_REVIEW_REQUIRED",
          "hold status")
    check(packet.get("observed_on") == "2026-11-03", "observation date")
    check(packet.get("frozen_shortlist_blob_sha") == PINNED[SHORT], "source binding")
    check(packet.get("written_by_level") == QUOTA, "written totals")
    check(packet.get("independently_approved_by_level") == ZERO, "false approval totals")
    check(packet.get("production_deployed") is False, "false production deployment")
    for k in ("audio_listening_signoffs", "physical_iphone_safari_signoffs"):
        check(type(packet.get(k)) is int and packet[k] == 0, "false signoffs " + k)
    limitation = packet.get("source_limitations", "")
    check(all(x in limitation for x in ("403", "520", "TOPIC", "NOT independent", "editorial hold")),
          "source limitations and no independent evidence")
    records = packet.get("records", [])
    if not isinstance(records, list):
        return errors + ["records is not a list"]
    check(len(records) == 6, "exactly six source cards")
    check(tuple(r.get("word") for r in records) == WORDS, "fixed research words")
    lookup = {e.get("word"): e for e in entries}
    for r in records:
        w = r.get("word")
        if w not in lookup:
            errors.append("unknown headword " + str(w))
            continue
        e = lookup[w]
        check(r.get("level") == "A2" and r.get("part_of_speech") == "noun",
              "exact POS/level " + w)
        check(r.get("frozen_snapshot") == {k: e.get(k) for k in FIELDS},
              "frozen bilingual/example mismatch " + w)
        p = r.get("provenance", {})
        check(p == {k: e.get(k) for k in ("source_path", "source_index", "source_blob_sha")},
              "provenance mismatch " + w)
        source_path = e.get("source_path")
        check(source_path in SOURCES and e.get("source_blob_sha") == SOURCES.get(source_path),
              "unrecognised historical source " + w)
        src = sources.get(source_path, {}).get("entries", [])
        i = e.get("source_index")
        check(type(i) is int and 0 <= i < len(src), "source index " + w)
        if type(i) is int and 0 <= i < len(src):
            old = src[i]
            check(old.get("word") == w and old.get("proposed_level") == "A2" and
                  all(old.get(k) == e.get(k) for k in FIELDS),
                  "historical record mismatch " + w)
        o = r.get("publisher_observation", {})
        check(o.get("publisher") == "Oxford Advanced Learner's Dictionary" and
              o.get("source_url") == URLS[w], "direct Oxford URL " + w)
        cu = o.get("cambridge_publisher_url", "")
        check(urlparse(cu).hostname == "dictionary.cambridge.org" and
              cu.rstrip("/").endswith("/" + CAMBRIDGE[w]),
              "Cambridge URL " + w)
        check(o.get("observed_on") == "2026-11-03" and
              o.get("access") == "DIRECT_OXFORD_PUBLISHER_PAGE_OPENED" and
              o.get("cambridge_access") == "PUBLISHER_OWNED_SEARCH_INDEX_ONLY_DIRECT_PAGE_403_OR_520",
              "publisher access honesty " + w)
        check(all(isinstance(o.get(k), str) and len(o[k]) >= 5 for k in
              ("source_line_range", "uk_ipa_lead", "source_sense_summary")),
              "publisher observation detail " + w)
        expected = ("CAMBRIDGE_INDEXED_B1_CONFLICT_NOT_INDEPENDENT"
                    if w == "saucepan" else "NOT_ESTABLISHED")
        check(o.get("exact_sense_cefr_label") == expected and
              o.get("independently_verified") is False, "CEFR signoff forgery " + w)
        alt = r.get("unapproved_teaching_alternative", {})
        check(all(isinstance(alt.get(k), str) and len(alt[k].strip()) >= 15 for k in FIELDS),
              "missing bilingual alternative " + w)
        check(w in alt.get("example_sentence", "").casefold(),
              "example must demonstrate headword " + w)
        check(isinstance(r.get("risk"), str) and len(r["risk"]) >= 15, "risk " + w)
        check("Independent human reviewer" in r.get("independent_review_task", ""),
              "review handoff " + w)
        check(r.get("editorial_hold") is True and
              all(r.get(k) is False for k in FALSE_FLAGS),
              "fabricated reviewer/audio/device signoff " + w)
    return errors

def negative_tests(packet, shortlist, sources):
    count = 0
    top = [
        ("scope", "FIVE_THOUSAND"), ("status", "APPROVED"),
        ("observed_on", "2027-01-01"),
        ("independently_approved_by_level", {**ZERO, "A2": 1}),
        ("audio_listening_signoffs", 1), ("physical_iphone_safari_signoffs", 1),
        ("production_deployed", True), ("source_limitations", "verified"),
    ]
    for k, v in top:
        p = copy.deepcopy(packet); p[k] = v
        if not validate(p, shortlist, sources):
            raise AssertionError("FAIL OPEN: top " + k)
        count += 1
    for i in range(6):
        for k, v in [
            ("editorial_hold", False), ("independently_reviewed", True),
            ("release_approved", True), ("george_headword_listened", True),
            ("emma_headword_listened", True), ("george_example_listened", True),
            ("emma_example_listened", True), ("physical_iphone_safari_tested", True),
        ]:
            p = copy.deepcopy(packet); p["records"][i][k] = v
            if not validate(p, shortlist, sources):
                raise AssertionError("FAIL OPEN: row " + k)
            count += 1
        for k, v in [
            ("source_url", "https://fake.invalid/word"),
            ("cambridge_access", "DIRECT_PAGE_VERIFIED"),
            ("exact_sense_cefr_label", "A2_INDEPENDENT_APPROVED"),
            ("independently_verified", True),
            ("observed_on", "2027-01-01"),
        ]:
            p = copy.deepcopy(packet); p["records"][i]["publisher_observation"][k] = v
            if not validate(p, shortlist, sources):
                raise AssertionError("FAIL OPEN: observation " + k)
            count += 1
        p = copy.deepcopy(packet); p["records"][i]["frozen_snapshot"]["burmese_meaning"] = "forged"
        if not validate(p, shortlist, sources):
            raise AssertionError("FAIL OPEN: Myanmar tamper")
        count += 1
        p = copy.deepcopy(packet); p["records"][i]["provenance"]["source_index"] = -1
        if not validate(p, shortlist, sources):
            raise AssertionError("FAIL OPEN: provenance tamper")
        count += 1
    s = copy.deepcopy(shortlist); s["entries"][0]["reviewed_level"] = True
    if not validate(packet, s, sources):
        raise AssertionError("FAIL OPEN: source reviewer tamper")
    count += 1
    s = copy.deepcopy(shortlist); s["entries"][0]["word"] = "doormat"
    if not validate(packet, s, sources):
        raise AssertionError("FAIL OPEN: duplicate word")
    count += 1
    for path in SOURCES:
        x = copy.deepcopy(sources)
        x[path]["entries"][0]["word"] = "FORGED"
        # Batch59's target is at index 3, and batches60/61 target index0/12/13.
        if path.endswith("BATCH59.json"):
            x[path]["entries"][3]["word"] = "FORGED"
        elif path.endswith("BATCH61.json"):
            x[path]["entries"][12]["word"] = "FORGED"
        if not validate(packet, shortlist, x):
            raise AssertionError("FAIL OPEN: historical source " + path)
        count += 1
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet, shortlist, sources = load()
    errors = validate(packet, shortlist, sources, args.level)
    if errors:
        raise SystemExit("BLOCK: " + "; ".join(errors[:15]))
    print("PASS: six A2 Oxford-direct research cards source-bound; 200 per level; 0 independently approved; release held; lane=" + args.level)
    if args.self_test:
        n = negative_tests(packet, shortlist, sources)
        print(f"PASS: {n}/{n} synthetic source, CEFR, bilingual, reviewer, listening, device and release forgeries rejected; NOT independent review")

if __name__ == "__main__":
    main()
