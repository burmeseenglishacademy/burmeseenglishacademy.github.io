#!/usr/bin/env python3
"""Batch56 structural / quarantine / production safety audit. No linguistic approval."""
import argparse, collections, json, re, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
COUNTS={"A2":2,"B1":6,"B2":12,"C1":1}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
def read(p): return json.loads((R/p).read_text(encoding="utf-8"))
def main(level):
 d=read("draft/A2-C1-RETIER-EDITORIAL-BATCH56.json")
 t=read("draft/A2-C1-RETIER-REVIEW-TASKS-BATCH56.json")
 q=read("draft/A2-C1-RETIER-QUARANTINE-BATCH56.json")
 assert d["release_status"]=="UNVERIFIED_RETIER_DRAFT_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"]
 assert q["release_status"]=="UNVERIFIED_CANDIDATE_HOLDS_DO_NOT_PUBLISH"
 assert all(x["independently_approved"]==0 for x in (d,t,q))
 assert d["counts_by_proposed_level"]==t["counts_by_proposed_level"]==COUNTS
 E=d["entries"]; T=t["entries"]; H=q["records"]
 assert len(E)==len(T)==21 and len(H)==143
 assert collections.Counter(e["proposed_level"] for e in E)==COUNTS
 assert len({e["word"] for e in E})==21 and len({e["example_sentence"] for e in E})==21
 assert {e["word"] for e in E}=={e["word"] for e in T}
 assert not {e["word"] for e in E}&{h["word"] for h in H}
 assert collections.Counter(h["source_pool_level"] for h in H)==q["counts_by_source_pool_level"]
 poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
 pool={e["word"]:e for e in poolrows}
 assert len(pool)==len(poolrows)==5000
 prior=[R/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((R/"draft").glob("A2-C1-EDITORIAL-BATCH*.json")),*sorted((R/"draft").glob("A2-C1-RETIER-EDITORIAL-BATCH5[2345].json"))]
 priorq=[R/"draft/A2-C1-CANDIDATE-QUARANTINE.json",*sorted((R/"draft").glob("A2-C1-QUARANTINE-BATCH*.json")),*sorted((R/"draft").glob("A2-C1-RETIER-QUARANTINE-BATCH5[2345].json"))]
 used=[e["word"] for p in prior for e in read(p.relative_to(R))["entries"]]
 held=[h["word"] for p in priorq for h in read(p.relative_to(R))["records"]]
 assert len(set(used))==3146 and len(used)-len(set(used))==182,(len(used),len(set(used)))
 assert len(held)==len(set(held))==1190,len(held)
 assert not set(used)&set(held)
 assert not ({e["word"] for e in E}|{h["word"] for h in H})&(set(used)|set(held))
 assert len({e["word"] for e in E}|{h["word"] for h in H})==164
 assert len(set(used)|set(held)|{e["word"] for e in E}|{h["word"] for h in H})==4500
 assert all(r["word"] in (set(used)|set(held)|{e["word"] for e in E}|{h["word"] for h in H}) for r in poolrows if r["level"]!="A1")
 for e in E:
  w=e["word"]; assert w in pool and pool[w]["level"]==e["source_pool_level"],w
  assert POS[pool[w]["part_of_speech"]]==e["part_of_speech"],w
  assert re.fullmatch(r"[a-z]{3,}",w),w
  assert len(e["english_definition"])>=25 and re.search(r"[\u1000-\u109f]",e["burmese_meaning"]),w
  s=e["example_sentence"]
  assert len(s)>=25 and s[0].isupper() and s[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",s.lower()),w
  assert all(e[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),w
  assert all(e[k]=="" for k in ("source_english","source_burmese","source_level")),w
  assert e["status"]=="AI_ASSISTED_RETIER_DRAFT_PENDING_INDEPENDENT_REVIEW",w
  if level=="ALL" or e["proposed_level"]==level: print("UNVERIFIED_DRAFT",e["proposed_level"],w,"SOURCE_POS",pool[w]["part_of_speech"])
 for x in T:
  assert x["release_approved"] is False and x["review_status"]=="PENDING_INDEPENDENT_REVIEW"
  for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert x[k]["completed"] is False and x[k]["observed_evidence"] is None and x[k]["reviewer"] is None,x["word"]
  assert x["english_definition_review"]["source_observed"] is False
  assert x["audio_review"]["real_listening"] is False and x["audio_review"]["real_device_test"] is False
 for h in H:
  w=h["word"]; assert w in pool and pool[w]["level"]==h["source_pool_level"],w
  assert h["source_observed"] is False and h["reviewed_independently"] is False and h["release_approved"] is False
  assert h["hold_kind"]=="REVERSIBLE_NOT_REJECTED" and len(h["risk"])>15
 bank=(R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in bank and re.search(r"entries:\s*\[\s*\]",bank)
 if level=="ALL":
  subprocess.run(["python3","tools/audit_cefr_batch55_retier.py","--level","ALL"],cwd=R,check=True)
  print("BATCH56 ALL structural pass; canonical=3478; separate retier=189; written=3667; independent approvals=0; cumulative reversible holds=1333; unwritten=1333; original source-pool unheld=0")
 else: print("BATCH56",level,"structural pass",COUNTS[level])
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--level",choices=["A2","B1","B2","C1","ALL"],required=True)
 main(p.parse_args().level)
