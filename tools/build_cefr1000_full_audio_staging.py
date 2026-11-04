#!/usr/bin/env python3
"""Make staging-only, UNREVIEWED George/Emma CEFR-1000 audio in deterministic shards.

The source is the frozen 1,000-word provisional shortlist; 54 lessons and the
existing IELTS audio/library are preserved. This tool never edits existing
audio files, main, the live site, or any independent approval flags.

Usage:
 python tools/build_cefr1000_full_audio_staging.py --shard 0 --shards 16
 python tools/build_cefr1000_full_audio_staging.py --validate-complete
"""
import argparse
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
from collections import Counter, defaultdict

ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCE=ROOT/"draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
MANIFEST=ROOT/"audio-manifest.js"
OUT=ROOT/"scratch/cefr1000-full-audio-unreviewed"
VOICES=("bm_george","bf_emma")
LEVELS=("A1","A2","B1","B2","C1")
SHARDS=16


def entries_and_texts():
    d=json.loads(SOURCE.read_text("utf-8"))
    assert d["release_status"]=="PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH"
    rows=d["entries"]
    assert len(rows)==1000 and Counter(e["level"] for e in rows)==dict.fromkeys(LEVELS,200)
    assert all(e["editorial_hold"] is True and e["release_approved"] is False for e in rows)
    sources=defaultdict(list)
    for idx,e in enumerate(rows):
        for kind,txt in (("headword",e.get("display_word") or e["word"]),
                         ("example",e["example_sentence"])):
            assert isinstance(txt,str) and txt.strip()
            t=txt.strip()
            sources[t].append({"index":idx,"word":e["word"],
                              "level":e["level"],"kind":kind,
                              "part_of_speech":e.get("part_of_speech")})
    items=[]
    for t,uses in sources.items():
        txt_sha=hashlib.sha256(t.encode("utf-8")).hexdigest()
        items.append({"text":t,"sha256_text":txt_sha,"id":txt_sha[:24],
                     "uses":uses})
    items.sort(key=lambda x:x["id"])
    assert len(items)==1996,(len(items),"unexpected distinct text count")
    assert len({x["id"] for x in items})==len(items)
    return d,items


def production_manifest():
    raw=MANIFEST.read_text("utf-8")
    tag="window.BEA_AUDIO_MANIFEST="
    d=json.loads(raw.split(tag,1)[1].strip().removesuffix(";"))
    assert len(d["clips"])==2326,"protected legacy audio manifest changed"
    return d["clips"]


def probe(p, decode=False):
    q=subprocess.run(["ffprobe","-v","error",
         "-show_entries","stream=codec_name,sample_rate,channels:format=duration",
         "-of","json",str(p)],capture_output=True,text=True)
    if q.returncode:
        raise RuntimeError(f"FFprobe failed: {p} {q.stderr[:200]}")
    meta=json.loads(q.stdout)
    audio=next((x for x in meta["streams"] if x.get("codec_name")=="mp3"),None)
    if (not audio or audio.get("sample_rate")!="24000"
         or audio.get("channels")!=1 or float(meta["format"]["duration"])<.12
         or p.stat().st_size<=500):
        raise RuntimeError(f"Invalid MP3 format: {p}")
    if decode:
        subprocess.run(["ffmpeg","-nostdin","-v","error","-xerror",
                        "-i",str(p),"-f","null","-"],
                        stdout=subprocess.DEVNULL,check=True)
    return {"duration_s":round(float(meta["format"]["duration"]),3),
            "bytes":p.stat().st_size,
            "sha256_audio":hashlib.sha256(p.read_bytes()).hexdigest()}


def generate_one_shard(shard,shards):
    if shards!=SHARDS or not 0<=shard<shards:
        raise ValueError("Must use 16 shards with valid 0-based index")
    d,items=entries_and_texts()
    legacy=production_manifest()
    chosen=[x for index,x in enumerate(items) if index%shards==shard]
    expected_ids={x["id"] for x in chosen}
    folder=OUT / f"shard-{shard:02d}"
    records=[]
    synth=None
    generated=0
    reused=0
    sys.path.insert(0,str(ROOT/"tools"))
    from build_kokoro_audio import synthesize
    for index,entry in enumerate(chosen,1):
        for voice in VOICES:
            rel=pathlib.Path("audio") / voice / f"{entry['id']}.mp3"
            target=folder/rel
            original=f"audio/{voice}/{entry['id']}.mp3"
            legacy_path=ROOT/original
            if legacy.get(entry["text"],{}).get(voice)==original:
                if not legacy_path.exists():
                    raise RuntimeError(f"Protected manifest points to missing file {original}")
                probe(legacy_path,decode=False)
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(legacy_path,target)
                provenance="EXACT_TEXT_REUSE_FROM_PRODUCTION"
                reused+=1
            else:
                if synth is None:
                    from kokoro import KPipeline
                    synth=KPipeline(lang_code="b")
                target.parent.mkdir(parents=True,exist_ok=True)
                synthesize(synth,entry["text"],voice,target)
                provenance="NEW_UNREVIEWED_KOKORO_SYNTHESIS"
                generated+=1
            media=probe(target,decode=True)
            records.append({"text":entry["text"],"sha256_text":entry["sha256_text"],
                    "id":entry["id"],"uses":entry["uses"],"voice":voice,
                    "path":rel.as_posix(),"origin":provenance,
                    "listening_review":"NOT_PERFORMED",
                    "independent_approval":False,**media})
        if index%25==0:
            print(f"shard={shard} completed {index}/{len(chosen)} distinct texts",flush=True)
    assert len(records)==len(chosen)*2
    assert len(expected_ids)==len(chosen)
    report={"schema":1,"status":"STAGING_UNREVIEWED_NOT_APPROVED_NOT_DEPLOYED",
            "source_blob_sha":"475e68ae17ab97bd937e73e5ce4794e0dcd76551",
            "shard":shard,"shards":shards,"text_count":len(chosen),
            "recording_count":len(records),"generated_recordings":generated,
            "reused_recordings":reused,"human_listening_approvals":0,
            "records":records}
    reports=folder/"reports"
    reports.mkdir(parents=True,exist_ok=True)
    (reports/f"shard-{shard:02d}.json").write_text(
        json.dumps(report,ensure_ascii=False,separators=(",",":"))+"\n","utf-8")
    print(json.dumps({"shard":shard,"recordings":len(records),
                      "new":generated,"reused":reused,"human_approvals":0}))


def validate_complete():
    d,items=entries_and_texts()
    exact=set()
    counts=Counter()
    all_paths=set()
    records={}
    for shard in range(SHARDS):
        p=OUT/"reports"/f"shard-{shard:02d}.json"
        data=json.loads(p.read_text("utf-8"))
        assert data["shard"]==shard and data["shards"]==SHARDS
        assert data["status"]=="STAGING_UNREVIEWED_NOT_APPROVED_NOT_DEPLOYED"
        assert data["human_listening_approvals"]==0
        assert data["recording_count"]==len(data["records"])
        for rec in data["records"]:
            key=(rec["sha256_text"],rec["voice"])
            if key in records:
                raise RuntimeError("Duplicate recording in shard reports")
            records[key]=rec
            counts[rec["voice"]]+=1
    total_bytes=0
    for item in items:
        for voice in VOICES:
            key=(item["sha256_text"],voice)
            if key not in records: raise RuntimeError(f"Missing {key}")
            rec=records[key]
            rel=f"audio/{voice}/{item['id']}.mp3"
            assert rec["path"]==rel
            assert rec["text"]==item["text"]
            assert rec["sha256_text"]==item["sha256_text"]
            assert rec["listening_review"]=="NOT_PERFORMED" and rec["independent_approval"] is False
            path=OUT/rel
            assert path.is_file(),rel
            media=probe(path,decode=False)
            assert media["sha256_audio"]==rec["sha256_audio"],rel
            total_bytes+=media["bytes"]
            all_paths.add(rel)
    assert len(records)==len(all_paths)==3992
    assert all(counts[x]==1996 for x in VOICES)
    assert total_bytes<700_000_000, "GitHub Pages asset preflight budget exceeded"
    output={"state":"COMPLETE_TECHNICAL_UNREVIEWED_AUDIO_CANDIDATE_NO_DEPLOYMENT",
            "source_sha256":hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "distinct_texts":len(items),"recordings":len(records),
            "per_voice":dict(counts),"total_audio_bytes":total_bytes,
            "human_listening_signoffs":0,"independent_word_approvals":0,
            "issues":["Output may need regeneration after source content changes.",
                      "Kokoro pronunciation/UK accent not verified by a human listener.",
                      "Source shortlist is provisional and not published.",
                      "This is technical file coverage, not an approved release."]}
    (OUT/"technical-inventory.json").write_text(
        json.dumps(output,ensure_ascii=False,indent=2)+"\n","utf-8")
    print(json.dumps(output,indent=2))
    print("PASS 3992 audio files technically complete; NO human approvals or deployment")


if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--shard",type=int)
    ap.add_argument("--shards",type=int,default=SHARDS)
    ap.add_argument("--validate-complete",action="store_true")
    args=ap.parse_args()
    if args.validate_complete:
        validate_complete()
    else:
        if args.shard is None: ap.error("--shard is required for generation")
        generate_one_shard(args.shard,args.shards)
