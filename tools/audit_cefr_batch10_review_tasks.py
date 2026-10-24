#!/usr/bin/env python3
"""Fail-closed structural QA for unpublished batch10; NOT linguistic or audio approval."""
import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A2", "B1", "B2", "C1")
REVIEW_FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
                "reviewed_level", "reviewed_pronunciation")

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def check():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=[*LEVELS, "ALL"], default="ALL")
    level = p.parse_args().level
    master = load("draft/A2-C1-EDITORIAL-STARTER.json")
    batch = load("draft/A2-C1-EDITORIAL-BATCH10.json")
    tasks = load("draft/A2-C1-REVIEW-TASKS-BATCH10.json")
    pool = load("draft/UNVERIFIED_CEFR_CANDIDATES.json")
    quarantine = load("draft/A2-C1-CANDIDATE-QUARANTINE.json")
    assert master["release_status"] == batch["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert master["reviewed_independently"] == batch["independently_approved"] == 0
    assert tasks["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert tasks["source_pages_not_yet_checked"] is True
    assert tasks["independently_approved"] == 0
    assert len(batch["entries"]) == len(tasks["entries"]) == 40
    assert Counter(x["level"] for x in batch["entries"]) == dict.fromkeys(LEVELS, 20)
    assert Counter(x["provisional_level"] for x in tasks["entries"]) == dict.fromkeys(LEVELS, 20)
    assert len(master["entries"]) >= 864
    assert all(Counter(x["level"] for x in master["entries"])[l] >= 216 for l in LEVELS)
    master_by_word = {x["word"]: x for x in master["entries"]}
    pool_by_word = {x["word"]: x for x in pool["entries"]}
    held = {x["word"] for x in quarantine["records"]}
    batch_by_word = {x["word"]: x for x in batch["entries"]}
    tasks_by_word = {x["word"]: x for x in tasks["entries"]}
    assert len(master_by_word) == len(master["entries"])
    assert len(batch_by_word) == len(tasks_by_word) == 40
    assert set(batch_by_word) == set(tasks_by_word)
    assert len({x["example_sentence"] for x in master["entries"]}) == len(master["entries"])
    assert "entries:[]" in (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
    for word, d in batch_by_word.items():
        if level != "ALL" and d["level"] != level:
            continue
        t = tasks_by_word[word]
        assert word not in held and re.fullmatch(r"[a-z]+", word), word
        assert pool_by_word[word]["level"] == d["level"] == t["provisional_level"], word
        assert d == master_by_word[word], word
        assert d["part_of_speech"] == t["part_of_speech"]
        assert d["status"] == "AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
        assert d["source_note"].startswith("Original draft")
        assert all(d[f] is False for f in REVIEW_FLAGS)
        assert all(d[f] == "" for f in ("source_english", "source_burmese", "source_level"))
        for f in ("english_definition", "burmese_meaning", "example_sentence", "part_of_speech"):
            assert isinstance(d[f], str) and d[f].strip(), (word, f)
            assert unicodedata.normalize("NFC", d[f]) == d[f], (word, f)
        assert re.search(r"[\u1000-\u109f]", d["burmese_meaning"]), word
        ex = d["example_sentence"]
        assert word in ex.lower() and ex[0].isupper() and ex[-1] in ".?!", word
        assert len(ex) <= 180 and len(d["english_definition"]) <= 300
        assert t["review_status"] == "PENDING_INDEPENDENT_REVIEW"
        assert t["release_approved"] is False
        assert t["english_definition_review"]["completed"] is False
        assert t["english_definition_review"]["source_observed"] is False
        assert t["english_definition_review"]["reference_url_to_consult"] == (
            "https://dictionary.cambridge.org/dictionary/english/" + word)
        assert t["burmese_review"]["completed"] is False and t["burmese_review"]["reviewer"] is None
        assert t["example_review"]["completed"] is False
        assert t["cefr_review"]["completed"] is False
        assert t["audio_review"]["completed"] is False
        if d["level"] == "C1":
            assert t["priority"] == "HIGH_CEFR_RECLASSIFICATION_RISK"
            assert "UNSUPPORTED_C1" in t["cefr_review"]["provisional_level_risk"]
    count = 40 if level == "ALL" else 10
    print(f"PASS: batch10 {level} {count} original bilingual DRAFTS with separate pending review tasks")
    print("NOT APPROVED: sense/POS, Myanmar, grammar, CEFR, Cambridge source, George/Emma listening")
    print("NOT DEPLOYED: no vocabulary release, audio release, browser/device signoff or live publication")

if __name__ == "__main__":
    check()
