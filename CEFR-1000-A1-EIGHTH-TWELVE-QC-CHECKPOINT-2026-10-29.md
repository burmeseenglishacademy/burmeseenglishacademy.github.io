# CEFR 1,000 — A1 eighth twelve official Oxford observations and fail-closed QC
**Research date:** 2026-10-29 (Singapore)  
**Branch:** `cefr-5000-bilingual-qa-staging` only  
**Scope:** user-approved **1,000 total**, 200 each at A1, A2, B1, B2, C1; the superseded 5,000-word plan is NOT in scope.  
**Status:** **BLOCKED / STAGING ONLY; 0 independently approved; no publication.**

## Official publisher source, provenance and exact limits

Directly inspected Oxford University Press, [*The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), on **2026-10-29**. The following **12 previously unobserved A1-draft words** have official A1 word/POS-list observations. PDF pages below are **one-based**, and extracted PDF lines **zero-based**. All records include the publisher URL, observation date, exact excerpt, frozen shortlist English definition, Myanmar meaning, original example, historical Git source path/index/blob SHA, and a specific independent-review task in [the evidence packet](draft/CEFR-1000-OXFORD-A1-EIGHTH-TWELVE-2026-10-29.json).

| A1-draft headword | PDF page | Extracted line | Publisher excerpt | Frozen original example |
|---|---:|---:|---|---|
| `today` | 3 | 805 | `today adv., n.` | Today is Monday. |
| `tomorrow` | 3 | 809 | `tomorrow adv., n.` | We have class tomorrow. |
| `yesterday` | 4 | 903 | `yesterday adv., n.` | Yesterday was Sunday. |
| `morning` | 2 | 495 | `morning n.` | I study in the morning. |
| `afternoon` | 1 | 18 | `afternoon n.` | We play in the afternoon. |
| `evening` | 1 | 248 | `evening n.` | I cook in the evening. |
| `night` | 2 | 522 | `night n.` | I sleep at night. |
| `week` | 4 | 868 | `week n.` | I work five days a week. |
| `month` | 2 | 493 | `month n.` | Next month is December. |
| `minute` | 2 | 485 | `minute1 n.` | Wait one minute, please. |
| `hour` | 2 | 379 | `hour n.` | The lesson lasts one hour. |
| `brother` | 1 | 110 | `brother n.` | My brother lives here. |

**Interpretation:** Oxford's word/POS classification is *not* a verified exact-sense CEFR level, nor a check of fluent Myanmar, sentence grammar, pronunciation, or original-example quality. No human-independent approval is inferred. All 12 remain on editorial hold.

## Substantive grammar and bilingual editorial findings — not applied or approved

- **today** is provisionally tagged *adverb* but the frozen example *Today is Monday* uses **today as a nominal subject**. Unapplied proposed adverbial example: *I am studying English today.*
- **yesterday** is provisionally tagged *adverb* but *Yesterday was Sunday* uses **yesterday as a nominal subject**. Unapplied proposed adverbial example: *I visited my aunt yesterday.*
- **tomorrow** is adverbial in *We have class tomorrow* and may remain a useful comparison with the nominal senses Oxford also lists.
- **minute** is Oxford's `minute1 n.` time-unit entry; distinguish it from the homographic adjective *minute* ('very small'), including **British pronunciation** before generating any George/Emma final headword audio.
- **brother** maps to Myanmar kinship terms that depend on relative age and the speaker's relation (အစ်ကို၊ မောင်၊ ညီ). The English example is grammatical, but a fluent independent Myanmar reviewer must approve the intended contextual translation.
- **morning / afternoon / evening / night** need time-boundary and collocation review, and **week / month / hour** need natural Myanmar temporal expressions. None of these self-evaluations constitutes signoff.

## Verified structural QC, negative tests and release gate

The new [fail-closed A1 packet auditor](tools/audit_cefr_1000_oxford_a1_eighth_twelve.py) reconstructs all 12 source snapshots from the frozen shortlist, rejects duplicates against seven prior A1 packets, requires exact Oxford URL/date/page/line/excerpt, binds English/Myanmar/example and historical Git provenance, and rejects fabricated independent-review receipts or changes to the review task. **144/144** adversarial row mutations were rejected in actual GitHub Actions logs. Cross-batch evidence and the source-bound 1,000-task independent-review handoff were updated without modifying the frozen shortlist.

Verified code commit: [`ec58480eae7afa645170883df64d6c6409745e39`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/ec58480eae7afa645170883df64d6c6409745e39).

- [Six-lane parallel structural run **40855836625**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40855836625): **SUCCESS**, all **A1/A2/B1/B2/C1/ALL** jobs completed successfully; 144/144 new mutations and 145/145 handoff-integrity mutations rejected. Exported 1,000-task handoff validated against source truth.
- [Documentary no-deployment run **40855836604**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40855836604): **SUCCESS as report-only**, 144/144 new mutations and 20/20 cross-batch mutations rejected; explicit blockers retained; protected production paths unchanged.
- [Read-only 1,000-scope guard **40855836584**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40855836584): **SUCCESS**, no legacy 5,000-word generation or production write.

Git comparison against `de9279c02e0b95521262dd537ae2d9ff4ce1acf1` confirms **six staging-only research/audit/workflow files** changed in the verified code commit. The 54 production lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy-related production assets were not modified.

## Exact staging counts and unresolved gates

| CEFR | First-pass written | Direct Oxford word/POS observations (distinct) | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 124 | 0 |
| A2 | 200 | 72 | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **401** | **0** |

The source auditor reports **420 observations** covering **401 distinct provisional words** (repeat observations do not increase coverage), **599 without direct Oxford observations** in these audited packets, **152 publisher-lower**, **13 publisher-higher**, **3 unlisted-not-a-CEFR-label**, and **233 matching word/POS level observations still requiring exact-sense human review**. These buckets sum to 1,000. Historical 36 excerpt recoveries remain cross-referenced, not counted as new words.

**Still missing:** independently signed-off English, fluent Myanmar, original-example grammar and source-backed exact-sense CEFR review for all 1,000; a final 200-per-level deduplicated approved release manifest; generated **both British George and Emma** headword **and** example audio for the approved manifest with **actual human listening signoff** (currently **0/1,000**); approved-corpus browser and mobile regression; real **physical iPhone Safari** testing and listening evidence; actual GitHub Pages hosting-size/bandwidth measurements; verified production deployment and preservation check. No fake receipts, device test, listening signoff, merge, main-branch change or production launch occurred. **Release remains BLOCKED / STAGING ONLY.**
