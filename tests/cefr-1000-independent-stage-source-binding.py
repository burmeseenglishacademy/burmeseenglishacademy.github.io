#!/usr/bin/env python3
"""Mock-only negative tests: never assert real independent signoff."""
import importlib.util
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("launch", root / "tools/audit_cefr_1000_launch_readiness.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

mock = {
    "result": "PASS",
    "reviewed_on": "2026-10-27",
    "reviewer_id": "TEST_ONLY_human_editor",
    "reviewer_role": "INDEPENDENT_HUMAN_LINGUIST",
    "reviewer_attestation_url": "https://github.com/mock-review/attestations/123",
    "notes": "TEST ONLY: source locator validation, not a human review",
    "source_url": "https://dictionary.cambridge.org/dictionary/english/apple",
    "source_access": "DIRECT_PUBLISHER_DICTIONARY_PAGE",
    "source_evidence_scope": "EXACT_SENSE",
    "source_sense_heading": "apple noun (FRUIT)",
    "source_observation": "Publisher entry describes the edible fruit sense rather than a technology brand.",
    "source_observed_on": "2026-10-27",
    "source_cefr_level": "A1",
    "source_cefr_evidence_scope": "PUBLISHER_EXACT_SENSE_CEFR_LABEL",
    "source_cefr_evidence_quote": "apple noun A1 (FRUIT)",
}
assert gate.independent_word_stage(mock, "apple", "english_sense")
assert gate.independent_word_stage(mock, "apple", "sense_specific_cefr", expected_level="A1")
assert not gate.independent_word_stage(mock, "banana", "english_sense"), "Wrong headword must fail"
assert not gate.independent_word_stage(mock, "banana", "sense_specific_cefr"), "Wrong CEFR source must fail"
assert gate.independent_word_stage(mock, "banana", "original_example"), "No dictionary URL required for example"
for name, value in (
    ("reviewer_attestation_url", ""),
    ("reviewer_role", "AI_REVIEWER"),
    ("reviewer_id", "gpt-6"),
    ("reviewer_id", "editorial-bot-3"),
    ("reviewer_id", "ChatGPT"),
):
    changed = dict(mock, **{name: value})
    assert not gate.independent_word_stage(changed, "apple", "english_sense"), name
# Broad Oxford wordlists and index snippets cannot sign off exact senses.
pdf = dict(mock, source_url="https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
pdf["source_locator"] = {"pdf_page": 1, "extracted_line": 9, "source_excerpt": "apple n. A1"}
assert not gate.independent_word_stage(pdf, "apple", "english_sense")
assert not gate.independent_word_stage(pdf, "apple", "sense_specific_cefr", expected_level="A1")
for field, bad in (
    ("source_url", "https://untrusted-dictionary.example/dictionary/english/apple"),
    ("source_access", "PUBLISHER_SEARCH_INDEXED_SNIPPET"),
    ("source_evidence_scope", "WORD_POS_LEVEL_ONLY"),
    ("source_sense_heading", ""),
    ("source_observation", "word"),
    ("source_observed_on", "2026-10-28"),
):
    assert not gate.independent_word_stage(dict(mock, **{field: bad}), "apple", "english_sense"), field
for field, bad in (
    ("source_cefr_level", "B1"),
    ("source_cefr_level", ""),
    ("source_cefr_evidence_scope", "OXFORD_TOPIC_CEFR"),
    ("source_cefr_evidence_quote", ""),
):
    assert not gate.independent_word_stage(dict(mock, **{field: bad}), "apple", "sense_specific_cefr", expected_level="A1"), field
assert not gate.independent_word_stage(mock, "apple", "sense_specific_cefr", expected_level="B1")
print("PASS: mock-only publisher exact-sense/date/CEFR negative tests; ZERO real approvals")
