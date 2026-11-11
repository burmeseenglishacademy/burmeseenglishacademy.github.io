# CEFR-1000 evidence-gate CI verification — 2026-11-12 (staging only)

## Scope and immutable release decision
User-approved scope: **1,000 total** (A1/A2/B1/B2/C1: 200 each); superseded 5,000-word plan is out of scope. This report is not a reviewer signoff or launch authorization. **RELEASE BLOCKED.** No main-branch change, deployment, approval-flag mutation or production audio change is authorized by this report.

## Actual CI verification
- Workflow run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/43076082683
- Tested commit: `1fc29e38714ab035c1a6514dc35047fb1ce295f4`.
- Retrieved actual raw logs from all five level jobs on 2026-11-12 (Singapore date); each log says `Ran 13 tests ... OK`, verifies exactly 1,000 shortlist entries and 200 in its level, prints `independent evidence absent; RELEASE BLOCKED`, and checks that the CLI exits nonzero with `PASS: staging release blocked`.
- A1 job 130716129963: conclusion success; raw log retrieved.
- A2 job 130716129980: conclusion success; raw log retrieved.
- B1 job 130716130196: conclusion success; raw log retrieved.
- B2 job 130716129885: job API returned `status: in_progress` alongside `conclusion: success` (internally inconsistent); all listed steps succeeded and raw log includes successful cleanup. Treat final job status as not conclusively verified until refreshed.
- C1 job 130716129524: conclusion success; raw log retrieved.
- The logs contain an `actions/checkout@v4` Node.js 20 deprecation warning (runner forces Node.js 24); not evidence of failed tests.

## Editorial inventory and evidence blockers
| Level | First-pass written | Independently checked/approved | Required voice audio | Listening signed off |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 800 | 0 verified |
| A2 | 200 | 0 | 800 | 0 verified |
| B1 | 200 | 0 | 800 | 0 verified |
| B2 | 200 | 0 | 800 | 0 verified |
| C1 | 200 | 0 | 800 | 0 verified |
| **Total** | **1,000** | **0** | **4,000** | **0 verified** |

Audio count is a **requirement**, not a claim that 4,000 audio files exist: 200 entries × two British voices (George and Emma) × headword/example × five levels. Final-shortlist audio generation and real listening are unverified. Each of 4,000 domain reviews (English, Myanmar, original example, publisher-backed exact-sense CEFR) requires genuine independent provenance, observation date, source URL and reviewer signoff. Existing first-pass entries remain on editorial hold. Physical iPhone Safari evidence, browser/mobile regression evidence, GitHub Pages capacity/hosting clearance, preservation of 54 lessons and separate IELTS 1,000 bank and production voice assets, and confirmed deployment remain missing or unverified.

## Next substantive editorial work
Prioritize publisher-backed exact-sense CEFR observations, cross-level sense conflicts, noncanonical/named-entity/WordNet-derived risks, fluent Myanmar and example grammar; keep evidence as proposed research until an independent human reviewer signs off. Preserve the shortlist source blob SHA and source URLs/dates. Do not populate review or audio approval fields from self-evaluation. Run the five parallel negative-regression jobs again after any code changes and inspect both conclusions and raw logs. Do not merge or publish while any release gate is missing.
