#!/usr/bin/env python3
"""Adversarial release-evidence regressions. All fixtures are synthetic, never signoff."""
import unittest
from test_cefr1000_release_gate import gate, synthetic


class ReleaseEvidenceAdversarialTests(unittest.TestCase):
    def setUp(self):
        self.manifest, self.evidence = synthetic()

    def assert_blocked(self):
        errors = gate.check(self.manifest, self.evidence)
        self.assertTrue(errors, "Malformed evidence must never pass")

    def test_missing_independent_review_object(self):
        del self.evidence["independent_reviews"]["A1-000"]
        self.assert_blocked()

    def test_review_not_independent(self):
        self.evidence["independent_reviews"]["A1-000"]["myanmar"]["independent_of_author"] = False
        self.assert_blocked()

    def test_review_source_http_not_https(self):
        self.evidence["independent_reviews"]["A1-000"]["cefr"]["source_url"] = "http://example.org/sense"
        self.assert_blocked()

    def test_review_source_credentials_rejected(self):
        self.evidence["independent_reviews"]["A1-000"]["cefr"]["source_url"] = "https://user:password@example.org/sense"
        self.assert_blocked()

    def test_missing_source_sense(self):
        del self.evidence["independent_reviews"]["A1-000"]["cefr"]["source_sense"]
        self.assert_blocked()

    def test_missing_observation_timestamp(self):
        del self.evidence["independent_reviews"]["A1-000"]["cefr"]["source_observed_at"]
        self.assert_blocked()

    def test_missing_audio_clip(self):
        del self.evidence["audio"]["A1-000"]["emma_headword"]
        self.assert_blocked()

    def test_audio_not_listened(self):
        self.evidence["audio"]["A1-000"]["george_example"]["listening_passed"] = False
        self.assert_blocked()

    def test_missing_listener_identity(self):
        del self.evidence["audio"]["A1-000"]["emma_example"]["listener_id"]
        self.assert_blocked()

    def test_audio_digest_not_hex(self):
        self.evidence["audio"]["A1-000"]["emma_headword"]["asset_sha256"] = "g" * 64
        self.assert_blocked()

    def test_duplicate_cross_level_sense(self):
        first = self.manifest["entries"][0]
        other = self.manifest["entries"][200]
        for field in ("word", "part_of_speech", "sense_id"):
            other[field] = first[field]
        self.assert_blocked()

    def test_wrong_level_count(self):
        self.manifest["entries"][0]["level"] = "A2"
        self.assert_blocked()

    def test_unapproved_entry(self):
        self.manifest["entries"][0]["release_approved"] = False
        self.assert_blocked()

    def test_editorial_hold_uncleared(self):
        self.manifest["entries"][0]["editorial_hold"] = True
        self.assert_blocked()

    def test_missing_physical_iphone_evidence(self):
        del self.evidence["release_gates"]["physical_iphone_safari"]
        self.assert_blocked()

    def test_missing_production_preservation_evidence(self):
        del self.evidence["release_gates"]["production_asset_preservation"]
        self.assert_blocked()

    def test_failed_privacy_gate(self):
        self.evidence["release_gates"]["privacy_review"]["passed"] = False
        self.assert_blocked()

    def test_extra_ci_level_job(self):
        self.evidence["parallel_cefr_ci"]["jobs"]["C2"] = {"conclusion": "success", "logs_url": "https://example.org/log"}
        self.assert_blocked()


if __name__ == "__main__":
    unittest.main()
