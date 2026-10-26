#!/usr/bin/env python3
"""Batch63: nondeploy structural triage only; no source-based linguistic or audio approval."""
import argparse,collections,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(p): return json.loads(p.read_text(encoding="utf-8"))
def main(level):
 d=read(ROOT/"draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH63.json")
 t=read(ROOT/"draft/A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH63.json")
 E,T=d["entries"],t["entries"]
 assert d["release_status"]=="UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH"
 assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH" and t["source_pages_not_yet_checked"] is True
 assert len(E)==len(T)==80 and len({e["word"].casefold() for e in E})==80
 assert {e["word"] for e in E}=={x["word"] for x in T}
 assert dict(collections.Counter(e["proposed_level"] for e in E))==d["counts_by_proposed_level"]=={"A2":16,"B1":20,"B2":24,"C1":20}
 pool={x["word"].casefold() for x in read(ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
 prior=set()
 files=[ROOT/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((ROOT/"draft").glob("A2-C1-EDITORIAL-BATCH*.json")),*sorted((ROOT/"draft").glob("A2-C1-RETIER-EDITORIAL-BATCH*.json")),*[p for p in sorted((ROOT/"draft").glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json")) if p.name!="A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH63.json"],ROOT/"draft/A1-EDITORIAL-STARTER.json",*sorted((ROOT/"draft").glob("A1-EXPANSION-BATCH*.json"))]
 for p in files: prior.update(x["word"].casefold() for x in read(p)["entries"])
 eligible=[];held=[]
 for e in E:
  w=e["word"];s=e["example_sentence"]
  assert re.fullmatch(r"[a-z]{4,}",w),w
  assert e["part_of_speech"] in ("noun","verb","adjective","adverb"),w
  assert e["proposed_level"] in ("A2","B1","B2","C1"),w
  assert len(e["english_definition"])>=30 and re.search("[\\u1000-\\u109f]",e["burmese_meaning"]),w
  assert len(s)>=35 and s[0].isupper() and s[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",s.casefold()),w
  assert all(e[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation","release_approved")),w
  assert all(e[k]=="" for k in ("source_english","source_burmese","source_level")),w
  assert e["editorial_hold"]==bool(e["editorial_hold_reasons"]),w
  assert e["status"]==("REVERSIBLE_QUARANTINE_EDITORIAL_RISK" if e["editorial_hold"] else "FIRST_PASS_UNVERIFIED_PENDING_CROSS_CORPUS_TRIAGE"),w
  reasons=[]
  if w.casefold() in pool or w.casefold() in prior: reasons.append("ALREADY_IN_ORIGINAL_5000_POOL_OR_PREVIOUS_DRAFT")
  reasons.extend(e["editorial_hold_reasons"])
  if any(k in e for k in ("wordnet_synset","wordnet_definition","unreviewed_wordnet_sense")): reasons.append("UNREVIEWED_WORDNET_SENSE")
  if w in {"amazon","google","microsoft","singapore","myanmar","london","oxford"}: reasons.append("NAMED_ENTITY_UNSUPPORTED")
  if reasons: held.append({"word":w,"level":e["proposed_level"],"reasons":reasons,"reversible":True,"independently_approved":False})
  else: eligible.append(e)
 for x in T:
  e=next(e for e in E if e["word"]==x["word"])
  assert x["release_approved"] is False and x["editorial_hold"]==e["editorial_hold"] and x["editorial_hold_reasons"]==e["editorial_hold_reasons"]
  for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
   assert x[k]["completed"] is False and x[k]["reviewer"] is None and x[k]["observed_evidence"] is None
  assert x["english_definition_review"]["source_observed"] is False
  assert x["audio_review"]["generated"] is False and x["audio_review"]["real_listening"] is False and x["audio_review"]["real_device_test"] is False
 bank=(ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
 assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in bank and re.search(r"entries:\s*\[\s*\]",bank)
 out={"batch":62,"stage":"STRUCTURAL_TRIAGE_NOT_LINGUISTIC_APPROVAL","proposals":len(E),"proposed_levels":d["counts_by_proposed_level"],"eligible_unapproved_first_pass":len(eligible),"eligible_by_level":dict(collections.Counter(e["proposed_level"] for e in eligible)),"quarantined_total":len(held),"duplicate_collisions":sum("ALREADY_IN_ORIGINAL_5000_POOL_OR_PREVIOUS_DRAFT" in x["reasons"] for x in held),"explicit_editorial_holds":sum(e["editorial_hold"] for e in E),"quarantined_by_level":dict(collections.Counter(x["level"] for x in held)),"quarantined_records":held,"dictionary_pages_observed":0,"independently_approved":0}
 if level=="ALL":
  subprocess.run(["python3","tools/audit_cefr_batch63_recovery.py","--level","ALL"],cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
  (ROOT/"batch63-triage-results.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
  print("BATCH63 TRIAGE RESULTS "+json.dumps(out,ensure_ascii=False))
  print("BATCH63 PASS: structural checks only; no editorial or listening approvals")
 else: print("BATCH63",level,"proposals",d["counts_by_proposed_level"][level],"eligible",sum(e["proposed_level"]==level for e in eligible),"held",sum(x["level"]==level for x in held))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--level",choices=["A2","B1","B2","C1","ALL"],required=True);main(p.parse_args().level)
