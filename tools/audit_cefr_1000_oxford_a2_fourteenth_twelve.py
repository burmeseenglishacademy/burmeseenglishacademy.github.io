#!/usr/bin/env python3
"""Fail-closed A2 fourteenth Oxford evidence audit. Never grants human approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-FOURTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "1dbc906d030c0400b9dbf2d48b869625722397a3"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF_BASE = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_"
EXPECTED = (("type","A1",4,832,"type n.","3000"),("action","A1",1,8,"action n.","3000"),("board","A2",4,1002,"board n.","3000"),("field","A2",5,1208,"field n.","3000"),("instead","A2",5,1308,"instead adv.","3000"),("moment","A1",2,490,"moment n.","3000"),("energy","A2",5,1166,"energy n.","3000"),("hear","A1",2,359,"hear v.","3000"),("rest","A2",6,1558,"rest (sleep/relax) n., v.","3000"),("term","A2",7,1697,"term n.","3000"),("miss","A1",2,486,"miss v.","3000"),("site","A2",6,1620,"site n.","3000"))
SENSES = {"board":("https://www.oxfordlearnersdictionaries.com/definition/english/board_1",1,105,114),"rest":("https://www.oxfordlearnersdictionaries.com/definition/english/rest_1",3,128,138),"term":("https://www.oxfordlearnersdictionaries.com/definition/english/term_1",1,105,118),"miss":("https://www.oxfordlearnersdictionaries.com/definition/english/miss_1",8,205,215)}
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def require(test, reason):
    if not test:
        raise ValueError(reason)

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet=None, shortlist=None):
    require(blob_sha(PACKET) == PACKET_SHA, "Pinned publisher packet changed")
    require(blob_sha(SHORTLIST) == SHORTLIST_SHA, "Frozen shortlist changed")
    p = packet if packet is not None else json.loads(PACKET.read_text(encoding="utf-8"))
    s = shortlist if shortlist is not None else json.loads(SHORTLIST.read_text(encoding="utf-8"))
    require(len(s.get("entries", [])) == 1000
            and s.get("counts_by_level") == dict.fromkeys(LEVELS, 200)
            and s.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Frozen 1,000 / five-level / zero-approval contract changed")
    by_word = {e["word"]: e for e in s["entries"]}
    require(len(by_word) == 1000, "Duplicate frozen headword")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english","reviewed_burmese","reviewed_example",
                         "reviewed_level","reviewed_pronunciation")) for e in s["entries"]),
            "Unverified shortlist reviewer flags changed")
    require(p.get("schema") == 1 and p.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and p.get("status") == "A2_FOURTEENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and p.get("observed_on") == "2026-10-31"
            and p.get("shortlist_blob_sha") == SHORTLIST_SHA
            and p.get("record_count") == 12
            and p.get("counts_by_level") == {"A1":0,"A2":12,"B1":0,"B2":0,"C1":0}
            and p.get("publisher_reference_level_counts") == {"A1":5,"A2":7,"B1":0,"B2":0,"C1":0}
            and p.get("word_pos_discrepancies") == 5
            and p.get("direct_dictionary_sense_leads") == 4
            and p.get("independently_approved_count") == 0
            and "not independent exact-sense cefr approval" in p.get("source_limitations","").lower(),
            "Publisher research scope/counts or editorial hold changed")
    rows = p.get("records")
    require(isinstance(rows, list) and len(rows) == 12, "Twelve records required")
    for r, (word, cefr, page, line, excerpt, list_id) in zip(rows, EXPECTED):
        e = by_word[word]
        require(e["level"] == "A2" and r.get("word") == word
                and r.get("level") == "A2" and r.get("part_of_speech") == e["part_of_speech"],
                "A2 word/POS mismatch: " + word)
        require(r.get("shortlist_snapshot") == {
                    "english_definition":e["english_definition"],
                    "myanmar_meaning":e["burmese_meaning"],
                    "example_sentence":e["example_sentence"]},
                "Bilingual/example snapshot changed: " + word)
        require(r.get("shortlist_provenance") == {
                    k:e[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical Git source provenance changed: " + word)
        require(r.get("publisher_source") == {
                    "publisher":"Oxford University Press",
                    "title":"The Oxford " + list_id + " by CEFR level",
                    "url":PDF_BASE + list_id + "_by_CEFR_level.pdf",
                    "observed_on":"2026-10-31",
                    "pdf_page":page,"extracted_line":line,
                    "source_excerpt":excerpt,"source_cefr_level":cefr,
                    "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                    "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Publisher PDF level, page/line or excerpt drift: " + word)
        require(len(r.get("editorial_risk","")) >= 40
                and "Independent human editor" in r.get("independent_reviewer_task",""),
                "Exact-sense human review task missing: " + word)
        require(r.get("editorial_hold") is True
                and r.get("independently_reviewed") is False
                and r.get("release_approved") is False
                and r.get("independent_reviewer_receipt") is None,
                "Fabricated reviewer or release approval: " + word)
        lead = r.get("dictionary_sense_lead")
        proposal = r.get("editorial_rewrite_candidate")
        if word in SENSES:
            url, number, start, end = SENSES[word]
            require(isinstance(lead, dict)
                    and lead.get("url") == url and lead.get("sense_number") == number
                    and lead.get("page_text_line_start") == start
                    and lead.get("page_text_line_end") == end
                    and lead.get("observed_on") == "2026-10-31"
                    and lead.get("evidence_scope") == "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and len(lead.get("sense_summary","")) > 50,
                    "Dictionary exact-sense attribution changed: " + word)
            require(isinstance(proposal,dict)
                    and len(proposal.get("myanmar_meaning","")) >= 12
                    and len(proposal.get("original_example","")) >= 25
                    and proposal.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL",
                    "Editorial alternative falsely approved: " + word)
        else:
            require(lead is None and proposal is None,
                    "Unobserved dictionary sense claimed: " + word)
    return True

def self_test():
    truth = json.loads(PACKET.read_text(encoding="utf-8"))
    count = 0
    cases = [
        (("word",), "forged"),
        (("publisher_source","source_cefr_level"), "FORGED"),
        (("publisher_source","pdf_page"), 99),
        (("publisher_source","extracted_line"), -1),
        (("publisher_source","source_excerpt"), "forged"),
        (("publisher_source","url"), "https://example.invalid/forged.pdf"),
        (("shortlist_snapshot","english_definition"), "forged"),
        (("shortlist_snapshot","myanmar_meaning"), "forged"),
        (("shortlist_snapshot","example_sentence"), "forged"),
        (("shortlist_provenance","source_blob_sha"), "forged"),
        (("editorial_hold",), False),
        (("independently_reviewed",), True),
        (("release_approved",), True),
        (("independent_reviewer_receipt",), {"fake":True}),
    ]
    for i in range(12):
        for path, value in cases:
            altered = copy.deepcopy(truth)
            target = altered["records"][i]
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = value
            try:
                audit(altered)
            except (ValueError, KeyError, TypeError):
                count += 1
            else:
                raise AssertionError("Forged evidence or approval escaped")
        if truth["records"][i].get("dictionary_sense_lead"):
            for path, value in (
                (("dictionary_sense_lead","url"),"https://example.invalid"),
                (("dictionary_sense_lead","sense_number"),999),
                (("dictionary_sense_lead","page_text_line_start"),0),
                (("editorial_rewrite_candidate","review_status"),"APPROVED"),
            ):
                altered = copy.deepcopy(truth)
                target = altered["records"][i]
                for key in path[:-1]:
                    target = target[key]
                target[path[-1]] = value
                try:
                    audit(altered)
                except (ValueError, KeyError, TypeError):
                    count += 1
                else:
                    raise AssertionError("Forged dictionary sense or review escaped")
    require(count == 184, "Unexpected adversarial mutation coverage")
    print("PASS: 184/184 A2 fourteenth forged publisher, Myanmar, grammar, provenance and approval mutations rejected")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS,"ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    audit()
    if args.self_test:
        self_test()
    print(json.dumps({"level":args.level,"source_records":12,"direct_dictionary_sense_leads":4,
                      "independently_approved":0,"release":"BLOCKED_STAGING_ONLY"},
                     sort_keys=True))

if __name__ == "__main__":
    main()
