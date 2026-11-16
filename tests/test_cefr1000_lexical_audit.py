"""Regression tests for the read-only provisional CEFR-1000 lexical triage.

Synthetic data only. Passing tests does NOT establish independent CEFR,
English/Myanmar, audio, iPhone, hosting or production verification.
Run: python3 -m unittest discover -s tests -p 'test_cefr1000_lexical_audit.py'
"""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "cefr1000_provisional_lexical_audit",
    ROOT / "scripts" / "cefr1000_provisional_lexical_audit.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def entry(word="book", level="A1", **overrides):
    item = {
        "word": word, "level": level, "part_of_speech": "noun",
        "source_path": "draft/A1-EDITORIAL-STARTER.json",
        "source_index": 0, "source_blob_sha": "a" * 40,
        "editorial_hold": True, "release_approved": False,
        "reviewed_english": False, "reviewed_burmese": False,
        "reviewed_example": False, "reviewed_level": False,
        "sense_id": "physical_volume",
        "english_definition": "A synthetic object for a regression test.",
        "burmese_meaning": "စမ်းသပ်ရန် ပစ္စည်း",
        "example_sentence": "This is a synthetic test object.",
    }
    item.update(overrides)
    return item


class LexicalAuditTests(unittest.TestCase):
    def audit(self, entries):
        return MODULE.audit({"entries": entries})

    def test_missing_source_evidence_counts_per_level(self):
        report = self.audit([entry("book"), entry("walk", "B2", source_level="B2",
                                   source_english="attested", source_burmese="attested")])
        self.assertEqual(report["missing_evidence_by_level"]["source_level"]["A1"], 1)
        self.assertEqual(report["missing_evidence_by_level"]["source_level"]["B2"], 0)
        self.assertEqual(report["missing_evidence_by_level"]["source_burmese"]["A1"], 1)
        self.assertEqual(report["missing_evidence_by_level"]["sense_id"]["B2"], 0)

    def test_lowercase_first_person_pronoun_is_editorial_risk(self):
        report = self.audit([entry("i", part_of_speech="pronoun")])
        self.assertIn("first_person_pronoun_capitalization",
                      {risk["risk"] for risk in report["risk_queue"]})
        self.assertEqual(self.audit([entry("I", part_of_speech="pronoun")])["risk_queue"], [])

    def test_missing_entries_fail_closed(self):
        with self.assertRaises(ValueError):
            MODULE.audit({})

    def test_empty_inventory_cannot_meet_target(self):
        report = self.audit([])
        self.assertFalse(report["target_200_each_met"])
        self.assertEqual(report["entries_observed"], 0)

    def test_unicode_casefold_collision_is_review_only(self):
        report = self.audit([entry("BOOK"), entry("book", "B1")])
        self.assertEqual(len(report["same_normalized_headword_groups"]), 1)
        self.assertEqual(report["classification"], "TRIAGE_NOT_INDEPENDENT_REVIEW")

    def test_distinct_senses_not_identical_sense_duplicates(self):
        report = self.audit([
            entry("bank", sense_id="financial_institution"),
            entry("bank", "B2", sense_id="river_edge"),
        ])
        self.assertEqual(len(report["same_normalized_headword_groups"]), 1)
        self.assertEqual(report["same_explicit_word_pos_sense_groups"], [])

    def test_identical_explicit_sense_flagged_across_levels(self):
        report = self.audit([entry("bank"), entry("BANK", "B2")])
        self.assertEqual(len(report["same_explicit_word_pos_sense_groups"]), 1)

    def test_article_forms_require_human_adjudication(self):
        report = self.audit([
            entry("a", part_of_speech="article", sense_id="indefinite"),
            entry("an", part_of_speech="article", sense_id="indefinite"),
        ])
        self.assertEqual(len(report["indefinite_article_a_an_review_queue"]), 2)

    def test_unexpected_review_or_release_flags_raise_risk(self):
        report = self.audit([entry("book", editorial_hold=False,
                                   release_approved=True, reviewed_level=True)])
        names = {risk["risk"] for risk in report["risk_queue"]}
        self.assertIn("provisional_hold_or_approval_invariant_changed", names)
        self.assertIn("unexpected_review_flag", names)

    def test_missing_sense_id_is_not_silently_accepted(self):
        report = self.audit([entry("book", sense_id="")])
        self.assertIn("missing_explicit_sense_id",
                      {risk["risk"] for risk in report["risk_queue"]})

    def test_wordnet_and_named_entity_markers_are_risks(self):
        report = self.audit([
            entry("thing", source_path="draft/wordnet_import.json"),
            entry("New York", source_path="draft/named_entity.json"),
        ])
        names = [risk["risk"] for risk in report["risk_queue"]]
        self.assertIn("historical_source_or_named_entity_marker", names)
        self.assertIn("possible_multiword_proper_name", names)

    def test_unknown_level_not_counted_as_valid(self):
        report = self.audit([entry("book", "C2")])
        self.assertEqual(report["unknown_levels"], {"C2": 1})
        self.assertFalse(report["target_200_each_met"])

    def test_malformed_entry_remains_visible(self):
        report = self.audit([None, entry("book")])
        self.assertEqual(report["entries_observed"], 2)
        self.assertIn("malformed_entry",
                      {risk["risk"] for risk in report["risk_queue"]})


if __name__ == "__main__":
    unittest.main()
