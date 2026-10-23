#!/usr/bin/env python3
"""Create unpublished 100-word A2–C1 review batches, preserving draft progress.

The 5,000 word-frequency / first-WordNet-sense placements are provisional.
AI-assisted bilingual starter material is visible in the *review packets* only;
it has not passed independent sense, level, Burmese or pronunciation approval.
"""
import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = {"A2":700,"B1":1000,"B2":1300,"C1":1500}
FIELDS = ("reviewed_english","reviewed_burmese","reviewed_example",
          "reviewed_level","reviewed_pronunciation")

def load_editorial_starters(raw, candidates):
    """Accept incomplete original drafts; refuse fabricated approvals."""
    if raw.get("release_status")!="UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        raise ValueError("A2-C1 editorial starters must remain unverified")
    entries=raw.get("entries",[])
    if not isinstance(entries,list):raise ValueError("Bad editorial starter entries")
    lookup={}
    for row in entries:
        word=row.get("word")
        if not isinstance(word,str) or word in lookup:
            raise ValueError("Invalid or duplicate starter headword")
        if word not in candidates or row.get("level")!=candidates[word]["level"]:
            raise ValueError("Starter/candidate level mismatch: "+word)
        if row["level"] not in LEVELS:
            raise ValueError("Starter is not A2-C1: "+word)
        if row.get("status")!="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW":
            raise ValueError("Starter prematurely approved: "+word)
        if any(row.get(key) is not False for key in FIELDS):
            raise ValueError("Starter has unverified reviewer flag marked true: "+word)
        if any(row.get(key) for key in ("source_english","source_burmese","source_level")):
            raise ValueError("Starter has source falsely marked confirmed: "+word)
        if not all(row.get(key) for key in
                   ("english_definition","burmese_meaning","example_sentence","part_of_speech")):
            raise ValueError("Incomplete draft: "+word)
        lookup[word]=row
    return lookup

def prepare(source, starters, outdir, batch_size=100):
    if batch_size < 1 or batch_size > 200:
        raise ValueError("batch_size must be between 1 and 200")
    if source.get("release_status") != "UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        raise ValueError("Do not export any published or supposedly approved content")
    rows = source.get("entries")
    if not isinstance(rows,list) or len(rows) != 5000:
        raise ValueError("Expected complete 5000-candidate inventory")
    candidate_map={row["word"]:row for row in rows}
    if len(candidate_map) != 5000:
        raise ValueError("Duplicate word in candidate inventory")
    counts = Counter(r["level"] for r in rows)
    if counts != Counter({"A1":500, **LEVELS}):
        raise ValueError(f"Unexpected provisional levels: {counts}")
    starters_by_word=load_editorial_starters(starters,candidate_map)
    outdir.mkdir(parents=True, exist_ok=True)
    inventory = []
    for level, expected in LEVELS.items():
        subset = [row for row in rows if row["level"]==level]
        assert len(subset)==expected
        level_dir = outdir/level
        level_dir.mkdir(parents=True,exist_ok=True)
        for start in range(0, expected, batch_size):
            work = []
            for row in subset[start:start+batch_size]:
                if any(row.get(field) is True for field in FIELDS):
                    raise ValueError(f"Candidate incorrectly approved: {row['word']}")
                word=row["word"]
                draft=starters_by_word.get(word)
                work.append({
                    "word":word, "provisional_level":level,
                    "provisional_pos":row.get("part_of_speech",""),
                    "wordnet_first_sense_clue_not_verified":row.get("english_definition_draft",""),
                    "wordnet_sense_id":row.get("lexical_sense_id",""),
                    "zipf_frequency":row.get("zipf_frequency"),
                    "english_definition":draft["english_definition"] if draft else "",
                    "burmese_meaning":draft["burmese_meaning"] if draft else "",
                    "example_sentence":draft["example_sentence"] if draft else "",
                    "part_of_speech":draft["part_of_speech"] if draft else "",
                    "source_english":"", "source_burmese":"", "source_level":"",
                    **{field:False for field in FIELDS},
                    "status":("AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW"
                              if draft else "EDITORIAL_WORK_QUEUE_NOT_APPROVED"),
                    "review_note":"Confirm English sense and POS, Burmese translation, original example, word/sense-specific level and independent pronunciation before any learner release."
                })
            number=start//batch_size+1
            path=level_dir/f"batch-{number:02d}.json"
            payload={
                "schema":1, "release_status":"UNVERIFIED_DRAFT_DO_NOT_PUBLISH",
                "level":level, "batch":number,
                "curriculum_cefr_level_is_provisional":True,
                "entries":work
            }
            path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n","utf-8")
            inventory.append({"level":level,"batch":number,"path":str(path.relative_to(outdir)),
                              "first_word":work[0]["word"],"last_word":work[-1]["word"],
                              "candidate_count":len(work),
                              "first_drafts_pending_review":sum(
                                  r["status"]=="AI_ASSISTED_DRAFT_PENDING_INDEPENDENT_REVIEW" for r in work),
                              "independently_verified":0})
    drafted=Counter(x["level"] for x in starters_by_word.values())
    summary={"schema":1,"status":"A2_C1_UNVERIFIED_WORK_QUEUE_ONLY",
             "curriculum_targets":LEVELS,"total_candidates":sum(LEVELS.values()),
             "total_batches":len(inventory),"batch_size":batch_size,
             "unverified_original_first_drafts":len(starters_by_word),
             "unverified_first_drafts_by_level":dict(drafted),
             "missing_first_drafts":sum(LEVELS.values())-len(starters_by_word),
             "reviewed_burmese":0,"reviewed_levels":0,"approved_audio":0,
             "publication_allowed":False,"batches":inventory}
    (outdir/"INDEX.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n","utf-8")
    return summary

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json")
    parser.add_argument("--starters",type=Path,default=ROOT/"draft/A2-C1-EDITORIAL-STARTER.json")
    parser.add_argument("--output",type=Path,default=ROOT/"scratch/cefr-a2-c1-work-packets")
    args=parser.parse_args()
    d=json.loads(args.source.read_text("utf-8"))
    s=json.loads(args.starters.read_text("utf-8"))
    result=prepare(d,s,args.output)
    print(f"PASS: {result['total_batches']} packets covering {result['total_candidates']} A2-C1 candidates")
    print(f"Original AI-assisted drafts awaiting independent verification: {result['unverified_original_first_drafts']}")
    print(f"Candidates without first draft: {result['missing_first_drafts']}")
    for level,count in LEVELS.items():
        sample=next(x for x in result["batches"] if x["level"]==level)
        print(f"{level}: {count} candidates; first packet {sample['first_word']} .. {sample['last_word']}; first drafts {result['unverified_first_drafts_by_level'].get(level,0)}")
    print("No claimed source approval, translation verification, CEFR certification or audio listening QA.")
    print("No website publication: private CI artifacts only.")

if __name__=="__main__":
    main()
