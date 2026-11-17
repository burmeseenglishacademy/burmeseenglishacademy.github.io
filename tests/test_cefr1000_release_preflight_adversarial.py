"""Adversarial schema tests for CEFR-1000 release preflight (not authenticity tests).

Synthetic positive fixtures only test structural acceptance; they are NEVER
reviewer signoff, audio listening evidence, or production release authorization.
"""
import json
import tempfile
import unittest
from pathlib import Path
from copy import deepcopy
from scripts.cefr1000_release_preflight import audit

LEVELS = ("A1", "A2", "B1", "B2", "C1")
GATES = ("desktop_browser", "mobile_browser", "physical_iphone_safari",
         "github_pages_limits", "production_deployment",
         "production_assets_preserved", "privacy_protection")
FIELDS = ("english", "myanmar", "example", "exact_sense_cefr", "pronunciation")

def fixture():
    entries, reviews = [], []
    for level in LEVELS:
        for i in range(200):
            ident = f"{level}-{i:03d}"
            entries.append({
                "entry_id": ident, "level": level, "word": f"synthetic-{ident}",
                "part_of_speech": "noun", "sense_id": "1",
                "audio": {voice: {kind: {
                    "asset_path": f"synthetic/{ident}/{voice}/{kind}.wav",
                    "sha256": "synthetic-not-a-real-hash",
                    "listened_by": "synthetic-not-a-reviewer",
                    "listened_at": "synthetic-not-a-date"
                } for kind in ("headword", "example")}
                          for voice in ("george", "emma")}
            })
            reviews.append({"entry_id": ident, **{field: {
                "decision": "approved", "reviewer_id": "synthetic",
                "signed_at": "synthetic", "source_url": "synthetic",
                "observed_on": "synthetic"
            } for field in FIELDS}})
    qa = {gate: {"passed": True, "evidence_url": "synthetic",
                 "verified_by": "synthetic", "verified_at": "synthetic"}
          for gate in GATES}
    return {"entries": entries}, {"reviews": reviews}, qa

class PreflightAdversarialTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "release").mkdir()
        self.manifest, self.evidence, self.qa = fixture()

    def write(self):
        for name, data in (
            ("cefr1000-approved-manifest.json", self.manifest),
            ("cefr1000-independent-evidence.json", self.evidence),
            ("cefr1000-release-qa.json", self.qa),
        ):
            (self.root / "release" / name).write_text(
                json.dumps(data), encoding="utf-8")

    def assert_blocked(self, needle):
        self.write()
        errors = audit(self.root)
        self.assertTrue(any(needle in e for e in errors), errors[:5])

    def test_missing_release_files_block(self):
        self.assertIn("missing independent release artifact", audit(self.root)[0])

    def test_missing_one_level_entry_blocks(self):
        self.manifest["entries"].pop()
        self.assert_blocked("exactly 1000")

    def test_wrong_level_distribution_blocks(self):
        self.manifest["entries"][0]["level"] = "A2"
        self.assert_blocked("incorrect level counts")

    def test_duplicate_sense_blocks(self):
        a, b = self.manifest["entries"][:2]
        b.update({k: a[k] for k in ("word", "part_of_speech", "sense_id")})
        self.assert_blocked("missing or duplicate")

    def test_missing_independent_signoff_blocks(self):
        self.evidence["reviews"][0]["myanmar"]["decision"] = "pending"
        self.assert_blocked("myanmar independent evidence/signoff missing")

    def test_missing_george_example_listening_blocks(self):
        del self.manifest["entries"][0]["audio"]["george"]["example"]["listened_at"]
        self.assert_blocked("george example audio/listening evidence missing")

    def test_missing_physical_iphone_blocks(self):
        self.qa["physical_iphone_safari"]["passed"] = False
        self.assert_blocked("physical_iphone_safari")

    def test_missing_production_preservation_blocks(self):
        del self.qa["production_assets_preserved"]
        self.assert_blocked("production_assets_preserved")

    def test_duplicate_review_id_blocks(self):
        self.evidence["reviews"][1]["entry_id"] = self.evidence["reviews"][0]["entry_id"]
        self.assert_blocked("duplicate review")

    @unittest.expectedFailure
    def test_known_limitation_fabricated_evidence_strings_must_not_pass(self):
        # Intentionally documents an unresolved authenticity gap: structurally
        # complete invented strings currently pass. Do not use this as release proof.
        self.write()
        self.assertTrue(audit(self.root),
                        "Synthetic evidence must never authorize production")

if __name__ == "__main__":
    unittest.main()
