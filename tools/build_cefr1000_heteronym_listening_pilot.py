#!/usr/bin/env python3
"""Generate an unreviewed 14-word UK heteronym listening pilot on staging CI.

Source is the frozen 1,000-total CEFR draft and publisher-index pronunciation
risk leads. These samples have not been listened to and must NEVER be published.
Two texts x two UK voices per word -> 56 unapproved comparison samples.
"""
import hashlib
import json
import pathlib
import subprocess
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_kokoro_audio import synthesize, VOICES

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "scratch/cefr1000-heteronym-listening-pilot"
DATA = ROOT / "draft/CEFR-1000-PROVISIONAL-SHORTLIST.json"
RISK = ROOT / "draft/CEFR-1000-BRITISH-PRONUNCIATION-HETERONYMS-FOURTEEN-2026-11-01.json"


def probe_and_decode(p):
    probe = subprocess.run(
        ["ffprobe", "-v", "error",
         "-show_entries", "stream=codec_name,sample_rate,channels:format=duration",
         "-of", "json", str(p)],
        capture_output=True, text=True, check=True)
    d = json.loads(probe.stdout)
    stream = next(x for x in d["streams"] if x["codec_name"] == "mp3")
    seconds = float(d["format"]["duration"])
    if not (stream["sample_rate"] == "24000" and stream["channels"] == 1
            and seconds >= .12 and p.stat().st_size > 500):
        raise RuntimeError("Invalid technical audio encoding for " + str(p))
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-xerror",
                    "-i", str(p), "-f", "null", "-"],
                   stdout=subprocess.DEVNULL, check=True)
    return round(seconds, 3)


def main():
    from kokoro import KPipeline

    data = json.loads(DATA.read_text("utf-8"))
    assert data["release_status"].endswith("DO_NOT_PUBLISH")
    assert len(data["entries"]) == 1000
    assert Counter(e["level"] for e in data["entries"]) == dict.fromkeys(
        ("A1", "A2", "B1", "B2", "C1"), 200)
    risks = json.loads(RISK.read_text("utf-8"))
    assert len(risks["records"]) == risks["record_count"] == 14
    assert all(e["editorial_hold"] is True and not e["release_approved"]
               for e in data["entries"])
    pipe = KPipeline(lang_code="b")
    samples = []
    used = set()
    for risk in risks["records"]:
        matches = [e for e in data["entries"]
                   if e["level"] == risk["level"] and e["word"] == risk["word"]]
        if len(matches) != 1:
            raise RuntimeError("Risk word not uniquely located in frozen shortlist: " +
                               risk["level"] + "/" + risk["word"])
        e = matches[0]
        for kind, text in (("headword", e.get("display_word") or e["word"]),
                           ("example", e["example_sentence"])):
            text = text.strip()
            clip_id = hashlib.sha256(text.encode("utf-8")).hexdigest()[:24]
            for voice in VOICES:
                # Shared texts can reuse a physical file without duplicating recordings.
                rel = pathlib.Path(voice) / (clip_id + ".mp3")
                path = OUT / rel
                if (voice, clip_id) not in used:
                    synthesize(pipe, text, voice, path)
                    used.add((voice, clip_id))
                seconds = probe_and_decode(path)
                samples.append({
                    "level": risk["level"],
                    "word": risk["word"],
                    "part_of_speech": e["part_of_speech"],
                    "kind": kind, "voice": voice, "text": text,
                    "asset_path": rel.as_posix(),
                    "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                    "asset_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "bytes": path.stat().st_size, "seconds": seconds,
                    "publisher_index_ipa_lead_NOT_CERTIFIED":
                        risk["publisher_observation"].get("draft_uk_ipa"),
                    "pronunciation_risk_kind":
                        risk["publisher_observation"].get("risk_kind"),
                    "technical_decode": "PASS",
                    "human_listening": "NOT_PERFORMED",
                    "independent_approval": False
                })
    assert len(samples) == 56, len(samples)
    assert all(x["technical_decode"] == "PASS" for x in samples)
    assert all(x["human_listening"] == "NOT_PERFORMED" for x in samples)
    report = {
        "classification": "STAGING_ONLY_UNREVIEWED_DO_NOT_PUBLISH",
        "source": DATA.relative_to(ROOT).as_posix(),
        "source_risks": RISK.relative_to(ROOT).as_posix(),
        "words": 14, "sample_assignments": 56,
        "unique_recordings": len(used),
        "audio_bytes": sum(p.stat().st_size for p in OUT.rglob("*.mp3")),
        "automated_codec_decode": "PASS",
        "human_listening_signoffs": 0,
        "review_instructions": [
            "Listen separately to George and Emma HEADWORD and EXAMPLE clips.",
            "For heteronyms, verify correct word sense, part of speech, stress and UK pronunciation.",
            "Verify example grammar/English and original Burmese meaning with an independent reviewer.",
            "For ambiguous headwords, compare in-context example and flag wrong word-only stress.",
            "Never accept this manifest as final evidence; audio content and SHA can change after editorial correction."
        ],
        "samples": samples
    }
    (OUT / "review-manifest.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", "utf-8")
    print("PASS: 14 risk words; 56 audible-format sample assignments;",
          len(used), "unique MP3s; 0 actual human listening signoffs.")
    print("Samples are CI artifacts only and are NOT published to the website.")


if __name__ == "__main__":
    main()
