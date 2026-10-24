#!/usr/bin/env python3
"""Batch08 unpublished draft/task consistency only; NOT independent linguistic review."""
import argparse,json,re,unicodedata
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
p=argparse.ArgumentParser()
p.add_argument("--level",choices=["ALL","A2","B1","B2","C1"],default="ALL")
level=p.parse_args().level
drafts=load("draft/A2-C1-EDITORIAL-STARTER.json")
tasks=load("draft/A2-C1-REVIEW-TASKS-BATCH08.json")
pool=load("draft/UNVERIFIED_CEFR_CANDIDATES.json")
quarantine=load("draft/A2-C1-CANDIDATE-QUARANTINE.json")
assert drafts["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH" and drafts["reviewed_independently"]==0
assert tasks["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
assert tasks["source_pages_not_yet_checked"] is True and tasks["independently_approved"]==0
assert len(tasks["entries"])==80
assert Counter(t["provisional_level"] for t in tasks["entries"])=={"A2":20,"B1":20,"B2":20,"C1":20}
assert len({t["word"] for t in tasks["entries"]})==80
assert len(drafts["entries"])>=744
assert all(Counter(d["level"] for d in drafts["entries"])[l]>=186 for l in ("A2","B1","B2","C1"))
by_word={x["word"]:x for x in drafts["entries"]}
pool_by_word={x["word"]:x for x in pool["entries"]}
held={x["word"] for x in quarantine["records"]}
assert len(by_word)==len(drafts["entries"])
assert len({x["example_sentence"] for x in drafts["entries"]})==len(drafts["entries"])
for t in tasks["entries"]:
    if level!="ALL" and t["provisional_level"]!=level: continue
    w=t["word"]; d=by_word[w]
    assert w not in held and re.fullmatch(r"[a-z]+",w)
    assert pool_by_word[w]["level"]==d["level"]==t["provisional_level"]
    assert d["part_of_speech"]==t["part_of_speech"]
    assert t["review_status"]=="PENDING_INDEPENDENT_REVIEW" and t["release_approved"] is False
    assert d["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
    assert all(d[f] is False for f in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation"))
    assert all(d[f]=="" for f in ("source_english","source_burmese","source_level"))
    for f in ("english_definition","burmese_meaning","example_sentence","part_of_speech"):
        assert isinstance(d[f],str) and d[f].strip() and unicodedata.normalize("NFC",d[f])==d[f]
    assert re.search(r"[\u1000-\u109f]",d["burmese_meaning"])
    assert d["example_sentence"].lower().find(w)>=0
    assert d["example_sentence"][0].isupper() and d["example_sentence"][-1] in ".?!"
    assert d["source_note"].startswith("Original draft")
    assert t["english_definition_review"]["completed"] is False
    assert t["english_definition_review"]["source_observed"] is False
    assert t["english_definition_review"]["reference_url_to_consult"]=="https://dictionary.cambridge.org/dictionary/english/"+w
    assert t["burmese_review"]["completed"] is False and t["burmese_review"]["reviewer"] is None
    assert t["example_review"]["completed"] is False and t["cefr_review"]["completed"] is False
    assert t["audio_review"]["completed"] is False
    if t["provisional_level"]=="C1":
        assert t["priority"]=="HIGH_CEFR_RECLASSIFICATION_RISK"
        assert "UNSUPPORTED" in t["cefr_review"]["provisional_level_risk"]
assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
print(f"PASS: batch08 {level} 80-task staging queue structurally consistent; zero independent approvals")
print("NOT VERIFIED: exact English sense, natural Myanmar, example grammar, CEFR, George/Emma listening, real iPhone Safari or hosting")
