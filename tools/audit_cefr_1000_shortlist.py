#!/usr/bin/env python3
"""Fail-closed STRUCTURAL QA for the user-approved 1,000-entry CEFR shortlist.

Validates the current shortlist + independent-review-task schemas. It checks
source linkage, selection conflicts, task parity and nonpublication only; it
NEVER certifies English/Myanmar quality, CEFR, pronunciation or audio.
"""
import argparse
import collections
import copy
import hashlib
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
TARGETS = {level: 200 for level in LEVELS}
HEADWORD = re.compile(r"^[a-z][a-z'-]{0,35}$")
MYANMAR = re.compile(r"[\u1000-\u109f\uaa60-\uaa7f]")
DATASET = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
TASKS = "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"
TRIAGE = "draft/CEFR-1000-SELECTION-TRIAGE.json"
HOLDS = (
    "draft/BATCH72-HISTORICAL-CROSS-LEVEL-HOLDS.json",
    "draft/BATCH74-CROSS-LEVEL-CANDIDATE-HOLDS.json",
    "draft/BATCH76-CANDIDATE-ONLY-EDITORIAL-HOLDS.json",
)
DRAFT_FIELDS = ("word", "part_of_speech", "english_definition", "burmese_meaning", "example_sentence")
REVIEW_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation", "release_approved")
TASK_STAGES = (
    "english_definition_review",
    "myanmar_meaning_review",
    "original_example_review",
    "exact_sense_cefr_review",
    "pronunciation_review",
)
SCREENS = (
    "CURRICULUM_OR_SENSE_LEVEL_DOUBT",
    "EXISTING_CANDIDATE_OR_CROSS_LEVEL_HOLD",
    "CROSS_LEVEL_SOURCE_CONFLICT",
    "MISSING_OR_INVALID_DRAFT_FIELD",
    "SOURCE_EDITORIAL_RISK_FLAGGED",
    "DUPLICATE_HEADWORD_SOURCE",
    "NONCANONICAL_OR_NAMED_FORM",
)


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def blob_sha(path):
    b = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def key_for(word):
    return unicodedata.normalize("NFC", str(word)).strip().casefold()


def validate(level="ALL", data=None, tasks=None, triage=None):
    issues = []
    data = read(DATASET) if data is None else data
    tasks = read(TASKS) if tasks is None else tasks
    triage = read(TRIAGE) if triage is None else triage
    rows = data.get("entries", []) if isinstance(data, dict) else []
    todo = tasks.get("tasks", []) if isinstance(tasks, dict) else []

    if not isinstance(rows, list) or len(rows) != 1000:
        issues.append("Exactly 1000 provisional shortlist rows required")
        return issues, {}
    if not isinstance(todo, list) or len(todo) != 1000:
        issues.append("Exactly 1000 independent review tasks required in tasks[]")
        return issues, {}

    if data.get("scope_target") != TARGETS or data.get("counts_by_level") != TARGETS:
        issues.append("Approved scope 200 entries per level not respected")
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        issues.append("Shortlist must remain unpublished / unverified")
    approved_counts = data.get("independently_approved_by_level", {})
    if not isinstance(approved_counts, dict) or any(approved_counts.get(l) != 0 for l in LEVELS):
        issues.append("False positive independent approval counts")

    if tasks.get("scope") != "CEFR-1000 ONLY":
        issues.append("Review-task scope must be CEFR-1000 ONLY")
    if tasks.get("release_status") != "ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH":
        issues.append("Review tasks must remain pending and unpublished")
    if tasks.get("counts_by_level") != TARGETS:
        issues.append("Review-task quota must remain 200 per CEFR level")
    try:
        expected_shortlist_sha = blob_sha(DATASET)
        if tasks.get("source_shortlist_blob_sha") != expected_shortlist_sha:
            issues.append("Review-task shortlist blob provenance is stale or mismatched")
    except OSError:
        issues.append("Cannot read provisional shortlist to verify task provenance")

    if triage.get("release_status") != "NOT_A_LINGUISTIC_OR_CEFR_VERIFICATION":
        issues.append("Selection triage cannot represent a verification")
    if triage.get("selected") != 1000:
        issues.append("Selection triage count not 1000")
    if not isinstance(triage.get("screened_source_candidate_rows"), int) or triage.get("screened_source_candidate_rows", 0) < 1000:
        issues.append("Source screening coverage is insufficient")

    entries_by_key = {}
    counts = collections.Counter()
    source_cache = {}
    source_sha_cache = {}
    for n, row in enumerate(rows):
        if not isinstance(row, dict):
            issues.append(f"{n}: shortlist row is not an object")
            continue
        word = row.get("word", "")
        proposed_level = row.get("level")
        if proposed_level not in TARGETS:
            issues.append(f"{n}: invalid level {proposed_level}")
            continue
        counts[proposed_level] += 1
        if not isinstance(word, str) or not HEADWORD.fullmatch(word):
            issues.append(f"{n}: invalid lowercase headword {word!r}")
        key = key_for(word)
        if not key or key in entries_by_key:
            issues.append(f"{n}: repeated or empty normalized headword {word!r}")
        entries_by_key[key] = row
        for field in DRAFT_FIELDS:
            if not isinstance(row.get(field), str) or not row[field].strip():
                issues.append(f"{n}: empty/missing {field}")
        if not MYANMAR.search(str(row.get("burmese_meaning", ""))):
            issues.append(f"{n}: Myanmar text missing")
        if (len(str(row.get("english_definition", ""))) > 300
                or len(str(row.get("example_sentence", ""))) > 350
                or len(str(row.get("burmese_meaning", ""))) > 250):
            issues.append(f"{n}: length limits exceeded")
        for flag in REVIEW_FLAGS:
            if row.get(flag) is not False:
                issues.append(f"{n}: {flag} must be false without independent review")
        for field in ("source_english", "source_burmese", "source_level"):
            if row.get(field) != "":
                issues.append(f"{n}: unverified source claims must remain empty")
        if row.get("editorial_hold") is not True or row.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            issues.append(f"{n}: selection must remain on editorial hold")

        source_path = row.get("source_path", "")
        source_index = row.get("source_index")
        if (not isinstance(source_path, str) or not source_path.startswith("draft/")
                or ".." in pathlib.PurePosixPath(source_path).parts
                or not source_path.endswith(".json")):
            issues.append(f"{n}: unsafe source path")
            continue
        if not isinstance(source_index, int) or isinstance(source_index, bool) or source_index < 0:
            issues.append(f"{n}: invalid source index")
            continue
        try:
            if source_path not in source_cache:
                source_cache[source_path] = read(source_path)["entries"]
                source_sha_cache[source_path] = blob_sha(source_path)
            source = source_cache[source_path][source_index]
        except (OSError, ValueError, IndexError, KeyError, TypeError):
            issues.append(f"{n}: missing/invalid source row {source_path}:{source_index}")
            continue
        if any(row.get(field) != source.get(field) for field in DRAFT_FIELDS):
            issues.append(f"{n}: draft text differs from source row")
        if (source.get("proposed_level") or source.get("level")) != proposed_level:
            issues.append(f"{n}: proposed level differs from source")
        if source_sha_cache[source_path] != row.get("source_blob_sha"):
            issues.append(f"{n}: source file changed; explicit re-triage required")
        if source.get("editorial_risks"):
            issues.append(f"{n}: source has unresolved targeted editorial risk")

    if counts != collections.Counter(TARGETS):
        issues.append(f"Per-level quota mismatch: {dict(counts)}")

    task_by_key = {}
    task_ids = set()
    task_counts = collections.Counter()
    for n, task in enumerate(todo):
        if not isinstance(task, dict):
            issues.append(f"Review task {n} is not an object")
            continue
        word = task.get("headword")
        key = key_for(word)
        if not key or key in task_by_key:
            issues.append(f"Review task duplicate or empty headword: {word!r}")
        task_by_key[key] = task
        matching = entries_by_key.get(key)
        if matching is None:
            issues.append(f"Unmatched review task {word!r}")
            continue
        expected_id = f"CEFR1000-{matching.get('level')}-{n + 1:04d}"
        task_id = task.get("task_id")
        if not isinstance(task_id, str) or task_id in task_ids:
            issues.append(f"Duplicate or missing canonical review task ID for {word}")
        task_ids.add(task_id)
        if task_id != expected_id:
            issues.append(f"Canonical review task ID mismatch for {word}: expected {expected_id}")
        if task.get("level") not in TARGETS:
            issues.append(f"Invalid review task level for {word}")
        task_counts[task.get("level")] += 1
        for field in ("level", "part_of_speech", "source_path", "source_index", "source_blob_sha"):
            shortlist_field = "level" if field == "level" else field
            if task.get(field) != matching.get(shortlist_field):
                issues.append(f"Review task source mismatch for {word}/{field}")
        if task.get("shortlist_blob_sha") != expected_shortlist_sha:
            issues.append(f"Review task shortlist blob SHA mismatch for {word}")
        if task.get("review_status") != "PENDING_INDEPENDENT_REVIEW":
            issues.append(f"Review task falsely completed for {word}")
        if task.get("reviewer_assigned") is not None or task.get("reviewer_identity") is not None or task.get("reviewer_signed_at") is not None:
            issues.append(f"Unverified reviewer identity/assignment/signature present for {word}")
        if task.get("approval") is not False:
            issues.append(f"Review task approval must remain false for {word}")
        for field in TASK_STAGES:
            if task.get(field) != "PENDING":
                issues.append(f"Review task stage must remain pending: {word}/{field}")
        if task.get("source_evidence_urls") != [] or task.get("source_observed_on") is not None:
            issues.append(f"Unverified task source evidence must remain empty/null: {word}")

    if task_counts != collections.Counter(TARGETS):
        issues.append(f"Review-task per-level quota mismatch: {dict(task_counts)}")
    if set(task_by_key) != set(entries_by_key):
        issues.append("Independent review task parity mismatch")

    held = set()
    for path in HOLDS:
        held.update(key_for(x.get("word")) for x in read(path).get("records", []) if x.get("word"))
    conflicts = {key_for(x.get("word")) for x in triage.get("cross_level_conflicting_wordforms", []) if x.get("word")}
    invalid = set(entries_by_key).intersection(held | conflicts)
    if invalid:
        issues.append(f"Previously held/conflicting forms selected: {sorted(invalid)[:15]}")
    if any(x.get("reason") not in SCREENS for x in triage.get("rejected_before_quota", [])):
        issues.append("Invalid selection triage code")

    publication = (ROOT / "cefr-vocabulary-data.js").read_text("utf-8")
    if "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" not in publication:
        issues.append("CEFR publication placeholder status changed")
    if "entries:[]" not in publication:
        issues.append("Unverified staging content published")
    if "targets:{A1:200,A2:200,B1:200,B2:200,C1:200}" not in publication:
        issues.append("CEFR publication placeholder uses wrong quotas")
    if level != "ALL" and level not in TARGETS:
        issues.append("Unrecognized auditor level")
    return issues, dict(counts)


def run_self_tests():
    data = read(DATASET)
    tasks = read(TASKS)
    issues, _ = validate(data=data, tasks=tasks)
    assert not issues, "baseline must pass before mutation tests: " + "; ".join(issues[:5])

    cases = []
    mutated = copy.deepcopy(data)
    mutated["entries"][0]["reviewed_english"] = True
    cases.append(("fake English review", validate(data=mutated)[0]))
    mutated = copy.deepcopy(data)
    mutated["entries"][1]["word"] = mutated["entries"][0]["word"]
    cases.append(("duplicate headword", validate(data=mutated)[0]))
    mutated = copy.deepcopy(data)
    mutated["entries"][0]["editorial_hold"] = False
    cases.append(("premature hold removal", validate(data=mutated)[0]))

    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"][0]["approval"] = True
    cases.append(("fake task approval", validate(tasks=mutated_tasks)[0]))
    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"][0]["source_evidence_urls"] = ["https://example.org/unverified"]
    cases.append(("unverified source URL in independent task metadata", validate(tasks=mutated_tasks)[0]))
    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"][0]["source_observed_on"] = "2026-11-28"
    cases.append(("unverified source observation date in independent task metadata", validate(tasks=mutated_tasks)[0]))
    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"][0]["reviewer_identity"] = "invented-reviewer"
    cases.append(("unverified reviewer identity", validate(tasks=mutated_tasks)[0]))
    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"][0]["english_definition_review"] = "APPROVED"
    cases.append(("fake dimension signoff", validate(tasks=mutated_tasks)[0]))
    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"].pop()
    cases.append(("missing review task", validate(tasks=mutated_tasks)[0]))
    mutated_tasks = copy.deepcopy(tasks)
    mutated_tasks["tasks"][0]["headword"] = "not-the-matching-headword"
    cases.append(("mismatched task headword", validate(tasks=mutated_tasks)[0]))

    for label, errors in cases:
        assert errors, f"mutation unexpectedly passed: {label}"
    print(f"PASS: baseline task schema and {len(cases)} adversarial shortlist/task mutations; no independent approval inferred")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    issues, counts = validate(args.level)
    if args.self_test and not issues:
        run_self_tests()
    if issues:
        for problem in issues[:45]:
            print("BLOCK:", problem, file=sys.stderr)
        print(f"FAIL: {len(issues)} structural problem(s)", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {args.level} 1000 staged review candidates; per-level counts {counts}; 1000 linked pending review tasks; 0 independently approved; NEVER PUBLISH")
    output = {
        "level": args.level,
        "staged_provisional_entries": 200 if args.level != "ALL" else 1000,
        "counts_by_level": counts,
        "independently_verified": {l: 0 for l in LEVELS},
        "audio_listening_verified": False,
        "production_deployed": False,
        "structural_only": True,
    }
    output_name = f"cefr-1000-shortlist-qa-{args.level}.json"
    pathlib.Path(output_name).write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
