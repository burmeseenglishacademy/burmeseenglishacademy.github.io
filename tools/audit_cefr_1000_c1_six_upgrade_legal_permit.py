#!/usr/bin/env python3
"""Fail-closed staging research audit. Mechanical checks are NOT human CEFR approval."""
import argparse
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-UPGRADE-LEGALLY-SLAVERY-PERMIT-WARRANT-CENSUS-2026-11-02.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PACKET_SHA = "485ba9bd42d5f2cee6e5e7353fee0f96ddb9f070"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "upgrade": ("verb", "B2", "CAMBRIDGE_PUBLISHER_INDEX_SEARCH_RESULT_DIRECT_PAGE_403", "https://dictionary.cambridge.org/dictionary/english/upgrade", "C1_B2_CONFLICT_AND_VERB_NOUN_STRESS"),
    "warrant": ("noun", "UNLABELLED_EXACT_SENSE", "DIRECT_OXFORD_PUBLISHER_PAGE_OPENED", "https://www.oxfordlearnersdictionaries.com/definition/english/warrant_1", "EXACT_SENSE_CEFR_UNSUBSTANTIATED_AND_TOPIC_LABEL"),
    "slavery": ("noun", "C1", "CAMBRIDGE_PUBLISHER_INDEX_SEARCH_RESULT_DIRECT_PAGE_403", "https://dictionary.cambridge.org/dictionary/english/slavery", "C1_ALIGNMENT_LEAD_UNCOUNTABLE_AND_BILINGUAL_SCOPE"),
    "legally": ("adverb", "B2", "CAMBRIDGE_PUBLISHER_INDEX_SEARCH_RESULT_DIRECT_PAGE_403", "https://dictionary.cambridge.org/dictionary/english/legally", "C1_B2_CONFLICT_AND_COLLOCATION_SCOPE"),
    "permit": ("noun", "C1", "CAMBRIDGE_PUBLISHER_INDEX_SEARCH_RESULT_DIRECT_PAGE_403", "https://dictionary.cambridge.org/dictionary/english/permit", "C1_ALIGNMENT_LEAD_NOUN_VERB_STRESS"),
    "census": ("noun", "UNLABELLED_EXACT_SENSE", "DIRECT_OXFORD_PUBLISHER_PAGE_OPENED", "https://www.oxfordlearnersdictionaries.com/definition/english/census", "EXACT_SENSE_CEFR_UNSUBSTANTIATED_AND_NOUN_PROCESS"),
}
FALSE_FIELDS = (
    "editorial_hold", "independently_reviewed", "release_approved",
    "george_headword_listened", "emma_headword_listened",
    "george_example_listened", "emma_example_listened",
    "physical_iphone_safari_tested",
)

def git_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def load():
    if git_blob(SHORT) != SHORT_SHA:
        raise SystemExit("FAIL: frozen shortlist blob changed")
    if git_blob(PACKET) != PACKET_SHA:
        raise SystemExit("FAIL: six-card research packet blob changed; re-review and re-pin deliberately")
    return json.loads(PACKET.read_text(encoding="utf-8")), json.loads(SHORT.read_text(encoding="utf-8"))

def validate(packet, shortlist, lane="ALL"):
    errors = []
    if lane not in (*LEVELS, "ALL"):
        return ["invalid lane"]
    entries = shortlist.get("entries", [])
    counts = Counter(e.get("level") for e in entries)
    if len(entries) != 1000 or any(counts[level] != 200 for level in LEVELS):
        errors.append("shortlist must contain 200 per level, 1000 total")
    if len({str(e.get("word", "")).casefold() for e in entries}) != 1000:
        errors.append("duplicate shortlist written forms")
    if any(not e.get("editorial_hold") or any(e.get(k) is not False for k in
           ("reviewed_english", "reviewed_burmese", "reviewed_example",
            "reviewed_level", "reviewed_pronunciation", "release_approved")) for e in entries):
        errors.append("shortlist forged review or release approval")
    if packet.get("frozen_shortlist_blob_sha") != SHORT_SHA:
        errors.append("source blob mismatch")
    if packet.get("scope") != "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY":
        errors.append("scope changed")
    if packet.get("observed_on") != "2026-11-02":
        errors.append("observation date changed")
    if "HTTP 403" not in packet.get("source_limitations", "") or "not" not in packet.get("source_limitations", "").lower():
        errors.append("source access limitations missing")
    if packet.get("written_by_level") != {k: 200 for k in LEVELS}:
        errors.append("written totals wrong")
    if packet.get("independently_approved_by_level") != {k: 0 for k in LEVELS}:
        errors.append("independent approval falsely claimed")
    if packet.get("audio_listening_signoffs") != 0 or packet.get("physical_iphone_safari_signoffs") != 0:
        errors.append("false listening or iPhone signoffs")
    if packet.get("production_deployed") is not False:
        errors.append("false production deployment")
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 6:
        return errors + ["six records required"]
    if set(r.get("word") for r in records) != set(EXPECTED):
        errors.append("research card headword set changed")
    lookup = {(e.get("level"), e.get("word")): e for e in entries}
    for r in records:
        word = r.get("word")
        if word not in EXPECTED:
            errors.append("unknown word")
            continue
        pos, cefr, access, url, risk = EXPECTED[word]
        e = lookup.get(("C1", word))
        if e is None:
            errors.append(word + ": not in frozen C1")
            continue
        if r.get("level") != "C1" or r.get("part_of_speech") != pos:
            errors.append(word + ": wrong POS or level")
        snapshot = {k: e[k] for k in ("english_definition", "burmese_meaning", "example_sentence")}
        provenance = {k: e[k] for k in ("source_path", "source_index", "source_blob_sha")}
        if r.get("frozen_snapshot") != snapshot or r.get("provenance") != provenance:
            errors.append(word + ": frozen bilingual source or historical provenance changed")
        p = r.get("publisher_observation", {})
        if (p.get("source_url"), p.get("access"), p.get("exact_sense_cefr_label")) != (url, access, cefr):
            errors.append(word + ": publisher URL/access/CEFR attribution changed")
        if p.get("observed_on") != "2026-11-02" or p.get("independently_verified") is not False:
            errors.append(word + ": publisher observation forged")
        if len(p.get("source_sense_summary", "")) < 65 or not p.get("uk_ipa_lead", "").startswith("/"):
            errors.append(word + ": source sense or UK pronunciation lead missing")
        if r.get("risk") != risk:
            errors.append(word + ": exact-sense risk lost")
        a = r.get("unapproved_teaching_alternative", {})
        if any(len(str(a.get(k, "")).strip()) < 18 for k in
               ("english_definition", "burmese_meaning", "example_sentence")):
            errors.append(word + ": bilingual teaching alternative incomplete")
        if len(r.get("independent_review_task", "")) < 100:
            errors.append(word + ": independent review task lost")
        if r.get("editorial_hold") is not True or any(r.get(k) is not False for k in FALSE_FIELDS[1:]):
            errors.append(word + ": forged reviewer, audio, device or release flags")
    return errors

def self_test(packet, shortlist):
    cases = []
    def add(label, p=None, s=None):
        cases.append((label, p if p is not None else copy.deepcopy(packet),
                      s if s is not None else copy.deepcopy(shortlist)))
    for idx, record in enumerate(packet["records"]):
        for key, replacement in (
            ("word", "invented"), ("level", "B2"), ("part_of_speech", "adjective"),
            ("risk", "NONE"), ("editorial_hold", False),
            ("independently_reviewed", True), ("release_approved", True),
            ("george_headword_listened", True), ("emma_headword_listened", True),
            ("george_example_listened", True), ("emma_example_listened", True),
            ("physical_iphone_safari_tested", True),
        ):
            m = copy.deepcopy(packet)
            m["records"][idx][key] = replacement
            add(record["word"] + " " + key, m)
        for key, replacement in (
            ("source_url", "https://example.com/unsupported"),
            ("access", "DIRECT_CAMBRIDGE_VERIFIED"),
            ("exact_sense_cefr_label", "C1_APPROVED"),
            ("observed_on", "2026-10-01"),
            ("independently_verified", True),
            ("source_sense_summary", ""),
            ("uk_ipa_lead", ""),
        ):
            m = copy.deepcopy(packet)
            m["records"][idx]["publisher_observation"][key] = replacement
            add(record["word"] + " publisher " + key, m)
        for key in ("english_definition", "burmese_meaning", "example_sentence"):
            m = copy.deepcopy(packet)
            m["records"][idx]["frozen_snapshot"][key] = "invented"
            add(record["word"] + " source " + key, m)
            m = copy.deepcopy(packet)
            m["records"][idx]["unapproved_teaching_alternative"][key] = ""
            add(record["word"] + " alternative " + key, m)
        m = copy.deepcopy(packet)
        m["records"][idx]["provenance"]["source_index"] = -1
        add(record["word"] + " provenance", m)
        m = copy.deepcopy(packet)
        m["records"][idx]["independent_review_task"] = "approved"
        add(record["word"] + " task", m)
    for key, value in (
        ("audio_listening_signoffs", 1), ("physical_iphone_safari_signoffs", 1),
        ("production_deployed", True), ("source_limitations", ""),
        ("frozen_shortlist_blob_sha", "fake"), ("observed_on", "2025-01-01"),
    ):
        m = copy.deepcopy(packet)
        m[key] = value
        add("packet " + key, m)
    m = copy.deepcopy(packet)
    m["independently_approved_by_level"]["C1"] = 1
    add("approval count", m)
    m = copy.deepcopy(shortlist)
    m["entries"][0]["release_approved"] = True
    add("shortlist release forgery", s=m)
    m = copy.deepcopy(shortlist)
    m["entries"][0]["word"] = m["entries"][1]["word"]
    add("shortlist duplicate", s=m)
    for label, p, s in cases:
        if not validate(p, s):
            raise AssertionError("Synthetic mutation escaped audit: " + label)
    print("PASS: " + str(len(cases)) + "/" + str(len(cases)) +
          " synthetic mutations rejected (mechanical only, no independent approval)")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet, shortlist = load()
    errors = validate(packet, shortlist, args.level)
    if errors:
        raise SystemExit("FAIL: " + "; ".join(errors[:20]))
    print("PASS: six held C1 research cards, source/CEFR/POS/provenance and no-release integrity, lane " + args.level)
    if args.self_test:
        self_test(packet, shortlist)

if __name__ == "__main__":
    main()
