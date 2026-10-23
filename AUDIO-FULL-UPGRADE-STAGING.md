# George/Emma full-audio staging — 23 October 2026

**Not live:** Files on this branch are preliminary. Do not merge or switch GitHub Pages to this branch before a full verified catalogue is built.

Current main branch has 10 Kokoro pilot MP3s (five unique passages × two voices); the original Web Speech system remains the default for lessons and vocabulary.

Read from current main sources:
- 54 lessons and 1,000 IELTS entries;
- 2,326 distinct playable English text strings (including voice preview);
- 4,652 George/Emma MP3s required for full coverage.
- Existing pilot recordings: 10. Additional recordings required: 4,642, assuming the matching text hashes and files are valid.

Local unit checks: catalogue fixture generation, voice switching/fallback, JavaScript syntax, Python syntax passed. **Not tested**: producing all Kokoro speech in this environment, hearing every file, actual iPhone Safari playback, GitHub Pages under real traffic.

Before deployment:
1. Generate all files offline using licensed Kokoro British voices `bm_george` and `bf_emma`.
2. Verify decoding, duration, sample rates, file size, exact source-text coverage, and pronunciation through listening QA.
3. Update the `audio-manifest.js` to list only validated MP3s.
4. Add `audio-manifest.js`, `audio-player.js`, `audio-integration.js` as deferred scripts after `script.js` in `index.html`; ensure the first two files are not duplicated.
5. Retest all lesson, speaking, vocabulary and stop/play actions on desktop and actual iPhone Safari.
6. Only then publish a reviewed and approved change to `main`. Preserve all other page layouts, study data and privacy policies.

There is no paid API requirement in the scripts. First-run model download may require internet access; thereafter synthesis can run locally.
