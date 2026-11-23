#!/usr/bin/env python3
"""Additional fail-closed mutation regressions for provisional CEFR-1000 intake.

Author-side structural checks only. No independent signoff or release authority.
Mutations operate on temporary JSON copies, never the source files.
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

NAMES = ("CEFR-1000-PROVISIONAL-SHORTLIST.json", "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json")


class AdditionalIntakeRefusalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = [
            json.loads((ROOT / "draft" / name).read_text(encoding="utf-8"))
            for name in NAMES
        ]

    def reject(self, mutation, expected):
        shortlist, tasks = copy.deepcopy(self.source)
        mutation(shortlist, tasks)
        with tempfile.TemporaryDirectory() as folder:
            for name, document in zip(NAMES, (shortlist, tasks)):
                (pathlib.Path(folder) / name).write_text(
                    json.dumps(document, ensure_ascii=False), encoding="utf-8"
                )
            with patch.object(guard, "DRAFT", pathlib.Path(folder)):
                errors, _ = guard.check()
        self.assertTrue(
            any(expected in error for error in errors),
            f"Expected {expected!r}, received {errors[:10]!r}",
        )

    def test_missing_english_definition(self):
        self.reject(lambda s, t: s["entries"][0].update(english_definition=" "),
                    "missing required editorial/provenance text")

    def test_missing_example(self):
        self.reject(lambda s, t: s["entries"][0].update(example_sentence=""),
                    "missing required editorial/provenance text")

    def test_missing_source_path(self):
        self.reject(lambda s, t: s["entries"][0].update(source_path=""),
                    "invalid source path")

    def test_source_path_traversal(self):
        self.reject(lambda s, t: s["entries"][0].update(source_path="draft/../main.json"),
                    "invalid source path")

    def test_malformed_blob_sha(self):
        self.reject(lambda s, t: s["entries"][0].update(source_blob_sha="bad"),
                    "malformed source blob SHA")

    def test_boolean_source_index(self):
        self.reject(lambda s, t: s["entries"][0].update(source_index=True),
                    "invalid nonnegative source index")

    def test_false_reviewed_english(self):
        self.reject(lambda s, t: s["entries"][0].update(reviewed_english=True),
                    "reviewed_english must remain false")

    def test_false_reviewed_pronunciation(self):
        self.reject(lambda s, t: s["entries"][0].update(reviewed_pronunciation=True),
                    "reviewed_pronunciation must remain false")

    def test_forged_reviewed_myanmar(self):
        self.reject(lambda s, t: s["entries"][0].update(reviewed_burmese=True),
                    "reviewed_burmese must remain false")

    def test_task_source_index_mismatch(self):
        self.reject(lambda s, t: t["tasks"][0].update(source_index=999999),
                    "source_index does not match shortlist")

    def test_task_source_path_mismatch(self):
        self.reject(lambda s, t: t["tasks"][0].update(source_path="draft/other.json"),
                    "source_path does not match shortlist")

    def test_task_approval_count_forgery(self):
        self.reject(lambda s, t: t["independently_approved_by_level"].update(A1=1),
                    "claims nonzero independent approval")

    def test_shortlist_approval_count_forgery(self):
        self.reject(lambda s, t: s["independently_approved_by_level"].update(C1=1),
                    "claims nonzero independent approval")

    def test_review_status_forgery(self):
        self.reject(lambda s, t: t["tasks"][0].update(review_status="APPROVED"),
                    "unexpected independent approval/status")

    def test_provisional_entry_status_forgery(self):
        self.reject(lambda s, t: s["entries"][0].update(status="APPROVED"),
                    "provisional status changed")


if __name__ == "__main__":
    unittest.main()
