#!/usr/bin/env python3
"""Staging-only adversarial checks for the CEFR-1000 release evidence gate.

No production data, approval records, or network calls are modified.
Run: python -m unittest discover -s scripts -p 'test_cefr1000_release_evidence_gate.py'
"""
import importlib.util
import pathlib
import unittest

MODULE = pathlib.Path(__file__).with_name("cefr1000_release_evidence_gate.py")
spec = importlib.util.spec_from_file_location("cefr1000_release_evidence_gate", MODULE)
gate_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate_module)

def manifest():
    return {"entries": [{"word": f"word-{i}", "level": ("A1","A2","B1","B2","C1")[i // 200]} for i in range(1000)]}

class EvidenceGateAdversarialTests(unittest.TestCase):
    def setUp(self):
        self.manifest = manifest()

    def test_duplicate_exact_sense_blocks_even_without_ledger(self):
        m = manifest()
        m["entries"][1]["word"] = m["entries"][0]["word"]
        result = gate_module.gate(m, None)
        self.assertTrue(any("duplicate level/headword/POS/sense" in x for x in result))

    def test_unknown_level_blocks_even_without_ledger(self):
        m = manifest()
        m["entries"][0]["level"] = "C2"
        result = gate_module.gate(m, None)
        self.assertTrue(any("unexpected CEFR level" in x for x in result))

    def test_casefolded_duplicate_blocks(self):
        m = manifest()
        m["entries"][0]["word"] = "Example"
        m["entries"][1]["word"] = " example "
        result = gate_module.gate(m, None)
        self.assertTrue(any("duplicate level/headword/POS/sense" in x for x in result))

    def test_cross_level_same_sense_blocks_without_ledger(self):
        m = manifest()
        m["entries"][200]["word"] = m["entries"][0]["word"]
        result = gate_module.gate(m, None)
        self.assertTrue(any("cross-level duplicate headword/POS/sense" in x for x in result))

    def test_cross_level_distinct_explicit_senses_not_conflated(self):
        m = manifest()
        m["entries"][0]["word"] = "bank"
        m["entries"][0]["sense_id"] = "financial-institution"
        m["entries"][200]["word"] = "bank"
        m["entries"][200]["sense_id"] = "river-edge"
        result = gate_module.gate(m, None)
        self.assertFalse(any("cross-level duplicate headword/POS/sense" in x for x in result))

    def test_missing_sense_and_pos_block_even_without_ledger(self):
        m = manifest()
        result = gate_module.gate(m, None)
        self.assertTrue(any("explicit lexical sense identifier missing" in x for x in result))
        self.assertTrue(any("part of speech missing" in x for x in result))

    def test_placeholder_sense_blocks_even_without_ledger(self):
        m = manifest()
        m["entries"][0]["pos"] = "noun"
        m["entries"][0]["sense_id"] = "TBD"
        result = gate_module.gate(m, None)
        self.assertTrue(any("explicit lexical sense identifier missing" in x for x in result))

    def test_absent_evidence_blocks(self):
        self.assertIn("independent evidence ledger absent or invalid", gate_module.gate(self.manifest, None))

    def test_short_manifest_blocks(self):
        m = {"entries": self.manifest["entries"][:-1]}
        self.assertIn("manifest must contain exactly 1000 entries", gate_module.gate(m, {}))

    def test_imbalanced_levels_block(self):
        m = manifest()
        m["entries"][0]["level"] = "B1"
        result = gate_module.gate(m, {})
        self.assertTrue(any("A1: expected 200" in x for x in result))
        self.assertTrue(any("B1: expected 200" in x for x in result))

    def test_empty_ledger_blocks_all_domains(self):
        result = gate_module.gate(self.manifest, {"independent_reviews":[],"audio":[],"qa":{}})
        self.assertTrue(any("independent english evidence" in x for x in result))
        self.assertTrue(any("george/headword" in x for x in result))
        self.assertTrue(any("physical_iphone_safari" in x for x in result))

    def test_self_asserted_manifest_hash_not_enough(self):
        result = gate_module.gate(self.manifest, {
            "independent_reviews": [], "audio": [], "qa": {},
            "manifest_blob_sha": "a"*40,
            "verified_manifest_blob_sha": "b"*40
        })
        self.assertIn("manifest blob SHA not reconciled against actual manifest bytes", result)

    def test_matching_ledger_hash_without_actual_bytes_blocks(self):
        ledger = {"independent_reviews": [], "audio": [], "qa": {},
                  "manifest_blob_sha": "a" * 40}
        result = gate_module.gate(self.manifest, ledger)
        self.assertIn("manifest blob SHA not reconciled against actual manifest bytes", result)

    def test_mismatched_actual_manifest_bytes_blocks(self):
        ledger = {"independent_reviews": [], "audio": [], "qa": {},
                  "manifest_blob_sha": "a" * 40}
        result = gate_module.gate(self.manifest, ledger, "b" * 40)
        self.assertIn("manifest blob SHA not reconciled against actual manifest bytes", result)

    def test_matching_actual_blob_sha_removes_only_hash_blocker(self):
        ledger = {"independent_reviews": [], "audio": [], "qa": {},
                  "manifest_blob_sha": "a" * 40}
        result = gate_module.gate(self.manifest, ledger, "a" * 40)
        self.assertFalse(any("manifest blob SHA" in x for x in result))
        self.assertTrue(any("independent english evidence" in x for x in result))

    def test_unexpected_review_index_blocks(self):
        result = gate_module.gate(self.manifest, {
            "independent_reviews":[{"entry_index":True,"domain":"english"}],
            "audio":[],"qa":{}
        })
        self.assertIn("unexpected review index/domain", result)

    def test_unexpected_audio_voice_blocks(self):
        result = gate_module.gate(self.manifest, {
            "independent_reviews":[],
            "audio":[{"entry_index":0,"voice":"unknown","kind":"headword"}],
            "qa":{}
        })
        self.assertIn("unexpected audio index/voice/kind", result)

    def test_unsubstantiated_qa_pass_blocks(self):
        result = gate_module.gate(self.manifest, {
            "independent_reviews":[],"audio":[],
            "qa":{"physical_iphone_safari":{"result":"pass"}}
        })
        self.assertIn("physical_iphone_safari: verified evidence missing", result)

if __name__ == "__main__":
    unittest.main()
