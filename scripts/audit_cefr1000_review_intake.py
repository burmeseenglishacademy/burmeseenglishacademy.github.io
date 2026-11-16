#!/usr/bin/env python3
"""Fail-closed independent-review intake integrity audit; NOT independent signoff."""
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
PENDING = ("english_definition_review", "myanmar_meaning_review",
           "original_example_review", "exact_sense_cefr_review", "pronunciation_review")
PROVENANCE = ("source_path", "source_index", "source_blob_sha")

def audit(shortlist, intake, shortlist_sha):
    errors = []
    entries, tasks = shortlist.get("entries"), intake.get("tasks")
    if not isinstance(entries, list) or not isinstance(tasks, list):
        return ["entries and tasks must be arrays"]
    if len(entries) != 1000 or len(tasks) != 1000:
        errors.append("both lists must contain exactly 1000 records")
    if intake.get("scope") != "CEFR-1000 ONLY" or intake.get("schema") != 1:
        errors.append("intake scope/schema mismatch")
    if intake.get("release_status") != "ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH":
        errors.append("intake must remain explicitly blocked")
    if intake.get("source_shortlist_blob_sha") != shortlist_sha:
        errors.append("intake points to a different shortlist blob")
    expected_counts = {level: 200 for level in LEVELS}
    if intake.get("counts_by_level") != expected_counts:
        errors.append("intake declared counts mismatch")
    if intake.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
        errors.append("intake claims independent approval")
    counts, ids = Counter(), set()
    for i, (entry, task) in enumerate(zip(entries, tasks)):
        if not isinstance(entry, dict) or not isinstance(task, dict):
            errors.append(f"record {i}: non-object entry/task")
            continue
        level = entry.get("level")
        counts[task.get("level")] += 1
        expected_id = f"CEFR1000-{level}-{counts[level]:04d}" if level in LEVELS else None
        if task.get("task_id") != expected_id or task.get("task_id") in ids:
            errors.append(f"record {i}: task ID/order/uniqueness mismatch")
        ids.add(task.get("task_id"))
        for source_field, task_field in (("word", "headword"), ("level", "level"),
                                          ("part_of_speech", "part_of_speech")):
            if entry.get(source_field) != task.get(task_field):
                errors.append(f"record {i}: {task_field} differs from shortlist")
        for field in PROVENANCE:
            if entry.get(field) != task.get(field):
                errors.append(f"record {i}: {field} provenance mismatch")
        if task.get("shortlist_blob_sha") != shortlist_sha:
            errors.append(f"record {i}: shortlist provenance mismatch")
        if task.get("review_status") != "PENDING_INDEPENDENT_REVIEW" or task.get("approval") is not False:
            errors.append(f"record {i}: task unexpectedly reviewed/approved")
        for field in PENDING:
            if task.get(field) != "PENDING":
                errors.append(f"record {i}: {field} is not pending")
        for field in ("reviewer_assigned", "reviewer_identity", "reviewer_signed_at", "source_observed_on"):
            if task.get(field) is not None:
                errors.append(f"record {i}: {field} unexpectedly populated")
        if task.get("source_evidence_urls") != []:
            errors.append(f"record {i}: source evidence must remain empty until genuine review")
    if dict(counts) != expected_counts:
        errors.append(f"actual task counts differ: {dict(counts)}")
    return errors

def main():
    try:
        shortlist_path = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
        intake_path = ROOT / "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"
        shortlist = json.loads(shortlist_path.read_text(encoding="utf-8"))
        intake = json.loads(intake_path.read_text(encoding="utf-8"))
        # SHA-1 of Git blob is not the plain file hash.
        import hashlib
        raw = shortlist_path.read_bytes()
        sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        errors = audit(shortlist, intake, sha)
    except (OSError, ValueError, TypeError) as exc:
        print(f"FAIL: cannot inspect review intake: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors[:50]:
            print("FAIL:", error, file=sys.stderr)
        print(f"FAIL: {len(errors)} intake integrity errors", file=sys.stderr)
        return 1
    print("PASS: 1000 matching PENDING tasks (200/level), provenance intact; ZERO independently reviewed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
