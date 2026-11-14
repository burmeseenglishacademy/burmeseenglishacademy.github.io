#!/usr/bin/env python3
"""Negative tests for the provisional CEFR-1000 audit. Staging-only, read-only."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from cefr1000_provisional_fail_closed_audit import audit

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
          "reviewed_level", "reviewed_pronunciation")


def fixture():
    entries = []
    for level in LEVELS:
        for n in range(200):
            entries.append({
                "level": level, "word": f"{level}_word_{n}",
                "part_of_speech": "noun", "english_definition": "An illustrative item.",
                "burmese_meaning": "နမူနာ", "example_sentence": "This is an example.",
                "source_path": "draft/source.json", "source_blob_sha": "a" * 40,
                "source_index": n, "editorial_hold": True,
                "release_approved": False, "status": "PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING", **{field: False for field in FIELDS}
            })
    return {
        "schema": 1,
        "release_status": "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
        "scope_target": {level: 200 for level in LEVELS},
        "counts_by_level": {level: 200 for level in LEVELS},
        "independently_approved_by_level": {level: 0 for level in LEVELS},
        "stages": {"production": "UNMODIFIED",
                   "english_definitions": "FIRST_PASS_UNVERIFIED",
                   "myanmar_meanings": "FIRST_PASS_UNVERIFIED",
                   "original_examples": "FIRST_PASS_UNVERIFIED",
                   "independent_source_evidence": "NOT_OBSERVED",
                   "audio": "NOT_GENERATED_FOR_FINAL_SHORTLIST_NOT_LISTENED"},
        "entries": entries
    }


def inspect(data):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "shortlist.json"
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = audit(path)
        return status, output.getvalue()


class ProvisionalAuditNegativeTests(unittest.TestCase):
    def test_complete_provisional_inventory_still_blocks_release(self):
        code, output = inspect(fixture())
        self.assertEqual(code, 1)
        self.assertIn("RELEASE BLOCKED", output)
        self.assertIn("Structural findings: 0", output)

    def test_tampered_metadata_detected(self):
        for field in ("scope_target", "counts_by_level", "independently_approved_by_level"):
            with self.subTest(field=field):
                data = fixture()
                data[field]["A1"] = True
                _, output = inspect(data)
                self.assertIn(field, output)

    def test_missing_production_preservation_detected(self):
        data = fixture()
        data["stages"]["production"] = "DEPLOYED"
        _, output = inspect(data)
        self.assertIn("production preservation stage", output)

    def test_invalid_source_sha_detected(self):
        data = fixture()
        data["entries"][0]["source_blob_sha"] = "not-a-sha"
        _, output = inspect(data)
        self.assertIn("invalid source_blob_sha", output)

    def test_negative_source_index_detected(self):
        data = fixture()
        data["entries"][0]["source_index"] = -1
        _, output = inspect(data)
        self.assertIn("invalid source_index", output)

    def test_status_tampering_detected(self):
        data = fixture()
        data["entries"][0]["status"] = "APPROVED"
        _, output = inspect(data)
        self.assertIn("provisional status missing or altered", output)

    def test_audio_stage_tampering_detected(self):
        data = fixture()
        data["stages"]["audio"] = "COMPLETE"
        _, output = inspect(data)
        self.assertIn("stage audio", output)

    def test_string_review_flag_rejected(self):
        data = fixture()
        data["entries"][0]["reviewed_english"] = "false"
        _, output = inspect(data)
        self.assertIn("must be an explicit JSON boolean", output)

    def test_null_release_approval_rejected(self):
        data = fixture()
        data["entries"][0]["release_approved"] = None
        _, output = inspect(data)
        self.assertIn("release_approved must be an explicit JSON boolean", output)

    def test_missing_entry_detected(self):
        data = fixture()
        data["entries"].pop()
        _, output = inspect(data)
        self.assertIn("C1: expected 200 entries, found 199", output)
        self.assertIn("expected 1000 entries, found 999", output)

    def test_case_only_collision_detected(self):
        data = fixture()
        data["entries"][1]["word"] = data["entries"][0]["word"].upper()
        _, output = inspect(data)
        self.assertIn("duplicate normalized headword", output)

    def test_unicode_nfkc_collision_detected(self):
        data = fixture()
        data["entries"][0]["word"] = "ＡＢＣ"
        data["entries"][1]["word"] = "abc"
        _, output = inspect(data)
        self.assertIn("duplicate normalized headword", output)

    def test_bare_approval_rejected(self):
        data = fixture()
        data["entries"][0]["release_approved"] = True
        _, output = inspect(data)
        self.assertIn("release_approved flag is insufficient", output)

    def test_bare_independent_review_flags_rejected(self):
        for field in FIELDS:
            with self.subTest(field=field):
                data = fixture()
                data["entries"][0][field] = True
                _, output = inspect(data)
                self.assertIn("bare review flag(s)", output)

    def test_editorial_hold_removal_rejected(self):
        data = fixture()
        data["entries"][0]["editorial_hold"] = False
        _, output = inspect(data)
        self.assertIn("editorial hold removed", output)

    def test_missing_myanmar_detected(self):
        data = fixture()
        data["entries"][0]["burmese_meaning"] = ""
        _, output = inspect(data)
        self.assertIn("missing burmese_meaning", output)

    def test_bool_source_index_rejected(self):
        data = fixture()
        data["entries"][0]["source_index"] = True
        _, output = inspect(data)
        self.assertIn("invalid source_index", output)

    def test_invalid_level_detected(self):
        data = fixture()
        data["entries"][0]["level"] = "C2"
        _, output = inspect(data)
        self.assertIn("invalid level", output)


if __name__ == "__main__":
    unittest.main()
