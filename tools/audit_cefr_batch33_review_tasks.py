#!/usr/bin/env python3
"""Batch33 fail-closed structural staging audit. NEVER linguistic/audio approval."""
import argparse, collections, json, re, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((R/path).read_text(encoding="utf-8"))
def audit(level):
    if level=="ALL":
        previous=subprocess.run([sys.executable,"tools/audit_cefr_batch32_review_tasks.py","--level","ALL"],cwd=R,capture_output=True,text=True)
        if previous.returncode:
            print(previous.stdout,previous.stderr,file=sys.stderr)
            raise AssertionError("Prior batch32 inventory failed")
        print(previous.stdout.strip())
    d=read("draft/A2-C1-EDITORIAL-BATCH33.json")
    t=read("draft/A2-C1-REVIEW-TASKS-BATCH33.json")
    q=read("draft/A2-C1-QUARANTINE-BATCH33.json")
    poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool={x["word"]:x for x in poolrows}
    assert len(pool)==len(poolrows)==5000
    assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["independently_approved"]==t["independently_approved"]==q["independently_approved"]==0
    expected={"A2":3,"B1":19,"B2":20,"C1":2}
    assert len(d["entries"])==len(t["entries"])==44
    assert collections.Counter(x["level"] for x in d["entries"])==expected
    assert d["counts_by_provisional_level"]==expected
    assert len(q["records"])==len({x["word"] for x in q["records"]})==30
    assert len({x["word"] for x in d["entries"]})==44
    assert len({x["example_sentence"] for x in d["entries"]})==44
    olddraft=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,33)]
    previous=[x for p in olddraft for x in read(p)["entries"]]
    oldholds=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,33)]
    priorheld=[x for p in oldholds for x in read(p)["records"]]
    oldwords={x["word"] for x in previous}
    newwords={x["word"] for x in d["entries"]}
    oldheld={x["word"] for x in priorheld}
    newheld={x["word"] for x in q["records"]}
    assert not oldwords & newwords,("duplicate draft",oldwords & newwords)
    assert not oldheld & newheld,("duplicate quarantine",oldheld & newheld)
    assert not (oldheld|newheld) & (oldwords|newwords),("held and drafted",(oldheld|newheld)&(oldwords|newwords))
    assert len(oldheld)==len(priorheld)==479
    assert len(oldheld|newheld)==509
    posmap={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
    taskmap={x["word"]:x for x in t["entries"]}
    assert len(taskmap)==44
    for x in d["entries"]:
        if level!="ALL" and x["level"]!=level: continue
        word=x["word"]
        assert re.fullmatch(r"[a-z]{3,}",word),word
        assert word in pool and pool[word]["level"]==x["level"],("candidate",word)
        assert posmap[pool[word]["part_of_speech"]]==x["part_of_speech"],("POS",word)
        assert len(x["english_definition"].strip())>=25,word
        assert re.search(r"[\u1000-\u109f]",x["burmese_meaning"]),word
        assert len(x["example_sentence"].strip())>=25,word
        assert re.search(r"(?<![a-z])"+re.escape(word)+r"(?![a-z])",x["example_sentence"].lower()),word
        assert all(x[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),word
        assert all(x[k]=="" for k in ("source_english","source_burmese","source_level")),word
        assert x["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and x["editorial_risk"],word
        y=taskmap[word]
        assert y["provisional_level"]==x["level"] and y["part_of_speech"]==x["part_of_speech"],word
        assert y["review_status"]=="PENDING_INDEPENDENT_REVIEW" and y["release_approved"] is False,word
        assert y["english_definition_review"]["source_observed"] is False,word
        for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
            assert y[k]["completed"] is False and y[k]["reviewer"] is None and y[k]["observed_evidence"] is None,word
        assert y["audio_review"]["completed"] is False and y["audio_review"]["real_listening"] is False and y["audio_review"]["real_device_test"] is False,word
    for x in q["records"]:
        assert x["word"] in pool and x["provisional_level"]==pool[x["word"]]["level"],x["word"]
        assert x["source_observed"] is False and x["reviewed_independently"] is False and x["release_approved"] is False,x["word"]
    if level=="ALL":
        byword=collections.defaultdict(list)
        for x in previous+d["entries"]:byword[x["word"]].append(x)
        assert len(byword)==2066,len(byword)
        counts=collections.Counter(v[0]["level"] for v in byword.values())
        assert counts=={"A2":516,"B1":569,"B2":572,"C1":409},counts
        for word,versions in byword.items():
            assert all((v["level"],v["part_of_speech"],v["english_definition"],v["burmese_meaning"],v["example_sentence"])==(versions[0]["level"],versions[0]["part_of_speech"],versions[0]["english_definition"],versions[0]["burmese_meaning"],versions[0]["example_sentence"]) for v in versions[1:]),("conflicting legacy duplicates",word)
        print("UNIQUE A2-C1 A2=516 B1=569 B2=572 C1=409 total=2066; independently approved=0")
        print("A1=500; A1-C1 written=2566; first drafts outstanding=2434; unique quarantine=509; legacy duplicate rows=",sum(len(v)-1 for v in byword.values()))
    assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print("STAGING ONLY batch33",level,"PASS: 44 drafts, 30 new held, zero approvals; no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=("A2","B1","B2","C1","ALL"),default="ALL")
    audit(p.parse_args().level)
