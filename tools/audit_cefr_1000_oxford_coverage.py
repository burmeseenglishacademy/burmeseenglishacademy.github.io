#!/usr/bin/env python3
"""Fail-closed cross-batch Oxford CEFR 1,000 source-coverage reconciliation.

Staging research only. Oxford word/POS labels do NOT independently establish
the intended exact sense, fluent Myanmar, example correctness or approval.
This deliberately normalizes two historical evidence schemas so missing
source_cefr_level cannot be mistaken for 'not listed'.
"""
import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = ("A1", "A2", "B1", "B2", "C1")
SHORTLIST = "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
SHORTLIST_SHA = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
PREFIX = "draft/CEFR-1000-OXFORD-"
PACKETS = {
    "A1": ("A1-TWELVE-DIRECT-PDF-2026-10-28", "A1-SECOND-TWELVE-2026-10-28",
           "A1-THIRD-TWELVE-2026-10-28", "A1-FOURTH-TWENTYFOUR-2026-10-29",
           "A1-FIFTH-TWENTYFOUR-2026-10-29", "A1-SIXTH-TWENTYFOUR-2026-10-29",
           "A1-SEVENTH-TWELVE-2026-10-29",
           "A1-EIGHTH-TWELVE-2026-10-29",
           "A1-NINTH-TWELVE-2026-10-29",
           "A1-TENTH-TWELVE-2026-10-29",
           "A1-ELEVENTH-TWELVE-2026-10-29",
           "A1-TWELFTH-TWELVE-2026-10-30",
           "A1-THIRTEENTH-TWELVE-2026-10-30",
           "A1-FOURTEENTH-ELEVEN-2026-10-30"),
    "A2": ("A2-TWELVE-DIRECT-PDF-2026-10-28", "A2-FOLLOWUP-TWELVE-2026-10-28",
           "A2-THIRD-TWENTYFOUR-2026-10-29",
           "A2-FOURTH-TWELVE-2026-10-29",
           "A2-FIFTH-TWELVE-2026-10-29",
           "A2-SIXTH-TWELVE-2026-10-30",
           "A2-SEVENTH-TWELVE-AND-THREE-DIRECT-SENSE-LEADS-2026-10-30",
           "A2-EIGHTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-30",
           "A2-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "A2-TWELFTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-31",
           "A2-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31"),
    "B1": ("B1-TWELVE-DIRECT-PDF-2026-10-28", "B1-LOWER-LEVEL-TWELVE-2026-10-28",
           "B1-MIXED-TWELVE-2026-10-28", "B1-FOURTH-TWENTYFOUR-2026-10-29",
           "B1-FIFTH-TWELVE-2026-10-29", "B1-SIXTH-TWELVE-2026-10-29",
           "B1-SEVENTH-TWELVE-AND-SIX-SENSE-LEADS-2026-10-30",
           "B1-EIGHTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-30",
           "B1-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B1-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B1-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B1-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31",
           "B1-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31"),
    "B2": ("B2-TWELVE-DIRECT-PDF-2026-10-28", "B2-LOWER-LEVEL-TWELVE-2026-10-28",
           "B2-ADDITIONAL-TWELVE-2026-10-28", "B2-FOURTH-TWENTYFOUR-2026-10-29",
           "B2-FIFTH-TWELVE-2026-10-29",
            "B2-SIXTH-TWELVE-2026-10-30",
           "B2-SEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B2-EIGHTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B2-NINTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B2-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "B2-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31",
           "B2-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31",
           "B2-THIRTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31"),
    "C1": ("C1-TWELVE-DIRECT-PDF-2026-10-28", "C1-B2-CONFLICT-TWELVE-2026-10-28",
           "C1-MIXED-TWELVE-2026-10-28", "C1-FOLLOWUP-TWELVE-2026-10-29",
           "C1-SIXTH-TWELVE-2026-10-29",
           "C1-SEVENTH-TWELVE-2026-10-30",
           "C1-EIGHTH-TWELVE-2026-10-30",
           "C1-NINTH-TWELVE-AND-EIGHT-DIRECT-SENSE-LEADS-2026-10-30",
           "C1-TENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30",
           "C1-ELEVENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30"),
}
EXPECTED = {
    "A1": {"observations": 203, "distinct": 195, "A1": 195},
    "A2": {"observations": 144, "distinct": 144, "A1": 92, "A2": 44, "B1": 8},
    "B1": {"observations": 168, "distinct": 168, "A1": 23, "A2": 68, "B1": 52, "B2": 25, "locator_only": 12},
    "B2": {"observations": 168, "distinct": 166, "A1": 3, "A2": 29, "B1": 36, "B2": 84, "C1": 13, "UNLISTED": 1, "locator_only": 12},
    "C1": {"observations": 120, "distinct": 111, "B1": 3, "B2": 44, "C1": 62, "UNLISTED": 2, "locator_only": 12},
}
SOURCE_PREFIX = "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_"
SOURCE_SUFFIX = "_by_CEFR_level.pdf"

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def git_blob_sha(path):
    raw = (ROOT / path).read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def load():
    shortlist = read(SHORTLIST)
    packets = {PREFIX + name + ".json": read(PREFIX + name + ".json")
               for names in PACKETS.values() for name in names}
    return shortlist, packets

def normalize(row):
    pub = row.get("publisher_source")
    if pub is not None:
        require(isinstance(pub, dict), "Publisher source object malformed")
        level = pub.get("source_cefr_level")
        url = pub.get("url")
        date = pub.get("observed_on")
        page = pub.get("pdf_page")
        line = pub.get("extracted_line")
        excerpt = pub.get("source_excerpt")
        scope = pub.get("evidence_scope")
        require(pub.get("publisher") == "Oxford University Press", "Publisher identity drift")
        require(pub.get("access") == "DIRECT_OFFICIAL_PDF_WEB_TEXT", "Direct-source access drift")
        absent_scopes = (
            "NOT_FOUND_IN_TWO_INSPECTED_PUBLISHER_CORE_LISTS_NOT_A_LEVEL",
            "NOT_FOUND_IN_TWO_INSPECTED_LISTS_NOT_EVIDENCE_OF_LEVEL",
            "NO_MATCH_IN_TWO_INSPECTED_CORE_LIST_PDFS_NOT_PROOF_OF_CEFR",
        )
        require(scope == "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE"
                or scope in absent_scopes, "Publisher evidence scope drift")
        if level is None:
            inspected = [x for x in (url, pub.get("additional_inspected_url"))
                         if x is not None] + pub.get("urls_inspected", [])
            require(scope in absent_scopes
                    and set(inspected) == {SOURCE_PREFIX + "3000" + SOURCE_SUFFIX,
                                           SOURCE_PREFIX + "5000" + SOURCE_SUFFIX}
                    and page is None and line is None and excerpt is None,
                    "Null CEFR is NOT a label: both actual PDF URLs must be recorded")
        else:
            require(scope == "DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE",
                    "Listed word must carry word/POS-only evidence")
        snapshot = row.get("shortlist_snapshot")
        provenance = row.get("shortlist_provenance")
        receipt = row.get("independent_reviewer_receipt")
    else:
        level = row.get("source_cefr")
        url = row.get("source_url")
        date = row.get("observed_on")
        page = row.get("pdf_page_1_based")
        line = row.get("pdf_extracted_line_0_based")
        excerpt = row.get("source_entry")
        scope = row.get("source_scope")
        require(row.get("source_authority") == "Oxford University Press", "Flat publisher identity drift")
        require(row.get("source_access") == "DIRECT_OFFICIAL_OUP_PDF_TEXT", "Flat source access drift")
        require(isinstance(scope, str) and "WORD_POS_LEVEL_ONLY_NOT_EXACT_SENSE" in scope,
                "Flat source cannot claim exact-sense approval")
        snapshot = {"english_definition": row.get("shortlist_english_definition"),
                    "myanmar_meaning": row.get("shortlist_myanmar_meaning"),
                    "example_sentence": row.get("shortlist_example")}
        provenance = {"source_path": row.get("shortlist_source_path"),
                      "source_index": row.get("shortlist_source_index"),
                      "source_blob_sha": row.get("shortlist_source_blob_sha")}
        receipt = row.get("reviewer_receipt")
    require(level in LEVELS or (level is None and pub is not None),
            "Missing source_cefr is NOT automatically UNLISTED")
    if level is not None or pub is None:
        require(url in (SOURCE_PREFIX + "3000" + SOURCE_SUFFIX,
                        SOURCE_PREFIX + "5000" + SOURCE_SUFFIX), "Untrusted Oxford PDF URL")
    require(date in ("2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31"), "Source observation date missing/drifted")
    if level is not None:
        require(type(page) is int and page > 0 and type(line) is int and line >= 0,
                "Invalid PDF page/line locator")
        if pub is not None:
            require(isinstance(excerpt, str) and excerpt.strip(), "Direct PDF excerpt missing")
        elif not excerpt:
            require("source_entry" not in row and isinstance(row.get("source_pos"), str)
                    and row["source_pos"].strip()
                    and isinstance(row.get("source_document"), str)
                    and row["source_document"].startswith("The Oxford "),
                    "Legacy locator-only evidence must not invent a source excerpt")
    require(row.get("editorial_hold") is True and row.get("independently_reviewed") is False
            and row.get("release_approved") is False and receipt is None,
            "Fabricated human review or approval in source packet")
    require(isinstance(row.get("editorial_risk"), str) and row["editorial_risk"].strip(),
            "Missing exact-sense editorial risk")
    return level or "UNLISTED", snapshot, provenance, (pub is None and not excerpt)

def audit(shortlist, packets, strict_counts=True):
    require(git_blob_sha(SHORTLIST) == SHORTLIST_SHA, "Frozen shortlist Git blob changed")
    require(shortlist.get("counts_by_level") == {l: 200 for l in LEVELS}
            and shortlist.get("independently_approved_by_level") == {l: 0 for l in LEVELS},
            "Incorrect approved scope or false independent approvals")
    entries = shortlist.get("entries")
    require(isinstance(entries, list) and len(entries) == 1000, "Exactly 1000 shortlist entries required")
    by_word = {r["word"]: r for r in entries}
    require(len(by_word) == 1000, "Duplicate headwords in provisional shortlist")
    require(all(r.get("editorial_hold") is True and r.get("release_approved") is False
                for r in entries), "Shortlist approval or editorial hold drift")
    summaries = {}
    overall = {}
    for level, names in PACKETS.items():
        unique = {}
        observations = 0
        locator_only = 0
        for name in names:
            path = PREFIX + name + ".json"
            packet = packets[path]
            require(packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
                    and packet.get("shortlist_blob_sha") == SHORTLIST_SHA,
                    path + ": wrong scope or frozen source binding")
            require(packet.get("independently_approved_count") == 0,
                    path + ": forged independent approval count")
            rows = packet.get("records")
            require(isinstance(rows, list) and packet.get("record_count") == len(rows),
                    path + ": record count drift")
            observations += len(rows)
            for row in rows:
                word = row.get("word")
                require(word in by_word and row.get("level") == level
                        and by_word[word]["level"] == level,
                        path + ": wrong word or proposed CEFR level")
                source = by_word[word]
                require(row.get("part_of_speech") == source.get("part_of_speech"),
                        path + ": shortlist POS drift for " + word)
                observed, snapshot, provenance, no_excerpt = normalize(row)
                locator_only += int(no_excerpt)
                require(snapshot == {"english_definition": source["english_definition"],
                                     "myanmar_meaning": source["burmese_meaning"],
                                     "example_sentence": source["example_sentence"]},
                        path + ": English/Myanmar/example snapshot drift for " + word)
                if provenance is not None:
                    require(provenance == {k: source[k] for k in
                            ("source_path", "source_index", "source_blob_sha")},
                            path + ": historical Git provenance drift for " + word)
                if word in unique:
                    require(unique[word]["observed"] == observed
                            and unique[word]["snapshot"] == snapshot,
                            path + ": duplicate publisher observations conflict for " + word)
                    unique[word]["sources"].append(path)
                else:
                    unique[word] = {"observed": observed, "snapshot": snapshot, "sources": [path]}
        counts = collections.Counter(x["observed"] for x in unique.values())
        actual = {"observations": observations, "distinct": len(unique), **dict(counts)}
        if locator_only:
            actual["locator_only"] = locator_only
        if strict_counts:
            require(actual == EXPECTED[level], level + ": evidence count drift " + str(actual))
        summaries[level] = actual
        for word, item in unique.items():
            require(word not in overall, "Cross-level headword observation conflict: " + word)
            overall[word] = {"draft_level": level, "oxford_word_pos": item["observed"],
                             "source_packets": item["sources"]}
    require(len(overall) == sum(x["distinct"] for x in summaries.values()),
            "Cross-level evidence coverage miscount")
    flagged = {word: item for word, item in overall.items()
               if item["draft_level"] != item["oxford_word_pos"]}
    return {"scope": "STAGING_ONLY_WORD_POS_RESEARCH_NOT_INDEPENDENT_SENSE_APPROVAL",
            "written_by_level": {l: 200 for l in LEVELS},
            "independently_approved_by_level": {l: 0 for l in LEVELS},
            "source_observations": sum(x["observations"] for x in summaries.values()),
            "distinct_observed_headwords": len(overall),
            "without_these_batch_observations": 1000 - len(overall),
            "by_level": summaries,
            "legacy_locator_only_records": sum(x.get("locator_only", 0) for x in summaries.values()),
            "flagged_distinct_headwords": len(flagged),
            "unlisted_not_a_cefr_label": sorted(w for w, x in flagged.items()
                                               if x["oxford_word_pos"] == "UNLISTED"),
            "duplicate_observation_words": sorted(w for w, x in overall.items()
                                                  if len(x["source_packets"]) > 1),
            "flagged_for_human_exact_sense_reconciliation": flagged,
            "independent_exact_sense_signoffs": 0,
            "final_george_emma_listening_signoffs": 0,
            "release_status": "BLOCKED_STAGING_ONLY"}

def self_test(shortlist, packets):
    baseline = audit(shortlist, packets)
    first = PREFIX + PACKETS["A1"][0] + ".json"
    flat = PREFIX + PACKETS["B1"][1] + ".json"
    last = PREFIX + "C1-FOLLOWUP-TWELVE-2026-10-29.json"
    newest = PREFIX + PACKETS["C1"][-1] + ".json"
    cases = [
        (first, lambda p: p["records"][0]["publisher_source"].update(source_cefr_level="C1")),
        (first, lambda p: p["records"][0]["shortlist_snapshot"].update(myanmar_meaning="forged")),
        (first, lambda p: p["records"][0].update(independently_reviewed=True)),
        (first, lambda p: p["records"][0].update(independent_reviewer_receipt={"fake": True})),
        (first, lambda p: p["records"][0]["publisher_source"].update(pdf_page=0)),
        (first, lambda p: p["records"][0]["publisher_source"].update(url="https://example.com/fake.pdf")),
        (first, lambda p: p.update(independently_approved_count=1)),
        (first, lambda p: p["records"].pop()),
        (flat, lambda p: p["records"][0].update(source_cefr=None)),
        (flat, lambda p: p["records"][0].update(shortlist_source_index=-1)),
        (flat, lambda p: p["records"][0].update(shortlist_example="forged")),
        (flat, lambda p: p["records"][0].update(release_approved=True)),
        (flat, lambda p: p["records"][0].update(source_pos="")),
        (flat, lambda p: p["records"][0].update(source_url="https://example.com/fake.pdf")),
        (last, lambda p: p["records"][-1]["publisher_source"].update(evidence_scope="DIRECT_PUBLISHER_PDF_WORD_POS_NOT_EXACT_SENSE")),
        (last, lambda p: p["records"][-1]["publisher_source"].update(source_cefr_level="C1")),
        (newest, lambda p: p["records"][0]["publisher_source"].update(source_excerpt="")),
        (newest, lambda p: p["records"][0]["publisher_source"].update(source_cefr_level="A1")),
        (newest, lambda p: p["records"][0].update(release_approved=True)),
        (newest, lambda p: p["records"][0]["shortlist_snapshot"].update(example_sentence="forged")),
    ]
    for path, change in cases:
        mutated = copy.deepcopy(packets)
        change(mutated[path])
        try:
            audit(shortlist, mutated)
        except ValueError:
            continue
        raise AssertionError("Forged publisher/reviewer mutation passed: " + path)
    return baseline, len(cases)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    shortlist, packets = load()
    if args.self_test:
        report, rejected = self_test(shortlist, packets)
        print("PASS: rejected %d/%d cross-batch forged evidence mutations" % (rejected, rejected))
    else:
        report = audit(shortlist, packets)
    if args.level != "ALL":
        print(json.dumps({args.level: report["by_level"][args.level],
                          "independent_approvals": 0, "release": "BLOCKED_STAGING_ONLY"}, sort_keys=True))
    else:
        print(json.dumps({k: v for k, v in report.items()
                          if k != "flagged_for_human_exact_sense_reconciliation"},
                         ensure_ascii=False, sort_keys=True))

if __name__ == "__main__":
    main()
