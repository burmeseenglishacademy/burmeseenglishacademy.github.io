#!/usr/bin/env python3
"""Batch44 fail-closed structural staging QA; no linguistic approval."""
import argparse,collections,json,re,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
EXPECTED={"A2":0,"B1":0,"B2":25,"C1":16}
HELD={"A2":0,"B1":0,"B2":23,"C1":26}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
def read(p):return json.loads((R/p).read_text(encoding="utf-8"))
def run(level):
    if level=="ALL":
        prior=subprocess.run([sys.executable,"tools/audit_cefr_batch43_review_tasks.py","--level","ALL"],cwd=R,text=True,capture_output=True)
        assert prior.returncode==0,prior.stdout+prior.stderr
        print(prior.stdout.strip())
    d=read("draft/A2-C1-EDITORIAL-BATCH44.json")
    t=read("draft/A2-C1-REVIEW-TASKS-BATCH44.json")
    q=read("draft/A2-C1-QUARANTINE-BATCH44.json")
    pool={x["word"]:x for x in read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
    assert len(pool)==5000
    assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert all(z["independently_approved"]==0 for z in (d,t,q))
    assert len(d["entries"])==len(t["entries"])==41
    assert len(q["records"])==49
    assert d["counts_by_provisional_level"]==t["counts_by_provisional_level"]==EXPECTED
    assert q["counts_by_provisional_level"]==HELD
    assert {k:v for k,v in collections.Counter(x["level"] for x in d["entries"]).items()}=={k:v for k,v in EXPECTED.items() if v}
    assert {k:v for k,v in collections.Counter(x["provisional_level"] for x in q["records"]).items()}=={k:v for k,v in HELD.items() if v}
    drafts={x["word"]:x for x in d["entries"]}
    tasks={x["word"]:x for x in t["entries"]}
    holds={x["word"]:x for x in q["records"]}
    assert len(drafts)==len(tasks)==41 and len(holds)==49
    assert set(drafts)==set(tasks) and not set(drafts)&set(holds)
    assert len({x["example_sentence"] for x in drafts.values()})==len(drafts)
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
        for k in ("english_definition_review","burmese_review","example_review","cefr_review"):
            assert x[k]["completed"] is False and x[k]["reviewer"] is None and x[k]["observed_evidence"] is None,word
        assert x["english_definition_review"]["source_observed"] is False,word
        assert x["audio_review"]["completed"] is False and x["audio_review"]["real_listening"] is False and x["audio_review"]["real_device_test"] is False,word
    for word,r in holds.items():
        if level!="ALL" and r["provisional_level"]!=level:continue
        assert word in pool and pool[word]["level"]==r["provisional_level"],word
        assert r["reviewed_independently"] is False and r["release_approved"] is False,word
        if word in ["presumably","subtle","allegedly","alter","realm","momentum"]:
            assert r["source_observed"] is True and r["source_url"].startswith("https://dictionary.cambridge.org/") and r["source_observation_type"]=="AI_ASSISTED_DIRECT_CAMBRIDGE_PAGE_OBSERVATION_NOT_INDEPENDENT_REVIEW",word
        else:
            assert r["source_observed"] is False,word
    if level=="ALL":
        obs=read("draft/A2-C1-SOURCE-OBSERVATIONS-BATCH44.json")
        assert obs["release_status"]=="UNVERIFIED_SOURCE_OBSERVATIONS_NOT_INDEPENDENT_APPROVAL"
        assert len(obs["records"])==8 and {x["word"] for x in obs["records"]}=={'presumably','subtle','allegedly','alter','realm','momentum','purely','nomination'},obs
        assert all(x["independently_approved"] is False and x["burmese_reviewed"] is False and x["example_reviewed"] is False and x["audio_listened"] is False for x in obs["records"])
        oldfiles=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,45)]
        oldholds=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,45)]
        allrows=[x for p in oldfiles for x in read(p)["entries"]]
        grouped=collections.defaultdict(list)
        for x in allrows:grouped[x["word"]].append(x)
        assert all(len({x["level"] for x in v})==1 for v in grouped.values())
        assert sum(len(v)-1 for v in grouped.values())==182
        assert len(grouped)==2655
        bylevel=collections.Counter(v[0]["level"] for v in grouped.values())
        assert bylevel=={"A2":521,"B1":747,"B2":853,"C1":534},bylevel
        heldwords=[x["word"] for p in oldholds for x in read(p)["records"]]
        assert len(heldwords)==len(set(heldwords))==922
        assert not set(heldwords)&set(grouped)
        assert all(all(x[k] is False for k in FLAGS) for v in grouped.values() for x in v)
        assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
        print("UNIQUE A2-C1 "+str(dict(bylevel))+" total=2655; independently approved=0")
        print("A1=500; A1-C1 written=3155; outstanding=1845; quarantine=922; legacy duplicate rows=182")
    print("STAGING ONLY batch44 "+level+" PASS: 41 new drafts, 49 holds, zero independent approvals; no audio/deploy")
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    run(p.parse_args().level)
