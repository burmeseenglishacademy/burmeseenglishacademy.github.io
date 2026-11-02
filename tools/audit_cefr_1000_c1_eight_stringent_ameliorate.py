#!/usr/bin/env python3
"""Fail-closed mechanical audit of eight UNAPPROVED Oxford C1 research cards.

Direct dictionary sense observations are not CEFR approvals. No audio,
physical iPhone testing, independent review or deployment occurs here.
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
PACKET = ROOT / "draft/CEFR-1000-C1-EIGHT-STRINGENT-AMELIORATE-DIRECT-OXFORD-2026-11-02.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PACKET_SHA = "ce5b9173b14dc23ea9464dc5014f509afc294e5a"
SOURCE_SHAS = {
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json": "7eaf88b9ed7687b26ccde713262f10fb209743a8",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json": "da7df62123acfac89a0acedad4652ec499c7ed3d",
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("stringent", "tenacious", "ubiquitous", "vindicate",
         "vilify", "whimsical", "acquiescence", "ameliorate")
RISKS = {
    "stringent": "TWO_SENSES_AND_TOPIC_C2_NOT_HEADWORD_CEFR",
    "tenacious": "DETERMINED_PERSON_VS_PERSISTENT_CONDITION",
    "ubiquitous": "VERY_COMMON_NOT_LITERAL_EVERYWHERE_AND_ATTRIBUTIVE_USAGE",
    "vindicate": "JUSTIFY_DECISION_VS_CLEAR_ACCUSATION_AND_TOPIC_LABEL",
    "vilify": "REPUTATION_DAMAGE_NOT_PROOF_OF_FALSE_ALLEGATION",
    "whimsical": "POSITIVE_ONLY_MYANMAR_GLOSS_OMITS_ANNOYING_SENSE",
    "acquiescence": "UNCOUNTABLE_AND_SILENCE_NOT_AUTOMATIC_CONSENT_TOPIC_C2",
    "ameliorate": "TRANSITIVE_COLLOCATION_AND_TOPIC_C2_NOT_CEFR",
}
AUDIO_FLAGS = ("george_headword_listened", "emma_headword_listened",
               "george_example_listened", "emma_example_listened")
FALSE_FLAGS = ("independently_reviewed", "release_approved",
               "physical_iphone_safari_tested", *AUDIO_FLAGS)
SNAPSHOT_FIELDS = ("english_definition", "burmese_meaning", "example_sentence")
PROVENANCE_FIELDS = ("source_path", "source_index", "source_blob_sha")
ROW_FIELDS = {"word", "level", "part_of_speech", "frozen_snapshot",
              "provenance", "publisher_observation", "risk",
              "unapproved_teaching_alternative", "independent_review_task",
              "editorial_hold", *FALSE_FLAGS}

def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def load():
    for path, sha in [(SHORT, SHORT_SHA), (PACKET, PACKET_SHA)] + [
        (ROOT / name, sha) for name, sha in SOURCE_SHAS.items()
    ]:
        if git_blob_sha(path) != sha:
            raise ValueError("Frozen Git blob changed without deliberate review: " + str(path))
    sources = {name: json.loads((ROOT / name).read_text(encoding="utf8"))
               for name in SOURCE_SHAS}
    return (json.loads(PACKET.read_text(encoding="utf8")),
            json.loads(SHORT.read_text(encoding="utf8")), sources)

def validate(packet, shortlist, sources, level="ALL"):
    errors = []
    def check(ok, why):
        if not ok:
            errors.append(why)
    if level not in (*LEVELS, "ALL"):
        return ["Invalid structural CEFR lane"]
    expected_counts = {k: 200 for k in LEVELS}
    entries = shortlist.get("entries", [])
    check(len(entries) == 1000, "Not exactly 1000 frozen entries")
    check(Counter(x.get("level") for x in entries) == Counter(expected_counts),
          "Not exactly 200 per CEFR level")
    check(len({str(x.get("word", "")).casefold() for x in entries}) == 1000,
          "Duplicate case-insensitive written headwords")
    check(shortlist.get("independently_approved_by_level") == {k: 0 for k in LEVELS},
          "Frozen independent approval count altered")
    for entry in entries:
        check(entry.get("editorial_hold") is True
              and all(entry.get(k) is False for k in
                      ("reviewed_english", "reviewed_burmese", "reviewed_example",
                       "reviewed_level", "reviewed_pronunciation", "release_approved")),
              "Frozen entry false signoff " + str(entry.get("word")))
    check(packet.get("schema") == 1, "Research schema changed")
    check(packet.get("scope") == "USER_APPROVED_1000_TOTAL_A1_A2_B1_B2_C1_STAGING_ONLY",
          "Scope changed from 1000")
    check(packet.get("status") == "C1_EIGHT_DIRECT_OXFORD_SENSE_TRIAGE_HUMAN_REVIEW_REQUIRED",
          "Research status falsely promoted")
    check(packet.get("observed_on") == "2026-11-02", "Observation date missing")
    check(packet.get("frozen_shortlist_blob_sha") == SHORT_SHA, "Source binding changed")
    caveat = packet.get("source_limitations", "")
    check(isinstance(caveat, str) and all(s in caveat for s in
          ("directly opened", "No exact-sense C1 CEFR", "not headword-specific",
           "NOT independently")), "Oxford source and approval caveat missing")
    check(packet.get("written_by_level") == expected_counts, "Written totals altered")
    check(packet.get("independently_approved_by_level") == {k: 0 for k in LEVELS},
          "Forged human approval totals")
    for k in ("audio_listening_signoffs", "physical_iphone_safari_signoffs"):
        check(type(packet.get(k)) is int and packet[k] == 0,
              "Forged listening/device signoffs " + k)
    check(packet.get("production_deployed") is False, "False production claim")
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != 8:
        return errors + ["Exactly eight held research cards required"]
    check([r.get("word") for r in rows if isinstance(r, dict)] == list(WORDS),
          "Wrong order, duplicate or missing C1 research headwords")
    frozen = {x["word"]: x for x in entries}
    for row in rows:
        if not isinstance(row, dict):
            errors.append("Non-object research card")
            continue
        word = row.get("word")
        if word not in WORDS:
            errors.append("Unknown research word")
            continue
        entry = frozen[word]
        check(set(row) == ROW_FIELDS, word + ": unexpected or missing fields")
        check(row.get("level") == "C1" == entry["level"], word + ": wrong CEFR")
        check(row.get("part_of_speech") == entry["part_of_speech"], word + ": POS")
        check(row.get("frozen_snapshot") == {k: entry[k] for k in SNAPSHOT_FIELDS},
              word + ": frozen English/Myanmar/example changed")
        check(row.get("provenance") == {k: entry[k] for k in PROVENANCE_FIELDS},
              word + ": provenance mismatch")
        src_path = entry["source_path"]
        src_rows = sources[src_path].get("entries", [])
        idx = entry["source_index"]
        check(isinstance(idx, int) and 0 <= idx < len(src_rows)
              and all(src_rows[idx].get(k) == entry[k]
                      for k in ("word", *SNAPSHOT_FIELDS)),
              word + ": historical source entry mismatch")
        obs = row.get("publisher_observation", {})
        if not isinstance(obs, dict):
            errors.append(word + ": missing source object")
            continue
        parsed = urlparse(str(obs.get("source_url", "")))
        check(parsed.scheme == "https"
              and parsed.hostname == "www.oxfordlearnersdictionaries.com"
              and parsed.path in ("/definition/english/" + word,
                                  "/us/definition/english/" + word)
              and not parsed.query and not parsed.fragment,
              word + ": invalid Oxford exact headword URL")
        check(obs.get("publisher") == "Oxford Advanced Learner's Dictionary"
              and obs.get("observed_on") == "2026-11-02"
              and obs.get("access") == "DIRECT_OXFORD_PUBLISHER_PAGE_OPENED",
              word + ": source provenance/access")
        check(obs.get("exact_sense_cefr_label") == "NOT_OBSERVED"
              and obs.get("independently_verified") is False,
              word + ": fabricated exact-sense CEFR or verification")
        line_range = str(obs.get("source_line_range", ""))
        parts = line_range.split("-")
        check(len(parts) == 2 and all(s.isdigit() for s in parts)
              and int(parts[0]) >= 80 and int(parts[1]) > int(parts[0]),
              word + ": Oxford line locator")
        check(str(obs.get("uk_ipa_lead", "")).startswith("/")
              and str(obs.get("uk_ipa_lead", "")).endswith("/"),
              word + ": UK pronunciation lead")
        check(len(str(obs.get("source_sense_summary", ""))) >= 100,
              word + ": exact-sense risk context truncated")
        check(row.get("risk") == RISKS[word], word + ": risk category altered")
        alt = row.get("unapproved_teaching_alternative", {})
        check(isinstance(alt, dict)
              and set(alt) == set(SNAPSHOT_FIELDS)
              and all(isinstance(alt.get(k), str) and len(alt[k].strip()) >= 25
                      for k in SNAPSHOT_FIELDS)
              and any("\u1000" <= c <= "\u109f" for c in alt["burmese_meaning"]),
              word + ": bilingual alternative incomplete")
        check(isinstance(row.get("independent_review_task"), str)
              and all(s in row["independent_review_task"] for s in
                      ("Independent human", "George/Emma", "signed evidence")),
              word + ": independent review instructions missing")
        check(row.get("editorial_hold") is True
              and all(row.get(k) is False for k in FALSE_FLAGS),
              word + ": forged human/audio/iPhone/deployment approval")
    return errors

def self_test(packet, shortlist, sources):
    base = validate(packet, shortlist, sources)
    if base:
        raise AssertionError("Baseline research invalid: " + repr(base[:8]))
    total = 0
    for idx, word in enumerate(WORDS):
        mutations = [
            ("level", lambda r: r.__setitem__("level", "B2")),
            ("pos", lambda r: r.__setitem__("part_of_speech", "noun" if r["part_of_speech"] != "noun" else "verb")),
            ("english", lambda r: r["frozen_snapshot"].__setitem__("english_definition", "FAKE")),
            ("myanmar", lambda r: r["frozen_snapshot"].__setitem__("burmese_meaning", "FAKE")),
            ("example", lambda r: r["frozen_snapshot"].__setitem__("example_sentence", "FAKE")),
            ("source_index", lambda r: r["provenance"].__setitem__("source_index", 99999)),
            ("publisher", lambda r: r["publisher_observation"].__setitem__("source_url", "https://example.org/" + word)),
            ("access", lambda r: r["publisher_observation"].__setitem__("access", "PUBLISHER_INDEX_ONLY")),
            ("cefr", lambda r: r["publisher_observation"].__setitem__("exact_sense_cefr_label", "C1")),
            ("review", lambda r: r.__setitem__("independently_reviewed", True)),
            ("release", lambda r: r.__setitem__("release_approved", True)),
            ("george", lambda r: r.__setitem__("george_headword_listened", True)),
            ("emma", lambda r: r.__setitem__("emma_example_listened", True)),
            ("iphone", lambda r: r.__setitem__("physical_iphone_safari_tested", True)),
            ("alt", lambda r: r["unapproved_teaching_alternative"].__setitem__("burmese_meaning", "bad")),
            ("source_summary", lambda r: r["publisher_observation"].__setitem__("source_sense_summary", "Oxford c2")),
        ]
        for label, change in mutations:
            forged = copy.deepcopy(packet)
            change(forged["records"][idx])
            if not validate(forged, shortlist, sources):
                raise AssertionError("Unsafe mutation accepted: " + word + "/" + label)
            total += 1
    for key, fake in (("production_deployed", True),
                      ("audio_listening_signoffs", 1),
                      ("physical_iphone_safari_signoffs", 1),
                      ("independently_approved_by_level", {k: 200 for k in LEVELS}),
                      ("status", "APPROVED"),
                      ("source_limitations", "")):
        forged = copy.deepcopy(packet)
        forged[key] = fake
        if not validate(forged, shortlist, sources):
            raise AssertionError("Unsafe packet mutation accepted: " + key)
        total += 1
    print("PASS: " + str(total) + "/" + str(total)
          + " synthetic source, Myanmar, CEFR, reviewer, audio and device mutations rejected")
    print("NO independent reviews or listening signoffs claimed")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet, shortlist, sources = load()
    errors = validate(packet, shortlist, sources, args.level)
    if errors:
        for issue in errors[:25]:
            print("BLOCK:", issue)
        return 1
    if args.self_test:
        self_test(packet, shortlist, sources)
    print("PASS: held C1 Oxford research mechanically consistent; 200 per level, 0 independently approved; release BLOCKED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
