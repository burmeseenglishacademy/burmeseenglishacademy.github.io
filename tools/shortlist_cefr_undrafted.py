#!/usr/bin/env python3
"""Staging-only shortlist of not-yet-authored candidate words, never CEFR approval."""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
BAD_CLUE=re.compile(r"\b(?:surname|given name|capital of|city in|state in|born in|genus|species|trademark|president of|king of|United States (?:actor|writer|politician)|English (?:actor|writer|politician)|initialism|acronym|abbreviation)\b",re.I)
NAMED={"amazon","singapore","myanmar","tokyo","google","microsoft","kennedy","moore","greece","malaysia","netherlands","indonesia","philippines","london","oxford","harrison","hughes","lucas","todd","shaw","brooklyn","alabama","maryland"}
def load(p): return json.loads(p.read_text(encoding="utf8"))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--limit",type=int,default=85)
    args=ap.parse_args()
    pool=load(ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json")
    assert pool["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH" and len(pool["entries"])==5000
    authored=collections.defaultdict(list)
    for p in [ROOT/"draft/A1-EDITORIAL-STARTER.json",*sorted((ROOT/"draft").glob("A1-EXPANSION-BATCH*.json")),ROOT/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((ROOT/"draft").glob("A2-C1-EDITORIAL-BATCH*.json")),*sorted((ROOT/"draft").glob("A2-C1-RETIER-EDITORIAL-BATCH*.json")),*sorted((ROOT/"draft").glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json"))]:
        for r in load(p)["entries"]:
            authored[r["word"].casefold()].append(p.name)
    held=set()
    for p in [ROOT/"draft/A2-C1-CANDIDATE-QUARANTINE.json",*sorted((ROOT/"draft").glob("A2-C1-QUARANTINE-BATCH*.json")),*sorted((ROOT/"draft").glob("A2-C1-RETIER-QUARANTINE-BATCH*.json"))]:
        if p.exists():
            held.update(x["word"].casefold() for x in load(p)["records"])
    print("SHORTLIST INDEX authored_unique",len(authored),"authored_collisions",sum(len(x)-1 for x in authored.values()),"explicit_quarantine_unique",len(held))
    for level in LEVELS:
        rows=[]; reasons=collections.Counter()
        for r in pool["entries"]:
            if r["level"]!=level: continue
            w=r["word"].casefold()
            clue=str(r.get("english_definition_draft",""))
            flags=[]
            if w in authored: flags.append("PREVIOUSLY_AUTHORED")
            if w in held: flags.append("PRIOR_QUARANTINE")
            if not re.fullmatch("[a-z]{4,}",w): flags.append("FORM")
            if w in NAMED or BAD_CLUE.search(clue): flags.append("SUSPECT_PROPER_OR_FIRST_SENSE")
            if len(w)>5 and w.endswith(("ing","ed","s")): flags.append("MORPHOLOGY_REVIEW")
            if level=="C1" and isinstance(r.get("zipf_frequency"),(int,float)) and r["zipf_frequency"]>=4: flags.append("FREQUENT_C1_TIER_REVIEW")
            if flags:
                reasons.update(flags)
                continue
            rows.append(r)
        rows.sort(key=lambda r:(-float(r.get("zipf_frequency") or 0),r["word"]))
        print("SHORTLIST_LEVEL",level,"available_preflight_only",len(rows),"held_reasons",dict(reasons))
        for r in rows[:args.limit]:
            clue=" ".join(str(r.get("english_definition_draft","")).split()).replace("|","/")[:95]
            print("CANDIDATE|{}|{}|{}|{}|{}".format(level,r["word"],r.get("part_of_speech",""),r.get("zipf_frequency",""),clue))
    print("NO SOURCES CHECKED; NO LINGUISTIC OR CEFR APPROVAL; NO DEPLOY")
if __name__=="__main__": main()
