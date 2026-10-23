# Burmese English Academy — Production Audio QA

Test date: 23 October 2026, Singapore. Target release: v1.2.5.

## Published build and full library
- GitHub Actions full Kokoro build 39935787562: success.
- 54 lessons; 1,000 IELTS vocabulary entries.
- Exactly 2,326 unique playable source texts; 4,652 files total, 2,326 George and 2,326 Emma.
- FFprobe automated checks passed for every MP3: decodable MP3 codec, mono, 24kHz sampling, positive duration.
- Validated complete manifest-to-text and file hash mapping for both voices; all physical files present.
- Static site measured 124,894,352 bytes in full build QC.
- GitHub Pages deployment 39943402731: successful, current full-audio production v1.2.4.

## Post-release regression
GitHub Actions regression run 39944672787 on the dedicated QA branch:
- Static text/MP3 integrity: passed.
- Chromium desktop: 432 lesson/tab render checks (54 × 8): passed.
- WebKit browser with iPhone 13 emulation: 64 representative lesson/tab render checks: passed.
- IELTS vocabulary search, topic filters, both voice-choice paths, play/stop routing: passed in both engines.
- 18 sampled MP3 HTTP responses with nonempty bodies: passed.
- Local browser-storage and cookie checks: passed.

## Scope limitations
- Mobile WebKit emulation is **not** a physical iPhone.
- Browser action tests stubbed `Audio.play()` to verify that click handlers route to the correct George/Emma file and stop; they do not prove audible output or complete media decoding on actual devices.
- User reported that the sampled live George/Emma audio worked on their iPhone; this does not certify all 4,652 clips.
- Automated codec integrity does **not** establish naturalness, stress, emotional quality, or correct pronunciation of every clip.
- There is no live user tracking or listening telemetry. No learner scores/preferences are saved.
- Traffic/load testing and monthly GitHub Pages bandwidth under real demand were not carried out.

## Release notes
Version 1.2.5 is a documentation/copy and maintainability update to match the existing prerecorded British audio reality. The previous website layout, 54 lessons, 1,000 bilingual vocabulary entries, two recorded UK voices, privacy commitments and lesson exercises remain intact.

## Rollback
Baseline full-audio deployed production commit before this QA: 4adedd1842cb2b4e038da8164bc644681765d2f1.
