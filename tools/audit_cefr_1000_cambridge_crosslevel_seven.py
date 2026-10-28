#!/usr/bin/env python3
"""Staging-only cross-level Cambridge sense-lead provenance audit; NEVER human approval."""
import argparse
import copy
import hashlib
import json
import pathlib
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET = ROOT / "draft/CEFR-1000-CAMBRIDGE-CROSSLEVEL-SEVEN-2026-10-28.json"
EXPECTED = {
    ("A2", "mind"): "B1",
    ("B1", "civil"): "C1",
    ("B1", "leadership"): "C1",
    ("B1", "apparently"): "B2",
    ("B1", "edition"): "B2",
    ("B1", "prison"): "B1",
    ("B2", "personality"): "B2",
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("word", "level", "part_of_speech", "english_definition",
          "burmese_meaning", "example_sentence")


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + bytes([0]) + data).hexdigest()


def validate(packet, shortlist, blob_sha, level="ALL"):
    errors = []
    if packet.get("schema") != 1 or packet.get("project") != "BEA_CEFR_1000_NOT_5000":
        errors.append("Wrong scope/schema")
    if packet.get("branch") != "cefr-5000-bilingual-qa-staging":
        errors.append("Wrong staging branch")
    if packet.get("release_status") != "STAGING_EDITORIAL_HOLD_NO_APPROVAL":
        errors.append("Invalid hold status")
    if packet.get("shortlist_path") != "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json":
        errors.append("Wrong shortlist path")
    if packet.get("shortlist_blob_sha") != blob_sha or blob_sha != "475e68ae17ab97bd937e73e5ce4794e0dcd76551":
        errors.append("Pinned canonical shortlist blob changed")
    if packet.get("observed_on") != "2026-10-28":
        errors.append("Invalid observation date")
    rows = shortlist.get("entries", [])
    canonical = {(r.get("level"), r.get("word")): r for r in rows if isinstance(r, dict)}
    if len(rows) != 1000 or len(canonical) != 1000:
        errors.append("Canonical shortlist cardinality/duplicates")
    if {l: sum(r.get("level") == l for r in rows) for l in LEVELS} != dict.fromkeys(LEVELS, 200):
        errors.append("Canonical level quota changed")
    if any(not r.get("editorial_hold") or r.get("release_approved") or
           any(r.get(k) for k in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level"))
           for r in rows):
        errors.append("Canonical approvals/holds unexpectedly changed")
    if packet.get("counts") != {
        "provisional_written": dict.fromkeys(LEVELS, 200),
        "independently_approved": dict.fromkeys(LEVELS, 0),
        "new_observations": 7,
    }:
        errors.append("Misleading count metadata")
    records = packet.get("entries", [])
    if not isinstance(records, list) or len(records) != 7:
        return errors + ["Must have seven records"]
    keys = [(r.get("level"), r.get("word")) for r in records if isinstance(r, dict)]
    if len(keys) != 7 or set(keys) != set(EXPECTED):
        errors.append("Missing, duplicate, or unexpected source record")
    for rec in records:
        if not isinstance(rec, dict):
            errors.append("Non-object record")
            continue
        key = (rec.get("level"), rec.get("word"))
        if level != "ALL" and rec.get("level") != level:
            continue
        original = canonical.get(key)
        if original is None or any(rec.get(k) != original.get(k) for k in FIELDS):
            errors.append(f"{key}: original bilingual/example/POS snapshot drift")
        if rec.get("source_shortlist_blob_sha") != blob_sha:
            errors.append(f"{key}: source blob binding drift")
        if rec.get("source_cefr_label") != EXPECTED.get(key):
            errors.append(f"{key}: source CEFR lead tampered")
        url = rec.get("source_url", "")
        parsed = urlparse(url) if isinstance(url, str) else None
        if (not parsed or parsed.scheme != "https" or parsed.hostname != "dictionary.cambridge.org"
                or not parsed.path.endswith(rec.get("word", "") if key[1] != "mind" else "change-mind")):
            errors.append(f"{key}: untrusted or unrelated publisher URL")
        if (rec.get("source_observed_on") != "2026-10-28"
                or rec.get("source_access") != "PUBLISHER_OWNED_SEARCH_INDEX_EXCERPT_FULL_PAGE_HTTP_403"
                or rec.get("source_publisher") != "Cambridge University Press"):
            errors.append(f"{key}: source provenance/access tampered")
        for field in ("source_sense_heading", "observation", "editorial_issue", "reviewer_task",
                      "myanmar_editorial_candidate", "provenance_note"):
            if not isinstance(rec.get(field), str) or len(rec[field].strip()) < 12:
                errors.append(f"{key}: missing {field}")
        if (rec.get("independent_reviewed") is not False or rec.get("editorial_hold") is not True
                or rec.get("release_approved") is not False
                or rec.get("proposed_change_status") != "EDITORIAL_SUGGESTION_ONLY_NOT_APPLIED"):
            errors.append(f"{key}: false approval or editorial hold bypass")
    return errors


def self_test(packet, shortlist, blob):
    mutations = [
        ("source_url", "https://example.com/dictionary/english/mind"),
        ("source_cefr_label", "A2"),
        ("english_definition", "Wrong meaning"),
        ("burmese_meaning", "အဓိပ္ပာယ်မှား"),
        ("example_sentence", "Unrelated example."),
        ("source_access", "DIRECT_PUBLISHER_DICTIONARY_PAGE"),
        ("source_observed_on", "2030-01-01"),
        ("independent_reviewed", True),
        ("editorial_hold", False),
        ("release_approved", True),
    ]
    for field, value in mutations:
        broken = copy.deepcopy(packet)
        broken["entries"][0][field] = value
        assert validate(broken, shortlist, blob), f"Mutation not rejected: {field}"
    for change in ("duplicate", "quota", "sha"):
        broken = copy.deepcopy(packet)
        local = copy.deepcopy(shortlist)
        b = blob
        if change == "duplicate":
            broken["entries"][1] = broken["entries"][0]
        elif change == "quota":
            local["entries"][0]["level"] = "C1"
        else:
            b = "0" * 40
        assert validate(broken, local, b), f"Mutation not rejected: {change}"
    return len(mutations) + 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = SHORT.read_bytes()
    blob = git_blob_sha(raw)
    shortlist = json.loads(raw)
    packet = json.loads(PACKET.read_text(encoding="utf8"))
    errors = validate(packet, shortlist, blob, args.level)
    if args.self_test:
        n = self_test(packet, shortlist, blob)
        print(f"PASS: {n} negative mutations rejected; no independent approval")
    print(json.dumps({"level": args.level, "publisher_indexed_leads": 7,
                      "independent_approvals": 0, "errors": errors,
                      "status": "STAGING_SOURCE_TRIAGE_NOT_HUMAN_REVIEW"}))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
