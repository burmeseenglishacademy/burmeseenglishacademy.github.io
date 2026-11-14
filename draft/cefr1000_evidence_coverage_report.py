#!/usr/bin/env python3
"""Read-only CEFR-1000 source-evidence coverage report. Never approves or publishes."""
import argparse
import json
from collections import Counter
from pathlib import Path

LEVELS = ("A1", "A2", "B1", "B2", "C1")
SOURCE_FIELDS = ("source_english", "source_burmese", "source_level")
REVIEW_FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation")

def summarize(data):
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        raise ValueError("Expected shortlist object with entries array")
    entries = data["entries"]
    if len(entries) != 1000:
        raise ValueError(f"Expected exactly 1000 entries; found {len(entries)}")
    output = {}
    for level in LEVELS:
        rows = [row for row in entries if isinstance(row, dict) and row.get("level") == level]
        if len(rows) != 200:
            raise ValueError(f"{level}: expected 200 provisional entries, found {len(rows)}")
        counts = {field: sum(isinstance(row.get(field), str) and bool(row[field].strip()) for row in rows) for field in SOURCE_FIELDS}
        approved = sum(row.get("release_approved") is True for row in rows)
        flags = sum(any(row.get(field) is True for field in REVIEW_FIELDS) for row in rows)
        held = sum(row.get("editorial_hold") is True for row in rows)
        output[level] = {
            "first_pass_written": len(rows),
            "editorial_holds": held,
            "independently_approved": 0,
            "independent_approval_basis": "UNPROVEN_NO_EXTERNAL_SIGNOFF_EVIDENCE",
            "source_fields_populated": counts,
            "bare_approval_flags": approved,
            "entries_with_any_bare_review_flag": flags,
            "audio_generated_and_listened": "UNVERIFIED",
            "physical_iphone_safari": "UNVERIFIED",
        }
    if sum(len([r for r in entries if isinstance(r, dict) and r.get("level") == level]) for level in LEVELS) != 1000:
        raise ValueError("Unknown or malformed CEFR levels in inventory")
    return {
        "release_decision": "BLOCKED_STAGING_ONLY",
        "scope": "USER_APPROVED_1000_TOTAL_NOT_5000",
        "levels": output,
        "blockers": [
            "Source-backed exact-sense CEFR and bilingual independent signoff absent",
            "Semantic cross-level sense deduplication not independently adjudicated",
            "George/Emma headword and example audio plus real listening attestations unverified",
            "Browser/mobile and physical iPhone Safari evidence unverified",
            "Candidate SHA-specific CI, GitHub Pages hosting, deployment and preservation evidence unverified",
        ],
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("shortlist", nargs="?", default="draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    parser.add_argument("--output", help="Optional local JSON report; never writes to source shortlist")
    args = parser.parse_args()
    report = summarize(json.loads(Path(args.shortlist).read_text(encoding="utf-8")))
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
