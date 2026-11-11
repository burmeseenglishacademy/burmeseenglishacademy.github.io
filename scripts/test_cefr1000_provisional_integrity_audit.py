#!/usr/bin/env python3
"""Adversarial, read-only tests for the provisional staging audit."""
import copy
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cefr1000_provisional_integrity_audit import audit

doc = json.loads(pathlib.Path("draft/CEFR-1000-PROVISIONAL-SHORTLIST.json").read_text(encoding="utf-8"))
baseline, warnings, counts = audit(doc)
assert not baseline, f"Baseline provisional structural errors: {baseline[:10]}"
assert counts == {level: 200 for level in ("A1", "A2", "B1", "B2", "C1")}
cases = [
    ("missing entry", lambda d: d["entries"].pop()),
    ("duplicate identity", lambda d: d["entries"][1].update(word=d["entries"][0]["word"], part_of_speech=d["entries"][0]["part_of_speech"])),
    ("editorial hold lifted", lambda d: d["entries"][0].update(editorial_hold=False)),
    ("review flag spoofed", lambda d: d["entries"][0].update(reviewed_english=True)),
    ("approval flag spoofed", lambda d: d["entries"][0].update(release_approved=True)),
    ("metadata approval spoofed", lambda d: d["independently_approved_by_level"].update(A1=1)),
    ("release status changed", lambda d: d.update(release_status="READY")),
    ("missing provenance", lambda d: d["entries"][0].update(source_blob_sha="")),
    ("negative source index", lambda d: d["entries"][0].update(source_index=-1)),
    ("missing translation", lambda d: d["entries"][0].update(burmese_meaning="")),
    ("unknown level", lambda d: d["entries"][0].update(level="C2")),
    ("metadata count mismatch", lambda d: d["counts_by_level"].update(A1=199)),
]
for name, mutation in cases:
    candidate = copy.deepcopy(doc)
    mutation(candidate)
    errors, _, _ = audit(candidate)
    assert errors, f"FAIL OPEN: {name}"
    print(f"PASS: rejected {name}")
print(f"PASS: {len(cases)} adversarial cases; baseline is structural-only, NOT release approval")
