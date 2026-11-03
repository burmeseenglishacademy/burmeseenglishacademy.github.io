#!/usr/bin/env python3
"""Fail-closed CEFR-1000 provisional inventory guard; never grants release approval.

Usage: python3 tools/check_cefr_1000_provisional_inventory.py
This guard deliberately checks draft integrity only, NOT independent signoff.
"""
import copy
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("word", "level", "part_of_speech", "english_definition",
          "burmese_meaning", "example_sentence", "source_path",
          "source_index", "source_blob_sha")
REVIEW_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                "reviewed_level", "reviewed_pronunciation", "release_approved")

def check(data):
    errors = []
    if not isinstance(data, dict):
        return ["Root must be an object"]
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"]
    if len(entries) != 1000:
        errors.append(f"Expected 1000 entries, got {len(entries)}")
    counts = Counter()
    seen = {}
    provenance_slots = {}
    provenance_blobs = {}
    for index, entry in enumerate(entries):
        label = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: not an object")
            continue
        for field in FIELDS:
            value = entry.get(field)
            if isinstance(value, str):
                if not value.strip():
                    errors.append(f"{label}: empty {field}")
            elif field == "source_index" and type(value) is int and value >= 0:
                pass
            else:
                errors.append(f"{label}: invalid/missing {field}")
        level = entry.get("level")
        if level not in LEVELS:
            errors.append(f"{label}: invalid level {level!r}")
        else:
            counts[level] += 1
        word = entry.get("word")
        if isinstance(word, str):
            normalized = " ".join(word.casefold().split())
            if normalized in seen:
                errors.append(f"{label}: duplicate headword {word!r} also at {seen[normalized]}")
            seen[normalized] = index
        if entry.get("editorial_hold") is not True:
            errors.append(f"{label}: provisional entry must remain on editorial hold")
        for flag in REVIEW_FLAGS:
            if entry.get(flag) is not False:
                errors.append(f"{label}: {flag} must be explicitly false in provisional inventory")
        source_path = entry.get("source_path")
        source_index = entry.get("source_index")
        if isinstance(source_path, str):
            if (not source_path.startswith("draft/") or not source_path.endswith(".json")
                    or ".." in source_path.split("/") or chr(92) in source_path
                    or source_path.startswith("draft//")):
                errors.append(f"{label}: unsafe/non-draft source_path")
            sha_value = entry.get("source_blob_sha")
            if isinstance(sha_value, str):
                old_sha = provenance_blobs.setdefault(source_path, sha_value)
                if old_sha != sha_value:
                    errors.append(f"{label}: inconsistent source blob for {source_path}")
            if type(source_index) is int and source_index >= 0:
                slot = (source_path, source_index)
                if slot in provenance_slots:
                    errors.append(f"{label}: reused historical source slot at {provenance_slots[slot]}")
                provenance_slots[slot] = index
        sha = entry.get("source_blob_sha")
        if not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
            errors.append(f"{label}: invalid historical blob SHA")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: expected 200, got {counts[level]}")
        if data.get("counts_by_level", {}).get(level) != 200:
            errors.append(f"{level}: declared count not 200")
        if data.get("independently_approved_by_level", {}).get(level) != 0:
            errors.append(f"{level}: provisional independent approvals must remain zero")
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("Provisional release_status altered")
    if data.get("stages", {}).get("production") != "UNMODIFIED":
        errors.append("Provisional production status altered")
    return errors

def adversarial_self_test(data):
    """Mutation tests must reject forged inventory and approvals; no human review implied."""
    cases = [
        ("missing-entry", lambda d: d["entries"].pop()),
        ("duplicate-headword", lambda d: d["entries"][1].__setitem__("word", d["entries"][0]["word"])),
        ("casefold-duplicate", lambda d: d["entries"][1].__setitem__("word", d["entries"][0]["word"].upper())),
        ("wrong-level", lambda d: d["entries"][0].__setitem__("level", "C9")),
        ("empty-myanmar", lambda d: d["entries"][0].__setitem__("burmese_meaning", "  ")),
        ("empty-example", lambda d: d["entries"][0].__setitem__("example_sentence", "")),
        ("missing-provenance", lambda d: d["entries"][0].pop("source_path", None)),
        ("unsafe-provenance-path", lambda d: d["entries"][0].__setitem__("source_path", "../outside.json")),
        ("duplicate-provenance-slot", lambda d: (d["entries"][1].__setitem__("source_path", d["entries"][0]["source_path"]), d["entries"][1].__setitem__("source_index", d["entries"][0]["source_index"]))),
        ("inconsistent-provenance-blob", lambda d: d["entries"][0].__setitem__("source_blob_sha", "a" * 40 if d["entries"][0]["source_blob_sha"] != "a" * 40 else "b" * 40)),
        ("forged-blob-sha", lambda d: d["entries"][0].__setitem__("source_blob_sha", "not-a-sha")),
        ("removed-editorial-hold", lambda d: d["entries"][0].__setitem__("editorial_hold", False)),
        ("forged-english-signoff", lambda d: d["entries"][0].__setitem__("reviewed_english", True)),
        ("forged-burmese-signoff", lambda d: d["entries"][0].__setitem__("reviewed_burmese", True)),
        ("forged-example-signoff", lambda d: d["entries"][0].__setitem__("reviewed_example", True)),
        ("forged-level-signoff", lambda d: d["entries"][0].__setitem__("reviewed_level", True)),
        ("forged-audio-signoff", lambda d: d["entries"][0].__setitem__("reviewed_pronunciation", True)),
        ("forged-release-approval", lambda d: d["entries"][0].__setitem__("release_approved", True)),
        ("forged-level-count", lambda d: d["counts_by_level"].__setitem__("A1", 201)),
        ("forged-independent-count", lambda d: d["independently_approved_by_level"].__setitem__("B2", 1)),
        ("forged-release-status", lambda d: d.__setitem__("release_status", "APPROVED")),
        ("forged-production-status", lambda d: d["stages"].__setitem__("production", "DEPLOYED")),
    ]
    if check(data):
        return ["Baseline inventory fails before adversarial tests"]
    failures = []
    for name, mutate in cases:
        altered = copy.deepcopy(data)
        mutate(altered)
        if not check(altered):
            failures.append("Mutation escaped detection: " + name)
    if not failures:
        print(f"PASS: {len(cases)}/{len(cases)} synthetic inventory and approval forgeries rejected; no independent signoff")
    return failures

def main():
    try:
        data = json.loads(PATH.read_text(encoding="utf-8"))
        errors = check(data)
        if not errors:
            errors.extend(adversarial_self_test(data))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors = [f"Unable to read inventory: {exc}"]
    for error in errors:
        print("FAIL:", error)
    if errors:
        print(f"BLOCKED: {len(errors)} inventory integrity failure(s); no release permission")
        return 1
    print("PASS: provisional 1000 inventory structure and zero-approval hold only.")
    print("RELEASE BLOCKED: independent review, audio listening, iPhone and deployment not verified.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
