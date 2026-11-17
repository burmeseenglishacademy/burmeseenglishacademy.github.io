#!/usr/bin/env python3
"""Fail-closed CEFR-1000 intake and independent-review gate; never publishes."""
import argparse
import collections
import json
import pathlib
import re
import subprocess
import sys

LEVELS = ("A1", "A2", "B1", "B2", "C1")
REVIEW_FIELDS = ("english_definition_review", "myanmar_meaning_review",
                 "original_example_review", "exact_sense_cefr_review",
                 "pronunciation_review")
ENTRY_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
               "reviewed_level", "reviewed_pronunciation", "release_approved")

def check(root):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    shortlist_path = root / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
    tasks_path = root / "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"
    shortlist = json.loads(shortlist_path.read_text(encoding="utf-8"))
    review = json.loads(tasks_path.read_text(encoding="utf-8"))
    entries, tasks = shortlist["entries"], review["tasks"]
    require(len(entries) == len(tasks) == 1000, "exactly 1000 aligned entries/tasks required")
    counts = collections.Counter(e.get("level") for e in entries)
    require(all(counts[level] == 200 for level in LEVELS) and set(counts) == set(LEVELS),
            "exactly 200 entries at each of A1/A2/B1/B2/C1 required")
    for doc in (shortlist, review):
        require(doc.get("counts_by_level") == {x: 200 for x in LEVELS}, "declared counts differ")
        require(doc.get("independently_approved_by_level") == {x: 0 for x in LEVELS},
                "intake must not declare independent approval")
    blob = subprocess.run(["git", "hash-object", str(shortlist_path)], cwd=root,
                          capture_output=True, text=True, check=True).stdout.strip()
    require(review.get("source_shortlist_blob_sha") == blob, "shortlist blob provenance mismatch")
    seen = set()
    for i, (e, t) in enumerate(zip(entries, tasks), 1):
        label = f"entry {i}"
        key = (str(e.get("word", "")).casefold().strip(), str(e.get("part_of_speech", "")).casefold().strip())
        require(key[0] and key[1] and key not in seen, f"{label}: missing/duplicate headword+POS")
        seen.add(key)
        require(t.get("task_id") == f"CEFR1000-{e.get('level')}-{i:04d}",
                f"{label}: task ID must use global sequence")
        for a, b in (("word", "headword"), ("level", "level"),
                     ("part_of_speech", "part_of_speech"), ("source_path", "source_path"),
                     ("source_index", "source_index"), ("source_blob_sha", "source_blob_sha")):
            require(e.get(a) == t.get(b), f"{label}: {a} provenance mismatch")
        require(t.get("shortlist_blob_sha") == blob, f"{label}: task shortlist SHA mismatch")
        require(e.get("editorial_hold") is True and all(e.get(f) is False for f in ENTRY_FLAGS),
                f"{label}: provisional entry must remain held/unapproved")
        require(t.get("review_status") == "PENDING_INDEPENDENT_REVIEW" and
                t.get("approval") is False and
                all(t.get(f) == "PENDING" for f in REVIEW_FIELDS),
                f"{label}: no self-attested review allowed")
        require(t.get("reviewer_identity") is None and t.get("reviewer_signed_at") is None
                and t.get("reviewer_assigned") is None,
                f"{label}: intake cannot impersonate an independent reviewer")
        require(t.get("source_evidence_urls") == [] and t.get("source_observed_on") is None,
                f"{label}: intake cannot impersonate evidence collection")
        require(all(isinstance(e.get(f), str) and e[f].strip() for f in
                    ("english_definition", "burmese_meaning", "example_sentence")),
                f"{label}: missing first-pass bilingual/example text")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = check(args.root.resolve())
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"BLOCKED: unreadable or invalid intake: {exc}", file=sys.stderr)
        return 1
    for error in errors[:30]:
        print("BLOCKED:", error, file=sys.stderr)
    if errors:
        print(f"BLOCKED: {len(errors)} intake failures", file=sys.stderr)
        return 1
    print("PASS: provisional intake structurally consistent; 0 independent approvals.")
    print("RELEASE BLOCKED: independent signoff, audio/listening, mobile/iPhone, hosting and deployment unverified.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
