"""Synthetic regression coverage for first-pass completeness and source provenance.

This does not certify independent bilingual, CEFR, or pronunciation review.
"""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lexical_audit", ROOT / "scripts" / "cefr1000_provisional_lexical_audit.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def item(word, level="A1", index=0, **changes):
    value = dict(word=word, level=level, part_of_speech="noun",
                 english_definition="A concrete object.", burmese_meaning="ပစ္စည်း",
                 example_sentence="This is a book.",
                 source_path="draft/A1-EDITORIAL-STARTER.json",
                 source_index=index, source_blob_sha="a" * 40,
                 editorial_hold=True, release_approved=False,
                 reviewed_english=False, reviewed_burmese=False,
                 reviewed_example=False, reviewed_level=False)
    value.update(changes)
    return value

class ProvenanceAndDraftTextTests(unittest.TestCase):
    def test_missing_first_pass_text_is_counted_by_field_and_level(self):
        result = module.audit({"entries": [
            item("book", english_definition="", burmese_meaning=" "),
            item("walk", "B2", 1, example_sentence=None),
        ]})
        gaps = result["missing_first_pass_text_by_level"]
        self.assertEqual(gaps["english_definition"]["A1"], 1)
        self.assertEqual(gaps["burmese_meaning"]["A1"], 1)
        self.assertEqual(gaps["example_sentence"]["B2"], 1)
        self.assertEqual(gaps["english_definition"]["B2"], 0)

    def test_duplicate_source_record_is_reported_without_approval(self):
        result = module.audit({"entries": [item("book"), item("table", "B1")]})
        self.assertEqual(len(result["duplicate_draft_source_records"]), 1)
        self.assertEqual(result["classification"], "TRIAGE_NOT_INDEPENDENT_REVIEW")

    def test_provenance_rejects_traversal_windows_path_boolean_index_and_bad_sha(self):
        result = module.audit({"entries": [
            item("book", source_path="draft/../secret.json", source_index=True,
                 source_blob_sha="not-a-sha"),
            item("table", "A2", 1, source_path="draft\\unsafe.json"),
        ]})
        self.assertEqual(result["provenance_gaps"]["invalid_source_path"], 2)
        self.assertEqual(result["provenance_gaps"]["invalid_source_index"], 1)
        self.assertEqual(result["provenance_gaps"]["invalid_source_blob_sha"], 1)

    def test_complete_first_pass_is_not_independent_evidence(self):
        result = module.audit({"entries": [item("book")]})
        self.assertEqual(sum(sum(v.values()) for v in
                         result["missing_first_pass_text_by_level"].values()), 0)
        self.assertEqual(result["missing_evidence_by_level"]["source_level"]["A1"], 1)
        self.assertFalse(result["target_200_each_met"])

if __name__ == "__main__":
    unittest.main()
