#!/usr/bin/env python3
"""Fail-closed frozen CEFR-1000 example-form and shared-sentence research audit.

Only editorial signals: valid inflections and example reuse are not mistakes.
This never grants independent linguistic, CEFR, audio or release approval.
"""
import argparse
import copy
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-EXAMPLE-MORPHOLOGY-AND-SHARED-SENTENCE-TRIAGE-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "17e940bb16f182d62b9faa2023a4bd67ae25f617"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("hand", "eye", "manage", "destroy", "grab")
EXPECTED = json.loads(r'''{
  "schema": 1,
  "scope": "CEFR_1000_TOTAL_STAGING_ONLY",
  "status": "FROZEN_SHORTLIST_EXAMPLE_MORPHOLOGY_AND_REUSE_RESEARCH_HOLD",
  "observed_on": "2026-11-01",
  "shortlist_blob_sha": "475e68ae17ab97bd937e73e5ce4794e0dcd76551",
  "method": "Case-insensitive ASCII word-boundary exact headword scan of all 1000 example sentences; normalized duplicate-example grouping. Heuristic signals, not grammar failures or CEFR approvals.",
  "first_pass_written_by_level": {
    "A1": 200,
    "A2": 200,
    "B1": 200,
    "B2": 200,
    "C1": 200
  },
  "independently_approved_by_level": {
    "A1": 0,
    "A2": 0,
    "B1": 0,
    "B2": 0,
    "C1": 0
  },
  "scanned_count": 1000,
  "nonliteral_headword_examples_count": 5,
  "nonliteral_by_level": {
    "A1": 2,
    "A2": 0,
    "B1": 0,
    "B2": 3,
    "C1": 0
  },
  "direct_oxford_dictionary_observations": 5,
  "duplicate_example_groups": 3,
  "duplicate_example_entries": 7,
  "source_limitations": "Publisher dictionary morphology and exact-sense observations do not constitute independent human English, Myanmar, CEFR, example or pronunciation approval. Cambridge grammar indexed search results returned direct HTTP 403 and are not counted as directly opened sources. No listening, physical iPhone QA or production deployment.",
  "records": [
    {
      "word": "hand",
      "level": "A1",
      "part_of_speech": "noun",
      "shortlist_index": 170,
      "shortlist_snapshot": {
        "english_definition": "The part of the body at the end of the arm.",
        "myanmar_meaning": "လက်",
        "example_sentence": "Please wash your hands."
      },
      "shortlist_provenance": {
        "source_path": "draft/A1-EDITORIAL-STARTER.json",
        "source_index": 172,
        "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
      },
      "matched_surface_form": "hands",
      "matching_rule": "REGULAR_NOUN_PLURAL",
      "publisher_evidence": {
        "publisher": "Oxford University Press",
        "source_url": "https://www.oxfordlearnersdictionaries.com/definition/english/hand_1",
        "observed_on": "2026-11-01",
        "access": "DIRECTLY_OPENED_PUBLISHER_DICTIONARY",
        "locator": "lines 106-125",
        "summary": "Oxford lists hand as a countable body-part noun and illustrates plural hands; plural is not a missing headword.",
        "cefr_scope": "MORPHOLOGY_OR_SENSE_ONLY_NOT_INDEPENDENT_CEFR_APPROVAL"
      },
      "editorial_risk": "The A1 hand example uses hands, which is valid plural grammar. Do not flag as an absent word or replace a natural plural example merely to satisfy literal-string matching.",
      "independent_reviewer_task": "Human-independent reviewer must verify original English, fluent Myanmar, grammar, exact sense, CEFR source alignment and audio before any signoff.",
      "editorial_hold": true,
      "independently_approved": false,
      "release_approved": false
    },
    {
      "word": "eye",
      "level": "A1",
      "part_of_speech": "noun",
      "shortlist_index": 171,
      "shortlist_snapshot": {
        "english_definition": "The part of the body used for seeing.",
        "myanmar_meaning": "မျက်လုံး",
        "example_sentence": "I have two eyes."
      },
      "shortlist_provenance": {
        "source_path": "draft/A1-EDITORIAL-STARTER.json",
        "source_index": 173,
        "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
      },
      "matched_surface_form": "eyes",
      "matching_rule": "REGULAR_NOUN_PLURAL",
      "publisher_evidence": {
        "publisher": "Oxford University Press",
        "source_url": "https://www.oxfordlearnersdictionaries.com/definition/english/eye_1",
        "observed_on": "2026-11-01",
        "access": "DIRECTLY_OPENED_PUBLISHER_DICTIONARY",
        "locator": "lines 106-129",
        "summary": "Oxford lists eye as a countable organ and gives plural eyes in its examples.",
        "cefr_scope": "MORPHOLOGY_OR_SENSE_ONLY_NOT_INDEPENDENT_CEFR_APPROVAL"
      },
      "editorial_risk": "The A1 eye example has eyes after two; it is grammatically expected. Check the intended singular lemma and teaching sense rather than mechanically demanding eye.",
      "independent_reviewer_task": "Human-independent reviewer must verify original English, fluent Myanmar, grammar, exact sense, CEFR source alignment and audio before any signoff.",
      "editorial_hold": true,
      "independently_approved": false,
      "release_approved": false
    },
    {
      "word": "manage",
      "level": "B2",
      "part_of_speech": "verb",
      "shortlist_index": 616,
      "shortlist_snapshot": {
        "english_definition": "To succeed in doing something difficult.",
        "myanmar_meaning": "အခက်အခဲရှိသော်လည်း အောင်မြင်စွာ လုပ်နိုင်သည်",
        "example_sentence": "We managed to finish the work before the deadline."
      },
      "shortlist_provenance": {
        "source_path": "draft/A2-C1-EDITORIAL-STARTER.json",
        "source_index": 101,
        "source_blob_sha": "b04dd85db5cfae131c25aa4c73109778991b6fdc"
      },
      "matched_surface_form": "managed",
      "matching_rule": "REGULAR_PAST_E_D",
      "publisher_evidence": {
        "publisher": "Oxford University Press",
        "source_url": "https://www.oxfordlearnersdictionaries.com/definition/english/manage",
        "observed_on": "2026-11-01",
        "access": "DIRECTLY_OPENED_PUBLISHER_DICTIONARY",
        "locator": "lines 103-108, 146-158, 173-178",
        "summary": "Oxford explicitly lists managed as the past form and manage to do as the successful-completion construction.",
        "cefr_scope": "MORPHOLOGY_OR_SENSE_ONLY_NOT_INDEPENDENT_CEFR_APPROVAL"
      },
      "editorial_risk": "B2 manage means succeed in doing something difficult, not manage a team. The draft managed to finish construction matches the intended sense; confirm the Myanmar translation reflects successful completion.",
      "independent_reviewer_task": "Human-independent reviewer must verify original English, fluent Myanmar, grammar, exact sense, CEFR source alignment and audio before any signoff.",
      "editorial_hold": true,
      "independently_approved": false,
      "release_approved": false
    },
    {
      "word": "destroy",
      "level": "B2",
      "part_of_speech": "verb",
      "shortlist_index": 654,
      "shortlist_snapshot": {
        "english_definition": "To damage something so badly that it no longer exists or works.",
        "myanmar_meaning": "ဖျက်ဆီးသည်",
        "example_sentence": "The fire destroyed the old warehouse."
      },
      "shortlist_provenance": {
        "source_path": "draft/A2-C1-EDITORIAL-STARTER.json",
        "source_index": 253,
        "source_blob_sha": "b04dd85db5cfae131c25aa4c73109778991b6fdc"
      },
      "matched_surface_form": "destroyed",
      "matching_rule": "REGULAR_PAST_ED",
      "publisher_evidence": {
        "publisher": "Oxford University Press",
        "source_url": "https://www.oxfordlearnersdictionaries.com/definition/english/destroy",
        "observed_on": "2026-11-01",
        "access": "DIRECTLY_OPENED_PUBLISHER_DICTIONARY",
        "locator": "lines 112-125",
        "summary": "Oxford lists destroyed as the past form and describes severe damage or loss of function.",
        "cefr_scope": "MORPHOLOGY_OR_SENSE_ONLY_NOT_INDEPENDENT_CEFR_APPROVAL"
      },
      "editorial_risk": "The B2 destroyed example is a valid past form, not a headword omission; check whether warehouse destruction is presented as physical destruction rather than a separate figurative sense.",
      "independent_reviewer_task": "Human-independent reviewer must verify original English, fluent Myanmar, grammar, exact sense, CEFR source alignment and audio before any signoff.",
      "editorial_hold": true,
      "independently_approved": false,
      "release_approved": false
    },
    {
      "word": "grab",
      "level": "B2",
      "part_of_speech": "verb",
      "shortlist_index": 657,
      "shortlist_snapshot": {
        "english_definition": "To take hold of something suddenly or quickly.",
        "myanmar_meaning": "အလျင်အမြန်ဆုပ်ကိုင်သည်",
        "example_sentence": "She grabbed her bag and ran outside."
      },
      "shortlist_provenance": {
        "source_path": "draft/A2-C1-EDITORIAL-STARTER.json",
        "source_index": 256,
        "source_blob_sha": "b04dd85db5cfae131c25aa4c73109778991b6fdc"
      },
      "matched_surface_form": "grabbed",
      "matching_rule": "DOUBLED_CONSONANT_PAST",
      "publisher_evidence": {
        "publisher": "Oxford University Press",
        "source_url": "https://www.oxfordlearnersdictionaries.com/us/definition/english/grab_1",
        "observed_on": "2026-11-01",
        "access": "DIRECTLY_OPENED_PUBLISHER_DICTIONARY",
        "locator": "lines 103-121",
        "summary": "Oxford explicitly lists grabbed as the past form and the sudden physical-taking sense.",
        "cefr_scope": "MORPHOLOGY_OR_SENSE_ONLY_NOT_INDEPENDENT_CEFR_APPROVAL"
      },
      "editorial_risk": "The B2 grabbed her bag example illustrates a sudden physical action; preserve consonant doubling in British spelling and distinguish this from grab an opportunity or a quick meal.",
      "independent_reviewer_task": "Human-independent reviewer must verify original English, fluent Myanmar, grammar, exact sense, CEFR source alignment and audio before any signoff.",
      "editorial_hold": true,
      "independently_approved": false,
      "release_approved": false
    }
  ],
  "shared_example_groups": [
    {
      "sentence": "the book is on the table.",
      "shortlist_indices": [
        6,
        93
      ],
      "words": [
        "the",
        "table"
      ],
      "levels": [
        "A1",
        "A1"
      ],
      "provenance": [
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 6,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        },
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 94,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        }
      ],
      "editorial_risk": "Reused example may be valid for multiple headwords, but independent review must assess whether each card clearly demonstrates its own sense, grammar and level.",
      "review_status": "UNAPPROVED_EDITORIAL_HANDOFF"
    },
    {
      "sentence": "what is your name?",
      "shortlist_indices": [
        13,
        77,
        115
      ],
      "words": [
        "your",
        "name",
        "what"
      ],
      "levels": [
        "A1",
        "A1",
        "A1"
      ],
      "provenance": [
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 13,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        },
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 78,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        },
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 116,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        }
      ],
      "editorial_risk": "Reused example may be valid for multiple headwords, but independent review must assess whether each card clearly demonstrates its own sense, grammar and level.",
      "review_status": "UNAPPROVED_EDITORIAL_HANDOFF"
    },
    {
      "sentence": "please sit here.",
      "shortlist_indices": [
        50,
        195
      ],
      "words": [
        "here",
        "sit"
      ],
      "levels": [
        "A1",
        "A1"
      ],
      "provenance": [
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 51,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        },
        {
          "source_path": "draft/A1-EDITORIAL-STARTER.json",
          "source_index": 197,
          "source_blob_sha": "ff1e93f60828ef2f94c9146522ce94075183b0ae"
        }
      ],
      "editorial_risk": "Reused example may be valid for multiple headwords, but independent review must assess whether each card clearly demonstrates its own sense, grammar and level.",
      "review_status": "UNAPPROVED_EDITORIAL_HANDOFF"
    }
  ],
  "independent_human_signoffs": [],
  "real_listening_signoffs": [],
  "release_approved": false
}''')

def require(test, message):
    if not test:
        raise ValueError(message)

def git_blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def scan(entries):
    missing = []
    groups = {}
    for index, entry in enumerate(entries):
        word = entry["word"]
        example = entry["example_sentence"]
        if not re.search(r"(?<![a-z])" + re.escape(word) + r"(?![a-z])", example, re.IGNORECASE):
            missing.append(index)
        normalized = " ".join(example.lower().split())
        groups.setdefault(normalized, []).append(index)
    repeated = [(sentence, indices) for sentence, indices in groups.items() if len(indices) > 1]
    return missing, repeated

def audit(packet, shortlist, check_disk=True):
    if check_disk:
        require(git_blob(PACKET) == PACKET_BLOB, "Research packet blob changed")
        require(git_blob(SHORTLIST) == SHORTLIST_BLOB, "Frozen shortlist blob changed")
    require(packet == EXPECTED, "Research evidence, provenance, count or signoff changed")
    require(shortlist.get("counts_by_level") == dict.fromkeys(LEVELS, 200)
            and shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Scope or independent approval drift")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000 and len({e["word"] for e in entries}) == 1000,
            "Missing/duplicated frozen headwords")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english", "reviewed_burmese", "reviewed_example",
                         "reviewed_level", "reviewed_pronunciation")) for e in entries),
            "Forged review approval")
    missing, repeated = scan(entries)
    require(missing == [170, 171, 616, 654, 657],
            "Nonliteral-example scan changed; research needs revision")
    require([indices for _, indices in repeated] == [[6,93], [13,77,115], [50,195]],
            "Shared-example scan changed; research needs revision")
    require(packet["scanned_count"] == len(entries)
            and packet["nonliteral_headword_examples_count"] == len(missing)
            and packet["duplicate_example_groups"] == len(repeated)
            and packet["duplicate_example_entries"] == sum(len(x[1]) for x in repeated),
            "Scan totals are inconsistent")
    for row, index in zip(packet["records"], missing):
        source = entries[index]
        require(row["word"] == source["word"] and row["level"] == source["level"]
                and row["part_of_speech"] == source["part_of_speech"]
                and row["shortlist_index"] == index,
                "Example source row mismatch")
        require(row["shortlist_snapshot"] == {
                    "english_definition": source["english_definition"],
                    "myanmar_meaning": source["burmese_meaning"],
                    "example_sentence": source["example_sentence"]},
                "Original English/Myanmar/example changed")
        require(row["shortlist_provenance"] == {k:source[k] for k in
                    ("source_path", "source_index", "source_blob_sha")},
                "Original historical source provenance changed")
        historical = ROOT / source["source_path"]
        require(historical.is_file() and git_blob(historical) == source["source_blob_sha"],
                "Historical source blob not found or changed")
        old = json.loads(historical.read_text(encoding="utf-8"))["entries"][source["source_index"]]
        require(all(old.get(k) == source.get(k) for k in
                    ("word", "level", "part_of_speech", "english_definition",
                     "burmese_meaning", "example_sentence")),
                "Historical row no longer matches frozen original")
        require(row["matched_surface_form"].lower() in
                source["example_sentence"].lower(),
                "Attested inflected surface form absent")
        require(row["publisher_evidence"]["cefr_scope"] ==
                "MORPHOLOGY_OR_SENSE_ONLY_NOT_INDEPENDENT_CEFR_APPROVAL"
                and row["publisher_evidence"]["access"] ==
                "DIRECTLY_OPENED_PUBLISHER_DICTIONARY"
                and row["editorial_hold"] is True
                and row["independently_approved"] is False
                and row["release_approved"] is False,
                "Unjustified source or independent approval")
    for group, (sentence, indices) in zip(packet["shared_example_groups"], repeated):
        require(group["sentence"] == sentence and group["shortlist_indices"] == indices
                and group["words"] == [entries[i]["word"] for i in indices]
                and group["levels"] == [entries[i]["level"] for i in indices]
                and group["provenance"] == [{k:entries[i][k] for k in
                    ("source_path", "source_index", "source_blob_sha")} for i in indices]
                and group["review_status"] == "UNAPPROVED_EDITORIAL_HANDOFF",
                "Shared example/provenance altered")
    require(packet["independent_human_signoffs"] == []
            and packet["real_listening_signoffs"] == []
            and packet["release_approved"] is False,
            "Invented human, listening or release signoff")
    return {"written":dict.fromkeys(LEVELS,200),
            "independently_approved":dict.fromkeys(LEVELS,0),
            "example_inflections":len(missing),
            "reused_example_groups":len(repeated),
            "status":"STAGING_ONLY_NOT_INDEPENDENT_REVIEW"}

def leaves(value, prefix=()):
    if isinstance(value, dict):
        for k,v in value.items():
            yield from leaves(v, prefix+(k,))
    elif isinstance(value, list):
        for i,v in enumerate(value):
            yield from leaves(v, prefix+(i,))
    else:
        yield prefix

def mutate(value, path):
    obj = value
    for part in path[:-1]:
        obj = obj[part]
    k = path[-1]
    old = obj[k]
    obj[k] = not old if isinstance(old,bool) else (
        777 if isinstance(old,int) else "FORGED" if isinstance(old,str) or old is None else None)

def self_test(packet, shortlist):
    paths = list(leaves(packet))
    for path in paths:
        forged = copy.deepcopy(packet)
        mutate(forged, path)
        try:
            audit(forged, shortlist, check_disk=False)
        except ValueError:
            continue
        raise AssertionError("Forged source or approval accepted: " + str(path))
    return len(paths)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    result = audit(packet, shortlist)
    if args.self_test:
        n = self_test(packet, shortlist)
        print(f"PASS: rejected {n}/{n} forged publisher, bilingual, provenance and signoff mutations")
    if args.level == "ALL":
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{args.level}: written=200, independently_approved=0, research_only=true")
if __name__ == "__main__":
    main()
