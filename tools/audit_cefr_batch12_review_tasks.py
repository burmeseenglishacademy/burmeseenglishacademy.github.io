#!/usr/bin/env python3
"""Staging-only structural audit of batch12. NOT a linguistic, CEFR or audio approval."""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A2", "B1", "B2", "C1")
EXPECTED = {level: 20 for level in LEVELS}
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation")

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def audit(level):
    batch = load("draft/A2-C1-EDITORIAL-BATCH12.json")
    tasks = load("draft/A2-C1-REVIEW-TASKS-BATCH12.json")
    master = load("draft/A2-C1-EDITORIAL-STARTER.json")
    quarantine = load("draft/A2-C1-CANDIDATE-QUARANTINE.json")
    candidates = load("draft/UNVERIFIED_CEFR_CANDIDATES.json")
    assert batch["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert tasks["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert batch["independently_approved"] == tasks["independently_approved"] == 0
    assert tasks["source_pages_not_yet_checked"] is True
    assert len(batch["entries"]) == len(tasks["entries"]) == 80
    assert Counter(x["level"] for x in batch["entries"]) == EXPECTED
    assert Counter(x["provisional_level"] for x in tasks["entries"]) == EXPECTED
    assert batch["counts_by_provisional_level"] == EXPECTED
    assert len(master["entries"]) == 926
    assert len(quarantine["records"]) >= 136
    held = {x["word"] for x in quarantine["records"]}
    already = {x["word"] for x in master["entries"]}
    pool = {x["word"]: x for x in candidates["entries"]}
    assert len(pool) == 5000
    assert len({x["word"] for x in batch["entries"]}) == 80
    assert len({x["example_sentence"] for x in batch["entries"]}) == 80
    review = {x["word"]: x for x in tasks["entries"]}
    assert len(review) == 80
    for item in batch["entries"]:
        if level != "ALL" and item["level"] != level:
            continue
        word = item["word"]
        assert word not in already and word not in held, word
        assert word in pool and pool[word]["level"] == item["level"], word
        assert re.fullmatch(r"[a-z]{3,}", word), word
        assert len(item["english_definition"].strip()) >= 20, word
        assert len(item["burmese_meaning"].strip()) >= 4, word
        assert re.search(r"[\u1000-\u109F]", item["burmese_meaning"]), word
        assert re.search(r"(?<![a-z])" + re.escape(word) + r"(?![a-z])", item["example_sentence"].lower()), word
        assert len(item["example_sentence"].strip()) >= 20, word
        assert all(item[flag] is False for flag in FLAGS), word
        assert all(item[field] == "" for field in ("source_english", "source_burmese", "source_level")), word
        assert item["status"] == "AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW", word
        task = review[word]
        assert task["provisional_level"] == item["level"], word
        assert task["part_of_speech"] == item["part_of_speech"], word
        assert task["release_approved"] is False, word
        assert task["review_status"] == "PENDING_INDEPENDENT_REVIEW", word
        assert task["english_definition_review"]["source_observed"] is False, word
        assert task["burmese_review"]["reviewer"] is None, word
        assert all(task[key]["completed"] is False for key in (
            "english_definition_review", "burmese_review", "example_review",
            "cefr_review", "audio_review")), word
    assert "entries:[]" in (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print("STAGING ONLY: batch12", level, "structure PASS; 80 drafts, 0 approvals; no audio or deploy")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    args = parser.parse_args()
    audit(args.level)
