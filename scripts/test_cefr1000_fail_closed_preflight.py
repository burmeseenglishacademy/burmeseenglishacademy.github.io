#!/usr/bin/env python3
"""Regression tests for CEFR-1000 fail-closed preflight; no editorial approval implied."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from scripts.cefr1000_fail_closed_preflight import run

LEVELS = ("A1", "A2", "B1", "B2", "C1")
def entry(level, number):
    return dict(word=f"word-{level}-{number}", level=level, part_of_speech="noun",
        english_definition="A test definition", burmese_meaning="စမ်းသပ်ချက်",
        example_sentence="This is a test.", source_path="test/source.json",
        source_index=number, source_blob_sha="a"*40, editorial_hold=True,
        reviewed_english=False, reviewed_burmese=False, reviewed_example=False,
        reviewed_level=False, reviewed_pronunciation=False, release_approved=False,
        source_english="", source_burmese="", source_level="")
def manifest():
    return dict(counts_by_level={level:200 for level in LEVELS},
        independently_approved_by_level={level:0 for level in LEVELS},
        entries=[entry(level,i) for level in LEVELS for i in range(200)])
def check(data, release=False):
    with tempfile.TemporaryDirectory() as tmp:
        path=Path(tmp)/"manifest.json"
        path.write_text(json.dumps(data,ensure_ascii=False),encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code=run(path,release=release)
        return code,json.loads(output.getvalue())
class PreflightTests(unittest.TestCase):
    def test_valid_first_pass_is_structurally_valid_only(self):
        code,result=check(manifest())
        self.assertEqual(code,0,result)
        self.assertEqual(result["counts"],{level:200 for level in LEVELS})
    def test_release_is_never_authorized_by_manifest(self):
        data=manifest()
        for e in data["entries"]:
            e.update(editorial_hold=False,release_approved=True,
                     **{k:True for k in ("reviewed_english","reviewed_burmese",
                       "reviewed_example","reviewed_level","reviewed_pronunciation")})
            e.update(source_english="https://example.org",source_burmese="review",
                     source_level="https://example.org")
        data["independently_approved_by_level"]={level:200 for level in LEVELS}
        code,result=check(data,release=True)
        self.assertNotEqual(code,0)
        self.assertTrue(any("release blocked" in s for s in result["details"]))
    def test_duplicate_headword_pos_is_rejected(self):
        data=manifest()
        data["entries"][1]["word"]=data["entries"][0]["word"].upper()
        code,result=check(data)
        self.assertNotEqual(code,0)
        self.assertTrue(any("duplicate" in s for s in result["details"]))
    def test_missing_burmese_is_rejected(self):
        data=manifest()
        data["entries"][0]["burmese_meaning"]=" "
        self.assertNotEqual(check(data)[0],0)
    def test_missing_review_boolean_is_rejected(self):
        data=manifest()
        del data["entries"][0]["reviewed_level"]
        self.assertNotEqual(check(data)[0],0)
    def test_wrong_level_count_is_rejected(self):
        data=manifest()
        data["entries"][0]["level"]="B1"
        self.assertNotEqual(check(data)[0],0)
    def test_declared_counts_cannot_mask_missing_entry(self):
        data=manifest()
        data["entries"].pop()
        self.assertNotEqual(check(data)[0],0)
    def test_unhashable_level_fails_closed_without_crash(self):
        data=manifest()
        data["entries"][0]["level"]=["A1"]
        code,result=check(data)
        self.assertNotEqual(code,0)
        self.assertTrue(any("invalid level" in item for item in result["details"]))
    def test_boolean_source_index_is_rejected(self):
        data=manifest()
        data["entries"][0]["source_index"]=True
        self.assertNotEqual(check(data)[0],0)
    def test_invalid_source_blob_sha_is_rejected(self):
        data=manifest()
        data["entries"][0]["source_blob_sha"]="not-a-sha"
        self.assertNotEqual(check(data)[0],0)
    def test_non_string_word_is_rejected(self):
        data=manifest()
        data["entries"][0]["word"]=123
        self.assertNotEqual(check(data)[0],0)
    def test_nontext_definition_is_rejected(self):
        data=manifest()
        data["entries"][0]["english_definition"]={"bad":"type"}
        self.assertNotEqual(check(data)[0],0)
    def test_cross_level_repeated_headword_is_rejected(self):
        data=manifest()
        data["entries"][200]["word"]=data["entries"][0]["word"]
        code,result=check(data)
        self.assertNotEqual(code,0)
        self.assertTrue(any("cross-level" in item for item in result["details"]))
    def test_a_an_lexical_unit_collision_is_rejected(self):
        data=manifest()
        data["entries"][0]["word"]="a"
        data["entries"][1]["word"]="an"
        code,result=check(data)
        self.assertNotEqual(code,0)
        self.assertTrue(any("a/an" in item for item in result["details"]))
    def test_missing_editorial_hold_is_rejected(self):
        data=manifest()
        del data["entries"][0]["editorial_hold"]
        self.assertNotEqual(check(data)[0],0)
    def test_provisional_cannot_clear_hold(self):
        data=manifest()
        data["entries"][0]["editorial_hold"]=False
        self.assertNotEqual(check(data)[0],0)
    def test_provisional_cannot_claim_review(self):
        data=manifest()
        data["entries"][0]["reviewed_english"]=True
        self.assertNotEqual(check(data)[0],0)
    def test_provisional_cannot_claim_release_approval(self):
        data=manifest()
        data["entries"][0]["release_approved"]=True
        self.assertNotEqual(check(data)[0],0)
if __name__=="__main__":
    unittest.main()
