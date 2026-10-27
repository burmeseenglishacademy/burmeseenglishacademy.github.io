#!/usr/bin/env python3
"""Fail-closed STRUCTURAL QA for the 1,000-entry provisional CEFR shortlist.

This checks source linkage, selection conflicts, independent-review-task parity
and nonpublication. It NEVER certifies English/Myanmar quality, CEFR or audio.
"""
import argparse
import collections
import hashlib
import json
import pathlib
import re
import sys

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
TASK_STAGES = ("english_sense", "myanmar_meaning", "usage_example", "cefr_level")
SCREENS = ("CURRICULUM_OR_SENSE_LEVEL_DOUBT", "EXISTING_CANDIDATE_OR_CROSS_LEVEL_HOLD",
           "CROSS_LEVEL_SOURCE_CONFLICT", "MISSING_OR_INVALID_DRAFT_FIELD",
           "SOURCE_EDITORIAL_RISK_FLAGGED", "DUPLICATE_HEADWORD_SOURCE", "NONCANONICAL_OR_NAMED_FORM")


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def blob_sha(path):
    b = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def validate(level="ALL", data=None, tasks=None, triage=None):
    issues = []
    data = data if data is not None else read(DATASET)
    tasks = tasks if tasks is not None else read(TASKS)
    triage = triage if triage is not None else read(TRIAGE)
    rows = data.get("entries", [])
    todo = tasks.get("entries", [])
    if not isinstance(rows, list) or len(rows) != 1000:
        issues.append("Exactly 1000 provisional shortlist rows required")
        return issues, {}
    if not isinstance(todo, list) or len(todo) != 1000:
        issues.append("Exactly 1000 independent review tasks required")
        return issues, {}
    if data.get("scope_target") != TARGETS or data.get("counts_by_level") != TARGETS:
        issues.append("Approved scope 200 entries per level not respected")
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        issues.append("Shortlist must remain unpublished / unverified")
    if tasks.get("release_status") != "ALL_REVIEW_TASKS_PENDING_NOT_APPROVED":
        issues.append("Review tasks must remain pending")
    if triage.get("release_status") != "NOT_A_LINGUISTIC_OR_CEFR_VERIFICATION":
        issues.append("Selection triage cannot represent a verification")
    if triage.get("selected") != 1000:
        issues.append("Selection triage count not 1000")
    if triage.get("screened_source_candidate_rows", 0) < 1000:
        issues.append("Source screening coverage is insufficient")
    if not all(data.get("independently_approved_by_level", {}).get(l) == 0 for l in LEVELS):
        issues.append("False positive independent approval counts")
    entries_by_key = {}
    counts = collections.Counter()
    source_cache = {}
    source_sha_cache = {}
    for n, row in enumerate(rows):
        word = row.get("word", "")
        proposed_level = row.get("level")
        if proposed_level not in TARGETS:
            issues.append(f"{n}: invalid level {proposed_level}")
            continue
        counts[proposed_level] += 1
        if not HEADWORD.fullmatch(word):
            issues.append(f"{n}: invalid lowercase headword {word!r}")
        if word in entries_by_key:
            issues.append(f"{n}: repeated headword {word}")
        entries_by_key[word] = row
        for field in DRAFT_FIELDS:
            if not isinstance(row.get(field), str) or not row[field].strip():
                issues.append(f"{n}: empty/missing {field}")
        if not MYANMAR.search(str(row.get("burmese_meaning", ""))):
            issues.append(f"{n}: Myanmar text missing")
        if len(str(row.get("english_definition", ""))) > 300 or len(str(row.get("example_sentence", ""))) > 350 or len(str(row.get("burmese_meaning", ""))) > 250:
            issues.append(f"{n}: length limits exceeded")
        for flag in REVIEW_FLAGS:
            if row.get(flag) is not False:
                issues.append(f"{n}: {flag} must be false without independent review")
        for field in ("source_english", "source_burmese", "source_level"):
            if row.get(field) != "":
                issues.append(f"{n}: unverified source claims must remain empty")
        if row.get("editorial_hold") is not True or row.get("status") != "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING":
            issues.append(f"{n}: selection must remain on editorial hold")
        path = row.get("source_path", "")
        idx = row.get("source_index")
        if not isinstance(path, str) or not path.startswith("draft/") or ".." in path or not path.endswith(".json"):
            issues.append(f"{n}: unsafe source path")
            continue
        try:
            if path not in source_cache:
                source_cache[path] = read(path)["entries"]
                source_sha_cache[path] = blob_sha(path)
            source = source_cache[path][idx] if isinstance(idx, int) else None
        except (OSError, ValueError, IndexError, KeyError, TypeError):
            issues.append(f"{n}: missing/invalid source row {path}:{idx}")
            continue
        if source is None or any(row.get(field) != source.get(field) for field in DRAFT_FIELDS):
            issues.append(f"{n}: draft text differs from source row")
        if (source.get("proposed_level") or source.get("level")) != proposed_level:
            issues.append(f"{n}: proposed level differs from source")
        if source_sha_cache[path] != row.get("source_blob_sha"):
            issues.append(f"{n}: source file changed; explicit re-triage required")
        if source.get("editorial_risks"):
            issues.append(f"{n}: source has unresolved targeted editorial risk")
    if counts != collections.Counter(TARGETS):
        issues.append(f"Per-level quota mismatch: {dict(counts)}")
    task_by_word = {}
    for n, t in enumerate(todo):
        word = t.get("word")
        if word in task_by_word:
            issues.append(f"Review task duplicate for {word}")
        task_by_word[word] = t
        matching = entries_by_key.get(word)
        if matching is None:
            issues.append(f"Unmatched review task {word}")
            continue
        if t.get("proposed_level") != matching.get("level") or t.get("source_path") != matching.get("source_path") or t.get("source_index") != matching.get("source_index"):
            issues.append(f"Review task source mismatch for {word}")
        if t.get("review_status") != "PENDING_INDEPENDENT_HUMAN_EVIDENCE" or t.get("release_approved") is not False:
            issues.append(f"Review task falsely completed for {word}")
        for field in TASK_STAGES:
            record = t.get(field, {})
            if record.get("reviewed") is not False or record.get("reviewer") is not None or not record.get("task"):
                issues.append(f"Review task stage falsely completed / missing: {word}/{field}")
        audio = t.get("george_emma_audio", {})
        if any(audio.get(f) is not False for f in ("generated", "george_listened", "emma_listened")) or audio.get("reviewer") is not None:
            issues.append(f"Unverified audio falsely approved for {word}")
    if set(task_by_word) != set(entries_by_key):
        issues.append("Independent review parity mismatch")
    held = set()
    for p in HOLDS:
        held.update(x["word"].lower() for x in read(p)["records"])
    conflicts = {x["word"] for x in triage.get("cross_level_conflicting_wordforms", [])}
    invalid = set(entries_by_key).intersection(held | conflicts)
    if invalid:
        issues.append(f"Previously held/conflicting forms selected: {sorted(invalid)[:15]}")
    if any(x.get("reason") not in SCREENS for x in triage.get("rejected_before_quota", [])):
        issues.append("Invalid selection triage code")
    if "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" not in (ROOT / "cefr-vocabulary-data.js").read_text("utf-8"):
        issues.append("CEFR publication placeholder status changed")
    if "entries:[]" not in (ROOT / "cefr-vocabulary-data.js").read_text("utf-8"):
        issues.append("Unverified staging content published")
    if "targets:{A1:200,A2:200,B1:200,B2:200,C1:200}" not in (ROOT / "cefr-vocabulary-data.js").read_text("utf-8"):
        issues.append("CEFR publication placeholder uses wrong quotas")
    if level != "ALL" and level not in TARGETS:
        issues.append("Unrecognized auditor level")
    return issues, dict(counts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    issues, counts = validate(args.level)
    if args.self_test and not issues:
        import copy
        obj = read(DATASET)
        obj["entries"][0]["reviewed_english"] = True
        assert any("reviewed_english must be false" in e for e in validate(data=obj)[0])
        obj = read(DATASET)
        obj["entries"][1]["word"] = obj["entries"][0]["word"]
        assert any("repeated headword" in e for e in validate(data=obj)[0])
        obj = read(DATASET)
        obj["entries"][0]["editorial_hold"] = False
        assert any("must remain on editorial hold" in e for e in validate(data=obj)[0])
        print("PASS: negative tests blocked fake English review, duplicate and premature hold removal")
    if issues:
        for s in issues[:45]:
            print("BLOCK:", s, file=sys.stderr)
        print(f"FAIL: {len(issues)} structural problem(s)", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {args.level} 1000 staged review candidates; per-level counts {counts}; 1000 linked review tasks; 0 independently approved; NEVER PUBLISH")
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
