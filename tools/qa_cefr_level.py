#!/usr/bin/env python3
"""Parallel, per-level editorial draft QA for unpublished A2–C1 vocabulary.

This validates structures and progress accounting only, never meaning accuracy
or independent linguistic verification. It fails closed on false approval.
"""
import argparse
import collections
import json
import pathlib
import re
import unicodedata

ROOT=pathlib.Path(__file__).resolve().parents[1]
TARGETS={"A2":700,"B1":1000,"B2":1300,"C1":1500}
FIELDS=("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")
BURMESE=re.compile(r"[\u1000-\u109f\uaa60-\uaa7f]")
WORD=re.compile(r"[a-z]+(?:'[a-z]+)?",re.ASCII)

def scan(level,candidates,drafts,observations):
    if level not in TARGETS:raise ValueError("Invalid CEFR level")
    for obj in (candidates,drafts,observations):
        if obj.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
            raise ValueError("Input not marked unpublished")
    entries=candidates.get("entries",[])
    all_drafts=drafts.get("entries",[])
    all_evidence=observations.get("records",[])
    if len(entries)!=5000 or len({r.get("word") for r in entries})!=5000:
        raise ValueError("Candidate inventory corrupt")
    if collections.Counter(r["level"] for r in entries)!=collections.Counter({"A1":500,**TARGETS}):
        raise ValueError("Candidate level quotas unexpectedly changed")
    if len({r.get("word") for r in all_drafts})!=len(all_drafts):
        raise ValueError("Duplicate editor draft")
    if len({r.get("word") for r in all_evidence})!=len(all_evidence):
        raise ValueError("Duplicate source evidence")
    inventory={r["word"]:r for r in entries if r["level"]==level}
    if len(inventory)!=TARGETS[level]:raise ValueError("Level candidate inventory count wrong")
    level_drafts=[r for r in all_drafts if r.get("level")==level]
    seen=set()
    alerts=[]
    for r in level_drafts:
        word=r.get("word","")
        if not WORD.fullmatch(word) or word in seen or word not in inventory:
            raise ValueError("Unknown, duplicate or invalid vocabulary draft: "+word)
        seen.add(word)
        if r.get("status")!="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW":
            raise ValueError("Draft improperly marked approved: "+word)
        if any(r.get(key) is not False for key in FIELDS):
            raise ValueError("Unverified status flag on draft: "+word)
        if any(r.get(key) for key in ("source_english","source_burmese","source_level")):
            raise ValueError("Unchecked source presented as verified: "+word)
        for key in ("english_definition","burmese_meaning","example_sentence","part_of_speech"):
            value=r.get(key)
            if not isinstance(value,str) or not value.strip():
                raise ValueError("Missing "+key+": "+word)
            if unicodedata.normalize("NFC",value)!=value:
                raise ValueError("Bad Unicode normalization "+key+": "+word)
        if not BURMESE.search(r["burmese_meaning"]):
            raise ValueError("No Burmese script: "+word)
        ex=r["example_sentence"]
        if not ex[0].isupper() or ex[-1] not in ".?!" or len(ex)>180:
            raise ValueError("Unusable example shape: "+word)
        if not re.search(r"\b"+re.escape(word)+r"(?:s|es|ed|ing)?\b",ex,re.I):
            alerts.append({"word":word,"note":"Example may require conjugation or sense review"})
    evidences=[r for r in all_evidence if r.get("provisional_level")==level]
    conflicts=[]
    for r in evidences:
        if r["word"] not in seen:raise ValueError("Evidence without draft: "+r["word"])
        if any(r.get(k) is not False for k in ("independent_semantic_review","independent_translation_review",
                                               "independent_cefr_review","audio_pronunciation_review","release_approved")):
            raise ValueError("Evidence independently approved without proof: "+r["word"])
        if r.get("provisional_level_conflicts_with_source"):
            conflicts.append({"word":r["word"],"provisional":level,"source":r.get("source_sense_level")})
    report={
      "level":level,
      "status":"STAGING_STRUCTURAL_QA_NOT_LINGUISTIC_APPROVAL",
      "target":TARGETS[level],
      "written_first_drafts":len(seen),
      "without_first_draft":TARGETS[level]-len(seen),
      "word_specific_source_observations_unverified":len(evidences),
      "level_conflicts":conflicts,
      "example_form_warnings":alerts,
      "independently_approved":0,
      "release_approved":False,
    }
    return report

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--level",choices=tuple(TARGETS),required=True)
    p.add_argument("--out",type=pathlib.Path,default=ROOT/"scratch/cefr-level-qa")
    args=p.parse_args()
    input_files=("draft/UNVERIFIED_CEFR_CANDIDATES.json",
                 "draft/A2-C1-EDITORIAL-STARTER.json",
                 "draft/A2-C1-SOURCE-EVIDENCE-REVIEW.json")
    data=[json.loads((ROOT/path).read_text("utf8")) for path in input_files]
    report=scan(args.level,*data)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/f"{args.level}.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n","utf8")
    print(f"PASS {args.level}: {report['written_first_drafts']}/{report['target']} original drafts, "
          f"{report['word_specific_source_observations_unverified']} unapproved dictionary observations, "
          f"{len(report['level_conflicts'])} flagged level conflicts.")
    print("NOT APPROVED: no English/Burmese meaning, CEFR level or pronunciation independently verified.")
if __name__=="__main__":
    main()
