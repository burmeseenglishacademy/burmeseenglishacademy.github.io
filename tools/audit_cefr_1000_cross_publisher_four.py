#!/usr/bin/env python3
"""Staging-only four-word Oxford/Cambridge cross-source integrity auditor.

Oxford PDF evidence is word/POS-level; Cambridge indexed snippets are
sense leads, NOT independently reviewed publisher pages. This program
does not approve CEFR, English, Myanmar, examples or publication.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CROSS-PUBLISHER-FOUR-RECONCILIATION-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
SOURCE_PATHS = {
    "cB2": "draft/CEFR-1000-CAMBRIDGE-B2-SIX-SENSE-LEADS-2026-10-28.json",
    "cC1": "draft/CEFR-1000-CAMBRIDGE-C1-TEN-SENSE-LEADS-2026-10-28.json",
    "cX": "draft/CEFR-1000-CAMBRIDGE-CROSSLEVEL-SEVEN-2026-10-28.json",
    "oB2": "draft/CEFR-1000-OXFORD-B2-TWELVE-DIRECT-PDF-2026-10-28.json",
    "oC1": "draft/CEFR-1000-OXFORD-C1-TWELVE-DIRECT-PDF-2026-10-28.json",
}
EXPECTED = {
    "constant": ("B2", "cB2", "oB2", "MIXED_B2_C2_CAMBRIDGE_SENSE_VS_OXFORD_B2_WORD_POS"),
    "personality": ("B2", "cX", "oB2", "CAMBRIDGE_B2_CHARACTER_SENSE_VS_OXFORD_A2_WORD_POS"),
    "neutral": ("C1", "cC1", "oC1", "CAMBRIDGE_C1_IMPARTIALITY_SENSE_VS_OXFORD_B2_WORD_POS"),
    "tribute": ("C1", "cC1", "oC1", "CAMBRIDGE_C2_RESPECT_SENSE_VS_OXFORD_C1_WORD_POS"),
}
LABELS = {
    "constant": ("B2 frequent; C2 staying same", "B2"),
    "personality": ("B2", "A2"),
    "neutral": ("C1", "B2"),
    "tribute": ("C2", "C1"),
}


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()


def source_evidence(key, word, sources):
    path, sha, doc = sources[key]
    rec = next(x for x in doc.get("records", doc.get("entries", [])) if x.get("word") == word)
    src = rec.get("publisher_source") or {}
    return {
        "source_packet_path": path,
        "source_packet_blob_sha": sha,
        "publisher": "Oxford University Press" if key.startswith("o") else "Cambridge University Press & Assessment",
        "source_url": src.get("url") or rec.get("source_url"),
        "source_observed_on": src.get("observed_on") or rec.get("observed_on") or rec.get("source_observed_on"),
        "source_cefr_label": src.get("source_cefr_level") or rec.get("source_cefr") or rec.get("source_cefr_label"),
        "source_sense_heading": src.get("source_sense_heading") or rec.get("sense_heading") or rec.get("source_sense_heading") or "WORD_POS_ONLY",
        "evidence_scope": src.get("evidence_scope") or src.get("observation_scope") or rec.get("provenance_note") or "PUBLISHER_SEARCH_INDEXED_SENSE_LEAD_NOT_INDEPENDENT",
        "access": src.get("access") or rec.get("source_access"),
        "pdf_page": src.get("pdf_page"),
        "extracted_line": src.get("extracted_line"),
        "source_excerpt": src.get("source_excerpt"),
    }


def audit(packet, shortlist, sources):
    issues = []
    raw = SHORTLIST.read_bytes()
    if packet.get("schema") != 1 or packet.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY":
        issues.append("Invalid approved scope or schema")
    if packet.get("status") != "FOUR_CROSS_PUBLISHER_RECONCILIATIONS_PENDING_INDEPENDENT_REVIEW":
        issues.append("Cross-source reconciliation cannot be marked complete")
    if packet.get("observed_on") != "2026-10-28" or packet.get("shortlist_blob_sha") != git_blob_sha(raw):
        issues.append("Unpinned or changed observation date/shortlist")
    if packet.get("record_count") != 4 or packet.get("counts_by_level") != {"A1": 0, "A2": 0, "B1": 0, "B2": 2, "C1": 2}:
        issues.append("Four-record level coverage changed")
    if packet.get("independently_approved_count") != 0:
        issues.append("Fabricated independent approval count")
    if (len(shortlist.get("entries", [])) != 1000 or
            shortlist.get("counts_by_level") != {k: 200 for k in LEVELS} or
            shortlist.get("independently_approved_by_level") != {k: 0 for k in LEVELS}):
        issues.append("1000-word scope or independent-review hold changed")
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != 4:
        return issues + ["Exactly four cross-publisher review records required"]
    originals = {(x.get("word"), x.get("level")): x for x in shortlist["entries"]}
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            issues.append("Malformed cross-source record")
            continue
        word = row.get("word")
        if word not in EXPECTED or word in seen:
            issues.append("Duplicate or unexpected cross-source word " + str(word))
            continue
        seen.add(word)
        level, cam, ox, classification = EXPECTED[word]
        original = originals.get((word, level))
        if not original:
            issues.append(word + ": missing canonical word/level")
            continue
        snapshot = {"english_definition": original.get("english_definition"),
                    "myanmar_meaning": original.get("burmese_meaning"),
                    "example_sentence": original.get("example_sentence")}
        if (row.get("level") != level or row.get("part_of_speech") != original.get("part_of_speech")
                or row.get("shortlist_snapshot") != snapshot):
            issues.append(word + ": English/Myanmar/example/POS snapshot drift")
        if row.get("classification") != classification:
            issues.append(word + ": risk classification changed")
        if (not isinstance(row.get("discrepancy"), str) or len(row["discrepancy"].strip()) < 90
                or "Oxford" not in row["discrepancy"] or "Cambridge" not in row["discrepancy"]
                or not isinstance(row.get("independent_reviewer_task"), str)
                or len(row["independent_reviewer_task"].strip()) < 95):
            issues.append(word + ": insufficient editorial discrepancy/review task")
        if (row.get("editorial_hold") is not True or row.get("independently_reviewed") is not False
                or row.get("release_approved") is not False or row.get("reviewer_receipt") is not None
                or original.get("editorial_hold") is not True or original.get("release_approved") is not False):
            issues.append(word + ": fabricated approval or lifted hold")
        try:
            expected_evidence = [source_evidence(cam, word, sources), source_evidence(ox, word, sources)]
        except (StopIteration, KeyError, TypeError):
            issues.append(word + ": missing upstream publisher source record")
            continue
        if row.get("publisher_evidence") != expected_evidence:
            issues.append(word + ": source URL, date, level, scope, PDF locator or packet SHA drift")
        if tuple(x.get("source_cefr_label") for x in expected_evidence) != LABELS[word]:
            issues.append(word + ": expected publisher evidence labels drift")
        for evidence in expected_evidence:
            url = urlparse(evidence["source_url"] or "")
            if url.scheme != "https" or url.hostname not in (
                    "dictionary.cambridge.org", "www.oxfordlearnersdictionaries.com"):
                issues.append(word + ": source is not approved publisher URL")
            if evidence["source_observed_on"] != "2026-10-28":
                issues.append(word + ": source observation date changed")
            if evidence["publisher"].startswith("Oxford"):
                if (evidence["evidence_scope"] != "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"
                        or not isinstance(evidence["pdf_page"], int)
                        or not isinstance(evidence["extracted_line"], int)):
                    issues.append(word + ": Oxford PDF word/POS scope or locator invalid")
            else:
                if (evidence["pdf_page"] is not None
                        or "403" not in str(evidence["access"])
                        or "DIRECT_PUBLISHER_DICTIONARY_PAGE" == evidence["evidence_scope"]):
                    issues.append(word + ": Cambridge indexed-only access misrepresented")
    if seen != set(EXPECTED):
        issues.append("Missing cross-source reconciliation words")
    return issues


def negative_tests(packet, shortlist, sources):
    mutants = []
    for key, value in (
        ("editorial_hold", False), ("independently_reviewed", True),
        ("release_approved", True), ("reviewer_receipt", {"reviewer_id": "FAKE"}),
        ("word", "be"), ("level", "A1"), ("classification", "RESOLVED"),
    ):
        obj = copy.deepcopy(packet)
        obj["records"][0][key] = value
        mutants.append(obj)
    for key, value in (
        ("source_url", "https://example.com/fake"),
        ("source_cefr_label", "C1"),
        ("source_packet_blob_sha", "0" * 40),
        ("evidence_scope", "DIRECT_PUBLISHER_DICTIONARY_PAGE"),
        ("source_observed_on", "2026-10-29"),
        ("pdf_page", 99),
    ):
        obj = copy.deepcopy(packet)
        obj["records"][0]["publisher_evidence"][1][key] = value
        mutants.append(obj)
    for key in ("english_definition", "burmese_meaning", "example_sentence"):
        obj = copy.deepcopy(packet)
        obj["records"][0]["shortlist_snapshot"][key] = "forged"
        mutants.append(obj)
    obj = copy.deepcopy(packet)
    obj["records"][1] = copy.deepcopy(obj["records"][0])
    mutants.append(obj)
    for n, obj in enumerate(mutants):
        if not audit(obj, shortlist, sources):
            raise AssertionError("Cross-source fail-closed mutation escaped: " + str(n))
    return len(mutants)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text("utf8"))
    shortlist = json.loads(SHORTLIST.read_text("utf8"))
    sources = {}
    for key, path in SOURCE_PATHS.items():
        raw = (ROOT / path).read_bytes()
        sources[key] = (path, git_blob_sha(raw), json.loads(raw))
    issues = audit(packet, shortlist, sources)
    tested = 0
    if args.self_test and not issues:
        tested = negative_tests(packet, shortlist, sources)
    count = sum(x.get("level") == args.level or args.level == "ALL" for x in packet["records"])
    report = {
        "level": args.level, "cross_publisher_reconciliation_holds": count,
        "independently_resolved": 0, "independently_approved": 0,
        "evidence_scope": "Oxford direct PDF word/POS versus Cambridge indexed sense leads; no independent signoff",
        "negative_mutations_rejected": tested,
        "status": "PASS_STRUCTURE_STILL_EDITORIAL_HOLD" if not issues else "FAIL",
        "errors": issues,
    }
    (ROOT / ("cefr-1000-cross-publisher-four-" + args.level + ".json")).write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
