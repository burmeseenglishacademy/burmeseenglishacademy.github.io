#!/usr/bin/env python3
"""Batch73 nonpublishing bilingual staging audit. Structural checks are NOT editorial approval."""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "draft"
EXPECTED = {"A2": 12, "B1": 20, "B2": 10, "C1": 8}
HOLD = [
    "SENSE_SPECIFIC_CEFR_SOURCE_NOT_OBSERVED",
    "INDEPENDENT_ENGLISH_MYANMAR_EXAMPLE_REVIEW_PENDING",
    "REAL_PRONUNCIATION_LISTENING_NOT_DONE",
]

def read(name):
    return json.loads((D / name).read_text(encoding="utf-8"))

def prior_words():
    paths = [D / "A1-EDITORIAL-STARTER.json"]
    paths += sorted(D.glob("A1-EXPANSION-BATCH*.json"))
    paths += [D / "A2-C1-EDITORIAL-STARTER.json"]
    paths += sorted(D.glob("A2-C1-EDITORIAL-BATCH*.json"))
    paths += sorted(D.glob("A2-C1-RETIER-EDITORIAL-BATCH*.json"))
    paths += [p for p in sorted(D.glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json")) if "BATCH73" not in p.name]
    index = collections.defaultdict(list)
    for p in paths:
        for e in json.loads(p.read_text(encoding="utf-8"))["entries"]:
            index[e["word"].casefold()].append(p.name)
    return index

def main(level):
    d = read("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH73.json")
    t = read("A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH73.json")
    q = read("A2-C1-SOURCE-RECOVERY-QUARANTINE-BATCH73.json")
    E, T, Q = d["entries"], t["entries"], q["records"]
    assert d["release_status"] == "UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH"
    assert t["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert q["release_status"] == "REVERSIBLE_EDITORIAL_QUARANTINE_NOT_APPROVED_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert d["counts_by_proposed_level"] == EXPECTED
    assert len(E) == len(T) == len(Q) == 50
    assert collections.Counter(e["proposed_level"] for e in E) == EXPECTED
    assert len({e["word"].casefold() for e in E}) == 50
    assert {e["word"] for e in E} == {x["word"] for x in T} == {x["word"] for x in Q}
    assert set(d["stages"].values()) == {
        "ORIGINAL_FIRST_PASS_UNVERIFIED", "NOT_OBSERVED", "NOT_GENERATED_NOT_LISTENED"
    }
    previous = prior_words()
    triage = read("BATCH72-EXTRA-CANDIDATE-TRIAGE.json")
    assert triage["screened"] == 167 and triage["clear_only"] == 86 and triage["quarantined"] == 81
    clear = {(r["level"], r["word"]): r for r in triage["records"]}
    earlier = read("BATCH70-CANDIDATE-TRIAGE.json")
    earlier_clear = {(r["proposed_level"], r["word"]): r for r in earlier["records"]}
    pool = {r["word"].casefold(): r for r in read("UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
    tasks = {r["word"]: r for r in T}
    quarantine = {r["word"]: r for r in Q}
    selected = 0
    problems = []
    risk_count = 0
    for e in E:
        if level != "ALL" and e["proposed_level"] != level:
            continue
        selected += 1
        w = e["word"]
        x = tasks[w]
        h = quarantine[w]
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
        assert x["editorial_hold"] is True and x["release_approved"] is False, w
        for k in ("english_definition_review", "burmese_review", "example_review", "cefr_review"):
            assert x[k]["completed"] is False and x[k]["reviewer"] is None and x[k]["observed_evidence"] is None, w
        assert x["english_definition_review"]["source_observed"] is False, w
        assert all(v is False for v in x["audio_review"].values()), w
        assert h["hold_reversible"] is True and h["reason_codes"] == HOLD, w
        assert h["independently_approved"] is False and h["release_approved"] is False, w
        assert h["additional_risk_flags"] == e["editorial_risks"] == x["editorial_risks"], w
        risk_count += len(e["editorial_risks"])
        if w.casefold() in previous:
            problems.append({"word": w, "issue": "PRIOR_AUTHORED_COLLISION", "files": previous[w.casefold()]})
        screening = clear.get((e["proposed_level"], w))
        if not screening or screening["mechanical_status"] != "CLEAR_ONLY_NOT_APPROVED":
            problems.append({"word": w, "issue": "NOT_CLEAR_IN_OBSERVED_BATCH72_PREFLIGHT"})
        if not screening or screening["independently_checked"] is not False:
            problems.append({"word": w, "issue": "SCREENING_INDEPENDENCE_MISMATCH"})
        prev = earlier_clear.get((e["proposed_level"], w))
        if prev and prev["mechanical_preflight"] != "CLEAR_ONLY_NOT_APPROVED":
            problems.append({"word": w, "issue": "BATCH70_PREFLIGHT_FLAGGED"})
        p = pool.get(w.casefold())
        if p and p.get("level") != e["proposed_level"]:
            problems.append({"word": w, "issue": "PROVISIONAL_TIER_DISAGREEMENT", "pool_level": p.get("level")})
        if p and re.search(r"\b(?:surname|given name|capital of|city in|genus|species|trademark)\b", str(p.get("english_definition_draft", "")), re.I):
            problems.append({"word": w, "issue": "SUSPECT_WORDNET_OR_NAMED_ENTITY_SENSE"})
    if level == "ALL":
        assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
        assert re.search(r"entries:\s*\[\s*\]", (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8"))
        historical = read("BATCH72-HISTORICAL-CROSS-LEVEL-HOLDS.json")
        assert historical["wordforms"] == 24 and historical["all_held"] is True
        print("BATCH73 prior historical cross-level holds:", historical["wordforms"], "(not resolved)")
        (ROOT / "batch73-structural-hold-report.json").write_text(json.dumps({
            "batch": 73, "drafts": len(E), "by_level": EXPECTED,
            "independently_approved": 0, "audio_generated": 0,
            "source_verified": 0, "release_approved": 0,
            "editorial_risk_flags": risk_count, "problems": problems,
            "candidate_preflight_source": triage["source"]
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("BATCH73", level, "checked", selected, "risk flags", risk_count, "problems", json.dumps(problems))
    assert not problems, "All 50 drafts remain held; resolve preflight and corpus conflicts"
    print("PASS: STRUCTURAL ONLY. Zero independent approval. No audio, merge or publication.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=[*EXPECTED, "ALL"], required=True)
    main(p.parse_args().level)
