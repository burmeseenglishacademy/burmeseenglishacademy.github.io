#!/usr/bin/env python3
"""Fail-closed staging-only integrity audit for 24 dated Oxford A1 word/POS leads.

This is a mechanical provenance/content integrity test, NOT independent language
review, exact-sense CEFR verification, pronunciation listening or release approval.
"""
import argparse
import copy
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-FIFTH-TWENTYFOUR-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
# Frozen directly inspected Oxford word/POS excerpts, one-based PDF pages, zero-based web lines.
EXPECTED = [
    ("work", 4, 891, "work v., n.", "WORK_EMPLOYMENT_VS_GENERAL_EFFORT"),
    ("year", 4, 900, "year n.", "YEAR_TWELVE_MONTHS_VS_CALENDAR_YEAR"),
    ("love", 2, 455, "love n., v.", "FAMILY_AFFECTION_VS_ROMANTIC_LOVE"),
    ("man", 2, 461, "man n.", "ADULT_MALE_VS_GENERIC_HUMAN_USAGE"),
    ("use", 4, 842, "use v.", "USE_TOOL_VS_USE_SERVICE_OR_RESOURCE"),
    ("come", 1, 163, "come v.", "COME_DEICTIC_DIRECTION_DEPENDS_ON_SPEAKER"),
    ("help", 2, 361, "help v., n.", "HELP_VERB_VS_NOUN_AND_ABILITY_MODAL"),
    ("old", 3, 547, "old adj.", "OLD_PERSON_VS_OLD_OBJECT_MYANMAR_POLYSEMY"),
    ("little", 2, 448, "little adj., det./pron.", "LITTLE_SMALL_SIZE_VS_SMALL_QUANTITY"),
    ("house", 2, 380, "house n.", "HOUSE_BUILDING_VS_HOME_FAMILY"),
    ("place", 3, 598, "place n.", "PLACE_PHYSICAL_LOCATION_VS_ABSTRACT_POSITION"),
    ("give", 2, 329, "give v.", "GIVE_TRANSFER_VS_GIVE_INFORMATION"),
    ("new", 2, 516, "new adj.", "NEW_RECENTLY_MADE_VS_NEW_TO_SPEAKER"),
    ("make", 2, 460, "make v.", "MAKE_CREATE_VS_CAUSATIVE_MAKE"),
    ("look", 2, 452, "look v.", "LOOK_DIRECT_GAZE_VS_APPEAR"),
    ("take", 3, 761, "take v.", "TAKE_CHAIR_EXAMPLE_AMBIGUOUS_CARRY_VS_ACCEPT"),
    ("very", 4, 847, "very adv.", "VERY_DEGREE_MODIFIER_NOT_STANDALONE"),
    ("many", 2, 462, "many det./pron.", "MANY_COUNTABLE_NOUNS_VS_MUCH_UNCOUNTABLE"),
    ("three", 3, 797, "three number", "THREE_NUMERAL_NOT_ORDINAL_THIRD"),
    ("small", 3, 710, "small adj.", "SMALL_PHYSICAL_SIZE_VS_IMPORTANCE"),
    ("big", 1, 85, "big adj.", "BIG_SIZE_VS_IMPORTANCE_OR_AGE"),
    ("eat", 1, 234, "eat v.", "EAT_BREAKFAST_NATURAL_COLLOCATION"),
    ("drink", 1, 225, "drink n., v.", "DRINK_LIQUID_VERB_VS_NOUN"),
    ("happy", 2, 349, "happy adj.", "HAPPY_FEELING_VS_CONGRATULATORY_WISH"),
]
PROPOSAL_WORDS = ("old", "little", "take", "year", "house", "love")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git_blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def audit(packet, shortlist, actual_sha, check_upstream=False):
    require(actual_sha == SHORTLIST_SHA, "Shortlist changed; evidence must be rebound")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "Wrong scope")
    require(packet.get("status") == "A1_FIFTH_TWENTYFOUR_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD", "Status drift")
    require(packet.get("observed_on") == "2026-10-29", "Observation date drift")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "Shortlist provenance drift")
    require(type(packet.get("record_count")) is int and packet["record_count"] == 24, "Count drift")
    require(packet.get("counts_by_level") == {"A1":24,"A2":0,"B1":0,"B2":0,"C1":0}, "Level counts drift")
    require(packet.get("independently_approved_count") == 0, "False approval count")
    limitations = packet.get("source_limitations", "")
    require("NOT exact-sense CEFR" in limitations and "No human-independent approvals" in limitations, "Scope caveat missing")
    require(len(packet.get("editorial_priority", [])) >= 6, "Risk triage missing")
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == 24, "Record count")
    require(len(set(r.get("word") for r in records)) == 24, "Duplicate headwords")
    entries = shortlist.get("entries", [])
    require(len(entries) == 1000, "1,000 shortlist entries required")
    require(shortlist.get("counts_by_level") == {k:200 for k in LEVELS}, "Level quotas drift")
    require(shortlist.get("independently_approved_by_level") == {k:0 for k in LEVELS}, "False approvals")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False for e in entries),
            "Shortlist editorial hold lost")
    selected = {e["word"]: e for e in entries if e.get("level") == "A1"}
    require(len(selected) == 200, "A1 quota drift")
    for row, (word, page, line, excerpt, risk) in zip(records, EXPECTED):
        require(row.get("word") == word and row.get("level") == "A1", word + ": identity")
        require(word in selected, word + ": absent from shortlist")
        source = selected[word]
        require(row.get("part_of_speech") == source.get("part_of_speech"), word + ": POS")
        require(row.get("shortlist_snapshot") == {
            "english_definition": source["english_definition"],
            "myanmar_meaning": source["burmese_meaning"],
            "example_sentence": source["example_sentence"]}, word + ": snapshot")
        provenance = {k:source[k] for k in ("source_path","source_index","source_blob_sha")}
        require(row.get("shortlist_provenance") == provenance, word + ": upstream Git provenance")
        require(row.get("publisher_source") == {
            "publisher":"Oxford University Press",
            "title":"The Oxford 3000 by CEFR level",
            "url":URL,"observed_on":"2026-10-29","pdf_page":page,
            "extracted_line":line,"source_excerpt":excerpt,
            "source_cefr_level":"A1",
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, word + ": publisher word/POS evidence")
        require(row.get("editorial_risk") == risk, word + ": risk omitted")
        task = row.get("independent_reviewer_task", "")
        require(isinstance(task,str) and len(task) > 180 and word in task and risk in task
                and "Human-independent" in task and "not exact-sense approval" in task,
                word + ": human review task omitted")
        require(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None, word + ": fake approval")
        if check_upstream:
            path = ROOT / provenance["source_path"]
            require(path.is_file(), word + ": source file missing")
            require(git_blob_sha(path) == provenance["source_blob_sha"], word + ": source blob mismatch")
            original = json.loads(path.read_text(encoding="utf-8"))["entries"][provenance["source_index"]]
            require(original["word"] == word and original["level"] == "A1", word + ": source index drift")
            for key in ("english_definition","burmese_meaning","example_sentence","part_of_speech"):
                require(original[key] == source[key], word + ": historical source field mismatch " + key)
    proposals = packet.get("unreviewed_editorial_proposals")
    require(isinstance(proposals,list) and len(proposals) == 6, "Missing original bilingual proposals")
    require(tuple(p.get("word") for p in proposals) == PROPOSAL_WORDS, "Proposal identity/order drift")
    for proposal in proposals:
        require(proposal.get("review_status") == "UNREVIEWED_UNAPPLIED_PROPOSAL"
                and proposal.get("human_independent_approval") is False, "Proposal falsely approved")
        for key in ("issue","suggested_english_definition","suggested_myanmar_meaning","suggested_example_sentence"):
            require(isinstance(proposal.get(key),str) and len(proposal[key]) >= (4 if key == "suggested_myanmar_meaning" else 10), "Proposal missing " + key)
        require(any("\u1000" <= ch <= "\u109f" for ch in proposal["suggested_myanmar_meaning"]),
                "Proposal Myanmar text missing")
    return len(records)


def self_test(packet, shortlist, sha):
    mutations = []
    for i in range(24):
        mutations.extend([
            lambda p,i=i: p["records"][i]["publisher_source"].update(source_excerpt="forged"),
            lambda p,i=i: p["records"][i]["shortlist_snapshot"].update(myanmar_meaning="fake"),
            lambda p,i=i: p["records"][i].update(independently_reviewed=True),
            lambda p,i=i: p["records"][i]["shortlist_provenance"].update(source_index=999),
        ])
    mutations += [
        lambda p: p.update(record_count=25),
        lambda p: p.update(independently_approved_count=24),
        lambda p: p.update(shortlist_blob_sha="0"*40),
        lambda p: p["records"][0].update(release_approved=True),
        lambda p: p["records"][0].update(independent_reviewer_receipt={"reviewer":"bot"}),
        lambda p: p["records"][1]["publisher_source"].update(source_cefr_level="C1"),
        lambda p: p["records"][2]["publisher_source"].update(url="https://example.com/forged.pdf"),
        lambda p: p["records"][3]["shortlist_snapshot"].update(example_sentence="forged"),
        lambda p: p["records"][4].update(editorial_risk=""),
        lambda p: p["records"][5].update(independent_reviewer_task="approved"),
        lambda p: p["records"].reverse(),
        lambda p: p["unreviewed_editorial_proposals"][0].update(human_independent_approval=True),
        lambda p: p["unreviewed_editorial_proposals"][1].update(review_status="APPROVED"),
        lambda p: p["unreviewed_editorial_proposals"][2].update(suggested_myanmar_meaning="English only"),
        lambda p: p["unreviewed_editorial_proposals"][3].update(word="wrong"),
        lambda p: p.update(source_limitations="approved"),
    ]
    for i, change in enumerate(mutations):
        altered = copy.deepcopy(packet)
        change(altered)
        try:
            audit(altered, shortlist, sha)
        except ValueError:
            continue
        raise AssertionError(f"Negative mutation {i} escaped")
    return len(mutations)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=(*LEVELS,"ALL"),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    packet=json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist=json.loads(SHORTLIST.read_text(encoding="utf-8"))
    sha=git_blob_sha(SHORTLIST)
    n=audit(packet,shortlist,sha,check_upstream=True)
    print(f"PASS Oxford A1 fifth batch: {n} dated word/POS leads; level={args.level}; 0 independent approvals; STAGING ONLY")
    if args.self_test:
        m=self_test(packet,shortlist,sha)
        print(f"PASS {m}/{m} forged-source, bilingual, upstream and false-approval mutations rejected")


if __name__=="__main__":
    main()
