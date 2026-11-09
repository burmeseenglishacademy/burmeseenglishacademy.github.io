#!/usr/bin/env python3
"""Regression tests for CEFR-1000 editorial risk scanner.

Synthetic fixtures only: passing a structural assertion never approves vocabulary.
Run: python3 -m unittest discover -s tests -p 'test_cefr1000_risk_queue.py'
"""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "cefr1000_risk_queue", ROOT / "scripts/cefr1000_editorial_risk_queue.py"
)
scanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scanner)


def fixture():
    entries = []
    for level in scanner.LEVELS:
        for i in range(200):
            entries.append({"word": f"synthetic_{level}_{i}", "level": level,
                            "source_path": "synthetic-only", "source_index": i,
                            "source_blob_sha": "synthetic-only"})
    for word, (level, _, _) in scanner.RISK_CASES.items():
        slot = next(i for i, e in enumerate(entries) if e["level"] == level and
                    e["word"].startswith("synthetic_"))
        entries[slot]["word"] = word
    return {"entries": entries}


class EditorialRiskQueueTests(unittest.TestCase):
    def test_all_known_risks_remain_blocking(self):
        risks = scanner.assess(fixture())
        for word in scanner.RISK_CASES:
            matching = [r for r in risks if r.get("word") == word]
            self.assertEqual(len(matching), 1, word)
            self.assertIs(matching[0]["independently_verified"], False)

    def test_missing_case_is_not_silently_dropped(self):
        data = fixture()
        next(e for e in data["entries"] if e["word"] == "terrorism")["word"] = "other"
        risks = scanner.assess(data)
        self.assertTrue(any(r.get("word") == "terrorism" and
                            r["risk"] == "MISSING_OR_DUPLICATED_RISK_CASE" for r in risks))

    def test_duplicate_case_is_blocked(self):
        data = fixture()
        next(e for e in data["entries"] if e["word"] == "synthetic_C1_199")["word"] = "terrorism"
        risks = scanner.assess(data)
        self.assertTrue(any(r.get("word") == "terrorism" and
                            r["risk"] == "MISSING_OR_DUPLICATED_RISK_CASE" for r in risks))

    def test_level_move_requires_adjudication(self):
        data = fixture()
        next(e for e in data["entries"] if e["word"] == "terrorism")["level"] = "B2"
        risks = scanner.assess(data)
        self.assertTrue(any(r.get("word") == "terrorism" and
                            r["risk"] == "LEVEL_CHANGED_REQUIRES_ADJUDICATION" for r in risks))
        self.assertTrue(any(r.get("risk") == "WRONG_LEVEL_COUNT" for r in risks))

    def test_wrong_total_is_blocked(self):
        data = fixture()
        data["entries"].pop()
        self.assertTrue(any(r["risk"] == "WRONG_TOTAL" for r in scanner.assess(data)))

    def test_normalization_is_case_and_nfkc_aware(self):
        self.assertEqual(scanner.norm(" ＴＥＲＲＯＲＩＳＭ "), "terrorism")

    def test_scanner_never_accepts_self_declared_review(self):
        data = fixture()
        for e in data["entries"]:
            e["reviewed_level"] = True
            e["release_approved"] = True
        risks = scanner.assess(data)
        self.assertEqual(len([r for r in risks if r.get("independently_verified") is False]),
                         len(scanner.RISK_CASES))


if __name__ == "__main__":
    unittest.main()
