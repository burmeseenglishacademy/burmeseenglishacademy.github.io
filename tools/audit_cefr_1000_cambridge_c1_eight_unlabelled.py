#!/usr/bin/env python3
"""Fail-closed staging audit for eight Cambridge C1 sense leads, NOT CEFR approval.

Checks a pinned research-packet Git blob, original held shortlist snapshots,
publisher URL/POS metadata, absent Oxford core-list matches, and zero approvals.
A Cambridge dictionary sense without a CEFR badge is not a C1 certification.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_PATH = "draft/CEFR-1000-CAMBRIDGE-C1-EIGHT-UNLABELLED-SENSE-TRIAGE-2026-10-31.json"
SHORTLIST_PATH = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
EXPECTED_PACKET_BLOB_SHA = "c4619985ff7aa4773a517a0ab48473611e81c5d6"
EXPECTED_SHORTLIST_BLOB_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
WORDS = {
    "affable": ("adjective", "adjective"),
    "adulation": ("noun", "noun [U]"),
    "acrimonious": ("adjective", "adjective, formal"),
    "culpability": ("noun", "noun [U]"),
    "conjecture": ("noun", "noun [C or U]"),
    "disparage": ("verb", "verb [T]"),
    "misconstrue": ("verb", "verb [T], formal"),
    "irrevocable": ("adjective", "adjective"),
}
OXFORD_3000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
OXFORD_5000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"

def require(ok, message):
    if not ok:
        raise ValueError(message)

def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def read_json(path, expected_sha):
    raw = (ROOT / path).read_bytes()
    require(blob_sha(raw) == expected_sha, "Pinned source Git blob changed: " + path)
    return json.loads(raw)

def audit(packet, shortlist, original_packet):
    require(packet == original_packet, "Research packet differs from pinned original")
    require(packet.get("schema") == 1 and packet.get("project") == "BEA_CEFR_1000"
            and packet.get("scope") == "STAGING_ONLY"
            and packet.get("observed_on") == "2026-10-31"
            and packet.get("count") == 8
            and packet.get("independently_approved_count") == 0
            and packet.get("production_deployed") is False
            and packet.get("shortlist_blob_sha") == EXPECTED_SHORTLIST_BLOB_SHA
            and packet.get("status") == "EIGHT_C1_CAMBRIDGE_SENSES_OXFORD_CORE_LIST_ABSENCE_NOT_CEFR_APPROVAL",
            "Staging/approval provenance drift")
    require(len(shortlist["entries"]) == 1000
            and shortlist["counts_by_level"] == dict.fromkeys(("A1", "A2", "B1", "B2", "C1"), 200)
            and shortlist["independently_approved_by_level"] == dict.fromkeys(("A1", "A2", "B1", "B2", "C1"), 0),
            "Shortlist size, level quotas or independent approvals changed")
    entries = {e["word"]: e for e in shortlist["entries"]}
    require(len(entries) == 1000, "Duplicate headwords in shortlist")
    rows = packet.get("records", [])
    require(len(rows) == 8 and {r.get("word") for r in rows} == set(WORDS),
            "Expected eight distinct C1 sense leads")
    for r in rows:
        word = r["word"]
        pos, cam_pos = WORDS[word]
        entry = entries[word]
        require(r.get("level") == "C1" and r.get("part_of_speech") == pos
                and r.get("cambridge_headword_pos") == cam_pos
                and r.get("cambridge_url") == "https://dictionary.cambridge.org/dictionary/english/" + word
                and r.get("cambridge_observed_on") == "2026-10-31"
                and r.get("cambridge_cefr_label") == "NOT_OBSERVED"
                and r.get("oxford_3000_url") == OXFORD_3000
                and r.get("oxford_5000_url") == OXFORD_5000
                and r.get("oxford_list_observed_on") == "2026-10-31"
                and r.get("oxford_3000_exact_headword_match") is False
                and r.get("oxford_5000_exact_headword_match") is False,
                "Source/POS/CEFR attribution drift: " + word)
        require(r.get("independent_exact_sense_review") == "NOT_DONE"
                and r.get("independent_cefr_review") == "NOT_DONE"
                and r.get("independent_myanmar_review") == "NOT_DONE"
                and r.get("independent_example_review") == "NOT_DONE"
                and r.get("editorial_hold") is True
                and r.get("release_approved") is False,
                "Forged independent signoff or release: " + word)
        require(entry["level"] == "C1" and entry["part_of_speech"] == pos
                and entry["editorial_hold"] is True and entry["release_approved"] is False
                and all(entry.get("reviewed_" + key) is False for key in
                        ("english", "burmese", "example", "level", "pronunciation")),
                "Shortlist independent review flags changed: " + word)
        snap = r["shortlist_snapshot"]
        for source_key, entry_key in (("english_definition", "english_definition"),
                                      ("myanmar_meaning", "burmese_meaning"),
                                      ("example_sentence", "example_sentence"),
                                      ("source_path", "source_path"),
                                      ("source_index", "source_index"),
                                      ("source_blob_sha", "source_blob_sha")):
            require(snap.get(source_key) == entry.get(entry_key),
                    "Frozen bilingual or historical source snapshot changed: " + word)
        require(bool(r.get("cambridge_sense_paraphrase"))
                and bool(r.get("editorial_risk"))
                and bool(r.get("unapproved_proposal", {}).get("myanmar_meaning"))
                and bool(r.get("unapproved_proposal", {}).get("original_example")),
                "Missing source-supported sense or editorial proposal: " + word)
    return {"source_supported_cambridge_sense_leads": 8,
            "source_supported_cefr_labels": 0,
            "new_oxford_cefr_observations": 0,
            "independent_approvals": 0,
            "release": "BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist):
    rejected = 0
    def reject(mutate):
        nonlocal rejected
        altered = copy.deepcopy(packet)
        mutate(altered)
        try:
            audit(altered, shortlist, packet)
        except (ValueError, KeyError, TypeError):
            rejected += 1
        else:
            raise AssertionError("Forged source or signoff mutation was accepted")
    for i in range(8):
        for field, value in (
            ("cambridge_cefr_label", "C1"),
            ("cambridge_url", "https://example.com/forged"),
            ("cambridge_observed_on", "2026-10-30"),
            ("cambridge_headword_pos", "unknown"),
            ("oxford_3000_exact_headword_match", True),
            ("oxford_5000_exact_headword_match", True),
            ("independent_cefr_review", "APPROVED"),
            ("independent_myanmar_review", "APPROVED"),
            ("independent_example_review", "APPROVED"),
            ("independent_exact_sense_review", "APPROVED"),
            ("editorial_hold", False),
            ("release_approved", True),
        ):
            reject(lambda p, i=i, field=field, value=value:
                   p["records"][i].__setitem__(field, value))
        reject(lambda p, i=i: p["records"][i]["shortlist_snapshot"].__setitem__("myanmar_meaning", "fake"))
        reject(lambda p, i=i: p["records"][i]["unapproved_proposal"].__setitem__("myanmar_meaning", "fake"))
    reject(lambda p: p.__setitem__("independently_approved_count", 8))
    reject(lambda p: p.__setitem__("production_deployed", True))
    reject(lambda p: p["records"].pop())
    return rejected

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("A1", "A2", "B1", "B2", "C1", "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = read_json(PACKET_PATH, EXPECTED_PACKET_BLOB_SHA)
    shortlist = read_json(SHORTLIST_PATH, EXPECTED_SHORTLIST_BLOB_SHA)
    result = audit(packet, shortlist, packet)
    if args.self_test:
        result["adversarial_mutations_rejected"] = self_test(packet, shortlist)
    result["lane"] = args.level
    print(json.dumps(result, sort_keys=True))
