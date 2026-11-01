# CEFR 1,000 — six Cambridge indexed CEFR leads vs directly inspected Oxford senses (1 November 2026)

**Scope:** user-approved **1,000 TOTAL** (A1/A2/B1/B2/C1 exactly 200 each), not the retired 5,000-word plan. **Branch:** `cefr-5000-bilingual-qa-staging` only. **RELEASE BLOCKED — STAGING ONLY.**

## Source method and limits

On **2026-11-01**, six Oxford Advanced Learner's Dictionary pages were directly opened and their precise sense/POS lines inspected. Cambridge English Dictionary search-index excerpts exposed the CEFR labels below, but **direct Cambridge page opens returned HTTP 403**. Cambridge labels are **indexed research leads**, not directly inspected publisher-page evidence or independent review. Oxford topic labels, where present, are not independent exact-sense CEFR proof. The source packet preserves publisher URLs, dates, access mode, line locators, original bilingual/example text, source path/index and historical Git blob provenance.

| Frozen word / level | Cambridge indexed label (unverified direct page) | Direct Oxford sense evidence | Independent review priority |
| --- | --- | --- | --- |
| **signature** noun / **C1** | **B1**, handwritten-name noun | [Oxford signature](https://www.oxfordlearnersdictionaries.com/definition/english/signature), lines 105–112; separate act of signing and characteristic senses at 134–155 | **High:** possible C1-to-B1 mismatch for exactly the frozen handwritten-name sense |
| **upgrade** verb / **C1** | **B2**, improving quality/version | [Oxford upgrade verb](https://www.oxfordlearnersdictionaries.com/definition/english/upgrade_1), lines 116–121; other meanings at 138–146 | **High:** Cambridge B2 index vs Oxford *Computers c1* topic label; independently adjudicate exact software-upgrade sense |
| **diverse** adjective / **C1** | **B2**, many different types | [Oxford diverse](https://www.oxfordlearnersdictionaries.com/definition/english/diverse), lines 103–112 | **High:** frozen mixed-researchers example is the many-types adjective; independently adjudicate B2 vs C1 |
| **closely** adverb / **B2** | **C1**, carefully/attentively | [Oxford closely](https://www.oxfordlearnersdictionaries.com/definition/english/closely), lines 131–136; near-in-space sense at 105–108 | **High:** original examined-drawing example is CAREFULLY, not NEAR; independently adjudicate C1 vs B2 |
| **neutral** adjective / **C1** | **C1**, no opinion or support for either side | [Oxford neutral](https://www.oxfordlearnersdictionaries.com/definition/english/neutral_1), lines 106–119 | **Normal:** exact disagreement sense aligns with indexed C1 but still needs human signoff |
| **asset** noun / **C1** | **C1**, valuable person/quality | [Oxford asset](https://www.oxfordlearnersdictionaries.com/definition/english/asset), lines 105–115; financial-property sense at 128–135 | **Normal:** frozen staff-as-asset example is useful-person sense, not balance-sheet property; refine Myanmar |

Cambridge indexed source URLs (publisher pages blocked on direct access): [signature](https://dictionary.cambridge.org/dictionary/english/signature), [upgrade](https://dictionary.cambridge.org/dictionary/english/upgrade), [diverse](https://dictionary.cambridge.org/dictionary/english/diverse), [closely](https://dictionary.cambridge.org/dictionary/english/closely), [neutral](https://dictionary.cambridge.org/dictionary/english/neutral), [asset](https://dictionary.cambridge.org/dictionary/english/asset).

All six frozen examples are grammatically plausible for the intended POS/sense; **no example was replaced**. The packet contains six original, unapproved Myanmar/example alternatives and reviewer questions. No CEFR relevel or approval was made. If any level changes after independent signoff, the approved 200-per-level quota must be rebalanced using independently reviewed replacement senses, not by relabelling automatically.

## Reproducible staging-only evidence and guardrails

- [Six-record source/provenance packet](draft/CEFR-1000-C1-B2-CAMBRIDGE-INDEXED-SIX-SENSE-TRIAGE-2026-11-01.json): frozen first-pass English/Myanmar/example, dated direct Oxford observations and **index-only** Cambridge labels, original Git source paths/index/blob SHAs, no false approval or listening receipts.
- [Fail-closed auditor](tools/audit_cefr_1000_cambridge_six_indexed_conflicts.py): pins exact research-packet and shortlist Git blobs, checks 1,000 held entries and 200 per level, case-insensitive deduplication, frozen bilingual/example provenance, historical source Git blobs, exact publisher headword URLs, access-mode truthfulness and false independent/audio claims. ALL-lane self-test attempts **123** adversarial mutations (six records × 20 each plus three packet-level mutations).
- [Parallel six-lane structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml): A1, A2, B1, B2, C1 and ALL each run the audit; ALL runs adversarial self-tests.
- [Documentary no-deployment workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml): also runs the adversarial audit and retains the existing release blocker report and production-protection check.

**CI evidence boundary:** The staging changes have been committed, but new GitHub Actions run IDs, actual job conclusions and logs have **not yet been retrieved**. No new CI PASS or 123/123 mutation result is asserted until actual job logs confirm it. Earlier successful workflow runs do not verify this new code.

## Exact release state

| Level | First-pass written | Independently approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

All 1,000 remain on editorial hold. Approved deduplicated manifest absent. Independent English, Myanmar, example and source-backed exact-sense CEFR receipts absent. Final British George/Emma headword-and-example audio **not certified complete** and actual listening signoffs **0/1,000**. Browser/mobile regression, real physical iPhone Safari evidence, measured GitHub Pages hosting gate, preserved-assets/privacy independent signoff and confirmed production deployment remain missing. The existing 54 lessons, separate IELTS 1,000-word bank, established production George/Emma audio and privacy assets are protected. **No merge, main-branch modification or publication.**
