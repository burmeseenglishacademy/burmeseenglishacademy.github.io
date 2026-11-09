#!/usr/bin/env python3
"""Deterministic CEFR-1000 editorial risk queue; never approves or edits entries.

Run: python3 scripts/cefr1000_editorial_risk_queue.py
Exit 2 when any known release-blocking semantic/CEFR risk remains unresolved.
This is intentionally NOT a provisional-inventory structural audit.
"""
import json
import pathlib
import sys
import unicodedata
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
# Explicitly documented editorial risks, not automatic CEFR verdicts.
RISK_CASES = {
    "a": ("A1", "INDEFINITE_ARTICLE_ALLOMORPH", "Compare with 'an': one lexical sense may occupy two slots."),
    "an": ("A1", "INDEFINITE_ARTICLE_ALLOMORPH", "Compare with 'a': phonological variant, not automatically a separate sense."),
    "you": ("A1", "POLYSEMY_LEVEL", "Confirm addressed-person sense; generic-person sense may have a different CEFR level."),
    "wheelbarrow": ("A2", "CEFR_EVIDENCE_MISSING", "Dictionary definition alone does not establish A2."),
    "greenhouse": ("A2", "CEFR_EVIDENCE_MISSING", "Dictionary definition alone does not establish A2."),
    "terrorism": ("C1", "CEFR_CONFLICT", "Prior publisher research suggested B2; require independent exact-sense adjudication."),
    "municipal": ("C1", "SENSE_MATCH", "Confirm local-government adjective sense and C1 evidence."),
    "abortion": ("C1", "SENSE_MATCH", "Confirm intentional-termination noun sense and C1 evidence."),
    "obfuscate": ("C1", "RARE_WORD", "Obtain explicit source-backed CEFR placement, not WordNet inference."),
    "alacrity": ("C1", "RARE_WORD", "Obtain explicit source-backed CEFR placement, not WordNet inference."),
}
def norm(value):
    return unicodedata.normalize("NFKC", value).casefold().strip()

def assess(data):
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise ValueError("entries must be an array")
    by_word = defaultdict(list)
    for i, e in enumerate(entries):
        if not isinstance(e, dict) or not isinstance(e.get("word"), str):
            raise ValueError(f"invalid entry at index {i}")
        by_word[norm(e["word"])].append((i, e))
    risks = []
    for word, (expected_level, category, detail) in RISK_CASES.items():
        matches = by_word.get(word, [])
        if len(matches) != 1:
            risks.append({"word": word, "risk": "MISSING_OR_DUPLICATED_RISK_CASE",
                          "detail": f"expected one candidate, found {len(matches)}"})
            continue
        index, e = matches[0]
        if e.get("level") != expected_level:
            risks.append({"word": word, "risk": "LEVEL_CHANGED_REQUIRES_ADJUDICATION",
                          "detail": f"expected provisional {expected_level}, found {e.get('level')}"})
        # A changed flag is NOT evidence of a real independent signoff.
        risks.append({"word": word, "level": e.get("level"), "index": index,
                      "source_path": e.get("source_path"), "source_index": e.get("source_index"),
                      "source_blob_sha": e.get("source_blob_sha"),
                      "risk": category, "detail": detail,
                      "independently_verified": False})
    if len(entries) != 1000:
        risks.append({"risk": "WRONG_TOTAL", "detail": f"found {len(entries)}; expected 1000"})
    for level in LEVELS:
        n = sum(e.get("level") == level for e in entries)
        if n != 200:
            risks.append({"risk": "WRONG_LEVEL_COUNT", "level": level, "detail": f"{n}, expected 200"})
    return risks

def main():
    try:
        risks = assess(json.loads(SHORTLIST.read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError) as exc:
        print(f"FAIL CLOSED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"release_ready": False, "risk_count": len(risks),
                      "risks": risks}, ensure_ascii=False, indent=2))
    return 2 if risks else 0

if __name__ == "__main__":
    sys.exit(main())
