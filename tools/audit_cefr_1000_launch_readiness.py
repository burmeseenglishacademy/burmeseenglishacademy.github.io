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
PAGES_LIMITS_URL = "https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits"
PAGES_SITE_BYTES_CAP = 1_000_000_000  # conservative decimal interpretation of 1 GB
PAGES_BANDWIDTH_SOFT_BYTES = 100_000_000_000  # 100 GB/month soft limit



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


def independent_source_for_word(record, word):
    """Documentary source-to-headword binding, not an exact-sense judgement.

    Dictionary pages must point to the reviewed headword, not a plausible
    unrelated dictionary entry. Broad publisher PDFs require a verifiable
    page/line locator and a verbatim short observation containing the word.
    Reviewers still have to independently judge POS, sense and CEFR.
    """
    from urllib.parse import unquote
    url = record.get("source_url")
    if not specific_url(url) or not isinstance(word, str) or not word:
        return False
    p = urlparse(url)
    path = unquote(p.path).casefold()
    word = word.casefold().strip()
    if path.endswith(".pdf"):
        locator = record.get("source_locator")
        if not isinstance(locator, dict):
            return False
        page, line = locator.get("pdf_page"), locator.get("extracted_line")
        quote = locator.get("source_excerpt")
        if type(page) is not int or page < 1 or type(line) is not int or line < 0:
            return False
        if not isinstance(quote, str) or len(quote.strip()) < 3 or len(quote) > 350:
            return False
        return word in re.findall(r"[a-z]+(?:[-'][a-z]+)*", quote.casefold())
    segments = [segment.split("_")[0] for segment in path.strip("/").split("/")]
    return word in segments


def independent_word_stage(record, word, stage):
    """Reject unsupported or anonymous independent signoff assertions.

    A receipt URL and declared independent HUMAN role are required. Their
    authenticity must still be checked against the original reviewer by a
    separate human; this validator does not authenticate identities.
    """
    if not real_observation(record, ("reviewer_id", "notes",
                                     "reviewer_attestation_url", "reviewer_role")):
        return False
    if record.get("reviewer_role") not in (
            "INDEPENDENT_HUMAN_EDITOR", "INDEPENDENT_HUMAN_LINGUIST"):
        return False
    if not specific_url(record.get("reviewer_attestation_url")):
        return False
    reviewer = record["reviewer_id"].casefold()
    if re.search(r"(?:^|[^a-z])(?:ai|gpt|chatgpt|llm|bot|automation|automated|agent)(?:[^a-z]|$)", reviewer):
        return False
    if stage in ("english_sense", "sense_specific_cefr"):
        return independent_source_for_word(record, word)
    return True


def hosting_limits_valid(hosting, approved_sha):
    """Check a documented measurement against actual GitHub Pages policy caps.

    This verifies receipt shape and conservative numerical constraints only.
    It does NOT independently measure hosting usage or authenticate the human.
    """
    if not real_observation(hosting, ("reviewer_id", "notes", "evidence_url",
                                      "measurement_method")):
        return False
    if (not specific_url(hosting.get("evidence_url"))
            or hosting.get("policy_url") != PAGES_LIMITS_URL
            or hosting.get("approved_dataset_sha256") != approved_sha
            or not SHA256.fullmatch(str(hosting.get("site_artifact_sha256", "")))):
        return False
    for key, maximum in (("measured_bytes", PAGES_SITE_BYTES_CAP),
                         ("source_repository_bytes", PAGES_SITE_BYTES_CAP),
                         ("forecast_monthly_bandwidth_bytes", PAGES_BANDWIDTH_SOFT_BYTES)):
        value = hosting.get(key)
        if type(value) is not int or value <= 0 or value > maximum:
            return False
    return True


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
              "cambridge_sense_observations": 0,
              "cambridge_sense_retained_requiring_resolution": 0,
              "cambridge_sense_retained_resolved": 0,
              "cambridge_second_sense_observations": 0,
              "cambridge_second_sense_retained_requiring_resolution": 0,
              "cambridge_second_sense_retained_resolved": 0,
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
            if not independent_word_stage(c, word, stage):
                good = False
                issues.append(f"{word}: {stage} lacks independent human attestation or word-linked source evidence")
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

    # Publisher sense-level observations must be reconciled for retained entries.
    # This catches polysemy and definition/example divergence (especially 'business')
    # that a coarse headword/POS Oxford check cannot establish.
    cambridge = read_json(ROOT / "draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json")
    sense_flags = cambridge.get("records", [])
    report["cambridge_sense_observations"] = len(sense_flags)
    sense_receipts = d.get("cambridge_sense_triage_review_receipts", [])
    if not isinstance(sense_receipts, list):
        issues.append("Cambridge sense review receipts are not a list")
        sense_receipts = []
    sense_index = {}
    for rec in sense_receipts:
        if not isinstance(rec, dict):
            issues.append("Invalid Cambridge sense receipt")
            continue
        key = (rec.get("word"), rec.get("proposed_level"))
        if key in sense_index:
            issues.append("Duplicate Cambridge sense receipt")
        sense_index[key] = rec
    for flag in sense_flags:
        key = (flag["word"], flag["level"])
        entry = entry_lookup.get(key)
        if entry is None:
            continue  # Replacement/retiering still needs full new independent review.
        report["cambridge_sense_retained_requiring_resolution"] += 1
        rec = sense_index.get(key)
        if not real_observation(rec, ("reviewer_id", "notes", "source_url")):
            continue
        if (rec.get("decision") != "RETAIN_WITH_INDEPENDENT_SENSE_EVIDENCE"
                or rec.get("reviewed_content_sha256") != content_hash(entry)
                or rec.get("verified_cefr_level") != entry.get("level")
                or rec.get("verified_part_of_speech") != entry.get("part_of_speech")
                or not specific_url(rec.get("source_url"))
                or entry["word"] not in urlparse(rec["source_url"]).path.lower()):
            continue
        # Certain drafts use a different source-labelled sense from their
        # target level. A receipt cannot bless an unchanged mixed/mislevelled
        # example: edit it and obtain new independent review, or replace/retier.
        if (entry["word"] == "business"
                and entry.get("english_definition") == flag.get("shortlist_english_definition")
                and entry.get("example_sentence") == flag.get("shortlist_example")):
            continue
        if (entry["word"] == "hardly"
                and entry.get("example_sentence") == flag.get("shortlist_example")):
            continue
        # If a lower-level sense is deliberately retained at a higher level,
        # demand a specific independent teaching rationale in addition to the
        # generic independent CEFR review and source URL.
        if (str(flag.get("triage", "")).startswith("SAME_SENSE_LOWER_SOURCE_LEVEL")
                and (not isinstance(rec.get("sense_level_rationale"), str)
                     or len(rec["sense_level_rationale"].strip()) < 24)):
            continue
        report["cambridge_sense_retained_resolved"] += 1
    if (report["cambridge_sense_retained_requiring_resolution"]
            != report["cambridge_sense_retained_resolved"]):
        issues.append("Retained Cambridge sense/POS/CEFR observations lack independent resolution")
    if sense_index and set(sense_index) - {(x["word"], x["level"]) for x in sense_flags}:
        issues.append("Unknown Cambridge sense reviewer receipts supplied")

    # Five additional publisher-indexed exact-sense leads are distinct from
    # Oxford word/POS labels. In particular Cambridge labels print(TEXT),
    # consistently(unchanging) and integrity(HONESTY) C2, while Oxford's
    # word/POS lists show B2/B2/C1. Never silently collapse this distinction.
    second_cambridge = read_json(
        ROOT / "draft/CEFR-1000-CAMBRIDGE-SECOND-SENSE-LEADS-2026-10-27.json")
    second_flags = second_cambridge.get("records", [])
    expected_second_words = {"print", "racism", "consistently", "diverse", "integrity"}
    report["cambridge_second_sense_observations"] = len(second_flags)
    if (second_cambridge.get("status") != "CAMBRIDGE_SECOND_SENSE_SOURCE_LEADS_STAGING_HOLD"
            or len(second_flags) != 5
            or {x.get("word") for x in second_flags if isinstance(x, dict)} != expected_second_words):
        issues.append("Second Cambridge publisher-sense packet missing, truncated or tampered")
    second_receipts = d.get("cambridge_second_sense_review_receipts", [])
    if not isinstance(second_receipts, list):
        issues.append("Second Cambridge sense receipts are not an array")
        second_receipts = []
    second_index = {}
    for rec in second_receipts:
        if not isinstance(rec, dict):
            issues.append("Invalid second Cambridge sense receipt")
            continue
        key = (rec.get("word"), rec.get("proposed_level"))
        if key in second_index:
            issues.append("Duplicate second Cambridge sense receipt")
        second_index[key] = rec
    for flag in second_flags:
        if not isinstance(flag, dict):
            issues.append("Invalid second Cambridge publisher observation")
            continue
        key = (flag.get("word"), flag.get("shortlist_level"))
        entry = entry_lookup.get(key)
        if entry is None:
            continue  # Replaced/retiered words still require new full independent signoff.
        report["cambridge_second_sense_retained_requiring_resolution"] += 1
        rec = second_index.get(key)
        if not real_observation(rec, ("reviewer_id", "notes", "source_url",
                                      "publisher_level_conflict_rationale")):
            continue
        if (rec.get("decision") != "RETAIN_AFTER_INDEPENDENT_SENSE_LEVEL_REVIEW"
                or rec.get("reviewed_content_sha256") != content_hash(entry)
                or rec.get("verified_cefr_level") != entry.get("level")
                or rec.get("verified_part_of_speech") != entry.get("part_of_speech")
                or rec.get("source_sense_cefr") != flag.get("source_sense_cefr")
                or rec.get("source_sense_heading") != flag.get("source_sense_heading")
                or rec.get("source_url") != flag.get("source_url")
                or len(rec["publisher_level_conflict_rationale"].strip()) < 40):
            continue
        report["cambridge_second_sense_retained_resolved"] += 1
    if (report["cambridge_second_sense_retained_requiring_resolution"]
            != report["cambridge_second_sense_retained_resolved"]):
        issues.append("Five Cambridge publisher exact-sense conflicts need independent reviewer resolution")
    if second_index and set(second_index) - {
            (x.get("word"), x.get("shortlist_level")) for x in second_flags if isinstance(x, dict)}:
        issues.append("Unknown second Cambridge sense receipts supplied")

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
    report["hosting_evidence_verified"] = hosting_limits_valid(
        hosting, d.get("approved_dataset_sha256"))
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
        # A user-supplied inflated 'hosted_limit_bytes' must never override
        # official Pages caps; missing bandwidth and artifact digests also fail.
        assert not hosting_limits_valid({
            "result": "PASS", "reviewer_id": "TEST_ONLY", "notes": "TEST_ONLY",
            "reviewed_on": "2026-10-27", "evidence_url": "https://github.com/test/evidence",
            "measurement_method": "TEST_ONLY", "policy_url": PAGES_LIMITS_URL,
            "approved_dataset_sha256": "0" * 64,
            "site_artifact_sha256": "0" * 64,
            "measured_bytes": 2_000_000_000,
            "source_repository_bytes": 1000,
            "forecast_monthly_bandwidth_bytes": 1000,
            "hosted_limit_bytes": 10_000_000_000
        }, "0" * 64)
        print("PASS: official Pages size/bandwidth caps reject inflated self-reported limits")
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
