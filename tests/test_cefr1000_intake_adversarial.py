"""Adversarial intake regression tests; never confer editorial approval."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cefr1000_intake_audit", ROOT / "scripts/audit_cefr1000_review_intake.py"
)
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)


class IndependentReviewIntakeRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = (ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json").read_bytes()
        cls.sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()
        cls.shortlist = json.loads(raw)
        cls.intake = json.loads(
            (ROOT / "draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json").read_text(encoding="utf-8")
        )

    def check_mutation_rejected(self, mutate):
        shortlist = copy.deepcopy(self.shortlist)
        intake = copy.deepcopy(self.intake)
        mutate(shortlist, intake)
        self.assertTrue(audit_module.audit(shortlist, intake, self.sha))

    def test_current_intake_is_structurally_consistent_but_not_approved(self):
        self.assertEqual(audit_module.audit(self.shortlist, self.intake, self.sha), [])
        self.assertEqual(self.intake["independently_approved_by_level"], dict.fromkeys(audit_module.LEVELS, 0))

    def test_rejects_cross_level_task_swap(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"].__setitem__(200, t["tasks"][0]))

    def test_rejects_duplicated_task_identifier(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"][1].__setitem__("task_id", t["tasks"][0]["task_id"]))

    def test_rejects_invalid_level(self):
        self.check_mutation_rejected(lambda s, t: s["entries"][0].__setitem__("level", "C2"))

    def test_rejects_source_provenance_mutation(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"][0].__setitem__("source_index", 99999))

    def test_rejects_forged_approval(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"][0].__setitem__("approval", True))

    def test_rejects_forged_reviewer_identity(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"][0].__setitem__("reviewer_identity", "self-certified"))

    def test_rejects_forged_source_url(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"][0].__setitem__("source_evidence_urls", ["https://example.org"]))

    def test_rejects_missing_task(self):
        self.check_mutation_rejected(lambda s, t: t["tasks"].pop())

    def test_rejects_wrong_shortlist_blob(self):
        self.check_mutation_rejected(lambda s, t: t.__setitem__("source_shortlist_blob_sha", "0" * 40))


if __name__ == "__main__":
    unittest.main()
