#!/usr/bin/env python3
"""Negative-only regression checks for the staging release veto.

Synthetic fixtures deliberately are not independent human review evidence.
"""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
import cefr1000_release_veto as veto

LEVELS = ("A1", "A2", "B1", "B2", "C1")
TARGET = {level: 200 for level in LEVELS}
ZERO = {level: 0 for level in LEVELS}

def fixtures(root):
    entries = [{"level": level, "word": f"{level}-{i}"} for level in LEVELS for i in range(200)]
    tasks = [{"level": level, "review_status": "PENDING_INDEPENDENT_REVIEW"} for level in LEVELS for _ in range(200)]
    shortlist = {"counts_by_level": TARGET, "independently_approved_by_level": ZERO,
                 "release_status": "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
                 "entries": entries}
    reviews = {"counts_by_level": TARGET, "independently_approved_by_level": ZERO,
               "source_shortlist_blob_sha": "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
               "release_status": "ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH",
               "tasks": tasks}
    a, b = root / "shortlist.json", root / "tasks.json"
    a.write_text(json.dumps(shortlist), encoding="utf-8")
    b.write_text(json.dumps(reviews), encoding="utf-8")
    return a, b, shortlist, reviews

class ReleaseVetoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.a, self.b, self.s, self.t = fixtures(Path(self.tmp.name))

    def save(self):
        self.a.write_text(json.dumps(self.s), encoding="utf-8")
        self.b.write_text(json.dumps(self.t), encoding="utf-8")

    def test_even_perfect_synthetic_structure_cannot_authorize_release(self):
        issues = veto.inspect(self.a, self.b)
        self.assertTrue(any("1000 independently signed" in issue for issue in issues))
        self.assertTrue(any("real listening signoff" in issue for issue in issues))
        self.assertTrue(any("physical iPhone Safari" in issue for issue in issues))
        self.assertTrue(any("live deployment" in issue for issue in issues))

    def test_forged_approval_counter_is_detected(self):
        self.s["independently_approved_by_level"]["A1"] = 200
        self.save()
        self.assertTrue(any("approval counters changed" in i for i in veto.inspect(self.a, self.b)))

    def test_unreviewed_task_status_change_is_detected(self):
        self.t["tasks"][0]["review_status"] = "APPROVED"
        self.save()
        self.assertTrue(any("no longer pending" in i for i in veto.inspect(self.a, self.b)))

    def test_missing_level_entry_is_detected(self):
        self.s["entries"].pop()
        self.save()
        self.assertTrue(any("actual allocation" in i for i in veto.inspect(self.a, self.b)))

    def test_forged_provenance_is_detected(self):
        self.t["source_shortlist_blob_sha"] = "0" * 40
        self.save()
        self.assertTrue(any("provenance differs" in i for i in veto.inspect(self.a, self.b)))

    def test_duplicate_level_headword_is_detected(self):
        self.s["entries"][1]["word"] = self.s["entries"][0]["word"].upper()
        self.save()
        self.assertTrue(any("Duplicate level/word" in i for i in veto.inspect(self.a, self.b)))

    def test_cross_level_same_word_requires_exact_sense_adjudication(self):
        self.s["entries"][200]["word"] = self.s["entries"][0]["word"]
        self.save()
        self.assertTrue(any("Cross-level headword collisions" in i for i in veto.inspect(self.a, self.b)))

    def test_unicode_compatibility_duplicate_is_detected(self):
        self.s["entries"][0]["word"] = "office"
        self.s["entries"][1]["word"] = "oﬃce"
        self.save()
        self.assertTrue(any("Duplicate level/word" in i for i in veto.inspect(self.a, self.b)))

    def test_missing_word_is_detected(self):
        del self.s["entries"][0]["word"]
        self.save()
        self.assertTrue(any("missing word" in i for i in veto.inspect(self.a, self.b)))

    def test_non_object_entry_is_detected(self):
        self.s["entries"][0] = None
        self.save()
        self.assertTrue(any("non-object record" in i for i in veto.inspect(self.a, self.b)))

    def test_non_object_shortlist_root_is_denied(self):
        self.a.write_text("[]", encoding="utf-8")
        self.assertTrue(any("top-level JSON must be objects" in i for i in veto.inspect(self.a, self.b)))

    def test_non_object_review_root_is_denied(self):
        self.b.write_text("null", encoding="utf-8")
        self.assertTrue(any("top-level JSON must be objects" in i for i in veto.inspect(self.a, self.b)))

    def test_missing_json_is_denied(self):
        self.a.unlink()
        self.assertTrue(any("Unable to parse" in i for i in veto.inspect(self.a, self.b)))

if __name__ == "__main__":
    unittest.main()
