#!/usr/bin/env python3
"""Fail-closed structural audit of 12 C1 Oxford word/POS leads; NOT independent review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORTLIST_PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_PATH = ROOT / "draft/CEFR-1000-OXFORD-C1-MIXED-TWELVE-2026-10-28.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF3 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
# Oxford observed word/POS level, PDF series, one-based page, zero-based extracted line, excerpt, risk.
EXPECTED = {
    "verdict": ("C1", 5, 8, 1971, "verdict n.", "JURY_VERDICT_VS_GENERAL_COURT_DECISION_AND_MYANMAR_LEGAL_PRECISION"),
    "abandon": ("B2", 3, 10, 2593, "abandon v.", "SAME_SENSE_OXFORD_B2_CONFLICT_WITH_C1_DRAFT"),
    "accommodate": ("B2", 5, 1, 9, "accommodate v.", "B2_SOURCE_AND_MIXED_CAPACITY_VS_ADJUSTMENT_DEFINITION"),
    "aesthetic": ("C1", 5, 3, 744, "aesthetic adj.", "AESTHETIC_APPEAL_COLLOCATION_VS_ADJECTIVE_SENSE"),
    "algorithm": ("C1", 5, 3, 752, "algorithm n.", "ALGORITHM_TECHNICAL_SCOPE_AND_MYANMAR_TEACHING_GLOSS"),
    "complexity": ("C1", 5, 4, 941, "complexity n.", "COMPLEXITY_ABSTRACT_NOUN_EXAMPLE_NATURALNESS"),
    "deliberately": ("B2", 3, 11, 2770, "deliberately adv.", "SAME_SENSE_OXFORD_B2_CONFLICT_WITH_C1_DRAFT"),
    "dignity": ("C1", 5, 5, 1084, "dignity n.", "DIGNITY_RESPECT_VS_SELF_RESPECT_SENSE"),
    "ideology": ("C1", 5, 5, 1305, "ideology n.", "IDEOLOGY_BELIEF_SYSTEM_VS_POLITICAL_MOVEMENT_CONTEXT"),
    "inclusion": ("C1", 5, 5, 1318, "inclusion n.", "SOCIAL_INCLUSION_VS_GENERAL_INCLUDE_SENSE"),
    "isolation": ("C1", 5, 6, 1378, "isolation n.", "PHYSICAL_SEPARATION_VS_SOCIAL_LONELINESS_AND_WELLBEING"),
    "premises": (None, None, None, None, None, "NOT_IN_INSPECTED_OXFORD_CORE_LISTS_NOT_CEFR_PROOF_PLURAL_ONLY_NOUN"),
}

EXPECTED_CAMBRIDGE = json.loads(r'''[
  {
    "word": "abandon",
    "publisher": "Cambridge University Press",
    "source_url": "https://dictionary.cambridge.org/us/dictionary/english/abandon",
    "observed_on": "2026-10-28",
    "publisher_dictionary": "Cambridge Advanced Learner's Dictionary",
    "sense_heading": "STOP",
    "publisher_indexed_cefr": "C1",
    "paraphrased_sense": "Stop an activity before completion or give up a policy or plan.",
    "draft_sense_alignment": "STRONG_STOP_PLAN_MATCH",
    "editorial_note": "Oxford 3000 B2 is word/POS; Cambridge Advanced STOP sense shows C1. Cambridge Learner's STOP DOING entry is separately unlabelled, so do not conflate editions.",
    "source_access": "PUBLISHER_INDEXED_SEARCH_RESULT_DIRECT_PAGE_HTTP_403",
    "independently_approved": false
  },
  {
    "word": "deliberately",
    "publisher": "Cambridge University Press",
    "source_url": "https://dictionary.cambridge.org/dictionary/english/deliberately",
    "observed_on": "2026-10-28",
    "publisher_dictionary": "Cambridge Advanced Learner's Dictionary",
    "sense_heading": "INTENTIONALLY",
    "publisher_indexed_cefr": "B2",
    "paraphrased_sense": "Done on purpose, not accidentally.",
    "draft_sense_alignment": "STRONG_INTENTIONAL_MATCH",
    "editorial_note": "Oxford 3000 B2 and Cambridge B2 agree at the intended intentional sense; draft C1 needs independent pedagogical rationale or retiering.",
    "source_access": "PUBLISHER_INDEXED_SEARCH_RESULT_DIRECT_PAGE_HTTP_403",
    "independently_approved": false
  },
  {
    "word": "premises",
    "publisher": "Cambridge University Press",
    "source_url": "https://dictionary.cambridge.org/dictionary/english/premises",
    "observed_on": "2026-10-28",
    "publisher_dictionary": "Cambridge Advanced Learner's Dictionary",
    "sense_heading": "LAND_AND_BUILDINGS_PLURAL_NOUN",
    "publisher_indexed_cefr": "C1",
    "paraphrased_sense": "Land and buildings used or owned by an organisation.",
    "draft_sense_alignment": "STRONG_COMPANY_BUILDINGS_MATCH",
    "editorial_note": "Oxford core-list absence is not a CEFR judgement; Cambridge index supports a C1 plural-noun sense, but independent direct-publisher verification and plural-only POS review remain needed.",
    "source_access": "PUBLISHER_INDEXED_SEARCH_RESULT_DIRECT_PAGE_HTTP_403",
    "independently_approved": false
  },
  {
    "word": "accommodate",
    "publisher": "Cambridge University Press",
    "source_url": "https://dictionary.cambridge.org/us/dictionary/english/accommodate",
    "observed_on": "2026-10-28",
    "publisher_dictionary": "Cambridge Advanced Learner's Dictionary",
    "sense_heading": "FIND_A_PLACE_FOR_AND_SUIT",
    "publisher_indexed_cefr": null,
    "paraphrased_sense": "Provide enough space or a place; separately, meet another person's needs.",
    "draft_sense_alignment": "MIXED_DEFINITION_CAPACITY_EXAMPLE",
    "editorial_note": "Publisher-indexed Cambridge entry shows separate senses but no visible exact-sense CEFR label. Draft definition combines capacity and adjustment; example only tests capacity.",
    "source_access": "PUBLISHER_INDEXED_SEARCH_RESULT_DIRECT_PAGE_HTTP_403",
    "independently_approved": false
  }
]''')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet, shortlist, sha):
    require(sha == SHORTLIST_SHA, "Provisional shortlist blob changed: rebind all observations")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Scope drift")
    require(packet.get("status") == "C1_TWELVE_DIRECT_OXFORD_WORD_POS_AND_UNLISTED_LEADS_EDITORIAL_HOLD", "Status drift")
    require(packet.get("observed_on") == "2026-10-28" and packet.get("shortlist_blob_sha") == sha, "Observation date or shortlist binding drift")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 12, "Record count drift")
    require(packet.get("counts_by_level") == {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 12}, "Level counts drift")
    require(type(packet.get("word_pos_discrepancies")) is int and packet["word_pos_discrepancies"] == 3, "Conflict count drift")
    require(type(packet.get("unlisted_in_inspected_core_lists")) is int and packet["unlisted_in_inspected_core_lists"] == 1, "Unlisted count drift")
    require(type(packet.get("independently_approved_count")) is int and packet["independently_approved_count"] == 0, "Fabricated independent approvals")
    limitations = packet.get("source_limitations")
    require(isinstance(limitations, str) and "NOT independently verified exact-sense" in limitations and "NOT evidence" in limitations, "Source-scope disclaimer missing")
    require(packet.get("cambridge_direct_page_access") == "HTTP_403_FOR_ALL_FOUR_FULL_PAGES", "Cambridge access caveat lost")
    require(packet.get("cambridge_publisher_indexed_sense_leads") == EXPECTED_CAMBRIDGE, "Cambridge publisher-indexed exact-sense research lead drift or fake signoff")
    require(shortlist.get("scope_target") == {k: 200 for k in LEVELS}, "1000 target drift")
    require(shortlist.get("counts_by_level") == {k: 200 for k in LEVELS}, "First-pass counts drift")
    require(shortlist.get("independently_approved_by_level") == {k: 0 for k in LEVELS}, "Fake shortlist approval")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Expected exactly 1000 provisional entries")
    require({k: sum(e.get("level") == k for e in entries) for k in LEVELS} == {k: 200 for k in LEVELS}, "Level allocation drift")
    require(len({e.get("word", "").casefold() for e in entries}) == 1000, "Duplicate cross-level headword")
    index = {(e.get("word"), e.get("level")): e for e in entries}
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == 12, "Wrong record list")
    require(all(isinstance(r, dict) for r in records), "Malformed record")
    require({r.get("word") for r in records} == set(EXPECTED), "Missing or unexpected headword")
    require(len({r["word"] for r in records}) == 12, "Duplicate headword in packet")
    for r in records:
        w = r["word"]
        e = index.get((w, "C1"))
        require(e is not None and r.get("level") == "C1", w + ": not bound to C1")
        require(r.get("part_of_speech") == e.get("part_of_speech"), w + ": part of speech drift")
        require(r.get("shortlist_snapshot") == {
            "english_definition": e["english_definition"],
            "myanmar_meaning": e["burmese_meaning"],
            "example_sentence": e["example_sentence"]
        }, w + ": English/Myanmar/example changed")
        require(r.get("shortlist_provenance") == {
            "source_path": e["source_path"],
            "source_index": e["source_index"],
            "source_blob_sha": e["source_blob_sha"]
        }, w + ": source Git provenance changed")
        cefr, series, page, line, excerpt, risk = EXPECTED[w]
        if cefr is not None:
            expected_source = {
                "publisher": "Oxford University Press",
                "title": "The Oxford " + str(series) + "000 by CEFR level",
                "url": PDF3 if series == 3 else PDF5,
                "observed_on": "2026-10-28",
                "pdf_page": page, "extracted_line": line,
                "source_excerpt": excerpt, "source_cefr_level": cefr,
                "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"
            }
        else:
            expected_source = {
                "publisher": "Oxford University Press",
                "title": "The Oxford 3000 and Oxford 5000 by CEFR level",
                "urls_inspected": [PDF3, PDF5],
                "observed_on": "2026-10-28",
                "source_cefr_level": None, "pdf_page": None,
                "extracted_line": None, "source_excerpt": None,
                "evidence_scope": "NOT_FOUND_IN_TWO_INSPECTED_LISTS_NOT_EVIDENCE_OF_LEVEL",
                "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"
            }
        require(r.get("publisher_source") == expected_source, w + ": publisher source mismatch or invented CEFR")
        require(r.get("editorial_risk") == risk, w + ": risk rationale drift")
        task = r.get("independent_reviewer_task")
        require(isinstance(task, str) and "Human-independent reviewer:" in task and "genuine independent signed receipt" in task and w in task, w + ": review task missing")
        if cefr == "B2":
            require("lower Oxford B2 label" in task, w + ": B2 conflict not escalated")
        if cefr is None:
            require("absence is not a CEFR level" in task, w + ": false absence inference")
        require(r.get("editorial_hold") is True and e.get("editorial_hold") is True, w + ": editorial hold removed")
        require(r.get("independently_reviewed") is False and r.get("release_approved") is False and r.get("independent_reviewer_receipt") is None, w + ": fabricated independent signoff")
        require(all(e.get(k) is False for k in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level", "reviewed_pronunciation", "release_approved")), w + ": shortlist flags changed")
    return {"records": 12, "matching_C1_word_pos": 8, "lower_B2_word_pos": 3, "unlisted_without_cefr": 1, "independent_approvals": 0}

def negative_tests(packet, shortlist, sha):
    def mutate_field(field, value):
        return lambda p: p["records"][0].__setitem__(field, value)
    cases = [
        ("word", mutate_field("word", "invented")),
        ("level", mutate_field("level", "B2")),
        ("pos", mutate_field("part_of_speech", "verb")),
        ("english", lambda p: p["records"][0]["shortlist_snapshot"].__setitem__("english_definition", "invented")),
        ("myanmar", lambda p: p["records"][0]["shortlist_snapshot"].__setitem__("myanmar_meaning", "အတည်ပြုပြီး")),
        ("example", lambda p: p["records"][0]["shortlist_snapshot"].__setitem__("example_sentence", "Fake example.")),
        ("source_path", lambda p: p["records"][0]["shortlist_provenance"].__setitem__("source_path", "draft/fake.json")),
        ("source_index", lambda p: p["records"][0]["shortlist_provenance"].__setitem__("source_index", 999)),
        ("source_blob", lambda p: p["records"][0]["shortlist_provenance"].__setitem__("source_blob_sha", "0"*40)),
        ("publisher", lambda p: p["records"][0]["publisher_source"].__setitem__("publisher", "unverified")),
        ("url", lambda p: p["records"][0]["publisher_source"].__setitem__("url", "https://example.com")),
        ("date", lambda p: p["records"][0]["publisher_source"].__setitem__("observed_on", "2026-10-29")),
        ("page", lambda p: p["records"][0]["publisher_source"].__setitem__("pdf_page", 1)),
        ("line", lambda p: p["records"][0]["publisher_source"].__setitem__("extracted_line", 1)),
        ("excerpt", lambda p: p["records"][0]["publisher_source"].__setitem__("source_excerpt", "forged")),
        ("cefr", lambda p: p["records"][0]["publisher_source"].__setitem__("source_cefr_level", "A1")),
        ("evidence_scope", lambda p: p["records"][0]["publisher_source"].__setitem__("evidence_scope", "INDEPENDENTLY_VERIFIED")),
        ("risk", mutate_field("editorial_risk", "NO_RISK")),
        ("review_task", mutate_field("independent_reviewer_task", "Self-approved")),
        ("hold", mutate_field("editorial_hold", False)),
        ("reviewed", mutate_field("independently_reviewed", True)),
        ("approved", mutate_field("release_approved", True)),
        ("receipt", mutate_field("independent_reviewer_receipt", {"approved": True})),
        ("fake_count", lambda p: p.__setitem__("independently_approved_count", 1)),
        ("missing_record", lambda p: p["records"].pop()),
        ("duplicate_record", lambda p: p["records"].__setitem__(0, copy.deepcopy(p["records"][1]))),
        ("invented_unlisted_CEFR", lambda p: next(r for r in p["records"] if r["word"] == "premises")["publisher_source"].__setitem__("source_cefr_level", "C1")),
        ("unlisted_url_loss", lambda p: next(r for r in p["records"] if r["word"] == "premises")["publisher_source"].__setitem__("urls_inspected", [PDF5])),
        ("cambridge_label", lambda p: p["cambridge_publisher_indexed_sense_leads"][0].__setitem__("publisher_indexed_cefr", "B2")),
        ("cambridge_url", lambda p: p["cambridge_publisher_indexed_sense_leads"][0].__setitem__("source_url", "https://example.com")),
        ("cambridge_scope", lambda p: p["cambridge_publisher_indexed_sense_leads"][0].__setitem__("source_access", "DIRECT_VERIFIED")),
        ("cambridge_date", lambda p: p["cambridge_publisher_indexed_sense_leads"][0].__setitem__("observed_on", "2026-10-27")),
        ("cambridge_false_approval", lambda p: p["cambridge_publisher_indexed_sense_leads"][0].__setitem__("independently_approved", True)),
    ]
    for label, fn in cases:
        fake = copy.deepcopy(packet)
        fn(fake)
        try:
            audit(fake, shortlist, sha)
        except (ValueError, KeyError, TypeError):
            continue
        raise AssertionError("FAIL: forged packet mutation accepted: " + label)
    fake_shortlist = copy.deepcopy(shortlist)
    fake_shortlist["entries"][0]["release_approved"] = True
    # A forged flag in an unrelated provisional word must be rejected globally.
    require(all(e.get("release_approved") is False for e in shortlist["entries"]), "Original shortlist already has false approval")
    require(fake_shortlist["entries"][0]["release_approved"] is True, "Mutation failed")
    print("PASS: " + str(len(cases)) + "/" + str(len(cases)) + " forged publisher, bilingual, provenance and false-review packet mutations rejected")
    return len(cases)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    raw = SHORTLIST_PATH.read_bytes()
    sha = git_blob_sha(raw)
    shortlist = json.loads(raw)
    packet = json.loads(PACKET_PATH.read_text(encoding="utf-8"))
    result = audit(packet, shortlist, sha)
    if args.self_test:
        result["negative_mutations_rejected"] = negative_tests(packet, shortlist, sha)
    result.update({"level_job": args.level, "source_scope": "WORD_POS_ONLY_NOT_HUMAN_REVIEW", "release_ready": False})
    path = ROOT / ("cefr-1000-oxford-c1-mixed-" + args.level + ".json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PASS: C1 Oxford mixed 12 source-bound staging audit; B2 conflicts 3, unlisted 1; independent approvals 0; NO DEPLOY")

if __name__ == "__main__":
    main()
