#!/usr/bin/env python3
"""Fail-closed staging audit for 12 new A2 Oxford word/POS observations.

Source line/page checks are anchored to directly inspected official PDF text
(29 October 2026). They do NOT authenticate exact senses or human approvals.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-FOURTH-TWELVE-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = ("https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/"
       "oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
EXPECTED = [
    ("level", "A2", 5, 1357, "level n.", "LEVEL_PROFICIENCY_VS_MEASURE"),
    ("mind", "A2", 6, 1398, "mind n., v.", "MIND_COGNITION_VS_CHANGE_MIND_IDIOM"),
    ("become", "A1", 1, 71, "become v.", "BECOME_A1_VS_A2_PROVISIONAL"),
    ("body", "A1", 1, 95, "body n.", "BODY_A1_VS_A2_PROVISIONAL"),
    ("problem", "A1", 3, 623, "problem n.", "PROBLEM_A1_VS_A2_PROVISIONAL"),
    ("almost", "A2", 4, 934, "almost adv.", "ALMOST_NEARLY_VS_COMPLETELY"),
    ("win", "A1", 4, 882, "win v.", "WIN_A1_VS_A2_PROVISIONAL"),
    ("idea", "A1", 2, 389, "idea n.", "IDEA_A1_VS_A2_PROVISIONAL"),
    ("community", "A2", 4, 1067, "community n.", "COMMUNITY_LOCAL_VS_SHARED_INTEREST"),
    ("cause", "A2", 4, 1031, "cause n., v.", "CAUSE_VERB_VS_NOUN"),
    ("data", "A2", 5, 1105, "data n.", "DATA_INFORMATION_PLURAL_USAGE"),
    ("general", "A2", 5, 1246, "general adj.", "GENERAL_BROAD_VS_UNSPECIFIC"),
]

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

def audit(packet, shortlist, sha):
    require(sha == SHORTLIST_SHA and packet.get("shortlist_blob_sha") == sha,
            "Shortlist provenance SHA drift")
    require(packet.get("schema") == 1
            and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") ==
                "A2_FOURTH_TWELVE_DIRECT_OXFORD_WORD_POS_TRIAGE_EDITORIAL_HOLD"
            and packet.get("observed_on") == "2026-10-29", "Scope/status/date drift")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 12
            and packet.get("counts_by_level") ==
                {"A1": 0, "A2": 12, "B1": 0, "B2": 0, "C1": 0}
            and packet.get("publisher_reference_level_counts") ==
                {"A1": 5, "A2": 7, "B1": 0, "B2": 0, "C1": 0}
            and packet.get("word_pos_discrepancies") == 5
            and packet.get("independently_approved_count") == 0,
            "Coverage/approval count drift")
    require("NOT exact-sense CEFR" in packet.get("source_limitations", ""),
            "Source limitation caveat removed")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000,
            "Frozen 1000-entry shortlist invalid")
    a2 = {r["word"]: r for r in entries if r.get("level") == "A2"}
    require(len(a2) == 200, "A2 quota or uniqueness drift")
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == 12
            and len({r.get("word") for r in records}) == 12, "Missing/duplicate records")
    for i, (word, observed, page, line, excerpt, risk_id) in enumerate(EXPECTED):
        row, e = records[i], a2[word]
        require(row.get("word") == word and row.get("level") == "A2"
                and row.get("part_of_speech") == e["part_of_speech"],
                word + ": identity/POS drift")
        require(row.get("shortlist_snapshot") == {
            "english_definition": e["english_definition"],
            "myanmar_meaning": e["burmese_meaning"],
            "example_sentence": e["example_sentence"]}, word + ": bilingual snapshot drift")
        require(row.get("shortlist_provenance") == {
            "source_path": e["source_path"], "source_index": e["source_index"],
            "source_blob_sha": e["source_blob_sha"]}, word + ": source provenance drift")
        require(row.get("publisher_source") == {
            "publisher": "Oxford University Press",
            "title": "The Oxford 3000 by CEFR level", "url": URL,
            "observed_on": "2026-10-29", "pdf_page": page,
            "extracted_line": line, "source_excerpt": excerpt,
            "source_cefr_level": observed,
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"}, word + ": publisher evidence drift")
        require(row.get("editorial_risk_id") == risk_id
                and isinstance(row.get("editorial_risk"), str)
                and len(row["editorial_risk"]) > 95, word + ": risk lost")
        task = row.get("independent_reviewer_task")
        require(isinstance(task, str) and word in task and risk_id in task
                and "Human-independent" in task and "NOT exact-sense" in task
                and len(task) > 220, word + ": reviewer task lost")
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                word + ": false independent approval")
    return len(records)

def self_test(packet, shortlist, sha):
    changes = []
    for i in range(12):
        changes.extend([
            lambda p, i=i: p["records"][i]["publisher_source"].update(source_cefr_level="C1"),
            lambda p, i=i: p["records"][i]["publisher_source"].update(source_excerpt="invented"),
            lambda p, i=i: p["records"][i]["shortlist_snapshot"].update(myanmar_meaning="forged"),
            lambda p, i=i: p["records"][i]["shortlist_snapshot"].update(example_sentence="Forged."),
            lambda p, i=i: p["records"][i].update(independently_reviewed=True),
            lambda p, i=i: p["records"][i].update(independent_reviewer_receipt={"fake": True}),
        ])
    changes.extend([
        lambda p: p.update(independently_approved_count=12),
        lambda p: p.update(word_pos_discrepancies=0),
        lambda p: p.update(shortlist_blob_sha="0"*40),
        lambda p: p["records"].reverse(),
        lambda p: p["records"].pop(),
        lambda p: p["records"][0]["publisher_source"].update(pdf_page=99),
        lambda p: p["records"][1]["publisher_source"].update(url="https://example.com/forged.pdf"),
        lambda p: p["records"][2]["publisher_source"].update(evidence_scope="EXACT_SENSE_VERIFIED"),
    ])
    rejected = 0
    for i, change in enumerate(changes):
        altered = copy.deepcopy(packet)
        change(altered)
        try:
            audit(altered, shortlist, sha)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError(f"Tampering mutation {i} was accepted")
    return rejected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=("A1", "A2", "B1", "B2", "C1", "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    n = audit(packet, shortlist, blob_sha(SHORTLIST))
    print(f"PASS Oxford A2 fourth packet: {n} observations, 5 lower A1, 7 A2; "
          f"0 independent approvals; lane={args.level}; STAGING ONLY")
    if args.self_test:
        m = self_test(packet, shortlist, blob_sha(SHORTLIST))
        print(f"PASS {m}/{m} forged-source, bilingual and false-approval mutations rejected")

if __name__ == "__main__":
    main()
