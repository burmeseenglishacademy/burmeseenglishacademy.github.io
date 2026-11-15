#!/usr/bin/env python3
"""Read-only CEFR-1000 provisional lexical-risk audit; never confers approval.

Usage: python3 scripts/cefr1000_provisional_lexical_audit.py draft/CEFR-1000-PROVISIONAL-SHORTLIST.json
Produces deterministic JSON on stdout. This is a triage tool, not a CEFR classifier.
"""
import argparse
import collections
import json
import pathlib
import re
import unicodedata

LEVELS = ("A1", "A2", "B1", "B2", "C1")
# Inflection/orthographic pairs require human *sense* adjudication, not automatic removal.
ARTICLE_VARIANTS = {"a": "indefinite_article", "an": "indefinite_article"}
HISTORICAL_RISK_TERMS = ("wordnet", "named_entity", "proper_noun", "unsubstantiated")


def canonical(value):
    return unicodedata.normalize("NFKC", value).casefold().strip()


def audit(document):
    entries = document.get("entries")
    if not isinstance(entries, list):
        raise ValueError("entries must be an array")
    counts = collections.Counter()
    by_word = collections.defaultdict(list)
    by_sense = collections.defaultdict(list)
    article = []
    holds = collections.Counter()
    evidence_gaps = {field: collections.Counter() for field in ("sense_id", "source_level", "source_english", "source_burmese")}
    risks = []
    provenance_gaps = collections.Counter()
    draft_text_gaps = {field: collections.Counter() for field in
                       ("english_definition", "burmese_meaning", "example_sentence")}
    source_records = collections.defaultdict(list)
    example_records = collections.defaultdict(list)
    definition_records = collections.defaultdict(list)
    for index, item in enumerate(entries):
        if not isinstance(item, dict):
            risks.append({"index": index, "risk": "malformed_entry"})
            continue
        level, word, pos = item.get("level"), item.get("word"), item.get("part_of_speech")
        if not all(isinstance(x, str) and x.strip() for x in (level, word, pos)):
            risks.append({"index": index, "risk": "missing_level_word_or_pos"})
            continue
        counts[level] += 1
        for field in draft_text_gaps:
            if not isinstance(item.get(field), str) or not item[field].strip():
                draft_text_gaps[field][level] += 1
                risks.append({"index": index, "level": level, "word": word,
                              "risk": "missing_first_pass_text", "field": field})
        for field, bucket in (("example_sentence", example_records),
                              ("english_definition", definition_records)):
            value = item.get(field)
            if isinstance(value, str) and value.strip():
                bucket[canonical(value)].append({"index": index, "level": level, "word": word})
        source_path, source_index, source_sha = (item.get("source_path"),
                                                 item.get("source_index"),
                                                 item.get("source_blob_sha"))
        if not isinstance(source_path, str) or not source_path.startswith("draft/") or (
                ".." in source_path.split("/") or chr(92) in source_path):
            provenance_gaps["invalid_source_path"] += 1
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "invalid_draft_source_path"})
        if type(source_index) is not int or source_index < 0:
            provenance_gaps["invalid_source_index"] += 1
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "invalid_draft_source_index"})
        if not isinstance(source_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", source_sha):
            provenance_gaps["invalid_source_blob_sha"] += 1
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "invalid_draft_source_blob_sha"})
        if isinstance(source_path, str) and type(source_index) is int:
            source_records[(source_path, source_index)].append(
                {"index": index, "level": level, "word": word})
        for field in evidence_gaps:
            if not isinstance(item.get(field), str) or not item[field].strip():
                evidence_gaps[field][level] += 1
        record = {"index": index, "level": level, "word": word, "pos": pos,
                  "source_path": item.get("source_path"), "source_index": item.get("source_index"),
                  "source_blob_sha": item.get("source_blob_sha")}
        normalized = canonical(word)
        if normalized == "i" and canonical(pos) in ("pronoun", "personal pronoun") and word != "I":
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "first_person_pronoun_capitalization", "provenance": record})
        by_word[normalized].append(record)
        sense = item.get("sense_id")
        if isinstance(sense, str) and sense.strip():
            by_sense[(normalized, canonical(pos), canonical(sense))].append(record)
        else:
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "missing_explicit_sense_id", "provenance": record})
        if normalized in ARTICLE_VARIANTS and canonical(pos) == "article":
            article.append(record)
        if item.get("editorial_hold") is not True or item.get("release_approved") is not False:
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "provisional_hold_or_approval_invariant_changed"})
        for flag in ("reviewed_english", "reviewed_burmese", "reviewed_example", "reviewed_level"):
            if item.get(flag) is not False:
                risks.append({"index": index, "level": level, "word": word,
                              "risk": "unexpected_review_flag", "field": flag})
        holds[level] += int(item.get("editorial_hold") is True)
        source_blob = " ".join(str(item.get(k, "")) for k in
                               ("source_path", "source_english", "source_burmese", "status")).casefold()
        if any(term in source_blob for term in HISTORICAL_RISK_TERMS):
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "historical_source_or_named_entity_marker", "provenance": record})
        if re.search(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b", word):
            risks.append({"index": index, "level": level, "word": word,
                          "risk": "possible_multiword_proper_name", "provenance": record})
    duplicates = [v for v in by_word.values() if len(v) > 1]
    duplicate_source_records = [v for v in source_records.values() if len(v) > 1]
    duplicate_senses = [v for v in by_sense.values() if len(v) > 1]
    return {
        "scope": "provisional_1000_only", "classification": "TRIAGE_NOT_INDEPENDENT_REVIEW",
        "entries_observed": len(entries),
        "counts_by_level": {level: counts[level] for level in LEVELS},
        "editorial_holds_by_level": {level: holds[level] for level in LEVELS},
        "provenance_gaps": dict(sorted(provenance_gaps.items())),
        "missing_first_pass_text_by_level": {
            field: {level: values[level] for level in LEVELS}
            for field, values in draft_text_gaps.items()},
        "duplicate_draft_source_records": duplicate_source_records,
        "repeated_example_sentence_groups": [group for group in example_records.values() if len(group) > 1],
        "repeated_english_definition_groups": [group for group in definition_records.values() if len(group) > 1],
        "unknown_levels": {k: v for k, v in sorted(counts.items()) if k not in LEVELS},
        "missing_evidence_by_level": {field: {level: values[level] for level in LEVELS}
                                      for field, values in evidence_gaps.items()},
        "target_200_each_met": len(entries) == 1000 and all(counts[x] == 200 for x in LEVELS),
        "same_normalized_headword_groups": duplicates,
        "same_explicit_word_pos_sense_groups": duplicate_senses,
        "indefinite_article_a_an_review_queue": article if len(article) > 1 else [],
        "risk_queue": risks,
        "warning": "NFKC headword collisions and a/an are review leads only. Repeated draft examples/definitions are triage leads, not proof of error. Distinct senses may be valid; no automatic deletion, CEFR assignment, or approval."
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("shortlist", type=pathlib.Path)
    args = parser.parse_args()
    with args.shortlist.open(encoding="utf-8") as handle:
        report = audit(json.load(handle))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
