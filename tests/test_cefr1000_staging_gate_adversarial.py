"""Adversarial tests for the fail-closed CEFR-1000 staging gate.

Operate on disposable copies; never mutate source JSON or approval flags.
These tests certify structural rejection only, not independent editorial review.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHORTLIST = "CEFR-1000-PROVISIONAL-SHORTLIST.json"
TASKS = "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"


class StagingGateAdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="cefr1000-gate-")
        cls.root = pathlib.Path(cls.tmp.name)
        (cls.root / "draft").mkdir()
        (cls.root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/cefr1000_staging_gate.py", cls.root / "scripts")
        cls.shortlist = json.loads((ROOT / "draft" / SHORTLIST).read_text(encoding="utf-8"))
        cls.tasks = json.loads((ROOT / "draft" / TASKS).read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def run_gate(self, shortlist=None, tasks=None, *args):
        (self.root / "draft" / SHORTLIST).write_text(
            json.dumps(self.shortlist if shortlist is None else shortlist, ensure_ascii=False), encoding="utf-8"
        )
        (self.root / "draft" / TASKS).write_text(
            json.dumps(self.tasks if tasks is None else tasks, ensure_ascii=False), encoding="utf-8"
        )
        p = subprocess.run(
            [sys.executable, str(self.root / "scripts/cefr1000_staging_gate.py"), *args],
            capture_output=True, text=True, check=False
        )
        return p, p.stdout + p.stderr

    def test_unmodified_provisional_inventory_passes_structure(self):
        p, output = self.run_gate()
        self.assertEqual(p.returncode, 0, output)
        self.assertIn('"independent_approval_inferred": false', output)

    def test_release_always_fails_without_external_signoffs(self):
        p, output = self.run_gate(None, None, "--release")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("RELEASE BLOCKED", output)

    def test_missing_level_entry_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        data["entries"].pop(0)
        p, output = self.run_gate(data)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("expected exactly 200 per level", output)

    def test_cross_level_duplicate_headword_pos_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        a1 = next(e for e in data["entries"] if e["level"] == "A1")
        b1 = next(e for e in data["entries"] if e["level"] == "B1")
        b1["word"], b1["part_of_speech"] = a1["word"], a1["part_of_speech"]
        p, output = self.run_gate(data)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("duplicate headword/part-of-speech", output)

    def test_unheld_entry_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        data["entries"][0]["editorial_hold"] = False
        p, output = self.run_gate(data, None, "--level", "A1")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("must remain held", output)

    def test_task_provenance_change_fails(self):
        data = json.loads(json.dumps(self.tasks))
        data["source_shortlist_blob_sha"] = "0" * 40
        p, output = self.run_gate(None, data)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("provenance changed", output)

    def test_missing_myanmar_field_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        data["entries"][0]["burmese_meaning"] = ""
        p, output = self.run_gate(data, None, "--level", "A1")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("missing burmese_meaning", output)


if __name__ == "__main__":
    unittest.main()
