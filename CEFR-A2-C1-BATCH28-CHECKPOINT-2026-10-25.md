# Burmese English Academy — Batch28 staging checkpoint (25 October 2026)
**HOLD: UNVERIFIED DRAFTS ONLY. DO NOT MERGE OR PUBLISH.**

## Original editorial drafting
- **63 new original bilingual first-pass drafts:** A2 12, B1 20, B2 23, C1 8. English definition, natural Myanmar meaning and original usage example are separately marked **DRAFT**. WordNet pool senses and CEFR levels remain provisional, not independently checked.
- **63 independent-review packets:** English exact sense/POS, natural Myanmar, example grammar/collocation, sense-specific CEFR, and George/Emma audio listening plus real iPhone Safari, each separately pending with zero observed evidence. Cambridge links are unvisited leads, not proof.
- **14 reversible quarantines:** A2 5, B1 1, B2 3, C1 5; e.g. nationality capitalization, uncommon POS, named entities, wrong WordNet contraction senses, chemical symbols.
- Five parallel staging-only structural jobs (A2, B1, B2, C1, ALL); no deployment/audio job.

## Exact inventory — unique written, NOT approved
| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 486 | 0 | 214 |
| B1 | 1,000 | 497 | 0 | 503 |
| B2 | 1,300 | 495 | 0 | 805 |
| C1 | 1,500 | 350 | 0 | 1,150 |
| **Total** | **5,000** | **2,328** | **0** | **2,672** |

Unique A2–C1 drafts: **1,828** (legacy identical duplicate rows excluded); cumulative quarantined candidates **440** (426+14). Pending CI verification.

## Source and release blockers
No independent English dictionary sense/POS evidence, natural Myanmar sign-off, example sign-off or sense-level CEFR confirmation. Some candidate tiers are implausible and require re-tiering. No complete new CEFR George/Emma generation or human listening, physical iPhone Safari validation, hosting/bandwidth sign-off, or live CEFR deployment. Do not mistake a structural QA pass for editorial approval.

## Production preservation
No change requested to production 54 lessons, existing IELTS 1000 bank, existing George/Emma audio, learner privacy, or live site. Staging `cefr-vocabulary-data.js` remains empty. This batch adds only staging draft, review, quarantine, auditor, workflow and checkpoint files.

## Commit and CI evidence
**Observed GitHub Actions evidence (25 October 2026, 05:24 UTC):**
- Initial atomic staging commit `9f5abefaacd0c9a10d30a96e240a3030c1908e08` added **exactly six staging-only files**; GitHub compare against baseline `761b2f6c1391d0af0aa5902f545c1da4bbf7bd44` confirmed one commit, six additions, no production files modified.
- [Batch28 five-job CI run 40165436565](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40165436565) **completed/success**. Inspected all five actual job objects and decoded logs: A2 job `121085402556`, B1 `121085402432`, B2 `121085402592`, C1 `121085402566`, ALL `121085402583` — each completed/success.
- ALL log explicitly reports `A2=486 B1=497 B2=495 C1=350; A2-C1 unique=1828; independently approved=0`, `A1=500; total written=2328; unwritten=2672; legacy identical duplicate rows=182`, and `63 drafts, 14 held, zero approvals; no audio/deploy`.
- Checked live `main` at `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged since prior checkpoint.
- **Scope limitation:** these five jobs test structural consistency and unpublished status only; they do **not** verify dictionary truth, natural Myanmar, CEFR evidence, grammar by an independent reviewer, audio listening, mobile hardware or hosting limits.
