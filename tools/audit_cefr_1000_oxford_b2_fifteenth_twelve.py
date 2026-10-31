#!/usr/bin/env python3
"""Fail-closed B2 fifteenth direct Oxford word/POS evidence and unapproved sense-lead audit.

The packet is staging research, NOT independently reviewed language, audio,
physical iPhone testing, release approval or publication permission.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-FIFTEENTH-TWELVE-AND-FOUR-DICTIONARY-SENSE-LEADS-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "4eea6c62b2035fc01dde8fb8972805402f81dc43"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
PDF_BASE = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_"
EXPECTED = [["administrative","C1",3,737,"administrative adj.","5000"],["argue","A2",4,955,"argue v.","3000"],["colour","A1",1,162,"colour n.","3000"],["defend","B2",11,2767,"defend v.","3000"],["element","B1",8,2010,"element n.","3000"],["extension","B2",1,237,"extension n.","5000"],["extent","B2",11,2843,"extent n.","3000"],["harm","B2",11,2899,"harm n., v.","3000"],["hunt","B1",8,2127,"hunt v.","3000"],["impressive","B1",8,2140,"impressive adj.","3000"],["moral","B2",11,3013,"moral adj., n.","3000"],["offensive","B2",11,3038,"offensive adj.","3000"]]
SENSES = {"administrative":"https://www.oxfordlearnersdictionaries.com/definition/english/administrative","colour":"https://www.oxfordlearnersdictionaries.com/definition/english/colour_1","harm":"https://www.oxfordlearnersdictionaries.com/definition/english/harm_1","moral":"https://www.oxfordlearnersdictionaries.com/definition/english/moral_1"}

def require(ok, why):
    if not ok:
        raise ValueError(why)

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(packet=None, shortlist=None):
    require(blob_sha(PACKET) == PACKET_SHA, "Research packet Git blob drift")
    require(blob_sha(SHORTLIST) == SHORTLIST_SHA, "Frozen shortlist Git blob drift")
    p = packet if packet is not None else json.loads(PACKET.read_text(encoding="utf-8"))
    s = shortlist if shortlist is not None else json.loads(SHORTLIST.read_text(encoding="utf-8"))
    require(len(s.get("entries", [])) == 1000
            and s.get("counts_by_level") == dict.fromkeys(LEVELS, 200)
            and s.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Incorrect frozen 1000 scope or fake approval")
    by_word = {e["word"]: e for e in s["entries"]}
    require(len(by_word) == 1000, "Duplicate frozen shortlist word")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english", "reviewed_burmese", "reviewed_example",
                         "reviewed_level", "reviewed_pronunciation"))
                for e in s["entries"]), "Forged shortlist review flags")
    require(p.get("schema") == 1 and p.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and p.get("status") == "B2_FIFTEENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD"
            and p.get("observed_on") == "2026-10-31"
            and p.get("shortlist_blob_sha") == SHORTLIST_SHA
            and p.get("record_count") == 12
            and p.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":12,"C1":0}
            and p.get("publisher_reference_level_counts") == {"A1":1,"A2":1,"B1":3,"B2":6,"C1":1}
            and p.get("word_pos_discrepancies") == 6
            and p.get("direct_dictionary_sense_leads") == 4
            and p.get("independently_approved_count") == 0
            and "not exact-sense cefr evidence" in p.get("source_limitations","").lower(),
            "Publisher research scope, count or limitations drift")
    rows = p.get("records")
    require(isinstance(rows, list) and len(rows) == 12, "Expected twelve B2 research rows")
    for r, (word, cefr, page, line, excerpt, list_id) in zip(rows, EXPECTED):
        e = by_word[word]
        require(e["level"] == "B2" and r.get("word") == word
                and r.get("level") == "B2" and r.get("part_of_speech") == e["part_of_speech"],
                "Draft word/POS drift: " + word)
        require(r.get("shortlist_snapshot") == {
                    "english_definition":e["english_definition"],
                    "myanmar_meaning":e["burmese_meaning"],
                    "example_sentence":e["example_sentence"]},
                "Frozen English/Myanmar/example changed: " + word)
        require(r.get("shortlist_provenance") == {
                    k:e[k] for k in ("source_path","source_index","source_blob_sha")},
                "Original Git source provenance drift: " + word)
        historical = ROOT / e["source_path"]
        require(historical.is_file() and blob_sha(historical) == e["source_blob_sha"],
                "Original source Git blob mismatch: " + word)
        original = json.loads(historical.read_text(encoding="utf-8"))["entries"][e["source_index"]]
        require(all(original.get(k) == e.get(k) for k in
                    ("word","level","part_of_speech","english_definition",
                     "burmese_meaning","example_sentence")),
                "Historical original entry mismatch: " + word)
        require(r.get("publisher_source") == {
                    "publisher":"Oxford University Press",
                    "title":"The Oxford " + list_id + " by CEFR level",
                    "url":PDF_BASE + list_id + "_by_CEFR_level.pdf",
                    "observed_on":"2026-10-31",
                    "pdf_page":page,"extracted_line":line,
                    "source_excerpt":excerpt,"source_cefr_level":cefr,
                    "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                    "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Oxford PDF excerpt, level or locator changed: " + word)
        require(isinstance(r.get("editorial_risk"), str)
                and len(r["editorial_risk"]) >= 45
                and "Independent human editor" in r.get("independent_reviewer_task", ""),
                "Human exact-sense review task missing: " + word)
        require(r.get("editorial_hold") is True
                and r.get("independently_reviewed") is False
                and r.get("release_approved") is False
                and r.get("independent_reviewer_receipt") is None,
                "Forged independent review or release flag: " + word)
        lead, proposal = r.get("dictionary_sense_lead"), r.get("editorial_rewrite_candidate")
        if word in SENSES:
            require(isinstance(lead, dict) and lead.get("url") == SENSES[word]
                    and lead.get("sense_number") == 1
                    and lead.get("observed_on") == "2026-10-31"
                    and lead.get("access") == "PUBLISHER_DICTIONARY_WEB_SEARCH_INDEXED_EXTRACT_NOT_HUMAN_VERIFIED"
                    and lead.get("evidence_scope") == "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and len(lead.get("sense_summary","")) > 60,
                    "Unsubstantiated or altered dictionary sense lead: " + word)
            require(isinstance(proposal, dict)
                    and len(proposal.get("myanmar_meaning","")) >= 12
                    and len(proposal.get("original_example","")) >= 25
                    and proposal.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL",
                    "Forged editorial rewrite approval: " + word)
        else:
            require(lead is None and proposal is None,
                    "Invented dictionary sense lead: " + word)
    return True

def self_test():
    original = json.loads(PACKET.read_text(encoding="utf-8"))
    mutations = [
        (("word",), "forged"), (("part_of_speech",), "forged"),
        (("publisher_source","source_cefr_level"), "C2"),
        (("publisher_source","pdf_page"), 99),
        (("publisher_source","extracted_line"), -1),
        (("publisher_source","source_excerpt"), "forged"),
        (("publisher_source","url"), "https://example.invalid/forged.pdf"),
        (("shortlist_snapshot","english_definition"), "forged"),
        (("shortlist_snapshot","myanmar_meaning"), "forged"),
        (("shortlist_snapshot","example_sentence"), "forged"),
        (("shortlist_provenance","source_blob_sha"), "forged"),
        (("shortlist_provenance","source_path"), "draft/forged.json"),
        (("shortlist_provenance","source_index"), -1),
        (("editorial_hold",), False),
        (("independently_reviewed",), True),
        (("release_approved",), True),
        (("independent_reviewer_receipt",), {"fake":True}),
    ]
    count = 0
    for i in range(12):
        for path, value in mutations:
            forged = copy.deepcopy(original)
            target = forged["records"][i]
            for k in path[:-1]:
                target = target[k]
            target[path[-1]] = value
            try:
                audit(forged)
            except (ValueError, KeyError, TypeError):
                count += 1
            else:
                raise AssertionError("Forged Oxford, bilingual or review evidence accepted")
        if original["records"][i].get("dictionary_sense_lead"):
            for path, value in (
                (("dictionary_sense_lead","url"), "https://example.invalid"),
                (("dictionary_sense_lead","sense_number"), 99),
                (("dictionary_sense_lead","access"), "DIRECT_HUMAN_APPROVED"),
                (("editorial_rewrite_candidate","review_status"), "APPROVED"),
            ):
                forged = copy.deepcopy(original)
                target = forged["records"][i]
                for k in path[:-1]:
                    target = target[k]
                target[path[-1]] = value
                try:
                    audit(forged)
                except (ValueError, KeyError, TypeError):
                    count += 1
                else:
                    raise AssertionError("Forged dictionary lead or approval accepted")
    require(count == 220, "Unexpected adversarial mutation count")
    print("PASS: 220/220 B2 fifteenth forged publisher, Myanmar, grammar, provenance and approval mutations rejected")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS,"ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    audit()
    if args.self_test:
        self_test()
    print(json.dumps({"level":args.level,"publisher_word_pos_observations":12,
                      "publisher_level_discrepancies":6,"dictionary_sense_leads":4,
                      "independently_approved":0,"release":"BLOCKED_STAGING_ONLY"},
                     sort_keys=True))

if __name__ == "__main__":
    main()
