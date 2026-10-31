#!/usr/bin/env python3
"""Fail-closed, source-bound integrity checks for the UNAPPROVED CEFR 1000 review handoff.

This compares every exported reviewer field against a freshly rebuilt, frozen
shortlist + independently audited Oxford word/POS research packet snapshot.
It does NOT establish CEFR exact-sense correctness, independent human review,
audio listening, device testing or release approval. It never writes production.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

import audit_cefr_1000_review_priority as handoff
import audit_cefr_1000_oxford_coverage as oxford
import audit_cefr_1000_oxford_legacy_excerpt_recovery as legacy

LEVELS = ("A1", "A2", "B1", "B2", "C1")


def canonical_sha(value):
    return hashlib.sha256(json.dumps(
        value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False
    ).encode("utf-8")).hexdigest()


def verify(candidate, expected):
    """Reject even count-preserving changes, unknown fields, or forged receipts."""
    if not isinstance(candidate, dict):
        raise ValueError("Handoff must be an object")
    handoff.validate(candidate)
    if canonical_sha(candidate) != canonical_sha(expected):
        raise ValueError("Handoff is not byte-content-equivalent to trusted source build")
    return True


def rebuild():
    shortlist, packets = oxford.load()
    recovery, originals = legacy.load()
    report = handoff.build(shortlist, packets, recovery, originals)
    handoff.validate(report)
    return report


def self_test(expected):
    """Exercise tampering at every level, including changes preserving all counts."""
    cases = [
        ("change headword", lambda r: r.update(word="forged-headword")),
        ("change level", lambda r: r.update(draft_level="C2")),
        ("change part of speech", lambda r: r.update(part_of_speech="forged")),
        ("change English definition", lambda r: r.update(english_definition="Forged definition.")),
        ("change Myanmar meaning", lambda r: r.update(myanmar_meaning="အမှား")),
        ("change original example", lambda r: r.update(original_example="Forged example.")),
        ("change historical source path", lambda r: r["shortlist_source"].update(path="draft/fake.json")),
        ("change historical source index", lambda r: r["shortlist_source"].update(index=-1)),
        ("change historical source blob", lambda r: r["shortlist_source"].update(git_blob_sha="0" * 40)),
        ("change reviewer priority", lambda r: r.update(priority_reason="FORGED_PRIORITY")),
        ("remove editorial risk", lambda r: r.update(editorial_risks=[])),
        ("change source packet", lambda r: r.update(evidence_packets=["draft/forged.json"])),
        ("forge exact-sense approval", lambda r: r.update(independent_exact_sense_cefr_signoff={"reviewer": "human"})),
        ("forge bilingual approval", lambda r: r.update(independent_english_myanmar_example_signoff={"reviewer": "human"})),
        ("forge real audio listening", lambda r: r.update(george_emma_real_listening_signoff={"reviewer": "human"})),
        ("forge release approval", lambda r: r.update(release_approved=True)),
        ("inject unknown receipt", lambda r: r.update(independent_reviewed=True)),
        ("forge Oxford level", lambda r: r.update(oxford_word_pos_level="C2")),
        ("forge publisher source URL", lambda r: r["oxford_observation"].update(source_url="https://example.invalid/word.pdf")),
        ("forge publisher observation date", lambda r: r["oxford_observation"].update(observed_on="2099-01-01")),
        ("forge PDF page", lambda r: r["oxford_observation"].update(pdf_page_1_based=999)),
        ("forge PDF line", lambda r: r["oxford_observation"].update(pdf_extracted_line_0_based=999)),
        ("forge source excerpt", lambda r: r["oxford_observation"].update(word_pos_excerpt="fabricated source")),
        ("forge source evidence scope", lambda r: r["oxford_observation"].update(scope="INDEPENDENT_EXACT_SENSE_APPROVAL")),
    ]
    n = 0
    for level in LEVELS:
        index = next(i for i, r in enumerate(expected["review_tasks"])
                     if r["draft_level"] == level and r["oxford_observation"] is not None
                     and isinstance(r["oxford_observation"].get("word_pos_excerpt"), str)
                     and r["oxford_observation"]["word_pos_excerpt"])
        for label, mutation in cases:
            mutated = copy.deepcopy(expected)
            mutation(mutated["review_tasks"][index])
            try:
                verify(mutated, expected)
            except ValueError:
                n += 1
                continue
            raise AssertionError("Tampered %s handoff accepted: %s" % (level, label))
    for level in LEVELS:
        missing = [i for i, r in enumerate(expected["review_tasks"])
                   if r["draft_level"] == level and r["oxford_observation"] is None]
        # Once a level reaches 200/200 direct word/POS observations, there is
        # no missing-source row to mutate. Never invent one for a negative test.
        if not missing:
            if level != "B1":
                raise AssertionError("Unexpected level with zero unobserved entries: " + level)
            continue
        index = missing[0]
        for label, mutation in [
            ("invent publisher observation", lambda r: r.update(oxford_observation={"source_url": "https://example.invalid"})),
            ("invent missing-source priority", lambda r: r.update(priority_reason="WORD_POS_MATCH_EXACT_SENSE_UNVERIFIED")),
        ]:
            mutated = copy.deepcopy(expected)
            mutation(mutated["review_tasks"][index])
            try:
                verify(mutated, expected)
            except ValueError:
                n += 1
                continue
            raise AssertionError("Forged no-source %s handoff accepted: %s" % (level, label))
    global_cases = [
        ("shortlist SHA", lambda x: x.update(source_shortlist_git_blob_sha="0" * 40)),
        ("publisher coverage", lambda x: x.update(publisher_word_pos_observed_distinct=999)),
        ("missing coverage", lambda x: x.update(publisher_word_pos_not_observed=1)),
        ("legacy excerpt count", lambda x: x.update(recovered_legacy_word_pos_excerpts=0)),
        ("priority counts", lambda x: x["priority_counts"].update(NO_DIRECT_WORD_POS_OBSERVATION=0)),
        ("level written counts", lambda x: x["by_level"]["A1"].update(written=199)),
        ("level approval count", lambda x: x["by_level"]["B2"].update(independently_approved=1)),
        ("human approvals", lambda x: x.update(human_independent_approvals=1)),
        ("audio listening signoffs", lambda x: x.update(real_george_emma_listening_signoffs=1)),
        ("release status", lambda x: x.update(release_status="READY_TO_PUBLISH")),
        ("review task removed", lambda x: x["review_tasks"].pop()),
        ("review task duplicated", lambda x: x["review_tasks"].append(copy.deepcopy(x["review_tasks"][0]))),
        ("review task order", lambda x: x["review_tasks"].reverse()),
        ("caveat removed", lambda x: x.update(caveat="")),
        ("unknown top-level field", lambda x: x.update(approval_receipt={"fake": True})),
    ]
    for label, mutation in global_cases:
        mutated = copy.deepcopy(expected)
        mutation(mutated)
        try:
            verify(mutated, expected)
        except ValueError:
            n += 1
            continue
        raise AssertionError("Tampered handoff accepted: " + label)
    return n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    parser.add_argument("--report", help="Compare an exported JSON handoff to rebuilt source truth")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    expected = rebuild()
    if args.report:
        exported = json.loads(Path(args.report).read_text(encoding="utf-8"))
        verify(exported, expected)
    else:
        verify(expected, expected)
    count = self_test(expected) if args.self_test else 0
    print(json.dumps({
        "level": args.level,
        "written": 1000 if args.level == "ALL" else 200,
        "independently_approved": 0,
        "source_bound_handoff": "PASS",
        "export_checked": bool(args.report),
        "forged_handoff_mutations_rejected": count,
        "release": "BLOCKED_STAGING_ONLY",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
