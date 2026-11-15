#!/usr/bin/env python3
"""Additional adversarial checks; synthetic evidence is never real signoff."""
import copy
import unittest
from test_cefr1000_release_gate import gate, synthetic


class ReleaseGateBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.manifest, self.evidence = synthetic()

    def blocked(self):
        self.assertTrue(gate.check(self.manifest, self.evidence))

    def test_synthetic_schema_baseline_only(self):
        self.assertEqual(gate.check(self.manifest, self.evidence), [])

    def test_non_object_manifest(self):
        self.manifest = []
        self.blocked()

    def test_non_array_entries(self):
        self.manifest["entries"] = {}
        self.blocked()

    def test_non_object_entry(self):
        self.manifest["entries"][0] = None
        self.blocked()

    def test_non_string_level(self):
        self.manifest["entries"][0]["level"] = ["A1"]
        self.blocked()

    def test_missing_source_path(self):
        del self.manifest["entries"][0]["source_path"]
        self.blocked()

    def test_invalid_source_blob_sha(self):
        self.manifest["entries"][0]["source_blob_sha"] = "not-a-sha"
        self.blocked()

    def test_boolean_source_index(self):
        self.manifest["entries"][0]["source_index"] = True
        self.blocked()

    def test_missing_release_commit(self):
        del self.evidence["release_commit_sha"]
        self.blocked()

    def test_malformed_release_commit(self):
        self.evidence["release_commit_sha"] = "abc"
        self.blocked()

    def test_mismatched_ci_sha(self):
        self.evidence["parallel_cefr_ci"]["commit_sha"] = "c" * 40
        self.blocked()

    def test_missing_ci_run_id(self):
        del self.evidence["parallel_cefr_ci"]["run_id"]
        self.blocked()

    def test_boolean_ci_run_id(self):
        self.evidence["parallel_cefr_ci"]["run_id"] = True
        self.blocked()

    def test_missing_level_job(self):
        del self.evidence["parallel_cefr_ci"]["jobs"]["C1"]
        self.blocked()

    def test_failed_level_job(self):
        self.evidence["parallel_cefr_ci"]["jobs"]["B2"]["conclusion"] = "failure"
        self.blocked()

    def test_missing_level_job_logs(self):
        del self.evidence["parallel_cefr_ci"]["jobs"]["A2"]["logs_url"]
        self.blocked()

    def test_missing_audio_asset_digest(self):
        del self.evidence["audio"]["A1-000"]["george_example"]["asset_sha256"]
        self.blocked()

    def test_unapproved_cefr_review(self):
        self.evidence["independent_reviews"]["C1-199"]["cefr"]["approved"] = False
        self.blocked()


if __name__ == "__main__":
    unittest.main()
