#!/usr/bin/env python3
"""Fail-closed staging audit for first original A2–C1 bilingual drafts.

PASS only means candidate alignment and structure are valid.
NEVER turns an AI-assisted draft into a verified language reference.
"""
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata

ROOT=Path(__file__).resolve().parents[1]
LEVELS={"A2","B1","B2","C1"}
REVIEW=("reviewed_english","reviewed_burmese","reviewed_example",
        "reviewed_level","reviewed_pronunciation")

def audit(drafts,candidates):
    errors=[]
    rows=drafts.get("entries",[])
    pool=candidates.get("entries",[])
    levels=Counter(e.get("level") for e in rows)
    lookup={r.get("word"):r for r in pool}
    if drafts.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        errors.append("Editorial drafts must remain marked unverified")
    if candidates.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        errors.append("Candidate pool must remain unverified")
    if len(rows)!=40 or levels!=Counter({"A2":10,"B1":10,"B2":10,"C1":10}):
        errors.append(f"Expected ten first drafts per A2-C1 level, got {levels}")
    if len(lookup)!=5000:
        errors.append("Candidate pool is missing records or has duplicate words")
    if len({x.get("word") for x in rows})!=len(rows):
        errors.append("Duplicate editorial starter headwords")
    for e in rows:
        word=e.get("word","")
        if not re.fullmatch(r"[a-z]+(?:'[a-z]+)?",word):
            errors.append("Noncanonical headword: "+word)
        linked=lookup.get(word)
        if not linked or linked.get("level")!=e.get("level"):
            errors.append(f"Candidate/level mismatch: {word}")
        if e.get("level") not in LEVELS:
            errors.append("Invalid starter level: "+word)
        if e.get("status")!="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW":
            errors.append("Premature editorial approval: "+word)
        if any(e.get(flag) is not False for flag in REVIEW):
            errors.append("Premature review flag: "+word)
        if any(e.get(source) for source in ("source_english","source_burmese","source_level")):
            errors.append("Starter has unverified source represented as checked: "+word)
        for field in ("english_definition","burmese_meaning","example_sentence","part_of_speech"):
            value=e.get(field)
            if not isinstance(value,str) or not value.strip():
                errors.append(f"{word}: missing {field}")
            elif unicodedata.normalize("NFC",value)!=value:
                errors.append(f"{word}: noncanonical Unicode in {field}")
        if not re.search(r"[\u1000-\u109f\uaa60-\uaa7f]",e.get("burmese_meaning","")):
            errors.append(f"{word}: Burmese Unicode meaning missing")
        ex=e.get("example_sentence","")
        if not ex or not ex[0].isupper() or ex[-1] not in ".?!":
            errors.append(f"{word}: incomplete example punctuation")
        if len(ex)>180 or len(e.get("english_definition",""))>300:
            errors.append(f"{word}: example or definition too long")
        if not e.get("source_note","").startswith("Original draft"):
            errors.append(f"{word}: provenance warning missing")
    return errors,levels

def main():
    starters=json.loads((ROOT/"draft/A2-C1-EDITORIAL-STARTER.json").read_text("utf8"))
    candidates=json.loads((ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json").read_text("utf8"))
    errors,levels=audit(starters,candidates)
    if errors:
        print("FAILED structural draft audit:")
        for e in errors[:40]:print(e)
        raise SystemExit(1)
    print("PASS: 40 A2–C1 original English-Myanmar example drafts, 10 per level")
    print("All 40 remain unverified for meaning, translation, CEFR level, sources and pronunciation")
    print("A2–C1 total candidate queue remains 4500 and is NOT ready for public learners")

if __name__=="__main__":
    main()
