# CEFR 1,000 — independently reviewable handoff and fail-closed QC (29 October 2026)

**STAGING ONLY — RELEASE BLOCKED.** This checkpoint is for the user-approved **1,000 total** CEFR vocabulary entries, **200 each at A1, A2, B1, B2, C1**, not the obsolete 5,000-word target. The branch remains `cefr-5000-bilingual-qa-staging` by explicit instruction. No change to `main`, production site, protected 54 lessons, IELTS 1,000-word bank, existing George/Emma audio or privacy assets.

## New substantive staging work

Created [`tools/audit_cefr_1000_review_priority.py`](tools/audit_cefr_1000_review_priority.py), a deterministic **1,000-item human-review handoff generator**. It reads the frozen shortlist, all 21 audited Oxford observation packets, and the 36 historical recovered word/POS excerpts. It binds every task to the shortlist's original English definition, Myanmar meaning, example sentence, original source path/index/Git blob SHA and observed publisher evidence (when present). It explicitly leaves independent exact-sense, bilingual/example and both-voice listening signoffs **null**, and release approval **false**. A generated queue is not a review receipt or an approved manifest.

The queue separates five actionable editorial priorities:

| Editorial category | Distinct entries | Human action |
|---|---:|---|
| No direct Oxford word/POS observation in audited packets | **695** | Obtain dated official source observations and verify the intended sense; no invented CEFR |
| Oxford word/POS lower than provisional level | **119** | Reconcile sense/POS and justify level independently; never automatically retier |
| Oxford word/POS higher than provisional level | **7** | Reconcile source and intended sense independently |
| Absent from both inspected core lists | **3** | Research an authoritative sense-level source; absence is not a CEFR label |
| Oxford word/POS matches provisional level | **176** | Still requires independent exact-sense, English, Myanmar and example review |
| **Total** | **1,000** | **0 independently approved** |

Distinct Oxford word/POS coverage: **A1 100/200, A2 48/200, B1 60/200, B2 58/200, C1 39/200** = **305/1,000**. Historical 324 source observations contain 19 duplicate observations and do not establish 324 unique words. The 36 recovered historical PDF word/POS excerpts are cross-referenced to their immutable historical packet path, index, PDF page/line and publisher URL; **they do not increase the 305 unique total**. The three unlisted research words are `divine`, `officially` and `premises`. The 129 mismatched/unlisted entries must not be treated as independently adjudicated.

The generator validates the complete 1,000-entry queue, 200 tasks per level, original content/provenance, recovered source-locator alignment, distinct counts, and absence of independent approvals. It includes five deliberate tampering tests for forged exact-sense receipts, false listening, fake release approval, missing task and inflated publisher coverage. All five were rejected in executed CI. This is **structural** assurance, not independent linguistic verification or physical-device testing.

## Actual executed GitHub Actions evidence

- [Parallel structural run **40799763607**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40799763607), head commit `ba7b8bec435a18ad6d2d06a09421aa93e88ad27f`: **SUCCESS** across all six A1/A2/B1/B2/C1/ALL jobs. Actual ALL-job logs show the priority counts above, **5/5 tampering tests rejected**, a generated `cefr-1000-review-handoff-ALL.json`, and protected production diff PASS. The generated queue was uploaded to GitHub Actions artifact **`cefr-1000-provisional-ALL`** (artifact ID **12865616784**; 30-day retention). It is a review handoff, **not** an approval or public launch artifact.
- [Documentary no-deployment run **40799767324**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40799767324), head commit `9c567eaee5e93ab51fadfb58d41016d505df716a`: **SUCCESS as report-only**. Actual job logs confirm **5/5 forged review/coverage mutations rejected**, zero independent approvals, source coverage counts, launch blockers retained and protected production diff PASS. Success here means the fail-closed blocker logic executed correctly; it does **not** mean release readiness.
- Source observation dates in the underlying publisher research packets are **28–29 October 2026**. Publisher word/POS research is anchored to the [official Oxford 3000 PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf), with packet-specific page/line references. The present run re-audited stored evidence; it did **not** independently re-open all 305 publisher entries or independently verify their exact senses.

## Exact release blockers

| Level | First-pass written | Independently approved | Direct Oxford word/POS observed |
|---|---:|---:|---:|
| A1 | 200 | 0 | 100 |
| A2 | 200 | 0 | 48 |
| B1 | 200 | 0 | 60 |
| B2 | 200 | 0 | 58 |
| C1 | 200 | 0 | 39 |
| **Total** | **1,000** | **0** | **305** |

No authenticated independent English/Myanmar/example/exact-sense CEFR signoffs exist. Final George **and** Emma headword+example generation and **real listening signoffs remain 0/1,000**. Approved-corpus browser/mobile regression, **real physical iPhone Safari** review, measured GitHub Pages hosting limits, authenticated release manifest and confirmed production deployment remain **not verified**. No audio listening or physical-device testing was performed in this run. Human-independent review is a required external gate; automated self-checks must not be relabelled independent approval.

**Next staging work:** use the generated queue to prioritize the 129 discrepant/unlisted senses and 695 source gaps, collect exact-sense publisher citations with observation dates, and obtain separate genuine human English/Myanmar/example/CEFR receipts. Preserve all protected production paths and continue CI; do not merge, publish or mark release ready until all release gates actually pass.

**Final status: BLOCKED / STAGING ONLY.**
