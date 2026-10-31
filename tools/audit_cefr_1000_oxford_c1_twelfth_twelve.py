#!/usr/bin/env python3
"""Source-bound C1 twelfth Oxford 12-word exact-sense triage. STAGING ONLY.

Eleven publisher core-list ABSENCES are not CEFR levels. One B2 word/POS
observation does not prove the intended exact sense. This code cannot perform
independent human review, real listening, iPhone testing, or deployment.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = "draft/CEFR-1000-OXFORD-C1-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
PACKET_BLOB = "111a309369f1f45bade53a4f25880348dc8f5fcf"
SHORTLIST_PATH = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PDF3000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5000 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
WORDS = ("actively", "imperial", "bearing", "repeatedly", "unexpected",
         "advisory", "deference", "delineate", "dichotomy", "disseminate",
         "eclectic", "efficacy")
DICTIONARY = {
    "bearing": ("https://www.oxfordlearnersdictionaries.com/definition/english/bearing", "88-123", 1),
    "delineate": ("https://www.oxfordlearnersdictionaries.com/definition/english/delineate", "88-115", 1),
    "dichotomy": ("https://www.oxfordlearnersdictionaries.com/definition/english/dichotomy", "88-109", 1),
    "efficacy": ("https://www.oxfordlearnersdictionaries.com/definition/english/efficacy", "88-110", 1),
}
SOURCE_BLOBS = {
    "draft/A2-C1-EDITORIAL-STARTER.json": "b04dd85db5cfae131c25aa4c73109778991b6fdc",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json": "7eaf88b9ed7687b26ccde713262f10fb209743a8",
}
FIELDS = ("english_definition", "burmese_meaning", "example_sentence")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def git_blob_sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def load():
    require(git_blob_sha(PATH) == PACKET_BLOB, "Research packet Git blob changed")
    require(git_blob_sha(SHORTLIST_PATH) == SHORTLIST_BLOB, "Frozen shortlist changed")
    for path, sha in SOURCE_BLOBS.items():
        require(git_blob_sha(path) == sha, "Historical Git source blob changed: " + path)
    return read(PATH), read(SHORTLIST_PATH), {p: read(p) for p in SOURCE_BLOBS}


def audit(packet, shortlist, historical):
    require(packet.get("schema") == 1
            and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == "C1_TWELFTH_TWELVE_CORE_LIST_TRIAGE_ELEVEN_UNLISTED_ONE_B2_FOUR_DIRECT_SENSE_LEADS_ALL_UNAPPROVED"
            and packet.get("observed_on") == "2026-10-31"
            and packet.get("shortlist_blob_sha") == SHORTLIST_BLOB,
            "Publisher research scope/date/provenance drift")
    require(packet.get("record_count") == 12
            and packet.get("counts_by_level") == {x: (12 if x == "C1" else 0)
                for x in ("A1", "A2", "B1", "B2", "C1")}
            and packet.get("publisher_reference_level_counts") == {
                "A1": 0, "A2": 0, "B1": 0, "B2": 1, "C1": 0, "UNLISTED": 11}
            and packet.get("word_pos_discrepancies") == 1
            and packet.get("direct_dictionary_sense_leads") == 4,
            "Research count or publisher-level drift")
    require(packet.get("independently_approved_count") == 0
            and packet.get("independent_human_review_receipts") == []
            and packet.get("audio_real_listening_signoffs") == []
            and packet.get("release_approved") is False,
            "Fabricated human approval or real listening")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000
            and shortlist.get("counts_by_level") == {
                x: 200 for x in ("A1", "A2", "B1", "B2", "C1")}
            and shortlist.get("independently_approved_by_level") == {
                x: 0 for x in ("A1", "A2", "B1", "B2", "C1")},
            "Frozen 200-per-level shortlist or independent approval drift")
    by_word = {r["word"]: r for r in entries}
    require(len(by_word) == 1000, "Shortlist duplicates")
    rows = packet.get("records")
    require(isinstance(rows, list) and len(rows) == 12
            and tuple(r.get("word") for r in rows if isinstance(r, dict)) == WORDS,
            "Wrong research words/order or duplicate rows")
    for row in rows:
        word = row["word"]
        original = by_word[word]
        require(original["level"] == row.get("level") == "C1"
                and original["part_of_speech"] == row.get("part_of_speech"),
                "Frozen draft level/POS drift: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": original["english_definition"],
            "myanmar_meaning": original["burmese_meaning"],
            "example_sentence": original["example_sentence"]},
            "Original English/Myanmar/example altered: " + word)
        provenance = {k: original[k] for k in
                      ("source_path", "source_index", "source_blob_sha")}
        require(row.get("shortlist_provenance") == provenance
                and provenance["source_path"] in SOURCE_BLOBS
                and provenance["source_blob_sha"] == SOURCE_BLOBS[provenance["source_path"]],
                "Historical Git provenance forged: " + word)
        path, index = provenance["source_path"], provenance["source_index"]
        source_rows = historical[path]["entries"]
        require(type(index) is int and 0 <= index < len(source_rows),
                "Historical source index invalid: " + word)
        prior = source_rows[index]
        require(prior.get("word") == word
                and prior.get("part_of_speech") == original["part_of_speech"]
                and prior.get("level", prior.get("proposed_level")) == "C1"
                and all(prior[k] == original[k] for k in FIELDS),
                "Historical source row does not match shortlist: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None
                and "Independent human reviewer" in row.get("independent_reviewer_task", "")
                and isinstance(row.get("editorial_risk"), str)
                and len(row["editorial_risk"]) >= 60,
                "False human approval or insufficient sense risk: " + word)
        pub = row.get("publisher_source")
        require(isinstance(pub, dict)
                and pub.get("publisher") == "Oxford University Press"
                and pub.get("observed_on") == "2026-10-31"
                and pub.get("access") == "DIRECT_OFFICIAL_PDF_WEB_TEXT",
                "Publisher identity/date/access forged: " + word)
        if word == "unexpected":
            require(pub == {
                "publisher": "Oxford University Press",
                "title": "The Oxford 3000 by CEFR level",
                "url": PDF3000, "observed_on": "2026-10-31",
                "pdf_page": 12, "extracted_line": 3274,
                "source_excerpt": "unexpected adj.",
                "source_cefr_level": "B2",
                "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Oxford B2 unexpected adjective locator forged")
        else:
            require(pub == {
                "publisher": "Oxford University Press",
                "title": "The Oxford 3000 and Oxford 5000 by CEFR level (both inspected)",
                "url": PDF3000, "additional_inspected_url": PDF5000,
                "observed_on": "2026-10-31",
                "pdf_page": None, "extracted_line": None,
                "source_excerpt": None, "source_cefr_level": None,
                "evidence_scope": "NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL",
                "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"},
                "Oxford core-list absence falsely promoted to a CEFR label: " + word)
        lead = row.get("dictionary_sense_lead")
        if word in DICTIONARY:
            url, lines, sense = DICTIONARY[word]
            require(isinstance(lead, dict)
                    and lead.get("url") == url
                    and lead.get("page_lines") == lines
                    and lead.get("sense_number") == sense
                    and lead.get("observed_on") == "2026-10-31"
                    and lead.get("access") == "DIRECT_OFFICIAL_PUBLISHER_DICTIONARY_WEB_TEXT"
                    and lead.get("evidence_scope") == "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and isinstance(lead.get("sense_summary"), str)
                    and len(lead["sense_summary"]) > 75,
                    "Direct dictionary sense evidence forged: " + word)
            proposal = row.get("editorial_rewrite_candidate")
            require(isinstance(proposal, dict)
                    and proposal.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and isinstance(proposal.get("myanmar_meaning"), str)
                    and any("\u1000" <= ch <= "\u109f" for ch in proposal["myanmar_meaning"])
                    and isinstance(proposal.get("original_example"), str)
                    and len(proposal["original_example"]) > 35,
                    "Unapproved Myanmar/example proposal removed or falsely approved: " + word)
        else:
            require(lead is None and row.get("editorial_rewrite_candidate") is None,
                    "Unobserved dictionary source or approved rewrite invented: " + word)
    return {"C1_new_observations": 12, "unlisted_not_a_cefr_level": 11,
            "publisher_B2_word_pos": 1, "direct_dictionary_sense_leads": 4,
            "independent_approvals": 0, "release": "BLOCKED_STAGING_ONLY"}


def self_test(packet, shortlist, historical):
    count = 0
    def reject(label, change):
        nonlocal count
        altered = copy.deepcopy(packet)
        change(altered)
        try:
            audit(altered, shortlist, historical)
        except (ValueError, KeyError, TypeError, IndexError):
            count += 1
            return
        raise AssertionError("Forged source/approval accepted: " + label)
    for i, word in enumerate(WORDS):
        reject(word + ": invented C1 level",
               lambda x, i=i: x["records"][i]["publisher_source"].update(source_cefr_level="C1"))
        reject(word + ": invented PDF page",
               lambda x, i=i: x["records"][i]["publisher_source"].update(pdf_page=77))
        reject(word + ": invented excerpt",
               lambda x, i=i: x["records"][i]["publisher_source"].update(source_excerpt="fabricated"))
        reject(word + ": forged publisher URL",
               lambda x, i=i: x["records"][i]["publisher_source"].update(url="https://example.org/fake.pdf"))
        reject(word + ": forged Oxford scope",
               lambda x, i=i: x["records"][i]["publisher_source"].update(evidence_scope="EXACT_SENSE_APPROVED"))
        reject(word + ": forged English",
               lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(english_definition="forged"))
        reject(word + ": forged Myanmar",
               lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(myanmar_meaning="အတု"))
        reject(word + ": forged example",
               lambda x, i=i: x["records"][i]["shortlist_snapshot"].update(example_sentence="forged"))
        reject(word + ": forged historical source",
               lambda x, i=i: x["records"][i]["shortlist_provenance"].update(source_index=999))
        reject(word + ": false approval",
               lambda x, i=i: x["records"][i].update(release_approved=True))
        reject(word + ": fake human receipt",
               lambda x, i=i: x["records"][i].update(independent_reviewer_receipt={"reviewer": "fake"}))
        reject(word + ": false independent review",
               lambda x, i=i: x["records"][i].update(independently_reviewed=True))
        reject(word + ": missing editorial risk",
               lambda x, i=i: x["records"][i].update(editorial_risk=""))
    for word in DICTIONARY:
        i = WORDS.index(word)
        reject(word + ": false dictionary URL",
               lambda x, i=i: x["records"][i]["dictionary_sense_lead"].update(url="https://example.org/fake"))
        reject(word + ": false dictionary sense",
               lambda x, i=i: x["records"][i]["dictionary_sense_lead"].update(sense_number=9))
        reject(word + ": false bilingual approval",
               lambda x, i=i: x["records"][i]["editorial_rewrite_candidate"].update(review_status="APPROVED"))
    for k,v in (("record_count",11),("word_pos_discrepancies",0),
                ("direct_dictionary_sense_leads",5),("independently_approved_count",1),
                ("release_approved",True)):
        reject("packet " + k, lambda x,k=k,v=v: x.update({k:v}))
    return count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=("A1","A2","B1","B2","C1","ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet, shortlist, historical = load()
    report = audit(packet, shortlist, historical)
    if args.self_test:
        n = self_test(packet, shortlist, historical)
        print("PASS: %d/%d forged Oxford, Myanmar, source and review mutations rejected" % (n,n))
    print(json.dumps({"lane": args.level, **report}, sort_keys=True))


if __name__ == "__main__":
    main()
