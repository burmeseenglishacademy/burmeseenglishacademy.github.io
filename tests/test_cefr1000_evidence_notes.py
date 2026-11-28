#!/usr/bin/env python3
"""Synthetic negative tests for CEFR-1000 evidence-note provenance validation."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_cefr1000_evidence_notes import validate_note_text  # noqa: E402

TASKS = {
    "CEFR1000-A1-0001": {
        "task_id": "CEFR1000-A1-0001",
        "level": "A1",
        "headword": "book",
        "approval": False,
    }
}
VALID = """# CEFR-1000 author-side evidence
**Observed:** 2026-11-29
**Scope:** Author-side source research only; this is not an independent review or approval.
Shortlist blob SHA: `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
Task: CEFR1000-A1-0001
Source: https://dictionary.cambridge.org/dictionary/learner-english/book
"""


class EvidenceNoteTests(unittest.TestCase):
    def test_valid_author_side_note_passes(self):
        self.assertEqual(validate_note_text(VALID, TASKS), [])

    def test_missing_observation_date_fails(self):
        self.assertTrue(any("observation date" in x for x in validate_note_text(
            VALID.replace("**Observed:** 2026-11-29", ""), TASKS
        )))

    def test_missing_source_url_fails(self):
        self.assertTrue(any("source URL" in x for x in validate_note_text(
            VALID.replace("https://dictionary.cambridge.org/dictionary/learner-english/book", ""), TASKS
        )))

    def test_missing_provenance_sha_fails(self):
        self.assertTrue(any("provenance SHA" in x for x in validate_note_text(
            VALID.replace("a" * 40, "not-a-sha"), TASKS
        )))

    def test_missing_non_independent_disclaimer_fails(self):
        self.assertTrue(any("not independent signoff" in x for x in validate_note_text(
            VALID.replace("this is not an independent review or approval", "review notes"), TASKS
        )))

    def test_unknown_task_id_fails(self):
        self.assertTrue(any("unknown review task" in x for x in validate_note_text(
            VALID.replace("CEFR1000-A1-0001", "CEFR1000-A2-0001"), TASKS
        )))

    def test_task_level_mismatch_fails(self):
        altered = {"CEFR1000-A2-0001": {"task_id": "CEFR1000-A2-0001", "level": "A1"}}
        self.assertTrue(any("task-level mismatch" in x for x in validate_note_text(
            VALID.replace("CEFR1000-A1-0001", "CEFR1000-A2-0001"), altered
        )))

    def test_invalid_date_fails(self):
        self.assertTrue(any("invalid observation date" in x for x in validate_note_text(
            VALID.replace("2026-11-29", "2026-19-45"), TASKS
        )))


if __name__ == "__main__":
    unittest.main(verbosity=2)
