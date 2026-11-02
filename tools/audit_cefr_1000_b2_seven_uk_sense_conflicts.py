#!/usr/bin/env python3
"""Fail-closed staging research-integrity audit. Never treats publisher leads as human approval."""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-B2-SEVEN-QUOTE-TIE-RAW-LIFT-SHOCK-SILENCE-CABINET-EXACT-SENSE-2026-11-02.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
PINNED = {
    PACKET: "270ea37bc516c3670f7040acbb5d35ed2fbe332c",
    SHORTLIST: "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
    SOURCE: "b04dd85db5cfae131c25aa4c73109778991b6fdc",
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FLAGS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
         "reviewed_level", "reviewed_pronunciation", "release_approved")
# Word: (historical index, Oxford path, exact line locator, Cambridge URL suffix,
#        indexed badge, research risk)
EXPECTED = {
    "raw": (544, "raw_1", "107-127", "dictionary/english/raw", "B1",
            "B2_VS_INDEXED_B1_FOOD_ADJECTIVE"),
    "lift": (555, "lift_1", "113-126", "dictionary/english/lift", "B1",
             "B2_VS_INDEXED_B1_RAISE_VERB"),
    "shock": (800, "shock_1", "106-125", "dictionary/english/shock", "B1",
              "B2_VS_INDEXED_B1_EMOTIONAL_NOUN"),
    "silence": (801, "silence_1", "107-113;146-153", "dictionary/english/silence", "B1",
                "B2_VS_INDEXED_B1_UNCOUNTABLE_QUIET_NOUN"),
    "quote": (551, "quote_1", "113-138;185-197", None, None,
              "B2_VS_OXFORD_B1_TOPIC_NOT_SENSE_BADGE"),
    "tie": (552, "tie_1", "113-123;103-108", "dictionary/english/tie", None,
            "B2_UNSUBSTANTIATED_FASTEN_VERB_SENSE"),
    "cabinet": (563, "cabinet", "105-123;149-156", "dictionary/learner-english/cabinet", "B2",
                "B2_LEARNER_INDEX_FURNITURE_ALIGNMENT_WITH_OXFORD_TOPIC_CONFLICT"),
}
CAM_SENSE = {
    "raw": "raw adjective (NOT COOKED)",
    "lift": "lift verb (RAISE)",
    "shock": "shock noun (SURPRISE)",
    "silence": "silence noun (QUIET), uncountable",
    "tie": "tie verb (FASTEN) indexed definition, no CEFR badge observed",
    "cabinet": "cabinet noun (furniture with shelves or drawers)",
}

def fail(message):
    raise ValueError(message)

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def held(item, context):
    if item.get("editorial_hold") is not True:
        fail(context + ": editorial hold not true")
    for field in FLAGS:
        if item.get(field) is not False:
            fail(context + ": missing or forged false flag " + field)
    if item.get("independently_approved", False) is not False:
        fail(context + ": forged independent approval")

def validate(packet, shortlist, source):
    target = {level: 200 for level in LEVELS}
    zeros = {level: 0 for level in LEVELS}
    if (packet.get("schema") != 1 or packet.get("created_on") != "2026-11-02"
        or packet.get("branch") != "cefr-5000-bilingual-qa-staging"
        or packet.get("scope") != "USER_APPROVED_1000_TOTAL_NOT_5000"
        or packet.get("release_status") != "STAGING_EDITORIAL_HOLD_DO_NOT_PUBLISH"
        or packet.get("shortlist_path") != "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
        or packet.get("shortlist_blob_sha") != PINNED[SHORTLIST]
        or packet.get("source_path") != "draft/A2-C1-EDITORIAL-STARTER.json"
        or packet.get("source_blob_sha") != PINNED[SOURCE]):
        fail("packet metadata, branch, scope or historical provenance")
    limits = packet.get("source_limitations", "")
    for token in ("directly opened", "search-index", "HTTP 403", "not exact-sense CEFR badges",
                  "different dictionary subproduct", "unapproved", "not independently",
                  "No British George/Emma audio listened", "physical iPhone"):
        if token not in limits:
            fail("source limitation removed: " + token)
    if (packet.get("counts_by_level") != target
        or packet.get("independently_approved_by_level") != zeros):
        fail("packet counts/approval")
    entries = shortlist.get("entries")
    if not isinstance(entries, list) or len(entries) != 1000:
        fail("shortlist size")
    if (shortlist.get("counts_by_level") != target
        or shortlist.get("independently_approved_by_level") != zeros
        or dict(collections.Counter(x.get("level") for x in entries)) != target):
        fail("shortlist per-level counts")
    words = [x.get("word", "").casefold() for x in entries]
    if len(set(words)) != 1000:
        fail("shortlist duplicate headwords")
    if any(x.get("editorial_hold") is not True or
           any(x.get(f) is not False for f in FLAGS) for x in entries):
        fail("shortlist unreviewed holds/flags")
    frozen = {x["word"]: x for x in entries if x.get("level") == "B2"}
    records = packet.get("records")
    if (not isinstance(records, list) or len(records) != 7
        or packet.get("research_record_count") != 7
        or {x.get("word") for x in records} != set(EXPECTED)):
        fail("record quota/identity")
    for rec in records:
        word = rec["word"]
        index, oxpath, locator, campath, badge, risk = EXPECTED[word]
        if rec.get("level") != "B2" or rec.get("part_of_speech") != frozen[word]["part_of_speech"]:
            fail(word + ": wrong level/POS")
        original = rec.get("frozen_original")
        if original != frozen[word]:
            fail(word + ": frozen original modified")
        if (original.get("source_path") != "draft/A2-C1-EDITORIAL-STARTER.json"
            or original.get("source_index") != index
            or original.get("source_blob_sha") != PINNED[SOURCE]):
            fail(word + ": historical source reference")
        historical = source["entries"][index]
        for key in ("word", "level", "part_of_speech", "english_definition",
                    "burmese_meaning", "example_sentence"):
            if original.get(key) != historical.get(key):
                fail(word + ": historical source field " + key)
        held(original, word + " frozen")
        held(rec, word + " packet")
        if (rec.get("independently_approved") is not False
            or rec.get("proposed_alternative_unapproved") is not True
            or rec.get("observed_on") != "2026-11-02"
            or rec.get("risk_category") != risk):
            fail(word + ": false approval, date or risk")
        ox = rec.get("oxford_direct")
        if (not isinstance(ox, dict)
            or ox.get("url") != "https://www.oxfordlearnersdictionaries.com/definition/english/" + oxpath
            or ox.get("access") != "DIRECT_PAGE_OPENED"
            or ox.get("line_locator") != locator
            or ox.get("observed_exact_sense_cefr_badge") is not None
            or ox.get("observation_method") !=
                "DIRECT_PUBLISHER_WEB_OPEN; HEADWORD_AND_SENSE_LINES_ONLY; TOPIC_LABELS_NOT_CEFR_BADGES"
            or len(str(ox.get("observed_sense", ""))) < 25):
            fail(word + ": Oxford evidence, footer/CEFR conflation or locator")
        cam = rec.get("cambridge_indexed")
        if campath is None:
            if cam is not None:
                fail(word + ": fabricated Cambridge evidence")
        else:
            if (not isinstance(cam, dict)
                or cam.get("url") != "https://dictionary.cambridge.org/" + campath
                or cam.get("access") != "PUBLIC_SEARCH_INDEX_ONLY_DIRECT_HTTP_403"
                or cam.get("observed_sense") != CAM_SENSE[word]
                or cam.get("observed_cefr_badge") != badge
                or cam.get("observation_method") !=
                    "PUBLIC_WEB_SEARCH_INDEX_RESULT; DIRECT_PUBLISHER_OPEN_RETURNED_HTTP_403"
                or cam.get("purpose") != "RESEARCH_LEAD_NOT_INDEPENDENT_REVIEW"):
                fail(word + ": Cambridge index URL/badge/access conflation")
        for key in ("proposed_english_definition", "proposed_myanmar_meaning",
                    "proposed_original_example", "evidence_note"):
            if not isinstance(rec.get(key), str) or len(rec[key].strip()) < 22:
                fail(word + ": missing substantive bilingual field " + key)
        if not any("\u1000" <= c <= "\u109f" for c in rec["proposed_myanmar_meaning"]):
            fail(word + ": proposed Myanmar script missing")
        if word not in rec["proposed_original_example"].casefold():
            fail(word + ": proposed example missing headword")
    return {
        "held_research_records": 7, "B2_indexed_B1_conflicts": 4,
        "B2_indexed_alignment_controls": 1, "CEFR_unsubstantiated_leads": 2,
        "independently_approved": 0, "George_Emma_listening_signoffs": 0,
        "release": "BLOCKED_STAGING_ONLY",
    }

def self_test(packet, shortlist, source):
    validate(packet, shortlist, source)
    mutations = 0
    def reject(obj, label):
        nonlocal mutations
        try:
            validate(obj, shortlist, source)
        except (ValueError, KeyError, TypeError, IndexError):
            mutations += 1
        else:
            fail("synthetic forgery accepted: " + label)
    fields = [
        ("level", "C1"), ("part_of_speech", "adverb"), ("observed_on", "2026-11-03"),
        ("risk_category", "INDEPENDENTLY_VERIFIED"), ("editorial_hold", False),
        ("independently_approved", True), ("proposed_alternative_unapproved", False),
        ("reviewed_english", True), ("reviewed_burmese", True),
        ("reviewed_example", True), ("reviewed_level", True),
        ("reviewed_pronunciation", True), ("release_approved", True),
        ("proposed_english_definition", "fake"), ("proposed_myanmar_meaning", "English only"),
        ("proposed_original_example", "No target term here."), ("evidence_note", "fake"),
    ]
    nested = [
        ("oxford_direct", "url", "https://www.oxfordlearnersdictionaries.com/blog/raw"),
        ("oxford_direct", "access", "DIRECT_INDEPENDENT_REVIEW"),
        ("oxford_direct", "line_locator", "footer"),
        ("oxford_direct", "observed_exact_sense_cefr_badge", "B2"),
        ("oxford_direct", "observation_method", "HUMAN_REVIEWED"),
        ("frozen_original", "source_index", 0),
        ("frozen_original", "english_definition", "fake"),
        ("frozen_original", "burmese_meaning", "fake"),
        ("frozen_original", "example_sentence", "fake"),
        ("frozen_original", "reviewed_level", True),
    ]
    for i, rec in enumerate(packet["records"]):
        for key, value in fields:
            mutated = copy.deepcopy(packet)
            mutated["records"][i][key] = value
            reject(mutated, str((i, key)))
        for group, key, value in nested:
            mutated = copy.deepcopy(packet)
            mutated["records"][i][group][key] = value
            reject(mutated, str((i, group, key)))
        if rec["cambridge_indexed"] is not None:
            for key, value in (
                ("url", "https://dictionary.cambridge.org/blog/cefr"),
                ("access", "DIRECT_PUBLISHER_VERIFIED"),
                ("observed_sense", "fabricated sense"),
                ("observed_cefr_badge", "C1"),
                ("purpose", "INDEPENDENT_REVIEW"),
                ("observation_method", "DIRECT_VERIFIED"),
            ):
                mutated = copy.deepcopy(packet)
                mutated["records"][i]["cambridge_indexed"][key] = value
                reject(mutated, str((i, "cambridge_indexed", key)))
        else:
            mutated = copy.deepcopy(packet)
            mutated["records"][i]["cambridge_indexed"] = {"url": "https://dictionary.cambridge.org/dictionary/english/quote"}
            reject(mutated, "quote forged Cambridge evidence")
    for key, value in (
        ("branch", "main"), ("scope", "5000"), ("release_status", "APPROVED"),
        ("shortlist_blob_sha", "0" * 40), ("source_blob_sha", "0" * 40),
        ("source_limitations", "Independent source review complete"),
        ("counts_by_level", {x: 201 for x in LEVELS}),
        ("independently_approved_by_level", {x: 200 for x in LEVELS}),
        ("research_record_count", 6),
    ):
        mutated = copy.deepcopy(packet)
        mutated[key] = value
        reject(mutated, key)
    mutated = copy.deepcopy(packet)
    mutated["records"].pop()
    reject(mutated, "missing record")
    return mutations

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    for path, expected in PINNED.items():
        if git_blob(path) != expected:
            fail("pinned Git blob mismatch: " + str(path.relative_to(ROOT)))
    packet, shortlist, source = map(load, (PACKET, SHORTLIST, SOURCE))
    result = validate(packet, shortlist, source)
    result["lane"] = args.level
    if args.self_test:
        result["synthetic_mutations_rejected"] = self_test(packet, shortlist, source)
    print(json.dumps(result, sort_keys=True, ensure_ascii=False))

if __name__ == "__main__":
    main()
