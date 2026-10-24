# BEA CEFR batch21 staging checkpoint — 25 October 2026 (SGT)

**STAGING ONLY — AI-ASSISTED UNVERIFIED DRAFTS — NEVER DEPLOY**

## Original substantive changes
- Added **46 new bilingual first-pass drafts**: A2 16, B1 14, B2 12, C1 4. Original English definitions, natural-language Myanmar draft meanings and grammatical examples are separate draft fields; these have not been independently reviewed.
- Created **46 five-stage independent review packets** for English/POS, Myanmar sense, examples, sense-specific CEFR evidence, and actual George/Emma listening. Cambridge URLs are unvisited reference leads, not observed evidence.
- Quarantined **20 additional distinct candidates** with named-entity, morphological, WordNet-sense, capitalization and level concerns. No permanent rejections without source review.
- Provisional C1 words are especially suspect: they remain unapproved and must be reclassified or held if source evidence does not support C1.
- Added parallelizable A2/B1/B2/C1/ALL GitHub Actions structural-only checks. **No job success claimed until actual runs and logs are inspected.**

## Exact inventory (written first passes, not verified)
| Level | Target | Unique first-pass written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 382 | 0 | 318 |
| B1 | 1,000 | 382 | 0 | 618 |
| B2 | 1,300 | 378 | 0 | 922 |
| C1 | 1,500 | 304 | 0 | 1,196 |
| **Total** | **5,000** | **1,946** | **0** | **3,054** |

The A2–C1 unique written total is **1,446**, excluding **182 identical legacy duplicate rows**. Candidate quarantine rises from **279 to 299** disjoint held words, pending structural CI confirmation.

## Gates and blockers
- Starting staging head: `753ee43379a33aba6a83d6bcb6262d1117ff865c`. The final content commit SHA and observed GitHub Actions run/job statuses must be added after execution, not invented.
- Independent linguistic/source review: **0 approvals**; George/Emma CEFR audio: **not generated/listening validated**; real-device iPhone Safari and hosting-budget checks: **not passed**; production deployment: **not performed**.
- Preserve `main`, 54 lessons, IELTS 1,000, George/Emma existing audio, privacy; `cefr-vocabulary-data.js` remains `entries:[]`. Never merge or publish these drafts.
