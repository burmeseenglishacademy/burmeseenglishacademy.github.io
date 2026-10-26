#!/usr/bin/env python3
"""Batch52 structural staging QA; not linguistic, CEFR or audio approval."""
import argparse,collections,json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
E={"A2":12,"B1":12,"B2":12,"C1":4}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
def rd(p):return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
 d=rd("draft/A2-C1-RETIER-EDITORIAL-BATCH52.json")
 t=rd("draft/A2-C1-RETIER-REVIEW-TASKS-BATCH52.json")
 q=rd("draft/A2-C1-RETIER-QUARANTINE-BATCH52.json")
 poolrows=rd("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
 pool={r["word"]:r for r in poolrows}
 assert len(pool)==len(poolrows)==5000
 assert d["release_status"]=="UNVERIFIED_RETIER_DRAFT_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"]
 assert q["release_status"]=="UNVERIFIED_CANDIDATE_HOLDS_DO_NOT_PUBLISH"
 assert all(x["independently_approved"]==0 for x in (d,t,q))
 assert d["counts_by_proposed_level"]==t["counts_by_proposed_level"]==E
 assert len(d["entries"])==len(t["entries"])==40 and len(q["records"])==14
 assert {k:sum(r["proposed_level"]==k for r in d["entries"]) for k in E}==E
 assert d["stages"]=={"english":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","myanmar":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","example":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","source_evidence":"PENDING_SEPARATE_REVIEW_TASKS"}
 words={r["word"]:r for r in d["entries"]}
 tasks={r["word"]:r for r in t["entries"]}
 held={r["word"]:r for r in q["records"]}
 assert len(words)==len(tasks)==40 and len(held)==14 and set(words)==set(tasks) and not set(words)&set(held)
 prior=[R/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((R/"draft").glob("A2-C1-EDITORIAL-BATCH*.json"))]
 priorq=[R/"draft/A2-C1-CANDIDATE-QUARANTINE.json",*sorted((R/"draft").glob("A2-C1-QUARANTINE-BATCH*.json"))]
 used={r["word"] for p in prior for r in json.loads(p.read_text(encoding="utf-8"))["entries"]}
 used|={r["word"] for p in priorq for r in json.loads(p.read_text(encoding="utf-8"))["records"]}
 assert not (set(words)|set(held))&used,f"existing draft/hold collision: {sorted((set(words)|set(held))&used)}"
 assert len({r["example_sentence"] for r in d["entries"]})==40
 for w,r in words.items():
  if level!="ALL" and r["proposed_level"]!=level:continue
  assert re.fullmatch(r"[a-z]{3,}",w) and w in pool,w
  assert pool[w]["level"]==r["source_pool_level"]=="C1",w
  assert POS[pool[w]["part_of_speech"]]==r["part_of_speech"],w
  assert len(r["english_definition"])>=25 and re.search(r"[\u1000-\u109f]",r["burmese_meaning"]),w
  s=r["example_sentence"]
  assert len(s)>=25 and s[0].isupper() and s[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",s.lower()),w
  assert all(r[f] is False for f in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),w
  assert all(r[f]=="" for f in ("source_english","source_burmese","source_level")),w
  task=tasks[w]
  assert task["proposed_level"]==r["proposed_level"] and task["release_approved"] is False,w
  assert task["review_status"]=="PENDING_INDEPENDENT_REVIEW" and task["cefr_review"]["provisional_level_risk"]==r["editorial_risk"],w
  for sec in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert task[sec]["completed"] is False and task[sec]["reviewer"] is None and task[sec]["observed_evidence"] is None,w
  assert task["english_definition_review"]["source_observed"] is False,w
  assert task["audio_review"]["real_listening"] is False and task["audio_review"]["real_device_test"] is False,w
 for w,r in held.items():
  assert w in pool and pool[w]["level"]==r["source_pool_level"]=="C1" and r["release_approved"] is False and r["source_observed"] is False,w
 if level=="ALL":
  old=subprocess.run([sys.executable,"tools/audit_cefr_batch51_review_tasks.py","--level","ALL"],cwd=R,text=True,capture_output=True)
  assert old.returncode==0,old.stdout+old.stderr
  print(old.stdout.strip())
  assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
  print("PRIOR canonical first-pass 3478; new separate retier first-pass 40; combined unique 3518; independent approved 0; holds 1157")
 print(f"STAGING batch52 {level} STRUCTURAL PASS; proposed {E[level] if level!='ALL' else 40}; 14 holds; NO CEFR/audio approval")
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--level",choices=(*E,"ALL"),default="ALL")
 audit(p.parse_args().level)
