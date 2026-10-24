# BEA CEFR A2–C1 Batch16 staging checkpoint
Date: 25 October 2026 (SGT). Branch: `cefr-5000-bilingual-qa-staging`.

**STAGING ONLY — NOT RELEASE READY. DO NOT MERGE OR PUBLISH.**

## Original editorial work
- 50 additional original first-pass bilingual drafts: A2 14, B1 18, B2 14, C1 4. Each has an English learner definition, original Myanmar gloss, POS and grammatical contextual example. All remain unverified.
- 50 separate independent English/POS, Burmese, example, sense-specific CEFR and audio evidence tasks; no sources consulted for these new records and zero approvals.
- 16 additional provisional CEFR-level mismatches held out of drafting. They are suspected misplacements, not verified corrections or rejections.
- C1 remains especially risky: the four drafted C1 senses are high-priority source-review candidates, **not confirmed C1**.

## Exact unique draft inventory (conditional on successful five-way GitHub Actions QA)
| Level | Target | Previous unique drafts | New unique drafts | Expected unique total | Independently approved |
|---|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 500 | 0 |
| A2 | 700 | 298 | 14 | 312 | 0 |
| B1 | 1000 | 296 | 18 | 314 | 0 |
| B2 | 1300 | 298 | 14 | 312 | 0 |
| C1 | 1500 | 276 | 4 | 280 | 0 |
| **All** | **5000** | **1668** | **50** | **1718** | **0** |

Remaining unique first drafts: **3,282**. Prior identical legacy duplicate rows: **182**, excluded from unique counts. The five-way CI audit checks these exact counts against all files; do not treat these expected counts as confirmed until its ALL job succeeds.

## QA and release blockers
- Automated structural checks, headword/example matching, cross-batch uniqueness, candidate alignment, quarantine separation and false-approval guards are distinct from independent linguistic review.
- Source URLs in review tasks are unvisited lookup leads, **not evidence of consultation or approval**.
- New George/Emma recordings and human listening checks are not completed; no physical iPhone Safari regression of the final corpus, hosting-capacity verification or production deployment.
- Production 54 lessons, IELTS 1000 bank, existing George/Emma audio, privacy and live Firebase are intentionally untouched.
- Production `main` baseline at preparation: `dca0db7aa30118ecc18350db8dc406e6cac91554`. Verify again after CI.
- GitHub Actions run IDs, conclusions and any corrections must be appended only after actual observation.
