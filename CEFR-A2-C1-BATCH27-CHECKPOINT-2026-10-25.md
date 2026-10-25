# Burmese English Academy — Batch27 staging checkpoint (25 October 2026)
**HOLD: UNVERIFIED DRAFTS ONLY. DO NOT MERGE OR PUBLISH.**
## Substantive work
- **50 original English–Myanmar vocabulary drafts**: A2 12, B1 15, B2 16, C1 7. Original English definition, Myanmar meaning and English usage example per entry. POS/CEFR are provisional candidate labels, not independently verified.
- **50 separate five-stage review packets** for dictionary exact sense/POS, natural Myanmar meaning, grammar/collocation, independently observed sense-specific CEFR, and George/Emma audio listening plus physical iPhone Safari checks. All review flags false; no observed evidence. Dictionary URLs are unvisited leads.
- **17 reversible candidate quarantines**: A2 4, B1 4, B2 4, C1 5. These are editorial holds, not independently sourced rejections.
- New five-way parallel A2/B1/B2/C1/ALL staging structural checks; no deployment or audio steps.
## Exact provisional inventory — unique written, not approved
| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 474 | 0 | 226 |
| B1 | 1,000 | 477 | 0 | 523 |
| B2 | 1,300 | 472 | 0 | 828 |
| C1 | 1,500 | 342 | 0 | 1,158 |
| **Total** | **5,000** | **2,265** | **0** | **2,735** |
A2–C1 unique first drafts: **1,765**; **182** legacy identical duplicate rows excluded. Distinct quarantined candidates: **426** (409+17). These counts await actual CI logs; structural checks are not linguistic approvals.
## Blockers
Candidate pool has unreliable WordNet senses and unsupported CEFR tiers. All C1 items especially require sense-level re-tiering. Some lower-level inflected/plural forms need headword policy. **hood** (dated/slang), **wireless** (dated), **wings** (figurative), **bath** (technical) and **runner** (specialized) need exact-sense source review. No independent English, Myanmar, examples or CEFR sign-off; no new CEFR George/Emma audio/listening, real-device Safari, hosting/bandwidth acceptance or live CEFR deployment.
Production 54 lessons, IELTS 1000 bank, existing George/Emma audio and privacy were not edited. CEFR publication data remains empty.
## CI and commit verification
**Observed real GitHub Actions outcomes, 25 October 2026 (04:14 UTC):**
- Initial commit `809c9de7944535317bd599c0518d581ffb43f1c3`: six staging-only files. Initial QA run [40161117879](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40161117879) failed B2 and ALL because the English definition for **mini** was too short (actual job logs `121072701613`, `121072701716` inspected). This was a **real QA failure**, not a linguistic review.
- Correction commit `a0daa74aebc784d61bb7b727607c8c26d984f580`: expanded the mini definition to a complete original sentence; no review status changed.
- Corrected QA run [40161146292](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40161146292): **completed/success**. Actual five jobs and decoded logs inspected: ALL `121072787415`, B2 `121072787480`, B1 `121072787489`, A2 `121072787495`, C1 `121072787554`; all **completed/success**. ALL log confirms `A2=474 B1=477 B2=472 C1=342 total=1765; independent approvals=0`, `A1=500; A1-C1 written=2265; first drafts outstanding=2735; legacy duplicate rows=182`, `50 drafts, 17 held, zero approvals; no audio/deploy`.
- Compared baseline `cc7fe9956c9bf4ba58fd55799d10d1e463ab40bd` to corrected `a0daa74aebc784d61bb7b727607c8c26d984f580`: **two commits; exactly six files** (three new draft JSON files, auditor, workflow and this checkpoint). No production lessons, IELTS bank, audio, UI or privacy file changed.
- Read `main` at `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from previous checkpoint. Staging `cefr-vocabulary-data.js` still has `entries:[]`.
- **Five-way CI success checks structural consistency only. It does NOT independently validate English/Myanmar linguistic truth, CEFR labels, pronunciation, hosting or real-device compatibility.**
