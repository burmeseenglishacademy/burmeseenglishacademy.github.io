# CEFR-1000 staging CI verification — 2026-11-05

Scope: approved **1,000-total** plan (A1/A2/B1/B2/C1: 200 provisional each). Branch `cefr-5000-bilingual-qa-staging` only. This document records observed evidence, **not** independent lexical approval or launch authorization.

## Verified GitHub Actions evidence
- Run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41968185356
- Trigger: push; run created 2026-11-05 04:30:09 UTC; completed 04:30:27 UTC.
- Tested head commit: `0d2f98d82b5a25ca05431f9e26ccea0af78024a8`.
- Overall run conclusion: **success**.
- Parallel job conclusions (each **success**): A1 `127050003379`, A2 `127050003111`, B1 `127050003538`, B2 `127050003434`, C1 `127050003697`.
- A2 job log directly inspected: five negative fixtures passed (missing entries, empty provisional inventory, forged approved status, invalid level, missing manifest). The provisional shortlist was rejected by the guard, with `RELEASE BLOCKED (12011 findings)`, and the step printed `PASS: provisional shortlist blocked`.
- **Coverage limitation:** the workflow invokes `scripts/cefr1000-release-manifest-guard-negative-tests.cjs` (five cases), **not** the separate eight-case `scripts/cefr1000-guard-adversarial-smoke.cjs`. Therefore the eight-case suite is **not** claimed as CI-tested. Five parallel lanes repeat the same negative-test suite; they do not constitute five independent linguistic reviews or per-level semantic validation.
- GitHub-hosted runner reported Node 22.23.4. The log included a Node 20 action deprecation warning for `actions/checkout@v4` and `actions/setup-node@v4`; this did not fail this run.

## Editorial and release status (not independently reapproved)
| Level | Provisional first-pass | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1000** | **0** |

The provisional shortlist is **not** a release manifest. Publisher-backed exact-sense CEFR support, fluent Myanmar/English and example review, cross-level sense resolution, independent signoffs, 4,000 verified George/Emma headword/example audio files and **real listening**, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages hosting review, preserved production assets, and confirmed deployment remain unverified. The review-task JSON fetch returned empty content through the connector, so its individual tasks were not independently inspected in this run.

## Next staging-only safeguards
1. Wire the eight-case adversarial smoke suite into the five-lane workflow, and verify its actual logs; add positive-schema synthetic fixture tests without forging human review evidence.
2. Audit audio signatures, actual listening attestations, publisher exact-sense URLs, and reviewer independence by humans; structural hashes/URLs alone cannot establish authenticity.
3. Preserve the existing 54 lessons, separate IELTS 1,000-word bank, George/Emma production audio, and privacy policy. Do not merge or publish while any gate is absent.
