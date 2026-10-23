#!/usr/bin/env python3
"""Count reusable live George/Emma clips for UNPUBLISHED A1 draft words.

Does not synthesize, overwrite or publish audio. Overlap does not imply
pronunciation has been listened to or approved.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOICES = ("bm_george", "bf_emma")


def main():
    a1 = json.loads((ROOT / "draft/A1-EDITORIAL-STARTER.json").read_text("utf8"))
    assert a1["release_status"] == "UNVERIFIED_DRAFT_DO_NOT_PUBLISH"
    entries = a1["entries"]
    assert len(entries) == 500
    manifest_text = (ROOT / "audio-manifest.js").read_text("utf8")
    manifest = json.loads(manifest_text[manifest_text.index("{"):manifest_text.rfind("}") + 1])
    clips = manifest.get("clips", {})
    assert len(clips) > 2000, "Released Kokoro catalogue is unexpectedly missing"

    expected = {}
    for row in entries:
        for kind, text in (
            ("word", row.get("display_word") or row["word"]),
            ("example", row["example_sentence"]),
        ):
            expected.setdefault(text.strip(), []).append((row["word"], kind))
    reusable = 0
    needs_generation = []
    existing_refs_missing_files = []
    for text, appearances in expected.items():
        sha = hashlib.sha256(text.encode("utf8")).hexdigest()[:24]
        for voice in VOICES:
            path = "audio/" + voice + "/" + sha + ".mp3"
            recorded = clips.get(text, {}).get(voice)
            file = ROOT / path
            if recorded == path and file.is_file() and file.stat().st_size >= 500:
                reusable += 1
            else:
                needs_generation.append({
                    "text": text, "voice": voice,
                    "a1_words": [x[0] for x in appearances],
                    "reason": "NOT_IN_RELEASED_AUDIO_CATALOGUE",
                })
                if recorded == path and not file.is_file():
                    existing_refs_missing_files.append(path)
    total = 2 * len(expected)
    assert total == reusable + len(needs_generation)
    report = {
        "classification": "A1_DRAFT_AUDIO_INVENTORY_ONLY_NOT_FOR_PUBLICATION",
        "a1_draft_words": len(entries),
        "distinct_word_and_example_passages": len(expected),
        "total_voice_recordings_required": total,
        "existing_legacy_clips_reusable_technically": reusable,
        "new_voice_recordings_missing": len(needs_generation),
        "existing_manifest_paths_without_files": existing_refs_missing_files,
        "new_recordings_reviewed_by_listener": 0,
        "recordings_to_generate": needs_generation,
    }
    output = ROOT / "draft/A1-AUDIO-REUSE-REPORT.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf8")
    print("A1 passages:", len(expected))
    print("Required voice recordings:", total)
    print("Already present in production audio catalogue:", reusable)
    print("New recordings missing:", len(needs_generation))
    print("Existing bad references:", len(existing_refs_missing_files))
    print("No recordings generated or released. Audio listening review PENDING.")
    if existing_refs_missing_files:
        raise SystemExit("Missing assets referenced by production manifest")


if __name__ == "__main__":
    main()
