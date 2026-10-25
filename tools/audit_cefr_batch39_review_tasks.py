#!/usr/bin/env python3
"""Unpublished batch39 structural QA; does not validate linguistic meaning, CEFR or audio."""
import argparse,collections,json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
EXPECTED={"A2":0,"B1":15,"B2":25,"C1":12}
HELD={"A2":0,"B1":8,"B2":8,"C1":4}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
def read(p):return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
    if level=="ALL":
        old=subprocess.run([sys.executable,"tools/audit_cefr_batch38_review_tasks.py","--level","ALL"],cwd=R,capture_output=True,text=True)
        assert old.returncode==0,old.stdout+old.stderr
        print(old.stdout.strip())
    d=read("draft/A2-C1-EDITORIAL-BATCH39.json")
    t=read("draft/A2-C1-REVIEW-TASKS-BATCH39.json")
    q=read("draft/A2-C1-QUARANTINE-BATCH39.json")
    pool={x["word"]:x for x in read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
    assert len(pool)==5000
    assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["independently_approved"]==t["independently_approved"]==q["independently_approved"]==0
    assert len(d["entries"])==len(t["entries"])==52 and len(q["records"])==20
    assert d["counts_by_provisional_level"]==EXPECTED
    assert q["counts_by_provisional_level"]==HELD
    assert collections.Counter(x["level"] for x in d["entries"])=={k:v for k,v in EXPECTED.items() if v}
    assert collections.Counter(x["provisional_level"] for x in q["records"])=={k:v for k,v in HELD.items() if v}
    drafts={x["word"]:x for x in d["entries"]}
    tasks={x["word"]:x for x in t["entries"]}
    holds={x["word"]:x for x in q["records"]}
    assert len(drafts)==len(tasks)==52 and len(holds)==20
    assert set(drafts)==set(tasks) and not (set(drafts)&set(holds))
    assert len({x["example_sentence"] for x in drafts.values()})==52
    for word,r in drafts.items():
        if level!="ALL" and r["level"]!=level:continue
        assert re.fullmatch("[a-z]{3,}",word) and word in pool and pool[word]["level"]==r["level"],word
        assert POS[pool[word]["part_of_speech"]]==r["part_of_speech"],word
        assert len(r["english_definition"])>=25 and re.search("[\\u1000-\\u109f]",r["burmese_meaning"]),word
        e=r["example_sentence"]
        assert len(e)>=25 and e[0].isupper() and e[-1] in ".?!" and re.search(r"(?<![a-z])"+re.escape(word)+r"(?![a-z])",e.lower()),word
        assert all(r[k] is False for k in FLAGS),word
        assert all(r[k]=="" for k in ("source_english","source_burmese","source_level")),word
        assert r["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and r["editorial_risk"],word
        x=tasks[word]
        assert x["provisional_level"]==r["level"] and x["part_of_speech"]==r["part_of_speech"],word
        assert x["review_status"]=="PENDING_INDEPENDENT_REVIEW" and x["release_approved"] is False,word
        assert x["cefr_review"]["provisional_level_risk"]==r["editorial_risk"],word
        for key in ("english_definition_review","burmese_review","example_review","cefr_review"):
            assert x[key]["completed"] is False and x[key]["reviewer"] is None and x[key]["observed_evidence"] is None,word
        assert x["english_definition_review"]["source_observed"] is False,word
        assert x["audio_review"]["completed"] is False and x["audio_review"]["real_listening"] is False and x["audio_review"]["real_device_test"] is False,word
    for word,r in holds.items():
        assert word in pool and pool[word]["level"]==r["provisional_level"],word
        assert r["source_observed"] is False and r["reviewed_independently"] is False and r["release_approved"] is False,word
    if level=="ALL":
        oldfiles=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,39)]
        olddrafts={r["word"] for p in oldfiles for r in read(p)["entries"]}
        oldholds={r["word"] for p in ["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,39)] for r in read(p)["records"]}
        assert len(olddrafts)==2370 and len(oldholds)==761
        assert not set(drafts)&olddrafts,("duplicate draft",set(drafts)&olddrafts)
        assert not set(holds)&oldholds,("duplicate hold",set(holds)&oldholds)
        assert not (set(drafts)&oldholds) and not (set(holds)&olddrafts)
        allrows=[r for p in oldfiles for r in read(p)["entries"]]+d["entries"]
        byword=collections.defaultdict(list)
        for r in allrows:byword[r["word"]].append(r)
        assert len(byword)==2422
        assert sum(len(v)-1 for v in byword.values())==182
        counts=collections.Counter(v[0]["level"] for v in byword.values())
        assert counts=={"A2":521,"B1":715,"B2":724,"C1":462},counts
        assert len(oldholds|set(holds))==781
        print("UNIQUE A2-C1 A2=521 B1=715 B2=724 C1=462 total=2422; independently approved=0")
        print("A1=500; A1-C1 written=2922; outstanding=2078; quarantine=781; legacy duplicate rows=182")
    assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print(f"STAGING ONLY batch39 {level} PASS: 52 drafts, 20 holds, zero approvals; no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    audit(p.parse_args().level)
