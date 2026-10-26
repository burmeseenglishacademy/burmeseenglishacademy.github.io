#!/usr/bin/env python3
"""Batch68 quarantine-first structural audit. Never grants linguistic, CEFR or audio approval."""
import argparse, collections, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "draft"
LEVELS = ("A2", "B1", "B2", "C1")
COUNTS = {"A2": 12, "B1": 12, "B2": 12, "C1": 24}
def load(path):
    return json.loads(path.read_text(encoding="utf-8"))
def prior_authored():
    paths = [
        DRAFT / "A1-EDITORIAL-STARTER.json",
        *sorted(DRAFT.glob("A1-EXPANSION-BATCH*.json")),
        DRAFT / "A2-C1-EDITORIAL-STARTER.json",
        *sorted(DRAFT.glob("A2-C1-EDITORIAL-BATCH*.json")),
        *sorted(DRAFT.glob("A2-C1-RETIER-EDITORIAL-BATCH*.json")),
        *[p for p in sorted(DRAFT.glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json")) if "BATCH68" not in p.name],
    ]
    found = collections.defaultdict(list)
    for p in paths:
        for row in load(p)["entries"]:
            found[row["word"].casefold()].append(p.name)
    return found
def audit(level):
    d = load(DRAFT / "A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH68.json")
    t = load(DRAFT / "A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH68.json")
    q = load(DRAFT / "A2-C1-SOURCE-RECOVERY-QUARANTINE-BATCH68.json")
    E, T, Q = d["entries"], t["entries"], q["records"]
    assert d["release_status"] == "UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH"
    assert t["release_status"] == "UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH"
    assert t["source_pages_not_yet_checked"] is True
    assert q["release_status"] == "REVERSIBLE_EDITORIAL_QUARANTINE_NOT_APPROVED_DO_NOT_PUBLISH"
    assert len(E) == len(T) == len(Q) == 60
    assert len({e["word"].casefold() for e in E}) == 60
    assert dict(collections.Counter(e["proposed_level"] for e in E)) == d["counts_by_proposed_level"] == COUNTS
    by_task = {x["word"]: x for x in T}
    by_hold = {x["word"]: x for x in Q}
    assert set(by_task) == set(by_hold) == {x["word"] for x in E}
    prior = prior_authored()
    pool = {x["word"].casefold(): x for x in load(DRAFT / "UNVERIFIED_CEFR_CANDIDATES.json")["entries"]}
    named = {"amazon", "google", "microsoft", "singapore", "myanmar", "london", "oxford", "tokyo"}
    collisions, tier_disagreements, suspicious_pool_senses = [], [], []
    for e in E:
        w = e["word"]
        if level != "ALL" and e["proposed_level"] != level:
            continue
        assert re.fullmatch(r"[a-z]{4,}", w), w
        assert e["part_of_speech"] in ("noun", "verb", "adjective", "adverb"), w
        assert len(e["english_definition"]) >= 30, w
        assert re.search(r"[\u1000-\u109f]", e["burmese_meaning"]), w
        sentence = e["example_sentence"]
        assert len(sentence) >= 35 and sentence[0].isupper() and sentence[-1] in ".?!", w
        assert re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", sentence.casefold()), w
        assert e["editorial_hold"] is True
        assert e["status"] == "REVERSIBLE_QUARANTINE_PENDING_PREFLIGHT_AND_SENSE_REVIEW"
        assert e["editorial_hold_reasons"] == ["CROSS_CORPUS_PREFLIGHT_RESULT_NOT_YET_OBSERVED", "SENSE_SPECIFIC_CEFR_SOURCE_NOT_YET_OBSERVED"]
        assert all(e[k] is False for k in ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation","release_approved"))
        assert all(e[k] == "" for k in ("source_english","source_burmese","source_level"))
        assert w not in named, w
        x = by_task[w]
        assert x["editorial_hold"] is True and x["release_approved"] is False
        assert x["editorial_hold_reasons"] == e["editorial_hold_reasons"]
        for key in ("english_definition_review","burmese_review","example_review","cefr_review"):
            assert x[key]["completed"] is False and x[key]["reviewer"] is None and x[key]["observed_evidence"] is None
        assert x["english_definition_review"]["source_observed"] is False
        assert all(x["audio_review"][k] is False for k in ("generated","real_listening","real_device_test"))
        hold = by_hold[w]
        assert hold["reason_codes"] == e["editorial_hold_reasons"]
        assert hold["proposed_level"] == e["proposed_level"]
        assert hold["hold_reversible"] is True and hold["independently_approved"] is False and hold["release_approved"] is False
        if w in prior:
            collisions.append({"word": w, "earlier_files": prior[w]})
        p = pool.get(w)
        if p and p.get("level") != e["proposed_level"]:
            tier_disagreements.append({"word": w, "pool_level": p.get("level"), "draft_level": e["proposed_level"]})
        if p and re.search(r"\\b(?:surname|given name|capital of|city in|genus|species|trademark)\\b", str(p.get("english_definition_draft", "")), re.I):
            suspicious_pool_senses.append(w)
    if level == "ALL":
        bank = (ROOT / "cefr-vocabulary-data.js").read_text(encoding="utf-8")
        assert "UNVERIFIED_DRAFT_DO_NOT_PUBLISH" in bank
        assert re.search(r"entries:\\s*\\[\\s*\\]", bank)
        out = {"batch":68,"stage":"STRUCTURAL_AUDIT_ONLY","drafts_written":60,"written_by_level":COUNTS,"independently_approved":0,"eligible_new_entries":0,"reversible_holds":60,"prior_authored_collisions":collisions,"unverified_pool_tier_disagreements":tier_disagreements,"suspect_wordnet_pool_senses":suspicious_pool_senses,"source_pages_observed":0,"audio_generated":0,"real_listening_validated":0,"production_deployed":False}
        (ROOT / "batch68-triage-results.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\\n",encoding="utf-8")
        print("BATCH68 TRIAGE "+json.dumps(out,ensure_ascii=False))
    else:
        print("BATCH68",level,"drafts",COUNTS[level],"held",COUNTS[level],"independently approved 0")
    print("PASS: structural consistency only; all 60 held, no publication")
if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=[*LEVELS,"ALL"],required=True)
    audit(p.parse_args().level)
