#!/usr/bin/env python3
"""Fail-closed C1 sixteenth source-bound research audit. Never approves or deploys."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = "draft/CEFR-1000-OXFORD-C1-SIXTEENTH-TWELVE-AND-EIGHT-DIRECT-SENSE-LEADS-2026-11-01.json"
PACKET_SHA = "8ec9c6725ea2b7b1399957907b08819061415960"
SHORTLIST = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
HISTORICAL = {
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json": "7eaf88b9ed7687b26ccde713262f10fb209743a8",
    "draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json": "da7df62123acfac89a0acedad4652ec499c7ed3d",
}
WORDS = ("meticulous", "nuanced", "pragmatic", "scrutinize", "stringent",
         "tenacious", "ubiquitous", "vindicate", "vilify", "whimsical",
         "acquiescence", "ameliorate")
DICTIONARY = {"meticulous", "nuanced", "pragmatic", "scrutinize",
              "vindicate", "whimsical", "acquiescence", "ameliorate"}
PDF3 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
PDF5 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
DATE = "2026-11-01"
STATUS = "C1_SIXTEENTH_TWELVE_ALL_CORE_LIST_UNLISTED_EIGHT_DIRECT_DICTIONARY_SENSE_LEADS_ALL_HELD"
LEVELS = ("A1", "A2", "B1", "B2", "C1")

def require(test, message):
    if not test:
        raise ValueError(message)

def sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load():
    for path, expected in [(PACKET, PACKET_SHA), (SHORTLIST, SHORTLIST_SHA), *HISTORICAL.items()]:
        require(sha(path) == expected, "Immutable Git blob drift: " + path)
    return (json.loads((ROOT / PACKET).read_text(encoding="utf-8")),
            json.loads((ROOT / SHORTLIST).read_text(encoding="utf-8")),
            {p: json.loads((ROOT / p).read_text(encoding="utf-8")) for p in HISTORICAL})

def audit(packet, shortlist, historical, reference):
    require(packet == reference, "Pinned publisher research packet tampered")
    require(packet.get("schema") == 1
            and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == STATUS
            and packet.get("observed_on") == DATE
            and packet.get("shortlist_blob_sha") == SHORTLIST_SHA,
            "Wrong project/date/status/source")
    require(packet.get("record_count") == 12
            and packet.get("counts_by_level") == {l: (12 if l == "C1" else 0) for l in LEVELS}
            and packet.get("publisher_reference_level_counts") ==
                {**{l: 0 for l in LEVELS}, "UNLISTED": 12}
            and packet.get("direct_dictionary_sense_leads") == 8,
            "Incorrect Oxford observations")
    require(packet.get("independently_approved_count") == 0
            and packet.get("independent_human_review_receipts") == []
            and packet.get("audio_real_listening_signoffs") == []
            and packet.get("release_approved") is False,
            "Invented human review, listening or release")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000
            and shortlist.get("counts_by_level") == {l: 200 for l in LEVELS}
            and shortlist.get("independently_approved_by_level") == {l: 0 for l in LEVELS},
            "Shortlist size, quota or human approval drift")
    require(len({e["word"] for e in entries}) == 1000, "Duplicate shortlist words")
    by_word = {e["word"]: e for e in entries}
    records = packet.get("records")
    require(isinstance(records, list) and tuple(r.get("word") for r in records) == WORDS,
            "Wrong research word set/order")
    for row in records:
        word = row["word"]
        entry = by_word[word]
        require(row.get("level") == entry["level"] == "C1"
                and row.get("part_of_speech") == entry["part_of_speech"],
                "Draft CEFR/POS changed: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": entry["english_definition"],
            "myanmar_meaning": entry["burmese_meaning"],
            "example_sentence": entry["example_sentence"]},
            "Frozen bilingual/example changed: " + word)
        prov = {k: entry[k] for k in ("source_path", "source_index", "source_blob_sha")}
        require(row.get("shortlist_provenance") == prov
                and prov["source_path"] in HISTORICAL
                and prov["source_blob_sha"] == HISTORICAL[prov["source_path"]],
                "Git historical source provenance mismatch: " + word)
        idx = prov["source_index"]
        old_entries = historical[prov["source_path"]]["entries"]
        require(type(idx) is int and 0 <= idx < len(old_entries),
                "Historical row index invalid: " + word)
        old = old_entries[idx]
        require(old.get("word") == word
                and old.get("part_of_speech") == entry["part_of_speech"]
                and old.get("proposed_level", old.get("level")) == "C1"
                and all(old.get(k) == entry[k] for k in
                        ("english_definition", "burmese_meaning", "example_sentence")),
                "Historical original content mismatch: " + word)
        require(row.get("publisher_source") == {
            "publisher": "Oxford University Press",
            "title": "The Oxford 3000 and Oxford 5000 by CEFR level (both inspected)",
            "url": PDF3,
            "additional_inspected_url": PDF5,
            "observed_on": DATE,
            "pdf_page": None, "extracted_line": None, "source_excerpt": None,
            "source_cefr_level": None,
            "evidence_scope": "NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"},
            "Forged Oxford CEFR/source/locator: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None
                and "independent HUMAN" in row.get("independent_reviewer_task", "")
                and len(row.get("editorial_risk", "")) >= 65,
                "False independent approval or missing risk: " + word)
        d = row.get("dictionary_sense_lead")
        if word in DICTIONARY:
            require(isinstance(d, dict)
                    and d.get("url") == "https://www.oxfordlearnersdictionaries.com/definition/english/" + word
                    and d.get("observed_on") == DATE
                    and d.get("access") == "DIRECT_OFFICIAL_PUBLISHER_DICTIONARY_WEB_TEXT"
                    and d.get("evidence_scope") == "PUBLISHER_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_APPROVAL"
                    and d.get("sense_number") == 1
                    and len(d.get("sense_summary", "")) > 65
                    and len(d.get("page_lines", "")) >= 5,
                    "Forged dictionary sense lead: " + word)
        else:
            require(d is None, "Unobserved dictionary access fabricated: " + word)
        proposal = row.get("editorial_rewrite_candidate")
        if word in DICTIONARY:
            require(isinstance(proposal, dict)
                    and proposal.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                    and all(len(proposal.get(k, "")) >= 20 for k in
                            ("english_definition", "myanmar_meaning", "example_sentence")),
                    "Unapproved bilingual proposal missing/altered: " + word)
        else:
            require(proposal is None, "Unobserved rewrite fabricated: " + word)
    return {"C1": {"first_pass_written": 200, "independently_approved": 0,
                   "new_core_list_absence_observations": 12,
                   "new_direct_dictionary_sense_leads": 8},
            "release": "BLOCKED_STAGING_ONLY"}

def self_test(packet, shortlist, historical):
    cases = []
    for i, word in enumerate(WORDS):
        for label, change in [
            ("word", lambda r: r.update(word="forged")),
            ("pos", lambda r: r.update(part_of_speech="adverb")),
            ("english", lambda r: r["shortlist_snapshot"].update(english_definition="forged")),
            ("myanmar", lambda r: r["shortlist_snapshot"].update(myanmar_meaning="forged")),
            ("example", lambda r: r["shortlist_snapshot"].update(example_sentence="forged")),
            ("history-index", lambda r: r["shortlist_provenance"].update(source_index=999)),
            ("history-sha", lambda r: r["shortlist_provenance"].update(source_blob_sha="0"*40)),
            ("source", lambda r: r["publisher_source"].update(url="https://example.invalid/")),
            ("cefr", lambda r: r["publisher_source"].update(source_cefr_level="C1")),
            ("pdf-page", lambda r: r["publisher_source"].update(pdf_page=1)),
            ("pdf-quote", lambda r: r["publisher_source"].update(source_excerpt="fake")),
            ("risk", lambda r: r.update(editorial_risk="")),
            ("approval", lambda r: r.update(release_approved=True)),
            ("review", lambda r: r.update(independently_reviewed=True)),
            ("receipt", lambda r: r.update(independent_reviewer_receipt={"fake": True})),
            ("dictionary", lambda r: r.update(dictionary_sense_lead={"fake": True})),
            ("rewrite", lambda r: r.update(editorial_rewrite_candidate={"fake": True})),
        ]:
            cases.append((i, label, change))
    for i, label, change in cases:
        mutant = copy.deepcopy(packet)
        change(mutant["records"][i])
        try:
            audit(mutant, shortlist, historical, packet)
        except ValueError:
            continue
        raise AssertionError("Forged " + label + " passed for " + WORDS[i])
    for label, change in [
        ("fake-approval", lambda p: p.update(independently_approved_count=1)),
        ("fake-audio", lambda p: p.update(audio_real_listening_signoffs=[{"fake": True}])),
        ("fake-release", lambda p: p.update(release_approved=True)),
        ("fake-count", lambda p: p.update(record_count=11)),
        ("fake-date", lambda p: p.update(observed_on="2026-10-31")),
        ("fake-dictionary-total", lambda p: p.update(direct_dictionary_sense_leads=9)),
    ]:
        mutant = copy.deepcopy(packet)
        change(mutant)
        try:
            audit(mutant, shortlist, historical, packet)
        except ValueError:
            continue
        raise AssertionError("Forged " + label + " passed")
    return 12*17 + 6

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet, shortlist, historical = load()
    report = audit(packet, shortlist, historical, packet)
    if args.self_test:
        n = self_test(packet, shortlist, historical)
        print("PASS: rejected %d/%d forged source, bilingual, provenance, approval mutations" % (n,n))
    print(json.dumps(report, sort_keys=True))

if __name__ == "__main__":
    main()
