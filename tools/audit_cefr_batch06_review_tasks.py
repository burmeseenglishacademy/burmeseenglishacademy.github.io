#!/usr/bin/env python3
"""Fail-closed staging-only batch06 review queue integrity test; NOT semantic approval."""
import json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"draft/A2-C1-EDITORIAL-STARTER.json").read_text("utf8"))
t=json.loads((ROOT/"draft/A2-C1-REVIEW-TASKS-BATCH06.json").read_text("utf8"))
q=json.loads((ROOT/"draft/A2-C1-CANDIDATE-QUARANTINE.json").read_text("utf8"))
assert d["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH" and d["reviewed_independently"]==0
assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
assert t["source_pages_not_yet_checked"] is True and t["independently_approved"]==0
assert len(t["entries"])==80
assert Counter(x["provisional_level"] for x in t["entries"])==Counter({"A2":20,"B1":20,"B2":20,"C1":20})
assert len({x["word"] for x in t["entries"]})==80
by_word={x["word"]:x for x in d["entries"]}
assert len(by_word)==len(d["entries"]) and len(d["entries"])>=584
held={x["word"] for x in q["records"]}
for x in t["entries"]:
    w=x["word"]
    assert w in by_word and w not in held
    row=by_word[w]
    assert row["level"]==x["provisional_level"] and row["part_of_speech"]==x["part_of_speech"]
    assert x["review_status"]=="PENDING_INDEPENDENT_REVIEW" and x["release_approved"] is False
    assert row["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
    for f in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation"):
        assert row[f] is False
    for f in ("source_english","source_burmese","source_level"): assert row[f]==""
    assert x["english_definition_review"]["completed"] is False
    assert x["english_definition_review"]["source_observed"] is False
    assert x["burmese_review"]["completed"] is False and x["burmese_review"]["reviewer"] is None
    assert x["example_review"]["completed"] is False
    assert x["cefr_review"]["completed"] is False
    assert x["audio_review"]["completed"] is False
    if x["provisional_level"]=="C1":
        assert x["priority"]=="HIGH_CEFR_RECLASSIFICATION_RISK"
        assert "UNSUPPORTED" in x["cefr_review"]["provisional_level_risk"]
assert (ROOT/"cefr-vocabulary-data.js").read_text("utf8").find("entries:[]")>=0
print(f"PASS: 80 batch06 review tasks preserved, 20 each A2/B1/B2/C1; {len(d['entries'])} total unverified drafts.")
print("PASS: 0 independent source/Burmese/example/CEFR/audio approvals; 0 held words drafted.")
print("WARNING: C1 placements are provisional and require reclassification review.")
print("STAGING ONLY: no production merge or deployment.")
