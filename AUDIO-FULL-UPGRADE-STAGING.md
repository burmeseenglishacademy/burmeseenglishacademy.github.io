# Archived staging instructions — full release published

This was the original staging plan and is no longer the current deployment state. Full George/Emma catalogue v1.2.4 was deployed to GitHub Pages on 23 October 2026. See [production audio QC](PRODUCTION-AUDIO-QC-2026-10-23.md).

---

# George & Emma full audio release — 23 October 2026

The automated Kokoro generation completed successfully in GitHub Actions run 39935787562. All 12 parallel synthesis shards succeeded. The release gate checked the 2,326 distinct English text strings across 54 lessons and 1,000 IELTS entries, both bm_george and bf_emma recordings for every text (4,652 MP3s total), file presence, MP3 codec, 24 kHz mono audio, positive duration, and total static site size below the 800 MB guard. The verified library was committed to the staging branch.

The full library is merged to main for GitHub Pages deployment. GitHub Pages success and live URLs must be checked separately.

Not yet verified: manual listening/pronunciation review of all recordings, physical iPhone Safari voice switching and playback, and real-traffic bandwidth performance. A GitHub Actions success does not prove these items.

The site preserves the original lessons, vocabulary, privacy protections, and UK-only device-voice fallback for unmatched text. No paid TTS API is required for playback.
