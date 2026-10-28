#!/usr/bin/env python3
"""Fail-closed staging integrity audit for six C1 publisher-indexed sense leads.
This is a structural provenance audit, NOT independent linguistic review.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-C1-SIX-FOLLOWUP-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
OXFORD = ROOT / "draft/CEFR-1000-OXFORD-C1-TWELVE-DIRECT-PDF-2026-10-28.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "signature": ("B1", "NAME", "C1_DRAFT_CAMBRIDGE_B1_EXACT_SENSE_OXFORD_B2_WORD_POS", "B2"),
    "conversion": ("C2", "CHANGE", "C1_DRAFT_CAMBRIDGE_C2_CHANGE_SENSE_OXFORD_C1_WORD_POS", "C1"),
    "municipal": ("C1", "CITY_OR_TOWN", "C1_PUBLISHER_SUPPORT_STILL_REQUIRES_MYANMAR_AND_SENSE_REVIEW", "C1"),
    "copyright": ("UNLABELLED", "LEGAL_RIGHT", "OXFORD_C1_WORD_POS_CAMBRIDGE_NO_VISIBLE_CEFR_EXACT_SENSE", "C1"),
    "functional": ("B2_USEFUL;WORKING_NORMALLY_UNLABELLED", "USEFUL_VS_WORKING_NORMALLY", "C1_DRAFT_USES_UNLABELLED_WORKING_SENSE_NOT_CAMBRIDGE_B2_USEFUL_SENSE", None),
    "naval": ("C2", "NAVY_MILITARY_SHIPS", "C1_DRAFT_CAMBRIDGE_C2_SAME_SENSE", None),
}

def git_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()

def audit(packet, shortlist, oxford, shortlist_sha, oxford_sha):
    issues = []
    if (packet.get("schema") != 1 or packet.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY"
            or packet.get("status") != "SIX_C1_CAMBRIDGE_EXACT_SENSE_LEADS_PENDING_INDEPENDENT_REVIEW"
            or packet.get("observed_on") != "2026-10-28"
            or packet.get("shortlist_blob_sha") != shortlist_sha
            or packet.get("record_count") != 6
            or packet.get("counts_by_level") != dict.fromkeys(LEVELS, 0) | {"C1": 6}
            or packet.get("independently_approved_count") != 0):
        issues.append("Scope, provenance, counts, status or independent approval claim changed")
    if (len(shortlist.get("entries", [])) != 1000
            or shortlist.get("counts_by_level") != dict.fromkeys(LEVELS, 200)
            or shortlist.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0)):
        issues.append("Canonical 1000 shortlist or hold counts changed")
    if ("403" not in str(packet.get("source_limitations"))
            or "not exact-sense" not in str(packet.get("source_limitations"))):
        issues.append("Source access limitations missing")
    rows = packet.get("records")
    if not isinstance(rows, list) or len(rows) != 6:
        return issues + ["Exactly six records required"]
    originals = {(x["word"], x["level"]): x for x in shortlist["entries"]}
    oxrows = {x["word"]: x for x in oxford["records"]}
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            issues.append("Malformed record")
            continue
        word = row.get("word")
        if word not in EXPECTED or word in seen:
            issues.append("Unexpected or duplicated word")
            continue
        seen.add(word)
        label, heading, risk, oxlabel = EXPECTED[word]
        original = originals.get((word, "C1"))
        if original is None:
            issues.append(word + ": not in C1 canonical shortlist")
            continue
        snap = {k: original[k] for k in ("english_definition", "example_sentence")}
        snap["myanmar_meaning"] = original["burmese_meaning"]
        if (row.get("level") != "C1" or row.get("part_of_speech") != original["part_of_speech"]
                or row.get("shortlist_snapshot") != snap or row.get("classification") != risk):
            issues.append(word + ": original English/Myanmar/example/POS/risk drift")
        if (row.get("editorial_hold") is not True
                or row.get("independently_reviewed") is not False
                or row.get("release_approved") is not False
                or row.get("reviewer_receipt") is not None
                or original.get("editorial_hold") is not True
                or original.get("release_approved") is not False):
            issues.append(word + ": forged approval or lifted editorial hold")
        if (len(str(row.get("editorial_analysis", ""))) < 85
                or len(str(row.get("independent_reviewer_task", ""))) < 120
                or "Independently" not in row.get("independent_reviewer_task", "")):
            issues.append(word + ": insufficient sense/translation/grammar review task")
        evidence = row.get("publisher_evidence")
        if not isinstance(evidence, list) or len(evidence) != (2 if oxlabel else 1):
            issues.append(word + ": missing or added publisher evidence")
            continue
        cam = evidence[0]
        if (cam.get("publisher") != "Cambridge University Press & Assessment"
                or cam.get("url") != "https://dictionary.cambridge.org/dictionary/english/" + word
                or cam.get("observed_on") != "2026-10-28"
                or cam.get("cefr_label") != label or cam.get("sense_heading") != heading
                or cam.get("access") != "PUBLISHER_SEARCH_INDEXED_RESULT_DIRECT_PAGE_HTTP_403"
                or cam.get("evidence_scope") != "PUBLISHER_INDEXED_SENSE_LEAD_NOT_INDEPENDENT_FULL_PAGE_REVIEW"):
            issues.append(word + ": forged Cambridge URL, exact-sense label, scope or access")
        if oxlabel:
            ox = oxrows.get(word, {}).get("publisher_source", {})
            expected = {
                "publisher": "Oxford University Press",
                "url": ox.get("url"),
                "observed_on": ox.get("observed_on"),
                "cefr_label": ox.get("source_cefr_level"),
                "sense_heading": "WORD_POS_ONLY",
                "access": ox.get("access"),
                "evidence_scope": ox.get("evidence_scope"),
                "pdf_page": ox.get("pdf_page"),
                "extracted_line": ox.get("extracted_line"),
                "source_excerpt": ox.get("source_excerpt"),
                "upstream_packet_path": "draft/CEFR-1000-OXFORD-C1-TWELVE-DIRECT-PDF-2026-10-28.json",
                "upstream_packet_blob_sha": oxford_sha,
            }
            if evidence[1] != expected or ox.get("source_cefr_level") != oxlabel:
                issues.append(word + ": Oxford PDF word/POS locator, label or packet hash changed")
            if urlparse(str(ox.get("url"))).hostname != "www.oxfordlearnersdictionaries.com":
                issues.append(word + ": Oxford publisher host invalid")
    if seen != set(EXPECTED):
        issues.append("Missing six required source leads")
    return issues

def negative_tests(packet, shortlist, oxford, shortsha, oxsha):
    mutants = []
    for key, value in (("word", "fake"), ("level", "B2"), ("classification", "RESOLVED"),
                       ("editorial_hold", False), ("independently_reviewed", True),
                       ("release_approved", True), ("reviewer_receipt", {"fake": True}),
                       ("editorial_analysis", "OK"), ("independent_reviewer_task", "OK")):
        p = copy.deepcopy(packet)
        p["records"][0][key] = value
        mutants.append(p)
    for key, value in (("url", "https://example.org/forged"),
                       ("cefr_label", "C1"), ("observed_on", "2026-10-29"),
                       ("access", "DIRECT_PAGE_REVIEWED"),
                       ("evidence_scope", "INDEPENDENTLY_APPROVED")):
        p = copy.deepcopy(packet)
        p["records"][0]["publisher_evidence"][0][key] = value
        mutants.append(p)
    for key in ("english_definition", "myanmar_meaning", "example_sentence"):
        p = copy.deepcopy(packet)
        p["records"][0]["shortlist_snapshot"][key] = "forged"
        mutants.append(p)
    for key, value in (("source_excerpt", "forged"), ("upstream_packet_blob_sha", "0" * 40)):
        p = copy.deepcopy(packet)
        p["records"][0]["publisher_evidence"][1][key] = value
        mutants.append(p)
    p = copy.deepcopy(packet)
    p["records"][1] = copy.deepcopy(p["records"][0])
    mutants.append(p)
    for index, mutant in enumerate(mutants):
        if not audit(mutant, shortlist, oxford, shortsha, oxsha):
            raise AssertionError("False-approval/provenance mutation escaped: " + str(index))
    return len(mutants)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist_raw = SHORTLIST.read_bytes()
    oxford_raw = OXFORD.read_bytes()
    shortlist = json.loads(shortlist_raw)
    oxford = json.loads(oxford_raw)
    issues = audit(packet, shortlist, oxford, git_sha(shortlist_raw), git_sha(oxford_raw))
    tested = negative_tests(packet, shortlist, oxford, git_sha(shortlist_raw), git_sha(oxford_raw)) if args.self_test and not issues else 0
    count = sum(x.get("level") == args.level or args.level == "ALL" for x in packet["records"])
    result = {"level": args.level, "publisher_indexed_C1_sense_leads": count,
              "independently_approved": 0, "negative_mutations_rejected": tested,
              "status": "PASS_STRUCTURE_STILL_EDITORIAL_HOLD" if not issues else "FAIL",
              "errors": issues}
    (ROOT / ("cefr-1000-cambridge-c1-six-followup-" + args.level + ".json")).write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    if issues:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
