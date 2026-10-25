#!/usr/bin/env python3
"""Batch26 fail-closed staging structural QA; never certifies linguistic truth."""
import argparse, json, re
from collections import Counter, defaultdict
from pathlib import Path
R = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((R / path).read_text(encoding="utf-8"))
def audit(level):
    d = read("draft/A2-C1-EDITORIAL-BATCH26.json")
    t = read("draft/A2-C1-REVIEW-TASKS-BATCH26.json")
    q = read("draft/A2-C1-QUARANTINE-BATCH26.json")
    pool_rows = read("draft/UNVERIFIED_CEFR_CANDIDATES.json")["entries"]
    pool = {x["word"]: x for x in pool_rows}
    assert len(pool_rows) == len(pool) == 5000
    assert d["release_status"] == q["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert t["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["independently_approved"] == t["independently_approved"] == q["independently_approved"] == 0
    expected = {"A2": 16, "B1": 16, "B2": 15, "C1": 3}
    assert len(d["entries"]) == len(t["entries"]) == 50
    assert Counter(x["level"] for x in d["entries"]) == expected
    assert d["counts_by_provisional_level"] == expected
    assert len({x["word"] for x in d["entries"]}) == 50
    assert len({x["example_sentence"] for x in d["entries"]}) == 50
    assert len(q["records"]) == len({x["word"] for x in q["records"]}) == 22
    assert all(x["word"] in pool and pool[x["word"]]["level"] == x["provisional_level"] for x in q["records"])
    assert all(x["risk"] and x["evidence_note"] and x["source_observed"] is False
               and x["reviewed_independently"] is False and x["release_approved"] is False
               for x in q["records"])
    previous = ["draft/A2-C1-EDITORIAL-STARTER.json"] + [
        f"draft/A2-C1-EDITORIAL-BATCH{i:02d}.json" for i in range(9, 26)]
    prior = [x for p in previous for x in read(p)["entries"]]
    current = d["entries"]
    assert not {x["word"] for x in prior} & {x["word"] for x in current}, "draft duplicates"
    holds = ["draft/A2-C1-CANDIDATE-QUARANTINE.json"] + [
        f"draft/A2-C1-QUARANTINE-BATCH{i:02d}.json" for i in range(14, 27)]
    held_rows = [x for p in holds for x in read(p)["records"]]
    held = [x["word"] for x in held_rows]
    assert len(held) == len(set(held)) == 409, "quarantine collision"
    assert not set(held) & {x["word"] for x in prior + current}, "held word was drafted"
    assert all(x["reviewed_independently"] is False and x["release_approved"] is False for x in held_rows)
    taskmap = {x["word"]: x for x in t["entries"]}
    assert len(taskmap) == 50
    posmap = {"n":"noun","v":"verb","a":"adjective","s":"adjective","r":"adverb"}
    for x in current:
        if level != "ALL" and x["level"] != level:
            continue
        w = x["word"]
        assert re.fullmatch(r"[a-z]{3,}", w), w
        assert w in pool and pool[w]["level"] == x["level"], ("candidate tier mismatch", w)
        assert posmap[pool[w]["part_of_speech"]] == x["part_of_speech"], ("candidate POS mismatch", w)
        assert len(x["english_definition"].strip()) >= 25, w
        assert re.search(r"[\u1000-\u109f]", x["burmese_meaning"]), w
        assert len(x["example_sentence"].strip()) >= 25, w
        assert re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", x["example_sentence"].lower()), w
        assert all(x[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")), w
        assert all(x[k] == "" for k in ("source_english","source_burmese","source_level")), w
        assert x["status"] == "AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW", w
        assert x["editorial_risk"] and x["source_note"], w
        y = taskmap[w]
        assert y["provisional_level"] == x["level"] and y["part_of_speech"] == x["part_of_speech"], w
        assert y["review_status"] == "PENDING_INDEPENDENT_REVIEW" and y["release_approved"] is False, w
        assert y["english_definition_review"]["source_observed"] is False, w
        assert y["english_definition_review"]["reviewer"] is None and y["english_definition_review"]["observed_evidence"] is None, w
        assert y["english_definition_review"]["reference_url_to_consult"].startswith("https://dictionary.cambridge.org/dictionary/english/"), w
        assert y["burmese_review"]["reviewer"] is None and y["burmese_review"]["observed_evidence"] is None, w
        assert y["cefr_review"]["observed_evidence"] is None, w
        assert y["audio_review"]["real_listening"] is False and y["audio_review"]["real_device_test"] is False, w
        assert all(y[k]["completed"] is False for k in ("english_definition_review","burmese_review","example_review","cefr_review","audio_review")), w
    if level == "ALL":
        byword = defaultdict(list)
        for x in prior + current:
            byword[x["word"]].append(x)
        assert len(byword) == 1715, len(byword)
        assert Counter(v[0]["level"] for v in byword.values()) == {"A2":462,"B1":462,"B2":456,"C1":335}
        assert all(all((x["level"],x["part_of_speech"],x["english_definition"],x["burmese_meaning"],x["example_sentence"]) ==
                       (v[0]["level"],v[0]["part_of_speech"],v[0]["english_definition"],v[0]["burmese_meaning"],v[0]["example_sentence"])
                       for x in v[1:]) for v in byword.values()), "legacy duplicate conflict"
        print("UNIQUE A2-C1 A2=462 B1=462 B2=456 C1=335 total=1715; independent approvals=0")
        print("A1=500; A1-C1 written=2215; first drafts outstanding=2785; legacy duplicate rows=",sum(len(v)-1 for v in byword.values()))
    assert "entries:[]" in (R/"cefr-vocabulary-data.js").read_text(encoding="utf-8")
    print("STAGING ONLY batch26", level, "PASS: 50 drafts, 22 held, zero approvals; no audio/deploy")
if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=("A2","B1","B2","C1","ALL"),default="ALL")
    audit(p.parse_args().level)
