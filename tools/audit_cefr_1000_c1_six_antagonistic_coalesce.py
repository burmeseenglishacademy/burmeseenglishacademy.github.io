#!/usr/bin/env python3
"""Fail-closed structural/source audit of six C1 Oxford research leads; NO APPROVAL.

Oxford dictionary definitions do not independently prove exact-sense C1 placement.
No independent reviewer, British George/Emma listening, iPhone test or deployment
is performed by this script. Synthetic forgeries test rejection, not correctness.
"""
import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json"
PACKET = ROOT / "draft/CEFR-1000-C1-SIX-ANTAGONISTIC-COALESCE-DIRECT-OXFORD-2026-11-03.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "da7df62123acfac89a0acedad4652ec499c7ed3d"
PACKET_SHA = "ba68cf9ec47b79a39a82c4493f48f96f87379da3"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("antagonistic", "arbitrariness", "assiduous", "catharsis",
         "circumvent", "coalesce")
RISKS = {
    "antagonistic": "HOSTILITY_VS_OPPOSITION_AND_TO_TOWARDS_COMPLEMENT",
    "arbitrariness": "UNCOUNTABLE_TWO_SENSES_NO_REASON_VS_UNLIMITED_POWER",
    "assiduous": "LONG_DURATION_NOT_REQUIRED_AND_TOPIC_C2_NOT_CEFR",
    "catharsis": "EMOTIONAL_RELEASE_PROCESS_VS_RESULT_AND_IRREGULAR_PLURAL",
    "circumvent": "TRANSITIVE_AVOID_RULE_VS_PHYSICAL_ROUTE_AND_TOPIC_C2",
    "coalesce": "INTRANSITIVE_INTO_COLLOCATION_VS_AROUND_PROPOSAL",
}
SENSE_MARKERS = {
    "antagonistic": ("opposition", "hostility"),
    "arbitrariness": ("uncountable", "power"),
    "assiduous": ("long duration", "topic tag"),
    "catharsis": ("process", "catharses"),
    "circumvent": ("transitive", "topic labels"),
    "coalesce": ("intransitive", "into"),
}
FALSE_FLAGS = ("independently_reviewed", "release_approved",
               "george_headword_listened", "emma_headword_listened",
               "george_example_listened", "emma_example_listened",
               "physical_iphone_safari_tested")
ROW_KEYS = {"word", "level", "part_of_speech", "frozen_snapshot",
            "provenance", "publisher_observation", "risk",
            "unapproved_teaching_alternative", "independent_review_task",
            "editorial_hold", *FALSE_FLAGS}
SNAP_KEYS = ("english_definition", "burmese_meaning", "example_sentence")
PROV_KEYS = ("source_path", "source_index", "source_blob_sha")
OBS_KEYS = {"publisher", "source_url", "observed_on", "access",
            "source_line_range", "uk_ipa_lead", "source_sense_summary",
            "exact_sense_cefr_label", "independently_verified"}
EXPECTED = {level: 200 for level in LEVELS}
ZERO = {level: 0 for level in LEVELS}


def blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load():
    for path, sha in ((SHORT, SHORT_SHA), (SOURCE, SOURCE_SHA), (PACKET, PACKET_SHA)):
        if blob_sha(path) != sha:
            raise ValueError("Frozen Git blob changed without review: " + str(path))
    return tuple(json.loads(path.read_text(encoding="utf-8"))
                 for path in (PACKET, SHORT, SOURCE))


def validate(packet, shortlist, source, level="ALL"):
    issues = []
    def require(condition, description):
        if not condition:
            issues.append(description)
    if level not in (*LEVELS, "ALL"):
        return ["Unknown CEFR lane"]
    entries = shortlist.get("entries", [])
    require(isinstance(entries, list) and len(entries) == 1000, "Frozen 1000 count")
    if not isinstance(entries, list):
        return issues
    require(Counter(e.get("level") for e in entries) == Counter(EXPECTED),
            "Frozen 200-per-level quotas")
    require(len({str(e.get("word", "")).casefold() for e in entries}) == 1000,
            "Duplicate written-form headwords")
    require(shortlist.get("independently_approved_by_level") == ZERO,
            "Frozen approval totals changed")
    for e in entries:
        require(e.get("editorial_hold") is True and all(
            e.get(k) is False for k in ("reviewed_english", "reviewed_burmese",
            "reviewed_example", "reviewed_level", "reviewed_pronunciation",
            "release_approved")), "False frozen approval: " + str(e.get("word")))
    require(packet.get("schema") == 1, "Research schema")
    require(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY",
            "Scope changed")
    require(packet.get("observed_on") == "2026-11-03", "Observation date changed")
    require(packet.get("status") == "C1_SIX_DIRECT_OXFORD_SENSE_TRIAGE_HUMAN_REVIEW_REQUIRED",
            "Status falsely promoted")
    require(packet.get("frozen_shortlist_blob_sha") == SHORT_SHA, "Frozen source binding")
    require(packet.get("written_by_level") == EXPECTED, "Written counts changed")
    require(packet.get("independently_approved_by_level") == ZERO,
            "Fabricated independent approvals")
    for k in ("audio_listening_signoffs", "physical_iphone_safari_signoffs"):
        require(type(packet.get(k)) is int and packet[k] == 0, "Forged signoffs: " + k)
    require(packet.get("production_deployed") is False, "False production claim")
    caveat = packet.get("source_limitations", "")
    require(isinstance(caveat, str) and all(s in caveat for s in (
        "directly opened", "No exact-sense C1 CEFR badge", "not exact-headword",
        "NOT independently reviewed")), "Source/CEFR/human-review caveat missing")
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != len(WORDS):
        return issues + ["Expected exactly six research cards"]
    require([r.get("word") for r in rows] == list(WORDS),
            "Research card ordering/identity changed")
    original_by_word = {e["word"]: e for e in entries}
    source_entries = source.get("entries", [])
    for row in rows:
        w = row.get("word")
        if w not in RISKS:
            issues.append("Unexpected headword " + str(w))
            continue
        original = original_by_word.get(w)
        if original is None:
            issues.append("Not in frozen shortlist: " + w)
            continue
        require(set(row) == ROW_KEYS, "Missing/extra research fields: " + w)
        require(row.get("level") == "C1" and original.get("level") == "C1",
                "C1 level changed: " + w)
        require(row.get("part_of_speech") == original.get("part_of_speech"),
                "POS mismatch: " + w)
        snap = row.get("frozen_snapshot", {})
        require(isinstance(snap, dict) and set(snap) == set(SNAP_KEYS),
                "Snapshot schema: " + w)
        for field in SNAP_KEYS:
            require(snap.get(field) == original.get(field),
                    "Frozen bilingual/example mismatch: " + w + "/" + field)
        prov = row.get("provenance", {})
        require(isinstance(prov, dict) and set(prov) == set(PROV_KEYS),
                "Provenance schema: " + w)
        for field in PROV_KEYS:
            require(prov.get(field) == original.get(field),
                    "Historical source mismatch: " + w + "/" + field)
        require(prov.get("source_path") == "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json"
                and prov.get("source_blob_sha") == SOURCE_SHA,
                "Source path/blob changed: " + w)
        index = prov.get("source_index")
        if type(index) is not int or not 0 <= index < len(source_entries):
            issues.append("Invalid historical source index: " + w)
        else:
            src = source_entries[index]
            require(src.get("word") == w and src.get("proposed_level") == "C1",
                    "Historical source identity/level: " + w)
            for field in (*SNAP_KEYS, "part_of_speech"):
                require(src.get(field) == original.get(field),
                        "Historical source content: " + w + "/" + field)
        obs = row.get("publisher_observation", {})
        require(isinstance(obs, dict) and set(obs) == OBS_KEYS,
                "Publisher evidence schema: " + w)
        require(obs.get("publisher") == "Oxford Advanced Learner's Dictionary",
                "Publisher identity: " + w)
        url = obs.get("source_url", "")
        parsed = urlparse(url) if isinstance(url, str) else urlparse("")
        require(parsed.scheme == "https"
                and parsed.hostname == "www.oxfordlearnersdictionaries.com"
                and parsed.path == "/definition/english/" + w
                and not parsed.query and not parsed.fragment,
                "Publisher URL/headword binding: " + w)
        require(obs.get("observed_on") == "2026-11-03"
                and obs.get("access") == "DIRECT_OXFORD_PUBLISHER_PAGE_OPENED",
                "Observation date/access: " + w)
        require(bool(re.fullmatch(r"\d{2,3}-\d{2,3}",
                str(obs.get("source_line_range", "")))), "Source line locator: " + w)
        require(isinstance(obs.get("uk_ipa_lead"), str)
                and obs["uk_ipa_lead"].startswith("/") and obs["uk_ipa_lead"].endswith("/")
                and len(obs["uk_ipa_lead"]) > 8, "UK IPA lead: " + w)
        summary = obs.get("source_sense_summary", "")
        require(isinstance(summary, str) and len(summary) >= 130
                and all(s in summary.lower() for s in SENSE_MARKERS[w]),
                "Oxford exact-sense caveat: " + w)
        require(obs.get("exact_sense_cefr_label") == "NOT_OBSERVED"
                and obs.get("independently_verified") is False,
                "Invented CEFR/human source verification: " + w)
        require(row.get("risk") == RISKS[w], "Risk lost: " + w)
        alt = row.get("unapproved_teaching_alternative", {})
        require(isinstance(alt, dict) and set(alt) == set(SNAP_KEYS),
                "Teaching alternative schema: " + w)
        require(isinstance(alt.get("english_definition"), str)
                and len(alt["english_definition"]) > 35
                and alt["english_definition"] != snap.get("english_definition"),
                "English alternative missing: " + w)
        burmese = alt.get("burmese_meaning", "")
        require(isinstance(burmese, str) and len(burmese) > 25
                and any("\u1000" <= c <= "\u109f" for c in burmese)
                and burmese != snap.get("burmese_meaning"),
                "Myanmar alternative missing: " + w)
        example = alt.get("example_sentence", "")
        require(isinstance(example, str) and len(example) > 35
                and example.endswith(".") and example != snap.get("example_sentence")
                and re.search(r"\b" + re.escape(w) + r"(?:d|s)?\b", example, re.I),
                "Original grammar/example lead missing: " + w)
        task = row.get("independent_review_task", "")
        require(isinstance(task, str) and all(s in task for s in (
                "separate human reviewer", "source-backed C1",
                "George/Emma", "actual listening", "NOT an independent review")),
                "Independent reviewer handoff missing: " + w)
        require(row.get("editorial_hold") is True and all(
                row.get(flag) is False for flag in FALSE_FLAGS),
                "Fabricated reviewer/audio/iPhone signoff: " + w)
    return issues


def self_test(packet, shortlist, source):
    total = 0
    for idx, word in enumerate(WORDS):
        tests = (
            ("word", lambda r: r.__setitem__("word", "fake")),
            ("level", lambda r: r.__setitem__("level", "C2")),
            ("pos", lambda r: r.__setitem__("part_of_speech", "adverb")),
            ("english", lambda r: r["frozen_snapshot"].__setitem__("english_definition", "fake")),
            ("myanmar", lambda r: r["frozen_snapshot"].__setitem__("burmese_meaning", "fake")),
            ("example", lambda r: r["frozen_snapshot"].__setitem__("example_sentence", "fake")),
            ("source_index", lambda r: r["provenance"].__setitem__("source_index", 0)),
            ("source_blob", lambda r: r["provenance"].__setitem__("source_blob_sha", "0"*40)),
            ("publisher_url", lambda r: r["publisher_observation"].__setitem__("source_url", "https://example.com/word")),
            ("publisher_date", lambda r: r["publisher_observation"].__setitem__("observed_on", "2026-10-01")),
            ("source_access", lambda r: r["publisher_observation"].__setitem__("access", "INDEX_ONLY")),
            ("source_locator", lambda r: r["publisher_observation"].__setitem__("source_line_range", "")),
            ("ipa", lambda r: r["publisher_observation"].__setitem__("uk_ipa_lead", "")),
            ("source_summary", lambda r: r["publisher_observation"].__setitem__("source_sense_summary", "Oxford c2")),
            ("cefr", lambda r: r["publisher_observation"].__setitem__("exact_sense_cefr_label", "C1")),
            ("verified", lambda r: r["publisher_observation"].__setitem__("independently_verified", True)),
            ("risk", lambda r: r.__setitem__("risk", "")),
            ("alt_english", lambda r: r["unapproved_teaching_alternative"].__setitem__("english_definition", "bad")),
            ("alt_myanmar", lambda r: r["unapproved_teaching_alternative"].__setitem__("burmese_meaning", "bad")),
            ("alt_example", lambda r: r["unapproved_teaching_alternative"].__setitem__("example_sentence", "bad")),
            ("task", lambda r: r.__setitem__("independent_review_task", "")),
            ("human", lambda r: r.__setitem__("independently_reviewed", True)),
            ("release", lambda r: r.__setitem__("release_approved", True)),
            ("george_headword", lambda r: r.__setitem__("george_headword_listened", True)),
            ("emma_headword", lambda r: r.__setitem__("emma_headword_listened", True)),
            ("george_example", lambda r: r.__setitem__("george_example_listened", True)),
            ("emma_example", lambda r: r.__setitem__("emma_example_listened", True)),
            ("iphone", lambda r: r.__setitem__("physical_iphone_safari_tested", True)),
        )
        for label, mutate in tests:
            forged = copy.deepcopy(packet)
            mutate(forged["records"][idx])
            if not validate(forged, shortlist, source):
                raise AssertionError("FAIL OPEN: " + word + "/" + label)
            total += 1
    for key, fake in (
        ("production_deployed", True),
        ("audio_listening_signoffs", 1),
        ("physical_iphone_safari_signoffs", 1),
        ("independently_approved_by_level", {k: 200 for k in LEVELS}),
        ("status", "APPROVED"),
        ("source_limitations", ""),
        ("written_by_level", {k: 1000 for k in LEVELS}),
    ):
        forged = copy.deepcopy(packet)
        forged[key] = fake
        if not validate(forged, shortlist, source):
            raise AssertionError("FAIL OPEN: packet/" + key)
        total += 1
    for label, mutate in (
        ("shortlist_approval", lambda s: s["entries"][0].__setitem__("release_approved", True)),
        ("shortlist_duplicate", lambda s: s["entries"][1].__setitem__("word", s["entries"][0]["word"])),
        ("shortlist_quota", lambda s: s["entries"][0].__setitem__("level", "B2")),
    ):
        forged = copy.deepcopy(shortlist)
        mutate(forged)
        if not validate(packet, forged, source):
            raise AssertionError("FAIL OPEN: " + label)
        total += 1
    print("PASS: " + str(total) + "/" + str(total)
          + " synthetic Oxford source, CEFR, Myanmar, historical, reviewer, audio, iPhone and release forgeries rejected")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet, shortlist, source = load()
    issues = validate(packet, shortlist, source, args.level)
    if issues:
        for issue in issues[:30]:
            print("BLOCK:", issue)
        return 1
    if args.self_test:
        self_test(packet, shortlist, source)
    print("PASS: six held C1 Oxford research cards mechanically consistent; "
          "200 first-pass per level, 0 independently approved; RELEASE BLOCKED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
