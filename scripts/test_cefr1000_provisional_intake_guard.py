#!/usr/bin/env python3
"""Adversarial tests for the CEFR-1000 provisional intake guard.

These are structural refusal tests, NOT independent review or release evidence.
Runs against disposable copies only; never modifies source JSON or production.
"""
import copy
import json
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import cefr1000_provisional_intake_guard as guard

SOURCE = ROOT / "draft"
SHORTLIST = "CEFR-1000-PROVISIONAL-SHORTLIST.json"
TASKS = "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"


class IntakeRefusalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = {
            name: json.loads((SOURCE / name).read_text(encoding="utf-8"))
            for name in (SHORTLIST, TASKS)
        }

    def check_mutation(self, mutate, expected_fragment):
        with tempfile.TemporaryDirectory() as directory:
            destination = pathlib.Path(directory)
            documents = copy.deepcopy(self.original)
            mutate(documents[SHORTLIST], documents[TASKS])
            for name, data in documents.items():
                (destination / name).write_text(
                    json.dumps(data, ensure_ascii=False), encoding="utf-8"
                )
            with patch.object(guard, "DRAFT", destination):
                errors, _ = guard.check()
            self.assertTrue(
                any(expected_fragment in error for error in errors),
                f"Expected refusal containing {expected_fragment!r}; got {errors[:8]}",
            )

    def test_unmodified_intake_remains_on_hold(self):
        with patch.object(guard, "DRAFT", SOURCE):
            errors, counts = guard.check()
        self.assertEqual(errors, [])
        self.assertEqual({level: counts[level] for level in guard.LEVELS}, guard.TARGET)

    def test_duplicate_headword_pos(self):
        self.check_mutation(
            lambda s, t: s["entries"][1].update(
                word=s["entries"][0]["word"],
                part_of_speech=s["entries"][0]["part_of_speech"],
            ),
            "duplicate headword/POS",
        )

    def test_missing_myanmar(self):
        self.check_mutation(
            lambda s, t: s["entries"][0].update(burmese_meaning=""),
            "missing required editorial/provenance text",
        )

    def test_false_independent_approval(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(approval=True),
            "unexpected independent approval/status",
        )

    def test_fake_reviewer_signoff(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(
                reviewer_identity="Unverified Person", reviewer_signed_at="2026-11-23"
            ),
            "signoff present",
        )

    def test_unreviewed_evidence_in_task(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(
                source_evidence_urls=["https://example.org/"],
            ),
            "evidence populated",
        )

    def test_level_count_mismatch(self):
        self.check_mutation(
            lambda s, t: s["entries"][0].update(level="B2"),
            "A1: entries=",
        )

    def test_task_mismatch(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(headword="wrong"),
            "headword does not match shortlist",
        )

    def test_lifted_editorial_hold(self):
        self.check_mutation(
            lambda s, t: s["entries"][0].update(editorial_hold=False),
            "editorial hold lifted",
        )

    def test_pinned_source_changed(self):
        self.check_mutation(
            lambda s, t: t.update(source_shortlist_blob_sha="untrusted"),
            "pinned original shortlist blob",
        )


    def test_scope_tampering(self):
        self.check_mutation(
            lambda s, t: s["scope_target"].update(C1=1000),
            "scope/schema mismatch",
        )

    def test_hidden_reviewer_assignment(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(reviewer_assigned="Unverified Person"),
            "reviewer assignment unexpectedly populated",
        )

    def test_forged_field_level_review(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(exact_sense_cefr_review="APPROVED"),
            "exact_sense_cefr_review not pending",
        )

    def test_mismatched_shortlist_blob(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(shortlist_blob_sha="0" * 40),
            "shortlist provenance mismatch",
        )

    def test_invalid_source_index(self):
        self.check_mutation(
            lambda s, t: s["entries"][0].update(source_index=-1),
            "invalid nonnegative source index",
        )

    def test_noncanonical_task_id(self):
        self.check_mutation(
            lambda s, t: t["tasks"][0].update(task_id="CEFR1000-A1-9999"),
            "task ID does not match per-level sequence",
        )

    def test_changed_release_hold(self):
        self.check_mutation(
            lambda s, t: s.update(release_status="READY"),
            "shortlist release hold status changed",
        )


if __name__ == "__main__":
    unittest.main()
