# CEFR-1000 staging CI evidence and release blockers — 2026-11-11

Scope: approved **1,000 total** (A1/A2/B1/B2/C1: 200 each), NOT the superseded 5,000-word plan. This document is a staging-only observation, not independent editorial approval or release authorization.

## Verified GitHub Actions observation
- Observation date: 2026-11-11 UTC.
- Source: https://api.github.com/repos/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42953145166
- Workflow run ID **42953145166**, push event, head SHA **882e6a62859df59c7644b50d431f4da0d131a01e**, status **completed**, conclusion **success**, started 2026-11-11T03:29:59Z, updated 2026-11-11T03:30:20Z.
- Job-list source: https://api.github.com/repos/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42953145166/jobs?per_page=100
- Jobs: adversarial regression **130301948901 success**; A1 **130301952506 success**; A2 **130301949027 success**; B1 **130301949153 success**; B2 **130301950041 success**; C1 **130301949182 success**; staging-only never-deploy **130302033164 success**. Each job's listed steps concluded success.
- Workflow source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/.github/workflows/cefr-1000-staging-release-preflight.yml
- The adversarial job runs the 12-case negative-path test file; the five matrix jobs assert 200 provisional entries per level, editorial holds, zero approval flags, and no duplicate normalized word/POS *within each level*. The last job expressly does not deploy.
- **Log limitation:** direct fetch of the individual job log was not supported by the available GitHub connector. Job and step conclusions were inspected from the jobs API; individual raw log output was **not** independently examined. Do not claim log-level verification.
- **Important limitation:** a successful staging *negative-path* test does not imply the full release gate passes, publisher-backed CEFR evidence exists, audio was generated or listened to, or iPhone QA occurred.

## Exact editorial and release state
| Level | First-pass written | Independently checked | Independently approved | Final audio/listening evidence |
|---|---:|---:|---:|---|
| A1 | 200 | 0 evidenced | 0 | Not verified |
| A2 | 200 | 0 evidenced | 0 | Not verified |
| B1 | 200 | 0 evidenced | 0 | Not verified |
| B2 | 200 | 0 evidenced | 0 | Not verified |
| C1 | 200 | 0 evidenced | 0 | Not verified |
| **Total** | **1,000** | **0 evidenced** | **0** | **4,000 required audio items unverified** |

Counts and holds are supported by the staging workflow's successful structural checks, not by independent language review. Do not infer a positive signoff from these assertions.

## Unresolved gate and risk inventory
1. Each entry needs publisher-supported **exact-sense** CEFR evidence with URL, observation date, locator and POS; a dictionary headword lookup alone is insufficient. Previously documented conflicts include B2 *portion* (food serving vs broader share) and C1 *integrity* (moral honesty listed at C2 by the previously consulted Cambridge source). Resolve by genuine sense evidence and independent adjudication, not automatic level promotion.
2. Independent English definition, fluent Myanmar meaning, original example grammar, exact-sense/CEFR and pronunciation review: **no independent signoffs evidenced**. Do not change flags.
3. Final George/Emma British voice files for headword and example (2 voices × 2 utterances × 1,000 entries = **4,000 artifacts**) plus real per-file listening signoff: **not evidenced**.
4. Browser/mobile regression, **physical iPhone Safari** test with device/session evidence, GitHub Pages hosting size/path/bandwidth assessment, current release-candidate CI and final production verification: **not evidenced**.
5. Protect the existing **54 lessons**, separate **IELTS 1,000-word bank**, production George/Emma audio, privacy constraints and main branch. This CI run makes no release or deployment claim.

**Disposition: BLOCK / STAGING ONLY.** No public launch, merge or production changes authorized by this report. Human-independent reviewers and actual device/audio evidence remain essential.
