#!/usr/bin/env python3
"""Batch34 staging structural and accounting checks; NEVER linguistic or audio approval."""
import argparse, collections, json, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
TARGET={"A1":500,"A2":700,"B1":1000,"B2":1300,"C1":1500}
EXPECTED_NEW={"A2":3,"B1":47,"B2":40,"C1":5}
EXPECTED_HOLDS={"A2":13,"B1":26,"B2":28,"C1":15}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
def read(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))
def audit(level):
    if level=="ALL":
        prev=subprocess.run([sys.executable,"tools/audit_cefr_batch33_review_tasks.py","--level","ALL"],
            cwd=ROOT,text=True,capture_output=True)
        if prev.returncode:
            print(prev.stdout,prev.stderr,file=sys.stderr)
            raise AssertionError("Prior batch33 audit failed")
        print(prev.stdout.strip())
    draft=read("draft/A2-C1-EDITORIAL-BATCH34.json")
    tasks=read("draft/A2-C1-REVIEW-TASKS-BATCH34.json")
    held=read("draft/A2-C1-QUARANTINE-BATCH34.json")
    poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool={x["word"]:x for x in poolrows}
    assert len(pool)==len(poolrows)==5000
    assert collections.Counter(x["level"] for x in poolrows)==TARGET
    assert draft["release_status"]==held["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert tasks["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert tasks["source_pages_not_yet_checked"] is True
    assert draft["independently_approved"]==tasks["independently_approved"]==held["independently_approved"]==0
    assert len(draft["entries"])==len(tasks["entries"])==95
    assert collections.Counter(x["level"] for x in draft["entries"])==EXPECTED_NEW
    assert draft["counts_by_provisional_level"]==EXPECTED_NEW
    assert len(held["records"])==82
    assert collections.Counter(x["provisional_level"] for x in held["records"])==EXPECTED_HOLDS
    assert held["counts_by_provisional_level"]==EXPECTED_HOLDS
    newwords={x["word"] for x in draft["entries"]}
    heldwords={x["word"] for x in held["records"]}
    assert len(newwords)==95 and len(heldwords)==82 and not (newwords&heldwords)
    assert len({x["example_sentence"] for x in draft["entries"]})==95
    oldfiles=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,34)]
    oldrows=[x for f in oldfiles for x in read(f)["entries"]]
    olddraftwords={x["word"] for x in oldrows}
    oldheldfiles=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,34)]
    oldheldrows=[x for f in oldheldfiles for x in read(f)["records"]]
    oldheldwords={x["word"] for x in oldheldrows}
    assert len(olddraftwords)==2066 and len(oldheldwords)==509
    assert not newwords & olddraftwords, ("previously drafted",newwords & olddraftwords)
    assert not heldwords & oldheldwords, ("previously quarantined",heldwords & oldheldwords)
    assert not (heldwords|oldheldwords)&(newwords|olddraftwords), "quarantine/draft conflict"
    taskmap={x["word"]:x for x in tasks["entries"]}
    assert len(taskmap)==95 and set(taskmap)==newwords
    for x in draft["entries"]:
        if level!="ALL" and x["level"]!=level:continue
        word=x["word"]
        assert re.fullmatch(r"[a-z]{3,}",word),word
        assert word in pool and pool[word]["level"]==x["level"],word
        assert POS[pool[word]["part_of_speech"]]==x["part_of_speech"],word
        assert len(x["english_definition"].strip())>=25,word
        assert re.search(r"[\u1000-\u109f]",x["burmese_meaning"]),word
        assert len(x["example_sentence"].strip())>=25,word
        assert re.search(r"(?<![a-z])"+re.escape(word)+r"(?![a-z])",x["example_sentence"].lower()),word
        assert x["example_sentence"][0].isupper() and x["example_sentence"][-1] in ".?!",word
        assert all(x[k] is False for k in FLAGS),word
        assert all(x[k]=="" for k in ("source_english","source_burmese","source_level")),word
        assert x["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and x["editorial_risk"],word
        t=taskmap[word]
        assert t["provisional_level"]==x["level"] and t["part_of_speech"]==x["part_of_speech"],word
        assert t["review_status"]=="PENDING_INDEPENDENT_REVIEW" and t["release_approved"] is False,word
        for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
            assert t[k]["completed"] is False and t[k]["reviewer"] is None and t[k]["observed_evidence"] is None,word
        assert t["english_definition_review"]["source_observed"] is False,word
        assert t["audio_review"]["completed"] is False and t["audio_review"]["real_listening"] is False and t["audio_review"]["real_device_test"] is False,word
    for x in held["records"]:
        assert x["word"] in pool and pool[x["word"]]["level"]==x["provisional_level"],x["word"]
        assert x["source_observed"] is False and x["reviewed_independently"] is False and x["release_approved"] is False,x["word"]
    if level=="ALL":
        byword=collections.defaultdict(list)
        for x in oldrows+draft["entries"]:byword[x["word"]].append(x)
        assert len(byword)==2161,len(byword)
        counts=collections.Counter(v[0]["level"] for v in byword.values())
        assert counts=={"A2":519,"B1":616,"B2":612,"C1":414},counts
        for word,versions in byword.items():
            assert all((x["level"],x["part_of_speech"],x["english_definition"],x["burmese_meaning"],x["example_sentence"])==
                       (versions[0]["level"],versions[0]["part_of_speech"],versions[0]["english_definition"],versions[0]["burmese_meaning"],versions[0]["example_sentence"]) for x in versions[1:]),("conflicting legacy duplicate",word)
        duplicates=sum(len(v)-1 for v in byword.values())
        assert duplicates==182,duplicates
        assert len(oldheldwords|heldwords)==591
        print("UNIQUE A2-C1 A2=519 B1=616 B2=612 C1=414 total=2161; independently approved=0")
        print("A1=500; A1-C1 written=2661; first drafts outstanding=2339; unique quarantine=591; legacy duplicate rows=182")
    assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print(f"STAGING ONLY batch34 {level} PASS: 95 drafts, 82 new held, zero approvals; no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    audit(p.parse_args().level)
