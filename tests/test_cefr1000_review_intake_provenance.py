"""Fail-closed provenance and review-intake consistency checks for CEFR-1000.

Structural checks only: never certify linguistic accuracy or independent approval.
"""
import copy
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
SHORTLIST_PATH = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
TASKS_PATH = ROOT / "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json"


def git_blob_sha(payload):
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def audit(shortlist, intake, actual_blob_sha):
    errors = []
    entries, tasks = shortlist.get("entries"), intake.get("tasks")
    if not isinstance(entries, list) or not isinstance(tasks, list):
        return ["entries and tasks must be lists"]
    if len(entries) != 1000 or len(tasks) != 1000:
        errors.append("exactly 1000 shortlist entries and 1000 review tasks required")
    if intake.get("source_shortlist_blob_sha") != actual_blob_sha:
        errors.append("intake source shortlist Git blob SHA mismatch")
    if any(x.get("independently_approved_by_level") != dict.fromkeys(LEVELS, 0)
           for x in (shortlist, intake)):
        errors.append("provisional independent approval counts must remain zero")
    if any(x.get("counts_by_level") != dict.fromkeys(LEVELS, 200)
           for x in (shortlist, intake)):
        errors.append("declared 200-per-level counts mismatch")
    seen_ids = set()
    for i, (entry, task) in enumerate(zip(entries, tasks), 1):
        if not isinstance(entry, dict) or not isinstance(task, dict):
            errors.append(f"row {i}: invalid record type")
            continue
        level = entry.get("level")
        expected_id = f"CEFR1000-{level}-{i:04d}"
        if task.get("task_id") != expected_id or expected_id in seen_ids:
            errors.append(f"row {i}: task ID mismatch or duplicate")
        seen_ids.add(expected_id)
        for field, counterpart in (("level", "level"), ("word", "headword"),
                                   ("part_of_speech", "part_of_speech"),
                                   ("source_path", "source_path"),
                                   ("source_index", "source_index"),
                                   ("source_blob_sha", "source_blob_sha")):
            if entry.get(field) != task.get(counterpart):
                errors.append(f"row {i}: {field} provenance mismatch")
        if task.get("shortlist_blob_sha") != actual_blob_sha:
            errors.append(f"row {i}: task shortlist blob SHA mismatch")
        if task.get("review_status") != "PENDING_INDEPENDENT_REVIEW":
            errors.append(f"row {i}: unexpected review status")
        if task.get("approval") is not False or task.get("reviewer_identity") is not None or task.get("reviewer_signed_at") is not None:
            errors.append(f"row {i}: unsupported approval or reviewer signoff")
        for field in ("english_definition_review", "myanmar_meaning_review",
                      "original_example_review", "exact_sense_cefr_review",
                      "pronunciation_review"):
            if task.get(field) != "PENDING":
                errors.append(f"row {i}: {field} must be pending")
        if task.get("source_evidence_urls") != [] or task.get("source_observed_on") is not None:
            errors.append(f"row {i}: unexpected evidence claims in administrative intake")
    return errors


class ReviewIntakeProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = SHORTLIST_PATH.read_bytes()
        cls.shortlist = json.loads(cls.raw)
        cls.intake = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
        cls.sha = git_blob_sha(cls.raw)

    def test_baseline_consistent_but_not_approved(self):
        self.assertEqual(audit(self.shortlist, self.intake, self.sha), [])

    def test_wrong_shortlist_sha_fails(self):
        self.assertTrue(audit(self.shortlist, self.intake, "0" * 40))

    def test_reordered_tasks_fail(self):
        data = copy.deepcopy(self.intake)
        data["tasks"][0], data["tasks"][1] = data["tasks"][1], data["tasks"][0]
        self.assertTrue(audit(self.shortlist, data, self.sha))

    def test_changed_source_index_fails(self):
        data = copy.deepcopy(self.intake)
        data["tasks"][0]["source_index"] = -1
        self.assertTrue(any("provenance mismatch" in e for e in audit(self.shortlist, data, self.sha)))

    def test_fake_reviewer_signoff_fails(self):
        data = copy.deepcopy(self.intake)
        data["tasks"][0]["reviewer_identity"] = "fabricated"
        self.assertTrue(any("unsupported approval" in e for e in audit(self.shortlist, data, self.sha)))

    def test_incomplete_task_list_fails(self):
        data = copy.deepcopy(self.intake)
        data["tasks"].pop()
        self.assertTrue(any("exactly 1000" in e for e in audit(self.shortlist, data, self.sha)))


if __name__ == "__main__":
    unittest.main()
