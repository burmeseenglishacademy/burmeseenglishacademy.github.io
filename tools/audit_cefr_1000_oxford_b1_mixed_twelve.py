#!/usr/bin/env python3
"""Staging-only provenance/hold auditor for twelve mixed Oxford B1-draft word/POS observations.

Direct Oxford PDF word/POS evidence is NOT independent exact-sense CEFR,
English, Myanmar, example, pronunciation or release approval.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B1-MIXED-TWELVE-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
STATUS = "DIRECT_OXFORD_B1_MIXED_LEVEL_TRIAGE_NOT_INDEPENDENT_APPROVAL"
SCOPE = "OXFORD_3000_WORD_POS_LEVEL_ONLY_NOT_EXACT_SENSE"
EXPECTED = {
    "independent": ("A2", "adj.", 5, 1301, "Oxford places the ordinary not-controlled-by-another adjective at A2; the B1 draft appears to teach the same sense. Require independent exact-sense evidence or replace/retier; do not infer B1 from a business example."),
    "impact": ("B1", "n., v.", 8, 2136, "Oxford B1 noun/verb label aligns at word/POS level, but the draft's strong-effect noun sense and policy example still require independent exact-sense, Myanmar and original-example review."),
    "cancer": ("B2", "n.", 10, 2679, "Oxford places cancer at B2, above the provisional B1 assignment. The illness definition is medically sensitive and must be checked for accuracy and appropriate Myanmar phrasing, without automatically downgrading publisher evidence."),
    "civil": ("B2", "adj.", 10, 2695, "Oxford places civil at B2, above the B1 draft. Civil rights and civilian-versus-military uses may diverge; require a human to reconcile the actual rights example with the military-related definition."),
    "organization": ("A2", "n.", 6, 1439, "Oxford places organization at A2, below the B1 draft. The generic group-of-people meaning appears ordinary; also review British spelling organisation versus American organization for British voice and curriculum consistency."),
    "multiple": ("B2", "adj.", 11, 3016, "Oxford places multiple at B2, above the B1 draft, despite the simple more-than-one definition. Require independently observed exact-sense B1 evidence or select a better-supported B1 word."),
    "operation": ("B1", "n.", 9, 2252, "Oxford B1 noun label matches the draft, but the warehouse business-activity example must be distinguished from the surgical operation sense; Myanmar wording should remain specific to the intended sense."),
    "disease": ("A2", "n.", 5, 1136, "Oxford places disease at A2, below the provisional B1. Generic illness definition and spread example do not alone substantiate B1; independently check the health terminology and Myanmar naturalness."),
    "notice": ("A2", "v., n.", 6, 1426, "Oxford places notice noun/verb at A2, below provisional B1. The draft uses the written-announcement noun rather than noticing as a verb; independently establish the sense and any B1-specific justification."),
    "basic": ("B1", "adj.", 7, 1844, "Oxford B1 adjective label matches, but the definition simple-or-essential and the basic computer skills example still require independent semantic, grammar and fluent Myanmar review."),
    "effective": ("B1", "adj.", 8, 2006, "Oxford B1 adjective label matches. Independently verify the intended producing-desired-results sense, example collocation and Myanmar distinction from efficient."),
    "highly": ("B1", "adv.", 8, 2119, "Oxford B1 adverb label matches. Check the intensifier sense in highly recommended and natural Myanmar translation; word/POS membership alone cannot sign off the example."),
}
RECORD_KEYS = {
    "word", "level", "part_of_speech", "source_cefr", "source_pos",
    "source_entry", "source_scope", "source_url", "source_authority", "source_document",
    "pdf_page_1_based", "pdf_extracted_line_0_based", "observed_on",
    "source_access", "shortlist_english_definition", "shortlist_myanmar_meaning",
    "shortlist_example", "shortlist_source_path", "shortlist_source_index",
    "shortlist_source_blob_sha", "editorial_risk", "independent_review_task",
    "editorial_hold", "independently_reviewed", "release_approved", "reviewer_receipt"
}
TOP_KEYS = {
    "schema", "scope", "status", "observed_on", "shortlist_blob_sha",
    "source_url", "record_count", "counts_by_level", "word_pos_discrepancies", "lower_than_B1", "higher_than_B1", "matching_B1",
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
    if data.get("record_count") != 12 or data.get("counts_by_level") != dict(A1=0, A2=0, B1=12, B2=0, C1=0):
        errors.append("record or per-level count drift")
    if data.get("word_pos_discrepancies") != 7 or data.get("independently_approved_count") != 0 or data.get("lower_than_B1") != 4 or data.get("higher_than_B1") != 3 or data.get("matching_B1") != 5:
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
        expected_cefr, expected_pos, expected_page, expected_line, expected_risk = EXPECTED[word]
        if set(row) != RECORD_KEYS:
            errors.append(word + ": unrecognised or missing record keys")
        if (row.get("level"), row.get("source_cefr"), row.get("source_pos"), row.get("pdf_page_1_based"), row.get("pdf_extracted_line_0_based")) != ("B1", expected_cefr, expected_pos, expected_page, expected_line):
            errors.append(word + ": direct Oxford word/POS/locator drift")
        if row.get("source_entry") != word + " " + expected_pos or row.get("editorial_risk") != expected_risk:
            errors.append(word + ": publisher entry or substantive editorial risk drift")
        if word not in str(row.get("independent_review_task", "")) or ("Oxford 3000 lists " + word + " at " + expected_cefr) not in str(row.get("independent_review_task", "")):
            errors.append(word + ": specific independent reviewer task missing")
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
        entry = lookup.get((word, "B1"))
        if not entry:
            errors.append(word + ": not in B1 shortlist")
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
    change("invent Oxford B1 label", "source_cefr", "C1")
    change("forge PDF entry", "source_entry", "false entry")
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
    x = copy.deepcopy(data); x["higher_than_B1"] = 0; cases.append(("erase upward conflicts", x))
    x = copy.deepcopy(data); x["independently_approved_count"] = 12; cases.append(("fake total", x))
    x = copy.deepcopy(data); x["shortlist_blob_sha"] = "0" * 40; cases.append(("fake shortlist hash", x))
    x = copy.deepcopy(data); x["provenance_note"] = ""; cases.append(("erase caveat", x))
    return cases


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=["A1", "A2", "B1", "B2", "C1", "ALL"], default="ALL")
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
        "level": args.level, "direct_oxford_B1_draft_observations": 12,
        "lower_word_pos_level_conflicts": 4, "higher_word_pos_level_conflicts": 3, "matching_word_pos_level": 5, "independently_approved": 0,
        "negative_mutations_rejected": rejected, "errors": errors,
        "status": "PASS_STRUCTURE_STILL_HOLD" if not errors else "FAIL"
    }, ensure_ascii=False))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
