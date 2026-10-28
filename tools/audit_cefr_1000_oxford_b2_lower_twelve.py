#!/usr/bin/env python3
"""Staging-only provenance/hold auditor for twelve Oxford B2-draft word/POS leads.

Direct Oxford PDF word/POS evidence is NOT independent exact-sense CEFR,
English, Myanmar, example, pronunciation or release approval.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-LOWER-LEVEL-TWELVE-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
STATUS = "DIRECT_OXFORD_B2_DRAFT_WORD_POS_TRIAGE_NOT_INDEPENDENT_APPROVAL"
SCOPE = "OXFORD_3000_WORD_POS_LEVEL_ONLY_NOT_EXACT_SENSE"
EXPECTED = {
    "plastic": ("A2", "n., adj.", 6, 1477),
    "childhood": ("B1", "n.", 7, 1895),
    "weapon": ("B1", "n.", 10, 2567),
    "theatre": ("A1", "n.", 3, 783),
    "sight": ("B1", "n.", 9, 2434),
    "approval": ("B2", "n.", 10, 2630),
    "print": ("B2", "n.", 12, 3092),
    "comedy": ("A2", "n.", 4, 1063),
    "advertising": ("A2", "n.", 4, 924),
    "survive": ("B1", "v.", 10, 2489),
    "comparison": ("B1", "n.", 7, 1915),
    "destroy": ("A2", "v.", 5, 1120),
}
RECORD_KEYS = {
    "word", "level", "part_of_speech", "source_cefr", "source_pos",
    "source_scope", "source_url", "source_authority", "source_document",
    "pdf_page_1_based", "pdf_extracted_line_0_based", "observed_on",
    "source_access", "shortlist_english_definition", "shortlist_myanmar_meaning",
    "shortlist_example", "shortlist_source_path", "shortlist_source_index",
    "shortlist_source_blob_sha", "editorial_risk", "independent_review_task",
    "editorial_hold", "independently_reviewed", "release_approved", "reviewer_receipt"
}
TOP_KEYS = {
    "schema", "scope", "status", "observed_on", "shortlist_blob_sha",
    "source_url", "record_count", "counts_by_level", "word_pos_discrepancies",
    "independently_approved_count", "provenance_note", "records"
}


def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def audit(data, shortlist, raw, level="ALL"):
    errors = []
    if not isinstance(data, dict):
        return ["source packet is not an object"]
    if set(data) != TOP_KEYS:
        errors.append("unexpected or missing top-level fields")
    if data.get("schema") != 1 or data.get("scope") != "CEFR_1000_TOTAL_STAGING_ONLY" or data.get("status") != STATUS:
        errors.append("schema/scope/status drift")
    if data.get("observed_on") != "2026-10-28" or data.get("source_url") != URL:
        errors.append("publisher source/date drift")
    if data.get("shortlist_blob_sha") != git_blob_sha(raw):
        errors.append("canonical shortlist blob mismatch")
    if data.get("record_count") != 12 or data.get("counts_by_level") != dict(A1=0, A2=0, B1=0, B2=12, C1=0):
        errors.append("record or per-level count drift")
    if data.get("word_pos_discrepancies") != 10 or data.get("independently_approved_count") != 0:
        errors.append("discrepancy count or false approval")
    note = str(data.get("provenance_note", ""))
    if not all(s in note.casefold() for s in ("direct official oxford", "not", "independent")):
        errors.append("provenance caveat missing")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000 or shortlist.get("counts_by_level") != {x: 200 for x in ("A1", "A2", "B1", "B2", "C1")}:
        errors.append("canonical 1000/level counts drift")
    lookup = {(x.get("word"), x.get("level")): x for x in entries}
    rows = data.get("records")
    if not isinstance(rows, list):
        return errors + ["records not a list"]
    if len(rows) != 12 or set(r.get("word") for r in rows if isinstance(r, dict)) != set(EXPECTED):
        errors.append("missing, unexpected or duplicate headwords")
    for row in rows:
        if not isinstance(row, dict):
            errors.append("record not object")
            continue
        word = row.get("word")
        if word not in EXPECTED:
            errors.append("unexpected headword " + str(word))
            continue
        expected_cefr, expected_pos, expected_page, expected_line = EXPECTED[word]
        if set(row) != RECORD_KEYS:
            errors.append(word + ": unrecognised or missing record keys")
        if (row.get("level"), row.get("source_cefr"), row.get("source_pos"), row.get("pdf_page_1_based"), row.get("pdf_extracted_line_0_based")) != ("B2", expected_cefr, expected_pos, expected_page, expected_line):
            errors.append(word + ": direct Oxford word/POS/locator drift")
        for k, value in {
            "source_url": URL, "source_scope": SCOPE,
            "source_authority": "Oxford University Press",
            "source_document": "The Oxford 3000 by CEFR level",
            "source_access": "DIRECT_OFFICIAL_OUP_PDF_TEXT",
            "observed_on": "2026-10-28",
            "editorial_hold": True, "independently_reviewed": False,
            "release_approved": False, "reviewer_receipt": None,
        }.items():
            if row.get(k) != value:
                errors.append(word + ": publisher/hold/review drift in " + k)
        entry = lookup.get((word, "B2"))
        if not entry:
            errors.append(word + ": not in B2 shortlist")
            continue
        for k, canonical in {
            "part_of_speech": entry.get("part_of_speech"),
            "shortlist_english_definition": entry.get("english_definition"),
            "shortlist_myanmar_meaning": entry.get("burmese_meaning"),
            "shortlist_example": entry.get("example_sentence"),
            "shortlist_source_path": entry.get("source_path"),
            "shortlist_source_index": entry.get("source_index"),
            "shortlist_source_blob_sha": entry.get("source_blob_sha"),
        }.items():
            if row.get(k) != canonical:
                errors.append(word + ": canonical snapshot drift in " + k)
        if entry.get("editorial_hold") is not True or any(entry.get(k) is not False for k in (
            "reviewed_english", "reviewed_burmese", "reviewed_example",
            "reviewed_level", "reviewed_pronunciation", "release_approved"
        )):
            errors.append(word + ": canonical independent review hold lost")
        if len(str(row.get("editorial_risk", ""))) < 60 or len(str(row.get("independent_review_task", ""))) < 80:
            errors.append(word + ": substantive reviewer instruction missing")
    if level not in ("A1", "A2", "B1", "B2", "C1", "ALL"):
        errors.append("unknown level")
    return errors


def negative_cases(data):
    cases = []
    def change(name, key, value):
        x = copy.deepcopy(data)
        x["records"][0][key] = value
        cases.append((name, x))
    change("invent Oxford B2 label", "source_cefr", "B2")
    change("forge POS", "source_pos", "v.")
    change("forge PDF page", "pdf_page_1_based", 12)
    change("forge PDF line", "pdf_extracted_line_0_based", 9999)
    change("replace publisher", "source_url", "https://example.com")
    change("forge direct access", "source_access", "PUBLISHER_CONFIRMED")
    change("forge source scope", "source_scope", "EXACT_SENSE_VERIFIED")
    change("invent independent approval", "independently_reviewed", True)
    change("invent release approval", "release_approved", True)
    change("invent receipt", "reviewer_receipt", {"approved": True})
    change("remove editorial hold", "editorial_hold", False)
    change("change Myanmar", "shortlist_myanmar_meaning", "တစ်ခုခု")
    change("change English", "shortlist_english_definition", "Unrelated meaning.")
    change("change example", "shortlist_example", "Wrong example.")
    change("change provenance path", "shortlist_source_path", "draft/other.json")
    change("change provenance index", "shortlist_source_index", 100000)
    change("change provenance blob", "shortlist_source_blob_sha", "0" * 40)
    change("remove editorial risk", "editorial_risk", "")
    change("remove review task", "independent_review_task", "")
    change("add unverified field", "independent_human_verified", True)
    x = copy.deepcopy(data); x["records"].append(copy.deepcopy(x["records"][0])); cases.append(("duplicate", x))
    x = copy.deepcopy(data); x["records"].pop(); cases.append(("missing word", x))
    x = copy.deepcopy(data); x["word_pos_discrepancies"] = 0; cases.append(("erase conflicts", x))
    x = copy.deepcopy(data); x["independently_approved_count"] = 12; cases.append(("fake total", x))
    x = copy.deepcopy(data); x["shortlist_blob_sha"] = "0" * 40; cases.append(("fake shortlist hash", x))
    x = copy.deepcopy(data); x["provenance_note"] = ""; cases.append(("erase caveat", x))
    return cases


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=["A1", "A2", "B2", "B2", "C1", "ALL"], default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    errors = audit(packet, shortlist, raw, args.level)
    rejected = 0
    if args.self_test and not errors:
        for name, mutated in negative_cases(packet):
            if not audit(mutated, shortlist, raw, args.level):
                errors.append("mutation wrongly accepted: " + name)
            else:
                rejected += 1
    print(json.dumps({
        "level": args.level, "direct_oxford_B2_draft_observations": 12,
        "lower_word_pos_level_conflicts": 10, "independently_approved": 0,
        "negative_mutations_rejected": rejected, "errors": errors,
        "status": "PASS_STRUCTURE_STILL_HOLD" if not errors else "FAIL"
    }, ensure_ascii=False))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
