#!/usr/bin/env python3
"""Adversarial regression tests for the provisional-only CEFR-1000 inventory audit.

These tests use synthetic entries, never grant approval, and never touch production.
Run: python3 -m unittest discover -s tests -p 'test_cefr1000_provisional_audit.py'
"""
import copy
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("provisional_audit", ROOT / "scripts/audit_cefr1000_provisional.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def fixture():
    entries = []
    for level in module.LEVELS:
        for i in range(200):
            entries.append({
                "word": f"{level.lower()}_synthetic_{i}",
                "level": level,
                "part_of_speech": "noun",
                "english_definition": "A synthetic testing item.",
                "burmese_meaning": "စမ်းသပ်ရန်",
                "example_sentence": "This is a synthetic testing item.",
                "source_path": "draft/synthetic-fixture.json",
                "source_index": i,
                "source_blob_sha": "a" * 40,
                "editorial_hold": True,
                "status": "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING",
                **{flag: False for flag in module.FLAGS},
            })
    return {
        "release_status": "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
        "scope_target": {level: 200 for level in module.LEVELS},
        "counts_by_level": {level: 200 for level in module.LEVELS},
        "independently_approved_by_level": {level: 0 for level in module.LEVELS},
        "entries": entries,
    }


class ProvisionalAuditAdversarialTests(unittest.TestCase):
    def setUp(self):
        self.data = fixture()

    def assert_rejected(self, needle):
        errors, _ = module.audit(self.data)
        self.assertTrue(any(needle in error for error in errors), errors)

    def test_valid_synthetic_fixture_is_only_structurally_valid(self):
        self.assertEqual(module.audit(self.data)[0], [])

    def test_missing_entry(self):
        self.data["entries"].pop()
        self.assert_rejected("expected 1000")

    def test_wrong_level_distribution(self):
        self.data["entries"][0]["level"] = "B1"
        self.assert_rejected("A1: expected 200")

    def test_casefold_duplicate(self):
        self.data["entries"][1]["word"] = self.data["entries"][0]["word"].upper()
        self.assert_rejected("duplicate headword")

    def test_missing_myanmar(self):
        self.data["entries"][0]["burmese_meaning"] = ""
        self.assert_rejected("missing burmese_meaning")

    def test_missing_provenance(self):
        self.data["entries"][0]["source_blob_sha"] = ""
        self.assert_rejected("invalid provenance SHA")

    def test_unheld_entry(self):
        self.data["entries"][0]["editorial_hold"] = False
        self.assert_rejected("not explicitly on editorial hold")

    def test_forged_independent_review(self):
        self.data["entries"][0]["reviewed_burmese"] = True
        self.assert_rejected("reviewed_burmese is not explicitly false")

    def test_forged_release_approval(self):
        self.data["entries"][0]["release_approved"] = True
        self.assert_rejected("release_approved is not explicitly false")

    def test_forged_aggregate_approval(self):
        self.data["independently_approved_by_level"]["C1"] = 1
        self.assert_rejected("provisional independent approval count must be zero")

    def test_modified_release_status(self):
        self.data["release_status"] = "READY"
        self.assert_rejected("provisional release status changed")

    def test_source_index_boolean_is_invalid(self):
        self.data["entries"][0]["source_index"] = True
        self.assert_rejected("invalid source_index")

    def test_wrong_declared_counts(self):
        self.data["counts_by_level"]["A1"] = 199
        self.assert_rejected("declared count differs")

    def test_extra_level(self):
        self.data["entries"][0]["level"] = "C2"
        self.assert_rejected("unexpected level")

    def test_normalized_duplicate(self):
        self.data["entries"][0]["word"] = "ＡＢＣ"
        self.data["entries"][1]["word"] = "abc"
        self.assert_rejected("duplicate headword")


if __name__ == "__main__":
    unittest.main()
