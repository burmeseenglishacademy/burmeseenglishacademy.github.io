#!/usr/bin/env python3
"""Adversarial tests for CEFR-1000 staging checker; never modify the inventory."""
import copy
import importlib.util
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/cefr1000_staging_check.py"
spec = importlib.util.spec_from_file_location("cefr_checker", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
ORIGINAL = json.loads(checker.SOURCE.read_text(encoding="utf-8"))


def evaluate(data, level="A1", release=False):
    with tempfile.TemporaryDirectory() as folder:
        path = pathlib.Path(folder) / "inventory.json"
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        with patch.object(checker, "SOURCE", path):
            return checker.check(level, release)[0]


class StagingGateTests(unittest.TestCase):
    def test_baseline_structural_all_levels(self):
        for level in checker.LEVELS:
            with self.subTest(level=level):
                self.assertEqual(evaluate(ORIGINAL, level), [])

    def test_release_fails_closed_all_levels(self):
        for level in checker.LEVELS:
            with self.subTest(level=level):
                self.assertTrue(evaluate(ORIGINAL, level, True))

    def test_cross_level_duplicate_detected_everywhere(self):
        data = copy.deepcopy(ORIGINAL)
        a1 = next(e for e in data["entries"] if e["level"] == "A1")
        c1 = next(e for e in data["entries"] if e["level"] == "C1")
        c1["word"] = a1["word"]
        c1["part_of_speech"] = a1["part_of_speech"]
        for level in checker.LEVELS:
            self.assertTrue(any("cross-level duplicate" in e for e in evaluate(data, level)))

    def test_unicode_compatibility_duplicate_detected(self):
        data = copy.deepcopy(ORIGINAL)
        first = next(e for e in data["entries"] if e["level"] == "A1")
        last = next(e for e in data["entries"] if e["level"] == "C1")
        # Fullwidth Latin letters normalize to ordinary Latin under NFKC.
        last["word"] = "".join(chr(ord(ch) + 0xFEE0) if "!" <= ch <= "~" else ch for ch in first["word"])
        last["part_of_speech"] = first["part_of_speech"]
        for level in checker.LEVELS:
            self.assertTrue(any("cross-level duplicate" in error for error in evaluate(data, level)))

    def test_spacing_alias_duplicate_detected(self):
        data = copy.deepcopy(ORIGINAL)
        first = next(e for e in data["entries"] if e["level"] == "A1")
        last = next(e for e in data["entries"] if e["level"] == "C1")
        last["word"] = "  " + first["word"].upper() + "  "
        last["part_of_speech"] = first["part_of_speech"]
        self.assertTrue(any("cross-level duplicate" in error for error in evaluate(data)))

    def test_forged_approval_rejected(self):
        data = copy.deepcopy(ORIGINAL)
        data["entries"][0]["release_approved"] = True
        for level in checker.LEVELS:
            self.assertTrue(evaluate(data, level))

    def test_reused_provenance_rejected(self):
        data = copy.deepcopy(ORIGINAL)
        first = data["entries"][0]
        second = data["entries"][1]
        for field in ("source_path", "source_blob_sha", "source_index"):
            second[field] = first[field]
        self.assertTrue(any("reused provenance" in e for e in evaluate(data)))

    def test_invalid_boolean_rejected(self):
        data = copy.deepcopy(ORIGINAL)
        data["entries"][0]["reviewed_english"] = "false"
        self.assertTrue(any("JSON boolean" in e for e in evaluate(data)))

    def test_count_mismatch_rejected(self):
        data = copy.deepcopy(ORIGINAL)
        data["entries"].pop()
        self.assertTrue(any("expected 1000" in e for e in evaluate(data)))


if __name__ == "__main__":
    unittest.main()
