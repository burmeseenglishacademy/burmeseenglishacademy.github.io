#!/usr/bin/env python3
"""Batch35 unpublished structural audit; never claim linguistic, audio or device approval."""
import argparse
import collections
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A2", "B1", "B2", "C1")
EXPECTED = {"A2": 2, "B1": 22, "B2": 19, "C1": 2}
HELD = {"A2": 3, "B1": 15, "B2": 20, "C1": 47}
TARGET = {"A1": 500, "A2": 700, "B1": 1000, "B2": 1300, "C1": 1500}
POS = {"n": "noun", "v": "verb", "a": "adjective", "s": "adjective", "r": "adverb"}
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation")

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def audit(level):
    if level == "ALL":
        previous = subprocess.run(
            [sys.executable, "tools/audit_cefr_batch34_review_tasks.py", "--level", "ALL"],
            cwd=ROOT, capture_output=True, text=True)
        if previous.returncode:
            raise AssertionError("Batch34 baseline failed: " + previous.stdout + previous.stderr)
        print(previous.stdout.strip())
    draft = read("draft/A2-C1-EDITORIAL-BATCH35.json")
    tasks = read("draft/A2-C1-REVIEW-TASKS-BATCH35.json")
    held = read("draft/A2-C1-QUARANTINE-BATCH35.json")
    poolrows = read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool = {row["word"]: row for row in poolrows}
    assert len(poolrows) == len(pool) == 5000
    assert collections.Counter(x["level"] for x in poolrows) == TARGET
    assert draft["release_status"] == held["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert tasks["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert tasks["source_pages_not_yet_checked"] is True
    assert draft["independently_approved"] == tasks["independently_approved"] == held["independently_approved"] == 0
    assert len(draft["entries"]) == len(tasks["entries"]) == 45
    assert collections.Counter(x["level"] for x in draft["entries"]) == EXPECTED
    assert draft["counts_by_provisional_level"] == EXPECTED
    assert len(held["records"]) == 85
    assert collections.Counter(x["provisional_level"] for x in held["records"]) == HELD
    assert held["counts_by_provisional_level"] == HELD
    newwords = {x["word"] for x in draft["entries"]}
    heldwords = {x["word"] for x in held["records"]}
    assert len(newwords) == 45 and len(heldwords) == 85 and not (newwords & heldwords)
    assert len({x["example_sentence"] for x in draft["entries"]}) == 45
    oldfiles = ["draft/A2-C1-EDITORIAL-STARTER.json"] + [
        f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9, 35)]
    oldrows = [x for path in oldfiles for x in read(path)["entries"]]
    oldheldfiles = ["draft/A2-C1-CANDIDATE-QUARANTINE.json"] + [
        f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14, 35)]
    oldheldrows = [x for path in oldheldfiles for x in read(path)["records"]]
    olddraftwords = {x["word"] for x in oldrows}
    oldheldwords = {x["word"] for x in oldheldrows}
    assert len(olddraftwords) == 2161 and len(oldheldwords) == 591
    assert not newwords & olddraftwords, ("already drafted", newwords & olddraftwords)
    assert not heldwords & oldheldwords, ("already held", heldwords & oldheldwords)
    assert not (heldwords | oldheldwords) & (newwords | olddraftwords), "draft/quarantine collision"
    taskmap = {x["word"]: x for x in tasks["entries"]}
    assert len(taskmap) == 45 and set(taskmap) == newwords
    for row in draft["entries"]:
        if level != "ALL" and row["level"] != level:
            continue
        word = row["word"]
        assert re.fullmatch(r"[a-z]{3,}", word), word
        assert word in pool and pool[word]["level"] == row["level"], word
        assert POS[pool[word]["part_of_speech"]] == row["part_of_speech"], word
        assert len(row["english_definition"].strip()) >= 25, word
        assert re.search(r"[\u1000-\u109f]", row["burmese_meaning"]), word
        assert len(row["example_sentence"].strip()) >= 25, word
        assert re.search(r"(?<![a-z])" + re.escape(word) + r"(?![a-z])",
                         row["example_sentence"].lower()), word
        assert row["example_sentence"][0].isupper() and row["example_sentence"][-1] in ".?!", word
        assert all(row[k] is False for k in FLAGS), word
        assert all(row[k] == "" for k in ("source_english", "source_burmese", "source_level")), word
        assert row["status"] == "AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and row["editorial_risk"], word
        task = taskmap[word]
        assert task["provisional_level"] == row["level"] and task["part_of_speech"] == row["part_of_speech"], word
        assert task["review_status"] == "PENDING_INDEPENDENT_REVIEW" and task["release_approved"] is False, word
        for key in ("english_definition_review", "burmese_review", "example_review", "cefr_review"):
            assert task[key]["completed"] is False and task[key]["reviewer"] is None, word
            assert task[key]["observed_evidence"] is None, word
        assert task["english_definition_review"]["source_observed"] is False, word
        assert task["audio_review"]["completed"] is False and task["audio_review"]["real_listening"] is False, word
        assert task["audio_review"]["real_device_test"] is False and task["audio_review"]["reviewer"] is None, word
    for row in held["records"]:
        assert row["word"] in pool and pool[row["word"]]["level"] == row["provisional_level"], row["word"]
        assert row["source_observed"] is False and row["reviewed_independently"] is False, row["word"]
        assert row["release_approved"] is False and row["risk"] and row["evidence_note"], row["word"]
    if level == "ALL":
        byword = collections.defaultdict(list)
        for row in oldrows + draft["entries"]:
            byword[row["word"]].append(row)
        assert len(byword) == 2206, len(byword)
        counts = collections.Counter(rows[0]["level"] for rows in byword.values())
        assert counts == {"A2": 521, "B1": 638, "B2": 631, "C1": 416}, counts
        for word, versions in byword.items():
            assert all(
                (v["level"], v["part_of_speech"], v["english_definition"],
                 v["burmese_meaning"], v["example_sentence"]) ==
                (versions[0]["level"], versions[0]["part_of_speech"],
                 versions[0]["english_definition"], versions[0]["burmese_meaning"],
                 versions[0]["example_sentence"])
                for v in versions[1:]), ("conflicting historical duplicate", word)
        duplicates = sum(len(rows) - 1 for rows in byword.values())
        assert duplicates == 182, duplicates
        assert len(oldheldwords | heldwords) == 676
        print("UNIQUE A2-C1 A2=521 B1=638 B2=631 C1=416 total=2206; independently approved=0")
        print("A1=500; A1-C1 written=2706; outstanding=2294; quarantine=676; legacy duplicate rows=182")
    assert "entries:[]" in (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print(f"STAGING ONLY batch35 {level} PASS: 45 drafts, 85 held, zero approvals; no audio/deploy")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    audit(parser.parse_args().level)
