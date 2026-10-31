#!/usr/bin/env python3
"""Fail-closed A2 Oxford sixteenth 11-entry evidence packet auditor. Staging only."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
PACKET = "draft/CEFR-1000-OXFORD-A2-SIXTEENTH-ELEVEN-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORTLIST = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SOURCE = "draft/A2-C1-EDITORIAL-STARTER.json"
PACKET_SHA = "fba2560d1c46dc31a1a6305172ee0d683a596e48"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCE_SHA = "b04dd85db5cfae131c25aa4c73109778991b6fdc"
PDF = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
EXPECTED = [
    ("member","A1",2,477,"member n."),
    ("usually","A1",4,844,"usually adv."),
    ("follow","A1",2,301,"follow v."),
    ("save","B1",6,1582,"save v."),
    ("round","B1",6,1568,"round adj., adv., prep."),
    ("worth","B1",10,2586,"worth adj."),
    ("exactly","A2",5,1180,"exactly adv."),
    ("source","B1",6,1644,"source n."),
    ("total","B1",10,2517,"total adj., n."),
    ("result","A1",3,650,"result n."),
    ("share","A1",3,685,"share v."),
]
SENSES = {
    "save": ("https://www.oxfordlearnersdictionaries.com/definition/english/save_1",2,158,171),
    "worth": ("https://www.oxfordlearnersdictionaries.com/definition/english/worth_1",1,103,115),
    "total": ("https://www.oxfordlearnersdictionaries.com/definition/english/total_2",1,103,122),
    "share": ("https://www.oxfordlearnersdictionaries.com/definition/english/share_1",1,113,122),
}
ROOT_KEYS = {"schema","scope","status","observed_on","shortlist_blob_sha","record_count","counts_by_level",
             "publisher_reference_level_counts","word_pos_discrepancies","direct_dictionary_sense_leads",
             "independently_approved_count","source_limitations","records"}
ROW_KEYS = {"word","level","part_of_speech","shortlist_snapshot","shortlist_provenance","publisher_source",
            "editorial_risk","independent_reviewer_task","editorial_hold","independently_reviewed",
            "release_approved","independent_reviewer_receipt"}
PUBLISHER_KEYS = {"publisher","title","url","observed_on","pdf_page","extracted_line",
                  "source_excerpt","source_cefr_level","evidence_scope","access"}
SENSE_KEYS = {"url","sense_number","page_text_line_start","page_text_line_end",
              "observed_on","evidence_scope","sense_summary"}
PROPOSAL_KEYS = {"myanmar_meaning","original_example","review_status"}

def require(value, reason):
    if not value:
        raise ValueError(reason)

def blob_sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def audit(packet, shortlist, historical):
    require(set(packet) == ROOT_KEYS and packet["schema"] == 1, "Packet schema drift")
    require(packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet["status"] == "A2_SIXTEENTH_ELEVEN_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and packet["observed_on"] == "2026-10-31"
            and packet["shortlist_blob_sha"] == SHORTLIST_SHA, "Scope, date or shortlist provenance drift")
    require(packet["record_count"] == 11
            and packet["counts_by_level"] == dict.fromkeys(LEVELS, 0) | {"A2": 11}
            and packet["publisher_reference_level_counts"] == dict.fromkeys(LEVELS, 0) | {"A1": 5, "A2": 1, "B1": 5}
            and packet["word_pos_discrepancies"] == 10
            and packet["direct_dictionary_sense_leads"] == 4
            and packet["independently_approved_count"] == 0
            and "not independent exact-sense cefr approval" in packet["source_limitations"].lower()
            and "word of the day" in packet["source_limitations"].lower(), "Publisher totals, release gate or source disclaimer drift")
    require(shortlist["release_status"] == "PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH"
            and shortlist["counts_by_level"] == dict.fromkeys(LEVELS, 200)
            and shortlist["independently_approved_by_level"] == dict.fromkeys(LEVELS, 0),
            "Frozen shortlist scope or approvals drift")
    entries = shortlist["entries"]
    require(len(entries) == 1000 and len({x["word"] for x in entries}) == 1000
            and all(x["editorial_hold"] is True and x["release_approved"] is False
                    and all(x[k] is False for k in
                        ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation"))
                    for x in entries), "Shortlist duplicates or forged approval")
    by_word = {x["word"]: x for x in entries}
    source_entries = historical["entries"]
    rows = packet["records"]
    require(isinstance(rows, list) and len(rows) == 11, "Packet rows missing")
    seen = set()
    for row, (word, cefr, page, line, excerpt) in zip(rows, EXPECTED):
        require(row["word"] == word and word not in seen and row["level"] == "A2", "Row order, duplicate or level drift")
        seen.add(word)
        keys = ROW_KEYS | ({"dictionary_sense_lead","editorial_rewrite_candidate"} if word in SENSES else set())
        require(set(row) == keys, "Unrecognized row/approval field: " + word)
        original = by_word[word]
        require(original["level"] == "A2" and row["part_of_speech"] == original["part_of_speech"], "POS drift: " + word)
        snapshot = {"english_definition": original["english_definition"],
                    "myanmar_meaning": original["burmese_meaning"],
                    "example_sentence": original["example_sentence"]}
        require(row["shortlist_snapshot"] == snapshot, "Bilingual/exemplar snapshot drift: " + word)
        provenance = {k: original[k] for k in ("source_path","source_index","source_blob_sha")}
        require(row["shortlist_provenance"] == provenance
                and provenance["source_path"] == SOURCE and provenance["source_blob_sha"] == SOURCE_SHA,
                "Historical provenance mismatch: " + word)
        upstream = source_entries[provenance["source_index"]]
        require(all(upstream[k] == original[k] for k in
                    ("word","level","part_of_speech","english_definition","burmese_meaning","example_sentence"))
                and all(upstream[k] is False for k in
                    ("reviewed_english","reviewed_burmese","reviewed_example","reviewed_level","reviewed_pronunciation")),
                "Actual historical source row does not match: " + word)
        publisher = row["publisher_source"]
        require(set(publisher) == PUBLISHER_KEYS and publisher == {
            "publisher":"Oxford University Press",
            "title":"The Oxford 3000 by CEFR level",
            "url":PDF,"observed_on":"2026-10-31",
            "pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,
            "source_cefr_level":cefr,
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Publisher locator or source level drift: " + word)
        require(isinstance(row["editorial_risk"], str) and len(row["editorial_risk"]) >= 40
                and "independent" in row["independent_reviewer_task"].lower()
                and "not independent approval" in row["independent_reviewer_task"].lower()
                and row["editorial_hold"] is True and row["independently_reviewed"] is False
                and row["release_approved"] is False and row["independent_reviewer_receipt"] is None,
                "Editorial risk or fabricated reviewer signoff: " + word)
        if word in SENSES:
            url, number, start, end = SENSES[word]
            sense = row["dictionary_sense_lead"]
            require(set(sense) == SENSE_KEYS
                    and sense["url"] == url and sense["sense_number"] == number
                    and sense["page_text_line_start"] == start and sense["page_text_line_end"] == end
                    and sense["observed_on"] == "2026-10-31"
                    and sense["evidence_scope"] == "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and isinstance(sense["sense_summary"], str) and len(sense["sense_summary"]) >= 50,
                    "Oxford exact-sense lead changed: " + word)
            proposal = row["editorial_rewrite_candidate"]
            require(set(proposal) == PROPOSAL_KEYS
                    and proposal["review_status"] == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and isinstance(proposal["myanmar_meaning"], str) and len(proposal["myanmar_meaning"]) > 15
                    and isinstance(proposal["original_example"], str) and len(proposal["original_example"]) > 25,
                    "Unapproved Myanmar/example candidate changed: " + word)
    require(seen == {r[0] for r in EXPECTED}, "Missing source headwords")
    return {"observed_A2":11,"publisher_levels":{"A1":5,"A2":1,"B1":5},
            "provisional_discrepancies":10,"direct_dictionary_sense_leads":4,
            "written_A2":200,"independently_approved_A2":0,
            "final_george_emma_listening_signoffs":0,"release":"BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist, historical):
    baseline = audit(packet, shortlist, historical)
    cases = 0
    for index, row in enumerate(packet["records"]):
        edits = [
            lambda r: r["publisher_source"].update(source_cefr_level="C1"),
            lambda r: r["publisher_source"].update(source_excerpt="forged"),
            lambda r: r["publisher_source"].update(pdf_page=0),
            lambda r: r["publisher_source"].update(extracted_line=0),
            lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အတု"),
            lambda r: r["shortlist_snapshot"].update(example_sentence="forged"),
            lambda r: r["shortlist_provenance"].update(source_index=-1),
            lambda r: r.update(independently_reviewed=True),
            lambda r: r.update(release_approved=True),
            lambda r: r.update(independent_reviewer_receipt={"fake":True}),
            lambda r: r.update(editorial_hold=False),
        ]
        if row["word"] in SENSES:
            edits += [
                lambda r: r["dictionary_sense_lead"].update(sense_number=999),
                lambda r: r["dictionary_sense_lead"].update(evidence_scope="APPROVED"),
                lambda r: r["editorial_rewrite_candidate"].update(review_status="APPROVED"),
                lambda r: r["editorial_rewrite_candidate"].update(myanmar_meaning=""),
            ]
        for edit in edits:
            forged = copy.deepcopy(packet)
            edit(forged["records"][index])
            try:
                audit(forged, shortlist, historical)
            except ValueError:
                cases += 1
                continue
            raise AssertionError("Forged publisher, provenance or review mutation passed: " + row["word"])
    for edit in [
        lambda p:p.update(independently_approved_count=1),
        lambda p:p.update(record_count=10),
        lambda p:p["records"].pop(),
        lambda p:p["records"].reverse(),
        lambda p:p.update(source_limitations="approved"),
    ]:
        forged = copy.deepcopy(packet)
        edit(forged)
        try:
            audit(forged, shortlist, historical)
        except ValueError:
            cases += 1
            continue
        raise AssertionError("Forged packet scope passed")
    return baseline, cases

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    for path, sha in ((PACKET,PACKET_SHA),(SHORTLIST,SHORTLIST_SHA),(SOURCE,SOURCE_SHA)):
        require(blob_sha(path) == sha, "Pinned historical Git blob changed: " + path)
    packet, shortlist, historical = read(PACKET), read(SHORTLIST), read(SOURCE)
    if args.self_test:
        report, n = self_test(packet, shortlist, historical)
        print("PASS: rejected %d/%d forged Oxford source, Myanmar, historical provenance and approval mutations" % (n,n))
    else:
        report = audit(packet, shortlist, historical)
    if args.level != "ALL":
        print(json.dumps({args.level:{"written":200,"new_source_observations":11 if args.level=="A2" else 0,
                                   "independently_approved":0},"release":"BLOCKED_STAGING_ONLY"},sort_keys=True))
    else:
        print(json.dumps(report,sort_keys=True))

if __name__ == "__main__":
    main()
