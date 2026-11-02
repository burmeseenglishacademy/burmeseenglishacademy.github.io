#!/usr/bin/env python3
"""Staging-only integrity audit of six Cambridge-indexed B2 sense research cards.
Search-index CEFR leads and synthetic mutations are NOT independent human review.
"""
import argparse
import collections
import copy
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B2-SIX-FOUNDATIONAL-SENSE-CAMBRIDGE-INDEXED-TRIAGE-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_BLOB = "0ba6e9d43fc44cad0407945f2d76a052e25c85ef"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_BLOB = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
EXPECTED = {
    "colour": ("noun", 845, "A1", "B2_VS_INDEXED_A1_FOUNDATIONAL_COLOUR_NOUN", "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"),
    "repeat": ("verb", 850, "A2", "B2_VS_INDEXED_A2_SAY_AGAIN_VERB", "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"),
    "speaker": ("noun", 852, "B1", "B2_VS_INDEXED_B1_PUBLIC_SPEECH_NOUN", "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"),
    "appointment": ("noun", 490, "A2", "B2_VS_INDEXED_A2_ARRANGED_MEETING_NOUN", "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"),
    "package": ("noun", 797, "B2", "B2_INDEXED_ALIGNMENT_CONTROL_SERVICE_BUNDLE", "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"),
    "graduate": ("verb", 489, "B2", "B2_TRANSLATION_INDEX_ALIGNMENT_CONTROL_UK_VERB", "PUBLIC_BILINGUAL_TRANSLATION_INDEX_ONLY_DIRECT_HEADWORD_HTTP_403"),
}

def fail(msg):
    raise ValueError(msg)

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def held(item, label):
    if item.get("editorial_hold") is not True:
        fail(label + ": editorial hold removed")
    for flag in FLAGS:
        if item.get(flag) is not False:
            fail(label + ": false/missing review flag " + flag)
    if item.get("independently_approved", False) is not False:
        fail(label + ": forged independent approval")

def validate(packet, shortlist, source):
    if packet.get("schema") != 1 or packet.get("created_on") != "2026-11-02":
        fail("packet schema/date")
    if (packet.get("branch") != "cefr-5000-bilingual-qa-staging"
        or packet.get("scope") != "USER_APPROVED_1000_TOTAL_NOT_5000"
        or packet.get("release_status") != "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"
        or packet.get("shortlist_path") != "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
        or packet.get("shortlist_blob_sha") != SHORTLIST_BLOB):
        fail("packet scope, hold or provenance")
    limitations = packet.get("source_limitations", "")
    if not all(t in limitations for t in ("HTTP 403", "search-index", "does not establish", "unapproved", "not the direct English headword")):
        fail("publisher-access or independent-review limitations absent")
    target = {x: 200 for x in LEVELS}
    zeros = {x: 0 for x in LEVELS}
    if packet.get("counts_by_level") != target or packet.get("independently_approved_by_level") != zeros:
        fail("packet quotas or approval totals")
    entries = shortlist.get("entries", [])
    if (len(entries) != 1000 or shortlist.get("counts_by_level") != target
        or shortlist.get("independently_approved_by_level") != zeros
        or dict(collections.Counter(x.get("level") for x in entries)) != target):
        fail("shortlist quotas")
    heads = [x.get("word", "").casefold() for x in entries]
    if len(set(heads)) != 1000:
        fail("shortlist duplicated headword")
    by_word = {x["word"]: x for x in entries if x.get("level") == "B2"}
    records = packet.get("records")
    if (not isinstance(records, list) or len(records) != 6
        or packet.get("research_record_count") != 6
        or {x.get("word") for x in records} != set(EXPECTED)):
        fail("research headwords or count")
    for record in records:
        word = record["word"]
        pos, index, badge, risk, access = EXPECTED[word]
        if record.get("level") != "B2" or record.get("part_of_speech") != pos:
            fail(word + ": part of speech or level")
        original = record.get("frozen_original")
        if original != by_word[word]:
            fail(word + ": changed frozen record")
        if (original.get("source_path") != "draft/A2-C1-EDITORIAL-STARTER.json"
            or original.get("source_blob_sha") != SOURCE_BLOB
            or original.get("source_index") != index):
            fail(word + ": historical source provenance")
        historical = source["entries"][index]
        for key in ("word", "level", "part_of_speech", "english_definition",
                    "burmese_meaning", "example_sentence"):
            if original.get(key) != historical.get(key):
                fail(word + ": historical bilingual field " + key)
        held(original, word + " frozen")
        held(record, word + " research")
        if record.get("independently_approved") is not False or record.get("proposed_alternative_unapproved") is not True:
            fail(word + ": approval/proposal markers")
        if record.get("observed_on") != "2026-11-02" or record.get("risk_category") != risk:
            fail(word + ": observation date/risk")
        for field in ("proposed_english_definition", "proposed_myanmar_meaning",
                      "proposed_original_example", "evidence_note"):
            if not isinstance(record.get(field), str) or len(record[field].strip()) < 20:
                fail(word + ": substantive field " + field)
        if not any("\\u1000" <= c <= "\\u109f" for c in record["proposed_myanmar_meaning"]):
            fail(word + ": Myanmar script missing")
        if word not in record["proposed_original_example"].casefold():
            fail(word + ": example does not use target headword")
        cam = record.get("cambridge_indexed")
        if not isinstance(cam, dict):
            fail(word + ": missing indexed evidence")
        if (cam.get("url") != "https://dictionary.cambridge.org/dictionary/english/" + word
            or cam.get("access") != access or cam.get("observed_cefr_badge") != badge
            or cam.get("purpose") != "SOURCE_RESEARCH_NOT_INDEPENDENT_CEFR_SIGNOFF"
            or cam.get("observation_method") != "PUBLIC_WEB_SEARCH_INDEX_RESULT; DIRECT_HEADWORD_OPEN_RETURNED_HTTP_403"
            or len(str(cam.get("observed_sense", ""))) < 22):
            fail(word + ": publisher URL, badge, sense or access provenance")
        if word == "graduate":
            if cam.get("support_url") != "https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94-%E8%8B%B1%E8%AA%9E/%E5%A4%A7%E5%AD%B8":
                fail("graduate: missing weaker translation-index provenance")
        elif cam.get("support_url") is not None:
            fail(word + ": unexpected translation-index locator")
    return {"level":"B2", "research_records":6, "indexed_lower_level_conflicts":4,
            "indexed_B2_alignment_controls":2, "independent_approvals":0,
            "listening_signoffs":0, "release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist, source):
    validate(packet, shortlist, source)
    count = 0
    simple = [
        ("level","C1"), ("part_of_speech","adjective"), ("observed_on","2026-11-03"),
        ("risk_category","INDEPENDENTLY_APPROVED"), ("editorial_hold",False),
        ("independently_approved",True), ("proposed_alternative_unapproved",False),
        ("reviewed_english",True), ("reviewed_burmese",True), ("reviewed_example",True),
        ("reviewed_level",True), ("reviewed_pronunciation",True), ("release_approved",True),
        ("proposed_myanmar_meaning","English only"), ("proposed_original_example","No headword here."),
        ("evidence_note","fake")
    ]
    nested = [
        ("cambridge_indexed","url","https://dictionary.cambridge.org/blog/colour"),
        ("cambridge_indexed","access","DIRECT_PAGE_OPENED"),
        ("cambridge_indexed","observed_cefr_badge","C1"),
        ("cambridge_indexed","purpose","INDEPENDENT_CEFR_APPROVED"),
        ("cambridge_indexed","observation_method","DIRECT_PUBLISHER_VERIFIED"),
        ("frozen_original","source_index",0),
        ("frozen_original","english_definition","forged"),
        ("frozen_original","burmese_meaning","forged"),
        ("frozen_original","example_sentence","forged"),
        ("frozen_original","reviewed_english",True)
    ]
    for i in range(6):
        for key,value in simple:
            changed=copy.deepcopy(packet)
            changed["records"][i][key]=value
            try: validate(changed,shortlist,source)
            except (ValueError,KeyError,TypeError,IndexError): count+=1
            else: fail("synthetic forged record accepted: "+str((i,key)))
        for group,key,value in nested:
            changed=copy.deepcopy(packet)
            changed["records"][i][group][key]=value
            try: validate(changed,shortlist,source)
            except (ValueError,KeyError,TypeError,IndexError): count+=1
            else: fail("synthetic forged nested evidence accepted: "+str((i,group,key)))
    for key,value in [("release_status","APPROVED"),("shortlist_blob_sha","0"*40),
                      ("counts_by_level",{x:201 for x in LEVELS}),
                      ("independently_approved_by_level",{x:200 for x in LEVELS}),
                      ("source_limitations","Verified"),("research_record_count",5)]:
        changed=copy.deepcopy(packet)
        changed[key]=value
        try: validate(changed,shortlist,source)
        except (ValueError,KeyError,TypeError,IndexError): count+=1
        else: fail("synthetic forged packet accepted: "+key)
    return count

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    for path,sha in ((PACKET,PACKET_BLOB),(SHORTLIST,SHORTLIST_BLOB),(SOURCE,SOURCE_BLOB)):
        if blob_sha(path)!=sha:
            fail("pinned Git blob changed: "+str(path.relative_to(ROOT)))
    packet,shortlist,source=map(load,(PACKET,SHORTLIST,SOURCE))
    result=validate(packet,shortlist,source)
    result["lane"]=args.level
    if args.self_test:
        result["synthetic_mutations_rejected"]=self_test(packet,shortlist,source)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))

if __name__=="__main__":
    main()
