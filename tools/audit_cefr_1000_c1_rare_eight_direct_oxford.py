#!/usr/bin/env python3
"""Frozen, source-bound C1 eight-card Oxford research auditor. NEVER approves content."""
import argparse
import copy
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-C1-EIGHT-DIRECT-OXFORD-RARE-SENSE-TRIAGE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "fd87b46061fc7240ff297ea4e117d497a7c00913"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
WORDS = ("ambivalence", "anachronism", "antipathy", "arbitrate",
         "belligerent", "benevolent", "brevity", "circumspect")
SLUGS = ("ambivalence", "anachronism", "antipathy", "arbitrate",
         "belligerent_1", "benevolent", "brevity", "circumspect")
LINES = ("101-107", "101-109", "101-110", "101-118",
         "101-110", "101-119", "101-115", "101-106")
LEVELS = ("A1", "A2", "B1", "B2", "C1")
ROOT_FLAGS = {"scope":"USER_APPROVED_CEFR_1000_STAGING_ONLY",
              "status":"UNAPPROVED_C1_EIGHT_DIRECT_OXFORD_EXACT_SENSE_TRIAGE",
              "observed_on":"2026-11-01",
              "shortlist_blob_sha":SHORTLIST_BLOB,
              "real_george_emma_listening_signoffs":0,
              "production_status":"BLOCKED_STAGING_ONLY"}
ROW_FLAGS = {"editorial_hold":True, "independently_checked":False,
             "release_approved":False, "independent_reviewer_receipt":None,
             "real_george_listening":False, "real_emma_listening":False}
SOURCE_URL_PREFIX = "https://www.oxfordlearnersdictionaries.com/definition/english/"

def git_blob(path):
    p = subprocess.run(["git", "hash-object", str(path)], cwd=ROOT,
                       text=True, capture_output=True, check=True)
    return p.stdout.strip()

def validate(packet, shortlist, baseline=None):
    """Research integrity only; source presence is NOT human CEFR approval."""
    errors = []
    if not isinstance(packet, dict) or not isinstance(shortlist, dict):
        return ["Invalid packet or shortlist JSON root"]
    for k,v in ROOT_FLAGS.items():
        if packet.get(k) != v: errors.append("root " + k)
    if packet.get("schema") != 1: errors.append("schema")
    if packet.get("counts_by_level") != dict.fromkeys(LEVELS,0)|{"C1":8}:
        errors.append("packet level counts")
    if packet.get("first_pass_written_by_level") != dict.fromkeys(LEVELS,200):
        errors.append("written counts")
    if packet.get("independently_approved_by_level") != dict.fromkeys(LEVELS,0):
        errors.append("approval counts")
    if not isinstance(packet.get("publisher_scope_notice"),str) or "not independently verified" not in packet["publisher_scope_notice"]:
        errors.append("publisher evidence disclaimer")
    rows = packet.get("records")
    frozen = shortlist.get("entries")
    if not isinstance(rows,list) or len(rows)!=8 or not isinstance(frozen,list) or len(frozen)!=1000:
        return errors + ["row cardinality or frozen shortlist"]
    if shortlist.get("counts_by_level") != dict.fromkeys(LEVELS,200):
        errors.append("shortlist level counts")
    if shortlist.get("independently_approved_by_level") != dict.fromkeys(LEVELS,0):
        errors.append("shortlist approvals")
    if sum(bool(r.get("release_approved")) for r in frozen if isinstance(r,dict)):
        errors.append("shortlist contains approval")
    frozen_by_word = {r.get("word"):r for r in frozen if isinstance(r,dict)}
    for idx,(word,slug,locator,row) in enumerate(zip(WORDS,SLUGS,LINES,rows)):
        if not isinstance(row,dict):
            errors.append("nonobject row");continue
        if row.get("word")!=word or row.get("level")!="C1":
            errors.append(word+" identity")
        original = frozen_by_word.get(word)
        if not original or original.get("level")!="C1":
            errors.append(word+" absent from frozen shortlist");continue
        for src,dst in (("part_of_speech","part_of_speech"),
                        ("english_definition","original_english_definition"),
                        ("burmese_meaning","original_burmese_meaning"),
                        ("example_sentence","original_example_sentence"),
                        ("source_path","source_path"),
                        ("source_index","source_index"),
                        ("source_blob_sha","source_blob_sha")):
            if row.get(dst)!=original.get(src):
                errors.append(word+" original mismatch "+dst)
        for key,value in ROW_FLAGS.items():
            if row.get(key)!=value: errors.append(word+" false review/launch "+key)
        sources=row.get("oxford_direct_sources")
        if not isinstance(sources,list) or len(sources)!=1:
            errors.append(word+" source count");continue
        source=sources[0]
        if not isinstance(source,dict):
            errors.append(word+" source object");continue
        expected={"publisher":"Oxford University Press",
                  "url":SOURCE_URL_PREFIX+slug,
                  "observed_on":"2026-11-01",
                  "access":"DIRECT_PUBLISHER_PAGE_OPENED",
                  "line_locator":locator,
                  "evidence_scope":"EXACT_SENSE_POS_GRAMMAR_NOT_INDEPENDENT_CEFR"}
        if source!=expected: errors.append(word+" source URL/locator/provenance")
        for key in ("risk_class","source_supported_observation",
                    "suggested_myanmar_UNAPPROVED","suggested_example_UNAPPROVED",
                    "independent_reviewer_question"):
            if not isinstance(row.get(key),str) or len(row[key].strip())<20:
                errors.append(word+" incomplete "+key)
        if not re.search("[\u1000-\u109f]",str(row.get("suggested_myanmar_UNAPPROVED",""))):
            errors.append(word+" Myanmar missing")
        if word not in str(row.get("suggested_example_UNAPPROVED","")).lower():
            errors.append(word+" example lacks lemma")
        if baseline is not None and row!=baseline["records"][idx]:
            errors.append(word+" frozen editorial research changed")
    if baseline is not None and packet!=baseline:
        errors.append("frozen packet modified")
    return errors

def self_test(packet,shortlist):
    count=0
    for i in range(8):
        for field,value in (
            ("level","B2"),("original_burmese_meaning","အမှား"),
            ("original_english_definition","Wrong definition"),
            ("original_example_sentence","Wrong example."),
            ("source_blob_sha","0"*40),("independently_checked",True),
            ("release_approved",True),("real_george_listening",True),
            ("real_emma_listening",True),("suggested_myanmar_UNAPPROVED","bad"),
            ("risk_class","x"),("independent_reviewer_receipt",{"forged":True}),
        ):
            bad=copy.deepcopy(packet);bad["records"][i][field]=value
            if not validate(bad,shortlist,packet):
                raise AssertionError("missed row mutation "+str((i,field)))
            count+=1
        for field,value in (("url","https://example.com/definition/english/"+WORDS[i]),
                            ("line_locator","0-0"),("access","INDEXED_ONLY"),
                            ("observed_on","2025-01-01")):
            bad=copy.deepcopy(packet);bad["records"][i]["oxford_direct_sources"][0][field]=value
            if not validate(bad,shortlist,packet):
                raise AssertionError("missed source mutation "+str((i,field)))
            count+=1
    for key,value in (("status","APPROVED"),("counts_by_level",{"C1":8}),
                      ("independently_approved_by_level",{"C1":8}),
                      ("real_george_emma_listening_signoffs",8),
                      ("production_status","LIVE"),
                      ("shortlist_blob_sha","0"*40)):
        bad=copy.deepcopy(packet);bad[key]=value
        if not validate(bad,shortlist,packet):
            raise AssertionError("missed root mutation "+key)
        count+=1
    bad=copy.deepcopy(packet);bad["records"].pop()
    if not validate(bad,shortlist,packet):raise AssertionError("missed deleted row")
    count+=1
    print(f"PASS: {count}/{count} synthetic research/provenance/approval mutations rejected; NOT independent review")
    
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    for path,expected in ((PACKET,PACKET_BLOB),(SHORTLIST,SHORTLIST_BLOB)):
        if not path.is_file() or git_blob(path)!=expected:
            raise SystemExit("BLOCK: frozen Git blob mismatch "+str(path))
    packet=json.loads(PACKET.read_text("utf8"))
    shortlist=json.loads(SHORTLIST.read_text("utf8"))
    errors=validate(packet,shortlist)
    if errors:
        print("\n".join("BLOCK: "+x for x in errors[:20]),file=sys.stderr)
        raise SystemExit(1)
    if args.self_test:self_test(packet,shortlist)
    print(f"PASS: frozen eight C1 Oxford research records checked for {args.level}; 0 independent approvals; STAGING ONLY")
if __name__=="__main__":main()
