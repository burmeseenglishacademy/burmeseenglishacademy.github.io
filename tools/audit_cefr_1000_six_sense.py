#!/usr/bin/env python3
"""Fail-closed integrity check of six indexed publisher sense leads; NOT independent review."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "draft/CEFR-1000-CAMBRIDGE-SIX-SENSE-LEADS-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
ACCESS = "SEARCH_INDEXED_PUBLISHER_PAGE_NOT_DIRECT_FETCH"
EXPECTED = {
    "independent": ("B1", "INFLUENCE", "B2", "SENSE_LEVEL_CONFLICT", "learner-english"),
    "impact": ("B1", "EFFECT", "B2", "SENSE_LEVEL_CONFLICT", "learner-english"),
    "retail": ("B2", "NOUN_SELLING_TO_PUBLIC", "C1", "SENSE_LEVEL_CONFLICT", "english"),
    "resistance": ("B2", "OPPOSITION_REFUSAL", "C2", "SENSE_LEVEL_CONFLICT", "english"),
    "personality": ("B2", "CHARACTER", "B2", "SENSE_LEVEL_MATCH", "english"),
    "municipal": ("C1", "TOWN_OR_CITY", "C1", "SENSE_LEVEL_MATCH", "english"),
}

def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()

def audit(data, shortlist, raw, level):
    errors = []
    if data.get("schema") != 1 or data.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY":
        errors.append("schema/scope drift")
    if data.get("status") != "SOURCE_INDEXED_EDITORIAL_LEADS_UNVERIFIED_HUMAN_REVIEW":
        errors.append("editorial hold status drift")
    if data.get("observed_on") != "2026-10-27":
        errors.append("observation date drift")
    if data.get("shortlist_blob_sha") != git_blob_sha(raw):
        errors.append("shortlist content changed; rebase publisher observations")
    if data.get("independently_approved_count") != 0:
        errors.append("false independent approval total")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000:
        errors.append("expected 1000 provisional entries")
    lookup = {(e.get("word"), e.get("level")): e for e in entries if isinstance(e, dict)}
    rows = data.get("records", [])
    if not isinstance(rows, list) or len(rows) != 6 or data.get("record_count") != 6:
        errors.append("expected exactly six source observations")
        rows = rows if isinstance(rows, list) else []
    words = [r.get("word") for r in rows if isinstance(r, dict)]
    if len(words) != 6 or set(words) != set(EXPECTED):
        errors.append("missing, duplicate or unexpected source headword")
    counts = {k: sum(1 for r in rows if isinstance(r, dict) and r.get("level") == k) for k in LEVELS}
    if data.get("counts_by_level") != counts or counts != {"A1":0,"A2":0,"B1":2,"B2":3,"C1":1}:
        errors.append("per-level source observation count drift")
    for r in rows:
        if not isinstance(r, dict):
            errors.append("invalid source observation type")
            continue
        word = r.get("word")
        if word not in EXPECTED:
            continue
        expected_level, sense, cefr, assessment, section = EXPECTED[word]
        if r.get("level") != expected_level or r.get("assessment") != assessment:
            errors.append(word + ": level/assessment drift")
        original = lookup.get((word, expected_level))
        if original is None:
            errors.append(word + ": missing exact source shortlist entry")
            continue
        if r.get("part_of_speech") != original.get("part_of_speech"):
            errors.append(word + ": POS drift")
        snapshot = r.get("shortlist_snapshot", {})
        if not isinstance(snapshot, dict) or any(
            snapshot.get(dst) != original.get(src) for dst, src in (
                ("english_definition", "english_definition"),
                ("burmese_meaning", "burmese_meaning"),
                ("example_sentence", "example_sentence"))):
            errors.append(word + ": bilingual definition/example no longer matches shortlist")
        source = r.get("publisher_source", {})
        expected_url = "https://dictionary.cambridge.org/dictionary/" + section + "/" + word
        if not isinstance(source, dict) or (
            source.get("url") != expected_url
            or source.get("observed_on") != "2026-10-27"
            or source.get("publisher") != "Cambridge University Press & Assessment"
            or source.get("access") != ACCESS
            or source.get("source_sense_heading") != sense
            or source.get("source_cefr_level") != cefr
            or source.get("observation_scope") != "PUBLISHER_INDEXED_SENSE_LABEL_NOT_HUMAN_REVIEW"):
            errors.append(word + ": source URL/sense/CEFR/provenance mismatch")
        for field in ("editorial_diagnosis", "independent_reviewer_task"):
            if not isinstance(r.get(field), str) or len(r[field].strip()) < 40:
                errors.append(word + ": missing substantive reviewer context " + field)
        if (r.get("editorial_hold") is not True
            or r.get("independently_approved") is not False
            or r.get("release_approved") is not False
            or r.get("independent_reviewer_receipt") is not None
            or original.get("editorial_hold") is not True
            or original.get("release_approved") is not False):
            errors.append(word + ": false approval or editorial hold bypass")
    selected = [r for r in rows if isinstance(r, dict) and (level == "ALL" or r.get("level") == level)]
    return errors, {
        "level": level, "indexed_source_observations": len(selected),
        "conflict_leads": sum(r.get("assessment") == "SENSE_LEVEL_CONFLICT" for r in selected),
        "independently_approved": 0,
        "source_access": ACCESS,
        "status": "STAGING_SOURCE_LEADS_NOT_INDEPENDENTLY_REVIEWED",
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    data = json.loads(SOURCE.read_text(encoding="utf8"))
    errors, report = audit(data, shortlist, raw, args.level)
    if args.self_test:
        mutations = (
            lambda d: d.update(independently_approved_count=1),
            lambda d: d["records"][0].update(independently_approved=True),
            lambda d: d["records"][0]["publisher_source"].update(source_cefr_level="B1"),
            lambda d: d["records"][1]["publisher_source"].update(access="DIRECT_PUBLISHER_DICTIONARY_PAGE"),
            lambda d: d["records"][2]["publisher_source"].update(url="https://example.org/retail"),
            lambda d: d["records"][3]["shortlist_snapshot"].update(example_sentence="Falsified example."),
            lambda d: d["records"].append(copy.deepcopy(d["records"][0])),
            lambda d: d.update(shortlist_blob_sha="0" * 40),
            lambda d: d["records"][4].update(release_approved=True),
        )
        for mutate in mutations:
            altered = copy.deepcopy(data)
            mutate(altered)
            negative, _ = audit(altered, shortlist, raw, "ALL")
            if not negative:
                errors.append("negative test accepted forged source or approval")
        report["negative_tests"] = "PASS" if not errors else "FAIL"
    report["errors"] = errors
    output = ROOT / ("cefr-1000-cambridge-six-sense-" + args.level + ".json")
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
