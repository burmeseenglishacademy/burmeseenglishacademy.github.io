# CEFR 1,000 — fourth A2 Oxford twelve, exact-sense holds and fail-closed QC
**29 October 2026 | STAGING ONLY | RELEASE BLOCKED**

This work concerns only the user-approved **1,000 total CEFR A1–C1 words** (200 each). The old 5,000-word proposal is superseded. All first-pass bilingual drafts remain held; no independent reviewer, listening, iPhone or production signoff is asserted. Branch remains `cefr-5000-bilingual-qa-staging`.

## Direct source-supported editorial research

Directly inspected [Oxford University Press, *The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-29**. Recorded **12 distinct new A2-draft word/POS observations**, with publisher URL, observed date, PDF page and extracted-line locator, original English/Myanmar/example snapshots and historical Git source path/index/blob SHA in [the immutable-style research packet](draft/CEFR-1000-OXFORD-A2-FOURTH-TWELVE-2026-10-29.json). The frozen shortlist was not modified.

| Draft A2 word | Oxford word/POS CEFR | Official PDF page (1-based), extracted line (0-based) | Editorial issue |
|---|---|---|---|
| level (noun) | A2 | 5, 1357 | Proficiency level vs degree/measurement |
| mind (noun) | A2 | 6, 1398 | Cognition definition vs *change one's mind* decision idiom in example |
| become (verb) | A1 | 1, 71 | Lower publisher word/POS classification |
| body (noun) | A1 | 1, 95 | Lower publisher word/POS classification |
| problem (noun) | A1 | 3, 623 | Lower publisher word/POS classification |
| almost (adverb) | A2 | 4, 934 | Nearly, not completely |
| win (verb) | A1 | 4, 882 | Lower publisher word/POS classification |
| idea (noun) | A1 | 2, 389 | Lower publisher word/POS classification |
| community (noun) | A2 | 4, 1067 | Neighbourhood vs shared-interest community |
| cause (verb) | A2 | 4, 1031 | Oxford combines noun and verb; draft uses verb |
| data (noun) | A2 | 5, 1105 | Information sense, number and Myanmar wording |
| general (adjective) | A2 | 5, 1246 | Broad overview vs nonspecific meaning |

**Five A1/A2 discrepancies, seven A2 word/POS matches.** These PDF classifications do **not** independently establish exact-sense CEFR, original example correctness or fluent Myanmar. Each item remains on editorial hold and requires genuine human-independent source-backed sense, English, Myanmar, example and British pronunciation review. No automatic retiering or rewrite was applied.

## Audited cross-batch coverage

| Level | First-pass written | Independently approved | Distinct direct Oxford word/POS observed |
|---|---:|---:|---:|
| A1 | 200 | 0 | 100 |
| A2 | 200 | 0 | **60** |
| B1 | 200 | 0 | 60 |
| B2 | 200 | 0 | 58 |
| C1 | 200 | 0 | 39 |
| **Total** | **1,000** | **0** | **317** |

Across **336** historical and new source observations, **19** duplicate observations were excluded from distinct coverage. The provenance-bound reviewer handoff now separates **683** words without direct Oxford word/POS observations, **124** with lower publisher classifications, **7** with higher classifications, **3** absent from the inspected core lists (absence is not a CEFR level), and **183** matching at word/POS level but still lacking independent exact-sense review. **134** mismatched/unlisted cases require explicit human reconciliation.

## Fail-closed staging and actual CI

Added [the fourth A2 integrity auditor](tools/audit_cefr_1000_oxford_a2_fourth_twelve.py) and connected it to all six parallel A1/A2/B1/B2/C1/ALL structural lanes and documentary no-deployment QC. It checks exact official PDF line/page/word/POS snapshots, shortlist and historical Git provenance, immutable English/Myanmar/example snapshots, reviewer-task content and absence of approvals. Its **80/80 negative mutation tests** reject forged source lines, changed bilingual content, fabricated receipts and false signoffs. Mechanical tests do **not** replace independent linguistic review.

- [Structural run **40807346511**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40807346511), commit `29a0b9b4d1d55d522703fc4b85c858cd70fda936`: **SUCCESS**, all six parallel lanes. Actual ALL-job logs confirm 12 A2 observations, 80/80 rejected mutations, 317 distinct coverage, updated 1,000-item human-review queue and protected production diff PASS. Reviewer artifact `cefr-1000-provisional-ALL`, ID **12868319354**; **not** an approved release manifest.
- [Documentary run **40807461472**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40807461472), commit `c3cbde8d61f98a9fe4ed2aeecf9d198a3ac9101c`: **SUCCESS as report-only**, not release readiness. Actual job logs confirm 80/80 mutation rejection, forged fourth-A2 human receipt rejected, zero approved entries, zero both-voice listening signoffs, absent approved manifest and mobile/WebKit evidence, protected production assets unchanged. An empty `oxford_a2_fourth_twelve_review_receipts` collection is mandatory; any retained word requires genuine independent content-hash-bound A2 exact-sense signoff. The five A1 conflicts additionally require documented reconciliation; `mind` requires separate phrase-sense resolution.
- Intermediate partial-commit CI failures were superseded by the successful complete-workflow runs above; no failed job is described as passing.

## Remaining blockers and production protection

**First-pass written/independently approved:** A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0. **Final George/Emma headword and example recordings actually listened to and signed off: 0/1,000.** No independently approved 1,000-word manifest, complete voice listening receipts, approved-corpus desktop/mobile regression, physical iPhone Safari evidence, measured GitHub Pages capacity or production deployment confirmation exists. Human-independent reviewers must supply authentic evidence; automation cannot sign on their behalf.

No merge, production publication or main-branch change occurred. The 54 production lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy assets remain protected. **Final release status: BLOCKED / STAGING ONLY.**
