#!/usr/bin/env python3
"""CEFR-1000 staging release veto. Deliberately cannot certify publication.

This is a negative-only preflight: a successful structural check is NEVER
independent linguistic, audio listening, physical device or deployment proof.
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
TARGET = {level: 200 for level in LEVELS}
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
TASKS = ROOT / "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"

def inspect(shortlist=SHORTLIST, tasks=TASKS):
    problems = []
    try:
        s = json.loads(Path(shortlist).read_text(encoding="utf-8"))
        t = json.loads(Path(tasks).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return ["Unable to parse required intake: " + str(exc)]
    for label, doc in (("shortlist", s), ("review tasks", t)):
        if doc.get("counts_by_level") != TARGET:
            problems.append(label + ": per-level declared counts differ from 200 each")
        if doc.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
            problems.append(label + ": independent approval counters changed; manual verification required")
    entries = s.get("entries")
    tasks_data = t.get("tasks")
    if not isinstance(entries, list) or not isinstance(tasks_data, list):
        return problems + ["Missing entries or tasks arrays"]
    for label, records, level_key in (("entries", entries, "level"), ("tasks", tasks_data, "level")):
        actual = Counter(r.get(level_key) for r in records if isinstance(r, dict))
        if actual != TARGET or len(records) != 1000:
            problems.append(label + ": actual allocation is not exactly 200 per level / 1000 total")
    # Structural duplicate check; distinct senses still require human adjudication.
    identities = []
    for index, record in enumerate(entries):
        if not isinstance(record, dict):
            problems.append(f"Entry {index}: non-object record")
            continue
        headword = record.get("headword")
        if not isinstance(headword, str) or not headword.strip():
            problems.append(f"Entry {index}: missing headword")
            continue
        identities.append((record.get("level"), headword.strip().casefold()))
    repeated = [key for key, count in Counter(identities).items() if count > 1]
    if repeated:
        problems.append(f"Duplicate level/headword identities require exact-sense adjudication: {len(repeated)}")
    if any(not isinstance(record, dict) for record in tasks_data):
        problems.append("Review tasks contain non-object records")
    if t.get("source_shortlist_blob_sha") != "475e68ae17ab97bd937e73e5ce4794e0dcd76551":
        problems.append("Task provenance differs from frozen first-pass shortlist; reconcile independently")
    if s.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        problems.append("Unexpected shortlist release status")
    if t.get("release_status") != "ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH":
        problems.append("Unexpected task release status")
    if any(r.get("review_status") != "PENDING_INDEPENDENT_REVIEW" for r in tasks_data if isinstance(r, dict)):
        problems.append("Some review tasks no longer pending: independently audit changes")
    # Positive release permission is deliberately not implemented here. A separate
    # independently audited final-manifest validator is required.
    problems.append("RELEASE BLOCKED: 1000 independently signed exact-sense bilingual reviews not established")
    problems.append("RELEASE BLOCKED: George/Emma word+example audio and real listening signoff not established")
    problems.append("RELEASE BLOCKED: browser/mobile and physical iPhone Safari QA not established")
    problems.append("RELEASE BLOCKED: GitHub Pages limits, 54 lessons/IELTS/audio/privacy preservation and live deployment not established")
    return problems

def main():
    issues = inspect()
    for issue in issues:
        print("BLOCK: " + issue)
    print("CEFR-1000 RELEASE PERMISSION: DENIED (staging only)")
    return 1

if __name__ == "__main__":
    sys.exit(main())
