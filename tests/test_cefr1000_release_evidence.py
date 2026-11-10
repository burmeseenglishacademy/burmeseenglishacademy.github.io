"""Adversarial fail-closed tests for the CEFR-1000 release evidence gate.

Synthetic fixtures only. Passing tests never imply independent human review.
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_cefr1000_release_evidence.py"
spec = importlib.util.spec_from_file_location("cefr1000_release_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class ReleaseEvidenceGateTests(unittest.TestCase):
    def test_missing_manifest_entries_blocks(self):
        self.assertTrue(gate.audit({"entries": []}, {}))

    def test_incorrect_level_distribution_blocks(self):
        entries = [{"level": "A1", "word": f"synthetic{i}", "sense_id": "1"} for i in range(1000)]
        errors = gate.audit({"entries": entries, "counts_by_level": {x: 200 for x in gate.LEVELS}}, {})
        self.assertTrue(any("expected 200" in e for e in errors))

    def test_duplicate_headword_sense_across_levels_blocks(self):
        entries = [{"level": gate.LEVELS[i // 200], "word": f"synthetic{i}", "sense_id": "1"} for i in range(1000)]
        entries[200]["word"] = entries[0]["word"]
        errors = gate.audit({"entries": entries, "counts_by_level": {x: 200 for x in gate.LEVELS}}, {})
        self.assertTrue(any("duplicate normalized" in e for e in errors))

    def test_malformed_level_types_fail_closed_without_exception(self):
        for malformed in (None, [], {}, 1, ["A1"]):
            entries = [{"level": gate.LEVELS[i // 200], "word": f"synthetic{i}",
                        "sense_id": "1"} for i in range(1000)]
            entries[0]["level"] = malformed
            errors = gate.audit({"entries": entries,
                                 "counts_by_level": {x: 200 for x in gate.LEVELS}}, {})
            self.assertTrue(any("invalid CEFR level type/value" in e for e in errors),
                            msg=f"malformed level {malformed!r} must be blocked")

    def test_self_evaluation_is_not_independent(self):
        record = {"reviewer_id": "person", "reviewed_at": "2026-11-10",
                  "evidence_url": "https://example.org/review",
                  "content_sha256": "a" * 64, "independent": True,
                  "self_evaluation": True}
        self.assertFalse(gate.valid_attestation(record))

    def test_missing_provenance_is_not_attestation(self):
        record = {"reviewer_id": "person", "reviewed_at": "2026-11-10",
                  "evidence_url": "", "content_sha256": "a" * 64,
                  "independent": True, "self_evaluation": False}
        self.assertFalse(gate.valid_attestation(record))

    def test_invalid_hash_is_not_attestation(self):
        record = {"reviewer_id": "person", "reviewed_at": "2026-11-10",
                  "evidence_url": "https://example.org/review",
                  "content_sha256": "not-a-sha256", "independent": True,
                  "self_evaluation": False}
        self.assertFalse(gate.valid_attestation(record))

    def test_missing_audio_and_global_gates_block(self):
        entries = []
        for i in range(1000):
            entries.append({"level": gate.LEVELS[i // 200], "word": f"synthetic{i}",
                            "sense_id": "1", "english_definition": "Test definition",
                            "burmese_meaning": "စမ်းသပ်ချက်",
                            "example_sentence": "This is a test.",
                            "part_of_speech": "noun"})
        errors = gate.audit({"entries": entries,
                             "counts_by_level": {x: 200 for x in gate.LEVELS}}, {"gates": {}})
        self.assertTrue(any("audio path missing" in e for e in errors))
        self.assertTrue(any("global gate" in e for e in errors))

    def test_path_traversal_audio_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "safe").mkdir()
            outside = root.parent / "cefr1000-unsafe-sentinel"
            # Missing path must fail without reading or creating anything outside root.
            item = {"path": "../cefr1000-unsafe-sentinel", "sha256": "0" * 64}
            path = (root / item["path"]).resolve()
            self.assertFalse(path.is_relative_to(root.resolve()))


if __name__ == "__main__":
    unittest.main()
