#!/usr/bin/env python3
"""Batch19 structural-only staging QA. Never treats drafts as approved."""
import argparse,json,re
from pathlib import Path
from collections import Counter,defaultdict
R=Path(__file__).resolve().parents[1]
def read(p): return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
 d=read("draft/A2-C1-EDITORIAL-BATCH20.json")
 t=read("draft/A2-C1-REVIEW-TASKS-BATCH20.json")
 q=read("draft/A2-C1-QUARANTINE-BATCH20.json")
 pool={x["word"]:x for x in read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
 assert len(pool)==5000
 assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
 assert t["source_pages_not_yet_checked"] is True
 assert d["independently_approved"]==t["independently_approved"]==q["independently_approved"]==0
 assert len(d["entries"])==len(t["entries"])==52
 assert Counter(x["level"] for x in d["entries"])=={"A2":16,"B1":16,"B2":16,"C1":4}
 assert d["counts_by_provisional_level"]=={"A2":16,"B1":16,"B2":16,"C1":4}
 assert len({x["word"] for x in d["entries"]})==len({x["example_sentence"] for x in d["entries"]})==52
 assert len(q["records"])==len({x["word"] for x in q["records"]})==20
 priorfiles=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,20)]
 prior=[x for p in priorfiles for x in read(p)["entries"]]
 assert not {x["word"] for x in prior}&{x["word"] for x in d["entries"]}
 heldfiles=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,21)]
 held=[x["word"] for p in heldfiles for x in read(p)["records"]]
 assert len(held)==len(set(held))
 assert not set(held)&{x["word"] for x in d["entries"]}
 assert all(x["reviewed_independently"] is False and x["release_approved"] is False for p in heldfiles for x in read(p)["records"])
 taskmap={x["word"]:x for x in t["entries"]}
 assert len(taskmap)==52
 for x in d["entries"]:
  if level!="ALL" and x["level"]!=level: continue
  w=x["word"]
  assert w in pool and pool[w]["level"]==x["level"],w
  assert re.fullmatch("[a-z]{3,}",w),w
  assert len(x["english_definition"].strip())>=25,w
  assert re.search(r"[\u1000-\u109f]",x["burmese_meaning"]),w
  assert re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",x["example_sentence"].lower()),w
  assert len(x["example_sentence"].strip())>=25,w
  assert all(x[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),w
  assert all(x[k]=="" for k in ("source_english","source_burmese","source_level")),w
  assert x["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW",w
  y=taskmap[w]
  assert y["provisional_level"]==x["level"] and y["part_of_speech"]==x["part_of_speech"],w
  assert y["release_approved"] is False and y["review_status"]=="PENDING_INDEPENDENT_REVIEW",w
  assert y["english_definition_review"]["source_observed"] is False,w
  assert y["burmese_review"]["reviewer"] is None,w
  assert all(y[k]["completed"] is False for k in ("english_definition_review","burmese_review","example_review","cefr_review","audio_review")),w
 if level=="ALL":
  byword=defaultdict(list)
  for x in prior+d["entries"]: byword[x["word"]].append(x)
  assert len(byword)==1400,len(byword)
  assert Counter(v[0]["level"] for v in byword.values())=={"A2":366,"B1":368,"B2":366,"C1":300}
  assert all(all((x["level"],x["part_of_speech"],x["english_definition"],x["burmese_meaning"],x["example_sentence"])==(v[0]["level"],v[0]["part_of_speech"],v[0]["english_definition"],v[0]["burmese_meaning"],v[0]["example_sentence"]) for x in v[1:]) for v in byword.values())
  print("UNIQUE A2-C1: A2=366 B1=368 B2=366 C1=300 total=1400; independent approvals=0")
  print("A1=500; A1-C1 written=1900; first drafts outstanding=3100; legacy duplicate rows=",sum(len(v)-1 for v in byword.values()))
 assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 print("STAGING ONLY batch20",level,"PASS: 52 drafts, 20 holds, zero approvals; no audio/deploy")
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--level",choices=("A2","B1","B2","C1","ALL"),default="ALL")
 audit(p.parse_args().level)
