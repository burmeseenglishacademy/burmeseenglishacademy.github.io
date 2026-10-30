#!/usr/bin/env python3
"""Fail-closed twelfth B2 publisher research. Editorial staging only, NO approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-OXFORD-B2-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json"
SHORT = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_SHA = "8770ad76b6961b7cc94d17feeae978941e08231e"
SHORT_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = [["quote","B1",9,2348,"quote v., n.","3000"],["tie","A2",7,1707,"tie v., n.","3000"],["wise","B2",12,3312,"wise adj.","3000"],["inner","B2",11,2941,"inner adj.","3000"],["lift","A2",5,1359,"lift v., n.","3000"],["tower","A2",7,1716,"tower n.","3000"],["cabinet","C1",4,871,"cabinet n.","5000"],["contrast","B1",8,1936,"contrast n., v.","3000"],["establish","B2",11,2827,"establish v.","3000"],["proposal","B2",12,3102,"proposal n.","3000"],["reputation","B2",12,3136,"reputation n.","3000"],["assessment","B2",10,2640,"assessment n.","3000"]]
LEADS = {"quote":["https://www.oxfordlearnersdictionaries.com/definition/english/quote_1",1,113,138],"cabinet":["https://www.oxfordlearnersdictionaries.com/definition/english/cabinet",2,147,154],"contrast":["https://www.oxfordlearnersdictionaries.com/definition/english/contrast_1",1,105,116],"establish":["https://www.oxfordlearnersdictionaries.com/definition/english/establish",1,112,120]}
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
            and p.get("status") == "B2_TWELFTH_TWELVE_DIRECT_OXFORD_WORD_POS_FOUR_SENSE_LEADS_EDITORIAL_HOLD"
            and p.get("observed_on") == "2026-10-31"
            and p.get("shortlist_blob_sha") == SHORT_SHA
            and p.get("record_count") == 12
            and p.get("counts_by_level") == dict(zip(LEVELS, (0, 0, 0, 12, 0)))
            and p.get("publisher_reference_level_counts") == {"A2": 3, "B1": 2, "B2": 6, "C1": 1}
            and p.get("word_pos_discrepancies") == 6
            and p.get("direct_dictionary_sense_leads") == 4
            and p.get("independently_approved_count") == 0
            and "NOT independent exact-sense CEFR" in p.get("source_limitations", ""),
            "Staging research scope or source limitation drift")
    rows = p.get("records")
    require(isinstance(rows, list) and len(rows) == 12, "Twelve B2 records required")
    for row, (word, cefr, page, line, excerpt, docname) in zip(rows, EXPECTED):
        e = by.get(word)
        require(e is not None and e.get("level") == "B2"
                and row.get("word") == word and row.get("level") == "B2"
                and row.get("part_of_speech") == e.get("part_of_speech"),
                "B2 headword/POS mismatch: " + word)
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
    print(f"PASS: {args.level} twelve B2 Oxford word/POS observations; A2=3 B1=2 B2=6 C1=1; four direct dictionary leads; 0 independent approvals; STAGING ONLY; NO DEPLOY")

if __name__ == "__main__":
    main()
