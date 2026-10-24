#!/usr/bin/env python3
"""Fail-closed structural and word-specific source-evidence audit for A2–C1.

This validates candidate alignment and the evidence-review queue only.
A passing result is NOT independent English, Myanmar, CEFR or audio approval.
"""
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
LEVELS={"A2":700,"B1":1000,"B2":1300,"C1":1500}
REVIEW=("reviewed_english","reviewed_burmese","reviewed_example",
        "reviewed_level","reviewed_pronunciation")

def audit(drafts,candidates,evidence):
    errors=[]
    rows=drafts.get("entries",[])
    pool=candidates.get("entries",[])
    counts=Counter(e.get("level") for e in rows)
    lookup={r.get("word"):r for r in pool}
    drafts_by_word={r.get("word"):r for r in rows}
    if drafts.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        errors.append("Editorial drafts must remain marked unverified")
    if candidates.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        errors.append("Candidate pool must remain unverified")
    if evidence.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        errors.append("Source observations must remain unverified")
    if drafts.get("reviewed_independently")!=0 or evidence.get("independently_approved")!=0:
        errors.append("Unreviewed drafts/evidence must never claim independent approval")
    if len(rows)<80 or any(counts.get(level,0)<20 or counts.get(level,0)>target
                            for level,target in LEVELS.items()) or sum(counts.values())!=len(rows):
        errors.append(f"Expected at least 20 A2-C1 original drafts per level, got {counts}")
    if len(lookup)!=5000 or len(pool)!=5000:
        errors.append("Candidate pool missing records or duplicate words")
    if len(drafts_by_word)!=len(rows):
        errors.append("Duplicate editorial starter headwords")
    if len({r.get("example_sentence") for r in rows})!=len(rows):
        errors.append("Duplicate example sentences across editorial drafts")
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
        if word.lower() not in ex.lower():
            errors.append(f"{word}: example does not contain headword spelling or inflection")
        if len(ex)>180 or len(e.get("english_definition",""))>300:
            errors.append(f"{word}: example or definition too long")
        if not e.get("source_note","").startswith("Original draft"):
            errors.append(f"{word}: provenance warning missing")
    observations=evidence.get("records",[])
    if len(observations)<8 or evidence.get("source_observations")!=len(observations):
        errors.append("Expected at least 8 word-specific external source observations")
    if len({r.get("word") for r in observations})!=len(observations):
        errors.append("Duplicate source observations")
    conflicts=0
    for e in observations:
        word=e.get("word","")
        draft=drafts_by_word.get(word)
        if not draft or e.get("provisional_level")!=draft.get("level"):
            errors.append("Evidence has no matching draft: "+word)
        if e.get("source_sense_level") not in {"A1",*LEVELS}:
            errors.append("Evidence missing observed source CEFR level: "+word)
        if e.get("source_name")!="Cambridge Advanced Learner's Dictionary / Cambridge Dictionary":
            errors.append("Unexpected evidence source: "+word)
        url=e.get("source_url","")
        parsed=urlparse(url)
        if (parsed.scheme!="https" or parsed.netloc!="dictionary.cambridge.org" or
            parsed.path!=f"/dictionary/english/{word}"):
            errors.append("Evidence URL is not a word-specific Cambridge English page: "+word)
        if not e.get("source_sense_paraphrase") or not e.get("part_of_speech"):
            errors.append("Missing sense/POS observation: "+word)
        if e.get("source_observed_on")!="2026-10-24" or e.get("word_specific_source_page_observed") is not True:
            errors.append("Source observation lacks actual dated page evidence: "+word)
        mismatch=e.get("source_sense_level")!=e.get("provisional_level")
        if e.get("provisional_level_conflicts_with_source") is not mismatch:
            errors.append("Mismatch flag inconsistent with source observation: "+word)
        if mismatch:
            conflicts+=1
            if e.get("editorial_issue")!="LEVEL_CONFLICT":
                errors.append("Unflagged provisional level conflict: "+word)
        for flag in ("burmese_translation_source_verified","independent_semantic_review",
                     "independent_cefr_review","independent_translation_review",
                     "audio_pronunciation_review","release_approved"):
            if e.get(flag) is not False:
                errors.append(f"{word}: source observation falsely claims {flag}")
    return errors,counts,conflicts

def main():
    starters=json.loads((ROOT/"draft/A2-C1-EDITORIAL-STARTER.json").read_text("utf8"))
    candidates=json.loads((ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json").read_text("utf8"))
    evidence=json.loads((ROOT/"draft/A2-C1-SOURCE-EVIDENCE-REVIEW.json").read_text("utf8"))
    errors,counts,conflicts=audit(starters,candidates,evidence)
    if errors:
        print("FAILED structural / source-evidence audit:")
        for error in errors[:50]:print(error)
        raise SystemExit(1)
    print(f"PASS: {sum(counts.values())} A2–C1 original bilingual first drafts, levels {dict(counts)}")
    print(f"PASS: {len(evidence['records'])} actual word-specific dictionary page observations, {conflicts} provisional level conflicts flagged")
    print("0 independent editorial approvals; all 4500 A2–C1 candidate levels provisional")
    print("0 newly approved British voice recordings; release remains BLOCKED")

if __name__=="__main__":
    main()
