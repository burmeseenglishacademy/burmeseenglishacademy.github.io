#!/usr/bin/env python3
"""Mutation tests: provisional structural gate must fail closed on corrupt evidence."""
import copy
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILES = ("CEFR-1000-PROVISIONAL-SHORTLIST.json", "CEFR-1000-INDEPENDENT-REVIEW-TASKS.json")

def run_gate(root):
    return subprocess.run([sys.executable, str(root / "scripts/cefr1000_staging_gate.py"), "--level", "A1"],
                          cwd=root, capture_output=True, text=True)

def assert_report(result, label, expected_text=None):
    """Require controlled JSON diagnostics, not a Python crash."""
    expected_code = 1 if expected_text else 0
    if result.returncode != expected_code or result.stderr.strip():
        raise AssertionError(f"{label}: exit={result.returncode}; stderr={result.stderr[:300]!r}")
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{label}: missing valid JSON report") from exc
    if report.get("mode") != "structural" or report.get("level") != "A1":
        raise AssertionError(f"{label}: incorrect gate mode or level")
    if report.get("independent_approval_inferred") is not False:
        raise AssertionError(f"{label}: independent approval inferred")
    errors = report.get("errors")
    if not isinstance(errors, list):
        raise AssertionError(f"{label}: missing errors list")
    if expected_text and not any(expected_text in str(error) for error in errors):
        raise AssertionError(f"{label}: missing expected diagnostic {expected_text!r}; got {errors[:3]}")
    if not expected_text and errors:
        raise AssertionError(f"{label}: baseline reported errors {errors[:3]}")

def main():
    with tempfile.TemporaryDirectory() as folder:
        root = pathlib.Path(folder)
        (root / "draft").mkdir()
        (root / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/cefr1000_staging_gate.py", root / "scripts")
        originals = {}
        for name in FILES:
            originals[name] = json.loads((ROOT / "draft" / name).read_text(encoding="utf-8"))
        def check(label, mutate, diagnostic):
            docs = copy.deepcopy(originals)
            mutate(docs[FILES[0]], docs[FILES[1]])
            for name, doc in docs.items():
                (root / "draft" / name).write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
            result = run_gate(root)
            assert_report(result, label, diagnostic)
            print(f"PASS rejected: {label}")
        # First establish that the unmodified provisional inventory passes structural checks.
        for name, doc in originals.items():
            (root / "draft" / name).write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        baseline = run_gate(root)
        assert_report(baseline, "baseline")
        # A clean provisional inventory must NEVER become a releasable inventory.
        # Exercise the actual --release path, not only the default structural mode.
        release = subprocess.run(
            [sys.executable, str(root / "scripts/cefr1000_staging_gate.py"), "--release"],
            cwd=root, capture_output=True, text=True)
        if release.returncode != 1 or release.stderr.strip():
            raise AssertionError(f"release gate did not fail cleanly: {release.returncode}, {release.stderr[:300]!r}")
        try:
            release_report = json.loads(release.stdout)
        except json.JSONDecodeError as exc:
            raise AssertionError("release gate did not return JSON") from exc
        if (release_report.get("mode") != "release"
                or release_report.get("independent_approval_inferred") is not False
                or not any("RELEASE BLOCKED" in str(err) for err in release_report.get("errors", []))):
            raise AssertionError("release gate did not explicitly block unaudited release")
        print("PASS rejected: provisional inventory cannot pass --release")
        check("missing entry", lambda s,t: s["entries"].pop(), "expected exactly 200 per level")
        check("cross-level duplicate", lambda s,t: s["entries"][-1].update(
            word=s["entries"][0]["word"], part_of_speech=s["entries"][0]["part_of_speech"]), "duplicate headword/part-of-speech")
        check("fabricated approval", lambda s,t: s["entries"][0].update(reviewed_english=True), "reviewed_english must be explicitly false")
        check("fake reviewer", lambda s,t: t["tasks"][0].update(reviewer_identity="Unverified Person"), "unverified reviewer_identity must remain null")
        check("wrong source provenance", lambda s,t: t["tasks"][0].update(source_blob_sha="invalid"), "source provenance differs")
        check("relabelled task", lambda s,t: t["tasks"][0].update(task_id="CEFR1000-A1-9999"), "expected immutable sequential task_id")
        check("altered source shortlist SHA", lambda s,t: t.update(source_shortlist_blob_sha="invalid"), "Review task source shortlist provenance changed")
        check("false release status", lambda s,t: t.update(release_status="APPROVED"), "do-not-publish release status")
        # Additional independent corruption classes: every one must be a controlled
        # JSON rejection, never an exception masquerading as a passed test.
        check("missing Myanmar meaning", lambda s,t: s["entries"][0].update(burmese_meaning=""), "missing burmese_meaning")
        check("missing English definition", lambda s,t: s["entries"][0].update(english_definition=""), "missing english_definition")
        check("missing example sentence", lambda s,t: s["entries"][0].update(example_sentence=""), "missing example_sentence")
        check("missing source blob", lambda s,t: s["entries"][0].update(source_blob_sha=""), "missing source_blob_sha")
        check("unverified CEFR evidence URL", lambda s,t: t["tasks"][0].update(source_evidence_urls=["https://example.org/unreviewed"]), "unverified source_evidence_urls must remain empty")
        check("fabricated CEFR review", lambda s,t: t["tasks"][0].update(exact_sense_cefr_review="APPROVED"), "exact_sense_cefr_review must remain PENDING")
        check("fake signed review", lambda s,t: t["tasks"][0].update(reviewer_signed_at="2026-11-20T00:00:00Z"), "unverified reviewer_signed_at must remain null")
        check("invalid source index", lambda s,t: s["entries"][0].update(source_index=-1), "source_index must be a nonnegative integer")
        # Swap two task payloads but retain canonical ordinal IDs: the old
        # unordered set comparison accepted this provenance/identity corruption.
        def swap_payloads(s, t):
            first, second = t["tasks"][0], t["tasks"][1]
            for key in ("headword", "part_of_speech", "source_path", "source_index", "source_blob_sha"):
                first[key], second[key] = second[key], first[key]
        check("swapped review payloads with intact task IDs", swap_payloads,
              "positional review-task payload differs from immutable shortlist ordinal")
        # A1 matrix jobs must still reject corruption outside A1. Otherwise
        # a level-filtered job can report success despite global release risk.
        check("C1 fabricated approval caught by A1 matrix",
              lambda s,t: s["entries"][-1].update(reviewed_level=True),
              "reviewed_level must be explicitly false")
        check("B2 missing Myanmar meaning caught by A1 matrix",
              lambda s,t: next(e for e in s["entries"] if e["level"] == "B2").update(burmese_meaning=""),
              "missing burmese_meaning")
        check("A2 forged reviewer caught by A1 matrix",
              lambda s,t: next(x for x in t["tasks"] if x["level"] == "A2").update(reviewer_signed_at="2026-11-23T00:00:00Z"),
              "unverified reviewer_signed_at must remain null")
        print("All twenty negative cases rejected; provisional release also rejected; no independent review inferred.")

if __name__ == "__main__":
    main()
