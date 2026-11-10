"""Regression tests for versioned review-content binding (no human approval implied)."""
import hashlib
import json
import unittest

from scripts.check_cefr1000_release_evidence import reviewed_content_sha256

ENTRY = {
    "word": "wheelbarrow", "part_of_speech": "noun", "sense_id": "transport-tool",
    "level": "A2", "english_definition": "A small cart with one wheel.",
    "burmese_meaning": "ဘီးတစ်လုံးပါသော လက်တွန်းလှည်း",
    "example_sentence": "She pushed the wheelbarrow across the garden.",
}


class ReviewContentBindingTests(unittest.TestCase):
    def test_deterministic_and_64_hex(self):
        value = reviewed_content_sha256(ENTRY, "myanmar")
        self.assertEqual(len(value), 64)
        self.assertEqual(value, reviewed_content_sha256(dict(ENTRY), "myanmar"))
        int(value, 16)

    def test_edit_invalidates_english_review(self):
        edited = dict(ENTRY, english_definition="A vehicle for transporting materials.")
        self.assertNotEqual(reviewed_content_sha256(ENTRY, "english"),
                            reviewed_content_sha256(edited, "english"))

    def test_myanmar_edit_invalidates_review(self):
        edited = dict(ENTRY, burmese_meaning="ပစ္စည်းများသယ်ရန် လက်တွန်းလှည်း")
        self.assertNotEqual(reviewed_content_sha256(ENTRY, "myanmar"),
                            reviewed_content_sha256(edited, "myanmar"))

    def test_cefr_reassignment_invalidates_review(self):
        edited = dict(ENTRY, level="B1")
        self.assertNotEqual(reviewed_content_sha256(ENTRY, "cefr"),
                            reviewed_content_sha256(edited, "cefr"))

    def test_example_edit_invalidates_review(self):
        edited = dict(ENTRY, example_sentence="He pushed the wheelbarrow.")
        self.assertNotEqual(reviewed_content_sha256(ENTRY, "example"),
                            reviewed_content_sha256(edited, "example"))

    def test_sense_and_pos_changes_invalidate_every_domain(self):
        for change in ({"sense_id": "other-sense"}, {"part_of_speech": "verb"}):
            edited = dict(ENTRY, **change)
            for domain in ("english", "myanmar", "example", "cefr", "pronunciation"):
                with self.subTest(change=change, domain=domain):
                    self.assertNotEqual(reviewed_content_sha256(ENTRY, domain),
                                        reviewed_content_sha256(edited, domain))


if __name__ == "__main__":
    unittest.main()
