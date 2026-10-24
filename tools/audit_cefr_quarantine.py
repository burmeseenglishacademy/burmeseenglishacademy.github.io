#!/usr/bin/env python3
"""Fail-closed audit of risky unpublished candidate headwords.

This verifies quarantine bookkeeping, NOT the truth of dictionary observations,
translations, level placements or the release.
"""
from collections import Counter
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
LEVELS={"A2","B1","B2","C1"}
CONFLICT="CAMBRIDGE_SENSE_LEVEL_CONFLICT"
RISKS={CONFLICT,"WORDNET_FIRST_SENSE_WRONG_FOR_COMMON_USAGE",
       "POSSIBLE_PROPER_NOUN_IN_GENERAL_VOCABULARY",
       "PROVISIONAL_C1_LIKELY_LOWER_OR_UNSUPPORTED"}

def main():
    q=json.loads((ROOT/"draft/A2-C1-CANDIDATE-QUARANTINE.json").read_text("utf8"))
    pool=json.loads((ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json").read_text("utf8"))
    drafts=json.loads((ROOT/"draft/A2-C1-EDITORIAL-STARTER.json").read_text("utf8"))
    assert q["release_status"]==pool["release_status"]==drafts["release_status"]=="UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    assert q["evidence_sources"]["independent_review_performed"] is False
    inventory={x["word"]:x for x in pool["entries"]}
    written={x["word"] for x in drafts["entries"]}
    assert len(inventory)==5000
    words=set()
    types=Counter()
    for e in q["records"]:
        w=e["word"]
        assert w not in words, "duplicate quarantine: "+w
        words.add(w)
        assert w in inventory and w not in written, "candidate must be undrafted: "+w
        assert e["provisional_level"] in LEVELS
        assert e["provisional_level"]==inventory[w]["level"], "candidate level changed: "+w
        assert e["risk"] in RISKS and e["evidence_note"].strip()
        if e["risk"]=="PROVISIONAL_C1_LIKELY_LOWER_OR_UNSUPPORTED":
            assert e["provisional_level"]=="C1", "new level hold must target provisional C1"
        assert e["action"]=="HOLD_FOR_MANUAL_REVIEW"
        assert e["release_approved"] is False and e["reviewed_independently"] is False
        types[e["risk"]]+=1
        if e["risk"]==CONFLICT:
            assert e["source_sense_level"] in {"A1",*LEVELS}
            assert e["source_sense_level"]!=e["provisional_level"]
            parsed=urlparse(e["source_url"])
            assert parsed.scheme=="https" and parsed.netloc=="dictionary.cambridge.org"
            assert parsed.path in (f"/dictionary/english/{w}",f"/dictionary/learner-english/{w}")
        else:
            assert not e.get("source_sense_level"), "unsourced CEFR must not be invented: "+w
    assert len(words)>=20 and types[CONFLICT]>=3
    assert "entries:[]" in (ROOT/"cefr-vocabulary-data.js").read_text("utf8")
    print(f"PASS: {len(words)} candidate headwords held for editorial triage")
    for kind,n in sorted(types.items()):print(f"  {kind}: {n}")
    print("PASS: no quarantined candidate drafted, released, or independently approved")
    print("NOTE: quarantine is a review priority, not a validated CEFR classification.")

if __name__=="__main__":
    main()
