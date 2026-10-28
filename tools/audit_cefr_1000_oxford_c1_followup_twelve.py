#!/usr/bin/env python3
"""Fail-closed source/provenance integrity audit for 12 C1 Oxford observations.
Does NOT verify exact-sense CEFR, translations, human review, listening or release.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-C1-FOLLOWUP-TWELVE-2026-10-29.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
U3 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf"
U5 = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf"
# Immutable publisher observations independently rechecked against official PDF text.
OBS = {
    "tribute": ("C1", 8, 1938, "tribute n.", "TRIBUTE_HONOUR_VS_PAYMENT_OR_OTHER_SENSE"),
    "trigger": ("B2", 3, 659, "trigger v.", "LOWER_B2_CAUSE_REACTION_VS_C1_DRAFT"),
    "racism": ("B2", 2, 503, "racism n.", "LOWER_B2_RACIAL_PREJUDICE_VS_UNFAIR_TREATMENT"),
    "signature": ("B2", 3, 569, "signature n.", "LOWER_B2_HANDWRITTEN_NAME_VS_DIGITAL_SIGNATURE"),
    "abortion": ("C1", 3, 706, "abortion n.", "INDUCED_VS_SPONTANEOUS_AND_NEUTRAL_MEDICAL_TERMINOLOGY"),
    "consistently": ("B2", 1, 121, "consistently adv.", "LOWER_B2_STABLE_STANDARD_VS_ALWAYS"),
    "conversion": ("C1", 4, 988, "conversion n.", "BUILDING_REPURPOSING_VS_RELIGIOUS_OR_UNIT_CONVERSION"),
    "copyright": ("C1", 4, 999, "copyright n.", "COPYRIGHT_LEGAL_RIGHT_VS_OWNERSHIP_AND_JURISDICTION"),
    "diverse": ("B2", 1, 185, "diverse adj.", "LOWER_B2_GROUP_VARIETY_VS_C1_DRAFT"),
    "exclusively": ("C1", 5, 1188, "exclusively adv.", "ONLY_VS_SPECIAL_PURPOSE_MYANMAR_ADVERB"),
    "functional": ("C1", 5, 1241, "functional adj.", "WORKING_STATE_VS_DESIGNED_FOR_PRACTICAL_PURPOSE"),
    "divine": (None, None, None, None, "UNLISTED_OXFORD_CORE_PDFS_NOT_A_CEFR_LABEL"),
}
RECORD_KEYS = {"word", "level", "part_of_speech", "shortlist_snapshot",
               "shortlist_provenance", "publisher_source", "editorial_risk",
               "independent_reviewer_task", "editorial_hold",
               "independently_reviewed", "release_approved", "independent_reviewer_receipt"}
PUBLISHER_KEYS = {"publisher", "title", "url", "additional_inspected_url",
                  "observed_on", "pdf_page", "extracted_line", "source_excerpt",
                  "source_cefr_level", "evidence_scope", "access"}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def audit(packet, shortlist):
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY", "scope/schema")
    require(packet.get("status") == "C1_FOLLOWUP_TWELVE_OXFORD_WORD_POS_EDITORIAL_HOLD", "status")
    require(packet.get("observed_on") == "2026-10-29", "date")
    require(packet.get("shortlist_blob_sha") == SHORTLIST_SHA, "shortlist blob reference")
    require(packet.get("record_count") == 12 and packet.get("counts_by_level") == {"A1": 0, "A2": 0, "B1": 0, "B2": 0, "C1": 12}, "packet counts")
    require(packet.get("word_pos_discrepancies") == 5 and packet.get("unlisted_in_inspected_core_lists") == 1, "conflict counts")
    require(packet.get("independently_approved_count") == 0, "fake packet approval")
    require(isinstance(packet.get("source_limitations"), str) and len(packet["source_limitations"]) > 100, "missing limitations")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "1000 shortlist")
    require({lvl: sum(e.get("level") == lvl for e in entries) for lvl in LEVELS} == dict.fromkeys(LEVELS, 200), "200 per level")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False and
                all(e.get(k) is False for k in ("reviewed_english", "reviewed_burmese",
                    "reviewed_example", "reviewed_level", "reviewed_pronunciation"))
                for e in entries), "shortlist cannot be self-approved")
    by_word = {(e["level"], e["word"]): e for e in entries}
    require(len(by_word) == 1000 and len({e["word"].casefold() for e in entries}) == 1000, "duplicate headwords")
    records = packet.get("records")
    require(isinstance(records, list) and [r.get("word") for r in records] == list(OBS), "12 exact words/order")
    for r in records:
        word = r["word"]
        expected_level, page, line, excerpt, risk = OBS[word]
        original = by_word[("C1", word)]
        require(set(r) == RECORD_KEYS, word + " record keys/hidden approval")
        require(r["level"] == "C1" and r["part_of_speech"] == original["part_of_speech"], word + " POS")
        require(r["shortlist_snapshot"] == {k: original[k] for k in ("english_definition", "myanmar_meaning", "example_sentence")}, word + " bilingual/example drift")
        provenance = {k: original[k] for k in ("source_path", "source_index", "source_blob_sha")}
        require(r["shortlist_provenance"] == provenance, word + " source provenance")
        path = ROOT / provenance["source_path"]
        require(path.is_file() and blob_sha(path.read_bytes()) == provenance["source_blob_sha"], word + " historical source blob")
        source = load_json(path)
        require(source["entries"][provenance["source_index"]]["word"] == word, word + " historical index")
        for k in ("english_definition", "burmese_meaning", "example_sentence", "part_of_speech", "level"):
            require(source["entries"][provenance["source_index"]][k] == original[k], word + " historical source field " + k)
        pub = r["publisher_source"]
        require(isinstance(pub, dict) and set(pub) == PUBLISHER_KEYS, word + " publisher keys")
        require(pub["publisher"] == "Oxford University Press" and pub["observed_on"] == "2026-10-29", word + " publisher/date")
        require(pub["url"] == U5 and pub["additional_inspected_url"] == (U3 if expected_level is None else None), word + " source URLs")
        require(pub["pdf_page"] == page and pub["extracted_line"] == line and pub["source_excerpt"] == excerpt and pub["source_cefr_level"] == expected_level, word + " publisher locator/level")
        require(pub["title"] == ("The Oxford 3000 and 5000 by CEFR level" if expected_level is None else "The Oxford 5000 by CEFR level"), word + " title")
        require(pub["access"] == "DIRECT_OFFICIAL_PDF_WEB_TEXT", word + " access")
        require(pub["evidence_scope"] == ("NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL" if expected_level is None else "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"), word + " evidence scope")
        require(r["editorial_risk"] == risk and "Human-independent reviewer" in r["independent_reviewer_task"], word + " risk/task")
        require(r["editorial_hold"] is True and r["independently_reviewed"] is False and r["release_approved"] is False and r["independent_reviewer_receipt"] is None, word + " fabricated signoff")
    proposals = packet.get("unreviewed_editorial_proposals")
    require(isinstance(proposals, list) and [p.get("word") for p in proposals] == ["functional", "consistently", "racism"], "proposals")
    for p in proposals:
        require(set(p) == {"word", "proposed_english_definition", "proposed_myanmar_meaning",
                           "proposed_original_example", "status", "reason"} and p["status"] == "UNREVIEWED_NOT_APPLIED", "proposal approval")
        require(all(isinstance(p[k], str) and len(p[k]) >= 10 for k in ("proposed_english_definition", "proposed_myanmar_meaning", "proposed_original_example", "reason")), "proposal fields")
    return {"records": 12, "Oxford_C1_word_pos": 6, "Oxford_B2_word_pos": 5,
            "not_found_in_inspected_core_lists": 1, "independent_approvals": 0}

def negative_tests(packet, shortlist):
    checks = 0
    for i in range(12):
        for field, bad in (("source_cefr_level", "C1" if i != 0 else "B2"),
                           ("source_excerpt", "forged n."),
                           ("pdf_page", 99),
                           ("extracted_line", 99999),
                           ("url", "https://invalid.example/forged.pdf"),
                           ("observed_on", "2035-01-01")):
            forged = copy.deepcopy(packet)
            forged["records"][i]["publisher_source"][field] = bad
            try:
                audit(forged, shortlist)
            except ValueError:
                checks += 1
            else:
                raise AssertionError("publisher forgery accepted: " + str((i, field)))
        for location, field, bad in (("shortlist_snapshot", "english_definition", "forged definition"),
                                     ("shortlist_snapshot", "myanmar_meaning", "အမှား"),
                                     ("shortlist_snapshot", "example_sentence", "Forged example."),
                                     ("shortlist_provenance", "source_blob_sha", "0"*40),
                                     ("root", "editorial_risk", "MISSING_RISK"),
                                     ("root", "independently_reviewed", True),
                                     ("root", "release_approved", True),
                                     ("root", "independent_reviewer_receipt", {"reviewer": "AI"}),
                                     ("root", "unexpected_reviewed_flag", True)):
            forged = copy.deepcopy(packet)
            target = forged["records"][i] if location == "root" else forged["records"][i][location]
            target[field] = bad
            try:
                audit(forged, shortlist)
            except ValueError:
                checks += 1
            else:
                raise AssertionError("content/approval forgery accepted: " + str((i, field)))
    for key, bad in (("record_count", 13), ("independently_approved_count", 1),
                     ("word_pos_discrepancies", 0), ("observed_on", "2030-01-01"),
                     ("shortlist_blob_sha", "0"*40)):
        forged = copy.deepcopy(packet)
        forged[key] = bad
        try:
            audit(forged, shortlist)
        except ValueError:
            checks += 1
        else:
            raise AssertionError("packet metadata forgery accepted: " + key)
    return checks

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    require(blob_sha(SHORTLIST.read_bytes()) == SHORTLIST_SHA, "shortlist Git blob changed")
    packet, shortlist = load_json(PACKET), load_json(SHORTLIST)
    result = audit(packet, shortlist)
    if args.self_test:
        result["negative_mutations_rejected"] = negative_tests(packet, shortlist)
        require(result["negative_mutations_rejected"] == 185, "mutation count")
        print("PASS: 185/185 forged Oxford source, Myanmar, provenance and false-review mutations rejected")
    print("PASS: Oxford C1 followup source-integrity", args.level, json.dumps(result, sort_keys=True))
    print("NOTE: no independent English/Myanmar/exact-sense CEFR signoff; no audio/iPhone/launch")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
