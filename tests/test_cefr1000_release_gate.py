#!/usr/bin/env python3
"""Adversarial, offline, fail-closed smoke tests for the CEFR-1000 release gate.

These tests use synthetic records only. They DO NOT constitute independent review,
audio listening, device QA, or a release certification.
Run: python3 -m unittest discover -s tests -p 'test_cefr1000_release_gate.py'
"""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cefr_gate", ROOT / "scripts" / "cefr1000_release_gate.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def synthetic():
    entries = []
    reviews = {}
    audio = {}
    for level in gate.LEVELS:
        for n in range(200):
            uid = f"{level}-{n:03d}"
            entries.append(dict(id=uid, word=f"synthetic-{uid}", level=level,
                                part_of_speech="noun", sense_id="1",
                                english_definition="Synthetic test only",
                                burmese_meaning="စမ်းသပ်မှု", example_sentence="This is a test.",
                                release_approved=True, editorial_hold=False))
            reviews[uid] = {field: dict(reviewer_id="synthetic-other", reviewed_at="2026-11-04",
                        source_url="https://example.org/synthetic", source_observed_at="2026-11-04",
                        source_sense="synthetic", evidence_reference="synthetic",
                        approved=True, independent_of_author=True) for field in gate.FIELDS}
            audio[uid] = {f"{voice}_{kind}": dict(asset_path="synthetic.wav",
                         asset_sha256="synthetic-not-a-hash", listener_id="synthetic",
                         listened_at="2026-11-04", listening_evidence="synthetic",
                         listening_passed=True) for voice in gate.VOICES for kind in gate.KINDS}
    gates = {name: dict(passed=True, evidence_url="https://example.org/synthetic",
                       verified_at="2026-11-04") for name in (
        "browser_regression", "mobile_regression", "physical_iphone_safari",
        "github_pages_limits", "production_deployment", "production_asset_preservation",
        "privacy_review")}
    return {"entries": entries}, {"independent_reviews": reviews, "audio": audio, "release_gates": gates}


class ReleaseGateAdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = synthetic()
        assert not gate.check(*cls.baseline), "Synthetic baseline schema must be structurally valid"

    def case(self):
        import copy
        return copy.deepcopy(self.baseline)

    def blocked(self, manifest, evidence):
        self.assertTrue(gate.check(manifest, evidence))

    def test_missing_independent_review(self):
        m, e = self.case()
        del e["independent_reviews"]["A1-000"]["cefr"]
        self.blocked(m, e)

    def test_false_independence(self):
        m, e = self.case()
        e["independent_reviews"]["A1-000"]["myanmar"]["independent_of_author"] = False
        self.blocked(m, e)

    def test_missing_listening(self):
        m, e = self.case()
        e["audio"]["A1-000"]["emma_example"]["listening_passed"] = False
        self.blocked(m, e)

    def test_missing_physical_iphone(self):
        m, e = self.case()
        del e["release_gates"]["physical_iphone_safari"]
        self.blocked(m, e)

    def test_duplicate_cross_level_sense(self):
        m, e = self.case()
        m["entries"][200]["word"] = m["entries"][0]["word"]
        self.blocked(m, e)

    def test_missing_entry(self):
        m, e = self.case()
        m["entries"].pop()
        self.blocked(m, e)

    def test_provisional_hold(self):
        m, e = self.case()
        m["entries"][0]["editorial_hold"] = True
        m["entries"][0]["release_approved"] = False
        self.blocked(m, e)

    def test_unexpected_review_id(self):
        m, e = self.case()
        e["independent_reviews"]["forged-extra"] = e["independent_reviews"]["A1-000"]
        self.blocked(m, e)

    def test_missing_source_observation(self):
        m, e = self.case()
        e["independent_reviews"]["C1-199"]["cefr"]["source_observed_at"] = ""
        self.blocked(m, e)

    def test_missing_production_preservation(self):
        m, e = self.case()
        e["release_gates"]["production_asset_preservation"]["passed"] = False
        self.blocked(m, e)


if __name__ == "__main__":
    unittest.main()
