#!/usr/bin/env python3
"""CEFR-1000 staging-only structural and release gate. No approval inferred from self-checks."""
import argparse
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {level: 200 for level in LEVELS}

def fail(message, errors):
    errors.append(message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=LEVELS, help="Test one level; global checks still run")
    parser.add_argument("--release", action="store_true", help="Fail closed unless all independent gates are evidenced")
    args = parser.parse_args()
    errors = []
    shortlist = json.loads((ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json").read_text(encoding="utf-8"))
    tasks = json.loads((ROOT / "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json").read_text(encoding="utf-8"))
    entries = shortlist["entries"]
    reviews = tasks["tasks"]
    for name, records in (("entries", entries), ("tasks", reviews)):
        counts = Counter(x.get("level") for x in records)
        if counts != EXPECTED:
            fail(f"{name}: expected exactly 200 per level; got {dict(counts)}", errors)
    if len(entries) != 1000 or len(reviews) != 1000:
        fail("Exactly 1000 entries and 1000 tasks required", errors)
    for field, data in (("shortlist", shortlist), ("tasks", tasks)):
        if data.get("counts_by_level") != EXPECTED:
            fail(f"{field} count metadata differs from target", errors)
    if tasks.get("source_shortlist_blob_sha") != "475e68ae17ab97bd937e73e5ce4794e0dcd76551":
        fail("Review task source shortlist provenance changed: regenerate tasks under independent control", errors)
    # Provisional input must never be mistaken for independently reviewed material.
    # Run globally, including in filtered CI matrix jobs.
    for name, document in (("shortlist", shortlist), ("tasks", tasks)):
        approvals = document.get("independently_approved_by_level")
        if approvals is not None and approvals != {level: 0 for level in LEVELS}:
            fail(f"{name}: provisional independent approval metadata must remain zero", errors)
    approval_fields = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                       "reviewed_level", "reviewed_pronunciation", "release_approved")
    for i, entry in enumerate(entries):
        for field in approval_fields:
            if entry.get(field) is not False:
                fail(f"entry {i}: provisional {field} must be explicitly false", errors)
    # Cross-level duplicate checks MUST be global even in --level matrix jobs.
    # Otherwise a collision between A1 and B1 evades both filtered jobs.
    global_keys = Counter((str(x.get("word", "")).strip().casefold(), str(x.get("part_of_speech", "")).strip().casefold()) for x in entries)
    for key, count in global_keys.items():
        if count > 1:
            fail(f"duplicate headword/part-of-speech across inventory: {key} ({count})", errors)
    # Global checks prevent unrelated matrix jobs from overlooking corruption.
    seen = set()
    task_keys = set()
    for i, entry in enumerate(entries):
        key = (str(entry.get("word", "")).strip().casefold(), str(entry.get("part_of_speech", "")).strip().casefold())
        if not all(key):
            fail(f"entry {i}: missing headword or part of speech", errors)
        if key in seen:
            fail(f"entry {i}: duplicate headword/part-of-speech {key}", errors)
        seen.add(key)
        for field in ("english_definition", "burmese_meaning", "example_sentence", "source_path", "source_blob_sha"):
            if not str(entry.get(field, "")).strip():
                fail(f"entry {i}: missing {field}", errors)
        if entry.get("editorial_hold") is not True:
            fail(f"entry {i}: provisional entry must remain held", errors)
    for i, task in enumerate(reviews):
        key = (task.get("level"), str(task.get("headword", "")).casefold(), str(task.get("part_of_speech", "")).casefold())
        if key in task_keys:
            fail(f"task {i}: duplicate review task {key}", errors)
        task_keys.add(key)
    # A pending task must not contain fabricated review evidence or partial approvals.
    # Check all levels even when CI selects a single matrix level.
    pending_fields = ("english_definition_review", "myanmar_meaning_review",
                      "original_example_review", "exact_sense_cefr_review",
                      "pronunciation_review")
    for i, task in enumerate(reviews):
        if task.get("review_status") != "PENDING_INDEPENDENT_REVIEW":
            fail(f"task {i}: review_status must remain pending", errors)
        if task.get("approval") is not False:
            fail(f"task {i}: approval must be explicitly false", errors)
        for field in pending_fields:
            if task.get(field) != "PENDING":
                fail(f"task {i}: {field} must remain PENDING", errors)
        for field in ("reviewer_assigned", "reviewer_identity", "reviewer_signed_at", "source_observed_on"):
            if task.get(field) is not None:
                fail(f"task {i}: unverified {field} must remain null", errors)
        if task.get("source_evidence_urls") != []:
            fail(f"task {i}: unverified source_evidence_urls must remain empty", errors)
        if task.get("shortlist_blob_sha") != tasks.get("source_shortlist_blob_sha"):
            fail(f"task {i}: shortlist blob provenance mismatch", errors)
    # A matching word/POS alone is insufficient: task provenance must match its entry.
    entry_provenance = {
        (e.get("level"), str(e.get("word", "")).casefold(), str(e.get("part_of_speech", "")).casefold()):
        (e.get("source_path"), e.get("source_index"), e.get("source_blob_sha"))
        for e in entries
    }
    for i, task in enumerate(reviews):
        key = (task.get("level"), str(task.get("headword", "")).casefold(),
               str(task.get("part_of_speech", "")).casefold())
        if key in entry_provenance and (
            task.get("source_path"), task.get("source_index"), task.get("source_blob_sha")
        ) != entry_provenance[key]:
            fail(f"task {i}: source provenance differs from shortlist entry", errors)
    for level in LEVELS:
        entry_keys = Counter((x["level"], x["word"].casefold(), x["part_of_speech"].casefold()) for x in entries if x["level"] == level)
        review_keys = Counter((x["level"], x["headword"].casefold(), x["part_of_speech"].casefold()) for x in reviews if x["level"] == level)
        if entry_keys != review_keys:
            fail(f"{level}: shortlist/review task mapping differs", errors)
    if args.release:
        # Structural QA cannot establish independence, listening, physical iPhone QA or deployment.
        # A separate signed evidence manifest and external attestation verifier must be integrated
        # before this gate can ever succeed. Never infer evidence from flags in provisional JSON.
        fail("RELEASE BLOCKED: independently signed linguistic/CEFR reviews, 4000 listened-to audio assets, physical iPhone Safari and browser/mobile QA, hosting clearance, production deployment and preservation attestations are not verified by this tool", errors)
    print(json.dumps({"mode": "release" if args.release else "structural", "level": args.level or "all", "errors": errors, "independent_approval_inferred": False}, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
