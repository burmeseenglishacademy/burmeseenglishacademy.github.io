#!/usr/bin/env python3
"""Fail-closed staging evidence gate. Does not grant or fabricate review signoff.

Usage: python scripts/cefr1000_release_evidence_gate.py [evidence.json]
Absent evidence is a BLOCK, never a pass. Does not modify any files.
"""
import collections
import json
import pathlib
import sys

LEVELS = ("A1", "A2", "B1", "B2", "C1")
DOMAINS = ("english", "myanmar", "example", "cefr")
VOICES = ("george", "emma")
KINDS = ("headword", "example")

def nonblank(value):
    return isinstance(value, str) and bool(value.strip())

def gate(manifest, evidence):
    blockers = []
    entries = manifest.get("entries") if isinstance(manifest, dict) else None
    if not isinstance(entries, list) or len(entries) != 1000:
        return ["manifest must contain exactly 1000 entries"]
    counts = collections.Counter(e.get("level") for e in entries if isinstance(e, dict))
    for level in LEVELS:
        if counts[level] != 200:
            blockers.append(f"{level}: expected 200 entries, found {counts[level]}")
    if not isinstance(evidence, dict):
        return blockers + ["independent evidence ledger absent or invalid"]
    reviews = evidence.get("independent_reviews")
    audio = evidence.get("audio")
    qa = evidence.get("qa")
    if not isinstance(reviews, list):
        blockers.append("independent_reviews must be a list")
        reviews = []
    if not isinstance(audio, list):
        blockers.append("audio must be a list")
        audio = []
    if not isinstance(qa, dict):
        blockers.append("qa must be an object")
        qa = {}
    # Exact entry index is tied to a specific shortlist blob; a new shortlist
    # revision invalidates the ledger rather than silently reusing signoffs.
    if not nonblank(evidence.get("manifest_blob_sha")) or len(evidence["manifest_blob_sha"]) != 40:
        blockers.append("manifest blob SHA binding missing")
    # Self-asserted booleans are not sufficient: demand reviewer identity,
    # independently traceable evidence and dated observations for each domain.
    review_index = collections.defaultdict(list)
    for r in reviews:
        if not isinstance(r, dict):
            blockers.append("malformed independent review record")
            continue
        key = (r.get("entry_index"), r.get("domain"))
        review_index[key].append(r)
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            blockers.append(f"{i}: malformed entry")
            continue
        for domain in DOMAINS:
            candidates = review_index.get((i, domain), [])
            accepted = [r for r in candidates if
                r.get("decision") == "approved" and
                nonblank(r.get("reviewer_id")) and
                nonblank(r.get("reviewer_independence_evidence")) and
                nonblank(r.get("observed_on")) and
                nonblank(r.get("source_url")) and
                nonblank(r.get("sense_id")) and
                r.get("headword") == entry.get("word") and
                r.get("level") == entry.get("level")]
            if len(accepted) != 1 or len(candidates) != 1:
                blockers.append(f"{i}: independent {domain} evidence missing/ambiguous")
    audio_index = collections.defaultdict(list)
    for a in audio:
        if isinstance(a, dict):
            audio_index[(a.get("entry_index"), a.get("voice"), a.get("kind"))].append(a)
        else:
            blockers.append("malformed audio record")
    for i in range(1000):
        for voice in VOICES:
            for kind in KINDS:
                candidates = audio_index.get((i, voice, kind), [])
                accepted = [a for a in candidates if
                    nonblank(a.get("file_sha256")) and
                    nonblank(a.get("artifact_path")) and
                    nonblank(a.get("listener_id")) and
                    nonblank(a.get("listened_on")) and
                    nonblank(a.get("listening_evidence_url")) and
                    a.get("listening_result") == "pass"]
                if len(accepted) != 1 or len(candidates) != 1:
                    blockers.append(f"{i}: {voice}/{kind} audio or actual listening evidence missing")
    for key in ("browser_regression", "mobile_regression", "physical_iphone_safari",
                "github_pages_limits", "production_assets_preserved",
                "production_deployment_confirmed"):
        q = qa.get(key)
        if not isinstance(q, dict) or q.get("result") != "pass" or not all(
            nonblank(q.get(k)) for k in ("evidence_url", "observed_on", "reviewer_id")
        ):
            blockers.append(f"{key}: verified evidence missing")
    return blockers

def main():
    manifest_path = pathlib.Path("draft/CEFR-1000-PROVISIONAL-SHORTLIST.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
    evidence = json.loads(path.read_text(encoding="utf-8")) if path and path.is_file() else None
    blockers = gate(manifest, evidence)
    print(json.dumps({"status": "BLOCKED" if blockers else "EVIDENCE_SCHEMA_COMPLETE_REQUIRES_EXTERNAL_VERIFICATION",
                      "blocker_count": len(blockers), "blocker_examples": blockers[:25],
                      "release_authorized": False,
                      "note": "Document checks alone cannot verify human independence, real listening, physical devices or deployment."},
                     ensure_ascii=False, indent=2))
    return 1  # Always fail closed: never authorize deployment from ledger assertions alone.

if __name__ == "__main__":
    sys.exit(main())
