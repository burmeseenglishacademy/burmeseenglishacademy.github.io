#!/usr/bin/env python3
"""Fail-closed structural/provenance audit for six Cambridge B2 source leads.
No source observation or test constitutes independent editorial approval.
"""
import argparse
import copy
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "draft/CEFR-1000-CAMBRIDGE-B2-SIX-SENSE-LEADS-2026-10-28.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
EXPECTED = {
    "absolute": ("B2", "https://dictionary.cambridge.org/dictionary/english/absolute", "B2"),
    "constant": ("B2", "https://dictionary.cambridge.org/dictionary/english/constant", "B2 frequent; C2 staying same"),
    "relief": ("B2", "https://dictionary.cambridge.org/dictionary/learner-english/relief", "B2"),
    "client": ("B2", "https://dictionary.cambridge.org/us/dictionary/english/client", "B2"),
    "decade": ("B2", "https://dictionary.cambridge.org/dictionary/english/decade", "B2"),
    "quit": ("B2", "https://dictionary.cambridge.org/dictionary/english/quit", "B1"),
}
LEVELS = ("A1", "A2", "B1", "B2", "C1")


def audit(evidence, shortlist, level):
    problems = []
    import hashlib
    # GitHub Git blob SHA-1, NOT SHA-1 of file bytes.
    b = SHORTLIST.read_bytes()
    git_sha = hashlib.sha1(b"blob " + str(len(b)).encode("ascii") + bytes([0]) + b).hexdigest()
    if evidence.get("shortlist_blob_sha") != git_sha:
        problems.append("Pinned canonical shortlist Git blob SHA differs")
    if evidence.get("scope") != "CEFR_1000_TOTAL_STAGING_ONLY":
        problems.append("Unexpected scope")
    if evidence.get("observed_on") != "2026-10-28":
        problems.append("Observation date drift")
    if evidence.get("record_count") != 6 or evidence.get("independently_approved_count") != 0:
        problems.append("False count/approval claim")
    if evidence.get("counts_by_level") != {"A1": 0, "A2": 0, "B1": 0, "B2": 6, "C1": 0}:
        problems.append("Per-level count mismatch")
    if len(shortlist.get("entries", [])) != 1000:
        problems.append("Canonical shortlist no longer 1000 entries")
    if shortlist.get("independently_approved_by_level") != {k: 0 for k in LEVELS}:
        problems.append("Independent approval baseline has changed; require separate human review verification")
    originals = {(r.get("level"), r.get("word")): r for r in shortlist.get("entries", [])}
    records = evidence.get("records", [])
    if not isinstance(records, list) or len(records) != 6:
        return problems + ["Six source records required"]
    seen = set()
    for r in records:
        if not isinstance(r, dict):
            problems.append("Invalid record object")
            continue
        w = r.get("word")
        if w not in EXPECTED or w in seen:
            problems.append("Unexpected/duplicate headword " + str(w))
            continue
        seen.add(w)
        expected_level, url, cefr = EXPECTED[w]
        if r.get("level") != expected_level:
            problems.append(w + ": draft CEFR level drift")
        source = r.get("publisher_source", {})
        if not isinstance(source, dict):
            source = {}
        if source.get("url") != url or source.get("source_cefr_level") != cefr:
            problems.append(w + ": publisher URL or sense-level label drift")
        if source.get("observed_on") != "2026-10-28" or source.get("publisher") != "Cambridge University Press & Assessment":
            problems.append(w + ": provenance date/publisher drift")
        if source.get("access") != "PUBLISHER_OWNED_SEARCH_INDEXED_PAGE_TEXT_DIRECT_FETCH_HTTP_403":
            problems.append(w + ": unsupported direct-source claim")
        if source.get("observation_scope") != "PUBLISHER_SEARCH_RESULT_SENSE_LABEL_NOT_INDEPENDENT_HUMAN_REVIEW":
            problems.append(w + ": unsupported independent-source claim")
        if not source.get("source_sense_heading"):
            problems.append(w + ": missing sense heading")
        original = originals.get((expected_level, w))
        if not original:
            problems.append(w + ": absent from canonical shortlist")
            continue
        expected_snapshot = {
            "english_definition": original.get("english_definition"),
            "myanmar_meaning": original.get("burmese_meaning"),
            "example_sentence": original.get("example_sentence"),
        }
        if r.get("shortlist_snapshot") != expected_snapshot or r.get("part_of_speech") != original.get("part_of_speech"):
            problems.append(w + ": original bilingual/example/POS snapshot drift")
        if any(r.get(k) is not False for k in ("independently_reviewed", "release_approved")):
            problems.append(w + ": forged review/approval flag")
        if r.get("editorial_hold") is not True or r.get("independent_reviewer_receipt") is not None:
            problems.append(w + ": review hold or receipt bypass")
        if original.get("editorial_hold") is not True or original.get("release_approved") is not False:
            problems.append(w + ": canonical entry unexpectedly approved")
        if not r.get("editorial_risk") or not r.get("independent_reviewer_task"):
            problems.append(w + ": missing editorial task")
    if seen != set(EXPECTED):
        problems.append("Missing source headword(s)")
    return problems


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    shortlist = json.loads(SHORTLIST.read_text(encoding="utf-8"))
    issues = audit(evidence, shortlist, args.level)
    if args.self_test:
        mutants = []
        for key, value in [
            ("independently_reviewed", True),
            ("release_approved", True),
            ("editorial_hold", False),
            ("independent_reviewer_receipt", {"reviewer_id": "FAKE"}),
        ]:
            m = copy.deepcopy(evidence)
            m["records"][0][key] = value
            mutants.append(m)
        for field, value in [
            ("url", "https://example.invalid/forged"),
            ("source_cefr_level", "C1"),
            ("access", "DIRECT_PUBLISHER_PAGE_VERIFIED"),
            ("observed_on", "2026-10-01"),
        ]:
            m = copy.deepcopy(evidence)
            m["records"][0]["publisher_source"][field] = value
            mutants.append(m)
        m = copy.deepcopy(evidence)
        m["records"][0]["shortlist_snapshot"]["myanmar_meaning"] = "FAKE"
        mutants.append(m)
        m = copy.deepcopy(evidence)
        m["records"][0]["word"] = "decade"
        mutants.append(m)
        for i, mutant in enumerate(mutants):
            if not audit(mutant, shortlist, "ALL"):
                issues.append(f"Negative test {i} accepted forged evidence")
        if not issues:
            print("PASS: ten false-source, false-approval and draft-drift mutations rejected")
    relevant = sum(r.get("level") == args.level for r in evidence["records"]) if args.level != "ALL" else len(evidence["records"])
    report = {"level": args.level, "publisher_indexed_observations": relevant,
              "independently_approved": 0, "editorial_hold": relevant,
              "errors": issues, "source_access": "search-indexed; direct 403",
              "is_independent_review": False}
    output = ROOT / f"cefr-1000-cambridge-b2-six-{args.level}.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
    print(f"Cambridge B2 six source leads: {relevant} in {args.level}, independent approvals 0, issues {len(issues)}")
    for issue in issues:
        print("BLOCK:", issue, file=sys.stderr)
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
