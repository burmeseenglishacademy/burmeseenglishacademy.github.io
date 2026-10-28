#!/usr/bin/env python3
"""Fail-closed staging integrity check for twelve UNAPPROVED A2 bilingual rewrite candidates.

This does not evaluate fluency or approve any rewrite; independent human
English/Myanmar/example/CEFR review remains required.
"""
import argparse
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REWRITES = ROOT / "draft/CEFR-1000-A2-THIRD-BILINGUAL-REWRITE-CANDIDATES-2026-10-29.json"
SOURCE = ROOT / "draft/CEFR-1000-OXFORD-A2-THIRD-TWENTYFOUR-2026-10-29.json"
EXPECTED = ("power", "side", "nothing", "whole", "less", "business",
            "however", "public", "fact", "half", "course", "information")
SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"

def check(ok, message):
    if not ok:
        raise ValueError(message)

def audit(data, source):
    check(data.get("schema") == 1 and data.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY",
          "Scope invalid")
    check(data.get("status") == "BILINGUAL_REWRITE_PROPOSALS_NOT_INDEPENDENTLY_VERIFIED",
          "False editorial status")
    check(data.get("shortlist_blob_sha") == SHA == source.get("shortlist_blob_sha"),
          "Shortlist provenance drift")
    check(data.get("candidate_count") == 12 and data.get("independent_approvals") == 0,
          "False count or approval")
    check(data.get("source_evidence_packet") ==
          "draft/CEFR-1000-OXFORD-A2-THIRD-TWENTYFOUR-2026-10-29.json",
          "Source evidence binding drift")
    check("not replacements" in data.get("policy", ""), "Non-production policy lost")
    candidates = data.get("candidates")
    check(isinstance(candidates, list) and len(candidates) == 12,
          "Candidate count invalid")
    lookup = {r["word"]: r for r in source.get("records", [])}
    for word, row in zip(EXPECTED, candidates):
        check(row.get("word") == word and row.get("provisional_level") == "A2",
              f"{word}: identity/level")
        ref = lookup[word]
        check(row.get("part_of_speech") == ref.get("part_of_speech"),
              f"{word}: POS")
        check(row.get("shortlist_source") == ref.get("shortlist_provenance")
              and row.get("original_snapshot") == ref.get("shortlist_snapshot"),
              f"{word}: original content/provenance drift")
        check(row.get("oxford_word_pos_level") ==
              ref["publisher_source"]["source_cefr_level"],
              f"{word}: Oxford level drift")
        check(row.get("source_url") == ref["publisher_source"]["url"]
              and row.get("source_observed_on") == "2026-10-29",
              f"{word}: source/date drift")
        p = row.get("proposal")
        check(isinstance(p, dict) and set(p) ==
              {"english_definition", "burmese_meaning", "example_sentence"},
              f"{word}: proposal shape")
        check(all(isinstance(v, str) and len(v.strip()) >= 12 for v in p.values()),
              f"{word}: empty/placeholder rewrite")
        check(any("\u1000" <= ch <= "\u109f" for ch in p["burmese_meaning"]),
              f"{word}: missing Myanmar script")
        check(re.search(r"\\b" + re.escape(word) + r"\\b",
                        p["example_sentence"], re.I) is not None,
              f"{word}: example missing headword")
        check(p["example_sentence"].endswith((".", "!", "?")),
              f"{word}: example punctuation")
        check(isinstance(row.get("rationale"), str)
              and len(row["rationale"].strip()) >= 70,
              f"{word}: missing editorial rationale")
        check(row.get("editorial_status") ==
              "UNREVIEWED_CANDIDATE_NOT_FOR_PRODUCTION"
              and row.get("independent_english_review") is False
              and row.get("independent_myanmar_review") is False
              and row.get("independent_example_review") is False
              and row.get("independent_cefr_review") is False
              and row.get("release_approved") is False,
              f"{word}: fabricated approval")
    return len(candidates)

def self_test(data, source):
    count = 0
    mutations = []
    for i in range(12):
        def change(d, idx=i):
            d["candidates"][idx]["original_snapshot"]["english_definition"] = "Forged."
        mutations.append(change)
    mutations.extend([
        lambda d: d.update(independent_approvals=12),
        lambda d: d.update(candidate_count=11),
        lambda d: d.update(status="APPROVED"),
        lambda d: d["candidates"][0].update(release_approved=True),
        lambda d: d["candidates"][1].update(independent_myanmar_review=True),
        lambda d: d["candidates"][2]["proposal"].update(myanmar_meaning="English only"),
        lambda d: d["candidates"][3]["proposal"].update(example_sentence="Unrelated example."),
        lambda d: d["candidates"][4].update(oxford_word_pos_level="C1"),
        lambda d: d["candidates"][5].update(source_url="https://example.com/fake"),
        lambda d: d["candidates"][6].update(editorial_status="PUBLISHED"),
        lambda d: d["candidates"].reverse(),
        lambda d: d.update(shortlist_blob_sha="0"*40),
    ])
    for i, change in enumerate(mutations):
        p = copy.deepcopy(data)
        change(p)
        try:
            audit(p, source)
        except ValueError:
            count += 1
        else:
            raise AssertionError(f"Invalid bilingual candidate mutation {i} passed")
    return count

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=("A1","A2","B1","B2","C1","ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    data = json.loads(REWRITES.read_text(encoding="utf-8"))
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    n = audit(data, source)
    print(f"PASS {n} A2 bilingual rewrite candidates structurally bound; 0 approved; {args.level}; NO release")
    if args.self_test:
        count = self_test(data, source)
        print(f"PASS {count}/{count} forged rewrite, provenance and false-approval mutations rejected")

if __name__ == "__main__":
    main()
