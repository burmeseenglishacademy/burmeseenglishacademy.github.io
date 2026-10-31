#!/usr/bin/env python3
"""Fail-closed research-only audit for the last ten provisional B2 Oxford observations.
No independent CEFR, bilingual, voice, iPhone, hosting or release signoff is implied.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-SIXTEENTH-FINAL-TEN-AND-FIVE-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "e8debad4dc51ec7946ba7f1208a02b0f67e9068e"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
# Word, source CEFR (None = not listed in BOTH inspected PDFs), PDF id,
# one-based page, zero-based extracted line, literal PDF entry.
EXPECTED = [
    ("package", "B1", "3000", 9, 2262, "package n."),
    ("pride", "B2", "5000", 2, 479, "pride n."),
    ("province", "C1", "5000", 6, 1643, "province n."),
    ("railway", "A2", "3000", 6, 1523, "railway n."),
    ("relative", "B1", "3000", 9, 2365, "relative adj., n."),
    ("repeat", "A1", "3000", 3, 647, "repeat v."),
    ("server", None, None, None, None, None),
    ("shock", "B2", "3000", 12, 3190, "shock n., v."),
    ("silence", "B2", "3000", 12, 3196, "silence n."),
    ("superior", "C1", "5000", 7, 1860, "superior adj."),
]
SENSES = {
    "package": ("https://www.oxfordlearnersdictionaries.com/definition/english/package_1", 3),
    "pride": ("https://www.oxfordlearnersdictionaries.com/definition/english/pride_1", 1),
    "province": ("https://www.oxfordlearnersdictionaries.com/us/definition/english/province", 1),
    "relative": ("https://www.oxfordlearnersdictionaries.com/definition/english/relative_1", 1),
    "server": ("https://www.oxfordlearnersdictionaries.com/definition/english/server", 1),
}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def validate(packet, shortlist):
    require(blob(PACKET) == PACKET_SHA and blob(SHORTLIST) == SHORTLIST_SHA,
            "Research packet or frozen shortlist Git blob changed")
    require(len(shortlist.get("entries", [])) == 1000
            and shortlist.get("counts_by_level") == dict.fromkeys(LEVELS, 200)
            and shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Wrong 1,000-word scope or fake independent approvals")
    source = {e["word"]: e for e in shortlist["entries"]}
    require(len(source) == 1000, "Duplicate frozen headword")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english", "reviewed_burmese", "reviewed_example",
                         "reviewed_level", "reviewed_pronunciation"))
                for e in shortlist["entries"]), "Frozen review flags altered")
    require(packet.get("schema") == 1
            and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == "B2_SIXTEENTH_FINAL_TEN_NINE_OXFORD_WORD_POS_ONE_CORE_LIST_UNLISTED_FIVE_DIRECT_DICTIONARY_SENSE_LEADS_EDITORIAL_HOLD"
            and packet.get("observed_on") == "2026-10-31"
            and packet.get("shortlist_blob_sha") == SHORTLIST_SHA
            and packet.get("record_count") == 10
            and packet.get("counts_by_level") == {"A1":0,"A2":0,"B1":0,"B2":10,"C1":0}
            and packet.get("publisher_reference_level_counts") ==
                {"A1":1,"A2":1,"B1":2,"B2":3,"C1":2,"UNLISTED":1}
            and packet.get("word_pos_discrepancies") == 7
            and packet.get("direct_dictionary_sense_leads") == 5
            and packet.get("independently_approved_count") == 0
            and "not independent exact-sense cefr evidence" in packet.get("source_limitations", "").lower(),
            "Publisher research scope/count or signoff drift")
    records = packet.get("records")
    require(isinstance(records, list) and len(records) == 10, "Ten records required")
    for row, (word, level, pdfid, page, line, excerpt) in zip(records, EXPECTED):
        e = source[word]
        require(e["level"] == "B2" and row.get("word") == word
                and row.get("level") == "B2"
                and row.get("part_of_speech") == e["part_of_speech"],
                "Draft word/POS changed: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": e["english_definition"],
            "myanmar_meaning": e["burmese_meaning"],
            "example_sentence": e["example_sentence"]},
            "Original bilingual snapshot changed: " + word)
        require(row.get("shortlist_provenance") ==
                {k:e[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical source pointer changed: " + word)
        historical = ROOT / e["source_path"]
        require(historical.is_file() and blob(historical) == e["source_blob_sha"],
                "Historical Git source blob mismatch: " + word)
        original = json.loads(historical.read_text(encoding="utf-8"))["entries"][e["source_index"]]
        require(all(original.get(k) == e.get(k) for k in
                    ("word","level","part_of_speech","english_definition",
                     "burmese_meaning","example_sentence")),
                "Historical source row mismatch: " + word)
        p = row.get("publisher_source")
        require(isinstance(p, dict), "Missing publisher evidence")
        expected_pub = {
            "publisher":"Oxford University Press",
            "title":"The Oxford " + pdfid + " by CEFR level" if pdfid
                    else "Oxford 3000 and Oxford 5000 core-list absence check",
            "url":PDF + (pdfid or "3000") + "_by_CEFR_level.pdf",
            "observed_on":"2026-10-31",
            "pdf_page":page,"extracted_line":line,"source_excerpt":excerpt,
            "source_cefr_level":level,
            "evidence_scope":"DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE" if pdfid
                    else "NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL",
            "access":"DIRECT_OFFICIAL_PDF_WEB_TEXT",
        }
        if pdfid is None:
            expected_pub["additional_inspected_url"] = PDF + "5000_by_CEFR_level.pdf"
        require(p == expected_pub, "Forged Oxford word/POS, URL, page, line or excerpt: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "Fabricated reviewer signoff: " + word)
        require(isinstance(row.get("editorial_risk"), str)
                and len(row["editorial_risk"]) >= 50
                and "Independent human reviewer" in row.get("independent_reviewer_task", ""),
                "Missing exact-sense review risk: " + word)
        if word in SENSES:
            d = row.get("dictionary_sense_lead")
            url, sense = SENSES[word]
            require(isinstance(d, dict) and d.get("url") == url
                    and d.get("sense_number") == sense
                    and d.get("observed_on") == "2026-10-31"
                    and d.get("access") == "DIRECT_OFFICIAL_PUBLISHER_DICTIONARY_WEB_TEXT"
                    and d.get("evidence_scope") ==
                        "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and len(d.get("sense_summary", "")) >= 60,
                    "Dictionary exact-sense lead altered: " + word)
            candidate = row.get("editorial_rewrite_candidate")
            require(isinstance(candidate, dict)
                    and candidate.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and len(candidate.get("myanmar_meaning", "")) >= 15
                    and len(candidate.get("original_example", "")) >= 25,
                    "Unapproved Myanmar/example proposal altered: " + word)
        else:
            require("dictionary_sense_lead" not in row
                    and "editorial_rewrite_candidate" not in row,
                    "Fabricated dictionary sense lead: " + word)
    return True

def mutations(packet, shortlist):
    n = 0
    for i in range(10):
        for field, bad in (
            ("word","fakeword"),("level","C1"),("part_of_speech","adverb"),
            ("editorial_hold",False),("independently_reviewed",True),
            ("release_approved",True),("independent_reviewer_receipt",{"name":"fake"}),
            ("editorial_risk",""),("independent_reviewer_task",""),
        ):
            altered = copy.deepcopy(packet)
            altered["records"][i][field] = bad
            try:
                validate(altered, shortlist)
            except ValueError:
                n += 1
            else:
                raise AssertionError("Forged " + field + " accepted for " + str(i))
        for group, field, bad in (
            ("shortlist_snapshot","myanmar_meaning","အတည်ပြုပြီး"),
            ("shortlist_snapshot","example_sentence","False example."),
            ("shortlist_provenance","source_index",0),
            ("publisher_source","source_cefr_level","C2"),
            ("publisher_source","pdf_page",999),
            ("publisher_source","extracted_line",0),
            ("publisher_source","source_excerpt","forged n."),
            ("publisher_source","url","https://example.com/forged.pdf"),
        ):
            altered = copy.deepcopy(packet)
            altered["records"][i][group][field] = bad
            try:
                validate(altered, shortlist)
            except ValueError:
                n += 1
            else:
                raise AssertionError("Forged " + group + "." + field + " accepted")
    for word in SENSES:
        i = next(i for i, x in enumerate(packet["records"]) if x["word"] == word)
        for group, field, bad in (
            ("dictionary_sense_lead","url","https://example.com"),
            ("dictionary_sense_lead","sense_number",999),
            ("dictionary_sense_lead","access","HUMAN_VERIFIED"),
            ("editorial_rewrite_candidate","review_status","APPROVED"),
        ):
            altered = copy.deepcopy(packet)
            altered["records"][i][group][field] = bad
            try:
                validate(altered, shortlist)
            except ValueError:
                n += 1
            else:
                raise AssertionError("Forged sense/proposal accepted")
    for key, bad in (("independently_approved_count",1),
                     ("record_count",11),("word_pos_discrepancies",0),
                     ("direct_dictionary_sense_leads",0)):
        altered = copy.deepcopy(packet)
        altered[key] = bad
        try:
            validate(altered, shortlist)
        except ValueError:
            n += 1
        else:
            raise AssertionError("Forged packet count accepted")
    return n

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    validate(packet, shortlist)
    if args.self_test:
        n = mutations(packet, shortlist)
        print("PASS: %d/%d forged Oxford, Myanmar, provenance, sense and signoff mutations rejected" % (n, n))
    print("PASS: B2 final ten source observations (nine word/POS, one core-list unlisted); "
          "five direct sense leads; 0 independent approvals; release BLOCKED / STAGING ONLY; lane=" + args.level)

if __name__ == "__main__":
    main()
