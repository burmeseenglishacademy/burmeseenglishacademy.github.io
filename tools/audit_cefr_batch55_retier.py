#!/usr/bin/env python3
"""Batch55 staging-only structure and safety audit; not independent linguistic review."""
import argparse,collections,json,re,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
COUNTS={"A2":8,"B1":14,"B2":16,"C1":2}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
def read(p): return json.loads((R/p).read_text(encoding="utf-8"))
def main(level):
 d=read("draft/A2-C1-RETIER-EDITORIAL-BATCH55.json")
 t=read("draft/A2-C1-RETIER-REVIEW-TASKS-BATCH55.json")
 q=read("draft/A2-C1-RETIER-QUARANTINE-BATCH55.json")
 assert d["release_status"]=="UNVERIFIED_RETIER_DRAFT_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"]
 assert q["release_status"]=="UNVERIFIED_CANDIDATE_HOLDS_DO_NOT_PUBLISH"
 assert all(x["independently_approved"]==0 for x in (d,t,q))
 assert d["counts_by_proposed_level"]==t["counts_by_proposed_level"]==COUNTS
 entries=d["entries"]; tasks=t["entries"]; held=q["records"]
 assert len(entries)==len(tasks)==40 and len(held)==10
 assert collections.Counter(e["proposed_level"] for e in entries)==COUNTS
 assert len({e["word"] for e in entries})==40
 assert len({e["example_sentence"] for e in entries})==40
 assert {e["word"] for e in entries}=={e["word"] for e in tasks}
 assert not ({e["word"] for e in entries}&{e["word"] for e in held})
 poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
 pool={e["word"]:e for e in poolrows}
 assert len(pool)==len(poolrows)==5000
 prior=[R/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((R/"draft").glob("A2-C1-EDITORIAL-BATCH*.json")),*sorted((R/"draft").glob("A2-C1-RETIER-EDITORIAL-BATCH5[234].json"))]
 priorq=[R/"draft/A2-C1-CANDIDATE-QUARANTINE.json",*sorted((R/"draft").glob("A2-C1-QUARANTINE-BATCH*.json")),*sorted((R/"draft").glob("A2-C1-RETIER-QUARANTINE-BATCH5[234].json"))]
 used=[e["word"] for p in prior for e in read(p.relative_to(R))["entries"]]
 heldprior=[e["word"] for p in priorq for e in read(p.relative_to(R))["records"]]
 assert len(used)==len(set(used))==3106,len(used)
 assert len(heldprior)==len(set(heldprior))==1180,len(heldprior)
 assert not set(used)&set(heldprior)
 assert not ({e["word"] for e in entries+held}&(set(used)|set(heldprior)))
 for e in entries:
  w=e["word"]; assert w in pool and pool[w]["level"]==e["source_pool_level"]=="C1",w
  assert POS[pool[w]["part_of_speech"]]==e["part_of_speech"],(w,pool[w]["part_of_speech"],e["part_of_speech"])
  assert re.fullmatch(r"[a-z]{3,}",w),w
  assert len(e["english_definition"])>=25 and re.search(r"[\u1000-\u109f]",e["burmese_meaning"]),w
  s=e["example_sentence"]
  assert len(s)>=25 and s[0].isupper() and s[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",s.lower()),w
  assert all(e[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),w
  assert all(e[k]=="" for k in ("source_english","source_burmese","source_level")),w
  assert e["status"]=="AI_ASSISTED_RETIER_DRAFT_PENDING_INDEPENDENT_REVIEW",w
  if level=="ALL" or e["proposed_level"]==level: print("UNVERIFIED_DRAFT",e["proposed_level"],w,"SOURCE_POS",pool[w]["part_of_speech"])
 for x in tasks:
  assert x["release_approved"] is False and x["review_status"]=="PENDING_INDEPENDENT_REVIEW"
  for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert x[k]["completed"] is False and x[k]["observed_evidence"] is None and x[k]["reviewer"] is None,x["word"]
  assert x["english_definition_review"]["source_observed"] is False
  assert x["audio_review"]["real_listening"] is False and x["audio_review"]["real_device_test"] is False
 for h in held:
  assert h["word"] in pool and pool[h["word"]]["level"]=="C1" and h["source_observed"] is False and h["reviewed_independently"] is False and h["release_approved"] is False,h["word"]
 bank=(R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in bank and re.search(r"entries:\s*\[\s*\]",bank)
 if level=="ALL":
  subprocess.run(["python3","tools/audit_cefr_batch54_retier.py","--level","ALL"],cwd=R,check=True)
  print("BATCH55 ALL structural pass; canonical=3478; separate retier=168; total written=3646; independent approvals=0; cumulative holds=1190; unwritten=1354")
 else: print("BATCH55",level,"structural pass",COUNTS[level])
if __name__=="__main__":
 ap=argparse.ArgumentParser();ap.add_argument("--level",choices=["A2","B1","B2","C1","ALL"],required=True)
 main(ap.parse_args().level)
