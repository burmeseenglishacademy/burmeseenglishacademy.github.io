#!/usr/bin/env python3
"""Adversarial structural tests for CEFR-1000 release gate.

These tests use SYNTHETIC records, not learner content or real approvals.
A passing test never establishes editorial, listening, device or deployment signoff.
Run: python3 -m unittest discover -s tests -p 'test_cefr1000_release_adversarial.py'
"""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cefr1000_release_gate import check

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("english", "myanmar", "example", "cefr")
VOICES = ("george", "emma")
KINDS = ("headword", "example")


def synthetic_valid():
    entries, reviews, audio = [], {}, {}
    for level in LEVELS:
        for i in range(200):
            uid = f"synthetic-{level}-{i:03d}"
            entries.append(dict(id=uid, level=level, word=uid, part_of_speech="noun",
                                sense_id="synthetic-sense", english_definition="Synthetic meaning.",
                                burmese_meaning="စမ်းသပ်ရန်", example_sentence="This is a synthetic test.",
                                release_approved=True, editorial_hold=False))
            reviews[uid] = {
                field: dict(reviewer_id="SYNTHETIC-INDEPENDENT-REVIEWER",
                            reviewed_at="2026-11-09", source_url="https://example.org/placeholder",
                            source_observed_at="2026-11-09", source_sense="synthetic",
                            evidence_reference="SYNTHETIC", approved=True,
                            independent_of_author=True)
                for field in FIELDS
            }
            audio[uid] = {
                f"{voice}_{kind}": dict(asset_path="synthetic.wav", asset_sha256="a" * 64,
                                        listener_id="SYNTHETIC-LISTENER", listened_at="2026-11-09",
                                        listening_evidence="SYNTHETIC", listening_passed=True)
                for voice in VOICES for kind in KINDS
            }
    gates = {gate: dict(passed=True, evidence_url="https://example.org/placeholder",
                        verified_at="2026-11-09") for gate in
             ("browser_regression", "mobile_regression", "physical_iphone_safari",
              "github_pages_limits", "production_deployment",
              "production_asset_preservation", "privacy_review")}
    return {"entries": entries}, {"independent_reviews": reviews, "audio": audio, "release_gates": gates}


class FailClosedAdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.evidence = synthetic_valid()

    def assert_blocked(self, change):
        manifest = copy.deepcopy(self.manifest)
        evidence = copy.deepcopy(self.evidence)
        change(manifest, evidence)
        self.assertTrue(check(manifest, evidence), "unsafe mutation passed release gate")

    def test_synthetic_fixture_structurally_passes(self):
        # Deliberately proves the gate cannot authenticate reviewer identities or URLs.
        self.assertEqual(check(self.manifest, self.evidence), [])

    def test_missing_level_entry(self):
        self.assert_blocked(lambda m, e: m["entries"].pop())

    def test_duplicate_across_levels(self):
        def mutate(m, e):
            m["entries"][200]["word"] = m["entries"][0]["word"]
        self.assert_blocked(mutate)

    def test_missing_sense(self):
        self.assert_blocked(lambda m, e: m["entries"][0].pop("sense_id"))

    def test_editorial_hold(self):
        self.assert_blocked(lambda m, e: m["entries"][0].update(editorial_hold=True))

    def test_unapproved_entry(self):
        self.assert_blocked(lambda m, e: m["entries"][0].update(release_approved=False))

    def test_missing_independent_cefr_review(self):
        self.assert_blocked(lambda m, e: e["independent_reviews"]["synthetic-A1-000"].pop("cefr"))

    def test_reviewer_independence_not_attested(self):
        self.assert_blocked(lambda m, e: e["independent_reviews"]["synthetic-A1-000"]["myanmar"].update(independent_of_author=False))

    def test_unsubstantiated_cefr_source(self):
        self.assert_blocked(lambda m, e: e["independent_reviews"]["synthetic-A1-000"]["cefr"].update(source_url=""))

    def test_missing_emma_example_audio(self):
        self.assert_blocked(lambda m, e: e["audio"]["synthetic-A1-000"].pop("emma_example"))

    def test_audio_not_listened(self):
        self.assert_blocked(lambda m, e: e["audio"]["synthetic-A1-000"]["george_headword"].update(listening_passed=False))

    def test_invalid_audio_hash(self):
        self.assert_blocked(lambda m, e: e["audio"]["synthetic-A1-000"]["george_headword"].update(asset_sha256="unverified"))

    def test_physical_iphone_not_signed_off(self):
        self.assert_blocked(lambda m, e: e["release_gates"]["physical_iphone_safari"].update(passed=False))

    def test_production_preservation_not_signed_off(self):
        self.assert_blocked(lambda m, e: e["release_gates"].pop("production_asset_preservation"))

    def test_hosting_evidence_missing(self):
        self.assert_blocked(lambda m, e: e["release_gates"]["github_pages_limits"].update(evidence_url=""))


if __name__ == "__main__":
    unittest.main()
