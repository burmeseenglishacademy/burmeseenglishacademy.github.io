#!/usr/bin/env python3
"""Batch74: nonpublishing structural integrity checks. NEVER editorial or CEFR approval."""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "draft"
EXPECTED = {"A2": 15, "B1": 15, "B2": 15, "C1": 15}
HOLD = [
    "SENSE_SPECIFIC_CEFR_SOURCE_NOT_OBSERVED",
    "INDEPENDENT_ENGLISH_MYANMAR_EXAMPLE_REVIEW_PENDING",
    "REAL_PRONUNCIATION_LISTENING_NOT_DONE",
]

def read(name):
    return json.loads((D / name).read_text(encoding="utf-8"))

def authored_before_batch74():
    paths = [D / "A1-EDITORIAL-STARTER.json"]
    paths += sorted(D.glob("A1-EXPANSION-BATCH*.json"))
    paths += [D / "A2-C1-EDITORIAL-STARTER.json"]
    paths += sorted(D.glob("A2-C1-EDITORIAL-BATCH*.json"))
    paths += sorted(D.glob("A2-C1-RETIER-EDITORIAL-BATCH*.json"))
    paths += [p for p in sorted(D.glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json")) if "BATCH74" not in p.name]
    result = collections.defaultdict(list)
    for path in paths:
        for entry in json.loads(path.read_text(encoding="utf-8"))["entries"]:
            result[entry["word"].casefold()].append(path.name)
    return result

def audit(level):
    d = read("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH74.json")
    t = read("A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH74.json")
    q = read("A2-C1-SOURCE-RECOVERY-QUARANTINE-BATCH74.json")
    triage = read("BATCH74-CANDIDATE-TRIAGE.json")
    E, T, Q = d["entries"], t["entries"], q["records"]
    assert d["release_status"] == "UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH"
    assert t["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert q["release_status"] == "REVERSIBLE_EDITORIAL_QUARANTINE_NOT_APPROVED_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["counts_by_proposed_level"] == EXPECTED
    assert len(E) == len(T) == len(Q) == 60
    assert collections.Counter(e["proposed_level"] for e in E) == EXPECTED
    assert len({e["word"].casefold() for e in E}) == 60
    assert {e["word"] for e in E} == {x["word"] for x in T} == {x["word"] for x in Q}
    assert set(d["stages"].values()) == {
        "ORIGINAL_FIRST_PASS_UNVERIFIED", "NOT_OBSERVED", "NOT_GENERATED_NOT_LISTENED"
    }
    assert triage["screened"] == 549
    assert triage["clear_only"] == 261 and triage["quarantined"] == 288
    assert sum(not r["risk_flags"] for r in triage["records"]) == 261
    assert len(triage["records"]) == 549
    candidate_pairs = set()
    for line in (D / "BATCH74-CANDIDATES.txt").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        lvl, word = line.split("|")
        candidate_pairs.add((lvl, word))
    assert candidate_pairs == {(r["level"], r["word"]) for r in triage["records"]}
    screened = {(r["level"], r["word"]): r for r in triage["records"]}
    previous = authored_before_batch74()
    pool = {r["word"].casefold(): r for r in read("UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
    tasks = {x["word"]: x for x in T}
    holds = {x["word"]: x for x in Q}
    problems = []
    count = 0
    risk_count = 0
    for e in E:
        if level != "ALL" and e["proposed_level"] != level:
            continue
        count += 1
        w = e["word"]
        task = tasks[w]
        hold = holds[w]
        assert re.fullmatch(r"[a-z]{3,}", w), w
        assert e["part_of_speech"] in ("noun", "verb", "adjective", "adverb", "plural noun"), w
        assert len(e["english_definition"]) >= 30, w
        assert re.search(r"[\u1000-\u109f]", e["burmese_meaning"]), w
        sentence = e["example_sentence"]
        assert len(sentence) >= 35 and sentence[0].isupper() and sentence[-1] in ".?!", w
        assert re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", sentence.casefold()), w
        assert e["editorial_hold"] is True and e["release_approved"] is False, w
        assert e["status"] == "REVERSIBLE_QUARANTINE_PENDING_INDEPENDENT_EVIDENCE", w
        assert e["editorial_hold_reasons"] == HOLD, w
        assert all(e[k] is False for k in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation")), w
        assert all(e[k] == "" for k in ("source_english", "source_burmese", "source_level")), w
        assert task["editorial_hold"] is True and task["release_approved"] is False, w
        for k in ("english_definition_review", "burmese_review", "example_review", "cefr_review"):
            assert task[k]["completed"] is False and task[k]["reviewer"] is None and task[k]["observed_evidence"] is None, w
        assert task["english_definition_review"]["source_observed"] is False, w
        assert all(v is False for v in task["audio_review"].values()), w
        assert hold["hold_reversible"] is True and hold["reason_codes"] == HOLD, w
        assert hold["independently_approved"] is False and hold["release_approved"] is False, w
        assert hold["additional_risk_flags"] == e["editorial_risks"] == task["editorial_risks"], w
        risk_count += len(e["editorial_risks"])
        if w.casefold() in previous:
            problems.append({"word": w, "reason": "PRIOR_AUTHORED_COLLISION", "files": previous[w.casefold()]})
        s = screened.get((e["proposed_level"], w))
        if not s or s["mechanical_status"] != "CLEAR_ONLY_NOT_APPROVED" or s["risk_flags"]:
            problems.append({"word": w, "reason": "NOT_CLEAR_IN_OBSERVED_PREFLIGHT"})
        if not s or s["independently_checked"] is not False:
            problems.append({"word": w, "reason": "PREFLIGHT_NOT_INDEPENDENT"})
        p = pool.get(w.casefold())
        if p and p.get("level") != e["proposed_level"]:
            problems.append({"word": w, "reason": "UNVERIFIED_SEED_TIER_DISAGREEMENT"})
        if p and re.search(r"\b(?:surname|given name|capital of|city in|genus|species|trademark)\b", str(p.get("english_definition_draft", "")), re.I):
            problems.append({"word": w, "reason": "SUSPECT_WORDNET_OR_NAMED_ENTITY_SENSE"})
    if level == "ALL":
        publication = (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
        assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in publication
        assert re.search(r"entries:\s*\[\s*\]", publication)
        historical = read("BATCH72-HISTORICAL-CROSS-LEVEL-HOLDS.json")
        assert historical["wordforms"] == 24 and historical["all_held"] is True
        (ROOT / "batch74-structural-hold-report.json").write_text(json.dumps({
            "batch": 74, "drafts": len(E), "by_level": EXPECTED,
            "independently_approved": 0, "audio_generated": 0,
            "source_verified": 0, "release_approved": 0,
            "editorial_risk_flags": risk_count, "problems": problems,
            "historical_cross_level_holds_unresolved": 24,
            "preflight_run": 40440285272
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("BATCH74", level, "checked", count, "risk flags", risk_count, "problems", json.dumps(problems))
    assert not problems, "Drafts are quarantined; resolve structural problems before review"
    print("PASS: STRUCTURAL ONLY. Zero independent approvals. No audio, merge or publication.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=[*EXPECTED, "ALL"], required=True)
    audit(p.parse_args().level)
