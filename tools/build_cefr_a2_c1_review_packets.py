#!/usr/bin/env python3
"""Prepare 45 A2–C1 editorial work packets without publishing draft vocabulary.

Candidate headwords are automatically shortlisted and CEFR labels provisional.
WordNet first senses are *clues*, not approved learner definitions.
Manual bilingual/source/level review must precede any published release.
"""
import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = {"A2":700,"B1":1000,"B2":1300,"C1":1500}
FIELDS = ("reviewed_english","reviewed_burmese","reviewed_example",
          "reviewed_level","reviewed_pronunciation")

def prepare(source, outdir, batch_size=100):
    if batch_size < 1 or batch_size > 200:
        raise ValueError("batch_size must be between 1 and 200")
    if source.get("release_status") != "UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        raise ValueError("Do not export any published or supposedly approved content")
    rows = source.get("entries")
    if not isinstance(rows,list) or len(rows) != 5000:
        raise ValueError("Expected the complete 5000-candidate inventory")
    if len({row["word"] for row in rows}) != 5000:
        raise ValueError("Duplicate word in candidate inventory")
    counts = Counter(r["level"] for r in rows)
    if counts != Counter({"A1":500, **LEVELS}):
        raise ValueError(f"Unexpected provisional levels: {counts}")
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
                if row.get("burmese_meaning") or row.get("example_sentence"):
                    raise ValueError(f"Candidate content unexpectedly populated: {row['word']}")
                work.append({
                    "word":row["word"], "provisional_level":level,
                    "provisional_pos":row.get("part_of_speech",""),
                    "wordnet_first_sense_clue_not_verified":row.get("english_definition_draft",""),
                    "wordnet_sense_id":row.get("lexical_sense_id",""),
                    "zipf_frequency":row.get("zipf_frequency"),
                    "english_definition":"", "burmese_meaning":"",
                    "example_sentence":"", "part_of_speech":"",
                    "source_english":"", "source_burmese":"", "source_level":"",
                    **{field:False for field in FIELDS},
                    "status":"EDITORIAL_WORK_QUEUE_NOT_APPROVED",
                    "review_note":"Verify POS/sense, independently translate and confirm meaning, provide original sentence, confirm sense-specific level; audio only after text is frozen."
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
                              "candidate_count":len(work),"independently_verified":0})
    summary={"schema":1,"status":"A2_C1_UNVERIFIED_WORK_QUEUE_ONLY",
             "curriculum_targets":LEVELS,"total_candidates":sum(LEVELS.values()),
             "total_batches":len(inventory),"batch_size":batch_size,
             "reviewed_burmese":0,"reviewed_levels":0,"approved_audio":0,
             "publication_allowed":False,"batches":inventory}
    (outdir/"INDEX.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n","utf-8")
    return summary

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source",type=Path,default=ROOT/"draft/UNVERIFIED_CEFR_CANDIDATES.json")
    parser.add_argument("--output",type=Path,default=ROOT/"scratch/cefr-a2-c1-work-packets")
    args=parser.parse_args()
    d=json.loads(args.source.read_text("utf-8"))
    result=prepare(d,args.output)
    print(f"PASS: {result['total_batches']} review packets for {result['total_candidates']} A2-C1 candidates")
    for level, count in LEVELS.items():
        sample=next(x for x in result["batches"] if x["level"]==level)
        print(f"{level}: {count} candidates; first packet {sample['first_word']} .. {sample['last_word']}")
    print("All meanings, examples, source evidence, level judgments and audio reviews remain PENDING.")
    print("Output stored only as GitHub Actions review artifacts, NEVER added to the live web page.")

if __name__=="__main__":
    main()
