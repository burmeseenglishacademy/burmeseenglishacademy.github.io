#!/usr/bin/env python3
"""Staging-only batch15 structural and unique-headword audit; NOT linguistic approval."""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
EXPECTED={"A2":15,"B1":15,"B2":15,"C1":15}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
FILES=["draft/A2-C1-EDITORIAL-STARTER.json"]+["draft/A2-C1-EDITORIAL-BATCH%02d.json"%i for i in range(9,16)]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf8"))
def audit(level):
    batch=load("draft/A2-C1-EDITORIAL-BATCH15.json")
    tasks=load("draft/A2-C1-REVIEW-TASKS-BATCH15.json")
    holds=load("draft/A2-C1-QUARANTINE-BATCH15.json")
    old_holds=load("draft/A2-C1-CANDIDATE-QUARANTINE.json")
    prior_holds=load("draft/A2-C1-QUARANTINE-BATCH14.json")
    candidates=load("draft/UNVERIFIED_CEFR_CANDIDATES.json")
    assert batch["release_status"]==holds["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert tasks["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert batch["independently_approved"]==tasks["independently_approved"]==holds["independently_approved"]==0
    assert tasks["source_pages_not_yet_checked"] is True
    assert len(batch["entries"])==len(tasks["entries"])==60
    assert Counter(e["level"] for e in batch["entries"])==EXPECTED
    assert Counter(e["provisional_level"] for e in tasks["entries"])==EXPECTED
    assert batch["counts_by_provisional_level"]==EXPECTED
    assert len({e["word"] for e in batch["entries"]})==42
    assert len({e["example_sentence"] for e in batch["entries"]})==42
    assert len({e["word"] for e in holds["records"]})==12
    held={e["word"] for e in holds["records"]}|{e["word"] for e in old_holds["records"]}|{e["word"] for e in prior_holds["records"]}
    assert len(held)==len(holds["records"])+len(old_holds["records"])+len(prior_holds["records"]), "Overlapping quarantine records"
    assert all(e["reviewed_independently"] is False and e["release_approved"] is False for e in holds["records"])
    pool={e["word"]:e for e in candidates["entries"]}
    assert len(pool)==5000
    earlier=[e for p in FILES[:-1] for e in load(p)["entries"]]
    already={e["word"] for e in earlier}
    assert not ({e["word"] for e in batch["entries"]}&already), "Batch14 duplicates previous drafts"
    assert not ({e["word"] for e in batch["entries"]}&held), "Quarantined candidate drafted"
    review={e["word"]:e for e in tasks["entries"]}
    assert len(review)==42
    for item in batch["entries"]:
        if level!="ALL" and item["level"]!=level: continue
        word=item["word"]
        assert word in pool and pool[word]["level"]==item["level"],word
        assert re.fullmatch(r"[a-z]{3,}",word),word
        assert len(item["english_definition"].strip())>=20,word
        assert re.search(r"[\u1000-\u109f]",item["burmese_meaning"]),word
        assert re.search(r"(?<![a-z])"+re.escape(word)+r"(?![a-z])",item["example_sentence"].lower()),word
        assert len(item["example_sentence"].strip())>=20,word
        assert all(item[k] is False for k in FLAGS),word
        assert all(item[k]=="" for k in ("source_english","source_burmese","source_level")),word
        assert item["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW",word
        task=review[word]
        assert task["provisional_level"]==item["level"] and task["part_of_speech"]==item["part_of_speech"],word
        assert task["review_status"]=="PENDING_INDEPENDENT_REVIEW" and task["release_approved"] is False,word
        assert task["english_definition_review"]["source_observed"] is False,word
        assert task["burmese_review"]["reviewer"] is None,word
        assert all(task[k]["completed"] is False for k in ("english_definition_review","burmese_review","example_review","cefr_review","audio_review")),word
    if level=="ALL":
        byword=defaultdict(list)
        for path in FILES:
            for row in load(path)["entries"]: byword[row["word"]].append(row)
        assert len(byword)==1168,(len(byword),"expected 1108 unique A2-C1 draft headwords")
        assert Counter(rs[0]["level"] for rs in byword.values())=={"A2":298,"B1":296,"B2":298,"C1":276}
        conflicts=[w for w,rs in byword.items() if any((r["level"],r["part_of_speech"],r["english_definition"],r["burmese_meaning"],r["example_sentence"])!=(rs[0]["level"],rs[0]["part_of_speech"],rs[0]["english_definition"],rs[0]["burmese_meaning"],rs[0]["example_sentence"]) for r in rs[1:])]
        assert not conflicts,("conflicting duplicate draft content",conflicts[:10])
        print("UNIQUE A2-C1 WRITTEN: A2=298 B1=296 B2=298 C1=276 total=1168; independent approvals=0")
        print("Legacy identical duplicate rows=",sum(len(rs)-1 for rs in byword.values()),"not counted twice")
    assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf8")
    print("STAGING ONLY: batch15",level,"structure PASS; 60 new drafts, 12 holds, 0 independent approvals, no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    audit(p.parse_args().level)
