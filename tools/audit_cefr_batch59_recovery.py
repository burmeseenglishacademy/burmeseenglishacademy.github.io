#!/usr/bin/env python3
"""Source recovery batch59: structural, duplicate, risk and publication gates; never linguistic approval."""
import argparse, collections, json, re, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def read(path): return json.loads((R/path).read_text(encoding="utf-8"))
def main(level):
 d=read("draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json")
 t=read("draft/A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH59.json")
 assert d["release_status"]=="UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"]
 E=d["entries"]; T=t["entries"]
 assert len(E)==len(T)==80
 assert len({e["word"] for e in E})==80
 assert {e["word"] for e in E}=={x["word"] for x in T}
 assert dict(collections.Counter(e["proposed_level"] for e in E))==d["counts_by_proposed_level"]
 pool={x["word"].casefold() for x in read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
 files=[R/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((R/"draft").glob("A2-C1-EDITORIAL-BATCH*.json")),*sorted((R/"draft").glob("A2-C1-RETIER-EDITORIAL-BATCH*.json")),*[f for f in sorted((R/"draft").glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json")) if f.name != "A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json"]]
 existing=set()
 for f in files:
  existing.update(x["word"].casefold() for x in json.loads(f.read_text(encoding="utf-8"))["entries"])
 quarantined=[]
 eligible=[]
 # Reversible holds: the suggested level is not a graded CEFR observation.
 high_risk_c1_c2={"alacrity","apocryphal","ascetic","conflagration","contrition","laconic","magnanimous","predilection","quintessential","recalcitrant","subterfuge","vicarious","vacillate","veracity"}
 high_risk_level={"pothole":"A2_OR_B1_LEVEL_UNSUPPORTED"}

 for e in E:
  w=e["word"]
  assert re.fullmatch(r"[a-z]{4,}",w),w
  assert e["part_of_speech"] in ("noun","verb","adjective","adverb"),w
  assert e["proposed_level"] in ("A2","B1","B2","C1"),w
  assert len(e["english_definition"])>=30,w
  assert re.search(r"[\u1000-\u109f]",e["burmese_meaning"]),w
  s=e["example_sentence"]
  assert len(s)>=35 and s[0].isupper() and s[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",s.casefold()),w
  assert all(e[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation","release_approved")),w
  assert all(e[k]=="" for k in ("source_english","source_burmese","source_level")),w
  reasons=[]
  if w.casefold() in pool or w.casefold() in existing: reasons.append("ALREADY_IN_ORIGINAL_5000_POOL_OR_PREVIOUS_DRAFT")
  if w in high_risk_c1_c2: reasons.append("C1_VS_C2_UNSUPPORTED_REQUIRES_GRADED_SENSE_SOURCE")
  if w in high_risk_level: reasons.append(high_risk_level[w])
  if reasons:
   quarantined.append({"word":w,"level":e["proposed_level"],"reasons":reasons,"reversible":True,"approved":False})
  else: eligible.append(e)
 for x in T:
  assert x["release_approved"] is False
  for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert x[k]["completed"] is False and x[k]["observed_evidence"] is None and x[k]["reviewer"] is None,x["word"]
  assert x["english_definition_review"]["source_observed"] is False
  assert x["audio_review"]["generated"] is False and x["audio_review"]["real_listening"] is False and x["audio_review"]["real_device_test"] is False
 bank=(R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in bank and re.search(r"entries:\s*\[\s*\]",bank)
 output={"batch":59,"stage":"STRUCTURAL_CANDIDATE_TRIAGE_NOT_LINGUISTIC_APPROVAL","proposals":len(E),"proposed_levels":dict(collections.Counter(e["proposed_level"] for e in E)),"new_unique_first_pass_proposals":len(eligible),"new_unique_by_level":dict(collections.Counter(e["proposed_level"] for e in eligible)),"quarantined_collisions":len(quarantined),"quarantined_by_level":dict(collections.Counter(x["level"] for x in quarantined)),"quarantined_records":quarantined,"independently_approved":0}
 if level=="ALL":
  subprocess.run(["python3","tools/audit_cefr_batch56_retier.py","--level","ALL"],cwd=R,check=True,stdout=subprocess.DEVNULL)
  out=R/"batch59-triage-results.json";out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
  print("BATCH59 TRIAGE RESULTS "+json.dumps(output,ensure_ascii=False))
  print("BATCH59 PASS: structural audit only; quarantine collisions and unsupported tiers; all editorial and audio flags false; public bank empty")
 else:
  sub=[e["word"] for e in eligible if e["proposed_level"]==level]
  held=[x["word"] for x in quarantined if x["level"]==level]
  print("BATCH59",level,"proposals",d["counts_by_proposed_level"].get(level,0),"unique_new",len(sub),"quarantined",len(held),"words",",".join(sub))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--level",choices=["A2","B1","B2","C1","ALL"],required=True);main(p.parse_args().level)
