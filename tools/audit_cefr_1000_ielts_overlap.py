#!/usr/bin/env python3
"""Mechanical-only audit of CEFR-1000 wordform overlap with PRESERVED IELTS-1000.

Shared spellings are not proof of wrong CEFR level or identical/different senses.
Do not edit the production IELTS dataset or mark semantic review completed.
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
shortlist = json.loads((ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json").read_text("utf8"))
ledger = json.loads((ROOT / "draft/CEFR-1000-IELTS-OVERLAP-REVIEW.json").read_text("utf8"))
text = (ROOT / "ielts-vocabulary-data.js").read_text("utf8")
prefix = "const IELTS_VOCAB_BANK="
assert text.startswith("/*"), "Unexpected IELTS data wrapper"
assert prefix in text
body = text.split(prefix, 1)[1].strip()
assert body.endswith(";"), "Unexpected IELTS data trailer"
ielts = json.loads(body[:-1])["entries"]
cefr = shortlist["entries"]
assert len(ielts) == 1000 and len(cefr) == 1000
assert all(isinstance(row, list) and len(row) >= 5 for row in ielts)
ix = {row[0].lower(): row for row in ielts}
assert len(ix) == 1000
expected = [row for row in cefr if row["word"].lower() in ix]
assert ledger["exact_casefold_headword_overlap"] == len(expected) == len(ledger["entries"])
assert ledger["cefr_provisional_size"] == ledger["ielts_production_size"] == 1000
assert ledger["stage"] == "OVERLAP_TRIAGE_NOT_REVIEWED_DO_NOT_PUBLISH"
assert ledger["independently_checked_overlaps"] == 0
counts = collections.Counter(row["level"] for row in expected)
assert ledger["counts_by_proposed_cefr_level"] == {
    l: counts[l] for l in ("A1", "A2", "B1", "B2", "C1")}
for original, r in zip(expected, ledger["entries"]):
    actual = ix[original["word"].lower()]
    assert r["word"] == original["word"] and r["proposed_cefr_level"] == original["level"]
    assert r["cefr_draft_definition"] == original["english_definition"]
    assert r["cefr_draft_burmese_meaning"] == original["burmese_meaning"]
    assert r["ielts_existing_definition"] == actual[1]
    assert r["ielts_existing_burmese_meaning"] == actual[2]
    assert r["ielts_existing_example"] == actual[3]
    assert r["same_sense_confirmed"] is False
    assert r["semantic_distinctness_reviewed"] is False
    assert r["release_approved"] is False
print(f"PASS structural only: {len(expected)} IELTS/CEFR shared headwords, "
      f"level split {dict(counts)}, 0 verified same-sense decisions; "
      "protected IELTS 1000 bank was read but never changed.")
