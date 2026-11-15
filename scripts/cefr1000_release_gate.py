#!/usr/bin/env python3
"""Fail-closed release gate for BEA CEFR-1000. No approvals inferred from provisional data.

Usage: python3 scripts/cefr1000_release_gate.py --manifest path.json --evidence path.json
Evidence must be supplied separately by genuinely independent reviewers. This gate
checks *presence and consistency*, not the truth of signatures or listening claims.
"""
import argparse
import json
import pathlib
import re
import sys
from datetime import datetime, timezone
from urllib.parse import urlsplit
from collections import Counter

LEVELS = ("A1", "A2", "B1", "B2", "C1")
FIELDS = ("english", "myanmar", "example", "cefr")
VOICES = ("george", "emma")
KINDS = ("headword", "example")


def https_evidence_url(value):
    """Check URL syntax, not the authenticity or content of evidence."""
    if not isinstance(value, str) or any(ch.isspace() for ch in value):
        return False
    try:
        parsed = urlsplit(value)
        return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password
    except ValueError:
        return False


def iso_timestamp(value):
    """Require an actual timezone-aware ISO-8601 instant, not arbitrary text."""
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.tzinfo is not None and parsed.utcoffset() is not None
    except ValueError:
        return False


def safe_relative_asset_path(value):
    """Reject traversal, absolute paths, URL strings and Windows separators."""
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    parts = pathlib.PurePosixPath(value)
    return not parts.is_absolute() and all(p not in (".", "..") for p in value.split("/")) and not value.startswith("/") and "://" not in value


def sha256_hex(value):
    """Require a digest-shaped string; only file-byte comparison verifies integrity."""
    return isinstance(value, str) and re.fullmatch(r"[a-fA-F0-9]{64}", value) is not None


def require(ok, message, errors):
    if not ok:
        errors.append(message)

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def check(manifest, evidence):
    errors = []
    if not isinstance(manifest, dict):
        return ["manifest must be an object"]
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
        if isinstance(level, str):
            counts[level] += 1
        else:
            errors.append(f"entry {i}: level must be a string")
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
        require(isinstance(uid, str) and uid not in ids, f"entry {i}: duplicate id", errors)
        if isinstance(uid, str):
            ids.add(uid)
        for provenance in ("source_path", "source_blob_sha", "source_index"):
            require(provenance in entry, f"entry {i}: missing provenance {provenance}", errors)
        require(safe_relative_asset_path(entry.get("source_path")), f"entry {i}: source_path invalid", errors)
        require(isinstance(entry.get("source_blob_sha"), str) and re.fullmatch(r"[a-fA-F0-9]{40}", entry["source_blob_sha"]) is not None, f"entry {i}: source_blob_sha invalid", errors)
        require(type(entry.get("source_index")) is int and entry["source_index"] >= 0, f"entry {i}: source_index invalid", errors)
        for field in ("english_definition", "burmese_meaning", "example_sentence"):
            require(isinstance(entry.get(field), str) and bool(entry.get(field).strip()), f"entry {i}: missing {field}", errors)
        require(entry.get("release_approved") is True, f"entry {i}: not release-approved", errors)
        require(entry.get("editorial_hold") is False, f"entry {i}: editorial hold not cleared", errors)
    for level in LEVELS:
        require(counts[level] == 200, f"{level}: expected 200, found {counts[level]}", errors)
    require(isinstance(evidence, dict), "evidence must be object", errors)
    if not isinstance(evidence, dict):
        return errors
    release_sha = evidence.get("release_commit_sha")
    require(isinstance(release_sha, str) and re.fullmatch(r"[a-fA-F0-9]{40}", release_sha) is not None, "release_commit_sha must be a full 40-character Git SHA", errors)
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
            require(https_evidence_url(review.get("source_url")), f"{uid}/{field}: source_url must be valid HTTPS", errors)
            require(iso_timestamp(review.get("reviewed_at")) and iso_timestamp(review.get("source_observed_at")), f"{uid}/{field}: invalid review/source observation timestamp", errors)
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
                require(safe_relative_asset_path(clip.get("asset_path")), f"{uid}/{voice}_{kind}: unsafe asset_path", errors)
                require(iso_timestamp(clip.get("listened_at")), f"{uid}/{voice}_{kind}: invalid listened_at timestamp", errors)
                require(sha256_hex(clip.get("asset_sha256")), f"{uid}/{voice}_{kind}: asset_sha256 must contain 64 hex digits", errors)
                require(clip.get("listening_passed") is True, f"{uid}/{voice}_{kind}: no listening pass", errors)
    require(set(reviews) == ids, "review ids do not match manifest exactly", errors)
    require(set(audio) == ids, "audio ids do not match manifest exactly", errors)
    ci = evidence.get("parallel_cefr_ci")
    if not isinstance(ci, dict):
        errors.append("missing parallel_cefr_ci evidence")
    else:
        sha = ci.get("commit_sha")
        require(isinstance(sha, str) and re.fullmatch(r"[a-fA-F0-9]{40}", sha) is not None, "parallel CEFR CI commit SHA invalid", errors)
        require(sha == evidence.get("release_commit_sha"), "CI commit SHA does not match release commit SHA", errors)
        require(type(ci.get("run_id")) is int and ci["run_id"] > 0, "parallel CEFR CI run_id missing", errors)
        jobs = ci.get("jobs")
        if not isinstance(jobs, dict):
            errors.append("parallel CEFR CI jobs missing")
        else:
            require(set(jobs) == set(LEVELS), "parallel CEFR CI must include exactly five level jobs", errors)
            for level in LEVELS:
                job = jobs.get(level)
                require(isinstance(job, dict) and job.get("conclusion") == "success" and https_evidence_url(job.get("logs_url")), f"{level}: successful job conclusion and HTTPS logs URL required", errors)
    gates = evidence.get("release_gates", {})
    if not isinstance(gates, dict):
        gates = {}
    for gate in ("browser_regression", "mobile_regression", "physical_iphone_safari", "github_pages_limits", "production_deployment", "production_asset_preservation", "privacy_review"):
        g = gates.get(gate)
        require(isinstance(g, dict) and g.get("passed") is True and https_evidence_url(g.get("evidence_url")) and iso_timestamp(g.get("verified_at")), f"release gate {gate} missing independently documented pass with HTTPS evidence URL", errors)
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
