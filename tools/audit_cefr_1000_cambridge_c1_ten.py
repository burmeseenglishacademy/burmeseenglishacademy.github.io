#!/usr/bin/env python3
"""Fail-closed staging integrity check for 10 Cambridge C1 sense review leads.

Mechanical integrity only: never claims Cambridge independently reviewed the
draft English/Myanmar/example, nor that an external human approved anything.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "draft/CEFR-1000-CAMBRIDGE-C1-TEN-SENSE-LEADS-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
STATUS = "PUBLISHER_INDEXED_SENSE_TRIAGE_NOT_INDEPENDENT_APPROVAL"
EXPECTED = {
    "tribute": ("C2", "SAME_SENSE_HIGHER_SOURCE_LEVEL"),
    "popularity": ("B2", "SAME_SENSE_LOWER_SOURCE_LEVEL"),
    "controversial": ("B2", "SAME_SENSE_LOWER_SOURCE_LEVEL"),
    "exclusively": ("C1", "SOURCE_LEVEL_SUPPORTS_DRAFT_SENSE_PENDING_BILINGUAL_REVIEW"),
    "sacred": ("C1", "SOURCE_LEVEL_SUPPORTS_DRAFT_SENSE_PENDING_BILINGUAL_REVIEW"),
    "asset": ("C1", "MIXED_SENSE_DEFINITION_EXAMPLE"),
    "neutral": ("C1", "SOURCE_LEVEL_SUPPORTS_DRAFT_SENSE_PENDING_BILINGUAL_REVIEW"),
    "noble": ("C1", "SOURCE_LEVEL_SUPPORTS_DRAFT_SENSE_PENDING_BILINGUAL_REVIEW"),
    "burden": ("C1", "SOURCE_LEVEL_SUPPORTS_DRAFT_SENSE_PENDING_BILINGUAL_REVIEW"),
    "dominant": ("C1", "SOURCE_LEVEL_SUPPORTS_DRAFT_SENSE_PENDING_BILINGUAL_REVIEW"),
}


def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()


def audit(data, shortlist, shortlist_raw, level="ALL"):
    errors = []
    rows = data.get("records")
    if not isinstance(rows, list):
        return ["records must be an array"]
    if data.get("schema") != 1 or data.get("status") != STATUS:
        errors.append("evidence schema/status is not the fixed staging hold")
    if data.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY":
        errors.append("superseded or unknown scope")
    if data.get("observed_on") != "2026-10-28":
        errors.append("source observation date changed")
    if data.get("shortlist_blob_sha") != blob_sha(shortlist_raw):
        errors.append("shortlist SHA drift")
    if data.get("record_count") != 10 or len(rows) != 10:
        errors.append("not exactly 10 evidence records")
    if data.get("independently_approved_count") != 0:
        errors.append("false independent approvals")
    if data.get("counts_by_level") != {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 10}:
        errors.append("unexpected per-level evidence counts")
    if len(shortlist.get("entries", [])) != 1000:
        errors.append("shortlist not 1000 entries")
    lookup = {(x.get("word"), x.get("level")): x for x in shortlist.get("entries", [])}
    words = [r.get("word") for r in rows if isinstance(r, dict)]
    if len(set(words)) != 10 or set(words) != set(EXPECTED):
        errors.append("missing, duplicate or unexpected evidence headwords")
    for r in rows:
        if not isinstance(r, dict):
            errors.append("malformed evidence record")
            continue
        word = r.get("word")
        if level != "ALL" and r.get("level") != level:
            continue
        source = lookup.get((word, "C1"))
        if not source or word not in EXPECTED:
            errors.append(str(word) + ": missing from canonical C1 shortlist")
            continue
        if r.get("level") != "C1" or r.get("part_of_speech") != source.get("part_of_speech"):
            errors.append(word + ": level/POS mismatch")
        if (r.get("source_cefr"), r.get("triage")) != EXPECTED[word]:
            errors.append(word + ": publisher label or triage drift")
        for key, original in (
            ("shortlist_english_definition", "english_definition"),
            ("shortlist_myanmar_meaning", "burmese_meaning"),
            ("shortlist_example", "example_sentence"),
        ):
            if r.get(key) != source.get(original):
                errors.append(word + ": original shortlist content drift " + key)
        url = r.get("source_url")
        p = urlparse(url) if isinstance(url, str) else urlparse("")
        if (p.scheme != "https" or p.hostname != "dictionary.cambridge.org"
                or p.path.split("/")[-1] != word or "/dictionary/english/" not in p.path):
            errors.append(word + ": source URL not publisher exact headword")
        if (r.get("observed_on") != "2026-10-28"
                or r.get("source_authority") != "Cambridge University Press & Assessment"
                or "search-indexed" not in str(r.get("source_access", ""))
                or "403" not in str(r.get("source_access", ""))):
            errors.append(word + ": publisher access caveat/provenance absent")
        for key in ("sense_heading", "source_observation", "editorial_risk"):
            if not isinstance(r.get(key), str) or len(r[key].strip()) < 15:
                errors.append(word + ": missing substantive sense evidence " + key)
        if (r.get("editorial_hold") is not True
                or r.get("independently_reviewed") is not False
                or r.get("release_approved") is not False
                or r.get("reviewer_receipt") is not None):
            errors.append(word + ": fabricated independent signoff")
        if (source.get("editorial_hold") is not True
                or source.get("release_approved") is not False):
            errors.append(word + ": provisional source unexpectedly approved")
    return errors


def negative_tests(data, shortlist, raw):
    tests = [
        ("forged approval", lambda x: x["records"][0].update(release_approved=True)),
        ("fabricated reviewer", lambda x: x["records"][0].update(reviewer_receipt={"reviewer_id": "someone"})),
        ("forged publisher CEFR", lambda x: x["records"][0].update(source_cefr="C1")),
        ("forged publisher URL", lambda x: x["records"][0].update(source_url="https://fake.example/dictionary/english/tribute")),
        ("changed Burmese snapshot", lambda x: x["records"][0].update(shortlist_myanmar_meaning="changed")),
        ("duplicate evidence", lambda x: x["records"].__setitem__(1, copy.deepcopy(x["records"][0]))),
        ("faked counts", lambda x: x.update(counts_by_level={"C1": 10})),
        ("false full-page claim", lambda x: x["records"][0].update(source_access="fully verified")),
    ]
    for label, mutate in tests:
        changed = copy.deepcopy(data)
        mutate(changed)
        if not audit(changed, shortlist, raw):
            raise AssertionError("Fail-closed negative test failed: " + label)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    errors = audit(data, shortlist, raw, args.level)
    if not errors and args.self_test:
        negative_tests(data, shortlist, raw)
    report = {
        "scope": "CEFR_1000_STAGING_ONLY",
        "level": args.level,
        "source_observations": sum(r.get("level") == args.level or args.level == "ALL" for r in data["records"]),
        "independently_approved": 0,
        "source_access": "publisher search-indexed snippets only; direct full-page fetch HTTP 403",
        "negative_tests": "PASS" if args.self_test and not errors else "NOT_RUN",
        "status": "PASS_STRUCTURE_NOT_LINGUISTIC_APPROVAL" if not errors else "FAIL",
        "errors": errors,
    }
    out = ROOT / ("cefr-1000-cambridge-c1-ten-" + args.level + ".json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
