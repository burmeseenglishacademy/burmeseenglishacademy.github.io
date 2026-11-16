"""Fail-closed regression tests for the CEFR-1000 release gate.

These tests verify structural rejection only. They cannot authenticate a human
reviewer, listening session, physical device, or hosted production deployment.
"""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cefr1000_release_gate", ROOT / "scripts" / "cefr1000_release_gate.py"
)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class ReleaseGateFailClosedTests(unittest.TestCase):
    def test_provisional_shortlist_cannot_be_released_with_empty_evidence(self):
        import json
        shortlist = json.loads(
            (ROOT / "draft" / "CEFR-1000-PROVISIONAL-SHORTLIST.json").read_text(encoding="utf-8")
        )
        failures = gate.check(shortlist, {})
        self.assertTrue(failures)
        self.assertTrue(any("release-approved" in str(item) for item in failures))
        self.assertTrue(any("independent_reviews" in str(item) for item in failures))
        self.assertTrue(any("physical_iphone_safari" in str(item) for item in failures))
        self.assertTrue(any("production_deployment" in str(item) for item in failures))

    def test_missing_manifest_entries_fail_closed(self):
        self.assertTrue(gate.check({"entries": []}, {}))

    def test_non_object_manifest_fails_closed(self):
        self.assertTrue(gate.check(None, {}))

    def test_evidence_urls_must_be_https_without_credentials(self):
        for url in ("http://example.org/evidence", "https://user:pass@example.org/x",
                    "https://", "https://example.org/has space", "", None):
            with self.subTest(url=url):
                self.assertFalse(gate.https_evidence_url(url))

    def test_listening_timestamps_require_timezone(self):
        for timestamp in ("2026-11-17T01:00:00", "yesterday", "", None):
            with self.subTest(timestamp=timestamp):
                self.assertFalse(gate.iso_timestamp(timestamp))
        self.assertTrue(gate.iso_timestamp("2026-11-17T01:00:00+08:00"))

    def test_audio_paths_reject_traversal_and_remote_urls(self):
        for path in ("../private.mp3", "/tmp/private.mp3", "https://example.org/x.mp3",
                     r"audio\\escape.mp3", "", None):
            with self.subTest(path=path):
                self.assertFalse(gate.safe_relative_asset_path(path))

    def test_audio_digest_requires_64_hex_characters(self):
        self.assertFalse(gate.sha256_hex("0" * 63))
        self.assertFalse(gate.sha256_hex("z" * 64))
        self.assertTrue(gate.sha256_hex("a" * 64))


if __name__ == "__main__":
    unittest.main()
