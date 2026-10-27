#!/usr/bin/env python3
"""Audit publisher-indexed Cambridge sense triage; NEVER independent signoff or deployment."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-SECOND-SENSE-LEADS-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
STATUS = "CAMBRIDGE_SECOND_SENSE_SOURCE_LEADS_STAGING_HOLD"
ROW_STATUS = "PUBLISHER_INDEXED_SENSE_LEAD_NOT_INDEPENDENT_APPROVAL"
EXPECTED = {
    "print": ("C2", "noun (TEXT)"),
    "racism": ("B2", "noun (racial unfairness / racist beliefs)"),
    "consistently": ("C2", "adverb (unchanging manner)"),
    "diverse": ("B2", "adjective (including different types)"),
    "integrity": ("C2", "noun (HONESTY)"),
}


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def validate(packet, shortlist, raw, level="ALL"):
    errors = []
    rows = packet.get("records", [])
    originals = {r.get("word"): r for r in shortlist.get("entries", [])}
    if packet.get("schema") != 1 or packet.get("status") != STATUS:
        errors.append("staging-only Cambridge source status/schema missing")
    if packet.get("observed_on") != "2026-10-27":
        errors.append("observation date altered")
    if packet.get("shortlist_blob_sha") != blob_sha(raw):
        errors.append("source shortlist changed; indexed evidence must be reviewed again")
    if len(shortlist.get("entries", [])) != 1000:
        errors.append("source shortlist not 1000")
    if packet.get("record_count") != 5 or len(rows) != 5:
        errors.append("expected five publisher-indexed exact-sense leads")
    if {r.get("word") for r in rows} != set(EXPECTED) or len({r.get("word") for r in rows}) != len(rows):
        errors.append("publisher sense lead word set missing/duplicated")
    if packet.get("independently_approved_count") != 0:
        errors.append("fake approval aggregate")
    for row in rows:
        word = row.get("word")
        if word not in EXPECTED:
            continue
        src = originals.get(word)
        if not src:
            errors.append(f"{word}: no shortlist record")
            continue
        cefr, heading = EXPECTED[word]
        expected = {
            "source_sense_cefr": cefr,
            "source_sense_heading": heading,
            "source_url": f"https://dictionary.cambridge.org/dictionary/english/{word}",
            "publisher": "Cambridge University Press & Assessment",
            "observed_on": "2026-10-27",
            "shortlist_level": src["level"],
            "shortlist_part_of_speech": src["part_of_speech"],
            "shortlist_english_definition": src["english_definition"],
            "shortlist_myanmar_meaning": src["burmese_meaning"],
            "shortlist_example": src["example_sentence"],
        }
        for field, value in expected.items():
            if row.get(field) != value:
                errors.append(f"{word}: publisher/snapshot field {field} drift")
        if "403" not in row.get("source_access", ""):
            errors.append(f"{word}: source-access limitation omitted")
        if not row.get("editorial_risk") or not row.get("source_observation") or not row.get("proposed_myanmar_review_hint"):
            errors.append(f"{word}: missing independent-review prompt")
        for field in ("independent_english_review", "independent_myanmar_review",
                      "independent_example_review", "independent_cefr_sense_review", "release_approved"):
            if row.get(field) is not False:
                errors.append(f"{word}: unsupported review flag {field}")
        if (row.get("independent_reviewer_receipt") is not None
                or row.get("editorial_hold") is not True
                or row.get("status") != ROW_STATUS
                or src.get("editorial_hold") is not True
                or src.get("release_approved") is not False):
            errors.append(f"{word}: editorial hold/reviewer receipt bypass")
    selected = [r for r in rows if level == "ALL" or r.get("shortlist_level") == level]
    return errors, {
        "level": level, "publisher_indexed_sense_leads": len(selected),
        "source_access": "CAMBRIDGE_SEARCH_INDEXED_TEXT_DIRECT_FETCH_403",
        "independently_approved": 0, "status": "STAGING_HOLD_ONLY",
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text("utf-8"))
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    errors, report = validate(packet, shortlist, raw, args.level)
    if args.self_test:
        cases = [
            lambda d: d["records"][0].update({"independent_english_review": True}),
            lambda d: d["records"][0].update({"source_sense_cefr": "A1"}),
            lambda d: d["records"][0].update({"source_url": "https://example.invalid"}),
            lambda d: d["records"][0].update({"independent_reviewer_receipt": {"name": "forged"}}),
            lambda d: d["records"].append(copy.deepcopy(d["records"][0])),
        ]
        for i, mutate in enumerate(cases):
            forged = copy.deepcopy(packet)
            mutate(forged)
            if not validate(forged, shortlist, raw, "ALL")[0]:
                errors.append(f"negative test {i} accepted fake Cambridge evidence")
        report["negative_tests"] = "PASS" if not errors else "FAIL"
    report["errors"] = errors
    (ROOT / f"cefr-1000-cambridge-second-sense-{args.level}.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
