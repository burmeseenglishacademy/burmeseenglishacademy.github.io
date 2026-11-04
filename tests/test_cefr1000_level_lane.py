#!/usr/bin/env python3
"""Staging-only, genuinely CEFR-lane-specific adversarial release-gate tests.

Invoke with CEFR_QA_LEVEL=A1|A2|B1|B2|C1. Five distinct CI matrix
lanes mutate the selected level, rather than repeating only the same
cross-level synthetic tests. Synthetic fixtures never confer approval.
"""
import copy
import os
import unittest

from test_cefr1000_release_gate import gate, synthetic


class SelectedLevelAdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.level = os.environ.get("CEFR_QA_LEVEL", "").strip()
        if cls.level not in gate.LEVELS:
            raise ValueError(
                "CEFR_QA_LEVEL must explicitly select A1, A2, B1, B2 or C1; "
                "a CI lane must not silently default to A1"
            )
        cls.baseline = synthetic()
        if gate.check(*cls.baseline):
            raise AssertionError("Synthetic structural baseline must be valid")
        cls.selected = f"{cls.level}-000"
        cls.other_level = next(x for x in gate.LEVELS if x != cls.level)
        cls.other = f"{cls.other_level}-000"

    def fixture(self):
        manifest, evidence = copy.deepcopy(self.baseline)
        entry = next(x for x in manifest["entries"] if x["id"] == self.selected)
        return manifest, evidence, entry

    def assert_blocked(self, manifest, evidence):
        errors = gate.check(manifest, evidence)
        self.assertTrue(errors, f"{self.level} corruption incorrectly permitted release")

    def test_selected_lane_is_real_and_distinct(self):
        self.assertIn(self.selected, {x["id"] for x in self.baseline[0]["entries"]})
        self.assertEqual(
            sum(x["level"] == self.level for x in self.baseline[0]["entries"]), 200
        )
        print(f"SELECTED_LANE={self.level}; mutated entry={self.selected}")

    def test_selected_level_independent_cefr_review_missing(self):
        m, e, _ = self.fixture()
        del e["independent_reviews"][self.selected]["cefr"]
        self.assert_blocked(m, e)

    def test_selected_level_myanmar_review_unapproved(self):
        m, e, _ = self.fixture()
        e["independent_reviews"][self.selected]["myanmar"]["approved"] = False
        self.assert_blocked(m, e)

    def test_selected_level_source_observation_missing(self):
        m, e, _ = self.fixture()
        e["independent_reviews"][self.selected]["english"]["source_observed_at"] = ""
        self.assert_blocked(m, e)

    def test_selected_level_george_headword_listening_missing(self):
        m, e, _ = self.fixture()
        e["audio"][self.selected]["george_headword"]["listening_passed"] = False
        self.assert_blocked(m, e)

    def test_selected_level_emma_example_clip_missing(self):
        m, e, _ = self.fixture()
        del e["audio"][self.selected]["emma_example"]
        self.assert_blocked(m, e)

    def test_selected_level_editorial_hold(self):
        m, e, entry = self.fixture()
        entry["editorial_hold"] = True
        self.assert_blocked(m, e)

    def test_selected_level_count_corruption(self):
        m, e, entry = self.fixture()
        entry["level"] = self.other_level
        self.assert_blocked(m, e)

    def test_selected_level_cross_level_duplicate_sense(self):
        m, e, entry = self.fixture()
        other = next(x for x in m["entries"] if x["id"] == self.other)
        other["word"] = entry["word"]
        other["part_of_speech"] = entry["part_of_speech"]
        other["sense_id"] = entry["sense_id"]
        self.assert_blocked(m, e)

    def test_selected_level_missing_part_of_speech(self):
        m, e, entry = self.fixture()
        entry["part_of_speech"] = ""
        self.assert_blocked(m, e)


if __name__ == "__main__":
    unittest.main()
