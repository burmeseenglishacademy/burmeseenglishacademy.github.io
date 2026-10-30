#!/usr/bin/env python3
"""Fail-closed thirteenth A2 publisher research. Editorial staging only, NO approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-A2-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "9f1c9619081dd9c2249f97efdaf76a790c6e0dfe"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = [["club","A1",1,157,"club n.","3000"],["film","A1",2,287,"film n.","3000"],["event","A1",1,249,"event n.","3000"],["watch","A1",4,860,"watch v., n.","3000"],["third","A1",3,791,"third number","3000"],["form","A1",2,307,"form n., v.","3000"],["act","A2",4,916,"act v.","3000"],["quite","A1",3,634,"quite adv.","3000"],["west","A1",4,872,"west n., adj., adv.","3000"],["final","A1",2,288,"final adj.","3000"],["current","B1",8,1953,"current adj.","3000"],["program","A2",6,1505,"program n.","3000"]]
LEADS = {"third":["https://www.oxfordlearnersdictionaries.com/definition/english/third_1",1,88,115],"act":["https://www.oxfordlearnersdictionaries.com/definition/english/act_1",1,124,146],"quite":["https://www.oxfordlearnersdictionaries.com/definition/english/quite",1,105,123],"program":["https://www.oxfordlearnersdictionaries.com/definition/english/program_1",1,88,123]}
BASE = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/"

def require(ok, msg):
    if not ok:
        raise ValueError(msg)

def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def audit(doc=None, shortlist=None):
    require(blob(PACKET) == PACKET_SHA and blob(SHORT) == SHORT_SHA,
            "Frozen source research packet or shortlist Git blob changed")
    truth = json.loads(PACKET.read_text(encoding="utf-8"))
    p = doc if doc is not None else truth
    require(p == truth, "Publisher packet altered or forged review receipt")
    s = shortlist if shortlist is not None else json.loads(SHORT.read_text(encoding="utf-8"))
    require(s.get("counts_by_level") == dict.fromkeys(LEVELS, 200)
            and s.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0)
            and len(s.get("entries", [])) == 1000, "Frozen 1000 scope/approval drift")
    by = {e["word"]: e for e in s["entries"]}
    require(len(by) == 1000, "Duplicate provisional headwords")
    require(all(e.get("editorial_hold") is True
                and e.get("release_approved") is False
                and all(e.get(k) is False for k in
                        ("reviewed_english", "reviewed_burmese", "reviewed_example",
                         "reviewed_level", "reviewed_pronunciation"))
                for e in s["entries"]), "Unverified shortlist approval drift")
    require(p.get("schema") == 1
            and p.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
            and p.get("status") == "A2_THIRTEENTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and p.get("observed_on") == "2026-10-31"
            and p.get("shortlist_blob_sha") == SHORT_SHA
            and p.get("record_count") == 12
            and p.get("counts_by_level") == dict(zip(LEVELS, (0, 12, 0, 0, 0)))
            and p.get("publisher_reference_level_counts") == {"A1": 9, "A2": 2, "B1": 1}
            and p.get("word_pos_discrepancies") == 10
            and p.get("direct_dictionary_sense_leads") == 4
            and p.get("independently_approved_count") == 0
            and "not independent exact-sense cefr" in p.get("source_limitations", "").lower(),
            "Staging research scope or source limitation drift")
    rows = p.get("records")
    require(isinstance(rows, list) and len(rows) == 12, "Twelve A2 records required")
    for row, (word, cefr, page, line, excerpt, docname) in zip(rows, EXPECTED):
        e = by.get(word)
        require(e is not None and e.get("level") == "A2"
                and row.get("word") == word and row.get("level") == "A2"
                and row.get("part_of_speech") == e.get("part_of_speech"),
                "A2 headword/POS mismatch: " + word)
        require(row.get("shortlist_snapshot") == {
            "english_definition": e["english_definition"],
            "myanmar_meaning": e["burmese_meaning"],
            "example_sentence": e["example_sentence"]},
            "Original bilingual/example snapshot drift: " + word)
        require(row.get("shortlist_provenance") == {
            k: e[k] for k in ("source_path", "source_index", "source_blob_sha")},
            "Historical Git source provenance drift: " + word)
        require(row.get("publisher_source") == {
            "publisher": "Oxford University Press",
            "title": "The Oxford " + docname + " by CEFR level",
            "url": BASE + "The_Oxford_" + docname + "_by_CEFR_level.pdf",
            "observed_on": "2026-10-31", "pdf_page": page,
            "extracted_line": line, "source_excerpt": excerpt,
            "source_cefr_level": cefr,
            "evidence_scope": "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
            "access": "DIRECT_OFFICIAL_PDF_WEB_TEXT"},
            "Publisher CEFR/POS or locator mismatch: " + word)
        require(row.get("editorial_hold") is True
                and row.get("independently_reviewed") is False
                and row.get("release_approved") is False
                and row.get("independent_reviewer_receipt") is None,
                "False independent review or approval: " + word)
        require(len(row.get("editorial_risk", "")) > 55
                and "Independent human editor" in row.get("independent_reviewer_task", ""),
                "Exact-sense editorial risk or reviewer task missing: " + word)
        lead = row.get("dictionary_sense_lead")
        proposal = row.get("editorial_rewrite_candidate")
        if word in LEADS:
            url, sense, first, last = LEADS[word]
            require(isinstance(lead, dict)
                    and lead.get("url") == url
                    and lead.get("sense_number") == sense
                    and lead.get("page_text_line_start") == first
                    and lead.get("page_text_line_end") == last
                    and lead.get("observed_on") == "2026-10-31"
                    and lead.get("evidence_scope") ==
                        "DIRECT_DICTIONARY_SENSE_LEAD_NOT_INDEPENDENT_CEFR_SIGNOFF"
                    and len(lead.get("editorial_interpretation", "")) > 50,
                    "Direct dictionary sense provenance mismatch: " + word)
            require(isinstance(proposal, dict)
                    and proposal.get("status") == "UNAPPROVED_EDITORIAL_PROPOSAL_NOT_APPLIED"
                    and len(proposal.get("myanmar_meaning", "")) > 10
                    and len(proposal.get("original_example_sentence", "")) > 25,
                    "Unapproved bilingual/example candidate drift: " + word)
        else:
            require(lead is None and proposal is None,
                    "Invented dictionary sense for uninspected entry: " + word)
    return True

def self_test():
    truth = json.loads(PACKET.read_text(encoding="utf-8"))
    mutations = [
        (("publisher_source", "source_cefr_level"), "INVALID"),
        (("publisher_source", "url"), "https://example.invalid/forged.pdf"),
        (("publisher_source", "observed_on"), "2026-11-01"),
        (("publisher_source", "pdf_page"), 999),
        (("publisher_source", "extracted_line"), 9999),
        (("publisher_source", "source_excerpt"), "invented evidence"),
        (("publisher_source", "evidence_scope"), "INDEPENDENT_EXACT_SENSE"),
        (("shortlist_snapshot", "english_definition"), "invented definition"),
        (("shortlist_snapshot", "myanmar_meaning"), "အတု"),
        (("shortlist_snapshot", "example_sentence"), "Invented sentence."),
        (("shortlist_provenance", "source_blob_sha"), "0" * 40),
        (("shortlist_provenance", "source_index"), -1),
        (("editorial_risk",), "no risk"),
        (("independently_reviewed",), True),
        (("release_approved",), True),
        (("editorial_hold",), False),
        (("independent_reviewer_receipt",), {"reviewer": "AI"}),
        (("independent_reviewer_task",), "approved by model"),
    ]
    n = 0
    for i in range(12):
        for path, value in mutations:
            forged = copy.deepcopy(truth)
            target = forged["records"][i]
            for k in path[:-1]:
                target = target[k]
            target[path[-1]] = value
            try:
                audit(forged)
            except ValueError:
                n += 1
                continue
            raise AssertionError("Forged publisher/bilingual/reviewer evidence accepted")
    for i, row in enumerate(truth["records"]):
        if row["word"] not in LEADS:
            continue
        for path, value in [
            (("dictionary_sense_lead", "url"), "https://example.invalid/fake"),
            (("dictionary_sense_lead", "sense_number"), 999),
            (("editorial_rewrite_candidate", "myanmar_meaning"), "အတု"),
            (("editorial_rewrite_candidate", "status"), "APPROVED"),
        ]:
            forged = copy.deepcopy(truth)
            target = forged["records"][i]
            for k in path[:-1]:
                target = target[k]
            target[path[-1]] = value
            try:
                audit(forged)
            except ValueError:
                n += 1
                continue
            raise AssertionError("Forged dictionary sense or candidate approval accepted")
    require(n == 232, "Expected exactly 232 adversarial mutations")
    return n

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    audit()
    if args.self_test:
        n = self_test()
        print(f"PASS: {n}/232 publisher, bilingual, sense, provenance and false-review mutations rejected")
    print(f"PASS: {args.level} twelve A2 Oxford word/POS observations; A1=9 A2=2 B1=1; four direct dictionary leads; 0 independent approvals; STAGING ONLY; NO DEPLOY")

if __name__ == "__main__":
    main()
