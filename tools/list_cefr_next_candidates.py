#!/usr/bin/env python3
"""Staging-only draft candidate preview. No CEFR or linguistic approvals."""
import argparse
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A2", "B1", "B2", "C1")
def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=85)
    args = parser.parse_args()
    pool = read("draft/UNVERIFIED_CEFR_CANDIDATES.json")
    assert pool["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert len(pool["entries"]) == 5000
    drafted = {}
    for path in ["draft/A2-C1-EDITORIAL-STARTER.json"] + [
        str(p.relative_to(ROOT)) for p in sorted((ROOT / "draft").glob("A2-C1-EDITORIAL-BATCH*.json"))
    ]:
        for row in read(path)["entries"]:
            if row["word"] in drafted:
                assert drafted[row["word"]]["level"] == row["level"], row["word"]
            drafted[row["word"]] = row
    quarantine = set()
    for path in [ROOT / "draft/A2-C1-CANDIDATE-QUARANTINE.json"] + sorted(
        (ROOT / "draft").glob("A2-C1-QUARANTINE-BATCH*.json")
    ):
        for row in read(path.relative_to(ROOT))["records"]:
            quarantine.add(row["word"])
    suspicious = re.compile(r"(?i)\b(?:person|surname|given name|proper noun|capital of|city in|state of|king of|saint|genus|species|abbreviation|acronym|initialism|trademark|brand name)\b")
    for level in LEVELS:
        rows = [r for r in pool["entries"] if r["level"] == level
                and r["word"] not in drafted and r["word"] not in quarantine
                and re.fullmatch(r"[a-z]{3,}", r["word"])]
        clear = [r for r in rows if not suspicious.search(r.get("english_definition_draft", ""))]
        print(f"LEVEL={level} drafted={sum(x['level']==level for x in drafted.values())} "
              f"remaining_unheld={len(rows)} candidate_clue_not_flagged={len(clear)}")
        for r in clear[:args.limit]:
            clue = r.get("english_definition_draft", "").replace("\n", " ")[:95]
            print(f"CANDIDATE|{level}|{r['word']}|{r.get('part_of_speech','')}|{clue}")
    print("All candidate tiers, POS and WordNet clues remain UNVERIFIED; no deploy.")

if __name__ == "__main__":
    main()
