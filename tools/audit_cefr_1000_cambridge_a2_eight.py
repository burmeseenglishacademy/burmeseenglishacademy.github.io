#!/usr/bin/env python3
"""Fail-closed provenance and shortlist-snapshot audit for eight A2 Cambridge leads.
Publisher-indexed excerpts are research leads, NEVER independent linguistic signoff.
"""
import argparse
import copy
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "draft/CEFR-1000-CAMBRIDGE-A2-EIGHT-SENSE-LEADS-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "public": ("B1", "https://dictionary.cambridge.org/dictionary/english/public"),
    "system": ("B1 connected equipment; B2 method", "https://dictionary.cambridge.org/us/dictionary/english/system"),
    "support": ("B1", "https://dictionary.cambridge.org/dictionary/english/support"),
    "power": ("B2", "https://dictionary.cambridge.org/dictionary/english/power"),
    "actually": ("A2 IN FACT; B1 SURPRISE", "https://dictionary.cambridge.org/dictionary/english/actually"),
    "however": ("A2", "https://dictionary.cambridge.org/us/dictionary/english/however"),
    "whole": ("A2", "https://dictionary.cambridge.org/dictionary/learner-english/whole"),
    "less": ("A2", "https://dictionary.cambridge.org/dictionary/english/less"),
}
ACCESS = "PUBLISHER_OWNED_SEARCH_INDEXED_PAGE_TEXT_DIRECT_FETCH_HTTP_403"
SCOPE = "PUBLISHER_SEARCH_RESULT_SENSE_LABEL_NOT_INDEPENDENT_HUMAN_REVIEW"


def audit(packet, shortlist):
    issues = []
    raw = SHORTLIST.read_bytes()
    git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()
    if packet.get("shortlist_blob_sha") != git_blob:
        issues.append("Pinned canonical shortlist blob differs")
    if packet.get("scope") != "CEFR_1000_TOTAL_STAGING_ONLY" or packet.get("status") != "A2_CAMBRIDGE_EIGHT_SOURCE_LEADS_EDITORIAL_HOLD":
        issues.append("Scope or staging hold changed")
    if packet.get("observed_on") != "2026-10-28" or packet.get("record_count") != 8 or packet.get("independently_approved_count") != 0:
        issues.append("Date/count/approval claim changed")
    if packet.get("counts_by_level") != {"A1": 0, "A2": 8, "B1": 0, "B2": 0, "C1": 0}:
        issues.append("Per-level source counts changed")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000 or shortlist.get("counts_by_level") != {k: 200 for k in LEVELS}:
        issues.append("Provisional 1000/200 scope changed")
    if shortlist.get("independently_approved_by_level") != {k: 0 for k in LEVELS}:
        issues.append("Independent approvals cannot be inferred from this source audit")
    originals = {(e.get("level"), e.get("word")): e for e in entries if isinstance(e, dict)}
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 8:
        return issues + ["Exactly eight source records required"]
    seen = set()
    for rec in records:
        if not isinstance(rec, dict):
            issues.append("Invalid source record")
            continue
        word = rec.get("word")
        if word not in EXPECTED or word in seen:
            issues.append("Unknown/duplicate headword: " + str(word))
            continue
        seen.add(word)
        expected_cefr, expected_url = EXPECTED[word]
        if rec.get("level") != "A2":
            issues.append(word + ": provisional level drift")
        src = rec.get("publisher_source")
        if not isinstance(src, dict):
            src = {}
        for key, expected in {
            "url": expected_url,
            "source_cefr_level": expected_cefr,
            "observed_on": "2026-10-28",
            "publisher": "Cambridge University Press & Assessment",
            "access": ACCESS,
            "observation_scope": SCOPE,
        }.items():
            if src.get(key) != expected:
                issues.append(word + ": unsupported publisher provenance " + key)
        if not isinstance(src.get("source_sense_heading"), str) or len(src["source_sense_heading"].strip()) < 5:
            issues.append(word + ": missing sense heading")
        if not isinstance(src.get("source_observation"), str) or len(src["source_observation"].strip()) < 30:
            issues.append(word + ": missing source observation")
        original = originals.get(("A2", word))
        if original is None:
            issues.append(word + ": absent from shortlist")
            continue
        snapshot = {
            "english_definition": original.get("english_definition"),
            "myanmar_meaning": original.get("burmese_meaning"),
            "example_sentence": original.get("example_sentence"),
        }
        if rec.get("shortlist_snapshot") != snapshot or rec.get("part_of_speech") != original.get("part_of_speech"):
            issues.append(word + ": original English/Myanmar/example/POS drift")
        if rec.get("editorial_hold") is not True or original.get("editorial_hold") is not True:
            issues.append(word + ": editorial hold removed")
        if rec.get("independently_reviewed") is not False or rec.get("release_approved") is not False or rec.get("independent_reviewer_receipt") is not None:
            issues.append(word + ": fabricated independent review or approval")
        if original.get("release_approved") is not False:
            issues.append(word + ": canonical release flag changed")
        if not rec.get("editorial_risk") or not rec.get("independent_reviewer_task"):
            issues.append(word + ": missing review task")
    if seen != set(EXPECTED):
        issues.append("Missing A2 source headwords")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(SOURCE.read_text(encoding="utf8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf8"))
    issues = audit(packet, shortlist)
    if args.self_test:
        mutants = []
        for field, value in [
            ("independently_reviewed", True),
            ("release_approved", True),
            ("editorial_hold", False),
            ("independent_reviewer_receipt", {"reviewer_id": "FAKE"}),
            ("level", "B1"),
            ("word", "power"),
        ]:
            m = copy.deepcopy(packet)
            m["records"][0][field] = value
            mutants.append(m)
        for field, value in [
            ("url", "https://example.invalid/public"),
            ("source_cefr_level", "A2"),
            ("access", "DIRECT_PUBLISHER_PAGE"),
            ("observation_scope", "INDEPENDENT_HUMAN_REVIEW"),
            ("observed_on", "2026-10-27"),
        ]:
            m = copy.deepcopy(packet)
            m["records"][0]["publisher_source"][field] = value
            mutants.append(m)
        m = copy.deepcopy(packet)
        m["records"][0]["shortlist_snapshot"]["myanmar_meaning"] = "FORGED"
        mutants.append(m)
        for i, mutant in enumerate(mutants):
            if not audit(mutant, shortlist):
                issues.append(f"Negative test {i} failed to reject forged source/review")
        if not issues:
            print("PASS: 12 negative mutations rejected; not independent review")
    count = sum(r.get("level") == args.level for r in packet["records"]) if args.level != "ALL" else len(packet["records"])
    report = {
        "level": args.level, "source_observations": count, "independent_approvals": 0,
        "editorial_hold": count, "source_access": "publisher-indexed only; direct page HTTP 403",
        "independent_human_review": False, "errors": issues,
    }
    (ROOT / f"cefr-1000-cambridge-a2-eight-{args.level}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + chr(10), encoding="utf8")
    print(f"Cambridge A2 eight: {count} source leads, 0 approvals, {len(issues)} errors")
    for issue in issues:
        print("BLOCK:", issue, file=sys.stderr)
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
