# CEFR 1,000 — direct-source review checkpoint (staging only)

**Observed:** 2026-10-27. **Release status:** BLOCKED. This checkpoint concerns the **approved scope of 1,000 TOTAL words** (A1/A2/B1/B2/C1 = 200 each), not the superseded 5,000-word plan. The existing staging branch name remains unchanged. No main-branch edit, merge or production deployment was performed by this checkpoint.

## Exact content counts and independent signoff

| Level | First-pass bilingual shortlist | Independently checked and approved | Direct Oxford PDF word/POS spotchecks | Direct-PDF level discrepancies |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 2 | 0 |
| A2 | 200 | 0 | 2 | 1 |
| B1 | 200 | 0 | 8 | 7 |
| B2 | 200 | 0 | 9 | 9 |
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
