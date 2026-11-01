# CEFR 1,000 — George/Emma audio collision release safeguard (1 November 2026)

**Status: STAGING ONLY / RELEASE BLOCKED.** Approved scope is **1,000 total** (A1/A2/B1/B2/C1: 200 each), not the superseded 5,000-word proposal. This work neither generates nor listens to audio, independently approves content, modifies main, nor deploys.

## Mechanical failure mode and remedy

Before this checkpoint, `tools/validate_cefr_release.py` checked that expected audio-manifest paths existed, MP3 files exceeded a minimum size, and ffprobe decoded a minimum duration. Those checks **did not detect** the same MP3 bytes copied to both British voice paths, or the same MP3 reused for two different full-sentence examples. Such placeholders can satisfy file-presence/duration tests without representing two genuine voices or the requested spoken text.

The future approved-manifest `--audio` validation now hashes successfully probed MP3 bytes and fails closed for **identical bytes** in either of these cases:

- Same text labelled as both `bm_george` and `bf_emma`; these must be distinct real voice recordings.
- Different texts where at least one is a multiword utterance of three or more tokens; copying a whole example recording across different text is not acceptable.

The detector compares **every pair** in each equal-digest group (not only the first). It deliberately does **not** automatically reject same-voice single-word homophones such as *two* and *too*, whose waveforms can legitimately coincide. Other audio problems, including wrong pronunciation, accent, silent recordings with differing bytes, clipped words, prosody and listening-device behaviour, **still require real human listening**. No audio has been generated or listened to during this checkpoint.

## Synthetic negative tests and CI scope

`tests/cefr-release-evidence-gate.py` now exercises copied George/Emma bytes, reused multiword examples, legitimate short homophones, genuinely different voice hashes, and a three-record transitive collision case. All hashes in these tests are invented **synthetic fixtures**, never recording/listening receipts.

`.github/workflows/cefr-1000-selection-structural-qa.yml` now watches release-validator and regression-test changes and runs the regression in its **ALL** matrix lane, while preserving separate A1, A2, B1, B2, C1 and ALL structural jobs. It does not publish.

Code/test/workflow commit sequence: `67e4a1d6c01f89523f56be586e99d44136230218`, `f97ace1c0f11797f8f8346f55d4a87f0725bd437`, `c1a1facbb3e67497b7e17a2795c1e5c30caa279e`, `acb69bc3599913a5e3e783bc708d4c8e79a507f1`, `223a058efa840c3bb008156972e83effe497ed36`. Baseline `07608511fd7baf14bca9486913a842aa475c3772`; GitHub comparison shows **five staging commits touching only three files** (validator, regression tests, structural workflow). No protected production assets were modified.

**Verified GitHub Actions:** [six-lane structural run 41301101365](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41301101365) completed **SUCCESS** for A1, A2, B1, B2, C1 and ALL at code/workflow SHA `223a058efa840c3bb008156972e83effe497ed36`. Actual ALL job `124831996682` logs confirmed the new copied-voice/multiword synthetic regression **PASS**, exact 200-per-level first-pass shortlist and 0 independent approvals. Structural ALL artifact ID `13081790746`. [Release regression run 41301078798](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41301078798) completed **SUCCESS** at SHA `acb69bc3599913a5e3e783bc708d4c8e79a507f1`, job `124831928853`, with actual log confirming copied-George/Emma and multiword audio-risk tests. [Documentary no-deploy run 41301078773](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41301078773) completed **SUCCESS, report-only** at the same SHA, job `124831928564`; its steps confirmed missing human/audio/iPhone/hosting blockers were reported and protected production checks passed. Blocker artifact ID `13081112259`. A documentary workflow SUCCESS is **not** a release-gate PASS.

## Editorial and launch status

| CEFR | First-pass written | Independently approved | Editorial status |
| --- | ---: | ---: | --- |
| A1 | 200 | 0 | Held |
| A2 | 200 | 0 | Held |
| B1 | 200 | 0 | Held |
| B2 | 200 | 0 | Held |
| C1 | 200 | 0 | Held |
| **Total** | **1,000** | **0** | **Blocked** |

The separate approved 1,000-entry manifest is absent. Real George/Emma headword/example listening signoffs are **0**; real browser/mobile, physical iPhone Safari, hosting-limit and confirmed production-deployment signoffs are absent. Release remains **BLOCKED / STAGING ONLY**. The protected 54 lessons, IELTS 1,000-word bank, existing production George/Emma audio and privacy settings must remain unchanged.
