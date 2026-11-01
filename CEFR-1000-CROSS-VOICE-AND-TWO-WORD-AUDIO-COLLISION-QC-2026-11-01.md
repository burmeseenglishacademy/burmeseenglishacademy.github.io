# CEFR 1,000 — cross-voice and two-word MP3 collision hardening (1 November 2026)

**STAGING ONLY — RELEASE BLOCKED.** This checkpoint applies only to the approved **1,000 total** A1–C1 vocabulary project (200 provisional cards per level), not the superseded 5,000-word plan. No main-branch edits, merge, public deployment, audio generation, independent approval or real listening were performed.

## Defect found

The previous mechanical MP3-byte collision check rejected George/Emma identical bytes only when the *text* was identical. Thus a George recording labelled `apple` could be reused unchanged as an Emma recording labelled `orange` without this check detecting it. It also rejected copied same-voice recordings of *different texts* only if one text contained **three or more words**. Two-word examples such as `Good morning` and `Good evening` could therefore share identical bytes without triggering the detector.

## Fail-closed fix

`tools/validate_cefr_release.py` now rejects byte-identical MP3s across **any different George/Emma voice IDs**, even for different words. For the **same voice**, different texts with **two or more tokens** must not share byte-identical MP3s. Identical single-word homophones within the same voice (for example `two` and `too`) remain structurally permissible, but must be listened to by a real reviewer. These tests are mechanical and **cannot** establish accent, content, pronunciation, audio quality, or actual playback/listening signoff.

`tests/cefr-release-evidence-gate.py` now includes synthetic negative cases for cross-voice different-word reuse, two-word example reuse, transitive collisions involving two legitimate homophones, and a positive control for different recordings of one text. No synthetic fingerprint is a real recording or signoff.

## Provenance, regression and safety

Code commit: `eeec160d877112ae3fd8c654905a230892b56510`; regression-test commit: `7f3e97325e2493090b74a7698b8cf0721392b3ce`. [Git comparison](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/compare/9d7838939ea0675bf92e4d9fa8f4d37a3d95bd3b...7f3e97325e2493090b74a7698b8cf0721392b3ce) confirms only two staging files changed. An intermediate code-only push triggered failing tests at run `41307605282`, because its old transitive-collision expectation did not yet account for the newly detected cross-voice pair. The follow-up test commit corrects that expectation; do not claim the intermediate run passed.

At code+test SHA `7f3e97325e2493090b74a7698b8cf0721392b3ce`, [release regression run 41307633818](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41307633818) and [integrated A1 staging regression run 41307633821](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41307633821) completed SUCCESS. The six-lane structural run [41307633878](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41307633878) and documentary no-deployment run [41307633836](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41307633836) were **still running at the time of this checkpoint**; their final conclusions must be verified from actual jobs/logs before any claim of success.

## Independent readiness remains blocked

Readback of the frozen provisional shortlist: **1,000 entries**, A1 200, A2 200, B1 200, B2 200, C1 200, **0 independent approvals in each level**, all 1,000 editorial holds intact, no duplicate case-folded headwords and no `reviewed_*` true values. This is first-pass writing, **not** independent linguistic verification. Final approved release manifest, complete British George/Emma headword/example recordings, actual human listening receipts, browser/mobile and physical iPhone Safari regression, GitHub Pages hosting-limit evidence and confirmed live production deployment remain absent. Existing 54 lessons, IELTS 1,000-word bank, production George/Emma audio and privacy must remain protected. **Do not merge, publish or change main.**
