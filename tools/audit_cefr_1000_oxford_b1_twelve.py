#!/usr/bin/env python3
"""Fail-closed B1-draft direct Oxford PDF word/POS provenance audit; NOT independent review.

The observed publisher PDF supplies A1/A2/B1 word/POS evidence only, never proof
of exact sense, Burmese accuracy, original example grammar or real human QA.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-TWELVE-DIRECT-PDF-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
EXPECTED = {
    "direction": (5, 1128, "direction n.", "A2"),
    "weekend": (4, 869, "weekend n.", "A1"),
    "wonder": (10, 2580, "wonder v., n.", "B1"),
    "cash": (4, 1028, "cash n.", "A2"),
    "clearly": (4, 1050, "clearly adv.", "A2"),
    "effort": (8, 2008, "effort n.", "B1"),
    "imagine": (2, 391, "imagine v.", "A1"),
    "ship": (6, 1608, "ship n.", "A2"),
    "band": (1, 61, "band n.", "A1"),
    "fan": (5, 1198, "fan n.", "A2"),
    "none": (6, 1423, "none pron.", "A2"),
    "lack": (8, 2174, "lack n., v.", "B1"),
}
ACCESS = "DIRECT_OFFICIAL_PDF_WEB_TEXT"
SCOPE = "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"

def audit(packet, shortlist):
    issues = []
    raw = SHORTLIST.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
    if packet.get("shortlist_blob_sha") != blob:
        issues.append("Pinned shortlist Git blob mismatch")
    if packet.get("scope") != "CEFR_1000_TOTAL_STAGING_ONLY" or packet.get("status") != "B1_OXFORD_TWELVE_DIRECT_PDF_WORD_POS_LEADS_EDITORIAL_HOLD":
        issues.append("Wrong scope/status")
    if packet.get("observed_on") != "2026-10-28" or packet.get("record_count") != 12 or packet.get("independently_approved_count") != 0:
        issues.append("Observation metadata/count/approval drift")
    if packet.get("counts_by_level") != dict(zip(LEVELS, (0, 0, 12, 0, 0))):
        issues.append("Incorrect per-level observation counts")
    if shortlist.get("counts_by_level") != {level: 200 for level in LEVELS} or len(shortlist.get("entries", [])) != 1000:
        issues.append("Provisional 1000 / 200 per-level quota changed")
    if shortlist.get("independently_approved_by_level") != {level: 0 for level in LEVELS}:
        issues.append("Canonical independent approval flags changed")
    if packet.get("publisher_reference_level_counts") != {"A1": 3, "A2": 6, "B1": 3}:
        issues.append("Incorrect publisher reference-level counts")
    originals = {(e.get("level"), e.get("word")): e for e in shortlist.get("entries", []) if isinstance(e, dict)}
    records = packet.get("records")
    if not isinstance(records, list) or len(records) != 12:
        return issues + ["Expected exactly twelve B1-draft records"]
    seen = set()
    for record in records:
        if not isinstance(record, dict):
            issues.append("Invalid record type")
            continue
        word = record.get("word")
        if word not in EXPECTED or word in seen:
            issues.append("Unknown/duplicate word: " + str(word))
            continue
        seen.add(word)
        original = originals.get(("B1", word))
        if original is None:
            issues.append(word + ": missing canonical B1 entry")
            continue
        expected_snapshot = {
            "english_definition": original.get("english_definition"),
            "myanmar_meaning": original.get("burmese_meaning"),
            "example_sentence": original.get("example_sentence"),
        }
        if record.get("level") != "B1" or record.get("part_of_speech") != original.get("part_of_speech"):
            issues.append(word + ": draft level/POS mismatch")
        if record.get("shortlist_snapshot") != expected_snapshot:
            issues.append(word + ": English/Myanmar/example snapshot changed")
        src = record.get("publisher_source")
        if not isinstance(src, dict):
            src = {}
        page, line, excerpt, source_level = EXPECTED[word]
        expected = {
            "publisher": "Oxford University Press",
            "title": "The Oxford 3000 by CEFR level",
            "url": URL,
            "observed_on": "2026-10-28",
            "pdf_page": page,
            "extracted_line": line,
            "source_excerpt": excerpt,
            "source_cefr_level": source_level,
            "evidence_scope": SCOPE,
            "access": ACCESS,
        }
        for key, value in expected.items():
            if src.get(key) != value:
                issues.append(word + ": ungrounded/changed source " + key)
        if original.get("editorial_hold") is not True or record.get("editorial_hold") is not True:
            issues.append(word + ": editorial hold lifted")
        if (record.get("independently_reviewed") is not False
                or record.get("release_approved") is not False
                or record.get("independent_reviewer_receipt") is not None
                or original.get("release_approved") is not False):
            issues.append(word + ": fabricated approval/review")
        if (not isinstance(record.get("editorial_risk"), str)
                or not isinstance(record.get("independent_reviewer_task"), str)
                or len(record["editorial_risk"].strip()) < 5
                or len(record["independent_reviewer_task"].strip()) < 25):
            issues.append(word + ": inadequate editorial risk/reviewer task")
        if not record.get("editorial_risk") or not record.get("independent_reviewer_task"):
            issues.append(word + ": missing risk or independent task")
    if seen != set(EXPECTED):
        issues.append("B1 draft direct PDF observation records missing")
    return issues

def negative_tests(packet, shortlist):
    mutants = []
    for field, value in [
        ("editorial_hold", False), ("independently_reviewed", True),
        ("release_approved", True), ("independent_reviewer_receipt", {"reviewer_id": "invented"}),
        ("level", "A1"), ("word", "be"), ("part_of_speech", "verb"),
    ]:
        mutant = copy.deepcopy(packet)
        mutant["records"][0][field] = value
        mutants.append(mutant)
    for field, value in [
        ("url", "https://example.invalid/wordlist.pdf"),
        ("source_excerpt", "i pron."),
        ("pdf_page", 99), ("extracted_line", 2),
        ("source_cefr_level", "C1"), ("evidence_scope", "INDEPENDENT_REVIEW"),
        ("access", "DIRECT_SENSE_REVIEW"),
    ]:
        mutant = copy.deepcopy(packet)
        mutant["records"][0]["publisher_source"][field] = value
        mutants.append(mutant)
    mutant = copy.deepcopy(packet)
    mutant["records"][0]["shortlist_snapshot"]["burmese_meaning"] = "FORGED"
    mutants.append(mutant)
    return [f"Negative mutation {i} escaped validation" for i, mutant in enumerate(mutants)
            if not audit(mutant, shortlist)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    issues = audit(packet, shortlist)
    if args.self_test:
        issues.extend(negative_tests(packet, shortlist))
    count = 12 if args.level in ("B1", "ALL") else 0
    report = {
        "level": args.level, "direct_pdf_word_pos_observations": count,
        "independent_approvals": 0, "editorial_hold": count,
        "exact_sense_verified": False, "human_review_verified": False,
        "source": URL, "errors": issues,
    }
    (ROOT / f"cefr-1000-oxford-b1-twelve-{args.level}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Oxford B1-draft direct PDF: {count} word/POS observations; 0 approvals; {len(issues)} errors")
    for issue in issues:
        print("BLOCK:", issue, file=sys.stderr)
    if args.self_test and not issues:
        print("PASS: 15 tamper/fake-signoff mutations rejected; no linguistic approval inferred")
    return int(bool(issues))

if __name__ == "__main__":
    raise SystemExit(main())
