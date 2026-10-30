#!/usr/bin/env python3
"""Build a provenance-bound human review handoff for the frozen CEFR 1,000.

Staging-only research queue. Oxford word/POS levels are NOT exact-sense CEFR
approvals. This script never edits the shortlist, creates independent review
receipts, produces audio, or authorises publication.
"""
import argparse
import collections
import copy
import json
from pathlib import Path

import audit_cefr_1000_oxford_coverage as oxford
import audit_cefr_1000_oxford_legacy_excerpt_recovery as legacy

ROOT = Path(__file__).resolve().parents[1]
LEVELS = oxford.LEVELS
STATUS = ("UNLISTED_NOT_A_CEFR_LEVEL", "PUBLISHER_HIGHER_WORD_POS",
          "PUBLISHER_LOWER_WORD_POS", "NO_DIRECT_WORD_POS_OBSERVATION",
          "WORD_POS_MATCH_EXACT_SENSE_UNVERIFIED")
RANK = {s: i for i, s in enumerate(STATUS)}
EXPECTED = {"UNLISTED_NOT_A_CEFR_LEVEL": 3, "PUBLISHER_HIGHER_WORD_POS": 35,
            "PUBLISHER_LOWER_WORD_POS": 232,
            "NO_DIRECT_WORD_POS_OBSERVATION": 324,
            "WORD_POS_MATCH_EXACT_SENSE_UNVERIFIED": 406}
URLS = {
    "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf",
    "https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf",
}

def require(test, message):
    if not test:
        raise ValueError(message)

def classify(draft, observed):
    if observed is None:
        return "NO_DIRECT_WORD_POS_OBSERVATION"
    if observed == "UNLISTED":
        return "UNLISTED_NOT_A_CEFR_LEVEL"
    if observed == draft:
        return "WORD_POS_MATCH_EXACT_SENSE_UNVERIFIED"
    return ("PUBLISHER_HIGHER_WORD_POS" if LEVELS.index(observed) > LEVELS.index(draft)
            else "PUBLISHER_LOWER_WORD_POS")

def build(shortlist, packets, recovery, originals):
    checked = oxford.audit(shortlist, packets)
    recovered = legacy.audit(recovery, originals)
    require(recovered["recovered_direct_publisher_excerpt_lines"] == 36,
            "Recovery auditor did not verify 36 legacy observations")
    by_recovery = {(r["draft_level"], r["word"]): r for r in recovery["records"]}
    require(len(by_recovery) == 36, "Repeated recovered word/level")
    by_word = {}
    for draft, names in oxford.PACKETS.items():
        for name in names:
            path = oxford.PREFIX + name + ".json"
            packet = packets[path]
            for row in packet["records"]:
                word = row["word"]
                observed, snapshot, provenance, locator_only = oxford.normalize(row)
                publisher = row.get("publisher_source")
                url = publisher.get("url") if publisher else row.get("source_url")
                date = publisher.get("observed_on") if publisher else row.get("observed_on")
                page = publisher.get("pdf_page") if publisher else row.get("pdf_page_1_based")
                line = publisher.get("extracted_line") if publisher else row.get("pdf_extracted_line_0_based")
                excerpt = publisher.get("source_excerpt") if publisher else row.get("source_entry")
                if locator_only:
                    supplement = by_recovery.get((draft, word))
                    require(supplement is not None, "Unrecovered historical PDF locator: " + word)
                    require(supplement["source_url"] == url
                            and supplement["pdf_page_1_based"] == page
                            and supplement["pdf_extracted_line_0_based"] == line
                            and supplement["oxford_word_pos_level"] == observed,
                            "Recovered source does not bind to historical locator: " + word)
                    excerpt = supplement["source_excerpt"]
                    date = supplement["observed_on"]
                if observed != "UNLISTED":
                    require(url in URLS and type(page) is int and type(line) is int
                            and isinstance(excerpt, str) and excerpt.strip(),
                            "Publisher excerpt/locator incomplete: " + word)
                evidence = {"publisher": "Oxford University Press",
                            "source_url": url, "observed_on": date,
                            "pdf_page_1_based": page, "pdf_extracted_line_0_based": line,
                            "word_pos_excerpt": excerpt,
                            "scope": "WORD_POS_ONLY_NOT_EXACT_SENSE"}
                if word not in by_word:
                    by_word[word] = {"observed": observed, "evidence": evidence,
                                     "packets": [path], "recovered_legacy": bool(locator_only),
                                     "editorial_risks": [row["editorial_risk"]]}
                else:
                    prior = by_word[word]
                    require(prior["observed"] == observed, "Conflicting duplicate Oxford level")
                    prior["packets"].append(path)
                    prior["recovered_legacy"] |= bool(locator_only)
                    prior["editorial_risks"].append(row["editorial_risk"])
    require(len(by_word) == checked["distinct_observed_headwords"] == 676,
            "Coverage and review handoff disagree")
    require(sum(x["recovered_legacy"] for x in by_word.values()) == 36,
            "Exactly 36 unique historical recoveries expected")
    rows = []
    for entry in shortlist["entries"]:
        word, draft = entry["word"], entry["level"]
        source = by_word.get(word)
        observed = source["observed"] if source else None
        status = classify(draft, observed)
        require(entry["editorial_hold"] is True and entry["release_approved"] is False
                and all(entry.get("reviewed_" + k) is False for k in
                        ("english", "burmese", "example", "level", "pronunciation")),
                "Shortlist entry has unverified or forged approval: " + word)
        rows.append({
            "word": word, "draft_level": draft,
            "part_of_speech": entry["part_of_speech"],
            "english_definition": entry["english_definition"],
            "myanmar_meaning": entry["burmese_meaning"],
            "original_example": entry["example_sentence"],
            "shortlist_source": {"path": entry["source_path"],
                                 "index": entry["source_index"],
                                 "git_blob_sha": entry["source_blob_sha"]},
            "priority_reason": status,
            "oxford_word_pos_level": observed,
            "oxford_observation": source["evidence"] if source else None,
            "evidence_packets": source["packets"] if source else [],
            "editorial_risks": sorted(set(source["editorial_risks"])) if source else
                               ["No direct Oxford word/POS observation in audited packets"],
            "historical_locator_excerpt_recovered": source["recovered_legacy"] if source else False,
            "independent_exact_sense_cefr_signoff": None,
            "independent_english_myanmar_example_signoff": None,
            "george_emma_real_listening_signoff": None,
            "release_approved": False,
        })
    rows.sort(key=lambda r: (RANK[r["priority_reason"]], LEVELS.index(r["draft_level"]), r["word"]))
    counts = collections.Counter(r["priority_reason"] for r in rows)
    require(dict(counts) == EXPECTED, "Unexpected publisher coverage priority counts")
    by_level = {level: {"written": 200, "independently_approved": 0,
                        "priority_counts": dict(collections.Counter(
                            r["priority_reason"] for r in rows if r["draft_level"] == level))}
                for level in LEVELS}
    require(all(sum(x["priority_counts"].values()) == 200 for x in by_level.values()),
            "Level-specific review handoff is incomplete")
    return {
        "schema": 1, "scope": "CEFR_1000_STAGING_ONLY_NOT_A_RELEASE_MANIFEST",
        "source_shortlist_git_blob_sha": oxford.SHORTLIST_SHA,
        "publisher_word_pos_observed_distinct": 676,
        "publisher_word_pos_not_observed": 324,
        "recovered_legacy_word_pos_excerpts": 36,
        "priority_counts": dict(counts), "by_level": by_level,
        "human_independent_approvals": 0,
        "real_george_emma_listening_signoffs": 0,
        "release_status": "BLOCKED_STAGING_ONLY",
        "caveat": "Oxford word/POS lists cannot independently verify exact sense, fluent Myanmar, original example grammar or pronunciation. Missing from lists is not a CEFR label. No reviewer receipts or real listening evidence exist in this handoff.",
        "review_tasks": rows,
    }

def self_test(report):
    cases = [
        ("fake exact-sense receipt", lambda x: x["review_tasks"][0].update(
            independent_exact_sense_cefr_signoff={"reviewer": "fake"})),
        ("fake listening receipt", lambda x: x["review_tasks"][0].update(
            george_emma_real_listening_signoff={"reviewer": "fake"})),
        ("fake release approval", lambda x: x["review_tasks"][0].update(release_approved=True)),
        ("wrong 1,000 count", lambda x: x["review_tasks"].pop()),
        ("false publisher observation", lambda x: x["publisher_word_pos_observed_distinct"].__class__),
    ]
    # Last mutation is implemented explicitly to avoid modifying immutable ints in place.
    cases[-1] = ("false publisher count", lambda x: x.update(publisher_word_pos_observed_distinct=306))
    for label, mutate in cases:
        test = copy.deepcopy(report)
        mutate(test)
        try:
            validate(test)
        except ValueError:
            continue
        raise AssertionError("Forged review handoff accepted: " + label)
    return len(cases)

def validate(report):
    rows = report["review_tasks"]
    require(len(rows) == 1000 and len({r["word"] for r in rows}) == 1000,
            "Review queue must contain 1,000 distinct headwords")
    require(report["publisher_word_pos_observed_distinct"] == 676
            and report["publisher_word_pos_not_observed"] == 324
            and report["recovered_legacy_word_pos_excerpts"] == 36
            and report["human_independent_approvals"] == 0
            and report["real_george_emma_listening_signoffs"] == 0
            and report["release_status"] == "BLOCKED_STAGING_ONLY",
            "Forged release evidence or coverage count")
    require(dict(collections.Counter(r["priority_reason"] for r in rows)) == EXPECTED,
            "Priority counts drift")
    for r in rows:
        require(r["release_approved"] is False
                and r["independent_exact_sense_cefr_signoff"] is None
                and r["independent_english_myanmar_example_signoff"] is None
                and r["george_emma_real_listening_signoff"] is None,
                "Fabricated human approval/listening receipt")
        require(r["priority_reason"] == classify(r["draft_level"], r["oxford_word_pos_level"]),
                "Incorrect publisher word/POS discrepancy classification")
        if r["oxford_word_pos_level"] is None:
            require(r["oxford_observation"] is None and not r["evidence_packets"],
                    "Manufactured Oxford source observation")
        else:
            require(r["oxford_observation"] is not None and r["evidence_packets"],
                    "Source provenance missing")
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", help="Write full unapproved human-review handoff JSON (CI artifact only)")
    args = parser.parse_args()
    shortlist, packets = oxford.load()
    recovery, originals = legacy.load()
    report = build(shortlist, packets, recovery, originals)
    validate(report)
    if args.self_test:
        n = self_test(report)
        print("PASS: %d/%d fabricated-review/coverage mutations rejected" % (n, n))
    if args.output:
        Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8")
    print(json.dumps({"level": args.level,
                      "counts": report["by_level"][args.level] if args.level != "ALL"
                      else report["priority_counts"],
                      "independently_approved": 0, "release": "BLOCKED_STAGING_ONLY"},
                     sort_keys=True))

if __name__ == "__main__":
    main()
