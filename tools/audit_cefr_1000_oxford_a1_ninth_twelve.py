#!/usr/bin/env python3
"""Audit ninth A1 Oxford PDF word/POS observations; never approve human review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A1-NINTH-TWELVE-2026-10-29.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
LIMIT = "Direct official Oxford University Press Oxford 3000 by CEFR level PDF word/POS observations on 2026-10-29. One-based PDF pages and zero-based web-extracted lines. These 12 A1 nouns remain independent exact-sense, English, fluent Myanmar, original-example and British-use unverified. Word/POS matches are NOT independent CEFR signoffs. No real George/Emma listening, physical iPhone QA or production publication."
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = json.loads(r'''[{"word":"sister","page":3,"line":700,"excerpt":"sister n.","risk":"A1_NINTH_TWELVE_SISTER_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Review older/younger sister distinctions in Myanmar. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"son","page":3,"line":719,"excerpt":"son n.","risk":"A1_NINTH_TWELVE_SON_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Verify a parent's male child sense and natural Myanmar wording. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"daughter","page":1,"line":194,"excerpt":"daughter n.","risk":"A1_NINTH_TWELVE_DAUGHTER_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Verify a parent's female child sense and natural Myanmar wording. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"grandmother","page":2,"line":335,"excerpt":"grandmother n.","risk":"A1_NINTH_TWELVE_GRANDMOTHER_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Review Myanmar spelling အဘွား versus အဖွား and family nuance. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"grandfather","page":2,"line":334,"excerpt":"grandfather n.","risk":"A1_NINTH_TWELVE_GRANDFATHER_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Check maternal/paternal family nuance and Myanmar usage. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"uncle","page":4,"line":834,"excerpt":"uncle n.","risk":"A1_NINTH_TWELVE_UNCLE_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Distinguish uncle by blood or marriage and Myanmar kinship nuance. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"aunt","page":1,"line":52,"excerpt":"aunt n.","risk":"A1_NINTH_TWELVE_AUNT_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Distinguish aunt by blood or marriage and Myanmar kinship nuance. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"phone","page":3,"line":588,"excerpt":"phone n., v.","risk":"A1_NINTH_TWELVE_PHONE_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Oxford lists noun and verb; draft is device noun, not verb. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"computer","page":1,"line":168,"excerpt":"computer n.","risk":"A1_NINTH_TWELVE_COMPUTER_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Ensure definition denotes computing, not any electronic machine. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"picture","page":3,"line":593,"excerpt":"picture n.","risk":"A1_NINTH_TWELVE_PICTURE_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Distinguish image, drawing, painting and photograph senses. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"bag","page":1,"line":58,"excerpt":"bag n.","risk":"A1_NINTH_TWELVE_BAG_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Distinguish carrying container from quantity or bag-shaped senses. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."},{"word":"money","page":2,"line":492,"excerpt":"money n.","risk":"A1_NINTH_TWELVE_MONEY_EXACT_SENSE_BILINGUAL_REVIEW","task":"Independent human reviewer: Frozen cash-only definition may exclude bank or electronic money. Verify exact publisher-backed sense/CEFR, English definition, fluent Myanmar, original example grammar, historical source provenance and British usage; Oxford word/POS listing alone is not independent approval."}]''')
PRIOR = ["A1-TWELVE-DIRECT-PDF-2026-10-28","A1-SECOND-TWELVE-2026-10-28","A1-THIRD-TWELVE-2026-10-28","A1-FOURTH-TWENTYFOUR-2026-10-29","A1-FIFTH-TWENTYFOUR-2026-10-29","A1-SIXTH-TWENTYFOUR-2026-10-29","A1-SEVENTH-TWELVE-2026-10-29","A1-EIGHTH-TWELVE-2026-10-29"]

def need(ok, why):
    if not ok:
        raise ValueError(why)

def audit(packet, shortlist):
    raw = SHORT.read_bytes()
    sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(sha == SHA, "Frozen shortlist Git blob drift")
    entries = shortlist["entries"]
    by_word = {e["word"]: e for e in entries}
    need(len(entries) == len(by_word) == 1000, "Headword count or duplicate drift")
    need(shortlist["counts_by_level"] == {l: 200 for l in LEVELS}
         and shortlist["independently_approved_by_level"] == {l: 0 for l in LEVELS},
         "Scope or approvals changed")
    need(packet["schema"] == 1 and packet["scope"] == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet["status"] == "A1_NINTH_TWELVE_DIRECT_OXFORD_WORD_POS_EDITORIAL_HOLD"
         and packet["observed_on"] == "2026-10-29" and packet["shortlist_blob_sha"] == SHA,
         "Packet scope or provenance changed")
    need(packet["record_count"] == len(packet["records"]) == 12
         and packet["counts_by_level"] == {"A1":12,"A2":0,"B1":0,"B2":0,"C1":0}
         and packet["publisher_reference_level_counts"] == {"A1":12,"A2":0,"B1":0,"B2":0,"C1":0}
         and packet["word_pos_discrepancies"] == packet["independently_approved_count"] == 0
         and packet["source_limitations"] == LIMIT, "Counts, limits or approval drift")
    words = {e["word"] for e in EXPECTED}
    need(len(words) == 12, "Expected words duplicated")
    for suffix in PRIOR:
        old = json.loads((ROOT / ("draft/CEFR-1000-OXFORD-" + suffix + ".json")).read_text("utf-8"))
        need(not words.intersection(x["word"] for x in old["records"]), "Repeated earlier A1 observation")
    for row, exp in zip(packet["records"], EXPECTED):
        src = by_word[exp["word"]]
        need(row["word"] == exp["word"] and row["level"] == src["level"] == "A1"
             and row["part_of_speech"] == src["part_of_speech"] == "noun",
             "Word/order/level/POS drift")
        need(row["shortlist_snapshot"] == {
            "english_definition":src["english_definition"],"myanmar_meaning":src["burmese_meaning"],
            "example_sentence":src["example_sentence"]}, "Frozen English/Myanmar/example drift")
        need(row["shortlist_provenance"] == {k:src[k] for k in
             ("source_path","source_index","source_blob_sha")}, "Git provenance drift")
        need(row["publisher_source"] == {
            "publisher":"Oxford University Press","title":"The Oxford 3000 by CEFR level",
            "url":URL,"observed_on":"2026-10-29","pdf_page":exp["page"],
            "extracted_line":exp["line"],"source_excerpt":exp["excerpt"],
            "source_cefr_level":"A1","evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"}, "Oxford URL/date/locator/word-POS forged")
        need(row["editorial_risk"] == exp["risk"] and row["independent_reviewer_task"] == exp["task"],
             "Reviewer task or risk drift")
        need(row["editorial_hold"] is True and row["independently_reviewed"] is False
             and row["release_approved"] is False and row["independent_reviewer_receipt"] is None,
             "False independent signoff")
    return True

def self_test(packet, shortlist):
    cases = [
        (("word",),"forged"), (("level",),"C1"), (("part_of_speech",),"verb"),
        (("shortlist_snapshot","english_definition"),"forged"),
        (("shortlist_snapshot","myanmar_meaning"),"အမှား"),
        (("shortlist_snapshot","example_sentence"),"forged"),
        (("shortlist_provenance","source_blob_sha"),"0"*40),
        (("publisher_source","url"),"https://example.com/forged.pdf"),
        (("publisher_source","observed_on"),"2026-01-01"),
        (("publisher_source","pdf_page"),99),
        (("publisher_source","extracted_line"),-1),
        (("publisher_source","source_excerpt"),"forged n."),
        (("editorial_risk",),"FORGED_RISK"), (("independent_reviewer_task",),"FORGED_TASK"),
        (("editorial_hold",),False), (("independently_reviewed",),True),
        (("release_approved",),True), (("independent_reviewer_receipt",),{"reviewer":"fake"}),
    ]
    rejected = 0
    for index in range(12):
        for path, fake in cases:
            p = copy.deepcopy(packet)
            target = p["records"][index]
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = fake
            try:
                audit(p, shortlist)
            except (ValueError, KeyError, TypeError):
                rejected += 1
            else:
                raise AssertionError("Forged source/review accepted")
    for field, fake in [("record_count",13),("independently_approved_count",1),
                        ("status","APPROVED"),("source_limitations",""),
                        ("records",packet["records"][:-1])]:
        p = copy.deepcopy(packet)
        p[field] = fake
        try:
            audit(p, shortlist)
        except (ValueError, KeyError, TypeError):
            rejected += 1
        else:
            raise AssertionError("Forged packet header accepted")
    need(rejected == 221, "Adversarial test count drift")
    return rejected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS,"ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text("utf-8"))
    shortlist = json.loads(SHORT.read_text("utf-8"))
    audit(packet, shortlist)
    print("PASS: 12 A1 family/home Oxford word-POS leads; 0 independent approvals")
    if args.self_test:
        n = self_test(packet, shortlist)
        print("PASS: rejected %d/%d forged source/bilingual/reviewer mutations" % (n,n))

if __name__ == "__main__":
    main()
