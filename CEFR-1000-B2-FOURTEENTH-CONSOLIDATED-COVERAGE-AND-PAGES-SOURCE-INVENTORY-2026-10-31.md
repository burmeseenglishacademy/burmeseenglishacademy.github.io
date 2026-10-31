# CEFR 1000 — B2 fourteenth Oxford consolidation and GitHub Pages source-tree inventory

**Observation date:** 2026-10-31. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Status:** BLOCKED / STAGING ONLY. This is evidence reconciliation, not independent linguistic approval, release approval, iPhone testing, audio listening, or deployment.

## Source-supported B2 word/POS evidence reconciled

The twelve previously recorded direct Oxford 3000 word/POS observations for `tone, topic, vast, earn, ignore, meanwhile, necessarily, practical, rescue, stable, temporary, technique` are now included in the fail-closed cross-batch coverage auditor and source-bound reviewer handoff. Their immutable source packet is [B2 fourteenth](draft/CEFR-1000-OXFORD-B2-FOURTEENTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json), with the official [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), dated publisher PDF page/line locators, original English/Myanmar/examples, historical Git source paths and blob SHA, and four unapproved exact-sense rewrite leads. Publisher classifications: A1 1, A2 1, B1 5, B2 5. Seven provisional B2 word/POS placement conflicts require human exact-sense resolution. No automatic retiering.

**CI-verified consolidated direct Oxford word/POS research:**

| Draft level | First-pass written | Direct Oxford observed distinct | Not yet directly observed | Independently approved |
|---|---:|---:|---:|---:|
| A1 | 200 | 195 | 5 | 0 |
| A2 | 200 | 168 | 32 | 0 |
| B1 | 200 | 200 | 0 | 0 |
| B2 | 200 | 178 | 22 | 0 |
| C1 | 200 | 111 | 89 | 0 |
| **Total** | **1,000** | **852** | **148** | **0** |

There are **871 source observations for 852 distinct shortlist headwords**, with 19 repeated observations; repeats are not counted as new words. The source-bound human review queue is **3 unlisted/not a CEFR label, 52 publisher-higher, 337 publisher-lower, 460 matching word/POS but exact-sense unverified, and 148 lacking direct Oxford observation**. All 1,000 remain on editorial hold; zero human-independent signoffs.

## Fail-closed implementation and actual Actions verification

Changes are limited to `tools/audit_cefr_1000_oxford_coverage.py` and `tools/audit_cefr_1000_review_priority.py`. The B2 fourteenth packet is included in coverage reconciliation; all twelve Oxford word/POS CEFR levels, PDF pages, extracted lines and source excerpts are pinned against source-evidence drift. Five new negative tests target forged B2 publisher level, excerpt, Myanmar, release flag and record deletion. An intermediate Actions run correctly failed when a forged excerpt escaped the generic coverage validator; fixed by pinning the twelve source locators before claiming success.

**Verified final tested code SHA:** `4b1530660f6ee2aa2761c42422a895af4709b0aa`.

- [Parallel structural run 41192070653](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41192070653): **SUCCESS** for A1, A2, B1, B2, C1 and ALL. Actual ALL job log: **25/25** cross-batch forged evidence mutations rejected, **143/143** source-bound reviewer handoff mutations rejected, and **208/208** B2 fourteenth source/grammar/Myanmar/false-signoff mutations rejected. ALL artifact `13038859053`.
- [Documentary no-deployment run 41192070288](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41192070288): **SUCCESS**, report-only; blocker artifact `13039925007`.
- [Source-scope run 41192070270](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41192070270): **SUCCESS**, no production writes. Actual log reports **852 distinct** direct word/POS observations and **148** missing.
- Actual ALL and documentary logs confirm protected production assets unchanged. Successful code tests do **not** satisfy linguistic, listening, physical-device, hosting, or deployment gates.

## GitHub Pages hosting source-tree inventory — NOT a passed hosting gate

Read-only GitHub Git tree snapshot at commit `4b1530660f6ee2aa2761c42422a895af4709b0aa`, tree `46626a7fcda38b11e0114d44f4e720db4bee5fc6`, recursively complete (`truncated=false`):

| Item | Git blob count | Sum of Git tree blob sizes |
|---|---:|---:|
| Entire staging branch source tree | 5,484 | 150,538,586 bytes |
| Existing `audio/` tree | 4,652 | 123,502,524 bytes |
| Existing `audio/bm_george/` | 2,326 | 65,887,902 bytes |
| Existing `audio/bf_emma/` | 2,326 | 57,614,622 bytes |

These are **source-tree Git blob byte sums**, not a measured Pages deployment artifact, repository Git pack size, live bandwidth, final CEFR 1000 audio inventory, or audio listening evidence. Existing production George/Emma recordings are protected and **must not be counted as generated/listened-to final shortlist audio**. No final 1,000-word George/Emma audio or actual listening signoffs are claimed.

[GitHub's official Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), checked 2026-10-31, state a recommended **1 GB source repository**, **1 GB maximum published site**, **10-minute deployment timeout**, **100 GB/month soft bandwidth limit**, and **10 builds/hour soft limit** (the build limit does not apply to a custom Actions publishing workflow). This read-only source inventory is useful for planning, **not** a hosting release signoff: a real, approved release artifact must be measured, and actual deployment/usage confirmed before passing that gate. No Pages publishing workflow was invoked.

## Outstanding release blockers

Exactly 200 independently approved, deduplicated exact-sense entries per CEFR level are still absent; English, fluent Myanmar, example grammar, source-backed CEFR and pronunciation require genuine independent human review and content-bound receipts. Final George/Emma headword and example audio must be generated and **actually listened to**, with real per-file signoffs (currently **0/1,000**). Approved-manifest deduplication, browser and mobile regression, physical iPhone Safari evidence, measured Pages artifact and bandwidth readiness, privacy/protected production asset checks, and confirmed production deployment remain outstanding. Preserve 54 live lessons, the separate IELTS 1,000-word bank and existing George/Emma production audio. **No merge, no main modification, no publication, no claim of deployment.**
