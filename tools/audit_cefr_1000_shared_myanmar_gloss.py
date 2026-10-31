#!/usr/bin/env python3
"""Research-only fail-closed audit for seven shared Myanmar-gloss pairs.

This is a documentary snapshot/structural integrity check, NOT independent
Myanmar editing, exact-sense CEFR approval, or permission to publish.
"""
import argparse
import collections
import copy
import hashlib
import json
import pathlib
import re
import sys
from urllib.parse import urlparse, unquote

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "draft/CEFR-1000-SHARED-MYANMAR-GLOSS-SEVEN-PAIRS-2026-11-01.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
PACKET_BLOB = "7bc4951d5244e866513b706570128a2c66614e8d"
SHORTLIST_BLOB = "475e68ae17ab97bd937e73e5ce4794e0dcd76551"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
PAIRS = (("need", "require"), ("deal", "agreement"),
         ("finally", "eventually"), ("protect", "defend"),
         ("competition", "contest"), ("mental", "psychological"),
         ("calm", "stable"))
EXPECTED_COUNTS = {"A1": 1, "A2": 2, "B1": 6, "B2": 5, "C1": 0}
DIRECT = frozenset(("deal", "finally", "eventually", "competition",
                    "contest", "mental", "stable"))
EXPECTED_LINES = {"deal": [108, 120], "finally": [103, 122],
                  "eventually": [103, 118], "competition": [113, 130],
                  "contest": [105, 115], "mental": [103, 119],
                  "stable": [111, 122]}
EXPECTED_CEFR_LEADS = {
    "need": "A1", "require": "B1", "deal": "B2",
    "agreement": "B2", "finally": "A2", "eventually": "B2",
    "protect": "B1", "defend": None, "competition": "A2",
    "contest": "B1", "mental": "B2", "psychological": "B2",
    "calm": None, "stable": "C1",
}
EXPECTED_URLS = {
    "need": "https://dictionary.cambridge.org/dictionary/english/need",
    "require": "https://dictionary.cambridge.org/dictionary/english/require",
    "deal": "https://www.oxfordlearnersdictionaries.com/definition/english/deal_2",
    "agreement": "https://dictionary.cambridge.org/dictionary/english/agreement",
    "finally": "https://www.oxfordlearnersdictionaries.com/definition/english/finally",
    "eventually": "https://www.oxfordlearnersdictionaries.com/definition/english/eventually",
    "protect": "https://dictionary.cambridge.org/dictionary/english/protect",
    "defend": "https://dictionary.cambridge.org/dictionary/english/defend",
    "competition": "https://www.oxfordlearnersdictionaries.com/definition/english/competition",
    "contest": "https://www.oxfordlearnersdictionaries.com/definition/english/contest_1",
    "mental": "https://www.oxfordlearnersdictionaries.com/definition/english/mental_1",
    "psychological": "https://dictionary.cambridge.org/dictionary/english/psychological",
    "calm": "https://dictionary.cambridge.org/dictionary/english/calm",
    "stable": "https://www.oxfordlearnersdictionaries.com/definition/english/stable_1",
}

def blob_sha(path):
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def check(packet, shortlist, baseline=None, check_disk=True):
    errors = []
    def need(condition, message):
        if not condition:
            errors.append(message)
    if check_disk:
        need(blob_sha(PACKET) == PACKET_BLOB, "Pinned research packet Git blob changed")
        need(blob_sha(SHORTLIST) == SHORTLIST_BLOB, "Frozen shortlist Git blob changed")
    if baseline is not None:
        need(packet == baseline, "Source-bound packet mutated relative to pinned research snapshot")
    need(isinstance(shortlist, dict) and isinstance(shortlist.get("entries"), list),
         "Missing provisional shortlist")
    entries = shortlist.get("entries", []) if isinstance(shortlist, dict) else []
    need(len(entries) == 1000, "Not exactly 1,000 provisional entries")
    counts = collections.Counter(x.get("level") for x in entries if isinstance(x, dict))
    need(dict(counts) == dict.fromkeys(LEVELS, 200), "Wrong per-level 200-word scope")
    need(shortlist.get("independently_approved_by_level") == dict.fromkeys(LEVELS, 0),
         "Unjustified independent approvals")
    need(all(isinstance(x, dict) and x.get("editorial_hold") is True
             and x.get("release_approved") is False
             and all(x.get(k) is False for k in ("reviewed_english", "reviewed_burmese",
                    "reviewed_example", "reviewed_level", "reviewed_pronunciation"))
             for x in entries), "Provisional shortlist review flags not held")
    by_word = {x.get("word"): x for x in entries if isinstance(x, dict)}
    need(len(by_word) == 1000, "Duplicate provisional headword")
    glosses = collections.defaultdict(list)
    for e in entries:
        if isinstance(e, dict):
            glosses[e.get("burmese_meaning")].append(e.get("word"))
    repeated = {frozenset(v) for v in glosses.values() if len(v) > 1}
    need(repeated == {frozenset(p) for p in PAIRS},
         "The seven repeated Myanmar gloss pairs drifted or new duplicates appeared")
    need(packet.get("schema") == 1 and packet.get("scope") == "CEFR_1000_TOTAL_STAGING_ONLY"
         and packet.get("status") == "SEVEN_SHARED_MYANMAR_GLOSS_PAIRS_SOURCE_TRIAGE_UNAPPROVED"
         and packet.get("observed_on") == "2026-11-01"
         and packet.get("shortlist_blob_sha") == SHORTLIST_BLOB,
         "Research packet scope, status, date or frozen provenance invalid")
    limitations = packet.get("source_limitations", "")
    need(isinstance(limitations, str) and "HTTP 403" in limitations
         and "NOT independently" in limitations and "unapproved" in limitations,
         "Publisher access and independent-review limitations must remain explicit")
    scan = packet.get("scan_scope", {})
    need(scan == {"entries_scanned": 1000, "identical_myanmar_gloss_pair_groups": 7,
                  "flagged_entries": 14, "per_level": EXPECTED_COUNTS,
                  "independent_approvals": 0},
         "Research scan counts or zero approval changed")
    distinctions = packet.get("pair_distinctions", [])
    need(len(distinctions) == 7 and all(
        d.get("pair_id") == i+1 and d.get("words") == list(pair)
        and len(d.get("editorial_distinction", "")) >= 35
        for i, (d, pair) in enumerate(zip(distinctions, PAIRS))),
        "Seven contrastive pair notes incomplete or altered")
    rows = packet.get("records", [])
    need(isinstance(rows, list) and len(rows) == 14, "Not fourteen source-bound rows")
    seen = set()
    for row in rows if isinstance(rows, list) else []:
        if not isinstance(row, dict):
            errors.append("Non-object source-bound row")
            continue
        w = row.get("word")
        if w not in EXPECTED_URLS:
            errors.append("Unexpected source-bound headword")
            continue
        need(w not in seen, w + ": duplicate row")
        seen.add(w)
        e = by_word.get(w, {})
        need(row.get("level") == e.get("level")
             and row.get("part_of_speech") == e.get("part_of_speech"),
             w + ": level/POS drift")
        need(row.get("original") == {"english_definition": e.get("english_definition"),
             "myanmar_meaning": e.get("burmese_meaning"),
             "example_sentence": e.get("example_sentence")},
             w + ": frozen English/Myanmar/example mismatch")
        need(row.get("provenance") == {k:e.get(k) for k in
             ("source_path", "source_index", "source_blob_sha")},
             w + ": historical source blob/index mismatch")
        pair_id = row.get("pair_id")
        pair = PAIRS[pair_id-1] if type(pair_id) is int and 1 <= pair_id <= 7 else ()
        need(w in pair and row.get("pair_word") in pair and row.get("pair_word") != w,
             w + ": pair binding mismatch")
        o = row.get("publisher_observation", {})
        direct = w in DIRECT
        need(o.get("source_url") == EXPECTED_URLS[w]
             and o.get("observed_on") == "2026-11-01"
             and o.get("source_scope") == "SENSE_AND_GRAMMAR_NOT_INDEPENDENT_CEFR_APPROVAL"
             and o.get("cambridge_indexed_exact_sense_cefr_lead") == EXPECTED_CEFR_LEADS[w]
             and o.get("line_range") == EXPECTED_LINES.get(w),
             w + ": publisher URL, date, line or index lead drift")
        need(o.get("access") == ("DIRECT_OXFORD_DICTIONARY_PAGE" if direct
             else "CAMBRIDGE_INDEXED_SEARCH_RESULT_DIRECT_PAGE_403"),
             w + ": indexed evidence incorrectly upgraded to direct")
        need("not" in str(o.get("level_note", "")).lower()
             and "automatic" in str(o.get("level_note", "")).lower(),
             w + ": no automatic retiering warning missing")
        need(row.get("editorial_hold") is True
             and row.get("independently_reviewed") is False
             and row.get("release_approved") is False,
             w + ": fabricated independent review or release approval")
        need(len(row.get("editorial_risk", "")) >= 35
             and len(row.get("independent_reviewer_task", "")) >= 35,
             w + ": editorial risk or human task missing")
        candidate = row.get("unapproved_rewrite_candidate", {})
        mm = candidate.get("myanmar_meaning", "")
        ex = candidate.get("original_example", "")
        need(candidate.get("review_status") == "UNAPPROVED_EDITORIAL_PROPOSAL"
             and isinstance(mm, str) and len(mm) >= 10
             and bool(re.search(r"[\u1000-\u109f]", mm))
             and mm != e.get("burmese_meaning"),
             w + ": Myanmar alternative missing or misrepresented as approved")
        need(isinstance(ex, str) and len(ex) >= 18
             and ex != e.get("example_sentence")
             and ex[0].isupper() and ex.endswith((".", "?", "!"))
             and re.search(r"\b" + re.escape(w) + r"[a-z]*\b", ex, re.I),
             w + ": candidate original example grammar/surface form needs review")
    need(seen == set(EXPECTED_URLS), "Research packet headword set incomplete")
    return errors

def mutate_tests(packet, shortlist):
    mutations = 0
    for i, row in enumerate(packet["records"]):
        cases = (
            ("word", "forged"), ("level", "C2"), ("part_of_speech", "forged"),
            ("pair_id", 99), ("pair_word", "forged"),
            ("original.english_definition", "forged"),
            ("original.burmese_meaning", "forged"),
            ("original.example_sentence", "forged"),
            ("provenance.source_path", "forged"),
            ("provenance.source_index", -1),
            ("provenance.source_blob_sha", "0"*40),
            ("publisher_observation.source_url", "https://example.org/fake"),
            ("publisher_observation.observed_on", "2027-01-01"),
            ("publisher_observation.access", "DIRECT_OXFORD_DICTIONARY_PAGE"),
            ("publisher_observation.line_range", [999, 1000]),
            ("publisher_observation.source_scope", "APPROVED"),
            ("publisher_observation.cambridge_indexed_exact_sense_cefr_lead", "C2"),
            ("publisher_observation.level_note", "auto"),
            ("editorial_risk", "forged"),
            ("unapproved_rewrite_candidate.myanmar_meaning", "approved"),
            ("unapproved_rewrite_candidate.original_example", "Forged."),
            ("unapproved_rewrite_candidate.review_status", "APPROVED"),
            ("independent_reviewer_task", "forged"),
            ("editorial_hold", False), ("independently_reviewed", True),
            ("release_approved", True),
        )
        for path, replacement in cases:
            altered = copy.deepcopy(packet)
            dest = altered["records"][i]
            keys = path.split(".")
            for key in keys[:-1]:
                dest = dest[key]
            # If replacement equals original, flip to a distinct value.
            if dest.get(keys[-1]) == replacement:
                replacement = "tampered"
            dest[keys[-1]] = replacement
            if not check(altered, shortlist, baseline=packet, check_disk=False):
                raise AssertionError("Undetected mutation for " + row["word"] + " " + path)
            mutations += 1
    # A forged shortlist approval is also forbidden.
    altered_shortlist = copy.deepcopy(shortlist)
    altered_shortlist["entries"][0]["release_approved"] = True
    if not check(packet, altered_shortlist, baseline=packet, check_disk=False):
        raise AssertionError("Undetected provisional shortlist approval")
    mutations += 1
    return mutations

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=LEVELS + ("ALL",), default="ALL")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    errors = check(packet, shortlist, baseline=packet)
    if errors:
        print("BLOCK: " + "; ".join(errors[:15]), file=sys.stderr)
        return 1
    tested = mutate_tests(packet, shortlist) if args.self_test else 0
    per_level = {k: sum(r["level"] == k for r in packet["records"]) for k in LEVELS}
    result = {"scope": "STAGING_ONLY_NO_DEPLOYMENT", "level": args.level,
              "first_pass_written": dict.fromkeys(LEVELS, 200),
              "independently_approved": dict.fromkeys(LEVELS, 0),
              "identical_myanmar_gloss_pairs": 7,
              "source_bound_entries": per_level if args.level == "ALL" else
                 {args.level: per_level[args.level]},
              "publisher_direct_dictionary_entries": 7,
              "cambridge_search_index_only_entries": 7,
              "mutation_tests_rejected": tested,
              "linguistic_or_cefr_review_approved": False,
              "release_status": "BLOCKED_STAGING_ONLY"}
    path = ROOT / ("cefr-1000-shared-myanmar-gloss-" + args.level + ".json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS: seven identical Myanmar gloss pairs / fourteen held source-linked rows;"
          " 7 Oxford direct dictionary pages; 7 Cambridge indexed-only leads;"
          " no independent approvals; " + str(tested) + " forged mutations rejected")
    return 0

if __name__ == "__main__":
    sys.exit(main())
