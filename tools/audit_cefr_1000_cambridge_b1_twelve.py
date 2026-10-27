#!/usr/bin/env python3
"""Structural provenance audit of twelve B1 Cambridge sense leads, not linguistic signoff."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-B1-TWELVE-SENSE-LEADS-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
ACCESS = "PUBLISHER_OWNED_SEARCH_INDEXED_PAGE_TEXT_DIRECT_FETCH_HTTP_403"
SCOPE = "PUBLISHER_SEARCH_RESULT_SENSE_LABEL_NOT_INDEPENDENT_HUMAN_REVIEW"
EXPECTED = {
    "independent": ("B2", "us/dictionary/english/independent"),
    "impact": ("B2", "us/dictionary/english/impact"),
    "effective": ("B2", "us/dictionary/english/effective"),
    "analysis": ("B2", "dictionary/english/analysis"),
    "complex": ("B2", "dictionary/english/complex"),
    "critical": ("B2", "dictionary/english/critical"),
    "necessary": ("B1", "dictionary/english/necessary"),
    "equipment": ("B1", "us/dictionary/learner-english/equipment"),
    "application": ("B1", "dictionary/learner-english/application"),
    "purpose": ("B1", "dictionary/learner-english/purpose"),
    "solution": ("B1", "dictionary/learner-english/solution"),
    "otherwise": ("B1", "dictionary/english/otherwise"),
}
# Pin the exact publisher-indexed observation and heading; prevent silent drift.
# These are human-readable search-result observations, NOT independent review.
EXPECTED_TEXT = {
    "independent": [
        "adjective (NOT INFLUENCED / NOT RULED)",
        "Cambridge marks freedom from another person's control or influence B2, while B1 is not needing help. The B1 draft's independent decision uses autonomy from control, not self-sufficiency."
    ],
    "impact": [
        "noun (EFFECT)",
        "Cambridge labels a strong effect on a person or situation B2; the draft policy's impact on businesses is that effect, not physical collision."
    ],
    "effective": [
        "adjective (SUCCESSFUL)",
        "Cambridge labels achieving a desired result B2; the draft describes regular practice as a successful method."
    ],
    "analysis": [
        "noun (DETAILED EXAMINATION)",
        "Cambridge labels the careful examination of information B2; the survey-results example uses this detailed-study sense."
    ],
    "complex": [
        "adjective (MANY CONNECTED PARTS / HARD TO UNDERSTAND)",
        "Cambridge labels both many-related-parts and difficult-to-understand adjective senses B2; the draft combines these two related B2 aspects."
    ],
    "critical": [
        "adjective (IMPORTANT)",
        "Cambridge labels the extremely-important adjective sense B2; draft emergency-water example is about importance, not critical illness or negative criticism."
    ],
    "necessary": [
        "adjective (NEEDED)",
        "Cambridge labels required-for-a-result adjective B1; the draft question about whether a ticket is needed matches."
    ],
    "equipment": [
        "noun (TOOLS FOR AN ACTIVITY; UNCOUNTABLE)",
        "Cambridge labels the collective uncountable tools/gear noun B1; draft safety-equipment use fits and does not pluralise equipment."
    ],
    "application": [
        "noun (FORMAL REQUEST)",
        "Cambridge labels the formal request noun B1, while computer-program sense is B2 in the Learner's Dictionary; draft submit-your-application context is a request."
    ],
    "purpose": [
        "noun (REASON)",
        "Cambridge Learner's Dictionary labels why something is done B1; draft meeting's purpose is this reason, not the 'on purpose' idiom."
    ],
    "solution": [
        "noun (ANSWER TO A PROBLEM)",
        "Cambridge labels answer-to-a-problem B1; draft waste-reduction proposal uses this sense, not the chemical-mixture sense."
    ],
    "otherwise": [
        "conjunction (IF NOT / OR ELSE); adverb (EXCEPT) B2",
        "Cambridge labels the conditional result after a command or suggestion as B1 under conjunction; draft uses 'Leave now; otherwise, you may miss the train' but records part_of_speech as adverb. Its separately labelled adverb 'except' sense is B2."
    ]
}
EXPECTED_STATUS = "B1_TWELVE_PUBLISHER_INDEXED_SENSE_LEADS_EDITORIAL_HOLD"

def audit(packet, shortlist):
    issues = []
    raw = SHORTLIST.read_bytes()
    git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if packet.get("shortlist_blob_sha") != git_blob:
        issues.append("Canonical shortlist Git blob binding failed")
    if packet.get("scope") != "CEFR_1000_TOTAL_STAGING_ONLY" or packet.get("status") != EXPECTED_STATUS:
        issues.append("Scope or staging-only status drift")
    if packet.get("observed_on") != "2026-10-28" or packet.get("record_count") != 12 or packet.get("independently_approved_count") != 0:
        issues.append("Observed date/count or zero-approval invariant drift")
    if packet.get("counts_by_level") != dict.fromkeys(LEVELS, 0) | {"B1": 12}:
        issues.append("B1 evidence per-level counts drift")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000 or shortlist.get("counts_by_level") != dict.fromkeys(LEVELS, 200):
        issues.append("1000-entry 200-per-level provisional scope drift")
    if shortlist.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        issues.append("Provisional shortlist falsely claims independent approvals")
    lookup = {(e.get("level"), e.get("word")): e for e in entries if isinstance(e, dict)}
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 12:
        return issues + ["Exactly twelve B1 records required"]
    seen = set()
    for rec in records:
        if not isinstance(rec, dict):
            issues.append("Malformed record")
            continue
        word = rec.get("word")
        if word not in EXPECTED or word in seen:
            issues.append("Unknown or duplicate headword " + str(word))
            continue
        seen.add(word)
        cefr, urlpath = EXPECTED[word]
        src = rec.get("publisher_source")
        if not isinstance(src, dict):
            src = {}
        for field, expected in {
            "url": "https://dictionary.cambridge.org/" + urlpath,
            "source_cefr_level": cefr,
            "observed_on": "2026-10-28",
            "publisher": "Cambridge University Press & Assessment",
            "access": ACCESS,
            "observation_scope": SCOPE,
        }.items():
            if src.get(field) != expected:
                issues.append(word + ": provenance drift in " + field)
        if [src.get("source_sense_heading"), src.get("source_observation")] != EXPECTED_TEXT[word]:
            issues.append(word + ": source observation/heading changed without re-evidence")
        if not isinstance(src.get("source_sense_heading"), str) or len(src["source_sense_heading"].strip()) < 8:
            issues.append(word + ": missing sense heading")
        if not isinstance(src.get("source_observation"), str) or len(src["source_observation"].strip()) < 35:
            issues.append(word + ": missing source observation")
        original = lookup.get(("B1", word))
        if original is None:
            issues.append(word + ": not in B1 shortlist")
            continue
        snapshot = {
            "english_definition": original.get("english_definition"),
            "myanmar_meaning": original.get("burmese_meaning"),
            "example_sentence": original.get("example_sentence"),
        }
        if rec.get("shortlist_snapshot") != snapshot or rec.get("part_of_speech") != original.get("part_of_speech") or rec.get("level") != "B1":
            issues.append(word + ": original bilingual/POS/level snapshot drift")
        if rec.get("editorial_hold") is not True or original.get("editorial_hold") is not True:
            issues.append(word + ": editorial hold removed")
        if rec.get("independently_reviewed") is not False or rec.get("release_approved") is not False or rec.get("independent_reviewer_receipt") is not None or original.get("release_approved") is not False:
            issues.append(word + ": fabricated independent review or release approval")
        if not isinstance(rec.get("editorial_risk"), str) or len(rec["editorial_risk"]) < 8:
            issues.append(word + ": missing editorial risk")
        if not isinstance(rec.get("independent_reviewer_task"), str) or len(rec["independent_reviewer_task"]) < 40:
            issues.append(word + ": missing independent reviewer task")
    if seen != set(EXPECTED):
        issues.append("Missing B1 source headwords")
    return issues

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    issues = audit(packet, shortlist)
    if args.self_test:
        mutations = []
        for field, value in (
            ("independently_reviewed", True), ("release_approved", True),
            ("editorial_hold", False), ("independent_reviewer_receipt", {"reviewer_id": "fake"}),
            ("level", "B2"), ("part_of_speech", "noun"),
        ):
            m = copy.deepcopy(packet)
            m["records"][0][field] = value
            mutations.append(m)
        for field, value in (
            ("url", "https://example.invalid/independent"), ("source_cefr_level", "B1"),
            ("access", "DIRECT_PUBLISHER_DICTIONARY_PAGE"),
            ("observation_scope", "INDEPENDENT_HUMAN_REVIEW"),
            ("observed_on", "2026-10-27"),
        ):
            m = copy.deepcopy(packet)
            m["records"][0]["publisher_source"][field] = value
            mutations.append(m)
        m = copy.deepcopy(packet)
        m["records"][0]["shortlist_snapshot"]["myanmar_meaning"] = "FORGED"
        mutations.append(m)
        m = copy.deepcopy(packet)
        m["records"][0]["publisher_source"]["source_observation"] = ""
        mutations.append(m)
        m = copy.deepcopy(packet)
        m["records"][0]["publisher_source"]["source_observation"] += " invented unsupported CEFR statement"
        mutations.append(m)
        for index, mutation in enumerate(mutations):
            if not audit(mutation, shortlist):
                issues.append("Negative mutation " + str(index) + " escaped audit")
        if not issues:
            print("PASS: 14 negative mutations rejected; no human review implied")
    count = len(packet["records"]) if args.level == "ALL" else sum(r["level"] == args.level for r in packet["records"])
    report = {"level": args.level, "publisher_indexed_source_leads": count,
              "independently_approved": 0, "source_access": "search-indexed; direct page HTTP 403",
              "human_review": False, "issues": issues}
    (ROOT / ("cefr-1000-cambridge-b1-twelve-" + args.level + ".json")).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("B1 Cambridge twelve:", count, "source leads, 0 independent approvals,", len(issues), "errors")
    for issue in issues:
        print("BLOCK:", issue, file=sys.stderr)
    return int(bool(issues))

if __name__ == "__main__":
    raise SystemExit(main())
