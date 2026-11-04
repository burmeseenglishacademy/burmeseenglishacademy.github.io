#!/usr/bin/env python3
"""Staging-only CEFR-1000 audio availability and technical decoding inventory.

Never generate, edit or publish an MP3, never certify a listening receipt.
Existing recordings are reusable only when the exact UTF-8 source text and
both expected physical files match the released manifest and ffprobe checks.
A matching audio file does NOT guarantee the correct sense/UK pronunciation.
"""
import argparse
import csv
import hashlib
import json
import pathlib
import subprocess
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
VOICES = ("bm_george", "bf_emma")
LEVELS = ("A1", "A2", "B1", "B2", "C1")
SOURCE = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
MANIFEST = ROOT / "audio-manifest.js"
OUTPUT = ROOT / "scratch/cefr1000-audio-readiness"
RISK = ROOT / "draft/CEFR-1000-BRITISH-PRONUNCIATION-HETERONYMS-FOURTEEN-2026-11-01.json"


def manifest_clips():
    text = MANIFEST.read_text("utf-8")
    start = text.index("window.BEA_AUDIO_MANIFEST=") + len("window.BEA_AUDIO_MANIFEST=")
    data = json.loads(text[start:].strip().removesuffix(";"))
    assert isinstance(data.get("clips"), dict), "Invalid released audio manifest"
    return data["clips"]


def inspect_audio(path, expected_codec=True):
    """Probe format/duration and SHA256 of files actually on disk."""
    p = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "stream=codec_name,sample_rate,channels:format=duration",
         "-of", "json", str(path)], check=False, capture_output=True, text=True)
    if p.returncode:
        return {"ok": False, "error": "FFPROBE_FAILED"}
    try:
        data = json.loads(p.stdout)
        stream = next(x for x in data["streams"] if x["codec_name"] == "mp3")
        seconds = float(data["format"]["duration"])
        good = (stream["sample_rate"] == "24000" and stream["channels"] == 1
                and seconds >= .12 and path.stat().st_size > 500)
        return {"ok": good, "seconds": round(seconds, 3),
                "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "codec": stream["codec_name"],
                "sample_rate": stream["sample_rate"], "channels": stream["channels"]}
    except (ValueError, TypeError, KeyError, IndexError, StopIteration):
        return {"ok": False, "error": "INVALID_MP3_METADATA"}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--skip-probe", action="store_true", help="inventory only; no media validation")
    args = p.parse_args()
    src = json.loads(SOURCE.read_text("utf-8"))
    assert src["release_status"].endswith("DO_NOT_PUBLISH"), "Unexpected draft scope"
    entries = src["entries"]
    assert len(entries) == 1000, "Exactly 1000 provisional entries required"
    assert Counter(e["level"] for e in entries) == Counter({k: 200 for k in LEVELS})
    assert all(e["editorial_hold"] is True and e["release_approved"] is False for e in entries)
    clips = manifest_clips()
    expected = defaultdict(list)
    by_level = {}
    for i, entry in enumerate(entries):
        level = entry["level"]
        for kind, text in (("headword", entry.get("display_word") or entry["word"]),
                           ("example", entry["example_sentence"])):
            assert isinstance(text, str) and text.strip(), (level, i, kind)
            text = text.strip()
            expected[text].append({"entry_index": i, "level": level,
                                   "word": entry["word"], "kind": kind,
                                   "part_of_speech": entry.get("part_of_speech")})
        by_level.setdefault(level, 0)
        by_level[level] += 1
    rows = []
    status = Counter()
    per_level = defaultdict(Counter)
    failed = []
    for text, uses in expected.items():
        audio_id = hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]
        for voice in VOICES:
            rel = f"audio/{voice}/{audio_id}.mp3"
            current = clips.get(text, {}).get(voice)
            file = ROOT / rel
            state = "MISSING_NEW_RECORDING"
            media = {}
            if current == rel and file.is_file():
                if args.skip_probe:
                    state = "PRESENT_NOT_MEDIA_PROBED"
                else:
                    media = inspect_audio(file)
                    state = "REUSABLE_TECHNICALLY" if media["ok"] else "INVALID_EXISTING_MEDIA"
            elif current == rel and not file.is_file():
                state = "MANIFEST_REFERENCE_MISSING_FILE"
            elif file.is_file() and current != rel:
                state = "UNMANIFESTED_OR_MISMATCHED_FILE"
            row = {"text": text, "voice": voice, "kind": uses[0]["kind"],
                   "audio_id": audio_id, "expected_path": rel, "state": state,
                   "used_by": uses, "technical": media,
                   "listening_review": "NOT_PERFORMED",
                   "pronunciation_approved": False}
            rows.append(row)
            status[state] += 1
            for level in set(u["level"] for u in uses):
                per_level[level][state] += 1
            if state in ("MANIFEST_REFERENCE_MISSING_FILE", "INVALID_EXISTING_MEDIA"):
                failed.append(row)
    risk_data = json.loads(RISK.read_text("utf-8"))
    risks = []
    for item in risk_data["records"]:
        word = item["word"]
        refs = [x for x in entries if x["word"] == word and x["level"] == item["level"]]
        if refs:
            risks.append({"word": word, "level": item["level"],
                          "risk_kind": item["publisher_observation"].get("risk_kind"),
                          "target_uk_ipa_research_only": item["publisher_observation"].get("draft_uk_ipa"),
                          "listening_review": "NOT_PERFORMED"})
    OUTPUT.mkdir(parents=True, exist_ok=True)
    report = {
        "status": "PRELIMINARY_AUDIO_TECHNICAL_INVENTORY_NO_LISTENING_APPROVAL",
        "source": str(SOURCE.relative_to(ROOT)), "manifest": str(MANIFEST.relative_to(ROOT)),
        "provisional_entries": len(entries),
        "per_level_entries": by_level,
        "distinct_text_passages": len(expected),
        "expected_distinct_recordings": len(rows),
        "recordings_by_availability": dict(status),
        "per_level_unique_recording_counts": {k: dict(v) for k, v in per_level.items()},
        "existing_invalid_count": len(failed),
        "heteronym_source_risk_entries": risks,
        "independently_listened_and_approved_count": 0,
        "limitations": [
            "Technical availability/ffprobe/sha256 is not actual audible listening.",
            "This does not perform ASR transcript comparison or UK IPA/accent assessment.",
            "Existing recordings may pronounce heteronyms incorrectly out of context.",
            "Provisional editorial data must not be approved or published.",
            "Recordings absent from released catalogue are not presumed to exist.",
            "No live website, main branch, existing MP3, reviewer flag or license is modified."
        ]
    }
    (OUTPUT / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", "utf-8")
    with (OUTPUT / "audio_review_queue.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["level", "word", "part_of_speech", "kind", "voice",
                         "spoken_text", "availability", "expected_audio_path",
                         "audio_sha256", "listening_status"])
        for row in rows:
            for use in row["used_by"]:
                writer.writerow([use["level"], use["word"], use["part_of_speech"],
                                 use["kind"], row["voice"], row["text"],
                                 row["state"], row["expected_path"],
                                 row["technical"].get("sha256", ""), "NOT_PERFORMED"])
    print(json.dumps({k: report[k] for k in ("status", "provisional_entries",
            "per_level_entries", "distinct_text_passages",
            "expected_distinct_recordings", "recordings_by_availability",
            "existing_invalid_count", "independently_listened_and_approved_count")},
                     ensure_ascii=False, indent=2))
    if failed:
        raise SystemExit(f"Existing production-referenced audio integrity problems: {len(failed)}")
    print("PASS: technical inventory prepared; human listening certification remains 0.")


if __name__ == "__main__":
    main()
