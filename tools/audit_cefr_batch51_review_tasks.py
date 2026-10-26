#!/usr/bin/env python3
"""Batch51 staging-only structural audit; NOT an independent linguistic review."""
import argparse,collections,json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
EXPECTED={"A2":0,"B1":0,"B2":4,"C1":36}
HELD={"A2":3,"B1":3,"B2":14,"C1":14}
TOTAL={"A2":534,"B1":778,"B2":931,"C1":735}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
def read(p):return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
 if level=="ALL":
  prev=subprocess.run([sys.executable,"tools/audit_cefr_batch50_review_tasks.py","--level","ALL"],cwd=R,text=True,capture_output=True)
  assert prev.returncode==0,prev.stdout+prev.stderr
  print(prev.stdout.strip())
 d=read("draft/A2-C1-EDITORIAL-BATCH51.json")
 t=read("draft/A2-C1-REVIEW-TASKS-BATCH51.json")
 q=read("draft/A2-C1-QUARANTINE-BATCH51.json")
 poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
 pool={r["word"]:r for r in poolrows}
 assert len(pool)==len(poolrows)==5000
 assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"] is True
 assert all(x["independently_approved"]==0 for x in (d,t,q))
 assert d["counts_by_provisional_level"]==t["counts_by_provisional_level"]==EXPECTED
 assert q["counts_by_provisional_level"]==HELD
 assert len(d["entries"])==len(t["entries"])==40 and len(q["records"])==34
 assert collections.Counter(x["level"] for x in d["entries"])==EXPECTED
 assert collections.Counter(x["provisional_level"] for x in q["records"])==HELD
 assert d["stages"]=={"english":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","myanmar":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","example":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","source_evidence":"PENDING_SEPARATE_REVIEW_TASKS"}
 drafts={x["word"]:x for x in d["entries"]}
 tasks={x["word"]:x for x in t["entries"]}
 holds={x["word"]:x for x in q["records"]}
 assert len(drafts)==len(tasks)==40 and len(holds)==34
 assert set(drafts)==set(tasks) and not set(drafts)&set(holds)
 assert len({x["example_sentence"] for x in d["entries"]})==40
 for word,row in drafts.items():
  if level!="ALL" and row["level"]!=level:continue
  assert re.fullmatch(r"[a-z]{3,}",word),word
  assert word in pool and pool[word]["level"]==row["level"],word
  assert POS[pool[word]["part_of_speech"]]==row["part_of_speech"],word
  assert len(row["english_definition"])>=25 and re.search(r"[\u1000-\u109f]",row["burmese_meaning"]),word
  ex=row["example_sentence"]
  assert len(ex)>=25 and ex[0].isupper() and ex[-1] in ".?!",word
  assert re.search(r"(?<![a-z])"+re.escape(word)+r"(?![a-z])",ex.lower()),word
  assert all(row[f] is False for f in FLAGS),word
  assert all(row[f]=="" for f in ("source_english","source_burmese","source_level")),word
  assert row["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and "UNVERIFIED" in row["editorial_risk"],word
  task=tasks[word]
  assert task["provisional_level"]==row["level"] and task["part_of_speech"]==row["part_of_speech"],word
  assert task["review_status"]=="PENDING_INDEPENDENT_REVIEW" and task["release_approved"] is False,word
  assert task["cefr_review"]["provisional_level_risk"]==row["editorial_risk"],word
  for sec in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert task[sec]["completed"] is False and task[sec]["reviewer"] is None and task[sec]["observed_evidence"] is None,word
  assert task["english_definition_review"]["source_observed"] is False,word
  assert task["audio_review"]["completed"] is False and task["audio_review"]["real_listening"] is False and task["audio_review"]["real_device_test"] is False,word
 for word,row in holds.items():
  if level!="ALL" and row["provisional_level"]!=level:continue
  assert word in pool and pool[word]["level"]==row["provisional_level"],word
  assert row["source_observed"] is False and row["reviewed_independently"] is False and row["release_approved"] is False,word
 if level=="ALL":
  paths=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,52)]
  qpaths=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,52)]
  grouped=collections.defaultdict(list)
  for p in paths:
   for row in read(p)["entries"]:grouped[row["word"]].append(row)
  assert all(len({x["level"] for x in rows})==1 for rows in grouped.values())
  assert sum(len(rows)-1 for rows in grouped.values())==182
  assert len(grouped)==2978,len(grouped)
  bylevel=collections.Counter(rows[0]["level"] for rows in grouped.values())
  assert bylevel==TOTAL,bylevel
  held=[x["word"] for p in qpaths for x in read(p)["records"]]
  assert len(held)==len(set(held))==1143,len(held)
  assert not set(held)&set(grouped)
  assert all(all(x[f] is False for f in FLAGS) for rows in grouped.values() for x in rows)
  assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
  print(f"UNIQUE A2-C1 {dict(bylevel)} total=2978; independently approved=0")
  print("A1=500; A1-C1 written=3478; outstanding=1522; quarantine=1143; historical duplicate rows excluded=182")
 print(f"STAGING ONLY batch51 {level} PASS: 40 drafts, 34 holds, zero approvals; no audio/deploy")
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
 audit(p.parse_args().level)
