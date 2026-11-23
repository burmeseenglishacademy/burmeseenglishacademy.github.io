#!/usr/bin/env python3
"""CEFR-1000 provisional intake integrity check. NOT a release approval gate.

This intentionally cannot approve or deploy anything. It verifies that the
editorial-hold shortlist and independent-review intake remain aligned, and
refuses to treat provisional content as production-ready.
"""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
TARGET = {level: 200 for level in LEVELS}


def check():
    shortlist = json.loads((DRAFT / "CEFR-1000-PROVISIONAL-SHORTLIST.json").read_text(encoding="utf-8"))
    tasks = json.loads((DRAFT / "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json").read_text(encoding="utf-8"))
    errors = []
    entries = shortlist.get("entries", [])
    reviews = tasks.get("tasks", [])
    count = collections.Counter(e.get("level") for e in entries)
    task_count = collections.Counter(t.get("level") for t in reviews)
    if len(entries) != 1000 or len(reviews) != 1000:
        errors.append(f"expected 1000 entries and tasks, got {len(entries)} and {len(reviews)}")
    for level in LEVELS:
        if count[level] != 200 or task_count[level] != 200:
            errors.append(f"{level}: entries={count[level]}, tasks={task_count[level]}; expected 200 each")
    for name, obj in (("shortlist", shortlist), ("tasks", tasks)):
        if obj.get("counts_by_level") != TARGET:
            errors.append(f"{name} declared level counts disagree with target")
        if obj.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0):
            errors.append(f"{name} claims nonzero independent approval: requires external audit")
    if tasks.get("source_shortlist_blob_sha") != "475e68ae17ab97bd937e73e5ce4794e0dcd76551":
        errors.append("review tasks no longer reference the pinned original shortlist blob")
    if shortlist.get("scope_target") != TARGET or shortlist.get("schema") != 1 or tasks.get("schema") != 1:
        errors.append("scope/schema mismatch: expected exactly the approved CEFR-1000 allocation")
    if shortlist.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("shortlist release hold status changed")
    if tasks.get("release_status") != "ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH":
        errors.append("review-task release hold status changed")
    if tasks.get("scope") != "CEFR-1000 ONLY":
        errors.append("review-task scope changed")
    seen = set()
    seen_tasks = set()
    task_sequence = collections.Counter()
    for index, entry in enumerate(entries):
        level = entry.get("level")
        word = entry.get("word")
        pos = entry.get("part_of_speech")
        if not all(isinstance(entry.get(k), str) and entry[k].strip() for k in
                   ("word", "part_of_speech", "english_definition", "burmese_meaning", "example_sentence",
                    "source_path", "source_blob_sha")):
            errors.append(f"entry {index}: missing required editorial/provenance text")
        if not isinstance(entry.get("source_index"), int) or isinstance(entry.get("source_index"), bool) or entry["source_index"] < 0:
            errors.append(f"entry {index}: invalid nonnegative source index")
        if not re.fullmatch(r"[0-9a-f]{40}", str(entry.get("source_blob_sha", ""))):
            errors.append(f"entry {index}: malformed source blob SHA")
        if not str(entry.get("source_path", "")).startswith("draft/") or ".." in str(entry.get("source_path", "")):
            errors.append(f"entry {index}: invalid source path")
        if entry.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            errors.append(f"entry {index}: provisional status changed")
        key = (str(word).casefold().strip(), str(pos).casefold().strip())
        if key in seen:
            errors.append(f"duplicate headword/POS across levels: {key}")
        seen.add(key)
        if entry.get("editorial_hold") is not True or entry.get("release_approved") is not False:
            errors.append(f"entry {index}: editorial hold lifted or release approval asserted")
        for field in ("reviewed_english", "reviewed_burmese", "reviewed_example",
                      "reviewed_level", "reviewed_pronunciation"):
            if entry.get(field) is not False:
                errors.append(f"entry {index}: {field} must remain false in provisional intake")
    for index, task in enumerate(reviews):
        ident = task.get("task_id")
        if ident in seen_tasks:
            errors.append(f"duplicate task ID {ident}")
        seen_tasks.add(ident)
        if task.get("level") in TARGET:
            task_sequence[task["level"]] += 1
            expected_id = f"CEFR1000-{task['level']}-{task_sequence[task['level']]:04d}"
            if ident != expected_id:
                errors.append(f"task {index}: task ID does not match per-level sequence")
        if task.get("shortlist_blob_sha") != tasks.get("source_shortlist_blob_sha"):
            errors.append(f"task {index}: shortlist provenance mismatch")
        if task.get("reviewer_assigned") is not None:
            errors.append(f"task {index}: reviewer assignment unexpectedly populated")
        for field in ("english_definition_review", "myanmar_meaning_review", "original_example_review",
                      "exact_sense_cefr_review", "pronunciation_review"):
            if task.get(field) != "PENDING":
                errors.append(f"task {index}: {field} not pending")
        if task.get("approval") is not False or task.get("review_status") != "PENDING_INDEPENDENT_REVIEW":
            errors.append(f"task {index}: unexpected independent approval/status")
        if task.get("reviewer_identity") is not None or task.get("reviewer_signed_at") is not None:
            errors.append(f"task {index}: signoff present in provisional intake")
        if task.get("source_evidence_urls") != [] or task.get("source_observed_on") is not None:
            errors.append(f"task {index}: evidence populated without separate verified review")
        if index < len(entries):
            entry = entries[index]
            for task_key, entry_key in (("level", "level"), ("headword", "word"),
                                        ("part_of_speech", "part_of_speech"),
                                        ("source_path", "source_path"),
                                        ("source_index", "source_index"),
                                        ("source_blob_sha", "source_blob_sha")):
                if task.get(task_key) != entry.get(entry_key):
                    errors.append(f"task {index}: {task_key} does not match shortlist")
    return errors, count


if __name__ == "__main__":
    errors, counts = check()
    for level in LEVELS:
        print(f"{level}: provisional={counts[level]}/200, independently_approved=0/200")
    if errors:
        print(f"FAIL: {len(errors)} intake integrity issue(s)", file=sys.stderr)
        for error in errors[:50]:
            print(f" - {error}", file=sys.stderr)
        sys.exit(1)
    print("PASS: provisional intake structurally aligned; RELEASE REMAINS BLOCKED.")
    print("NOT VERIFIED: exact-sense CEFR, independent reviewers, George/Emma audio/listening,")
    print("browser/mobile/physical iPhone Safari, Pages hosting, protected assets, deployment.")
