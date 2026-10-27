#!/usr/bin/env python3
"""Staging-only Oxford direct-dictionary five-entry C1 sense evidence audit.

This verifies source/provenance bindings and editorial holds, NOT dictionary
content independently, exact-sense CEFR certification or human Myanmar review.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
EVIDENCE = ROOT / "draft/CEFR-1000-OXFORD-C1-FIVE-DIRECT-SENSE-LEADS-2026-10-27.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "meticulous": ("adjective", (88, 114), "TOPIC_PERSONAL_QUALITIES_C2_NOT_WORDLIST",
                   "Oxford entry describes detailed care", "HIGH_C1_VS_C2_SENSE_LEVEL_CONFLICT"),
    "nuanced": ("adjective", (88, 105), "NO_ENTRY_SPECIFIC_CEFR_LABEL",
                "Oxford describes subtle distinctions", "NO_WORD_SPECIFIC_CEFR_EVIDENCE"),
    "tenacious": ("adjective", (88, 114), "NO_ENTRY_SPECIFIC_CEFR_LABEL",
                 "Oxford distinguishes determined refusal", "SENSE_DISAMBIGUATION_AND_LEVEL_SOURCE_GAP"),
    "mitigate": ("verb", (88, 121), "NO_ENTRY_SPECIFIC_CEFR_LABEL",
                "Oxford records a formal transitive verb", "SENSE_MATCH_CEFR_SOURCE_MISSING"),
    "ubiquitous": ("adjective", (88, 115), "NO_ENTRY_SPECIFIC_CEFR_LABEL",
                  "Oxford describes something apparently everywhere", "REGISTER_AND_CEFR_SOURCE_GAP"),
}
HOLD_FIELDS = ("editorial_hold",)
NO_APPROVAL = ("independent_english_review", "independent_myanmar_review",
               "independent_example_review", "independent_cefr_sense_review",
               "release_approved")
SNAPSHOT_KEYS = ("english_definition", "myanmar_meaning", "example_sentence")


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def validate(packet, shortlist, shortlist_sha, level="ALL"):
    issues = []
    if packet.get("schema") != 1 or packet.get("scope") != "CEFR_1000_TOTAL_STAGING_ONLY":
        issues.append("Wrong source packet schema/scope")
    if packet.get("status") != "EDITORIAL_HOLD_NOT_INDEPENDENTLY_REVIEWED":
        issues.append("Source packet must remain on editorial hold")
    if packet.get("observed_on") != "2026-10-27" or packet.get("shortlist_blob_sha") != shortlist_sha:
        issues.append("Source observation date or original shortlist Git blob SHA drift")
    if packet.get("record_count") != 5 or packet.get("independently_approved_count") != 0:
        issues.append("Wrong five-record source count or fabricated approval")
    if packet.get("counts_by_level") != {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 5}:
        issues.append("Incorrect source counts by level")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000 or shortlist.get("counts_by_level") != dict.fromkeys(LEVELS, 200):
        issues.append("Shortlist scope is not exactly 200 per level")
    by_key = {(e.get("level"), e.get("word")): e for e in entries if isinstance(e, dict)}
    records = packet.get("records", [])
    if not isinstance(records, list) or len(records) != 5:
        issues.append("Missing or additional source records")
        records = records if isinstance(records, list) else []
    seen = set()
    for r in records:
        if not isinstance(r, dict):
            issues.append("Non-object source record")
            continue
        word, lev = r.get("word"), r.get("level")
        if word not in EXPECTED or lev != "C1" or word in seen:
            issues.append("Unknown/duplicated word or wrong shortlist level")
            continue
        seen.add(word)
        e = by_key.get((lev, word))
        if not e:
            issues.append(word + ": missing from canonical shortlist")
            continue
        pos, line_range, scope, anchor, risk = EXPECTED[word]
        snapshot = r.get("shortlist_snapshot", {})
        if r.get("part_of_speech") != pos or e.get("part_of_speech") != pos:
            issues.append(word + ": POS drift")
        if not isinstance(snapshot, dict) or any(
            snapshot.get(k) != e.get("burmese_meaning" if k == "myanmar_meaning" else k)
            for k in SNAPSHOT_KEYS
        ):
            issues.append(word + ": original English/Myanmar/example snapshot drift")
        src = r.get("publisher_source", {})
        if not isinstance(src, dict) or any((
            src.get("url") != "https://www.oxfordlearnersdictionaries.com/definition/english/" + word,
            src.get("publisher") != "Oxford University Press",
            src.get("dictionary") != "Oxford Advanced Learner's Dictionary",
            src.get("observed_on") != "2026-10-27",
            src.get("access") != "DIRECT_PUBLISHER_DICTIONARY_WEB_VIEW",
            src.get("line_range_0_based") != list(line_range),
            src.get("source_word_pos") != pos,
            src.get("cefr_evidence_scope") != scope,
            not isinstance(src.get("observation"), str) or not src["observation"].startswith(anchor),
        )):
            issues.append(word + ": publisher URL, locator, observation or CEFR scope forged/drifted")
        if r.get("editorial_risk") != risk or not isinstance(r.get("independent_reviewer_task"), str) or len(r["independent_reviewer_task"]) < 50:
            issues.append(word + ": reviewer task/risk missing")
        if any(r.get(k) is not True for k in HOLD_FIELDS) or any(r.get(k) is not False for k in NO_APPROVAL) or r.get("independent_reviewer_receipt") is not None:
            issues.append(word + ": false independent approval or removed editorial hold")
        if any(e.get(k) is not False for k in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "release_approved")) or e.get("editorial_hold") is not True:
            issues.append(word + ": canonical shortlist hold changed")
        if word == "meticulous":
            secondary = r.get("additional_publisher_evidence", {})
            if not isinstance(secondary, dict) or any((
                secondary.get("url") != "https://dictionary.cambridge.org/us/dictionary/english/meticulous",
                secondary.get("publisher") != "Cambridge University Press & Assessment",
                secondary.get("observed_on") != "2026-10-27",
                secondary.get("access") != "PUBLISHER_OWNED_SEARCH_INDEXED_PAGE_TEXT_DIRECT_FETCH_403",
                secondary.get("sense_label") != "C2 careful attention to every detail",
                not isinstance(secondary.get("limitation"), str) or len(secondary["limitation"]) < 50,
            )):
                issues.append("meticulous: secondary Cambridge C2 evidence/provenance drift")
    if seen != set(EXPECTED):
        issues.append("Source record identities incomplete")
    return issues


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    packet = json.loads(EVIDENCE.read_text(encoding="utf8"))
    issues = validate(packet, shortlist, blob_sha(raw), a.level)
    if a.self_test:
        cases = [
            ("false approval", lambda x: x["records"][0].update(release_approved=True)),
            ("fabricated reviewer", lambda x: x["records"][0].update(independent_reviewer_receipt={"reviewer_id": "AI"})),
            ("forged source URL", lambda x: x["records"][0]["publisher_source"].update(url="https://example.com/fake")),
            ("forged CEFR scope", lambda x: x["records"][0]["publisher_source"].update(cefr_evidence_scope="PUBLISHER_EXACT_SENSE_C1")),
            ("changed example", lambda x: x["records"][0]["shortlist_snapshot"].update(example_sentence="Unverified replacement.")),
            ("missing word", lambda x: x["records"].pop()),
            ("false Cambridge C1", lambda x: x["records"][0]["additional_publisher_evidence"].update(sense_label="C1")),
            ("removed hold", lambda x: x["records"][0].update(editorial_hold=False)),
            ("source date drift", lambda x: x["records"][0]["publisher_source"].update(observed_on="2026-10-28")),
        ]
        for name, mutate in cases:
            bad = copy.deepcopy(packet)
            mutate(bad)
            if not validate(bad, shortlist, blob_sha(raw), a.level):
                issues.append("Negative test accepted " + name)
    report = {"level": a.level, "observed_on": "2026-10-27",
              "source_observations": 5 if a.level in ("C1", "ALL") else 0,
              "independently_approved": 0,
              "source_scope": "DIRECT_DICTIONARY_SENSE_AND_REGISTER_NOT_CEFR_HUMAN_SIGNOFF",
              "negative_tests_executed": 9 if a.self_test else 0,
              "issues": issues}
    out = ROOT / ("cefr-1000-oxford-c1-five-" + a.level + ".json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        return 1
    print("PASS:", a.level, "direct Oxford C1 leads:", report["source_observations"],
          "independent approvals: 0; negative tests:", report["negative_tests_executed"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
