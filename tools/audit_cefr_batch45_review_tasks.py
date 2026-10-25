#!/usr/bin/env python3
"""Batch45 staging-only structural QA. Never equate automated checks with linguistic approval."""
import argparse, collections, json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A2", "B1", "B2", "C1")
EXPECTED = {"A2": 0, "B1": 0, "B2": 24, "C1": 24}
HELD = {"A2": 0, "B1": 0, "B2": 29, "C1": 32}
POS = {"n": "noun", "v": "verb", "a": "adjective", "s": "adjective", "r": "adverb"}
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation")

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def audit(level):
    if level == "ALL":
        prior = subprocess.run([sys.executable, "tools/audit_cefr_batch44_review_tasks.py", "--level", "ALL"], cwd=ROOT, text=True, capture_output=True)
        assert prior.returncode == 0, prior.stdout + prior.stderr
        print(prior.stdout.strip())
    d = read("draft/A2-C1-EDITORIAL-BATCH45.json")
    t = read("draft/A2-C1-REVIEW-TASKS-BATCH45.json")
    q = read("draft/A2-C1-QUARANTINE-BATCH45.json")
    pool_rows = read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool = {x["word"]: x for x in pool_rows}
    assert len(pool_rows) == len(pool) == 5000
    assert d["release_status"] == q["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert all(x["independently_approved"] == 0 for x in (d, t, q))
    assert d["counts_by_provisional_level"] == t["counts_by_provisional_level"] == EXPECTED
    assert q["counts_by_provisional_level"] == HELD
    assert len(d["entries"]) == len(t["entries"]) == 48
    assert len(q["records"]) == 61
    assert collections.Counter(x["level"] for x in d["entries"]) == {"B2":24, "C1":24}
    assert collections.Counter(x["provisional_level"] for x in q["records"]) == {"B2":29, "C1":32}
    assert d["stages"] == {
        "english":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED",
        "myanmar":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED",
        "example":"FIRST_PASS_NOT_INDEPENDENTLY_REVIEWED",
        "source_evidence":"PENDING_SEPARATE_REVIEW_TASKS"
    }
    drafts = {x["word"]: x for x in d["entries"]}
    tasks = {x["word"]: x for x in t["entries"]}
    holds = {x["word"]: x for x in q["records"]}
    assert len(drafts) == len(tasks) == 48 and len(holds) == 61
    assert set(drafts) == set(tasks) and not set(drafts) & set(holds)
    assert len({x["example_sentence"] for x in drafts.values()}) == 48
    for word, r in drafts.items():
        if level != "ALL" and r["level"] != level:
            continue
        assert re.fullmatch(r"[a-z]{3,}", word), word
        assert word in pool and pool[word]["level"] == r["level"], word
        assert POS[pool[word]["part_of_speech"]] == r["part_of_speech"], word
        assert len(r["english_definition"]) >= 25, word
        assert re.search(r"[\u1000-\u109f]", r["burmese_meaning"]), word
        example = r["example_sentence"]
        assert len(example) >= 25 and example[0].isupper() and example[-1] in ".?!", word
        assert re.search(r"(?<![a-z])" + re.escape(word) + r"(?![a-z])", example.lower()), word
        assert all(r[f] is False for f in FLAGS), word
        assert all(r[f] == "" for f in ("source_english", "source_burmese", "source_level")), word
        assert r["status"] == "AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" and r["editorial_risk"], word
        task = tasks[word]
        assert task["provisional_level"] == r["level"] and task["part_of_speech"] == r["part_of_speech"], word
        assert task["review_status"] == "PENDING_INDEPENDENT_REVIEW" and task["release_approved"] is False, word
        assert task["cefr_review"]["provisional_level_risk"] == r["editorial_risk"], word
        for section in ("english_definition_review", "burmese_review", "example_review", "cefr_review"):
            assert task[section]["completed"] is False and task[section]["reviewer"] is None and task[section]["observed_evidence"] is None, word
        assert task["english_definition_review"]["source_observed"] is False, word
        assert task["audio_review"]["completed"] is False and task["audio_review"]["real_listening"] is False and task["audio_review"]["real_device_test"] is False, word
    for word, r in holds.items():
        if level != "ALL" and r["provisional_level"] != level:
            continue
        assert word in pool and pool[word]["level"] == r["provisional_level"], word
        assert r["source_observed"] is False and r["reviewed_independently"] is False and r["release_approved"] is False, word
        assert len(r["evidence_note"]) > 40 and "No independent" in r["evidence_note"], word
    if level == "ALL":
        paths = ["draft/A2-C1-EDITORIAL-STARTER.json"] + [f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9,46)]
        hold_paths = ["draft/A2-C1-CANDIDATE-QUARANTINE.json"] + [f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14,46)]
        all_rows = [row for p in paths for row in read(p)["entries"]]
        grouped = collections.defaultdict(list)
        for row in all_rows:
            grouped[row["word"]].append(row)
        assert all(len({x["level"] for x in rows}) == 1 for rows in grouped.values())
        assert sum(len(rows)-1 for rows in grouped.values()) == 182
        assert len(grouped) == 2703, len(grouped)
        bylevel = collections.Counter(rows[0]["level"] for rows in grouped.values())
        assert bylevel == {"A2":521, "B1":747, "B2":877, "C1":558}, bylevel
        held_words = [row["word"] for p in hold_paths for row in read(p)["records"]]
        assert len(held_words) == len(set(held_words)) == 983, len(held_words)
        assert not set(held_words) & set(grouped), set(held_words) & set(grouped)
        assert all(all(row[f] is False for f in FLAGS) for rows in grouped.values() for row in rows)
        assert "entries:[]" in (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
        print(f"UNIQUE A2-C1 {dict(bylevel)} total=2703; independently approved=0")
        print("A1=500; A1-C1 written=3203; outstanding=1797; quarantine=983; historical duplicate rows excluded=182")
    print(f"STAGING ONLY batch45 {level} PASS: 48 new drafts, 61 new reversible holds, zero independent approvals; no audio/deploy")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    audit(parser.parse_args().level)
