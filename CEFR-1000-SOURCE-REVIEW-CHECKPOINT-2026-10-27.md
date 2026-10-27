# CEFR 1,000 — direct-source review checkpoint (staging only)

**Observed:** 2026-10-27. **Release status:** BLOCKED. This checkpoint concerns the **approved scope of 1,000 TOTAL words** (A1/A2/B1/B2/C1 = 200 each), not the superseded 5,000-word plan. The existing staging branch name remains unchanged. No main-branch edit, merge or production deployment was performed by this checkpoint.

## Exact content counts and independent signoff

| Level | First-pass bilingual shortlist | Independently checked and approved | Direct Oxford PDF word/POS spotchecks | Direct-PDF level discrepancies |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 2 | 0 |
| A2 | 200 | 0 | 2 | 1 |
| B1 | 200 | 0 | 8 | 8 |
| B2 | 200 | 0 | 9 | 8 |
| C1 | 200 | 0 | 2 | 2 |
| **Total** | **1,000** | **0** | **23** | **19** |

These are **word/POS-level reference comparisons**, not exact-sense or Myanmar verification, and not independent human review. All 1,000 entries remain on editorial hold. A level discrepancy is a **review prompt**, not proof that a specific meaning has the wrong CEFR level.

## New direct publisher-source observations

Directly inspected [Oxford University Press, *The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-27**. Recorded 23 short, attributed lexical observations with human-readable PDF page and extracted-line locators, source URLs, original English/Myanmar drafts and contextual examples in [the staging evidence file](draft/CEFR-1000-OXFORD-DIRECT-PDF-SPOTCHECK-2026-10-27.json).

Representative exact word/POS conflicts for human review:
- **A2 business (noun)** appears in the official Oxford A1 list (PDF page 1, extracted line 115).
- **B1 address (noun), band (noun), adult (noun)** appear in the Oxford A1 list (page 1, lines 13, 61, 14).
- **B2 destroy (verb), engineer (noun), employee (noun)** appear in the Oxford A2 list (page 5, lines 1120, 1168, 1162).
- **B1 cancer (noun)** appears in the Oxford B2 list (page 10, line 2679).
- **C1 abandon (verb), acknowledge (verb)** appear in the Oxford B2 list (page 10, lines 2593, 2601).

Important correction to secondary-transcription interpretation: **an** is expressly present in the publisher's A1 PDF (page 1, line 29), despite an absence warning in the secondary transcribed dataset. An absent word in a mirror is not a valid CEFR rejection.

The Oxford wordlist does not by itself prove the exact contextual sense, Burmese meaning, example grammar or final teaching level. Use a sense-level reference such as [Cambridge English Vocabulary Profile](https://www.englishprofile.org/) alongside Oxford and obtain genuinely independent bilingual editorial signoff. Do not copy protected dictionary definitions into learner content.

## Safeguards and execution limits

- Added `tools/audit_cefr_1000_oxford_direct_spotcheck.py` to validate 23 source records against the original shortlist, pinned Git blob SHA, CEFR differences, hold flags, source URL, observation date and page/line references; it has negative tests for false review claims, changed levels and forged source URLs.
- Wired this audit into the existing **six-way parallel GitHub Actions matrix** (A1, A2, B1, B2, C1, ALL) via `.github/workflows/cefr-1000-selection-structural-qa.yml`; each job should emit a separate spotcheck audit artifact. Workflow file changed at commit `af55d9e6b8dfd6a057c10c28c0f9bd31bc7c90c7`.
- Repository file reads and an in-tool deterministic consistency comparison of all 23 records against the 1,000-row shortlist were performed. **Actual GitHub Actions run IDs, job conclusions and logs were not accessible through the available commit-run lookup**, so CI must be marked **NOT YET VERIFIED**; do not claim the new Python tests ran successfully in Actions.
- The new script's Git blob NUL and output newline literals were corrected in commit `08d48f578c54916834c9298fe87074a4cc514df6`. The direct PDF observations were committed at `3efcef47474de9255b7a69991a42dbc8d89f6000`.

## Outstanding mandatory release gates

**0/1,000 independent approvals.** All exact English senses, fluent Myanmar translations, example grammar, and level source evidence need independent reviewer receipts; all Oxford discrepancy and IELTS cross-bank overlaps need resolution where relevant. The **final 1,000-word George/Emma headword and example audio inventory is not certified complete**, and **real listening signoff is missing**. Post-content browser and mobile regressions, **physical iPhone Safari evidence**, verified GitHub Pages storage/bandwidth limits, production protection check, and **confirmed live deployment** are not complete. The pre-existing 54 lessons, separate IELTS 1,000-word bank, production George/Emma audio and privacy must remain protected.

**Do not merge, publish or announce completion.** The source evidence is a substantive editorial lead only; 23 observed entries are not 23 independently approved entries.


## Additional 2026-10-27 sense-specific publisher evidence and verified CI

**Scope remains 1,000 total** (A1 200, A2 200, B1 200, B2 200, C1 200); all **1,000 first-pass bilingual entries are written, 0/1,000 independently approved**, and all remain on editorial hold. The separate IELTS 1,000-word bank is not part of this quota.

Six new [Cambridge publisher dictionary sense observations](draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json) were recorded on **2026-10-27**, based on publisher-owned search-indexed page text. Their per-level staging counts are **A1 0, A2 1, B1 3, B2 0, C1 2**; independent approvals **0 for every level**. They supplement the 23 Oxford PDF word/POS observations above (they are not 6 new approved words). They carry the exact provisional English/Myanmar/example strings, original shortlist blob SHA, dictionary URLs, observed sense labels, editorial risks and provenance limitations:

- **A2 business**: [Cambridge](https://dictionary.cambridge.org/dictionary/english/business) distinguishes selling activity (A1, uncountable) from a company (A2, countable). Current A2 definition describes the former while its *runs a small business* example depicts the latter; this is a substantive English sense/example and Myanmar gloss alignment issue requiring correction and independent review.
- **B1 band**: [Cambridge Learner's Dictionary](https://dictionary.cambridge.org/dictionary/learner-english/band) labels the exact music-group noun sense **A1**. A B1 placement needs a documented independent teaching rationale or replacement.
- **B1 address**: [Cambridge](https://dictionary.cambridge.org/us/dictionary/english/address?topic=dealing-with-things-or-people) labels the home/postal details noun sense **A1**. The current B1 delivery-address example is not by itself evidence for B1.
- **B1 cancer**: [Cambridge](https://dictionary.cambridge.org/dictionary/english/cancer) marks the disease noun sense **B1**, unlike the Oxford B2 word/POS listing. This supports further sense-specific B1 review rather than automatic rejection.
- **C1 abandon**: [Cambridge](https://dictionary.cambridge.org/us/dictionary/english/abandon) differentiates STOP activity (**C1**) from LEAVE behind (**B2**). The provisional event-cancellation context targets STOP, so the Oxford B2 word/POS listing is not sufficient to invalidate C1.
- **C1 acknowledge**: [Cambridge](https://dictionary.cambridge.org/dictionary/english/acknowledge) marks admitting/recognising a fact **C1**, matching the provisional intended sense despite the Oxford B2 word/POS reference.

**No publisher search result proves a full independent review.** These observations are evidence leads, not copied definitions, and do not validate Myanmar fluency, grammar or final CEFR approval. A new [fail-closed publisher-sense audit](tools/audit_cefr_1000_cambridge_sense.py) checks source URLs, date, pinned shortlist SHA, exact source content, sense labels, editorial holds and negative tests against forged approvals. The [release readiness auditor](tools/audit_cefr_1000_launch_readiness.py) now requires separate independent Cambridge sense-resolution receipts for retained flagged entries; an unchanged mixed-sense *business* draft cannot satisfy that receipt gate. The [release ledger](draft/CEFR-1000-RELEASE-EVIDENCE.json) contains **zero** such receipts.

**Verified GitHub Actions (actual job conclusions and logs, not inferred):**

- [Six-way structural run 40460413317](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40460413317), commit `0d4402403faf16def8e045b3dcca6363f221795e`: **success**, all six A1/A2/B1/B2/C1/ALL jobs concluded success, including new Cambridge audit and ALL negative tests. The ALL job log confirms 1,000 first-pass rows, 1,000 review tasks, **0 independent approvals**, 23 Oxford direct-PDF checks, 6 Cambridge sense observations, **525 Oxford-transcription/reference flags** (not independently validated), and **120** shared IELTS/CEFR headwords requiring independent semantic review. Production-protection diff step passed.
- [Staging release evidence run 40460488645](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40460488645), commit `0c33caba6a8d31a72867a508bf2898e7769dc71a`: documentary launch-gate job **success**, including new Cambridge negative tests, browser UI script tests and production-protection diff. This is **report-only** success, explicitly **not release-ready**: its log lists missing approved manifest, 0 independent review packets, missing real George/Emma listening receipts, missing desktop/mobile regression receipts, physical iPhone Safari signoff, hosting measurements and final production asset review. No release-enforcement or deployment step ran.

**Release state: BLOCKED / STAGING ONLY.** No approved manifest, final George/Emma audio listening signoff, physical iPhone review, hosting verification or confirmed production deployment. The existing 54 lessons, IELTS bank, production George/Emma assets and privacy remain untouched by these staging commits. Do not publish or notify completion.

## Second publisher-sense evidence batch — 2026-10-27

The [Cambridge source triage file](draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json) now has **14** source-indexed sense observations (previously six), all on editorial hold. Eight added: [direction](https://dictionary.cambridge.org/dictionary/english/direction) (B1 position versus A2 plural route instructions), [budget](https://dictionary.cambridge.org/dictionary/english/budget) (B2 financial plan versus B1 draft), [advertising](https://dictionary.cambridge.org/dictionary/english/advertising) (B2 industry supports B2 draft), [attractive](https://dictionary.cambridge.org/dictionary/english/attractive) (A2 visual appeal versus B2 interesting/beneficial offer), [destroy](https://dictionary.cambridge.org/dictionary/learner-english/destroy) (B1 severe damage versus B2 draft), [employee](https://dictionary.cambridge.org/dictionary/english/employee) (B1 paid worker versus B2 draft), [engineer](https://dictionary.cambridge.org/dictionary/english/engineer) (A2 technical profession versus B2 draft), and [appointment](https://dictionary.cambridge.org/dictionary/english/appointment) (A2 arranged meeting versus B2 draft; C2 official job selection is different). Source observations dated 2026-10-27. Full publisher pages returned HTTP 403 when opened directly; these are search-indexed publisher page excerpts, **not** independent dictionary or Myanmar reviews.

**High-priority meaning/example conflict:** B2 *attractive* uses a packaging-design appearance example that matches Cambridge A2 rather than B2 beneficial-offer sense. B2 *appointment* uses the A2 dental-meeting sense. B1 *direction* is potentially correctly B1 despite Oxford A2 word/POS flag because Cambridge distinguishes plural route *directions* A2. These are editorial leads, not automatic level changes.

**Actual GitHub Actions verification:** [six-job structural run 40465386555](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40465386555), SHA `51d04bd2413f2473266ec50b966952943bc9d31b`, concluded **success** in all A1/A2/B1/B2/C1/ALL jobs. Its ALL job log confirms 14 Cambridge observations, negative-test PASS, 23 Oxford PDF spotchecks, 525 Oxford transcription/reference flags, 120 IELTS shared headwords, 1,000 first-pass shortlist and linked review tasks, **0 independent approvals**, and protected production diff PASS. [Documentary release-blocker run 40465393057](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40465393057), SHA `efd50b949395565b63e95029b22b1d15a79c7128`, concluded **success** but is *report-only*; log explicitly blocks release for missing approved manifest, 0 independent receipts, no real George/Emma listening, missing browser/mobile and physical iPhone Safari evidence, hosting measurements, and final production preservation signoff.

**Exact per-level counts:** first-pass written A1 200, A2 200, B1 200, B2 200, C1 200; independently approved **A1 0, A2 0, B1 0, B2 0, C1 0**. All 1,000 held. New Cambridge observations split B1 2, B2 6; cumulative 14 split A1 0, A2 1, B1 5, B2 6, C1 2. Final audio generation/listening, device tests, hosting and live deployment remain **unverified / blocked**. No publication or main changes.
