#!/usr/bin/env python3
"""Staging-only, fail-closed six B2 Oxford research handoff integrity check.

No linguistic, human, voice, physical-device, hosting or release approval.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
NOTE = ROOT / "draft/CEFR-1000-B2-SIX-PERSONALITY-SOMEWHAT-DIRECT-OXFORD-2026-11-03.md"
SOURCE = ROOT / "draft/A2-C1-EDITORIAL-STARTER.json"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
NOTE_SHA = "5651be5e77184b7f94d4836ee0bb4cacadc1a45f"
SOURCE_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
WORDS = ("personality", "relief", "resistance", "retail", "shame", "somewhat")
LEVELS = ("A1", "A2", "B1", "B2", "C1")
FORBIDDEN = ("reviewed_english", "reviewed_burmese", "reviewed_example",
             "reviewed_level", "reviewed_pronunciation", "release_approved")
OXFORD = {
 "personality": "https://www.oxfordlearnersdictionaries.com/definition/english/personality",
 "relief": "https://www.oxfordlearnersdictionaries.com/definition/english/relief",
 "resistance": "https://www.oxfordlearnersdictionaries.com/definition/english/resistance",
 "retail": "https://www.oxfordlearnersdictionaries.com/definition/english/retail_1",
 "shame": "https://www.oxfordlearnersdictionaries.com/definition/english/shame_1",
 "somewhat": "https://www.oxfordlearnersdictionaries.com/definition/english/somewhat",
}

def git_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def require(ok, reason):
    if not ok:
        raise AssertionError(reason)

def validate(short, note, source, *, enforce_blob=True):
    if enforce_blob:
        for data, sha, name in ((short, SHORT_SHA, "shortlist"),
                                (note, NOTE_SHA, "research note"),
                                (source, SOURCE_SHA, "historical source")):
            require(git_sha(data) == sha, name + " blob drift")
    s, src = json.loads(short), json.loads(source)
    entries = s["entries"]
    require(len(entries) == 1000, "not 1000 entries")
    for level in LEVELS:
        require(sum(x["level"] == level for x in entries) == 200, level + " count")
        require(s["counts_by_level"][level] == 200, level + " count metadata")
        require(s["independently_approved_by_level"][level] == 0, level + " false approvals")
    require(len({e["word"].casefold() for e in entries}) == 1000, "duplicate headwords")
    require(s["release_status"] == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH",
            "release status drift")
    note_text = note.decode("utf-8")
    require("3 November 2026" in note_text and "2026-11-03" in note_text,
            "source observation date missing")
    require("not 5,000" in note_text and "zero independent approvals" in note_text,
            "no-release caveat missing")
    require("topic" in note_text.lower() and "not" in note_text.lower(),
            "Oxford topic/headword CEFR warning missing")
    require(note_text.count("\n| **") == 6, "research table count")
    for i, word in enumerate(WORDS):
        e = next((x for x in entries if x["word"] == word and x["level"] == "B2"), None)
        require(e is not None and e["part_of_speech"] == ("adverb" if word == "somewhat" else "noun"),
                word + " missing or POS drift")
        require(e["source_path"] == "draft/A2-C1-EDITORIAL-STARTER.json"
                and e["source_index"] == 20 + i
                and e["source_blob_sha"] == SOURCE_SHA, word + " provenance drift")
        require(all(e.get(k) is False for k in FORBIDDEN) and e.get("editorial_hold") is True,
                word + " false review or hold")
        require(all(isinstance(e.get(k), str) and e[k].strip()
                    for k in ("english_definition", "burmese_meaning", "example_sentence")),
                word + " incomplete bilingual/example")
        # Exact original text is frozen by shortlist blob; source index binding additionally checked.
        require(word in note_text and OXFORD[word] in note_text, word + " source URL missing")
        require(e["english_definition"] in note_text
                and e["burmese_meaning"] in note_text
                and e["example_sentence"] in note_text, word + " original source text missing")
    require("Cambridge" in note_text and "B2" in note_text
            and "not a review receipt" in note_text, "publisher evidence caveat missing")
    require("No George/Emma audio generated or listened" in note_text
            and "no physical iPhone Safari test" in note_text
            and "no hosting clearance or deployment" in note_text, "release safeguards missing")
    return True

def self_test(short, note, source):
    validate(short, note, source)
    tests = 0
    for token in ("personality", "relief", "resistance", "retail", "shame", "somewhat",
                  "zero independent approvals", "topic", "3 November 2026",
                  "no physical iPhone Safari test", "not 5,000"):
        altered = note.replace(token, "FORGED", 1)
        require(altered != note, "self-test token absent: " + token)
        try:
            validate(short, altered, source)
        except AssertionError:
            tests += 1
        else:
            raise AssertionError("forged note accepted: " + token)
    for word in WORDS:
        obj = json.loads(short)
        e = next(x for x in obj["entries"] if x["word"] == word and x["level"] == "B2")
        e["release_approved"] = True
        forged = json.dumps(obj, ensure_ascii=False).encode()
        try:
            validate(forged, note, source, enforce_blob=False)
        except AssertionError:
            tests += 1
        else:
            raise AssertionError("forged approval accepted: " + word)
    for level in LEVELS:
        obj = json.loads(short)
        obj["independently_approved_by_level"][level] = 1
        try:
            validate(json.dumps(obj, ensure_ascii=False).encode(), note, source, enforce_blob=False)
        except AssertionError:
            tests += 1
        else:
            raise AssertionError("false level count accepted: " + level)
    print(f"PASS: {tests}/{tests} synthetic note and approval forgeries rejected; no human signoff")
    return tests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    short, note, source = SHORT.read_bytes(), NOTE.read_bytes(), SOURCE.read_bytes()
    validate(short, note, source)
    if args.self_test:
        self_test(short, note, source)
    print(f"PASS {args.level}: six B2 direct Oxford sense research cards, 200 written/0 independent per level; release BLOCKED")

if __name__ == "__main__":
    main()
