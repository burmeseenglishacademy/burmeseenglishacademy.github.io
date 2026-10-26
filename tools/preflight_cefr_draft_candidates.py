#!/usr/bin/env python3
"""Preflight unique bilingual draft headwords. NEVER grants linguistic, CEFR or audio approval.

The 5,000-item seed pool is an unverified candidate list, NOT a completed draft
corpus. A pool-only match is informational; prior AUTHORED drafts are collisions.
"""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A2", "B1", "B2", "C1")
PROPER_CLUE = re.compile(
    r"\b(?:surname|given name|capital of|city in|state in|born in|"
    r"american (?:actor|writer|politician)|genus|species|trademark)\b",
    re.IGNORECASE,
)
NAMED_WORDS = {"singapore", "myanmar", "london", "tokyo", "amazon", "google", "microsoft"}

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def build_index():
    pool_file = ROOT / "draft/UNVERIFIED_CEFR_CANDIDATES.json"
    pool_data = load(pool_file)
    assert pool_data["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert len(pool_data["entries"]) == 5000
    pool = {row["word"].casefold(): row for row in pool_data["entries"]}
    draft_dir = ROOT / "draft"
    paths = [
        draft_dir / "A1-EDITORIAL-STARTER.json",
        *sorted(draft_dir.glob("A1-EXPANSION-BATCH*.json")),
        draft_dir / "A2-C1-EDITORIAL-STARTER.json",
        *sorted(draft_dir.glob("A2-C1-EDITORIAL-BATCH*.json")),
        *sorted(draft_dir.glob("A2-C1-RETIER-EDITORIAL-BATCH*.json")),
        *sorted(draft_dir.glob("A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json")),
    ]
    prior = collections.defaultdict(list)
    held = set()
    for path in paths:
        for row in load(path)["entries"]:
            word = row["word"].casefold()
            prior[word].append(path.name)
            if row.get("editorial_hold"):
                held.add(word)
    return pool, prior, held

def classify(word, proposed_level, pool, prior, held):
    word = word.casefold().strip()
    risks = []
    if not re.fullmatch(r"[a-z]{3,}", word):
        risks.append("HEADWORD_FORM_REVIEW")
    if word in NAMED_WORDS:
        risks.append("NAMED_ENTITY_QUARANTINE")
    if word in prior:
        risks.append("ALREADY_IN_AUTHORED_DRAFT")
    if word in held:
        risks.append("EXISTING_EDITORIAL_HOLD")
    row = pool.get(word)
    if row is not None:
        if proposed_level and row.get("level") != proposed_level:
            risks.append("UNVERIFIED_POOL_TIER_DISAGREEMENT")
        if PROPER_CLUE.search(str(row.get("english_definition_draft", ""))):
            risks.append("SUSPECT_WORDNET_CANDIDATE_SENSE")
    if proposed_level and proposed_level not in LEVELS:
        risks.append("INVALID_PROPOSED_LEVEL")
    return {
        "word": word, "proposed_level": proposed_level,
        "in_unverified_pool_not_by_itself_duplicate": row is not None,
        "pool_provisional_level": row.get("level") if row else None,
        "previous_authored_files": prior.get(word, []),
        "risk_flags": risks,
        "preflight_clear_only_not_approved": not risks,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=Path, help="UTF-8 newline list: LEVEL|word or word")
    parser.add_argument("--words", help="Comma-separated candidate headwords")
    parser.add_argument("--level", choices=LEVELS, help="Proposed tier for --words")
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    parser.add_argument("--self-test", action="store_true", help="Assert collision semantics")
    args = parser.parse_args()
    pool, prior, held = build_index()
    if args.self_test:
        known = next(iter(prior))
        assert "ALREADY_IN_AUTHORED_DRAFT" in classify(known, None, pool, prior, held)["risk_flags"]
        pool_only = next((w for w in pool if w not in prior), None)
        if pool_only:
            r = classify(pool_only, None, pool, prior, held)
            assert r["in_unverified_pool_not_by_itself_duplicate"]
            assert "ALREADY_IN_AUTHORED_DRAFT" not in r["risk_flags"]
        assert classify("singapore", "A2", pool, prior, held)["risk_flags"]
        print("PASS: preflight distinguishes unverified pool from authored drafts; never approves content")
        return
    candidates = []
    if args.file:
        for line in args.file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|")
            if len(parts) == 2:
                level, word = (x.strip() for x in parts)
            elif len(parts) == 1:
                level, word = args.level, parts[0].strip()
            else:
                raise ValueError("Expected LEVEL|word or word, got " + line)
            candidates.append((level, word))
    if args.words:
        candidates.extend((args.level, w.strip()) for w in args.words.split(",") if w.strip())
    rows = [classify(word, level, pool, prior, held) for level, word in candidates]
    summary = {
        "stage": "PREFLIGHT_ONLY_NOT_CEFR_OR_LINGUISTIC_APPROVAL",
        "unverified_seed_pool": len(pool),
        "authored_distinct_wordforms": len(prior),
        "input_candidates": len(rows),
        "preflight_clear": sum(r["preflight_clear_only_not_approved"] for r in rows),
        "requires_triage": sum(not r["preflight_clear_only_not_approved"] for r in rows),
    }
    if args.json:
        print(json.dumps({"summary": summary, "candidates": rows}, ensure_ascii=False, indent=2))
    else:
        print("PREFLIGHT SUMMARY", json.dumps(summary, sort_keys=True))
        for row in rows:
            print("CANDIDATE|{proposed_level}|{word}|{risk_flags}|pool_only_is_not_duplicate={in_unverified_pool_not_by_itself_duplicate}".format(**row))
        print("NO LINGUISTIC APPROVAL / NO AUDIO / NO DEPLOY")

if __name__ == "__main__":
    main()
