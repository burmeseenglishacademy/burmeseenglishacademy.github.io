#!/usr/bin/env python3
"""Audit CEFR editorial evidence without claiming linguistic verification.

Read-only input. Output is a structured, unpublished reviewer work queue.
A successful audit means *the audit ran*, NOT that words are release-ready.
"""
import argparse
import collections
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REVIEW_KEYS = ("reviewed_english", "reviewed_burmese", "reviewed_example",
               "reviewed_level", "reviewed_pronunciation")
TARGETS = {"A1": 500, "A2": 700, "B1": 1000, "B2": 1300, "C1": 1500}
MYANMAR = re.compile(r"[\u1000-\u109f\uaa60-\uaa7f]")
HEADWORD = re.compile(r"[a-z]+(?:'[a-z]+)?", re.ASCII)


def reference_is_specific(value):
    """Only structural specificity: a word-specific URL may still be wrong."""
    if not isinstance(value, str) or not value.startswith("https://"):
        return False
    parts = urlparse(value)
    path = parts.path.strip("/").lower()
    generic = {
        "", "about/wordlists/oxford3000-5000", "wordlists",
        "english", "dictionary", "learner", "grammar", "free-resources",
        "license-and-commercial-use",
    }
    if path in generic:
        return False
    if parts.netloc.endswith("oxfordlearnersdictionaries.com") and path.startswith("about/wordlists/"):
        return False
    return True


def audit(a1, candidates):
    severe = []
    warnings = []
    review_queue = []
    entries = a1.get("entries", [])
    pool = candidates.get("entries", [])
    if a1.get("release_status") != "UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        severe.append("A1 draft must remain explicitly UNVERIFIED")
    if candidates.get("release_status") != "UNVERIFIED_DRAFT_DO_NOT_PUBLISH":
        severe.append("Candidate corpus must remain explicitly UNVERIFIED")
    if len(entries) != 500:
        severe.append("Expected exactly 500 A1 editorial drafts")
    if len(pool) != 5000:
        severe.append("Expected exactly 5000 provisional word candidates")
    levels = dict(collections.Counter(row.get("level") for row in pool))
    if levels != TARGETS:
        severe.append("Expected A1/A2/B1/B2/C1 counts do not match")
    pool_lookup = {row.get("word"): row for row in pool}
    if len(pool_lookup) != len(pool):
        severe.append("Duplicate headwords in candidate corpus")
    seen = set()
    per_issue = collections.Counter()
    for row in entries:
        word = row.get("word", "")
        issues = []
        if not HEADWORD.fullmatch(word):
            issues.append("INVALID_HEADWORD")
        if word in seen:
            issues.append("DUPLICATE_A1_HEADWORD")
        seen.add(word)
        if row.get("level") != "A1":
            issues.append("WRONG_A1_LABEL")
        linked = pool_lookup.get(word)
        if not linked or linked.get("level") != "A1":
            issues.append("NOT_IN_A1_CANDIDATES")
        if linked and linked.get("editorial_burmese_meaning_draft") != row.get("burmese_meaning"):
            issues.append("CANDIDATE_DRAFT_MISMATCH")
        if not row.get("english_definition") or not row.get("example_sentence"):
            issues.append("ENGLISH_OR_EXAMPLE_MISSING")
        if not MYANMAR.search(row.get("burmese_meaning", "")):
            issues.append("BURMESE_SCRIPT_MISSING")
        for field in ("english_definition", "burmese_meaning", "example_sentence"):
            value = row.get(field, "")
            if unicodedata.normalize("NFC", value) != value:
                issues.append("UNICODE_NORMALIZATION_" + field.upper())
        if not reference_is_specific(row.get("source_level_reference")):
            issues.append("CEFR_LEVEL_SOURCE_NOT_WORD_SPECIFIC")
        if not reference_is_specific(row.get("source_english_reference")):
            issues.append("ENGLISH_SOURCE_NOT_SENSE_SPECIFIC")
        if "pending" in row.get("source_burmese_reference", "").lower() or not reference_is_specific(row.get("source_burmese_reference")):
            issues.append("INDEPENDENT_BURMESE_EVIDENCE_MISSING")
        if any(row.get(flag) is not False for flag in REVIEW_KEYS):
            severe.append("Review flags must remain false until independent checks: " + word)
        if row.get("status") != "DRAFT_PENDING_INDEPENDENT_REVIEW":
            severe.append("Incorrect unreviewed status: " + word)
        for issue in issues:
            per_issue[issue] += 1
        review_queue.append({
            "word": word,
            "level": "A1_PROVISIONAL",
            "editorial_issues": issues,
            "must_review": list(REVIEW_KEYS),
            "status": "NOT_APPROVED_FOR_LEARNERS",
        })
    missing_burmese = sum(not x.get("burmese_meaning") for x in pool)
    missing_examples = sum(not x.get("example_sentence") for x in pool)
    independently_approved = sum(all(x.get(field) is True for field in REVIEW_KEYS) for x in entries)
    if independently_approved:
        severe.append("Unreviewed corpus contains incorrectly approved A1 records")
    if len(seen) != len(entries):
        severe.append("A1 duplicates detected")
    if len(seen - set(pool_lookup)):
        severe.append("A1 words absent in candidate inventory")
    if len(entries) != 500 or len(pool) != 5000:
        warnings.append("Input file coverage incomplete")
    return {
        "classification": "STAGING_ONLY_NOT_A_LINGUISTIC_APPROVAL",
        "release_ready": False,
        "a1_draft_count": len(entries),
        "total_candidate_count": len(pool),
        "candidate_level_counts": levels,
        "provisional_candidates_missing_burmese": missing_burmese,
        "provisional_candidates_missing_example": missing_examples,
        "a1_independently_approved_records": independently_approved,
        "issue_counts": dict(sorted(per_issue.items())),
        "fatal_invariant_violations": severe,
        "warnings": warnings,
        "a1_review_queue": review_queue,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "draft/CEFR-EVIDENCE-REVIEW-QUEUE.json")
    parser.add_argument("--require-release", action="store_true",
                        help="Fail if learner publication is not independently verified")
    args = parser.parse_args()
    a1 = json.loads((ROOT / "draft/A1-EDITORIAL-STARTER.json").read_text("utf8"))
    candidates = json.loads((ROOT / "draft/UNVERIFIED_CEFR_CANDIDATES.json").read_text("utf8"))
    result = audit(a1, candidates)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", "utf8")
    print("A1 drafted:", result["a1_draft_count"])
    print("CEFR candidates:", result["total_candidate_count"])
    print("Independent editorial approvals:", result["a1_independently_approved_records"])
    print("Missing Burmese translations in candidate pool:", result["provisional_candidates_missing_burmese"])
    print("Issues:", json.dumps(result["issue_counts"], sort_keys=True))
    print("Release ready:", result["release_ready"])
    if result["fatal_invariant_violations"]:
        print("INTEGRITY FAIL:", *result["fatal_invariant_violations"][:20], sep="\n")
        raise SystemExit(1)
    if args.require_release and not result["release_ready"]:
        print("BLOCK: editorial evidence and finished audio are not independently approved")
        raise SystemExit(1)
    print("PASS: report created; NOT A RELEASE APPROVAL")


if __name__ == "__main__":
    main()
