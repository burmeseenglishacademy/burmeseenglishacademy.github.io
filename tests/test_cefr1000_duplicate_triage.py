"""Adversarial tests for read-only provisional duplicate triage.

These tests do not validate CEFR classification or provide human signoff.
"""
import copy
import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "cefr1000_duplicate_triage",
    ROOT / "scripts" / "triage_cefr1000_provisional_duplicates.py",
)
triage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(triage)
SHORTLIST = json.loads(
    (ROOT / "draft" / "CEFR-1000-PROVISIONAL-SHORTLIST.json").read_text(encoding="utf-8")
)


class ProvisionalDuplicateTriageTests(unittest.TestCase):
    def test_baseline_has_no_structural_errors_but_is_not_approved(self):
        errors, warnings = triage.audit(SHORTLIST)
        self.assertEqual(errors, [])
        self.assertEqual(SHORTLIST["independently_approved_by_level"], dict.fromkeys(triage.LEVELS, 0))
        self.assertTrue(any("capitalised I" in w for w in warnings))

    def test_unicode_compatibility_duplicate_headword_is_rejected(self):
        data = copy.deepcopy(SHORTLIST)
        data["entries"][1]["word"] = "Ａ"
        errors, _ = triage.audit(data)
        self.assertTrue(any("duplicate normalised headword" in e for e in errors))

    def test_cross_level_duplicate_headword_is_rejected(self):
        data = copy.deepcopy(SHORTLIST)
        data["entries"][200]["word"] = data["entries"][0]["word"]
        errors, _ = triage.audit(data)
        self.assertTrue(any("duplicate normalised headword" in e for e in errors))

    def test_level_reassignment_is_rejected_even_with_1000_records(self):
        data = copy.deepcopy(SHORTLIST)
        data["entries"][0]["level"] = "A2"
        errors, _ = triage.audit(data)
        self.assertTrue(any("A1: expected 200" in e for e in errors))
        self.assertTrue(any("A2: expected 200" in e for e in errors))

    def test_fake_independent_approval_is_rejected(self):
        data = copy.deepcopy(SHORTLIST)
        data["entries"][0]["release_approved"] = True
        data["entries"][0]["editorial_hold"] = False
        data["entries"][0]["reviewed_level"] = True
        data["independently_approved_by_level"]["A1"] = 1
        errors, _ = triage.audit(data)
        self.assertTrue(any("hold/approval invariant" in e for e in errors))
        self.assertTrue(any("reviewed_level" in e for e in errors))
        self.assertTrue(any("claims independent approval" in e for e in errors))

    def test_empty_myanmar_and_example_are_rejected(self):
        data = copy.deepcopy(SHORTLIST)
        data["entries"][0]["burmese_meaning"] = " "
        data["entries"][1]["example_sentence"] = ""
        errors, _ = triage.audit(data)
        self.assertTrue(any("burmese_meaning" in e for e in errors))
        self.assertTrue(any("example_sentence" in e for e in errors))

    def test_malformed_entry_is_rejected_without_crashing(self):
        data = copy.deepcopy(SHORTLIST)
        data["entries"][0] = None
        errors, _ = triage.audit(data)
        self.assertTrue(any("not an object" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
