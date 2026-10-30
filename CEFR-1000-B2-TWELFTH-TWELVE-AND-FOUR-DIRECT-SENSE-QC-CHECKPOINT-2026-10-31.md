# CEFR 1000 — B2 twelfth Oxford twelve and four direct dictionary sense leads (31 October 2026)

**STAGING ONLY — NO independent human review, approval, audio signoff or deployment.** User-approved scope is 1,000 total, exactly 200 first-pass entries each at A1/A2/B1/B2/C1. The superseded 5,000-word target is not in scope. All entries remain editorial holds. Work is restricted to `cefr-5000-bilingual-qa-staging`; the frozen shortlist and independent review tasks are unchanged.

## Direct official Oxford CEFR word/POS evidence

Inspected the official [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) on **2026-10-31**. PDF pages below are 1-based; extracted web text lines are 0-based. Publisher word/POS classifications **do not independently certify the exact intended sense**.

| B2 draft headword | Publisher word/POS | Official PDF | Page / line | Review priority |
|---|---|---|---|---|
| quote (verb) | B1 | Oxford 3000 | 9 / 2348 | Publisher lower; quotation vs price quote |
| tie (verb) | A2 | Oxford 3000 | 7 / 1707 | Publisher lower; physical fastening |
| wise (adjective) | B2 | Oxford 3000 | 12 / 3312 | Exact-sense human review |
| inner (adjective) | B2 | Oxford 3000 | 11 / 2941 | Physical inner area vs private feelings |
| lift (verb) | A2 | Oxford 3000 | 5 / 1359 | Publisher lower; transitive raising |
| tower (noun) | A2 | Oxford 3000 | 7 / 1716 | Publisher lower; physical structure |
| cabinet (noun) | C1 | Oxford 5000 | 4 / 871 | **Publisher higher; major furniture vs government sense risk** |
| contrast (noun) | B1 | Oxford 3000 | 8 / 1936 | Publisher lower; countability and prepositions |
| establish (verb) | B2 | Oxford 3000 | 11 / 2827 | Start lasting organisation/system |
| proposal (noun) | B2 | Oxford 3000 | 12 / 3102 | Formal suggested plan |
| reputation (noun) | B2 | Oxford 3000 | 12 / 3136 | Public opinion, not merely fame |
| assessment (noun) | B2 | Oxford 3000 | 10 / 2640 | Evaluation process vs examination |

**Batch classifications:** A2 3, B1 2, B2 6, C1 1. **Six** B2 provisional word/POS discrepancies (five publisher-lower, one publisher-higher). All twelve are first-time Oxford direct word/POS observations in the reconciled B2 shortlist evidence collection.

## Four directly inspected dictionary senses

- [quote verb, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/quote_1), page text lines 113–138: repeat another person's exact words; the source distinguishes this from providing an example or a price
- [cabinet noun, sense 2](https://www.oxfordlearnersdictionaries.com/definition/english/cabinet), lines 147–154: storage furniture with doors/drawers/shelves; **sense 1 (lines 105–123) is senior government ministers**. The Oxford 5000 C1 word/POS listing is not proof of C1 for the furniture sense. The dictionary's topic tag `Houses and homes c1` is not a separate independent exact-sense CEFR approval, and the site-wide Word of the Day C1 footer belongs to `applicable`, not `cabinet`
- [contrast noun, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/contrast_1), lines 105–116: visible difference between things; both countable and uncountable, including `contrast between A and B`
- [establish verb, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/establish), lines 112–120: create a lasting organisation/system; distinguish other senses such as prove or become recognised

Four new Myanmar/example alternatives are **unapproved editorial proposals**; no text was changed in the frozen shortlist. Source snapshots, historical Git source path/index/blob, exact PDF locators, dictionary URLs, observation dates and separate human review tasks are retained in [the twelve-record packet](draft/CEFR-1000-OXFORD-B2-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json). No independent reviewer receipt exists.

## Reconciliation and release readiness

The [fail-closed auditor](tools/audit_cefr_1000_oxford_b2_twelfth_twelve.py) pins the frozen packet and shortlist Git blobs and rejects **232 designed adversarial changes** (publisher CEFR, PDF page/line, original English/Myanmar/examples, historical provenance, dictionary sense and fabricated approvals). It is integrated into six parallel A1/A2/B1/B2/C1/ALL structural jobs and documentary no-deployment QC. **CI VERIFIED:** [structural run 41138158402](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41138158402) completed **SUCCESS across A1/A2/B1/B2/C1/ALL**, code SHA `1e68d5299d5bf40fdf26582ae19b1a8df84fbd44`; [documentary no-deploy run 41138171974](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41138171974) completed **SUCCESS as report-only**, code SHA `23df3035c9c7c5ae9304e8adf3cee438ba1bd902`. Actual ALL and documentary logs each confirm **232/232 forged source, Myanmar, sense, provenance and independent-review mutations rejected**. The documentary job retains all human, audio, device, hosting and deployment blockers; neither CI run authorises publication. Structural ALL artifact ID `13017324540`; documentary blocker artifact ID `13016984387`.

**CI-verified direct Oxford word/POS coverage after this batch:** A1 **195/200**, A2 **132/200**, B1 **156/200**, B2 **154/200**, C1 **111/200** = **748/1,000 distinct** across **767 observations**; **252** without direct Oxford observations. Human priority queue: **3 unlisted / 43 publisher-higher / 274 publisher-lower / 428 word/POS matching but exact-sense unverified / 252 without direct observation**. The reviewer-handoff script also corrects a pre-existing stale 724/276 exported coverage count; CI logs confirm the corrected 748/252. This is publisher word/POS research coverage, not independent exact-sense approval.

| Level | First-pass written | Independently checked and approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Final British George/Emma headword **and** example audio generation and actual listening remain unverified; final human listening receipts **0/1,000**. Independent source-backed exact-sense CEFR, English/Myanmar/example review, approved-corpus browser/mobile regression, real physical iPhone Safari review, measured GitHub Pages hosting and confirmed production deployment are **all missing**. Existing 54 lessons, separate IELTS 1,000-word bank, George/Emma production audio and privacy must remain unchanged. **No merge, main change or public launch. RELEASE BLOCKED / STAGING ONLY.**
