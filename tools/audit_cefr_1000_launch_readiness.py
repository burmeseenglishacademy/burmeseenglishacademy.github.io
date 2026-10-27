#!/usr/bin/env python3
"""Conservative, staging-only CEFR 1,000-word release evidence ledger auditor.

This NEVER independently verifies language, listening or physical devices. It can
only check documentary evidence supplied by actual external human reviewers and
testers. An empty/stale/forged record is NOT licence to deploy. No publish step.
"""
import argparse
import collections
import datetime
import hashlib
import json
import pathlib
import re
import sys
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ROOT / "draft/CEFR-1000-RELEASE-EVIDENCE.json"
TARGETS = {k: 200 for k in ("A1", "A2", "B1", "B2", "C1")}
VOICES = ("bm_george", "bf_emma")
STAGES = ("english_sense", "myanmar_meaning", "original_example", "sense_specific_cefr")
BROWSERS = ("desktop-chromium", "desktop-webkit", "mobile-chromium", "mobile-webkit")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")


def read_json(path):
    return json.loads(path.read_text("utf8"))


def content_hash(entry):
    """Invalidate prior review if any user-visible reviewed element changed."""
    relevant = {k: entry.get(k) for k in
                ("word", "level", "part_of_speech", "english_definition",
                 "burmese_meaning", "example_sentence")}
    return hashlib.sha256(json.dumps(relevant, ensure_ascii=False,
                            sort_keys=True, separators=(",", ":")).encode("utf8")).hexdigest()


def real_observation(record, fields):
    if not isinstance(record, dict):
        return False
    if record.get("result") != "PASS":
        return False
    for field in fields:
        if not isinstance(record.get(field), str) or len(record[field].strip()) < 3:
            return False
    # A string timestamp alone cannot prove a review took place.
    try:
        stamp = datetime.date.fromisoformat(record["reviewed_on"])
        if stamp > datetime.date.today() or stamp < datetime.date(2026, 10, 1):
            return False
    except (KeyError, ValueError, TypeError):
        return False
    reviewer = str(record.get("reviewer_id", "")).casefold()
    return reviewer not in {"ai", "chatgpt", "gpt", "auto", "bot", "unknown", "pending"}


def specific_url(url):
    if not isinstance(url, str) or not url.startswith("https://"):
        return False
    p = urlparse(url)
    return bool(p.hostname and len([x for x in p.path.split("/") if x]) >= 2
                and "example." not in p.hostname.lower())


def audit(ledger=None, after_deployment=False):
    d = ledger if ledger is not None else read_json(LEDGER)
    issues = []
    report = {"scope_targets": TARGETS, "provisional_selected": 1000,
              "independent_stage_complete": {k: 0 for k in TARGETS},
              "both_voice_listening_complete_words": {k: 0 for k in TARGETS},
              "approved_manifest_present": False,
              "browser_evidence_complete": False,
              "physical_iphone_safari_verified": False,
              "hosting_evidence_verified": False,
              "production_assets_preserved": False,
              "live_site_confirmed": False,
              "oxford_reference_flags_in_provisional_shortlist": 0,
              "oxford_conflicts_requiring_independent_resolution": 0,
              "oxford_conflicts_resolution_receipts_valid": 0,
              "ielts_shared_headwords_in_provisional_shortlist": 0,
              "ielts_overlaps_requiring_independent_resolution": 0,
              "ielts_overlaps_resolution_receipts_valid": 0,
              "validated_audio_voice_text_pairs": 0,
              "check_type": "DOCUMENTARY_EVIDENCE_INTEGRITY_NOT_REAL_WORLD_CONFIRMATION"}
    if d.get("scope_targets") != TARGETS:
        issues.append("Wrong 200-per-level approved scope")
    if d.get("status") not in ("BLOCKED_PENDING_INDEPENDENT_QC_DO_NOT_PUBLISH",
                               "INDEPENDENT_QC_COMPLETE_RELEASE_CANDIDATE"):
        issues.append("Unknown release evidence status")
    approved_path = d.get("approved_dataset_path")
    if approved_path != "draft/CEFR-1000-APPROVED-RELEASE.json":
        issues.append("Approved dataset must be explicit separate reviewed manifest")
    source = ROOT / "draft/CEFR-1000-APPROVED-RELEASE.json"
    manifest = None
    entries = []
    if not source.exists():
        issues.append("Missing separately independently approved 1000-entry release manifest")
    else:
        raw = source.read_bytes()
        manifest_sha = hashlib.sha256(raw).hexdigest()
        if manifest_sha != d.get("approved_dataset_sha256"):
            issues.append("Approved release manifest SHA-256 mismatch")
        try:
            manifest = json.loads(raw.decode("utf8"))
            entries = manifest.get("entries", []) if isinstance(manifest, dict) else []
            report["approved_manifest_present"] = True
            # Import the existing fail-closed 1000-row release structural validator.
            import importlib.util
            spec = importlib.util.spec_from_file_location("cefr_release_gate", ROOT / "tools/validate_cefr_release.py")
            gate = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(gate)
            for issue in gate.validate(manifest, root=ROOT, verify_audio=True)[:12]:
                issues.append("Approved manifest/audio gate: " + issue)
        except (ValueError, TypeError, OSError) as exc:
            issues.append("Cannot parse approved manifest: " + str(exc)[:100])

    receipts = d.get("independent_word_review_receipts", [])
    if not isinstance(receipts, list):
        receipts = []
        issues.append("Word review evidence is not an array")
    receipt_index = {}
    for r in receipts:
        if not isinstance(r, dict):
            issues.append("Invalid word-review receipt type")
            continue
        key = (r.get("level"), r.get("word"))
        if key in receipt_index:
            issues.append(f"Duplicate human word-review receipt {key}")
        receipt_index[key] = r
    if len(receipt_index) != 1000:
        issues.append(f"Only {len(receipt_index)} of 1000 independent word-review packets recorded")
    expected_keys = {(x.get("level"), x.get("word")) for x in entries if isinstance(x, dict)}
    for n, entry in enumerate(entries):
        if not isinstance(entry, dict):
            continue
        level, word = entry.get("level"), entry.get("word")
        r = receipt_index.get((level, word))
        if not r:
            continue
        if r.get("reviewed_content_sha256") != content_hash(entry):
            issues.append(f"{word}: independent review content hash stale/missing")
            continue
        checks = r.get("checks", {})
        good = True
        for stage in STAGES:
            c = checks.get(stage, {}) if isinstance(checks, dict) else {}
            if not real_observation(c, ("reviewer_id", "notes")):
                good = False
                issues.append(f"{word}: {stage} lacks independent review receipt")
            if stage in ("english_sense", "sense_specific_cefr") and not specific_url(c.get("source_url")):
                good = False
                issues.append(f"{word}: {stage} lacks exact-sense public source URL")
        if good and level in TARGETS:
            report["independent_stage_complete"][level] += 1
    if len(receipt_index) and set(receipt_index) != expected_keys:
        issues.append("Review receipt words do not match approved release entries")
    if report["independent_stage_complete"] != TARGETS:
        issues.append("Not all 200 entries in every level have independent stage signoffs")

    # Check prior Oxford wordlist CEFR/POS differences are not forgotten when
    # the final approved shortlist is selected. An alternate CEFR score is a
    # review task, NOT proof of an error, and resolved claims need real reviewers.
    oxford_holds = read_json(ROOT / "draft/CEFR-1000-OXFORD-DISCREPANCY-QUARANTINE.json")
    reported_risks = oxford_holds.get("records", [])
    report["oxford_reference_flags_in_provisional_shortlist"] = len(reported_risks)
    ox_receipts = d.get("oxford_level_discrepancy_review_receipts", [])
    if not isinstance(ox_receipts, list):
        issues.append("Oxford discrepancy review receipts are not a list")
        ox_receipts = []
    ox_index = {}
    for rec in ox_receipts:
        if not isinstance(rec, dict):
            issues.append("Invalid Oxford discrepancy reviewer record")
            continue
        key = (rec.get("word"), rec.get("proposed_level"))
        if key in ox_index:
            issues.append("Duplicate Oxford discrepancy reviewer record")
        ox_index[key] = rec
    entry_lookup = {(x.get("word"), x.get("level")): x for x in entries if isinstance(x, dict)}
    for hold in reported_risks:
        key = (hold["word"], hold["proposed_level"])
        if key not in entry_lookup:
            continue  # Replaced/retiered entries must undergo independent new-entry review.
        report["oxford_conflicts_requiring_independent_resolution"] += 1
        rec = ox_index.get(key)
        entry = entry_lookup[key]
        if not real_observation(rec, ("reviewer_id", "notes", "source_url")):
            continue
        if (rec.get("decision") != "RETAIN_WITH_INDEPENDENT_SENSE_LEVEL_EVIDENCE"
                or rec.get("reviewed_content_sha256") != content_hash(entry)
                or rec.get("verified_part_of_speech") != entry.get("part_of_speech")
                or rec.get("verified_cefr_level") != entry.get("level")
                or not specific_url(rec.get("source_url"))
                or entry["word"] not in urlparse(rec["source_url"]).path.lower()):
            continue
        report["oxford_conflicts_resolution_receipts_valid"] += 1
    if report["oxford_conflicts_requiring_independent_resolution"] != report["oxford_conflicts_resolution_receipts_valid"]:
        issues.append("Oxford POS/level/source or absent-core-list discrepancies remain unresolved for retained entries")
    if ox_index and set(ox_index) - {(x["word"], x["proposed_level"]) for x in reported_risks}:
        issues.append("Unknown Oxford discrepancy receipts supplied")

    # Cross-bank duplication is not automatically wrong, but each retained
    # overlap must have an independent documented semantic/teaching rationale.
    crossbank = read_json(ROOT / "draft/CEFR-1000-IELTS-OVERLAP-REVIEW.json")
    shared = crossbank.get("entries", [])
    report["ielts_shared_headwords_in_provisional_shortlist"] = len(shared)
    decisions = d.get("ielts_cross_bank_overlap_review_receipts", [])
    if not isinstance(decisions, list):
        issues.append("IELTS overlap decisions are not a list")
        decisions = []
    decisions_by_word = {}
    for rec in decisions:
        if not isinstance(rec, dict):
            issues.append("Invalid IELTS overlap decision")
            continue
        key = (rec.get("word"), rec.get("proposed_cefr_level"))
        if key in decisions_by_word:
            issues.append("Duplicate IELTS overlap decision")
        decisions_by_word[key] = rec
    for record in shared:
        key = (record["word"], record["proposed_cefr_level"])
        if key not in entry_lookup:
            continue
        report["ielts_overlaps_requiring_independent_resolution"] += 1
        rec = decisions_by_word.get(key)
        entry = entry_lookup[key]
        if (real_observation(rec, ("reviewer_id", "notes"))
                and rec.get("decision") in ("RETAIN_DISTINCT_SENSE", "RETAIN_DISTINCT_CEFR_TEACHING_CONTEXT")
                and rec.get("reviewed_content_sha256") == content_hash(entry)):
            report["ielts_overlaps_resolution_receipts_valid"] += 1
    if report["ielts_overlaps_requiring_independent_resolution"] != report["ielts_overlaps_resolution_receipts_valid"]:
        issues.append("Retained CEFR/IELTS headword overlaps have not undergone independent sense/usefulness review")
    if decisions_by_word and set(decisions_by_word) - {(x["word"], x["proposed_cefr_level"]) for x in shared}:
        issues.append("Unknown IELTS overlap reviewer decisions supplied")

    # Audio real-listening receipts are 1 per unique word/example text and voice.
    # The separate validator must ALSO confirm files exist and decode.
    audio = d.get("audio_listening_receipts", [])
    if not isinstance(audio, list):
        audio = []
        issues.append("Audio listening evidence is not an array")
    audio_seen = {}
    for r in audio:
        if not isinstance(r, dict):
            issues.append("Invalid listening record")
            continue
        key = (r.get("text"), r.get("voice"))
        if key in audio_seen:
            issues.append(f"Duplicate listening record {str(key)[:80]}")
        audio_seen[key] = r
    expected_audio = set()
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        for text in (entry.get("word"), entry.get("example_sentence")):
            if isinstance(text, str):
                expected_audio.update((text, voice) for voice in VOICES)
    if not audio_seen:
        issues.append("No real George/Emma audio listening receipts provided")
    if len(audio_seen) != len(expected_audio):
        issues.append(f"Listening coverage {len(audio_seen)} records / {len(expected_audio)} required voice-text pairs")
    if audio_seen and set(audio_seen) != expected_audio:
        issues.append("Listening receipts do not exactly cover the approved headword/example corpus")
    verified_pairs = set()
    for key in expected_audio:
        r = audio_seen.get(key)
        if not real_observation(r, ("reviewer_id", "notes", "recording_sha256")) or not SHA256.fullmatch(str((r or {}).get("recording_sha256", ""))):
            continue
        # Counting as listened requires matching the actual immutable MP3 bytes.
        text, voice = key
        file = ROOT / "audio" / voice / (hashlib.sha256(text.encode("utf8")).hexdigest()[:24] + ".mp3")
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != r["recording_sha256"]:
            issues.append("Audio listening fingerprint mismatch: " + text[:30] + "/" + voice)
            continue
        verified_pairs.add(key)
    report["validated_audio_voice_text_pairs"] = len(verified_pairs)
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("level") not in TARGETS:
            continue
        necessary = {(t, v) for t in (entry.get("word"), entry.get("example_sentence")) for v in VOICES}
        if necessary.issubset(verified_pairs):
            report["both_voice_listening_complete_words"][entry["level"]] += 1
    if report["both_voice_listening_complete_words"] != TARGETS:
        issues.append("Real George/Emma listening unverified for some or all words and sentences")

    # Browser evidence must be tied to the same approved release manifest.
    browsers = d.get("automated_browser_checks", [])
    if not isinstance(browsers, list):
        browsers = []
    have = set()
    for b in browsers:
        if not isinstance(b, dict):
            continue
        if real_observation(b, ("reviewer_id", "notes", "run_url")) and specific_url(b.get("run_url")) and b.get("approved_dataset_sha256") == d.get("approved_dataset_sha256"):
            have.add(b.get("browser"))
    report["browser_evidence_complete"] = set(BROWSERS).issubset(have)
    if not report["browser_evidence_complete"]:
        issues.append("Missing matched desktop/mobile Chromium and WebKit regression evidence")
    ios = d.get("physical_iphone_safari_check")
    report["physical_iphone_safari_verified"] = (
        real_observation(ios, ("reviewer_id", "notes", "model", "ios_version", "safari_version", "evidence_url"))
        and ios.get("physical_device") is True and ios.get("both_voices_listened") is True
        and specific_url(ios.get("evidence_url")) and ios.get("approved_dataset_sha256") == d.get("approved_dataset_sha256"))
    if not report["physical_iphone_safari_verified"]:
        issues.append("No verified physical iPhone Safari and British audio test evidence")
    hosting = d.get("hosting_limits_check")
    report["hosting_evidence_verified"] = (
        real_observation(hosting, ("reviewer_id", "notes", "evidence_url"))
        and specific_url(hosting.get("evidence_url"))
        and isinstance(hosting.get("measured_bytes"), int)
        and isinstance(hosting.get("hosted_limit_bytes"), int)
        and 0 < hosting["measured_bytes"] <= hosting["hosted_limit_bytes"]
        and hosting.get("approved_dataset_sha256") == d.get("approved_dataset_sha256"))
    if not report["hosting_evidence_verified"]:
        issues.append("No evidence of actual measured GitHub Pages hosting limits")
    preservation = d.get("protected_production_assets_check")
    report["production_assets_preserved"] = (
        real_observation(preservation, ("reviewer_id", "notes", "run_url"))
        and specific_url(preservation.get("run_url"))
        and preservation.get("protected_assets_unchanged") is True)
    if not report["production_assets_preserved"]:
        issues.append("No final evidence of preserved 54 lessons, IELTS, audio and privacy")
    if d.get("status") != "INDEPENDENT_QC_COMPLETE_RELEASE_CANDIDATE":
        issues.append("Release candidate has not been formally approved")
    if after_deployment:
        deployment = d.get("production_deployment_confirmation")
        report["live_site_confirmed"] = (
            real_observation(deployment, ("reviewer_id", "notes", "production_url", "live_commit"))
            and deployment.get("production_url") == "https://burmeseenglishacademy.github.io/"
            and bool(COMMIT.fullmatch(str(deployment.get("live_commit", ""))))
            and deployment.get("approved_dataset_sha256") == d.get("approved_dataset_sha256"))
        if not report["live_site_confirmed"]:
            issues.append("Live GitHub Pages deployment has not been independently confirmed")
    report["issues_count"] = len(issues)
    report["release_ready"] = not issues
    return issues, report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--expect-blocked", action="store_true", help="Temporary diagnostic: expect release to remain blocked")
    parser.add_argument("--report-only", action="store_true", help="Report readiness without treating legitimate pending QC as a workflow failure")
    parser.add_argument("--self-test", action="store_true", help="Prove missing human review and false ready flag are rejected")
    parser.add_argument("--after-deployment", action="store_true", help="Final production confirmation (never claims success prelaunch)")
    parser.add_argument("--report", default="cefr-1000-launch-gate-report.json")
    args = parser.parse_args()
    issues, report = audit(after_deployment=args.after_deployment)
    if args.self_test:
        import copy
        false_ready = copy.deepcopy(read_json(LEDGER))
        false_ready["status"] = "INDEPENDENT_QC_COMPLETE_RELEASE_CANDIDATE"
        fake_issues, fake_report = audit(false_ready, after_deployment=True)
        assert fake_issues and not fake_report["release_ready"]
        assert any("independently approved 1000-entry" in item for item in fake_issues)
        assert any("physical iPhone Safari" in item for item in fake_issues)
        assert any("No real George/Emma audio listening receipts" in item for item in fake_issues)
        print("PASS: false ready flag cannot override missing independent, listening, iPhone or hosting evidence")
    pathlib.Path(args.report).write_text(json.dumps({"report": report, "blockers": issues[:100]},
                                           ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print("CEFR 1000: source-reviewed", sum(report["independent_stage_complete"].values()),
          "/1000; both-voice listening", sum(report["both_voice_listening_complete_words"].values()),
          "/1000; actual production confirmed", report["live_site_confirmed"])
    for issue in issues[:25]:
        print("BLOCK:", issue)
    if args.report_only:
        print("REPORT ONLY: readiness blockers remain recorded; this is NOT a release approval" if issues else "REPORT ONLY: documentary checklist complete, independent evidence/authenticity must still be confirmed")
        return 0
    if args.expect_blocked:
        if not issues:
            print("UNEXPECTED UNBLOCKED RELEASE: staging-only safeguard needs review", file=sys.stderr)
            return 1
        print("PASS: intentional fail-closed launch QC; no deployment")
        return 0
    if issues:
        print(f"NOT RELEASE READY: {len(issues)} evidence blocker(s)", file=sys.stderr)
        return 1
    print("Structural evidence ledger complete; human attestations and actual observed tests still require independent confirmation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
