#!/usr/bin/env python3
"""Structural integrity for Cambridge sense-level editorial leads; never an approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "business": ("A2", "A1 (selling activity, uncountable); A2 (company, countable)"),
    "band": ("B1", "A1"),
    "address": ("B1", "A1"),
    "cancer": ("B1", "B1"),
    "abandon": ("C1", "C1"),
    "acknowledge": ("C1", "C1"),
}
STATUS = "SENSE_SPECIFIC_PUBLISHER_SOURCE_TRIAGE_NO_INDEPENDENT_APPROVAL"


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()


def audit(data, shortlist, raw, level="ALL"):
    errors = []
    rows = data.get("records", [])
    if data.get("schema") != 1 or data.get("status") != STATUS:
        errors.append("staging status/schema missing or altered")
    if data.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY":
        errors.append("scope not fixed to approved 1000-total project")
    if data.get("observed_on") != "2026-10-27":
        errors.append("observation date changed without new source inspection")
    if data.get("shortlist_blob_sha") != blob_sha(raw):
        errors.append("source shortlist changed: sense evidence requires refresh")
    if data.get("record_count") != 6 or len(rows) != 6:
        errors.append("unexpected record count")
    if data.get("reviewed_and_approved_count") != 0:
        errors.append("unearned independent approvals")
    if {r.get("word") for r in rows} != set(EXPECTED):
        errors.append("missing, duplicate or unknown source records")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000:
        errors.append("shortlist is not 1000 entries")
    lookup = {r.get("word"): r for r in entries}
    selected = [r for r in rows if level == "ALL" or r.get("level") == level]
    for r in selected:
        word = r.get("word")
        source = lookup.get(word)
        if not source or word not in EXPECTED:
            errors.append(str(word) + ": not in canonical shortlist/expected observations")
            continue
        if (r.get("level"), r.get("source_cefr")) != EXPECTED[word]:
            errors.append(word + ": observed CEFR evidence or shortlist level changed")
        for key, original in (
            ("level", "level"), ("part_of_speech", "part_of_speech"),
            ("shortlist_english_definition", "english_definition"),
            ("shortlist_myanmar_meaning", "burmese_meaning"),
            ("shortlist_example", "example_sentence"),
        ):
            if r.get(key) != source.get(original):
                errors.append(word + ": provisional source content drift: " + key)
        url = r.get("source_url", "")
        parsed = urlparse(url) if isinstance(url, str) else urlparse("")
        if (parsed.scheme != "https" or parsed.hostname != "dictionary.cambridge.org"
                or word not in parsed.path.split("/") or "/dictionary/" not in parsed.path):
            errors.append(word + ": missing publisher-owned exact headword URL")
        if (r.get("observed_on") != "2026-10-27"
                or r.get("source_authority") != "Cambridge University Press & Assessment"
                or "indexed" not in r.get("source_access", "").lower()):
            errors.append(word + ": source provenance missing or overstated")
        for key in ("sense_heading", "source_observation", "editorial_risk", "triage",
                    "proposed_burmese_review_hint"):
            if not isinstance(r.get(key), str) or len(r[key].strip()) < 12:
                errors.append(word + ": missing sense-level reviewer task: " + key)
        if (r.get("independently_reviewed") is not False
                or r.get("release_approved") is not False
                or r.get("editorial_hold") is not True
                or r.get("reviewer_receipt") is not None
                or source.get("editorial_hold") is not True
                or source.get("release_approved") is not False):
            errors.append(word + ": independent approval or editorial hold bypassed")
    return errors, {"level": level, "source_records": len(selected),
                    "independently_approved": 0,
                    "status": "STAGING_HOLD_ONLY",
                    "errors": errors}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    data = json.loads(DATA.read_text(encoding="utf8"))
    errors, report = audit(data, shortlist, raw, args.level)
    if args.self_test:
        for mutate in (
            lambda d: d.update(reviewed_and_approved_count=6),
            lambda d: d["records"][0].update(independently_reviewed=True),
            lambda d: d["records"][0].update(source_url="https://example.org/false"),
            lambda d: d["records"][0].update(source_cefr="C2"),
            lambda d: d["records"][0].update(shortlist_example="forged"),
            lambda d: d.update(shortlist_blob_sha="0" * 40),
        ):
            altered = copy.deepcopy(data)
            mutate(altered)
            negative_errors, _ = audit(altered, shortlist, raw, "ALL")
            if not negative_errors:
                errors.append("negative test unexpectedly accepted falsified record")
        report["negative_tests"] = "PASS" if not errors else "FAIL"
    report["errors"] = errors
    out = ROOT / ("cefr-1000-cambridge-sense-" + args.level + ".json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + chr(10), encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
