#!/usr/bin/env python3
"""Batch28 fail-closed structural QA only; NOT an independent linguistic review."""
import argparse, json, re
from pathlib import Path
from collections import Counter, defaultdict
R=Path(__file__).resolve().parents[1]
def read(p): return json.loads((R/p).read_text(encoding="utf-8"))
def audit(level):
    d=read("draft/A2-C1-EDITORIAL-BATCH29.json")
    t=read("draft/A2-C1-REVIEW-TASKS-BATCH29.json")
    q=read("draft/A2-C1-QUARANTINE-BATCH29.json")
    poolrows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool={x["word"]:x for x in poolrows}
    assert len(poolrows)==len(pool)==5000
    assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["independently_approved"]==t["independently_approved"]==q["independently_approved"]==0
    expected={"A2":8,"B1":10,"B2":12,"C1":12}
    assert len(d["entries"])==len(t["entries"])==42
    assert Counter(x["level"] for x in d["entries"])==expected
    assert d["counts_by_provisional_level"]==expected
    assert len({x["word"] for x in d["entries"]})==42
    assert len({x["example_sentence"] for x in d["entries"]})==42
    assert len(q["records"])==len({x["word"] for x in q["records"]})==9
    assert all(x["word"] in pool and pool[x["word"]]["level"]==x["provisional_level"] for x in q["records"])
    assert all(x["risk"] and x["evidence_note"] and x["source_observed"] is False
               and x["reviewed_independently"] is False and x["release_approved"] is False for x in q["records"])
    paths=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,29)]
    prior=[x for p in paths for x in read(p)["entries"]]
    current=d["entries"]
    assert not {x["word"] for x in prior}&{x["word"] for x in current}, "draft duplicates"
    holds=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,30)]
    heldrows=[x for p in holds for x in read(p)["records"]]
    held=[x["word"] for x in heldrows]
    assert len(held)==len(set(held))==449, ("quarantine collision",len(held),len(set(held)))
    assert not set(held)&{x["word"] for x in prior+current}, "held word was drafted"
    assert all(x["reviewed_independently"] is False and x["release_approved"] is False for x in heldrows)
    taskmap={x["word"]:x for x in t["entries"]}
    assert len(taskmap)==42
    posmap={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
    for x in current:
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
        assert x["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW",w
        assert x["editorial_risk"] and x["source_note"],w
        y=taskmap[w]
        assert y["provisional_level"]==x["level"] and y["part_of_speech"]==x["part_of_speech"],w
        assert y["review_status"]=="PENDING_INDEPENDENT_REVIEW" and y["release_approved"] is False,w
        assert y["english_definition_review"]["source_observed"] is False,w
        assert y["english_definition_review"]["reference_url_to_consult"].startswith("https://dictionary.cambridge.org/dictionary/english/"),w
        assert all(y[k]["observed_evidence"] is None and y[k]["reviewer"] is None and y[k]["completed"] is False
                   for k in ("english_definition_review","burmese_review","example_review","cefr_review")),w
        assert y["audio_review"]["real_listening"] is False and y["audio_review"]["real_device_test"] is False,w
        assert y["audio_review"]["reviewer"] is None and y["audio_review"]["completed"] is False,w
    if level=="ALL":
        byword=defaultdict(list)
        for x in prior+current: byword[x["word"]].append(x)
        assert len(byword)==1870,len(byword)
        assert Counter(v[0]["level"] for v in byword.values())=={"A2":494,"B1":507,"B2":507,"C1":362}
        assert all(all((x["level"],x["part_of_speech"],x["english_definition"],x["burmese_meaning"],x["example_sentence"])==
            (v[0]["level"],v[0]["part_of_speech"],v[0]["english_definition"],v[0]["burmese_meaning"],v[0]["example_sentence"]) for x in v[1:]) for v in byword.values()),"legacy duplicate conflict"
        print("UNIQUE A2-C1 A2=494 B1=507 B2=507 C1=362 total=1870; independently approved=0")
        print("A1=500; A1-C1 written=2370; first drafts outstanding=2630; legacy duplicate rows=",sum(len(v)-1 for v in byword.values()))
    assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print("STAGING ONLY batch29",level,"PASS: 42 drafts, 9 held, zero approvals; no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=("A2","B1","B2","C1","ALL"),default="ALL")
    audit(p.parse_args().level)
