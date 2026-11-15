#!/usr/bin/env python3
"""CEFR-1000 negative-path schema checks; synthetic fixtures, NOT signoff.

Run: python3 -m unittest discover -s tests -p 'test_cefr1000_malformed_evidence.py'
"""
import copy
import unittest
from test_cefr1000_release_gate import gate, synthetic


class MalformedEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.good = synthetic()
        assert gate.check(*cls.good) == [], "Synthetic baseline unexpectedly rejected"

    def setUp(self):
        self.manifest, self.evidence = copy.deepcopy(self.good)

    def blocked(self):
        errors = gate.check(self.manifest, self.evidence)
        self.assertTrue(errors, "Invalid evidence must fail closed")

    def test_manifest_is_list(self):
        self.manifest = []
        self.blocked()

    def test_entries_is_object(self):
        self.manifest["entries"] = {}
        self.blocked()

    def test_entry_is_null(self):
        self.manifest["entries"][0] = None
        self.blocked()

    def test_level_is_list(self):
        self.manifest["entries"][0]["level"] = ["A1"]
        self.blocked()

    def test_source_index_is_boolean(self):
        self.manifest["entries"][0]["source_index"] = True
        self.blocked()

    def test_source_index_negative(self):
        self.manifest["entries"][0]["source_index"] = -1
        self.blocked()

    def test_source_blob_sha_short(self):
        self.manifest["entries"][0]["source_blob_sha"] = "a" * 39
        self.blocked()

    def test_source_path_parent_traversal(self):
        self.manifest["entries"][0]["source_path"] = "../draft/source.json"
        self.blocked()

    def test_release_sha_is_list(self):
        self.evidence["release_commit_sha"] = ["b" * 40]
        self.blocked()

    def test_ci_run_id_is_boolean(self):
        self.evidence["parallel_cefr_ci"]["run_id"] = True
        self.blocked()

    def test_ci_job_is_null(self):
        self.evidence["parallel_cefr_ci"]["jobs"]["A1"] = None
        self.blocked()

    def test_review_is_null(self):
        self.evidence["independent_reviews"]["A1-000"]["cefr"] = None
        self.blocked()

    def test_audio_clip_is_list(self):
        self.evidence["audio"]["A1-000"]["emma_example"] = []
        self.blocked()

    def test_audio_digest_is_null(self):
        self.evidence["audio"]["A1-000"]["emma_headword"]["asset_sha256"] = None
        self.blocked()

    def test_listening_date_without_timezone(self):
        self.evidence["audio"]["A1-000"]["george_example"]["listened_at"] = "2026-11-15T13:00:00"
        self.blocked()

    def test_review_date_impossible(self):
        self.evidence["independent_reviews"]["A1-000"]["english"]["reviewed_at"] = "2026-02-30T12:00:00Z"
        self.blocked()

    def test_release_gates_is_list(self):
        self.evidence["release_gates"] = []
        self.blocked()

    def test_iphone_evidence_url_is_null(self):
        self.evidence["release_gates"]["physical_iphone_safari"]["evidence_url"] = None
        self.blocked()


if __name__ == "__main__":
    unittest.main()
