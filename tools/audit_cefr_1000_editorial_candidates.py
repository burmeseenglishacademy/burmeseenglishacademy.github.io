#!/usr/bin/env python3
"""Fail-closed integrity audit for eight editorial candidate rewrites; never reviewer approval."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "draft/CEFR-1000-SENSE-REWRITE-CANDIDATES-2026-10-27.json"
SHORTLIST = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
CAMBRIDGE = ROOT / "draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json"
LEVELS = ("A1", "A2", "B1", "B2", "C1")
EXPECTED = {
    "business": ("A2", "REWRITE_SENSE_ALIGNMENT", "A2 (company, countable)"),
    "attractive": ("B2", "REWRITE_FOR_TARGET_SENSE", "B2 (interesting or beneficial offer)"),
    "appointment": ("B2", "REPLACE_OR_RETIER_REQUIRED", "A2 (arranged meeting); C2 (official job selection)"),
    "hardly": ("B2", "REWRITE_FOR_TARGET_SENSE", "B1 (almost not); B2 (emphatic denial)"),
    "cash": ("B1", "REWRITE_FOR_TARGET_SENSE", "A2 (physical notes and coins); B1 (money in any form)"),
    "prepare": ("B2", "REPLACE_OR_RETIER_REQUIRED", "A2 (get ready); B1 (mentally ready for difficult event)"),
    "implement": ("C1", "REPLACE_OR_RETIER_REQUIRED", "B2 (put plan or system into use)"),
    "upgrade": ("C1", "REPLACE_OR_RETIER_REQUIRED", "B2 (improve or replace with better version)"),
}

def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()

def audit(data, shortlist, raw, cambridge, level="ALL"):
    errors = []
    rows = data.get("records", [])
    if data.get("schema") != 1 or data.get("scope") != "CEFR_1000_TOTAL_A1_TO_C1_STAGING_ONLY":
        errors.append("schema or scope drift")
    if data.get("status") != "PROPOSED_EDITORIAL_REWRITES_NOT_INDEPENDENTLY_REVIEWED":
        errors.append("staging hold status drift")
    if data.get("observed_on") != "2026-10-27":
        errors.append("unsubstantiated observation date change")
    if data.get("shortlist_blob_sha") != git_blob_sha(raw):
        errors.append("canonical shortlist changed: proposals must be refreshed")
    if data.get("record_count") != 8 or len(rows) != 8:
        errors.append("candidate count drift")
    if data.get("independently_approved_count") != 0:
        errors.append("false independent approval count")
    words = [r.get("word") for r in rows]
    if len(set(words)) != 8 or set(words) != set(EXPECTED):
        errors.append("candidate headwords missing, duplicate or unrecognised")
    entries = shortlist.get("entries", [])
    if len(entries) != 1000:
        errors.append("canonical shortlist must contain exactly 1000 entries")
    lookup = {e.get("word"): e for e in entries}
    source_lookup = {e.get("word"): e for e in cambridge.get("records", [])}
    selected = [r for r in rows if level == "ALL" or r.get("level") == level]
    for r in selected:
        word = r.get("word")
        if word not in EXPECTED or word not in lookup or word not in source_lookup:
            errors.append(str(word) + ": no pinned shortlist or publisher triage source")
            continue
        source = lookup[word]
        triage = source_lookup[word]
        if (r.get("level"), r.get("action"), r.get("publisher_cefr_sense")) != EXPECTED[word]:
            errors.append(word + ": proposed level/action/source sense changed")
        if r.get("part_of_speech") != source.get("part_of_speech"):
            errors.append(word + ": part of speech drift")
        for key, src in (("english_definition", "english_definition"),
                         ("myanmar_meaning", "burmese_meaning"),
                         ("example_sentence", "example_sentence")):
            if r.get("original", {}).get(key) != source.get(src):
                errors.append(word + ": original source field drift: " + key)
        evidence = r.get("source", {})
        url = evidence.get("url", "")
        parsed = urlparse(url) if isinstance(url, str) else urlparse("")
        if (parsed.scheme != "https" or parsed.hostname != "dictionary.cambridge.org"
                or word not in parsed.path.split("/") or url != triage.get("source_url")):
            errors.append(word + ": forged or inconsistent publisher source URL")
        if (evidence.get("observed_on") != "2026-10-27"
                or evidence.get("publisher") != "Cambridge University Press & Assessment"
                or "web search" not in evidence.get("access", "").lower()):
            errors.append(word + ": provenance missing or overstated")
        if not isinstance(r.get("diagnosis"), str) or len(r["diagnosis"]) < 35:
            errors.append(word + ": diagnosis missing")
        if not isinstance(r.get("reviewer_task"), str) or len(r["reviewer_task"]) < 30:
            errors.append(word + ": independent reviewer task missing")
        candidate = r.get("candidate", {})
        if r.get("action") == "REPLACE_OR_RETIER_REQUIRED":
            if any(candidate.get(k) is not None for k in ("english_definition", "myanmar_meaning", "example_sentence")):
                errors.append(word + ": unsupported level cannot be silently rewritten")
        else:
            for key in ("english_definition", "myanmar_meaning", "example_sentence"):
                if not isinstance(candidate.get(key), str) or len(candidate[key].strip()) < 12:
                    errors.append(word + ": missing original editorial proposal: " + key)
        if (r.get("editorial_hold") is not True or r.get("independently_approved") is not False
                or r.get("release_approved") is not False or r.get("reviewer_receipt") is not None
                or source.get("editorial_hold") is not True or source.get("release_approved") is not False
                or triage.get("editorial_hold") is not True):
            errors.append(word + ": independent approval/hold bypass")
    return errors, {"level": level, "candidate_records": len(selected), "independently_approved": 0,
                    "status": "EDITORIAL_PROPOSALS_ONLY_DO_NOT_PUBLISH", "errors": errors}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--level", choices=(*LEVELS, "ALL"), default="ALL")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    raw = SHORTLIST.read_bytes()
    shortlist = json.loads(raw)
    data = json.loads(CANDIDATES.read_text(encoding="utf8"))
    cambridge = json.loads(CAMBRIDGE.read_text(encoding="utf8"))
    errors, report = audit(data, shortlist, raw, cambridge, args.level)
    if args.self_test:
        for mutate in (
            lambda d: d.update(independently_approved_count=8),
            lambda d: d["records"][0].update(independently_approved=True),
            lambda d: d["records"][0]["source"].update(url="https://example.org/business"),
            lambda d: d["records"][0]["original"].update(example_sentence="forged"),
            lambda d: d["records"][1]["candidate"].update(english_definition=None),
            lambda d: d["records"][2]["candidate"].update(example_sentence="Unsourced B2 claim"),
            lambda d: d["records"][0].update(publisher_cefr_sense="C2"),
            lambda d: d.update(shortlist_blob_sha="0" * 40),
        ):
            altered = copy.deepcopy(data)
            mutate(altered)
            negative, _ = audit(altered, shortlist, raw, cambridge, "ALL")
            if not negative:
                errors.append("negative test accepted a falsified proposal")
        report["negative_tests"] = "PASS" if not errors else "FAIL"
    report["errors"] = errors
    out = ROOT / ("cefr-1000-editorial-candidates-" + args.level + ".json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + chr(10), encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
