#!/usr/bin/env python3
"""Fail-closed staging QA for batch05 editorial review tasks.

This checks structural alignment and honesty of pending-review flags only.
It does NOT establish lexical, Burmese, CEFR, audio or source verification.
"""
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
load = lambda name: json.loads((ROOT / name).read_text(encoding="utf-8"))

def main():
    tasks = load("draft/A2-C1-REVIEW-TASKS-BATCH05.json")
    drafts = load("draft/A2-C1-EDITORIAL-STARTER.json")
    holds = load("draft/A2-C1-CANDIDATE-QUARANTINE.json")
    assert tasks["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert tasks["source_pages_not_yet_checked"] is True
    assert tasks["independently_approved"] == 0
    assert drafts["release_status"] == holds["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    by_word = {x["word"]: x for x in drafts["entries"]}
    held = {x["word"] for x in holds["records"]}
    assert len(by_word) == len(drafts["entries"])
    entries = tasks["entries"]
    assert len(entries) == 40
    assert len({x["word"] for x in entries}) == 40
    assert Counter(x["provisional_level"] for x in entries) == {"A2": 10, "B1": 10, "B2": 10, "C1": 10}
    for task in entries:
        word = task["word"]
        assert word not in held, f"Quarantined word in review batch: {word}"
        draft = by_word[word]
        assert draft["level"] == task["provisional_level"]
        assert draft["part_of_speech"] == task["part_of_speech"]
        assert task["review_status"] == "PENDING_INDEPENDENT_REVIEW"
        assert task["release_approved"] is False
        assert all(draft[f] is False for f in (
            "reviewed_english", "reviewed_burmese", "reviewed_example",
            "reviewed_level", "reviewed_pronunciation"))
        assert not any(draft[f] for f in ("source_english", "source_burmese", "source_level"))
        english = task["english_definition_review"]
        assert english["completed"] is False and english["source_observed"] is False
        url = urlparse(english["reference_url_to_consult"])
        assert url.scheme == "https" and url.netloc == "dictionary.cambridge.org"
        assert url.path == "/dictionary/english/" + word
        assert task["burmese_review"]["completed"] is False
        assert task["burmese_review"]["reviewer"] is None
        assert task["example_review"]["completed"] is False
        assert task["cefr_review"]["completed"] is False
        assert task["audio_review"]["completed"] is False
        if task["provisional_level"] == "C1":
            assert task["priority"] == "HIGH_CEFR_RECLASSIFICATION_RISK"
            assert task["cefr_review"]["provisional_level_risk"]
    assert "entries:[]" in (ROOT / "cefr-vocabulary-data.js").read_text("utf-8")
    print("PASS: 40 new draft-to-task mappings, 10 per level; 0 verified approvals")
    print(f"PASS: {len(held)} held candidates excluded from batch05 review queue")
    print("PASS: dictionary links marked as unconsulted leads; production release data empty")
    print("NOT CHECKED: actual source pages, CEFR accuracy, Burmese semantics, audio, iPhone Safari")

if __name__ == "__main__":
    main()
