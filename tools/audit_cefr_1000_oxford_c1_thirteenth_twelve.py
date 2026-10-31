#!/usr/bin/env python3
"""Fail-closed staging audit for twelve C1 Oxford research leads (2026-11-01).

Publisher PDF absence is not a CEFR label. The veteran NOUN entry does not
classify the draft ADJECTIVE. No automated review or audio/device signoff.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = "draft/CEFR-1000-OXFORD-C1-THIRTEENTH-TWELVE-AND-FIVE-DIRECT-SENSE-LEADS-2026-11-01.json"
PACKET_BLOB = "934edb9f9884487a81135a6363d178d263a53dae"
SHORTLIST = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
SOURCES = {
    "draft/A2-C1-EDITORIAL-STARTER.json": "b04dd85db5cfae131c25aa4c73109778991b6fdc",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json": "7eaf88b9ed7687b26ccde713262f10fb209743a8",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json": "da7df62123acfac89a0acedad4652ec499c7ed3d",
}
WORDS = ("naval", "noble", "treasury", "ethics", "manufacturer", "veteran",
         "legally", "census", "destiny", "mitigate", "disproportionate", "perpetuate")
DICT = {
    "naval": ("https://www.oxfordlearnersdictionaries.com/definition/english/naval", "88-110"),
    "ethics": ("https://www.oxfordlearnersdictionaries.com/definition/english/ethic", "88-125"),
    "manufacturer": ("https://www.oxfordlearnersdictionaries.com/definition/english/manufacturer", "88-115"),
    "census": ("https://www.oxfordlearnersdictionaries.com/definition/english/census", "88-132"),
    "mitigate": ("https://www.oxfordlearnersdictionaries.com/definition/english/mitigate", "88-122"),
}
PROPOSALS = {"ethics", "manufacturer", "veteran", "census", "mitigate"}
PDF3 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
DATE = "2026-11-01"
STATUS = "C1_THIRTEENTH_TWELVE_ONE_C1_WORD_POS_ELEVEN_CORE_LIST_UNLISTED_FIVE_DICTIONARY_LEADS_ALL_HELD"
SNAP = ("english_definition", "burmese_meaning", "example_sentence")

def require(test, message):
    if not test:
        raise ValueError(message)

def blob_sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\\0" + raw).hexdigest()

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf8"))

def load():
    require(blob_sha(PATH) == PACKET_BLOB, "Immutable research packet Git blob changed")
    require(blob_sha(SHORTLIST) == SHORTLIST_BLOB, "Frozen shortlist Git blob changed")
    for path, sha in SOURCES.items():
        require(blob_sha(path) == sha, "Historical source Git blob changed: " + path)
    return read(PATH), read(SHORTLIST), {p: read(p) for p in SOURCES}

def audit(packet, shortlist, historical):
    require(packet.get("schema") == 1
            and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == STATUS and packet.get("observed_on") == DATE
            and packet.get("shortlist_blob_sha") == SHORTLIST_BLOB,
            "Scope, date, or frozen-source binding changed")
    require(packet.get("record_count") == 12
            and packet.get("counts_by_level") == {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 12}
            and packet.get("publisher_reference_level_counts") ==
                {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 1, "UNLISTED": 11}
            and packet.get("word_pos_discrepancies") == 0
            and packet.get("part_of_speech_mismatch_leads") == 1
            and packet.get("direct_dictionary_sense_leads") == 5,
            "Oxford publisher/part-of-speech/source counts changed")
    require(packet.get("independently_approved_count") == 0
            and packet.get("independent_human_review_receipts") == []
            and packet.get("audio_real_listening_signoffs") == []
            and packet.get("release_approved") is False,
            "Invented independent human approval or listening evidence")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000
            and shortlist.get("counts_by_level") == {x: 200 for x in ("A1","A2","B1","B2","C1")}
            and shortlist.get("independently_approved_by_level") == {x: 0 for x in ("A1","A2","B1","B2","C1")},
            "Provisional 200-per-level scope or approvals drifted")
    by_word = {x["word"]: x for x in entries}
    require(len(by_word) == 1000, "Duplicate shortlist headwords")
    rows = packet.get("records")
    require(isinstance(rows, list) and len(rows) == 12
            and tuple(x.get("word") for x in rows) == WORDS,
            "Wrong C1 words, order or duplicates")
    for row in rows:
        word = row["word"]
        source = by_word[word]
        require(source["level"] == row.get("level") == "C1"
                and source["part_of_speech"] == row.get("part_of_speech"),
                "Draft level/POS altered: " + word)
        require(row.get("shortlist_snapshot") == {
                    "english_definition": source["english_definition"],
                    "myanmar_meaning": source["burmese_meaning"],
                    "example_sentence": source["example_sentence"]},
                "Frozen English/Myanmar/example changed: " + word)
        provenance = {k: source[k] for k in ("source_path","source_index","source_blob_sha")}
        require(row.get("shortlist_provenance") == provenance
                and provenance["source_path"] in SOURCES
                and provenance["source_blob_sha"] == SOURCES[provenance["source_path"]],
                "Historical provenance altered: " + word)
        hist = historical[provenance["source_path"]]["entries"]
        i = provenance["source_index"]
        require(type(i) is int and 0 <= i < len(hist), "Historical index invalid: " + word)
        old = hist[i]
        require(old.get("word") == word
                and old.get("part_of_speech") == source["part_of_speech"]
                and old.get("level", old.get("proposed_level")) == "C1"
                and all(old[k] == source[k] for k in SNAP),
                "Historical Git row does not match frozen shortlist: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None
                and "independent HUMAN" in row.get("independent_reviewer_task","")
                and len(row.get("editorial_risk","")) > 65,
                "False approval or insufficient exact-sense risk: " + word)
        pub = row.get("publisher_source")
        common = {"publisher": "Oxford University Press", "observed_on": DATE,
                  "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"}
        if word == "mitigate":
            expected = {**common, "title": "The Oxford 5000 by CEFR level",
                        "url": PDF5, "pdf_page": 6, "extracted_line": 1488,
                        "source_excerpt": "mitigate v.", "source_cefr_level": "C1",
                        "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"}
        else:
            expected = {**common, "title": "The Oxford 3000 and Oxford 5000 by CEFR level (both inspected)",
                        "url": PDF3, "additional_inspected_url": PDF5,
                        "pdf_page": None, "extracted_line": None,
                        "source_excerpt": None, "source_cefr_level": None,
                        "evidence_scope": "NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL"}
        require(pub == expected, "Forged Oxford PDF word/POS or absence observation: " + word)
        lead = row.get("dictionary_sense_lead")
        if word in DICT:
            url, lines = DICT[word]
            require(isinstance(lead, dict) and lead.get("url") == url
                    and lead.get("page_lines") == lines
                    and lead.get("sense_number") == 1
                    and lead.get("observed_on") == DATE
                    and lead.get("access") == "DIRECT_OFFICIAL_PUBLISHER_DICTIONARY_WEB_TEXT"
                    and lead.get("evidence_scope") == "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and len(lead.get("sense_summary","")) > 75,
                    "Forged Oxford dictionary sense lead: " + word)
        else:
            require(lead is None, "Invented dictionary page access: " + word)
        proposal = row.get("editorial_rewrite_candidate")
        if word in PROPOSALS:
            require(isinstance(proposal, dict)
                    and proposal.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and any("\\u1000" <= ch <= "\\u109f" for ch in proposal.get("myanmar_meaning",""))
                    and len(proposal.get("original_example","")) > 35,
                    "Forged approval or missing Myanmar/example candidate: " + word)
        else:
            require(proposal is None, "Invented rewrite candidate: " + word)
    return {"new_C1_observations": 12, "publisher_C1_word_POS": 1,
            "unlisted_not_a_cefr_level": 11, "POS_mismatch_leads": 1,
            "direct_dictionary_sense_leads": 5, "human_approvals": 0,
            "release": "BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist, historical):
    passed = 0
    def reject(label, fn):
        nonlocal passed
        changed = copy.deepcopy(packet)
        fn(changed)
        try:
            audit(changed, shortlist, historical)
        except (ValueError, KeyError, TypeError, IndexError):
            passed += 1
            return
        raise AssertionError("Forged publisher/bilingual approval accepted: " + label)
    for i, word in enumerate(WORDS):
        cases = (
            ("level", lambda r: r.update(level="B2")),
            ("English", lambda r: r["shortlist_snapshot"].update(english_definition="fake")),
            ("Myanmar", lambda r: r["shortlist_snapshot"].update(myanmar_meaning="အတု")),
            ("example", lambda r: r["shortlist_snapshot"].update(example_sentence="fake")),
            ("historical index", lambda r: r["shortlist_provenance"].update(source_index=9999)),
            ("publisher level", lambda r: r["publisher_source"].update(source_cefr_level="B2")),
            ("publisher line", lambda r: r["publisher_source"].update(extracted_line=9999)),
            ("publisher URL", lambda r: r["publisher_source"].update(url="https://example.org/fake.pdf")),
            ("publisher excerpt", lambda r: r["publisher_source"].update(source_excerpt="fake")),
            ("publisher scope", lambda r: r["publisher_source"].update(evidence_scope="APPROVED_EXACT_SENSE")),
            ("approval", lambda r: r.update(release_approved=True)),
            ("independent review", lambda r: r.update(independently_reviewed=True)),
            ("human receipt", lambda r: r.update(independent_reviewer_receipt={"reviewer":"fake"})),
            ("editorial hold", lambda r: r.update(editorial_hold=False)),
        )
        for label, fn in cases:
            reject(word + " " + label, lambda p, i=i, fn=fn: fn(p["records"][i]))
    for word in DICT:
        i = WORDS.index(word)
        reject(word + " dictionary URL", lambda p,i=i: p["records"][i]["dictionary_sense_lead"].update(url="https://example.org/fake"))
        reject(word + " dictionary scope", lambda p,i=i: p["records"][i]["dictionary_sense_lead"].update(evidence_scope="INDEPENDENT_APPROVED"))
    for word in PROPOSALS:
        i = WORDS.index(word)
        reject(word + " proposal approved", lambda p,i=i: p["records"][i]["editorial_rewrite_candidate"].update(review_status="APPROVED"))
    for key,value in (("record_count",11),("independently_approved_count",1),
                      ("direct_dictionary_sense_leads",6),("part_of_speech_mismatch_leads",0),
                      ("release_approved",True)):
        reject("packet " + key, lambda p,key=key,value=value: p.update({key:value}))
    return passed

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=("A1","A2","B1","B2","C1","ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    packet, shortlist, historical = load()
    result = audit(packet, shortlist, historical)
    if args.self_test:
        n = self_test(packet, shortlist, historical)
        print("PASS: %d/%d forged source, bilingual, provenance and false approval mutations rejected" % (n,n))
    print(json.dumps({"lane": args.level, **result}, sort_keys=True))

if __name__ == "__main__":
    main()
