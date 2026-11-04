#!/usr/bin/env python3
"""Fail-closed release gate for BEA CEFR-1000. No approvals inferred from provisional data.

Usage: python3 scripts/cefr1000_release_gate.py --manifest path.json --evidence path.json
Evidence must be supplied separately by genuinely independent reviewers. This gate
checks *presence and consistency*, not the truth of signatures or listening claims.
"""
import argparse
import json
import pathlib
import sys
from collections import Counter

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("english", "myanmar", "example", "cefr")
VOICES = ("george", "emma")
KINDS = ("headword", "example")

def require(ok, message, errors):
    if not ok:
        errors.append(message)

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def check(manifest, evidence):
    errors = []
    entries = manifest.get("entries")
    if not isinstance(entries, list):
        return ["manifest.entries must be an array"]
    require(len(entries) == 1000, "manifest must contain exactly 1000 entries", errors)
    counts = Counter()
    seen = set()
    ids = set()
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry {i} not an object")
            continue
        level = entry.get("level")
        counts[level] += 1
        word = entry.get("word")
        pos = entry.get("part_of_speech")
        sense = entry.get("sense_id")
        key = (str(word).strip().casefold(), str(pos).strip().casefold(), str(sense).strip().casefold())
        require(level in LEVELS, f"entry {i}: invalid CEFR level", errors)
        require(all(isinstance(v, str) and v.strip() for v in (word, pos, sense)), f"entry {i}: missing word/POS/sense_id", errors)
        require(key not in seen, f"entry {i}: duplicate word/POS/sense across levels", errors)
        seen.add(key)
        uid = entry.get("id")
        require(isinstance(uid, str) and bool(uid.strip()), f"entry {i}: missing stable id", errors)
        require(uid not in ids, f"entry {i}: duplicate id", errors)
        ids.add(uid)
        for field in ("english_definition", "burmese_meaning", "example_sentence"):
            require(isinstance(entry.get(field), str) and bool(entry.get(field).strip()), f"entry {i}: missing {field}", errors)
        require(entry.get("release_approved") is True, f"entry {i}: not release-approved", errors)
        require(entry.get("editorial_hold") is False, f"entry {i}: editorial hold not cleared", errors)
    for level in LEVELS:
        require(counts[level] == 200, f"{level}: expected 200, found {counts[level]}", errors)
    require(isinstance(evidence, dict), "evidence must be object", errors)
    if not isinstance(evidence, dict):
        return errors
    reviews = evidence.get("independent_reviews")
    audio = evidence.get("audio")
    if not isinstance(reviews, dict):
        errors.append("missing independent_reviews object")
        reviews = {}
    if not isinstance(audio, dict):
        errors.append("missing audio object")
        audio = {}
    for uid in ids:
        item = reviews.get(uid)
        if not isinstance(item, dict):
            errors.append(f"{uid}: independent reviews missing")
            continue
        for field in FIELDS:
            review = item.get(field)
            if not isinstance(review, dict):
                errors.append(f"{uid}: missing {field} review")
                continue
            for attr in ("reviewer_id", "reviewed_at", "source_url", "source_observed_at", "source_sense", "evidence_reference"):
                require(isinstance(review.get(attr), str) and bool(review[attr].strip()), f"{uid}/{field}: missing {attr}", errors)
            require(review.get("approved") is True, f"{uid}/{field}: not approved", errors)
            require(review.get("independent_of_author") is True, f"{uid}/{field}: independence not attested", errors)
        item_audio = audio.get(uid)
        if not isinstance(item_audio, dict):
            errors.append(f"{uid}: audio evidence missing")
            continue
        for voice in VOICES:
            for kind in KINDS:
                clip = item_audio.get(f"{voice}_{kind}")
                if not isinstance(clip, dict):
                    errors.append(f"{uid}: missing {voice}_{kind} clip")
                    continue
                for attr in ("asset_path", "asset_sha256", "listener_id", "listened_at", "listening_evidence"):
                    require(isinstance(clip.get(attr), str) and bool(clip[attr].strip()), f"{uid}/{voice}_{kind}: missing {attr}", errors)
                require(clip.get("listening_passed") is True, f"{uid}/{voice}_{kind}: no listening pass", errors)
    require(set(reviews) == ids, "review ids do not match manifest exactly", errors)
    require(set(audio) == ids, "audio ids do not match manifest exactly", errors)
    gates = evidence.get("release_gates", {})
    if not isinstance(gates, dict):
        gates = {}
    for gate in ("browser_regression", "mobile_regression", "physical_iphone_safari", "github_pages_limits", "production_deployment", "production_asset_preservation", "privacy_review"):
        g = gates.get(gate)
        require(isinstance(g, dict) and g.get("passed") is True and isinstance(g.get("evidence_url"), str) and bool(g["evidence_url"].strip()) and isinstance(g.get("verified_at"), str) and bool(g["verified_at"].strip()), f"release gate {gate} missing independently documented pass", errors)
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--evidence", required=True)
    args = parser.parse_args()
    try:
        errors = check(load(args.manifest), load(args.evidence))
    except (OSError, ValueError, TypeError) as exc:
        print(f"BLOCKED: cannot read valid input: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"BLOCKED: {len(errors)} release requirements failed")
        for err in errors[:80]:
            print(" -", err)
        if len(errors) > 80:
            print(f" ... {len(errors)-80} more")
        return 1
    print("STRUCTURAL GATE PASS ONLY: verify reviewer identities, actual audio listening, source authenticity, physical devices, hosting and live deployment independently.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
