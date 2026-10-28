#!/usr/bin/env python3
"""Staging-only integrity audit: 24 Oxford A2-draft publisher word/POS observations.

Checks content binding and rejects fabricated approvals; cannot authenticate
publisher facts or human linguistic review. NEVER deploys.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-THIRD-TWENTYFOUR-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
URL = ("https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/"
       "oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf")
EXPECTED = json.loads(r'''[["public","A2",6,1512,"public adj., n.","PUBLIC_NOUN_VS_ADJECTIVE_AND_COMMUNITY_SCOPE"],["system","A2",7,1687,"system n.","SYSTEM_CONNECTED_PARTS_VS_DIGITAL_ORDER_TRACKING"],["support","A2",7,1678,"support v., n.","SUPPORT_VERB_HELP_VS_NOUN"],["power","A2",6,1491,"power n.","POWER_AUTHORITY_VS_GENERAL_CONTROL_AND_ENERGY"],["side","A2",6,1612,"side n.","SIDE_SURFACE_VS_EDGE"],["business","A1",1,115,"business n.","A1_BUSINESS_VS_A2_DRAFT"],["however","A1",2,382,"however adv.","A1_HOWEVER_CONTRAST_VS_A2_DRAFT"],["nothing","A1",3,533,"nothing pron.","A1_NOTHING_VS_A2_DRAFT"],["actually","A2",4,918,"actually adv.","ACTUALLY_CORRECTION_VS_FACTUALITY"],["less","A2",5,1356,"less det./pron., adv.","LESS_DETERMINER_UNCOUNTABLE_VS_ADVERB"],["party","A1",3,576,"party n.","A1_SOCIAL_EVENT_VS_A2_DRAFT"],["whole","A2",7,1763,"whole adj.","WHOLE_COMPLETE_VS_TIME_DURATION"],["maybe","A1",2,469,"maybe adv.","A1_MAYBE_VS_A2_DRAFT"],["story","A1",3,742,"story n.","A1_NARRATIVE_VS_A2_DRAFT"],["health","A1",2,357,"health n.","A1_HEALTH_VS_A2_DRAFT"],["hope","A1",2,374,"hope v.","A1_HOPE_VS_A2_DRAFT"],["important","A1",2,392,"important adj.","A1_IMPORTANT_VS_A2_DRAFT"],["information","A1",2,396,"information n.","A1_INFORMATION_UNCOUNTABLE_VS_A2_DRAFT"],["local","A1",2,450,"local adj.","A1_LOCAL_VS_A2_DRAFT"],["course","A1",1,178,"course n.","A1_COURSE_STUDY_VS_OTHER_SENSES"],["video","A1",4,848,"video n.","A1_VIDEO_VS_A2_DRAFT"],["ago","A1",1,21,"ago adv.","A1_AGO_VS_A2_DRAFT"],["fact","A1",2,265,"fact n.","A1_FACT_VS_A2_DRAFT"],["half","A1",2,346,"half n., det./pron.","HALF_NOUN_VS_QUANTIFIER_AND_A1_DRAFT_CONFLICT"]]''')
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def git_blob_sha(path):
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def audit(packet, shortlist, sha):
    require(sha == SHORTLIST_SHA and packet.get("shortlist_blob_sha") == sha,
            "Source shortlist changed or provenance unbound")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY",
            "Scope invalid")
    require(packet.get("status") == "A2_THIRD_TWENTYFOUR_DIRECT_OXFORD_WORD_POS_TRIAGE_EDITORIAL_HOLD",
            "Status drift")
    require(packet.get("observed_on") == "2026-10-29", "Observation date drift")
    require(packet.get("record_count") == 24 and type(packet.get("record_count")) is int,
            "Record count drift")
    require(packet.get("counts_by_level") == dict(A1=0, A2=24, B1=0, B2=0, C1=0),
            "Quota drift")
    require(packet.get("publisher_reference_level_counts") ==
            dict(A1=16, A2=8, B1=0, B2=0, C1=0), "Oxford levels drift")
    require(packet.get("word_pos_discrepancies") == 16, "Discrepancy count drift")
    require(packet.get("independently_approved_count") == 0, "False independent approval")
    require("NOT exact-sense CEFR" in packet.get("source_limitations", ""),
            "Missing word/POS-only caveat")
    entries = [e for e in shortlist.get("entries", []) if e.get("level") == "A2"]
    require(len(entries) == 200 and len({e.get("word") for e in entries}) == 200,
            "A2 shortlist quota/uniqueness drift")
    byword = {e["word"]: e for e in entries}
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == len(EXPECTED),
            "Wrong packet size")
    require(len({r.get("word") for r in records if isinstance(r, dict)}) == 24,
            "Duplicate headword")
    for i, (word, oxlevel, page, line, excerpt, risk_id) in enumerate(EXPECTED):
        r = records[i]
        require(isinstance(r, dict) and r.get("word") == word and r.get("level") == "A2",
                f"{word}: identity/level drift")
        e = byword[word]
        require(r.get("part_of_speech") == e.get("part_of_speech"),
                f"{word}: POS drift")
        require(r.get("shortlist_snapshot") == dict(
            english_definition=e.get("english_definition"),
            myanmar_meaning=e.get("burmese_meaning"),
            example_sentence=e.get("example_sentence")),
            f"{word}: definition/Myanmar/example altered")
        require(r.get("shortlist_provenance") == dict(
            source_path=e.get("source_path"), source_index=e.get("source_index"),
            source_blob_sha=e.get("source_blob_sha")), f"{word}: Git provenance drift")
        require(r.get("publisher_source") == dict(
            publisher="Oxford University Press",
            title="The Oxford 3000 by CEFR level", url=URL,
            observed_on="2026-10-29", pdf_page=page, extracted_line=line,
            source_excerpt=excerpt, source_cefr_level=oxlevel,
            evidence_scope="DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            access="DIRECT_OFFICIAL_PDF_WEB_TEXT"),
            f"{word}: source evidence tampered")
        require(r.get("editorial_risk_id") == risk_id
                and isinstance(r.get("editorial_risk"), str)
                and len(r["editorial_risk"]) >= 70, f"{word}: editorial risk lost")
        task = r.get("independent_reviewer_task")
        require(isinstance(task, str) and word in task and risk_id in task
                and "Human-independent" in task and len(task) >= 220,
                f"{word}: independent review task lost")
        require(r.get("editorial_hold") is True
                and r.get("independently_reviewed") is False
                and r.get("release_approved") is False
                and r.get("independent_reviewer_receipt") is None,
                f"{word}: fabricated approval")
    leads = packet.get("secondary_indexed_sense_leads")
    require(isinstance(leads, list) and len(leads) == 2, "Cambridge sense leads missing")
    for r, word, level, heading in zip(leads, ("power", "less"), ("B2", "A2"),
                                      ("power noun (CONTROL)",
                                       "less determiner, pronoun, adverb (SMALLER AMOUNT)")):
        require(r.get("word") == word and r.get("indexed_cefr_level") == level
                and r.get("source_sense_heading") == heading
                and r.get("publisher") == "Cambridge University Press"
                and r.get("source_url") == "https://dictionary.cambridge.org/dictionary/english/" + word
                and r.get("observed_on") == "2026-10-29"
                and r.get("access") == "PUBLISHER_SEARCH_INDEX_ONLY_DIRECT_PAGE_HTTP_403"
                and r.get("source_scope") ==
                    "SEARCH_INDEXED_SENSE_LEAD_NOT_INDEPENDENT_EXACT_SENSE_EVIDENCE"
                and r.get("independently_verified") is False
                and isinstance(r.get("editorial_risk"), str)
                and len(r["editorial_risk"]) > 60,
                f"{word}: Cambridge indexed lead misrepresented")
    return len(records)

def self_test(packet, shortlist, sha):
    total = 0
    for i in range(24):
        p = copy.deepcopy(packet)
        p["records"][i]["publisher_source"]["source_excerpt"] = "invented dictionary CEFR label"
        try:
            audit(p, shortlist, sha)
        except ValueError:
            total += 1
        else:
            raise AssertionError(f"Forged Oxford source {i} passed")
    changes = [
        lambda p: p.update(record_count=25),
        lambda p: p.update(word_pos_discrepancies=0),
        lambda p: p.update(independently_approved_count=24),
        lambda p: p.update(shortlist_blob_sha="0"*40),
        lambda p: p["records"][0].update(editorial_hold=False),
        lambda p: p["records"][1].update(independently_reviewed=True),
        lambda p: p["records"][2].update(release_approved=True),
        lambda p: p["records"][3].update(independent_reviewer_receipt={"reviewer":"bot"}),
        lambda p: p["records"][4]["shortlist_snapshot"].update(myanmar_meaning="approved"),
        lambda p: p["records"][5]["shortlist_snapshot"].update(example_sentence="Changed."),
        lambda p: p["records"][6]["shortlist_provenance"].update(source_index=9999),
        lambda p: p["records"][7]["publisher_source"].update(source_cefr_level="C1"),
        lambda p: p["records"][8]["publisher_source"].update(url="https://example.com/fake.pdf"),
        lambda p: p["records"][9]["publisher_source"].update(evidence_scope="EXACT_SENSE"),
        lambda p: p["records"][10].update(editorial_risk_id=""),
        lambda p: p["records"][11].update(independent_reviewer_task="approved"),
        lambda p: p["records"][12].update(part_of_speech="verb"),
        lambda p: p["records"][13].update(level="B1"),
        lambda p: p["records"][14]["publisher_source"].update(pdf_page=0),
        lambda p: p["records"][15]["publisher_source"].update(extracted_line=10000),
        lambda p: p["records"].reverse(),
        lambda p: p["secondary_indexed_sense_leads"][0].update(independently_verified=True),
        lambda p: p["secondary_indexed_sense_leads"][1].update(access="DIRECT_PUBLISHER_DICTIONARY_PAGE"),
        lambda p: p["secondary_indexed_sense_leads"][0].update(indexed_cefr_level="A2"),
    ]
    for i, change in enumerate(changes):
        p = copy.deepcopy(packet)
        change(p)
        try:
            audit(p, shortlist, sha)
        except ValueError:
            total += 1
        else:
            raise AssertionError(f"False-signoff/provenance mutation {i} passed")
    return total

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    n = audit(packet, shortlist, git_blob_sha(SHORTLIST))
    print(f"PASS A2 third Oxford packet: {n} word/POS research leads; 16 lower-level conflicts; 0 approvals; {args.level}; NO release")
    if args.self_test:
        m = self_test(packet, shortlist, git_blob_sha(SHORTLIST))
        print(f"PASS {m}/{m} forged-source and false-approval mutations rejected")

if __name__ == "__main__":
    main()
