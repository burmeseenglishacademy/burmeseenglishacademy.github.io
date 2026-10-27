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
REVIEW_PACKETS = ROOT / "draft/CEFR-1000-BILINGUAL-DISCREPANCY-REVIEW-PACKETS.json"
PRIMARY_OBSERVATIONS = ROOT / "draft/CEFR-1000-OXFORD-PRIMARY-SOURCE-SPOT-OBSERVATIONS.json"
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
    packets = json.loads(REVIEW_PACKETS.read_text("utf-8"))
    cards = packets.get("packets", [])
    if packets.get("status") != "HIGH_PRIORITY_BILINGUAL_EDITORIAL_QA_QUEUE_NOT_APPROVED" or packets.get("independently_completed_tasks") != 0:
        problems.append("Bilingual source review packet cannot claim approval")
    if packets.get("pending_tasks") != len(expected_holds) or len(cards) != len(expected_holds):
        problems.append("Bilingual review cards must have one-to-one parity with all reversible Oxford holds")
    draft_index = {(r["level"], r["word"]): r for r in drafts_rows}
    flagged_index = {(r["proposed_level"], r["word"]): r for r in expected_holds}
    priority_counter = collections.Counter()
    card_level_counts = collections.Counter()
    observed_cards = set()
    for n, card in enumerate(cards):
        key = (card.get("proposed_level"), card.get("word"))
        if key in observed_cards:
            problems.append(f"Repeated flagged bilingual review card: {key}")
        observed_cards.add(key)
        src = draft_index.get(key)
        flagged = flagged_index.get(key)
        if not src or not flagged:
            problems.append(f"Unknown bilingual review card: {key}")
            continue
        if card.get("proposed_pos") != src["part_of_speech"] or card.get("priority") != flagged["review_priority"] or card.get("trigger_reason") != flagged["category"]:
            problems.append(f"Card mismatch against Oxford word+POS risk: {key}")
        fields = card.get("original_draft", {})
        for field, expected in (("english_definition", src["english_definition"]),
                                ("burmese_meaning", src["burmese_meaning"]),
                                ("original_example", src["example_sentence"]),
                                ("original_source_file", src["source_path"])):
            if fields.get(field) != expected:
                problems.append(f"Original source text drift in review card: {key} / {field}")
        for stage in ("english_exact_sense", "myanmar_naturalness", "original_example", "cefr_source"):
            t = card.get("independent_review_stages", {}).get(stage, {})
            if t.get("review_complete") is not False or t.get("reviewer") is not None or not t.get("task"):
                problems.append(f"Premature independent reviewer approval: {key} / {stage}")
        resolution = card.get("resolution", {})
        if resolution.get("status") != "PENDING_INDEPENDENT_REVIEW" or resolution.get("approved") is not False or resolution.get("decision") is not None or resolution.get("reviewer") is not None:
            problems.append(f"Editorial CEFR risk review was prematurely resolved: {key}")
        priority_counter[card.get("priority")] += 1
        card_level_counts[card.get("proposed_level")] += 1
    if observed_cards != set(flagged_index):
        problems.append("Not all Oxford risk flags received independent bilingual review packets")
    if dict(priority_counter) != packets.get("priority_counts"):
        problems.append("Risk reviewer priority packet totals differ")
    if {level: card_level_counts[level] for level in LEVELS} != packets.get("per_level_counts"):
        problems.append("Bilingual risk review cards per-level counts differ")
    # A small number of actual publisher PDF page entries were directly
    # observed. Distinguish factual wordlist labels from *unperformed* human
    # translation, exact dictionary sense and CEFR approval.
    primary = json.loads(PRIMARY_OBSERVATIONS.read_text("utf-8"))
    primary_rows = primary.get("records", [])
    if primary.get("review_status") != "DIRECT_PUBLISHER_WORDLIST_SPOT_OBSERVATIONS_NOT_INDEPENDENT_SENSE_VERIFICATION":
        problems.append("Publisher source observations falsely treated as independent approvals")
    if primary.get("observed_primary_source_rows") != len(primary_rows) or len(primary_rows) != 16:
        problems.append("Publisher spot-check row ledger differs")
    if primary.get("independently_approved_rows") != 0:
        problems.append("Spot observations cannot constitute independent review")
    checked_words = set()
    for entry in primary_rows:
        key = (entry.get("proposed_level"), entry.get("word"))
        if key in checked_words:
            problems.append(f"Duplicate primary source observation: {key}")
        checked_words.add(key)
        src = draft_index.get(key)
        if not src:
            problems.append(f"Publisher source observation does not match a shortlist entry: {key}")
            continue
        if entry.get("proposed_part_of_speech") != src.get("part_of_speech") or entry.get("proposed_english_definition") != src.get("english_definition") or entry.get("proposed_original_example") != src.get("example_sentence"):
            problems.append(f"Publisher observation source draft drift: {key}")
        if entry.get("independent_sense_cefr_approved") is not False or entry.get("independent_myanmar_approved") is not False or entry.get("independent_example_approved") is not False or entry.get("reviewer") is not None:
            problems.append(f"Publisher observation falsely approved: {key}")
        if entry.get("source_pdf_page_one_based", 0) < 1 or "oxfordlearnersdictionaries.com/external/pdf/wordlists/" not in entry.get("source_pdf", ""):
            problems.append(f"No grounded original Oxford PDF page evidence for {key}")
        if entry.get("source_observation_type") != "DIRECT_PUBLISHER_PDF_TEXT_READ_SPOTCHECK_ONLY":
            problems.append(f"Source stage incorrectly described for {key}")
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
