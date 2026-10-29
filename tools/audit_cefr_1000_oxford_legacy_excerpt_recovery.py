#!/usr/bin/env python3
"""Fail-closed Oxford 36 legacy excerpt recovery audit. Staging only.

Direct Oxford word/POS lines checked 2026-10-29; never exact-sense or
independent bilingual/CEFR approval. The 36 are already counted among 305
distinct observed headwords and MUST NOT increase coverage counts.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECOVERY = "draft/CEFR-1000-OXFORD-LEGACY-THIRTYSIX-EXCERPT-RECOVERY-2026-10-29.json"
LEGACY = {
    "B1": ("draft/CEFR-1000-OXFORD-B1-LOWER-LEVEL-TWELVE-2026-10-28.json",
           "a5c41a79cc7c39658635b84c811c9e91ff1d4a6e"),
    "B2": ("draft/CEFR-1000-OXFORD-B2-LOWER-LEVEL-TWELVE-2026-10-28.json",
           "014e73dba5139e972f3781033875012abbe456f5"),
    "C1": ("draft/CEFR-1000-OXFORD-C1-B2-CONFLICT-TWELVE-2026-10-28.json",
           "bf1a68895fb3164a1695522599a5f52f9a8b180e"),
}
PDF_ROOT = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_"
PDF_END = "_by_CEFR_level.pdf"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED_LINES = {
    "B1": (13, 15, 261, 341, 457, 820, 1069, 1351, 1415, 1509, 1594, 1813),
    "B2": (1477, 1895, 2567, 783, 2434, 2630, 3092, 1063, 924, 2489, 1915, 1120),
    "C1": (17, 172, 188, 222, 316, 320, 328, 348, 351, 475, 483, 613),
}

def require(test, reason):
    if not test:
        raise ValueError(reason)

def blob_sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load():
    recovery = json.loads((ROOT / RECOVERY).read_text(encoding="utf-8"))
    original = {level: json.loads((ROOT / path).read_text(encoding="utf-8"))
                for level, (path, _) in LEGACY.items()}
    return recovery, original

def audit(recovery, original):
    require(recovery.get("schema") == 1 and
            recovery.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY" and
            recovery.get("status") == "DIRECT_PUBLISHER_EXCERPT_RECOVERY_NOT_HUMAN_REVIEW" and
            recovery.get("observed_on") == "2026-10-29" and
            recovery.get("independently_approved_count") == 0 and
            recovery.get("record_count") == 36,
            "Recovery scope/count/hold drift")
    rows = recovery.get("records")
    require(isinstance(rows, list) and len(rows) == 36, "Exactly 36 recovered lines required")
    require(all(blob_sha(path) == sha for path, sha in LEGACY.values()),
            "Original historical source packet blob changed")
    require(all(len(original[l]["records"]) == 12 for l in LEGACY),
            "Legacy packet record count drift")
    seen = set()
    by_level = collections.Counter()
    for row in rows:
        level = row.get("draft_level")
        require(level in LEGACY, "Unexpected draft level")
        path, sha = LEGACY[level]
        idx = row.get("original_record_index")
        require(type(idx) is int and 0 <= idx < 12, "Invalid original record index")
        old = original[level]["records"][idx]
        word = old["word"]
        require((level, idx) not in seen, "Duplicate recovery row")
        seen.add((level, idx))
        require(row.get("word") == word and old["level"] == level,
                "Original word/level mismatch")
        require(row.get("original_packet_path") == path and
                row.get("original_packet_blob_sha") == sha,
                "Historical source path or Git blob SHA mismatch")
        require("source_entry" not in old and
                row.get("source_excerpt") == word + " " + old["source_pos"] and
                isinstance(old["source_pos"], str) and old["source_pos"].strip(),
                "Recovered Oxford literal excerpt mismatch")
        require(row.get("oxford_word_pos_level") == old["source_cefr"] and
                row["oxford_word_pos_level"] in LEVELS,
                "Oxford word/POS CEFR level drift")
        require(row.get("source_url") == old["source_url"] and
                row["source_url"] == PDF_ROOT +
                ("5000" if level == "C1" else "3000") + PDF_END,
                "Direct publisher URL drift")
        require(row.get("pdf_page_1_based") == old["pdf_page_1_based"] and
                row.get("pdf_extracted_line_0_based") == old["pdf_extracted_line_0_based"] and
                row["pdf_extracted_line_0_based"] == EXPECTED_LINES[level][idx],
                "Direct publisher page/line locator mismatch")
        require(row.get("observed_on") == "2026-10-29" and
                row.get("source_access") == "DIRECT_OFFICIAL_OXFORD_PDF_WEB_TEXT_LINE" and
                row.get("evidence_scope") == "PUBLISHER_WORD_POS_ONLY_NOT_EXACT_SENSE",
                "Recovery date or source scope drift")
        require(row.get("editorial_hold") is True and
                row.get("independently_reviewed") is False and
                row.get("release_approved") is False and
                row.get("human_reviewer_receipt") is None,
                "Fabricated independent review or release approval")
        by_level[level] += 1
    require(seen == {(l, i) for l in LEGACY for i in range(12)},
            "Missing legacy source observation")
    require(dict(by_level) == {l: 12 for l in LEGACY},
            "Expected twelve recovered excerpt lines per B1/B2/C1")
    return {
        "recovered_direct_publisher_excerpt_lines": 36,
        "by_draft_level": dict(by_level),
        "new_distinct_headwords": 0,
        "prior_locator_only_records_now_cross_referenced_to_recovery": 36,
        "human_independent_approvals": 0,
        "exact_sense_approvals": 0,
        "release": "BLOCKED_STAGING_ONLY"
    }

def self_test(recovery, original):
    mutations = [
        lambda r: r["records"][0].update(source_excerpt="address v."),
        lambda r: r["records"][0].update(pdf_extracted_line_0_based=14),
        lambda r: r["records"][0].update(pdf_page_1_based=2),
        lambda r: r["records"][0].update(oxford_word_pos_level="C1"),
        lambda r: r["records"][0].update(observed_on="2026-10-30"),
        lambda r: r["records"][0].update(source_url="https://example.org/oxford.pdf"),
        lambda r: r["records"][0].update(independently_reviewed=True),
        lambda r: r["records"][0].update(human_reviewer_receipt={"fake": True}),
        lambda r: r["records"][0].update(release_approved=True),
        lambda r: r["records"][0].update(original_packet_blob_sha="0" * 40),
        lambda r: r["records"][0].update(original_record_index=11),
        lambda r: r["records"][0].update(word="fake"),
        lambda r: r["records"].pop(),
        lambda r: r["records"].append(copy.deepcopy(r["records"][0])),
        lambda r: r.update(independently_approved_count=1),
        lambda r: r.update(status="INDEPENDENTLY_APPROVED"),
        lambda r: r["records"][-1].update(source_excerpt="sustainable n."),
        lambda r: r["records"][-1].update(evidence_scope="EXACT_SENSE_APPROVED"),
        lambda r: r["records"][-1].update(editorial_hold=False),
        lambda r: r["records"][-1].update(source_access="SEARCH_SNIPPET"),
    ]
    for n, change in enumerate(mutations, 1):
        altered = copy.deepcopy(recovery)
        change(altered)
        try:
            audit(altered, original)
        except ValueError:
            continue
        raise AssertionError("False evidence or signoff mutation accepted: " + str(n))
    return len(mutations)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    recovery, original = load()
    result = audit(recovery, original)
    if args.self_test:
        n = self_test(recovery, original)
        print("PASS: rejected %d/%d forged excerpt, provenance and reviewer mutations" % (n, n))
    if args.level != "ALL":
        print(json.dumps({"draft_level": args.level,
                          "recovered_excerpt_lines": result["by_draft_level"].get(args.level, 0),
                          "independently_approved": 0,
                          "release": "BLOCKED_STAGING_ONLY"}))
    else:
        print(json.dumps(result, sort_keys=True))

if __name__ == "__main__":
    main()
