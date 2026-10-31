#!/usr/bin/env python3
"""Fail-closed, research-only A1 five-exception audit. Not an independent CEFR approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-A1-FINAL-FIVE-INFLECTED-FORMS-AND-RABBIT-SENSE-TRIAGE-2026-10-31.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "ede8c397635736a29f0b0bfa5031677425a7365c"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
WORDS = ("is", "are", "does", "did", "rabbit")
LEMMAS = ("be", "be", "do", "do", "rabbit")
URLS = (
    "https://dictionary.cambridge.org/dictionary/english/is",
    "https://dictionary.cambridge.org/dictionary/english/are",
    "https://dictionary.cambridge.org/us/dictionary/english/does",
    "https://dictionary.cambridge.org/us/dictionary/english/did",
    "https://www.oxfordlearnersdictionaries.com/definition/english/rabbit_1",
)
SUPPORT = (
    "https://dictionary.cambridge.org/dictionary/learner-english/be",
    "https://dictionary.cambridge.org/grammar/british-grammar/be",
    "https://dictionary.cambridge.org/us/dictionary/essential-british-english/do",
    "https://dictionary.cambridge.org/us/dictionary/essential-british-english/do",
    "https://dictionary.cambridge.org/dictionary/english/rabbit",
)
BADGES = (
    "A1_LEMMA_DESCRIPTION_NOT_IS_HEADWORD",
    "GRAMMAR_FORM_ONLY_NO_INDEPENDENT_CEFR",
    "A1_AUXILIARY_DO_NOT_DOES_HEADWORD",
    "A1_AUXILIARY_DO_NOT_DID_HEADWORD",
    "OXFORD_ANIMALS_TOPIC_A2_AND_CAMBRIDGE_INDEXED_NOUN_A2",
)

def require(ok, why):
    if not ok:
        raise ValueError(why)

def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\\0" + data).hexdigest()

def load():
    return (json.loads(PACKET.read_text(encoding="utf-8")),
            json.loads(SHORTLIST.read_text(encoding="utf-8")))

def audit(packet, shortlist, check_files=True):
    if check_files:
        require(blob(PACKET) == PACKET_SHA and blob(SHORTLIST) == SHORTLIST_SHA,
                "Immutable packet or shortlist Git blob changed")
    require(len(shortlist.get("entries", [])) == 1000 and
            shortlist.get("counts_by_level") == dict.fromkeys(LEVELS, 200) and
            shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
            "Wrong 1,000 scope or fabricated approvals")
    require(all(e.get("editorial_hold") is True and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english","reviewed_burmese","reviewed_example",
                         "reviewed_level","reviewed_pronunciation"))
                for e in shortlist["entries"]), "Shortlist flags not held")
    source = {e["word"]:e for e in shortlist["entries"]}
    require(len(source) == 1000, "Duplicate shortlist headwords")
    require(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and packet.get("status") == "A1_LAST_FIVE_NON_OXFORD_WORD_POS_LEMMA_AND_SENSE_TRIAGE_EDITORIAL_HOLD"
            and packet.get("observed_on") == "2026-10-31"
            and packet.get("shortlist_blob_sha") == SHORTLIST_SHA
            and packet.get("record_count") == 5
            and packet.get("counts_by_level") == {"A1":5,"A2":0,"B1":0,"B2":0,"C1":0}
            and packet.get("independently_approved_count") == 0
            and packet.get("oxford_direct_word_pos_count_added") == 0,
            "Wrong packet scope/count or false Oxford coverage/approval")
    limitations = packet.get("source_limitations", "")
    require("HTTP 403" in limitations and "topic tag" in limitations and
            "not directly inspected" in limitations and "unapproved" in limitations,
            "Source access limitation or approval warning removed")
    rows = packet.get("records")
    require(isinstance(rows,list) and len(rows) == 5 and
            [r.get("word") for r in rows] == list(WORDS), "Five exact A1 exceptions required")
    for i, row in enumerate(rows):
        word = WORDS[i]
        original = source[word]
        require(original["level"] == "A1" and row.get("level") == "A1"
                and row.get("part_of_speech") == original["part_of_speech"]
                and row.get("lemma") == LEMMAS[i], "Word/POS/lemma mismatch: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": original["english_definition"],
            "myanmar_meaning": original["burmese_meaning"],
            "example_sentence": original["example_sentence"]},
            "Frozen bilingual snapshot changed: " + word)
        require(row.get("shortlist_provenance") ==
                {k:original[k] for k in ("source_path","source_index","source_blob_sha")},
                "Historical source provenance changed: " + word)
        historical = ROOT / original["source_path"]
        require(historical.is_file() and blob(historical) == original["source_blob_sha"],
                "Historical source blob mismatch: " + word)
        old = json.loads(historical.read_text(encoding="utf-8"))["entries"][original["source_index"]]
        require(all(old.get(k) == original.get(k) for k in
                    ("word","level","part_of_speech","english_definition",
                     "burmese_meaning","example_sentence")),
                "Historical original row mismatch: " + word)
        lead = row.get("publisher_lead")
        require(isinstance(lead,dict) and lead.get("source_url") == URLS[i]
                and lead.get("support_url") == SUPPORT[i]
                and lead.get("observed_on") == "2026-10-31"
                and lead.get("observed_label_scope") == BADGES[i]
                and lead.get("evidence_scope") ==
                    ("OXFORD_DIRECT_SENSE_AND_CAMBRIDGE_INDEXED_A2" if word=="rabbit"
                     else "CAMBRIDGE_INDEXED_FORM_PLUS_LEMMA")
                and lead.get("access") ==
                    ("DIRECT_OXFORD_DICTIONARY_WEB_TEXT_AND_CAMBRIDGE_SEARCH_INDEX_ONLY"
                     if word=="rabbit" else "CAMBRIDGE_SEARCH_INDEX_ONLY_DIRECT_PAGE_403")
                and lead.get("publisher") ==
                    ("Oxford University Press; Cambridge University Press" if word=="rabbit"
                     else "Cambridge University Press")
                and isinstance(lead.get("source_excerpt_summary"),str)
                and len(lead["source_excerpt_summary"]) > 30,
                "Publisher scope/URL/observation drift: " + word)
        require(isinstance(row.get("editorial_risk"),str) and
                len(row["editorial_risk"]) > 80 and
                isinstance(row.get("independent_reviewer_task"),str) and
                "Human-independent" in row["independent_reviewer_task"],
                "Exact-sense or human-review risk removed: " + word)
        candidate = row.get("editorial_rewrite_candidate")
        require(isinstance(candidate,dict) and
                candidate.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
                and all(isinstance(candidate.get(k),str) and len(candidate[k]) > 15
                        for k in ("myanmar_meaning","original_example")),
                "Editorial candidate improperly approved or incomplete: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "False independent approval: " + word)
    return True

def self_test(packet, shortlist):
    trials = 0
    for i in range(5):
        for field, value in (
            ("word","fake"), ("level","C1"), ("lemma","fake"),
            ("part_of_speech","fake"), ("editorial_hold",False),
            ("independently_reviewed",True), ("release_approved",True),
            ("independent_reviewer_receipt",{"reviewer":"fabricated"}),
        ):
            mutated = copy.deepcopy(packet)
            mutated["records"][i][field] = value
            try: audit(mutated, shortlist, False)
            except ValueError: trials += 1
            else: raise AssertionError("Forged row accepted: " + str((i,field)))
        for path, value in (
            (("shortlist_snapshot","myanmar_meaning"),"wrong"),
            (("shortlist_snapshot","example_sentence"),"wrong"),
            (("shortlist_provenance","source_index"),999),
            (("publisher_lead","source_url"),"https://example.invalid/forged"),
            (("publisher_lead","observed_label_scope"),"A1_DIRECT_APPROVED"),
            (("publisher_lead","access"),"DIRECT_UNVERIFIED"),
            (("editorial_rewrite_candidate","review_status"),"APPROVED"),
        ):
            mutated = copy.deepcopy(packet)
            mutated["records"][i][path[0]][path[1]] = value
            try: audit(mutated, shortlist, False)
            except (ValueError,IndexError): trials += 1
            else: raise AssertionError("Forged nested field accepted: " + str((i,path)))
    for field, value in (
        ("record_count",1000), ("independently_approved_count",5),
        ("oxford_direct_word_pos_count_added",5), ("source_limitations","approved"),
        ("shortlist_blob_sha","forged"), ("status","RELEASE_APPROVED"),
    ):
        mutated=copy.deepcopy(packet); mutated[field]=value
        try: audit(mutated, shortlist, False)
        except ValueError: trials += 1
        else: raise AssertionError("Forged packet accepted: " + field)
    print("PASS: " + str(trials) +
          "/"+str(5*15+6)+" A1 final-five source, lemma, bilingual and fake-review mutations rejected")
    require(trials == 81, "Wrong adversarial test total")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--level",choices=LEVELS+("ALL",),default="ALL")
    ap.add_argument("--self-test",action="store_true")
    args=ap.parse_args()
    packet,shortlist=load()
    audit(packet,shortlist)
    print("PASS: A1 last five remain research-only; four forms map to lemmas and rabbit A2 lead is not an Oxford word/POS count; independent approvals 0/5")
    if args.self_test: self_test(packet,shortlist)

if __name__ == "__main__":
    main()
