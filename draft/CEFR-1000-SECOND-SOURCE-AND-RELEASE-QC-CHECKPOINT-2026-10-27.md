# BEA CEFR 1,000 — second publisher-source and release-QC checkpoint (staging ONLY)

**Observation date:** 2026-10-27. **Branch:** `cefr-5000-bilingual-qa-staging` (name deliberately retained). **Scope:** 1,000 TOTAL A1–C1 entries, 200 per level, **not** the superseded 5,000-word project. **Release:** BLOCKED, do not merge or deploy.

## Written first pass, human independence and publisher observations

| Level | First-pass bilingual shortlist (written, unverified) | Independently approved | Earlier Oxford 3000 direct PDF | New Oxford 3000/5000 direct PDF | Combined direct PDF word/POS checks | Combined direct PDF CEFR-level discrepancies |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 200 | 0 | 2 | 0 | 2 | 0 |
| A2 | 200 | 0 | 2 | 6 | 8 | 7 |
| B1 | 200 | 0 | 8 | 6 | 14 | 14 |
| B2 | 200 | 0 | 9 | 4 | 13 | 10 |
| C1 | 200 | 0 | 2 | 11 | 13 | 12 |
| **Total** | **1,000** | **0** | **23** | **27** | **50** | **43** |

These are *word/POS-level source observations*, **not** 50 independently reviewed words, **not** 50 verified senses and **not** 43 proven CEFR errors. A source discrepancy prompts a reviewer to decide the exact taught sense and level. The first-pass original examples and Myanmar meanings remain **unverified**. All 1,000 editorial holds and 1,000 independent review tasks remain unchanged.

New directly inspected publisher sources (2026-10-27):
- [Oxford 3000 official CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), which lists A1–B2 words and POS.
- [Oxford 5000 official CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf), the additional B2–C1 words and POS.
- [27 new source observations with exact 1-based PDF pages, 0-based extracted text lines, shortlist snapshot, Myanmar/English/example context and unresolved editorial issues](CEFR-1000-OXFORD-SECOND-DIRECT-PDF-BATCH-2026-10-27.json). **24/27** have different proposed versus Oxford word/POS CEFR levels. `print` **noun** and `anniversary` **noun** correctly match Oxford B2; `integrity` **noun** matches Oxford C1. In particular, do **not** conflate Oxford A2 `print` **verb** with B2 `print` **noun**.

Five new **exact-sense publisher leads** (in addition to the earlier 23 Cambridge leads, now **28 publisher-indexed Cambridge observations**):
- [Cambridge print](https://dictionary.cambridge.org/dictionary/english/print): noun **TEXT** is **C2** in Cambridge, while Oxford 3000 lists the noun at B2. The draft example concerns small printed lettering, **not** the A2 printing verb.
- [Cambridge racism](https://dictionary.cambridge.org/dictionary/english/racism): noun unfair-treatment/belief senses **B2**, matching Oxford B2 but differing from provisional C1; distinguish institutional discrimination from beliefs and acts in Myanmar.
- [Cambridge consistently](https://dictionary.cambridge.org/dictionary/english/consistently): unchanging-manner adverb **C2**, while Oxford 5000 lists B2 and provisional shortlist is C1.
- [Cambridge diverse](https://dictionary.cambridge.org/dictionary/english/diverse): mixed-types adjective **B2**, matching Oxford B2 but differing from provisional C1.
- [Cambridge integrity](https://dictionary.cambridge.org/dictionary/english/integrity): **HONESTY** noun **C2** in Cambridge, while Oxford 5000 lists the word/POS C1. Draft illustrates moral honesty, not structural/data integrity.

**Provenance limitation:** Cambridge direct page requests returned HTTP 403. These five observations came from indexed publisher-owned Cambridge search result text on 2026-10-27; they are **not** complete direct-page inspections and **not** independent editorial approval. The separate [five-record sense packet](CEFR-1000-CAMBRIDGE-SECOND-SENSE-LEADS-2026-10-27.json) records source URLs, observed date, source-access caveat, original first-pass definitions, Myanmar glosses, examples and independent-review questions. Do not automatically retier from either publisher's labels. These discrepancies require **genuine independent sense-specific CEFR and Myanmar signoff** or independently reviewed replacement/retiering.

## Staging-only safeguards and real GitHub Actions evidence

New fail-closed structural checks:
- `tools/audit_cefr_1000_oxford_second_batch.py` pins all 27 observed publisher word/POS levels, PDF page/line locators, shortlist Git blob SHA, original English/Myanmar/example snapshots and zero-approval holds. Negative tests reject fake independent flags, altered PDF locators, changed source levels/URLs, duplicates and fake aggregates.
- `tools/audit_cefr_1000_cambridge_second_sense.py` pins five exact-sense publisher labels and URLs, explicit Cambridge 403 limitation, unchanged first-pass content and editorial holds. Negative tests reject forged review, CEFR labels, URLs, reviewer receipts and duplicates.
- Six parallel `A1, A2, B1, B2, C1, ALL` structural jobs run both checks. **Structural success is not a linguistic or release approval.**
- `tools/audit_cefr_1000_launch_readiness.py` now requires **separate independent human review receipts** for any of these five retained Cambridge conflicts, including content hash, reviewer/date, publisher sense and explicit CEFR-level rationale. `draft/CEFR-1000-RELEASE-EVIDENCE.json` has **zero** such receipts.
- `.github/workflows/cefr-1000-go-live-qc-gate.yml` checks the second Cambridge packet and negative tests. This workflow reports blockers and **does not deploy**.

Actual CI runs and logs examined:
- [Structural run 40482564939](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40482564939), SHA `824848b15c3468a29a60f869d512fd092e8dee78`: **six job conclusions SUCCESS**; ALL job log confirms 27 Oxford observations, 24 publisher-level discrepancies and negative tests PASS.
- [Structural run 40482682093](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40482682093), SHA `e8a403c2bda060efc15e2d85566f50e84d67cf09`: **six job conclusions SUCCESS**; ALL job log confirms five Cambridge publisher-indexed leads, zero approvals and negative tests PASS.
- [Report-only release gate 40482741483](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40482741483), SHA `ed20209a908cfc48b6443883711b37c7d2903419`: **SUCCESS as blocker-reporting workflow, NOT launch readiness**. Logs still show zero independently reviewed and zero listening receipts, missing approved manifest, physical iPhone, browser regression and hosting receipts.
- [Updated report-only release gate 40482775972](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40482775972), SHA `5f1bce88536ebbe202cd7cf911e0f9feb43b25c5`: **documentary-launch-gate job SUCCESS**, actual log checked. New five-sense negative tests PASS; logs explicitly show 0/1,000 independent reviews, 0/1,000 both-voice listening receipts, absent iPhone/hosting/browser/manifest signoffs and production unchanged. This is **report-only success, NOT launch approval**.

## Unresolved release gates — fail closed

| Gate | Evidence status |
|---|---|
| Exactly 200 first-pass candidates at A1, A2, B1, B2, C1 | Structural QA PASS, but no independent approval |
| Independent English, fluent Myanmar, original-example, exact-sense CEFR and provenance review | **0/200 each level; 0/1,000 approved** |
| 525 historical Oxford/transcription flags and 68 two-plus-band priorities | Editorial conflicts; **0 independent resolutions**. Some mirror absences are false positives, e.g. `an` is in official A1 |
| 120 CEFR/IELTS shared headwords | 120 cross-bank review tasks; **0 independent semantic decisions** |
| 28 Cambridge indexed exact-sense leads | **0 independent approvals**, including five newly recorded |
| Final George and Emma headword+example audio | **No final-shortlist generated-audio manifest or independent listening signoff established**; 0 verified listening receipts; do not alter existing production audio |
| Desktop/mobile Chromium and WebKit | No completed release-candidate regression receipts |
| Real physical iPhone Safari | No device/audio reviewer evidence; never infer from desktop emulation |
| GitHub Pages limits | Official 1 GB published-site cap and 100 GB/month soft bandwidth confirmed from GitHub Docs on 2026-10-27; **no measured final artifact/bandwidth evidence** |
| Preserve 54 lessons, separate IELTS 1,000, production George/Emma audio and privacy | Staging CI comparison with `main` reports protected files unchanged; final release preservation attestation missing |
| Approved 1,000-entry manifest and confirmed live deployment | **Missing; production unchanged** |

**Hosting source verification (2026-10-27):** [GitHub Pages official limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) specify a recommended 1 GB source-repository limit, 1 GB maximum published site, 10-minute deployment timeout, 100 GB/month soft bandwidth limit and 10 builds/hour soft limit (custom GitHub Actions publishing exempt from that last limit). This is policy verification only, **not a measured website or traffic signoff**.

**Next work:** collect further exact-sense primary-source observations and high-risk Myanmar/example discrepancies; route independent review to actual qualified humans; preserve immutable reviewer receipts. Only after 1,000 approvals, real audio generation/listening, physical iPhone, desktop/mobile, measured hosting and protected-assets checks may a release candidate be prepared. Never use a green report-only Actions run as permission to publish.
