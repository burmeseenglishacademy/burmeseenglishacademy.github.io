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

    def test_cross_level_duplicate_detected_in_filtered_matrix_job(self):
        data = json.loads(json.dumps(self.shortlist))
        a1 = next(e for e in data["entries"] if e["level"] == "A1")
        b1 = next(e for e in data["entries"] if e["level"] == "B1")
        b1["word"], b1["part_of_speech"] = a1["word"], a1["part_of_speech"]
        for level in ("A1", "B1", "C1"):
            with self.subTest(level=level):
                p, output = self.run_gate(data, None, "--level", level)
                self.assertNotEqual(p.returncode, 0, output)
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

    def test_forged_review_flags_fail_in_unrelated_level_job(self):
        data = json.loads(json.dumps(self.shortlist))
        a1 = next(e for e in data["entries"] if e["level"] == "A1")
        a1["reviewed_english"] = True
        a1["release_approved"] = True
        p, output = self.run_gate(data, None, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("provisional reviewed_english must be explicitly false", output)
        self.assertIn("provisional release_approved must be explicitly false", output)

    def test_forged_approval_summary_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        data["independently_approved_by_level"]["B2"] = 1
        p, output = self.run_gate(data, None, "--level", "A1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("independent approval metadata must remain zero", output)

    def test_missing_review_flag_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        data["entries"][0].pop("reviewed_burmese")
        p, output = self.run_gate(data)
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("provisional reviewed_burmese must be explicitly false", output)

    def test_missing_myanmar_field_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        data["entries"][0]["burmese_meaning"] = ""
        p, output = self.run_gate(data, None, "--level", "A1")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("missing burmese_meaning", output)


    def test_unrelated_level_missing_myanmar_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        a1 = next(e for e in data["entries"] if e["level"] == "A1")
        a1["burmese_meaning"] = ""
        p, output = self.run_gate(data, None, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("missing burmese_meaning", output)

    def test_unrelated_level_editorial_hold_fails(self):
        data = json.loads(json.dumps(self.shortlist))
        a1 = next(e for e in data["entries"] if e["level"] == "A1")
        a1["editorial_hold"] = False
        p, output = self.run_gate(data, None, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("must remain held", output)

    def test_unrelated_level_review_mapping_fails(self):
        data = json.loads(json.dumps(self.tasks))
        a1 = next(e for e in data["tasks"] if e["level"] == "A1")
        a1["headword"] = "invented-nonexistent-headword"
        p, output = self.run_gate(None, data, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("shortlist/review task mapping differs", output)

    def test_forged_independent_task_signoff_rejected_by_other_level(self):
        data = json.loads(json.dumps(self.tasks))
        task = next(t for t in data["tasks"] if t["level"] == "A1")
        task["reviewer_identity"] = "invented-reviewer"
        task["reviewer_signed_at"] = "2026-11-18T12:00:00Z"
        task["approval"] = True
        task["english_definition_review"] = "APPROVED"
        p, output = self.run_gate(None, data, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("approval must be explicitly false", output)
        self.assertIn("unverified reviewer_identity", output)

    def test_forged_source_evidence_rejected(self):
        data = json.loads(json.dumps(self.tasks))
        data["tasks"][0]["source_evidence_urls"] = ["https://example.org/unsupported"]
        data["tasks"][0]["source_observed_on"] = "2026-11-18"
        p, output = self.run_gate(None, data, "--level", "B2")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("unverified source_evidence_urls", output)

    def test_per_task_source_index_mismatch_rejected(self):
        data = json.loads(json.dumps(self.tasks))
        data["tasks"][0]["source_index"] = 999999
        p, output = self.run_gate(None, data, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("source provenance differs", output)

    def test_per_task_shortlist_sha_mismatch_rejected(self):
        data = json.loads(json.dumps(self.tasks))
        data["tasks"][0]["shortlist_blob_sha"] = "0" * 40
        p, output = self.run_gate(None, data, "--level", "B1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("shortlist blob provenance mismatch", output)


    def test_forged_duplicate_review_task_id_fails_in_unrelated_level(self):
        data = json.loads(json.dumps(self.tasks))
        data["tasks"][1]["task_id"] = data["tasks"][0]["task_id"]
        p, output = self.run_gate(None, data, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("duplicate task_id", output)
        self.assertIn("expected immutable sequential task_id", output)

    def test_global_review_ids_remain_stable_across_level_boundaries(self):
        # Original task IDs are globally numbered: A2 starts at 0201,
        # not 0001. The unmodified inventory must pass every matrix level.
        self.assertEqual(self.tasks["tasks"][200]["task_id"], "CEFR1000-A2-0201")
        self.assertEqual(self.tasks["tasks"][400]["task_id"], "CEFR1000-B1-0401")
        for level in ("A1", "A2", "B1", "B2", "C1"):
            with self.subTest(level=level):
                p, output = self.run_gate(None, None, "--level", level)
                self.assertEqual(p.returncode, 0, output)

    def test_per_level_restarted_review_id_rejected(self):
        data = json.loads(json.dumps(self.tasks))
        data["tasks"][200]["task_id"] = "CEFR1000-A2-0001"
        p, output = self.run_gate(None, data, "--level", "C1")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("expected immutable sequential task_id CEFR1000-A2-0201", output)

    def test_boolean_source_index_fails(self):
        data = json.loads(json.dumps(self.tasks))
        data["tasks"][0]["source_index"] = True
        p, output = self.run_gate(None, data, "--level", "B2")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("source_index must be a nonnegative integer", output)

    def test_forged_release_status_fails(self):
        data = json.loads(json.dumps(self.tasks))
        data["release_status"] = "APPROVED_FOR_PUBLICATION"
        p, output = self.run_gate(None, data, "--level", "A2")
        self.assertNotEqual(p.returncode, 0, output)
        self.assertIn("do-not-publish release status", output)


if __name__ == "__main__":
    unittest.main()
