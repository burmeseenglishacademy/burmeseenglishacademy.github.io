#!/usr/bin/env python3
"""Staging-only batch07 structural/queue integrity checks. Not independent editorial approval."""
import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
p=argparse.ArgumentParser()
p.add_argument("--level", choices=["ALL","A2","B1","B2","C1"],default="ALL")
level=p.parse_args().level
drafts=load("draft/A2-C1-EDITORIAL-STARTER.json")
tasks=load("draft/A2-C1-REVIEW-TASKS-BATCH07.json")
holds=load("draft/A2-C1-CANDIDATE-QUARANTINE.json")
pool=load("draft/UNVERIFIED_CEFR_CANDIDATES.json")
assert drafts["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH" and drafts["reviewed_independently"]==0
assert tasks["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
assert tasks["source_pages_not_yet_checked"] is True and tasks["independently_approved"]==0
assert len(tasks["entries"])==80
assert Counter(t["provisional_level"] for t in tasks["entries"])=={"A2":20,"B1":20,"B2":20,"C1":20}
by_word={x["word"]:x for x in drafts["entries"]}
pool_map={x["word"]:x for x in pool["entries"]}
held={x["word"] for x in holds["records"]}
assert len(by_word)==len(drafts["entries"]) and len(drafts["entries"])>=664
assert all(Counter(x["level"] for x in drafts["entries"])[l]>=166 for l in ("A2","B1","B2","C1"))
assert len({x["example_sentence"] for x in drafts["entries"]})==len(drafts["entries"])
assert len({t["word"] for t in tasks["entries"]})==80
for t in tasks["entries"]:
 if level!="ALL" and t["provisional_level"]!=level: continue
 word=t["word"]; row=by_word[word]
 assert word not in held and pool_map[word]["level"]==row["level"]==t["provisional_level"]
 assert row["part_of_speech"]==t["part_of_speech"]
 assert re.fullmatch(r"[a-z]+(?:'[a-z]+)?",word)
 assert t["review_status"]=="PENDING_INDEPENDENT_REVIEW" and t["release_approved"] is False
 assert row["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
 assert all(row[f] is False for f in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation"))
 assert all(row[f]=="" for f in ("source_english","source_burmese","source_level"))
 for f in ("english_definition","burmese_meaning","example_sentence","part_of_speech"):
  assert isinstance(row[f],str) and row[f].strip() and unicodedata.normalize("NFC",row[f])==row[f]
 assert re.search(r"[\u1000-\u109f]",row["burmese_meaning"])
 assert word in row["example_sentence"].lower() and row["example_sentence"][-1] in ".?!"
 assert t["english_definition_review"]["completed"] is False and t["english_definition_review"]["source_observed"] is False
 assert t["english_definition_review"]["reference_url_to_consult"]=="https://dictionary.cambridge.org/dictionary/english/"+word
 assert t["burmese_review"]["completed"] is False and t["burmese_review"]["reviewer"] is None
 assert t["example_review"]["completed"] is False
 assert t["cefr_review"]["completed"] is False
 assert t["audio_review"]["completed"] is False
 if t["provisional_level"]=="C1":
  assert t["priority"]=="HIGH_CEFR_RECLASSIFICATION_RISK"
  assert "UNSUPPORTED" in t["cefr_review"]["provisional_level_risk"]
assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text("utf-8")
print(f"PASS: batch07 {level} staging queue structurally consistent; 0 independent approvals")
print("NOT VERIFIED: dictionary sense, Myanmar meaning, CEFR, listening, mobile Safari, hosting")
