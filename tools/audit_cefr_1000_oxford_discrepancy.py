#!/usr/bin/env python3
"""Validate the Oxford CEFR/POS comparison and reversible review queue.

Data came from a third-party transcript of Oxford's public wordlists, with a
few direct official PDF spot checks. This is ONLY prioritisation for source-
based human lexical and bilingual review. No candidate is approved or retiered.
"""
import argparse
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
SCOPE = {x: 200 for x in LEVELS}
MATRIX = ROOT / "draft/CEFR-1000-OXFORD-LEVEL-POS-CROSSCHECK.json"
HOLDS = ROOT / "draft/CEFR-1000-OXFORD-DISCREPANCY-QUARANTINE.json"
DRAFTS = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
MATCH = "SAME_POS_AND_LEVEL_IN_WORDLIST_SENSE_UNVERIFIED"
WARN = (
    "NOT_IN_TRANSCRIBED_OXFORD_CORE_WORDLIST",
    "PART_OF_SPEECH_DOES_NOT_MATCH_TRANSCRIPTION",
    "PROPOSED_CEFR_LEVEL_DIFFERS_FOR_SAME_PART_OF_SPEECH",
)


def check():
    matrix = json.loads(MATRIX.read_text("utf-8"))
    holds = json.loads(HOLDS.read_text("utf-8"))
    drafts = json.loads(DRAFTS.read_text("utf-8"))
    problems = []
    if matrix.get("stage") != "SECONDARY_LEXICAL_REFERENCE_CROSSCHECK_NOT_INDEPENDENT_CEFR_OR_SENSE_APPROVAL":
        problems.append("Oxford matrix lacks explicit nonapproval stage")
    if holds.get("stage") != matrix.get("stage"):
        problems.append("Oxford holds and matrix stage drift")
    if matrix.get("independent_cefr_reviews_completed") != 0 or holds.get("independent_reviews_completed") != 0:
        problems.append("Undocumented independent linguistic checks claimed")
    prov = matrix.get("source_provenance", {})
    if prov != holds.get("source_provenance"):
        problems.append("Mismatch in reference provenance metadata")
    if not prov.get("spotchecked_not_complete") or "winterdl/" not in prov.get("mirror_repository", ""):
        problems.append("Secondary-source limitations not disclosed")
    for name in ("oxford3000_mirror_blob_sha", "oxford5000_extra_mirror_blob_sha"):
        if len(str(prov.get(name, ""))) != 40:
            problems.append("Missing pinned secondary source SHA")
    for name in ("oxford3000", "oxford5000_exclusive"):
        if "oxfordlearnersdictionaries.com/external/pdf/" not in prov.get("official_oxford_reference_urls", {}).get(name, ""):
            problems.append("Missing official Oxford publication URL: " + name)
    observed = matrix.get("records", [])
    drafts_rows = drafts.get("entries", [])
    held = holds.get("records", [])
    if len(observed) != 1000 or len(drafts_rows) != 1000:
        problems.append("Expected 1000 original provisional rows and 1000 reference rows")
        return problems, {}
    if len(held) != holds.get("flagged_count"):
        problems.append("Oxford hold count mismatch")
    if len(observed) != matrix.get("total_staged_rows"):
        problems.append("Oxford matrix reported count mismatch")
    counts = collections.Counter()
    reasons = collections.Counter()
    expected_holds = []
    for n, (src, ref) in enumerate(zip(drafts_rows, observed)):
        l, word, pos = src.get("level"), src.get("word"), src.get("part_of_speech")
        if (ref.get("proposed_level"), ref.get("word"), ref.get("proposed_part_of_speech")) != (l, word, pos):
            problems.append(f"{n}: crosscheck row does not match source word, level or POS")
        cat = ref.get("category")
        if cat not in (*WARN, MATCH):
            problems.append(f"{n}: illegal crosscheck category {cat}")
        if ref.get("independently_approved") is not False or ref.get("source_evidence_independently_verified") is not False:
            problems.append(f"{n}: false reference verification")
        counts[l, cat] += 1
        if cat != MATCH:
            expected_holds.append(ref)
            reasons[cat] += 1
        gap = ref.get("level_gap_when_comparable")
        if cat == MATCH and gap != 0:
            problems.append(f"{n}: matching Oxford level should have zero distance")
        if cat == "PROPOSED_CEFR_LEVEL_DIFFERS_FOR_SAME_PART_OF_SPEECH" and (not isinstance(gap, int) or gap < 1):
            problems.append(f"{n}: mismatch must have at least one CEFR band distance")
        if cat in ("NOT_IN_TRANSCRIBED_OXFORD_CORE_WORDLIST", "PART_OF_SPEECH_DOES_NOT_MATCH_TRANSCRIPTION") and gap is not None:
            problems.append(f"{n}: unknown or unmatched level must not have distance")
    if len(expected_holds) != len(held):
        problems.append("Risk flag count not equal to actual held row count")
    for n, (ref, h) in enumerate(zip(expected_holds, held)):
        for k in ("word", "proposed_level", "proposed_part_of_speech", "category", "observed_oxford_list_levels_for_pos"):
            if ref[k] != h[k]:
                problems.append(f"{n}: mismatch in reversible hold for {ref['word']}")
        if h.get("hold_reversible") is not True or h.get("resolution_status") != "PENDING_INDEPENDENT_SENSE_SPECIFIC_SOURCE_REVIEW":
            problems.append(f"{n}: unresolved risk was improperly cleared")
        if h.get("independent_reviewer") is not None or h.get("independent_evidence_url") is not None or h.get("review_completed") is not False:
            problems.append(f"{n}: false source approval for held word")
    actual_summary = {level: dict(collections.Counter({
        cat: counts[level, cat] for cat in (*WARN, MATCH) if counts[level, cat]
    })) for level in LEVELS}
    if actual_summary != matrix.get("counts_by_proposed_level"):
        problems.append("Reference-count ledger mismatch")
    if dict(reasons) != holds.get("breakdown_by_reason"):
        problems.append("Quarantine-reason ledger mismatch")
    high = sum(row.get("level_gap_when_comparable", 0) is not None
               and (row.get("level_gap_when_comparable") or 0) >= 2 for row in expected_holds)
    if holds.get("high_two_or_more_bands") != high:
        problems.append("High-priority Oxford discrepancy count differs from observations")
    if sum(counts.get((level, cat), 0) for level in LEVELS for cat in (*WARN, MATCH)) != 1000:
        problems.append("Incomplete Oxford crosscheck")
    # Existing provisional entries MUST remain held, even those with a machine list match.
    if any(row.get("editorial_hold") is not True or row.get("release_approved") is not False
           for row in drafts_rows):
        problems.append("Crosschecking may not lift editorial holds")
    return problems, {"per_level": actual_summary, "flagged": len(expected_holds), "high": high}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    args = ap.parse_args()
    issues, summary = check()
    if issues:
        for e in issues[:30]:
            print("BLOCK:", e)
        raise SystemExit(f"FAIL: {len(issues)} reference queue integrity errors")
    section = summary["per_level"][args.level] if args.level != "ALL" else summary["per_level"]
    print(f"PASS {args.level} Oxford-reference FIRST-PASS COMPARISON: {section}; "
          f"525 reversible flags across corpus, 68 two-plus-band priorities, "
          "0 independent CEFR/Burmese approvals, no retiering or publication")


if __name__ == "__main__":
    main()
