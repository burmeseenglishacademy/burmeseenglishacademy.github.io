#!/usr/bin/env python3
"""Read-only CEFR-1000 staging audit; never grants independent approval."""
import collections
import json
import pathlib
import re
import sys

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")

def audit(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["root must be a JSON object"], warnings, {}
    entries = data.get("entries")
    if not isinstance(entries, list):
        return ["entries is not a list"], warnings, {}
    for metadata in ("counts_by_level", "independently_approved_by_level", "scope_target"):
        if not isinstance(data.get(metadata), dict):
            errors.append(f"{metadata} must be an object")
    counts = collections.Counter()
    seen = collections.defaultdict(list)
    source_seen = collections.defaultdict(list)
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"{index}: invalid entry")
            continue
        level = entry.get("level")
        if level not in LEVELS:
            errors.append(f"{index}: invalid level")
        else:
            counts[level] += 1
        for field in ("word", "part_of_speech", "english_definition",
                      "burmese_meaning", "example_sentence", "source_path",
                      "source_blob_sha"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append(f"{index}: missing {field}")
        word = entry.get("word")
        pos = entry.get("part_of_speech")
        if isinstance(word, str) and isinstance(pos, str):
            seen[(word.strip().casefold(), pos.strip().casefold())].append(index)
            if word == "i":
                warnings.append(f"{index}: lowercase English pronoun I")
        if type(entry.get("source_index")) is not int or entry["source_index"] < 0:
            errors.append(f"{index}: invalid source_index")
        source_path = entry.get("source_path")
        source_sha = entry.get("source_blob_sha")
        source_index = entry.get("source_index")
        if isinstance(source_path, str) and source_path.strip():
            if not source_path.startswith("draft/") or ".." in source_path.split("/"):
                errors.append(f"{index}: invalid draft source_path")
        if not isinstance(source_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", source_sha):
            errors.append(f"{index}: invalid source_blob_sha")
        if isinstance(source_path, str) and isinstance(source_sha, str) and type(source_index) is int and source_index >= 0:
            source_seen[(source_path, source_sha, source_index)].append(index)
        if entry.get("editorial_hold") is not True:
            errors.append(f"{index}: editorial hold missing")
        for flag in FLAGS:
            if entry.get(flag) is not False:
                errors.append(f"{index}: {flag} not false")
        burmese = entry.get("burmese_meaning")
        if isinstance(burmese, str) and not re.search(r"[\u1000-\u109f]", burmese):
            warnings.append(f"{index}: no Myanmar script")
        example = entry.get("example_sentence")
        if isinstance(example, str) and not re.search(r"[.!?]$", example.strip()):
            warnings.append(f"{index}: example punctuation")
    for level in LEVELS:
        if counts[level] != 200:
            errors.append(f"{level}: {counts[level]} entries, expected 200")
        if not isinstance(data.get("counts_by_level"), dict) or type(data["counts_by_level"].get(level)) is not int or data["counts_by_level"][level] != counts[level]:
            errors.append(f"{level}: count metadata mismatch")
        if not isinstance(data.get("scope_target"), dict) or type(data["scope_target"].get(level)) is not int or data["scope_target"][level] != 200:
            errors.append(f"{level}: scope target metadata mismatch")
        if not isinstance(data.get("independently_approved_by_level"), dict) or type(data["independently_approved_by_level"].get(level)) is not int or data["independently_approved_by_level"][level] != 0:
            errors.append(f"{level}: nonzero approval metadata")
    if len(entries) != 1000:
        errors.append("total is not 1000")
    for identity, indexes in seen.items():
        if len(indexes) > 1:
            errors.append(f"duplicate normalized headword/POS {identity}: {indexes}")
    for source_identity, indexes in source_seen.items():
        if len(indexes) > 1:
            errors.append(f"duplicate source provenance {source_identity}: {indexes}")
    if data.get("release_status") != "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH":
        errors.append("release hold status changed")
    return errors, warnings, dict(counts)

if __name__ == "__main__":
    path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    errors, warnings, counts = audit(json.loads(path.read_text(encoding="utf-8")))
    print(json.dumps({"result": "FAIL" if errors else "STRUCTURAL_ONLY_PASS",
                      "counts": counts, "errors": errors, "editorial_warnings": warnings,
                      "release_authorized": False,
                      "note": "No independent review, publisher evidence, listening or device QA is inferred."},
                     ensure_ascii=False, indent=2))
    sys.exit(bool(errors))
