# BEA CEFR batch20 staging checkpoint — 25 October 2026 (SGT)

**STAGING ONLY / AI-ASSISTED DRAFTS / UNVERIFIED / NEVER DEPLOY**

## Substantive work
- Prepared **52 new original bilingual drafts**: A2 16, B1 16, B2 16, C1 4. Each has an independently authored first-pass English definition, Myanmar sense rendering, grammatical example and explicit editorial risk; this is drafting, not linguistic approval.
- Prepared **52 separate five-stage review packets** for English sense/POS, Myanmar meaning, example, sense-specific CEFR evidence, and real George/Emma listening. Cambridge URLs are **unvisited leads**, not observed sources.
- Quarantined **20 additional distinct candidates** with WordNet mismatches, named entities, capitalization, acronym, morphology and other issues. No permanent rejections without evidence.
- Added five-way A2/B1/B2/C1/ALL structural-only GitHub Actions checks. This checkpoint is written **before the new workflow executes**; do not claim CI success until real jobs and logs have been inspected.
- B2 and C1 include likely lower-level everyday words because the source's frequency-based tier is not authoritative. Their `LIKELY_LOWER_THAN_PROVISIONAL` and other risks require reclassification before any approval.

## Exact inventory after batch20 (assuming new audit confirms)
| Level | Curriculum target | Unique first-pass written | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 366 | 0 | 334 |
| B1 | 1,000 | 368 | 0 | 632 |
| B2 | 1,300 | 366 | 0 | 934 |
| C1 | 1,500 | 300 | 0 | 1,200 |
| **Total** | **5,000** | **1,900** | **0** | **3,100** |

A2–C1: 1,400 unique written headwords; legacy 182 duplicate rows excluded. Previously 259 held distinct candidates; 20 newly held disjoint words bring the hold count to 279, pending structural audit. Quarantine records are not drafts or approvals.

## Evidence and release blockers
- Starting staging head: `553edcf8455914ed6cf7d2e51a9711916e77d1dc`; this report and the draft/QA files will be committed atomically. The resulting commit SHA and actual job logs must be recorded in a follow-up evidence checkpoint, not invented here.
- Independent source-based English/Myanmar/CEFR/example reviews: **0 approved**. No new CEFR audio generation or actual listening; no physical iPhone Safari test; no measured hosting budget confirmation; no live CEFR release.
- `cefr-vocabulary-data.js` must stay empty, and the production 54 lessons, IELTS 1,000 bank, existing George/Emma recordings, privacy safeguards and `main` must remain untouched.
- **Do not merge, publish, or notify as completed.**

## Post-commit CI evidence (observed, not inferred)

- Batch20 atomic staging content commit: [`38dfd3001ed99598696854ec4eb77a33aa69ccf4`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/38dfd3001ed99598696854ec4eb77a33aa69ccf4).
- [Actual GitHub Actions run 40133472286](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40133472286): **completed / success**; individually fetched all five jobs and their decoded logs:
  - A2 job `120989951572`: completed / success; structural PASS.
  - B1 job `120989951561`: completed / success; structural PASS.
  - B2 job `120989951506`: completed / success; structural PASS.
  - C1 job `120989951582`: completed / success; structural PASS.
  - ALL job `120989951635`: completed / success; `A2=366 B1=368 B2=366 C1=300 total=1400; independent approvals=0`, `A1-C1 written=1900; first drafts outstanding=3100; legacy duplicate rows=182`.
- Read the real `main` branch metadata: production head was `dca0db7aa30118ecc18350db8dc406e6cac91554` at this inspection. Staging CEFR release file still has `entries:[]`.
- **Limits:** These CI passes are structural only; they cannot establish sense-specific English correctness, natural Burmese, true CEFR levels, authentic listening quality, physical iPhone Safari behavior or GitHub Pages budget.
- **Review blockers remain:** 3,100 unwritten first drafts, 5,000 independent editorial approvals, new CEFR George/Emma recordings plus listening, mobile/device and hosting verification, and confirmed production deployment. No merge, no new CEFR publication, no completion notification.
