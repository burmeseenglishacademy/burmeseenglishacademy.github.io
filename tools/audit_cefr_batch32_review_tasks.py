#!/usr/bin/env python3
"""Batch32 fail-closed structural QA, NOT linguistic review or audio validation."""
import argparse,json,re
from pathlib import Path
from collections import Counter,defaultdict
R=Path(__file__).resolve().parents[1]
def read(p): return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
    from subprocess import run
    # Preserve the prior inventory baseline and all its structural checks.
    if level=="ALL":
        old=run(["python3","tools/audit_cefr_batch31_review_tasks.py","--level","ALL"],cwd=R,check=True,capture_output=True,text=True)
        print(old.stdout.strip())
    d=read("draft/A2-C1-EDITORIAL-BATCH32.json")
    t=read("draft/A2-C1-REVIEW-TASKS-BATCH32.json")
    q=read("draft/A2-C1-QUARANTINE-BATCH32.json")
    poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool={x["word"]:x for x in poolrows}
    assert len(poolrows)==len(pool)==5000
    assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["independently_approved"]==t["independently_approved"]==q["independently_approved"]==0
    expected={"A2":3,"B1":9,"B2":13,"C1":15}
    assert len(d["entries"])==len(t["entries"])==40
    assert Counter(x["level"] for x in d["entries"])==expected
    assert d["counts_by_provisional_level"]==expected
    assert len({x["word"] for x in d["entries"]})==40
    assert len({x["example_sentence"] for x in d["entries"]})==40
    assert len(q["records"])==len({x["word"] for x in q["records"]})==7
    olddraft=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,32)]
    prior=[x for p in olddraft for x in read(p)["entries"]]
    heldfiles=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,33)]
    held=[x for p in heldfiles for x in read(p)["records"]]
    assert len({x["word"] for x in held})==len(held)==479, ("held_count",len(held),"unique",len({x["word"] for x in held}),"duplicates",[w for w,c in Counter(x["word"] for x in held).items() if c>1])
    assert not {x["word"] for x in prior}&{x["word"] for x in d["entries"]},("duplicate_prior_draft",sorted({x["word"] for x in prior}&{x["word"] for x in d["entries"]}))
    assert not {x["word"] for x in held}&{x["word"] for x in prior+d["entries"]},("held_drafted",sorted({x["word"] for x in held}&{x["word"] for x in prior+d["entries"]}))
    assert all(x["reviewed_independently"] is False and x["release_approved"] is False for x in held)
    assert all(x["word"] in pool and x["provisional_level"]==pool[x["word"]]["level"] and x["source_observed"] is False for x in q["records"])
    taskmap={x["word"]:x for x in t["entries"]}
    assert len(taskmap)==40
    posmap={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
    for x in d["entries"]:
        if level!="ALL" and x["level"]!=level: continue
        w=x["word"]
        assert re.fullmatch(r"[a-z]{3,}",w),w
        assert w in pool and pool[w]["level"]==x["level"],("tier",w)
        assert posmap[pool[w]["part_of_speech"]]==x["part_of_speech"],("POS",w)
        assert len(x["english_definition"].strip())>=25,w
        assert re.search(r"[\u1000-\u109f]",x["burmese_meaning"]),w
        assert len(x["example_sentence"].strip())>=25,w
        assert re.search(r"(?<![a-z])"+re.escape(w)+r"(?![a-z])",x["example_sentence"].lower()),w
        assert all(x[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),w
        assert all(x[k]=="" for k in ("source_english","source_burmese","source_level")),w
        assert x["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and x["editorial_risk"] and x["source_note"],w
        y=taskmap[w]
        assert y["provisional_level"]==x["level"] and y["part_of_speech"]==x["part_of_speech"],w
        assert y["review_status"]=="PENDING_INDEPENDENT_REVIEW" and not y["release_approved"],w
        assert y["english_definition_review"]["source_observed"] is False
        assert y["english_definition_review"]["reference_url_to_consult"].startswith("https://dictionary.cambridge.org/dictionary/english/")
        assert all(y[k]["observed_evidence"] is None and y[k]["reviewer"] is None and y[k]["completed"] is False for k in ("english_definition_review","burmese_review","example_review","cefr_review")),w
        assert y["audio_review"]["real_listening"] is False and y["audio_review"]["real_device_test"] is False and y["audio_review"]["completed"] is False,w
    if level=="ALL":
        byword=defaultdict(list)
        for x in prior+d["entries"]: byword[x["word"]].append(x)
        assert len(byword)==2022,len(byword)
        assert Counter(v[0]["level"] for v in byword.values())=={"A2":513,"B1":550,"B2":552,"C1":407}
        assert all(all((x["level"],x["part_of_speech"],x["english_definition"],x["burmese_meaning"],x["example_sentence"])==(v[0]["level"],v[0]["part_of_speech"],v[0]["english_definition"],v[0]["burmese_meaning"],v[0]["example_sentence"]) for x in v[1:]) for v in byword.values()),"legacy duplicate conflict"
        print("UNIQUE A2-C1 A2=513 B1=550 B2=552 C1=407 total=2022; independently approved=0")
        print("A1=500; A1-C1 written=2522; first drafts outstanding=2478; legacy duplicate rows=",sum(len(v)-1 for v in byword.values()))
    assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print("STAGING ONLY batch32",level,"PASS: 40 drafts, 7 new held, zero approvals; no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=("A2","B1","B2","C1","ALL"),default="ALL")
    audit(p.parse_args().level)
