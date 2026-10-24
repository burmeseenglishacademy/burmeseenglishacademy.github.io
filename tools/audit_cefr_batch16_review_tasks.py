#!/usr/bin/env python3
"""Fail-closed staging-only batch16 structural QA; never claims linguistic verification."""
import argparse,json,re
from pathlib import Path
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
EXPECTED={"A2":14,"B1":18,"B2":14,"C1":4}
TARGET={"A2":312,"B1":314,"B2":312,"C1":280}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
FILES=["draft/A2-C1-EDITORIAL-STARTER.json"]+["draft/A2-C1-EDITORIAL-BATCH%02d.json"%i for i in range(9,17)]
def load(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def audit(level):
    batch=load("draft/A2-C1-EDITORIAL-BATCH16.json")
    tasks=load("draft/A2-C1-REVIEW-TASKS-BATCH16.json")
    holds=load("draft/A2-C1-QUARANTINE-BATCH16.json")
    all_holds=[load("draft/A2-C1-CANDIDATE-QUARANTINE.json")]+[load("draft/A2-C1-QUARANTINE-BATCH%d.json"%i) for i in (14,15,16)]
    candidates=load("draft/UNVERIFIED_CEFR_CANDIDATES.json")
    assert batch["release_status"]==holds["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert tasks["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert batch["independently_approved"]==tasks["independently_approved"]==holds["independently_approved"]==0
    assert tasks["source_pages_not_yet_checked"] is True
    assert len(batch["entries"])==len(tasks["entries"])==50
    assert Counter(e["level"] for e in batch["entries"])==EXPECTED
    assert Counter(e["provisional_level"] for e in tasks["entries"])==EXPECTED
    assert batch["counts_by_provisional_level"]==EXPECTED
    assert len({e["word"] for e in batch["entries"]})==50
    assert len({e["example_sentence"] for e in batch["entries"]})==50
    assert len({e["word"] for e in holds["records"]})==16
    held=[e["word"] for h in all_holds for e in h["records"]]
    assert len(set(held))==len(held),"overlapping quarantine records"
    assert all(e["reviewed_independently"] is False and e["release_approved"] is False for h in all_holds for e in h["records"])
    pool={e["word"]:e for e in candidates["entries"]}
    assert len(pool)==5000
    prior=[e for p in FILES[:-1] for e in load(p)["entries"]]
    assert not ({e["word"] for e in batch["entries"]}&{e["word"] for e in prior}),"duplicate earlier drafts"
    assert not ({e["word"] for e in batch["entries"]}&set(held)),"quarantined candidate drafted"
    review={e["word"]:e for e in tasks["entries"]}
    assert len(review)==50
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
        assert len(byword)==1218,(len(byword),"expected 1218 unique A2-C1 headwords")
        assert Counter(rs[0]["level"] for rs in byword.values())==TARGET
        conflicts=[w for w,rs in byword.items() if any((r["level"],r["part_of_speech"],r["english_definition"],r["burmese_meaning"],r["example_sentence"])!=(rs[0]["level"],rs[0]["part_of_speech"],rs[0]["english_definition"],rs[0]["burmese_meaning"],rs[0]["example_sentence"]) for r in rs[1:])]
        assert not conflicts,("conflicting duplicate content",conflicts[:10])
        print("UNIQUE A2-C1 WRITTEN: A2=312 B1=314 B2=312 C1=280 total=1218; independent approvals=0")
        print("Legacy identical duplicate rows=",sum(len(rs)-1 for rs in byword.values()),"not counted twice")
    assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print("STAGING ONLY: batch16",level,"structure PASS; 50 new drafts, 16 holds, zero approvals, no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    audit(p.parse_args().level)
