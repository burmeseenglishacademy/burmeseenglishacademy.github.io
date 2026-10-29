# CEFR 1,000 — A1 ninth Oxford 12: family and everyday nouns — verified staging QC

**Date:** 2026-10-29 (Singapore). **Branch:** `cefr-5000-bilingual-qa-staging`. **Code commit:** `9015cba07bb58fb155d8a753304a9f37c5f6236e`. **Release:** **BLOCKED / STAGING ONLY**. User-approved total remains **1,000** (200 per A1, A2, B1, B2, C1); the superseded 5,000-word scope is not active.

## Source-supported editorial research, not independent signoff

Directly inspected the [official Oxford University Press Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-29**. The following **12 previously unobserved A1-draft nouns** are listed in the PDF's A1 word/POS section. Page numbers are **one-based PDF pages**; line locators are **zero-based extracted web text lines**, not printed page line numbers. Publisher word/POS classification does **not** establish the exact drafted sense or human approval.

| Provisional headword | Oxford PDF page / line | Publisher entry | Independent-review focus |
|---|---:|---|---|
| sister | 3 / 700 | sister n. | Myanmar older/younger sister distinction |
| son | 3 / 719 | son n. | Parent-child relationship, Myanmar naturalness |
| daughter | 1 / 194 | daughter n. | Parent-child relationship, Myanmar naturalness |
| grandmother | 2 / 335 | grandmother n. | အဘွား / အဖွား spelling and kinship nuance |
| grandfather | 2 / 334 | grandfather n. | Maternal/paternal kinship nuance |
| uncle | 4 / 834 | uncle n. | Blood versus marriage, Myanmar kinship |
| aunt | 1 / 52 | aunt n. | Blood versus marriage, Myanmar kinship |
| phone | 3 / 588 | phone n., v. | Draft device noun versus listed verb sense |
| computer | 1 / 168 | computer n. | Broad electronic-device definition versus computing sense |
| picture | 3 / 593 | picture n. | Image, drawing, painting and photograph |
| bag | 1 / 58 | bag n. | Carrying-container noun versus other senses |
| money | 2 / 492 | money n. | Draft coins/notes definition may omit non-cash money |

All 12 records preserve the **frozen English definition, Myanmar meaning, original example, historical source path/index/Git blob SHA, publisher URL, observation date, PDF locator and source excerpt** in [the staging evidence packet](draft/CEFR-1000-OXFORD-A1-NINTH-TWELVE-2026-10-29.json). Each has an explicit independent reviewer task, editorial hold, no reviewer receipt and no approval. No proposed correction was applied to the shortlist.

## Verified evidence coverage

| Level | First-pass written | Distinct direct Oxford word/POS observations | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 136 | 0 |
| A2 | 200 | 72 | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **413** | **0** |

**432** publisher observations correspond to **413** distinct headwords (repeat observations do not inflate coverage). **587** provisional entries have no direct observation in the audited Oxford packets. Reviewer queue: **152** publisher-lower word/POS classifications, **13** higher, **3** unlisted (not CEFR labels), and **245** matching word/POS classifications whose exact senses remain unverified. **36** historical excerpt recoveries are cross-referenced, not additional distinct words.

## Executed CI and fail-closed safeguards

- [Structural GitHub Actions run 40863759737](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40863759737): **SUCCESS**, all six parallel **A1 / A2 / B1 / B2 / C1 / ALL** jobs individually **SUCCESS**, on code commit `9015cba07bb58fb155d8a753304a9f37c5f6236e`. ALL-job logs show **221/221** new ninth-batch forged-source/English/Myanmar/example/provenance/reviewer mutations rejected, **20/20** cross-batch mutations rejected and **145/145** reviewer-handoff integrity mutations rejected. The full 1,000-item reviewer handoff was regenerated and checked.
- [Documentary no-deployment run 40863759714](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40863759714): **SUCCESS as report-only**, not a release approval. Its logs retain independent linguistic review, audio listening, desktop/mobile regression, physical iPhone Safari, measured GitHub Pages hosting, production-asset signoff and release-approval blockers.
- [Read-only 1,000-word scope guard run 40863759763](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40863759763): **SUCCESS**. The code commit's Git diff includes **six staging research/audit/workflow files only**, with no protected production assets touched.

## Unresolved mandatory release gates

**First-pass written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. **Final British George/Emma headword and example audio listening signoffs: 0/1,000.** Missing: separately authenticated human English, fluent Myanmar, original-example and exact-sense CEFR signoffs; complete generated final audio and real listening evidence; approved-corpus desktop/mobile browser regression; actual physical iPhone Safari review; measured GitHub Pages size/bandwidth limits; release-candidate approval; and confirmed production deployment with preservation checks for **54 lessons**, the separate **IELTS 1,000-word bank**, established production George/Emma audio and privacy.

**No merge, main-branch modification, production publication or independent-review claim. Do not notify as complete.**
