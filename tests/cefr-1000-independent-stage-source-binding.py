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
}
assert gate.independent_word_stage(mock, "apple", "english_sense")
assert gate.independent_word_stage(mock, "apple", "sense_specific_cefr")
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
pdf = dict(mock, source_url="https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
assert not gate.independent_word_stage(pdf, "apple", "sense_specific_cefr"), "Unlocated PDF must fail"
pdf["source_locator"] = {"pdf_page": 1, "extracted_line": 9, "source_excerpt": "apple n. A1"}
assert gate.independent_word_stage(pdf, "apple", "sense_specific_cefr")
for bad in (
    {"pdf_page": 0, "extracted_line": 9, "source_excerpt": "apple n. A1"},
    {"pdf_page": 1, "extracted_line": -1, "source_excerpt": "apple n. A1"},
    {"pdf_page": 1, "extracted_line": 9, "source_excerpt": "banana n. A1"},
    {"pdf_page": True, "extracted_line": 9, "source_excerpt": "apple n. A1"},
):
    assert not gate.independent_word_stage(dict(pdf, source_locator=bad), "apple", "sense_specific_cefr"), bad
print("PASS: mock-only source/headword binding and independent-stage negative tests; ZERO real approvals")
