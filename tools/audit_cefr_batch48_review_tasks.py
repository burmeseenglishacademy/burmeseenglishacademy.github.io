#!/usr/bin/env python3
"""Batch48 unpublished structural audit; NOT independent linguistic or CEFR verification."""
import argparse, collections, json, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LEVELS=("A2","B1","B2","C1")
EXPECTED={"A2":8,"B1":18,"B2":20,"C1":20}
HELD={"A2":3,"B1":6,"B2":22,"C1":18}
TOTAL={"A2":529,"B1":765,"B2":906,"C1":653}
POS={"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
FLAGS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
def read(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))
def audit(level):
    if level=="ALL":
        previous=subprocess.run([sys.executable,"tools/audit_cefr_batch47_review_tasks.py","--level","ALL"],cwd=ROOT,text=True,capture_output=True)
        assert previous.returncode==0, previous.stdout+previous.stderr
        print(previous.stdout.strip())
    d=read("draft/A2-C1-EDITORIAL-BATCH48.json")
    t=read("draft/A2-C1-REVIEW-TASKS-BATCH48.json")
    q=read("draft/A2-C1-QUARANTINE-BATCH48.json")
    pool_rows=read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool={r["word"]:r for r in pool_rows}
    assert len(pool_rows)==len(pool)==5000
    assert d["release_status"]==q["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"]=="UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert all(x["independently_approved"]==0 for x in (d,t,q))
    assert d["counts_by_provisional_level"]==t["counts_by_provisional_level"]==EXPECTED
    assert q["counts_by_provisional_level"]==HELD
    assert len(d["entries"])==len(t["entries"])==66
    assert len(q["records"])==49
    assert collections.Counter(r["level"] for r in d["entries"])==EXPECTED
    assert collections.Counter(r["provisional_level"] for r in q["records"])==HELD
    assert d["stages"]=={"english":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","myanmar":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","example":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED","source_evidence":"PENDING_SEPARATE_REVIEW_TASKS"}
    drafts={r["word"]:r for r in d["entries"]}
    tasks={r["word"]:r for r in t["entries"]}
    holds={r["word"]:r for r in q["records"]}
    assert len(drafts)==len(tasks)==66 and len(holds)==49
    assert set(drafts)==set(tasks) and not set(drafts)&set(holds)
    assert len({r["example_sentence"] for r in d["entries"]})==66
    for word,row in drafts.items():
        if level!="ALL" and row["level"]!=level:continue
        assert re.fullmatch(r"[a-z]{3,}",word),word
        assert word in pool and pool[word]["level"]==row["level"],word
        assert POS[pool[word]["part_of_speech"]]==row["part_of_speech"],word
        assert len(row["english_definition"])>=25,word
        assert re.search(r"[\u1000-\u109f]",row["burmese_meaning"]),word
        example=row["example_sentence"]
        assert len(example)>=25 and example[0].isupper() and example[-1] in ".?!",word
        assert re.search(r"(?<![a-z])"+re.escape(word)+r"(?![a-z])",example.lower()),word
        assert all(row[f] is False for f in FLAGS),word
        assert all(row[f]=="" for f in ("source_english","source_burmese","source_level")),word
        assert row["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
        assert "UNVERIFIED" in row["editorial_risk"],word
        task=tasks[word]
        assert task["provisional_level"]==row["level"] and task["part_of_speech"]==row["part_of_speech"],word
        assert task["review_status"]=="PENDING_INDEPENDENT_REVIEW" and task["release_approved"] is False,word
        assert task["cefr_review"]["provisional_level_risk"]==row["editorial_risk"],word
        for section in ("english_definition_review","burmese_review","example_review","cefr_review"):
            assert task[section]["completed"] is False and task[section]["reviewer"] is None and task[section]["observed_evidence"] is None,word
        assert task["english_definition_review"]["source_observed"] is False,word
        assert task["audio_review"]["completed"] is False and task["audio_review"]["real_listening"] is False and task["audio_review"]["real_device_test"] is False,word
    for word,row in holds.items():
        if level!="ALL" and row["provisional_level"]!=level:continue
        assert word in pool and pool[word]["level"]==row["provisional_level"],word
        assert row["source_observed"] is False and row["reviewed_independently"] is False and row["release_approved"] is False,word
        assert "No independent" in row["evidence_note"],word
    if level=="ALL":
        paths=["draft/A2-C1-EDITORIAL-STARTER.json"]+[f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,49)]
        holdpaths=["draft/A2-C1-CANDIDATE-QUARANTINE.json"]+[f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,49)]
        allrows=[row for p in paths for row in read(p)["entries"]]
        grouped=collections.defaultdict(list)
        for row in allrows:grouped[row["word"]].append(row)
        assert all(len({x["level"] for x in rows})==1 for rows in grouped.values())
        assert sum(len(rows)-1 for rows in grouped.values())==182
        assert len(grouped)==2853,len(grouped)
        bylevel=collections.Counter(rows[0]["level"] for rows in grouped.values())
        assert bylevel==TOTAL,bylevel
        heldwords=[r["word"] for p in holdpaths for r in read(p)["records"]]
        assert len(heldwords)==len(set(heldwords))==1079,len(heldwords)
        assert not set(heldwords)&set(grouped)
        assert all(all(row[f] is False for f in FLAGS) for rows in grouped.values() for row in rows)
        assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
        print(f"UNIQUE A2-C1 {dict(bylevel)} total=2853; independently approved=0")
        print("A1=500; A1-C1 written=3353; outstanding=1647; quarantine=1079; historical duplicate rows excluded=182")
    print(f"STAGING ONLY batch48 {level} PASS: 66 new drafts, 49 reversible holds, zero independent approvals; no audio/deploy")
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    audit(ap.parse_args().level)
