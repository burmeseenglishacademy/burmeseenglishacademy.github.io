#!/usr/bin/env python3
"""Staging-only full unheld candidate triage. NEVER assigns or approves CEFR."""
import argparse, collections, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
def read(p):
    return json.loads(p.read_text(encoding="utf-8"))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=LEVELS,required=True)
    ap.add_argument("--limit",type=int,default=800)
    args=ap.parse_args()
    pool=read(ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json")
    assert pool["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert len(pool["entries"])==5000
    draft_paths=[ROOT/"draft/A2-C1-EDITORIAL-STARTER.json",*sorted((ROOT/"draft").glob("A2-C1-EDITORIAL-BATCH*.json"))]
    hold_paths=[ROOT/"draft/A2-C1-CANDIDATE-QUARANTINE.json",*sorted((ROOT/"draft").glob("A2-C1-QUARANTINE-BATCH*.json"))]
    drafted={r["word"] for p in draft_paths for r in read(p)["entries"]}
    held={r["word"] for p in hold_paths for r in read(p)["records"]}
    assert not drafted & held
    rows=[r for r in pool["entries"] if r["level"]==args.level and r["word"] not in drafted and r["word"] not in held]
    risks=collections.Counter()
    print(f"STAGING_CANDIDATE_TRIAGE level={args.level} remaining_unheld={len(rows)} drafted_unique={len(drafted)} held_unique={len(held)}")
    for row in rows[:args.limit]:
        word=row["word"]
        pos=row.get("part_of_speech","")
        clue=" ".join(str(row.get("english_definition_draft","")).split()).replace("|","/")
        zipf=row.get("zipf_frequency")
        flags=[]
        if not re.fullmatch(r"[a-z]{3,}",word): flags.append("HEADWORD_FORM")
        if re.search(r"(?i)\\b(?:surname|given name|capital of|city in|state in|american actor|american writer|english philosopher|english architect|born in|genus|species|president of|king of)\\b",clue): flags.append("PROPER_OR_TECHNICAL_SENSE")
        if word.endswith(("ing","ed","s")) and len(word)>5: flags.append("MORPHOLOGY_CHECK")
        if args.level=="C1" and isinstance(zipf,(float,int)) and zipf>=4: flags.append("HIGH_FREQUENCY_C1_RECHECK")
        if not flags: flags=["SENSE_AND_CEFR_UNVERIFIED"]
        risks.update(flags)
        print("PENDING|"+args.level+"|"+word+"|"+pos+"|"+str(zipf)+"|"+",".join(flags)+"|"+clue[:170])
    print("HEURISTIC_RISKS",json.dumps(risks,sort_keys=True))
    print("NO APPROVAL / NO AUDIO / NO DEPLOY")
if __name__=="__main__":
    main()
