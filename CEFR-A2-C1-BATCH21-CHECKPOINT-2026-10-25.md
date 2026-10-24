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

## Actual commits and GitHub Actions evidence (observed after execution)

- Initial six-file staging commit: [`79098dfa5c8e407f3531734229a94a5ffe837548`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/79098dfa5c8e407f3531734229a94a5ffe837548).
- Corrections: [`0fb73080`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/0fb73080eb73c7e71ef54ce52518ca4d121b38c4) removed a previously drafted duplicate C1 word; [`f57f3294`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/f57f3294ace2bc99d647d7fc6ca7941264e2ebf6) corrected a quarantine-audit type error; [`a41f89c2`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/a41f89c292cbd93af4df4d21578224d5701194be) and [`05d90e22`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/05d90e223b76729d94c6bcf1110037092f3276b9) removed repeated quarantine candidates; [`0c419da3`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/0c419da3afcd011eb77faaeec787236da676b6b6) strengthened candidate-membership and provisional-tier checks.
- Earlier actual CI runs [40138124325](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40138124325), [40138187809](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40138187809), [40138207756](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40138207756), and [40138235781](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40138235781) **failed**. Inspected their real job logs, identified and corrected the issues; failures were not concealed.
- [Corrected run **40138271668**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40138271668) completed **success** across five jobs. The subsequent **stronger** [run **40138307108**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40138307108) also completed **success** at commit `0c419da3`; actual job statuses and decoded logs were read:
  - A2 job `121004462247`: completed / success, structural PASS.
  - B1 job `121004462569`: completed / success, structural PASS.
  - B2 job `121004462475`: completed / success, structural PASS.
  - C1 job `121004462416`: completed / success, structural PASS.
  - ALL job `121004462473`: completed / success; actual log: `A2=382 B1=382 B2=378 C1=304 total=1446; independent approvals=0`; `A1-C1 written=1946; first drafts outstanding=3054; legacy duplicate rows=182`.
- Staging CEFR release data was directly inspected and still contains `entries:[]`. Direct read of production `main` branch shows head `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from before this iteration.
- **All GitHub Actions results above are structural QA only.** They do not establish independently sourced CEFR correctness, natural Myanmar, grammar/collocation, authentic George/Emma listening, physical iPhone Safari compatibility or hosting-budget compliance. The 46 new entries remain **unapproved** and must not be merged or published.
