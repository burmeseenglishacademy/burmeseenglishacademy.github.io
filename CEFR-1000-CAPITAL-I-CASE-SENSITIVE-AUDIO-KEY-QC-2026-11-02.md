> **Final verified CI addendum (2 Nov 2026).** All four newest staging workflows tested SHA `88c351735a13918be14082c87016ac7062525a0e` and completed **SUCCESS**: [six-lane structural 41330436098](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436098) (A1/A2/B1/B2/C1/ALL, ALL job `124919194763`, artifact `13093600257`); [documentary no-deploy 41330436142](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436142) (job `124919194516`, blocker artifact `13092848408`); [release regression 41330436114](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436114) (job `124919195424`); [integrated A1 regression 41330436134](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436134). Actual job logs confirm capital-I/exact-whitespace negative cases, 200 written/0 approved per level, zero human word-review receipts, zero final George/Emma real listening receipts, preserved protected production assets and missing physical iPhone/hosting/approved-manifest gates. **CI SUCCESS is structural/report-only, NOT release approval. RELEASE BLOCKED / STAGING ONLY.**

# CEFR 1,000 — capital-I audio-key / canonical headword release regression
**Observed:** 2026-11-02 (Singapore). **Scope:** user-approved 1,000 TOTAL, A1/A2/B1/B2/C1 200 each. **Branch:** `cefr-5000-bilingual-qa-staging`. **State:** RELEASE BLOCKED; no deployment.

## Concrete defect and repair
The held A1 first-person pronoun is spelled `i` in the provisional shortlist (source blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, starter `draft/A1-EDITORIAL-STARTER.json` index 3, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`). British Council's [capitalisation guidance](https://takeielts.britishcouncil.org/blog/capital-letters-in-english-common-errors-and-how-to-fix-them), directly observed 2026-11-01 in the [ten-record source packet](draft/CEFR-1000-UK-ORTHOGRAPHY-CAPITAL-I-AND-SPELLING-TEN-2026-11-01.json), supports `I` as the required display form; this is spelling guidance, NOT independent CEFR evidence.

The future release validator already blocked lowercase display `i`, but its audio collector unconditionally lowercased every headword before looking up `audio-manifest.js` keys and computing the SHA256-derived filename. Thus even a legitimately capitalised `I` release record would request the **wrong lowercase `i` recording**. The production audio manifest uses exact-case text keys and hashes; a lowercase-`i` file is not equivalent to `I`.

Repaired `tools/validate_cefr_release.py` to collect exact canonical **display** headwords for audio lookup, retaining `I` while rejecting ordinary mixed-case `Apple`/`APPLE`. Example text retains original case. Added regression cases in `tests/cefr-release-evidence-gate.py` verifying the `I` manifest key, distinct `I` vs `i` SHA filenames, and mixed-case rejection. These are synthetic structural tests, NOT actual generation or listening.

**Code commit:** `c7f27c7460264fe994d2467e4ade74c243b6c70d`. **Test commit:** `09449834cb63992a31f7d3562669981ba04930d1`.

## Additional exact-whitespace mismatch repaired
The original release validator also normalised leading/trailing spaces and repeated spaces in headwords/examples before looking up audio. This could silently map the user-visible `I eat  an apple.` to a different `I eat an apple.` recording, or accept ` apple ` while looking up `apple`. A future release must not approve audio for text that differs from what the learner sees.

Added explicit fail-closed checks for canonical raw headword and example whitespace, and synthetic negative tests for padded headwords, double spaces, trailing spaces and newlines. The helper still preserves exact canonical text and does not create audio. **Additional code commit:** `47f99b16866b01cb28ac8650b231a90162653ea5`; **additional test commit:** `88c351735a13918be14082c87016ac7062525a0e`.

[Release regression 41330436114](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436114), job `124919195424`: **SUCCESS at `88c351735`**. Actual logs confirm the new case and whitespace adversarial controls and unchanged empty published CEFR bank. [Integrated A1 regression 41330436134](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436134) also **SUCCESS**. [Six-lane structural run 41330436098](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436098) and [documentary run 41330436142](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330436142) are **pending final verification** at this addendum.

## GitHub Actions evidence
- [Release regression run 41330333104](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330333104), job `124918882105`: **SUCCESS** at test commit `09449834`; actual logs explicitly confirm the new capital-I audio/hash and canonical casing tests passed and the published CEFR bank remains empty.
- [Integrated A1 regression run 41330333096](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330333096), job `124918881853`: **SUCCESS**; actual logs confirm existing 54 lessons, separate IELTS 1,000 entries, 4,652 existing production MP3 paths, and privacy/static safeguards. This is an automated baseline test, not a new human preservation signoff.
- [Parallel six-lane structural run 41330333084](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330333084): **pending final job conclusions/logs at checkpoint creation**.
- [Documentary no-deploy run 41330333107](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41330333107): **pending final conclusion/logs at checkpoint creation**.

## Accurate release blockers
| Level | First-pass written | Independently approved | Editorial hold |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |

The 995/1,000 historical Oxford word/POS research coverage is not exact-sense independent CEFR review. Four inflected A1 items and rabbit still require resolution. No final independently approved 1,000-word manifest, no human-independent English/Myanmar/example/CEFR receipts, no completed final George/Emma headword+example audio with real listening signoffs, no final approved-corpus browser/mobile regressions, no physical iPhone Safari testing, no measured GitHub Pages hosting signoff and no confirmed production deployment. Existing production audio is separate and must remain protected.

**Never count this repair as linguistic review, actual voice listening, physical device testing, release readiness or publication. Main unchanged; no merge or deploy.**
