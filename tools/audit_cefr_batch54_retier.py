#!/usr/bin/env python3
"""Batch54 structural, collision and production guard; never linguistic approval."""
import argparse, collections, json, re, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
COUNTS={"A2":12,"B1":16,"B2":18,"C1":2}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
def read(p):return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
 d=read("draft/A2-C1-RETIER-EDITORIAL-BATCH54.json")
 t=read("draft/A2-C1-RETIER-REVIEW-TASKS-BATCH54.json")
 q=read("draft/A2-C1-RETIER-QUARANTINE-BATCH54.json")
 poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
 pool={x["word"]:x for x in poolrows}
 assert len(pool)==len(poolrows)==5000
 assert d["release_status"]=="UNVERIFIED_RETIER_DRAFT_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"]
 assert q["release_status"]=="UNVERIFIED_CANDIDATE_HOLDS_DO_NOT_PUBLISH"
 assert all(x["independently_approved"]==0 for x in (d,t,q))
 assert d["counts_by_proposed_level"]==t["counts_by_proposed_level"]==COUNTS
 assert len(d["entries"])==len(t["entries"])==48 and len(q["records"])==12
 words={x["word"]:x for x in d["entries"]}
 tasks={x["word"]:x for x in t["entries"]}
 held={x["word"]:x for x in q["records"]}
 assert len(words)==len(tasks)==48 and len(held)==12 and set(words)==set(tasks) and not set(words)&set(held)
 assert collections.Counter(x["proposed_level"] for x in d["entries"])==COUNTS
 assert len({x["example_sentence"] for x in d["entries"]})==48
 prior=[R/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((R/"draft").glob("A2-C1-EDITORIAL-BATCH*.json")),R/"draft/A2-C1-RETIER-EDITORIAL-BATCH52.json",R/"draft/A2-C1-RETIER-EDITORIAL-BATCH53.json"]
 priorq=[R/"draft/A2-C1-CANDIDATE-QUARANTINE.json",*sorted((R/"draft").glob("A2-C1-QUARANTINE-BATCH*.json")),R/"draft/A2-C1-RETIER-QUARANTINE-BATCH52.json",R/"draft/A2-C1-RETIER-QUARANTINE-BATCH53.json"]
 used={x["word"] for p in prior for x in read(p.relative_to(R))["entries"]}
 used|={x["word"] for p in priorq for x in read(p.relative_to(R))["records"]}
 collision=(set(words)|set(held))&used
 assert not collision, f"prior draft/hold collision: {sorted(collision)}"
 for w,e in words.items():
  assert re.fullmatch(r"[a-z]{3,}",w) and w in pool,w
  assert pool[w]["level"]==e["source_pool_level"]=="C1",w
  assert POS[pool[w]["part_of_speech"]]==e["part_of_speech"],(w,pool[w]["part_of_speech"],e["part_of_speech"])
  assert len(e["english_definition"])>=25 and re.search(r"[\u1000-\u109f]",e["burmese_meaning"]),w
  s=e["example_sentence"]
  assert len(s)>=25 and s[0].isupper() and s[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",s.lower()),w
  assert all(e[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),w
  assert all(e[k]=="" for k in ("source_english","source_burmese","source_level")),w
  assert e["status"]=="AI_ASSISTED_RETIER_DRAFT_PENDING_INDEPENDENT_REVIEW",w
  task=tasks[w]
  assert task["proposed_level"]==e["proposed_level"] and task["release_approved"] is False,w
  assert task["review_status"]=="PENDING_INDEPENDENT_REVIEW",w
  for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert task[k]["completed"] is False and task[k]["reviewer"] is None and task[k]["observed_evidence"] is None,w
  assert task["english_definition_review"]["source_observed"] is False,w
  assert task["audio_review"]["real_listening"] is False and task["audio_review"]["real_device_test"] is False,w
  if level=="ALL" or e["proposed_level"]==level:
   print("DRAFT_ONLY",e["proposed_level"],w,"sourcePOS",pool[w]["part_of_speech"],"NO CEFR APPROVAL")
 for w,h in held.items():
  assert w in pool and pool[w]["level"]=="C1" and h["source_observed"] is False and h["release_approved"] is False,w
  assert h["reviewed_independently"] is False,w
 bank=(R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in bank and re.search(r"entries:\s*\[\s*\]",bank)
 if level=="ALL":
  subprocess.run(["python3","tools/audit_cefr_batch53_retier.py","--level","ALL"],cwd=R,check=True)
  print("BATCH54 ALL structural pass; canonical prior=3478; separate retier=128; combined first-pass=3606; independent approvals=0; new holds=12; cumulative holds=1179")
 else:print("BATCH54",level,"structural pass",COUNTS[level])
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--level",choices=["A2","B1","B2","C1","ALL"],required=True)
 audit(ap.parse_args().level)
