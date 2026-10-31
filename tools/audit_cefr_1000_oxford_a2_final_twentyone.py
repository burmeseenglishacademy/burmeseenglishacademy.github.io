#!/usr/bin/env python3
"""Source-bound final 21 A2 Oxford core-list triage; STAGING ONLY.

Twenty ABSENCES from two publisher core lists are not CEFR labels. One B2
publisher word/POS label is not independent exact-sense approval. This auditor
cannot authenticate independent human reviews or real listening/device QA.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = "draft/CEFR-1000-OXFORD-A2-FINAL-TWENTY-ONE-COMPOUNDS-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
PACKET_BLOB = "fd78e2260de00a716621ec5cda21fefe497b6377"
SHORTLIST_PATH = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
WORDS = ("raincoat", "lunchbox", "toothache", "sunscreen", "shoelace",
         "bookshelf", "doormat", "shoebox", "saucepan", "washcloth",
         "postcard", "sunflower", "dustbin", "bathrobe", "snowman",
         "hairbrush", "toothbrush", "crossroads", "wheelbarrow",
         "greenhouse", "backseat")
DICTIONARY = {
    "raincoat": ("https://www.oxfordlearnersdictionaries.com/definition/english/raincoat", "88-104"),
    "washcloth": ("https://www.oxfordlearnersdictionaries.com/definition/english/washcloth", "88-111"),
    "crossroads": ("https://www.oxfordlearnersdictionaries.com/definition/english/crossroads", "88-123"),
    "greenhouse": ("https://www.oxfordlearnersdictionaries.com/definition/english/greenhouse", "88-109"),
}
REWRITES = {"washcloth", "wheelbarrow", "crossroads", "greenhouse", "bookshelf"}
PDF3000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
SOURCE_BLOBS = {
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json": "da7df62123acfac89a0acedad4652ec499c7ed3d",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json": "228c772697e4879f6b8a30f85709d188a1df266c",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json": "96d54ddb6fdc204e8cbea45e8c97a6c98fb17b11",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json": "6a10ae41eb41370a9a5b74d907fa395bb43e18d8",
}
FIELDS = ("english_definition", "burmese_meaning", "example_sentence")
NO_APPROVAL = ("independently_reviewed", "release_approved")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def blob_sha(path):
    data = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load():
    require(blob_sha(PATH) == PACKET_BLOB, "Pinned publisher research packet changed")
    require(blob_sha(SHORTLIST_PATH) == SHORTLIST_BLOB, "Frozen 1,000 shortlist changed")
    for path, expected in SOURCE_BLOBS.items():
        require(blob_sha(path) == expected, "Historical source Git blob drift: " + path)
    return read(PATH), read(SHORTLIST_PATH), {p: read(p) for p in SOURCE_BLOBS}


def audit(packet, shortlist, historical):
    require(packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("shortlist_blob_sha") == SHORTLIST_BLOB
            and packet.get("observed_on") == "2026-10-31", "Scope, date or shortlist provenance drift")
    require(packet.get("record_count") == 21
            and packet.get("counts_by_level") == {"A1": 0, "A2": 21, "B1": 0, "B2": 0, "C1": 0}
            and packet.get("publisher_reference_level_counts") == {
                "A1": 0, "A2": 0, "B1": 0, "B2": 1, "C1": 0, "UNLISTED": 20}
            and packet.get("word_pos_discrepancies") == 1
            and packet.get("direct_dictionary_sense_leads") == 4
            and packet.get("independently_approved_count") == 0, "Packet counts or false approval")
    require(packet.get("status") == "A2_FINAL_TWENTY_ONE_CORE_LIST_TRIAGE_TWENTY_UNLISTED_ONE_B2_FOUR_DIRECT_DICTIONARY_SENSE_LEADS_ALL_UNAPPROVED", "Release status drift")
    rows = packet.get("records")
    require(isinstance(rows, list) and len(rows) == 21
            and tuple(r.get("word") for r in rows if isinstance(r, dict)) == WORDS,
            "Wrong words, order or duplicate publisher observations")
    entries = shortlist.get("entries")
    require(shortlist.get("counts_by_level") == {l: 200 for l in ("A1", "A2", "B1", "B2", "C1")}
            and shortlist.get("independently_approved_by_level") == {l: 0 for l in ("A1", "A2", "B1", "B2", "C1")}
            and isinstance(entries, list) and len(entries) == 1000, "Frozen shortlist count or approval drift")
    by_word = {r["word"]: r for r in entries}
    require(len(by_word) == 1000, "Shortlist duplicate")
    for row in rows:
        word = row["word"]
        original = by_word[word]
        require(original["level"] == row.get("level") == "A2"
                and original["part_of_speech"] == row.get("part_of_speech") == "noun",
                word + ": draft level/POS drift")
        require(row.get("shortlist_snapshot") == {k: original[k] for k in FIELDS},
                word + ": altered original English, Myanmar or example")
        provenance = {k: original[k] for k in ("source_path", "source_index", "source_blob_sha")}
        require(row.get("shortlist_provenance") == provenance, word + ": source provenance drift")
        path, index = provenance["source_path"], provenance["source_index"]
        require(path in SOURCE_BLOBS and provenance["source_blob_sha"] == SOURCE_BLOBS[path]
                and type(index) is int and 0 <= index < len(historical[path]["entries"]),
                word + ": wrong historical blob or index")
        actual = historical[path]["entries"][index]
        require(actual["word"] == word and actual["part_of_speech"] == "noun"
                and actual["proposed_level"] == "A2"
                and all(actual[k] == original[k] for k in FIELDS),
                word + ": historical source does not match frozen shortlist")
        require(row.get("editorial_hold") is True
                and row.get("independent_reviewer_receipt") is None
                and all(row.get(k) is False for k in NO_APPROVAL)
                and isinstance(row.get("editorial_risk"), str)
                and len(row["editorial_risk"]) > 30
                and "Independent human reviewer" in row.get("independent_reviewer_task", ""),
                word + ": editorial hold or genuine human review requirement missing")
        pub = row.get("publisher_source")
        require(isinstance(pub, dict)
                and pub.get("publisher") == "Oxford University Press"
                and pub.get("observed_on") == "2026-10-31"
                and pub.get("access") == "DIRECT_OFFICIAL_PDF_WEB_TEXT",
                word + ": publisher identity/date/access drift")
        if word == "greenhouse":
            require(pub.get("url") == PDF5000
                    and pub.get("source_cefr_level") == "B2"
                    and pub.get("pdf_page") == 2
                    and pub.get("extracted_line") == 292
                    and pub.get("source_excerpt") == "greenhouse n."
                    and pub.get("evidence_scope") == "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"
                    and "additional_inspected_url" not in pub,
                    "Greenhouse B2 source word/POS line forged")
        else:
            require(pub.get("url") == PDF3000
                    and pub.get("additional_inspected_url") == PDF5000
                    and pub.get("source_cefr_level") is None
                    and pub.get("pdf_page") is None
                    and pub.get("extracted_line") is None
                    and pub.get("source_excerpt") is None
                    and pub.get("evidence_scope") == "NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL",
                    word + ": core-list absence falsely treated as a CEFR label")
        lead = row.get("dictionary_sense_lead")
        if word in DICTIONARY:
            url, lines = DICTIONARY[word]
            require(isinstance(lead, dict) and lead.get("url") == url
                    and lead.get("page_lines") == lines
                    and lead.get("observed_on") == "2026-10-31"
                    and lead.get("access") == "DIRECT_OFFICIAL_PUBLISHER_DICTIONARY_WEB_TEXT"
                    and lead.get("evidence_scope") == "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and isinstance(lead.get("sense_summary"), str)
                    and len(lead["sense_summary"]) > 50,
                    word + ": publisher dictionary sense lead forged")
        else:
            require(lead is None, word + ": unobserved dictionary source invented")
        candidate = row.get("editorial_rewrite_candidate")
        if word in REWRITES:
            require(isinstance(candidate, dict)
                    and candidate.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and all(isinstance(candidate.get(k), str) and candidate[k].strip()
                            for k in ("myanmar_meaning", "original_example")),
                    word + ": rewrite improperly approved or removed")
        else:
            require(candidate is None, word + ": invented approved rewrite")
    return {"A2_observed": 21, "Oxford_core_list_absent": 20,
            "Oxford_B2_word_pos": 1, "direct_dictionary_sense_leads": 4,
            "independent_approvals": 0, "release": "BLOCKED_STAGING_ONLY"}


def self_test(packet, shortlist, historical):
    cases = []
    def change(label, fn):
        altered = copy.deepcopy(packet)
        fn(altered)
        try:
            audit(altered, shortlist, historical)
        except (ValueError, KeyError, TypeError, IndexError):
            return
        raise AssertionError("Forged evidence accepted: " + label)
    for i, word in enumerate(WORDS):
        change(word + ": false A2 publisher level",
               lambda x, i=i: x["records"][i]["publisher_source"].update(source_cefr_level="A2"))
        change(word + ": false PDF locator",
               lambda x, i=i: x["records"][i]["publisher_source"].update(pdf_page=99))
        change(word + ": false source excerpt",
               lambda x, i=i: x["records"][i]["publisher_source"].update(source_excerpt="invented n."))
        change(word + ": false source URL",
               lambda x, i=i: x["records"][i]["publisher_source"].update(url="https://example.org/fake.pdf"))
        change(word + ": forged English definition",
               lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(english_definition="forged"))
        change(word + ": forged Myanmar meaning",
               lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(myanmar_meaning="အတည်ပြု"))
        change(word + ": forged example",
               lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(example_sentence="forged"))
        change(word + ": forged source index",
               lambda x, i=i: x["records"][i]["shortlist_provenance"].update(source_index=999))
        change(word + ": false approval",
               lambda x, i=i: x["records"][i].update(release_approved=True))
        change(word + ": false independent review",
               lambda x, i=i: x["records"][i].update(independently_reviewed=True))
        change(word + ": fabricated human receipt",
               lambda x, i=i: x["records"][i].update(independent_reviewer_receipt={"reviewer": "fake"}))
        change(word + ": missing editorial risk",
               lambda x, i=i: x["records"][i].update(editorial_risk=""))
        cases.extend(range(12))
    for key, value in (("record_count", 20), ("independently_approved_count", 1),
                       ("word_pos_discrepancies", 0), ("direct_dictionary_sense_leads", 5)):
        change("forged packet " + key, lambda x, k=key, v=value: x.update({k: v}))
        cases.append(1)
    for word in DICTIONARY:
        i = WORDS.index(word)
        change(word + ": forged dictionary URL",
               lambda x, i=i: x["records"][i]["dictionary_sense_lead"].update(url="https://example.org/fake"))
        cases.append(1)
    for word in REWRITES:
        i = WORDS.index(word)
        change(word + ": fake approved rewrite",
               lambda x, i=i: x["records"][i]["editorial_rewrite_candidate"].update(review_status="APPROVED"))
        cases.append(1)
    return len(cases)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=("A1", "A2", "B1", "B2", "C1", "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet, shortlist, historical = load()
    result = audit(packet, shortlist, historical)
    if args.self_test:
        n = self_test(packet, shortlist, historical)
        print("PASS: %d/%d false Oxford, bilingual, historical source and review mutations rejected" % (n, n))
    print(json.dumps({"lane": args.level, **result}, sort_keys=True))


if __name__ == "__main__":
    main()
