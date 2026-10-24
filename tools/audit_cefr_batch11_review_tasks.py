#!/usr/bin/env python3
"""Fail-closed batch11 structure/quarantine QA. NEVER linguistic, CEFR, or audio approval."""
import argparse,json,re,unicodedata
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
COUNTS={"A2":20,"B1":20,"B2":20,"C1":2}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
def read(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def check(level):
 m=read("draft/A2-C1-EDITORIAL-STARTER.json")
 b=read("draft/A2-C1-EDITORIAL-BATCH11.json")
 t=read("draft/A2-C1-REVIEW-TASKS-BATCH11.json")
 q=read("draft/A2-C1-CANDIDATE-QUARANTINE.json")
 pool=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")
 assert m["release_status"]==b["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
 assert m["reviewed_independently"]==b["independently_approved"]==t["independently_approved"]==0
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"] is True
 assert len(b["entries"])==len(t["entries"])==62
 assert Counter(x["level"] for x in b["entries"])==COUNTS
 assert Counter(x["provisional_level"] for x in t["entries"])==COUNTS
 assert len(m["entries"])==926
 assert Counter(x["level"] for x in m["entries"])=={"A2":236,"B1":236,"B2":236,"C1":218}
 assert len({x["word"] for x in m["entries"]})==len(m["entries"])
 assert len({x["example_sentence"] for x in m["entries"]})==len(m["entries"])
 assert len(q["records"])>=136
 assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 master={x["word"]:x for x in m["entries"]}
 cand={x["word"]:x for x in pool["entries"]}
 held={x["word"] for x in q["records"]}
 review={x["word"]:x for x in t["entries"]}
 assert len(review)==62
 for d in b["entries"]:
  w=d["word"]
  if level!="ALL" and d["level"]!=level: continue
  assert re.fullmatch("[a-z]+",w) and w not in held
  assert cand[w]["level"]==d["level"] and master[w]==d
  assert review[w]["provisional_level"]==d["level"] and review[w]["part_of_speech"]==d["part_of_speech"]
  assert all(d[k] is False for k in FLAGS)
  assert all(d[k]=="" for k in ("source_english","source_burmese","source_level"))
  assert d["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
  assert d["english_definition"].strip() and d["part_of_speech"].strip()
  assert any(0x1000<=ord(ch)<=0x109F for ch in d["burmese_meaning"])
  assert re.search(r"(?<![A-Za-z])"+re.escape(w)+r"(?![A-Za-z])",d["example_sentence"],re.I),w
  assert 25<=len(d["example_sentence"])<=180
  assert not any(s in d["english_definition"].lower() for s in ("placeholder","todo","tbd"))
  task=review[w]
  assert task["review_status"]=="PENDING_INDEPENDENT_REVIEW" and task["release_approved"] is False
  assert task["english_definition_review"]["source_observed"] is False
  assert task["english_definition_review"]["completed"] is False
  assert task["english_definition_review"]["reference_url_to_consult"].endswith("/"+w)
  assert all(task[k]["completed"] is False for k in ("burmese_review","example_review","cefr_review","audio_review"))
 print(f"BATCH11 {level}: PASS structural/quarantine/candidate alignment only; 62 new unverified drafts; ZERO independent approvals; NO deploy")
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--level",choices=[*LEVELS,"ALL"],default="ALL");check(p.parse_args().level)
