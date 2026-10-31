# CEFR 1000 — final ten provisional B2 Oxford research and release-blocking QC

**Observation:** 2026-10-31 (Singapore). **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / STAGING ONLY. **Scope:** user-approved 1,000 total, exactly 200 provisional first-pass entries at each of A1/A2/B1/B2/C1; not the superseded 5,000-word plan.

## Publisher observations — source-backed, not independent CEFR approval

Directly inspected [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) on 2026-10-31. PDF page numbers are **one-based**, extracted line numbers **zero-based**. A word/POS level is not an independently reviewed exact-sense level. The draft entries and review flags were not modified.

| Provisional B2 word/POS | Oxford word/POS result | PDF | Page | Extracted line | Editorial risk |
|---|---|---|---:|---:|---|
| package (n.) | B1 | 3000 | 9 | 2262 | Bundled training services vs postal parcel |
| pride (n.) | B2 | 5000 | 2 | 479 | Achievement satisfaction vs arrogance/self-respect/lions |
| province (n.) | C1 | 5000 | 6 | 1643 | Geographic administrative unit vs figurative domain |
| railway (n.) | A2 | 3000 | 6 | 1523 | Ordinary train system appears below draft B2 |
| relative (adj.) | B1 | 3000 | 9 | 2365 | Comparison adjective vs family-member noun or grammar term |
| repeat (v.) | A1 | 3000 | 3 | 647 | Basic say-again sense conflicts strongly with draft B2 |
| server (n.) | **Not found in either inspected core list** | 3000 + 5000 | — | — | Not a CEFR level; computing sense needs independent review |
| shock (n.) | B2 | 3000 | 12 | 3190 | Emotional surprise vs medical/electrical shock |
| silence (n.) | B2 | 3000 | 12 | 3196 | Absence of sound vs deliberate withholding of speech |
| superior (adj.) | C1 | 5000 | 7 | 1860 | Better quality vs higher authority/status |

**Publisher word/POS distribution:** A1 1, A2 1, B1 2, B2 3, C1 2, one core-list unlisted. **Seven** of the nine listed word/POS labels differ from the provisional B2 level. This does **not** establish retiering or human approval.

Five additional **directly opened** Oxford dictionary pages provide exact-sense leads: [package noun, bundled offer sense 3](https://www.oxfordlearnersdictionaries.com/definition/english/package_1), [pride noun, satisfaction sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/pride_1), [province noun, administrative division sense 1](https://www.oxfordlearnersdictionaries.com/us/definition/english/province), [relative adjective, comparison sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/relative_1), and [server noun, computing sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/server). **Server's Computers c1 and pride's Personal qualities b2 badges are topic badges, not Oxford 3000/5000 word/POS observations or independently signed-off exact-sense CEFR.** All five Myanmar/example rewrites remain **UNAPPROVED**.

The [immutable ten-record research packet](draft/CEFR-1000-OXFORD-B2-SIXTEENTH-FINAL-TEN-AND-FIVE-DIRECT-SENSE-LEADS-2026-10-31.json) preserves original English/Myanmar/example, source path/index/blob, publisher URLs, observation dates, PDF line/page/excerpt or explicit two-list absence, direct dictionary URLs, editorial risks and null human receipts. The [fail-closed auditor](tools/audit_cefr_1000_oxford_b2_sixteenth_ten.py) binds both the packet and frozen shortlist Git blobs, historical original source rows, fixed publisher locators, explicit unlisted case, and five sense URLs. Its **194 adversarial mutation cases** target forged sources, bilingual text, provenance, sense, counts and approvals; **these are defined and CI-wired, not claimed as passed until actual job logs are checked**.

## Consolidated counts (code expectations; GitHub Actions results not yet independently retrieved)

| Level | First-pass written | Oxford direct word/POS observations (distinct) | Missing direct Oxford observations | Independently approved |
|---|---:|---:|---:|---:|
| A1 | 200 | 195 | 5 | 0 |
| A2 | 200 | 168 | 32 | 0 |
| B1 | 200 | 200 | 0 | 0 |
| B2 | 200 | **200** | **0** | 0 |
| C1 | 200 | 111 | 89 | 0 |
| **Total** | **1,000** | **874** | **126** | **0** |

**Expected** 893 total Oxford observations across packets (including repeated observations), 874 distinct. Source-bound independent-review priority queue: **4 core-list unlisted, 55 publisher-higher, 346 publisher-lower, 469 word/POS matching but exact sense unverified, 126 not yet directly observed**. All categories sum to 1,000. This is **publisher research coverage only**, not verified linguistic accuracy or independent CEFR approvals.

## CI and release evidence

The staging source auditor, coverage reconciliation, reviewer-priority auditor and both [parallel six-lane structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml) have been updated. The structural workflow runs the final-ten audit on A1/A2/B1/B2/C1/ALL, with 194 adversarial cases on ALL. The documentary workflow runs the same audit in report-only mode. **No new run IDs, job conclusions or logs have been verified in this checkpoint**: the available GitHub commit-run lookup returned no push-triggered runs. Do not report CI SUCCESS from code wiring.

Git comparison against preceding staging checkpoint `2db1c479b4740d51781543d9cd366bcad219f562` showed **six changed staging research/audit/workflow paths only**. No main-branch change, production publication or protected production file modification was made.

**Release remains blocked.** Written/independently approved: A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0. George/Emma final word+example audio real listening signoffs: **0/1,000**. Missing independent English/Myanmar/example/exact-sense CEFR review, final approved deduplicated manifest, dual-voice audio generation/listening, browser/mobile regression, physical iPhone Safari evidence, measured Pages release artifact/hosting readiness, and confirmed production deployment. Preserve 54 lessons, separate IELTS 1,000 bank, existing George/Emma audio and privacy. **NO MERGE / NO MAIN CHANGE / NO PUBLICATION.**
