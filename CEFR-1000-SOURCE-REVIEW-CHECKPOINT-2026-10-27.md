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

## Third publisher-sense evidence batch and hosting policy safeguards — 2026-10-27

**Scope and status:** 1,000 total provisional bilingual entries (A1 200, A2 200, B1 200, B2 200, C1 200); independently checked/approved **A1 0, A2 0, B1 0, B2 0, C1 0**. All 1,000 remain on editorial hold. No approved manifest, no final George/Emma listening receipts, no physical iPhone Safari QA, no verified production deployment.

**Nine new exact-sense publisher leads** were added to [Cambridge sense triage](draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json), bringing the cumulative total from 14 to **23** (A1 **0**, A2 **1**, B1 **7**, B2 **8**, C1 **7**). Observed **2026-10-27** in Cambridge publisher-owned search-indexed page excerpts; attempted direct publisher-page fetch returned **HTTP 403**, so this is *not* full-page or independent review. Each record retains publisher URL, exact first-pass English/Myanmar/example strings, provisional level/POS, source label, observation date, editorial risk and pinned shortlist blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No dictionary definitions were copied into the draft.

- **B1 weekend**: [Cambridge A1](https://dictionary.cambridge.org/us/dictionary/english/weekend) for the ordinary Saturday/Sunday noun sense. **B1 cash**: [Cambridge A2](https://dictionary.cambridge.org/dictionary/learner-english/cash) for physical coins/notes; its broader-money sense is B1. The first-pass cash-only payment example targets the A2 sense.
- **B2 manage**: [Cambridge B1](https://dictionary.cambridge.org/dictionary/english/manage) for succeeding at something difficult, matching the provisional *managed to finish* example. **B2 hardly**: [Cambridge B1](https://dictionary.cambridge.org/us/dictionary/english/hardly) for *could hardly hear* (almost not); Cambridge B2 is a different emphatic denial sense. The current B2 example must be replaced or the entry independently retiered/replaced, not merely signed off unchanged.
- **C1 signature**: [Cambridge Learner's B1](https://dictionary.cambridge.org/us/dictionary/learner-english/signature) for a handwritten name. **C1 identical**: [Cambridge B2](https://dictionary.cambridge.org/dictionary/english/identical) for exact sameness; the draft's *looked identical, but one had a missing signature* needs a human clarity check.
- **C1 manufacturer**: [Cambridge B2](https://dictionary.cambridge.org/dictionary/english/manufacturer) for a manufacturing company. **C1 implement**: [Cambridge B2](https://dictionary.cambridge.org/dictionary/english/implement) for carrying out a plan. **C1 permit**: [Cambridge C1](https://dictionary.cambridge.org/dictionary/english/permit) for an official authorisation document, supporting further C1 exact-sense review rather than automatic rejection.

These publisher-level differences are **editorial review leads**, not independent linguistic approval or automatic proof of a wrong curriculum level. All Myanmar glosses and original examples remain unverified by an independent fluent reviewer.

**Safeguards changed on staging only:** source triage expanded in commit `c12434d5b2ef1331894fec0b544228116e104e99`; the parallel A1/A2/B1/B2/C1/ALL source-integrity validator now expects all 23 records and rejects forged approvals/source drift (commit `6c348c1971889c509411614285d0fd58d3029b0f`). Release audit now blocks the unchanged B2 *hardly* example and requires a specific independent rationale for any retained same-sense lower-source-level entry (commit `003e54434920751b40c8c138dd11bfd90dae76b6`); release ledger remains empty of reviewer/listening receipts (commit `781c2add3bb8b220a94eda18a554d52141d8e9ce`).

**GitHub Pages limits sourced, not measured:** On **2026-10-27**, [GitHub's official Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) state a **1 GB published site cap**, **1 GB recommended source repository size**, **100 GB/month soft bandwidth limit**, and **10-minute deployment timeout**. The launch auditor now refuses inflated user-supplied hosting limits and demands actual measured site/repository bytes, a monthly bandwidth forecast, a content digest, measurement method, reviewer receipt and supporting evidence URL (commit `dfa6b62fe7a332e0820efa1f8116f36ba01550bf`). **Actual site/audio inventory bytes and real bandwidth are not measured or signed off; hosting gate is still BLOCKED.**

**Verified historical Actions evidence, not evidence of these new commits:** [structural run 40465386555](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40465386555) concluded **success in all six matrix jobs** and its ALL job log recorded **14** Cambridge observations at that time, 0 independent approvals, and unchanged protected production assets. [documentary release-blocker run 40465393057](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40465393057) concluded **success** as a report-only blocker check, not as release approval; its log listed missing independent reviews, audio listening, mobile/physical iPhone, hosting and preservation signoffs. **Run IDs, conclusions and logs for the new 23-record commits have not been retrieved; latest CI remains UNVERIFIED, not passed.** No merge, main edit, production publication or public launch was performed.

## Fourth publisher sense triage — 2026-10-27 (staging only)

Four additional Cambridge publisher-owned, **search-indexed** exact-sense leads were checked on **2026-10-27**; attempted direct page access returned **HTTP 403**, so these are *not* full-page, independently reviewed dictionary or Myanmar observations. The [publisher sense evidence packet](draft/CEFR-1000-CAMBRIDGE-SENSE-TRIAGE-2026-10-27.json) now contains **27** records: **A1 0, A2 1, B1 7, B2 10, C1 9**. The four new observations are:

- **B2 prepare (verb):** [Cambridge A2 get-ready sense](https://dictionary.cambridge.org/dictionary/english/prepare) matches the draft's meeting-documents example; a separate B1 expectation sense does not justify B2.
- **B2 calm (adjective):** [Cambridge B1 relaxed/unworried sense](https://dictionary.cambridge.org/dictionary/english/calm) matches the draft's emergency example.
- **C1 upgrade (verb):** [Cambridge B2 improve-to-newer-standard sense](https://dictionary.cambridge.org/dictionary/english/upgrade) matches the draft's software example.
- **C1 insight (noun):** [Cambridge C1 deep-understanding sense](https://dictionary.cambridge.org/us/dictionary/english/insight) is consistent with the draft's survey context; independent Myanmar and example checks still required.

These are **three same-sense lower-source-level flags and one C1 supporting lead**, *not* four independent approvals. The existing fail-closed Cambridge source audit now pins all 27 against the unchanged shortlist blob and rejects false approval, forged URLs, altered labels and content drift. The release auditor already requires separate independent resolutions for every retained Cambridge triage flag, including a specific teaching-level rationale for lower-source-level senses.

**Current counts remain unchanged:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0** (first-pass written / independently approved); **1,000/1,000 held**. Final George/Emma headword+example generation and real listening, browser/mobile/physical iPhone Safari, hosting measurements, final protected-asset review and production deployment are **not verified**. Before this change, six-job structural run [40489581060](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40489581060) and documentary blocker run [40495608585](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40495608585) had actual successful job conclusions; the latter's log explicitly blocked launch. **The new 27-record commit requires its own Actions run conclusions/logs before claiming CI verification.** No main edit, merge or deployment.

### Fourth-batch CI evidence — checked 2026-10-27

The **same staging commit** [`cf9b648e8c19e2b8df6b6c0c26df04d52e735f8d`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/cf9b648e8c19e2b8df6b6c0c26df04d52e735f8d) triggered [structural run **40504135917**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40504135917): **all six A1/A2/B1/B2/C1/ALL jobs completed successfully**. The actual ALL job **122189006879** log confirms 27 Cambridge source records, zero approvals, no source-audit errors and **negative tests PASS**, plus exactly 200 first-pass entries and 200 linked review tasks per level. Its IELTS overlap check still records 120 shared headwords and zero independently resolved same-sense decisions; production-protection diff passed.

[Documentary blocker run **40504135690**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40504135690), job **122189005518**, also concluded **success** as *report-only*. Its log explicitly lists the missing independently approved manifest, **0/1,000 independent review packets**, missing real George/Emma listening, browser/mobile and physical iPhone Safari evidence, hosting measurements, final production preservation receipts and release authorisation. **These successful CI checks do not approve vocabulary or authorise publication.** All 1,000 remain held, and main/production are unchanged.

## Fifth checkpoint — eight exact-sense editorial correction proposals (2026-10-27)

**Still staging only, still blocked.** The user-approved project remains **1,000 TOTAL** (A1/A2/B1/B2/C1 = **200 first-pass bilingual entries each**), with **zero independently checked/approved in every level** and all 1,000 on hold. The separate IELTS bank, 54 lessons, existing George/Emma production audio, privacy, and main remain outside these edits.

Added [eight publisher-supported editorial decision packets](draft/CEFR-1000-SENSE-REWRITE-CANDIDATES-2026-10-27.json) on 2026-10-27: **A2 1, B1 1, B2 4, C1 2, A1 0**. Cambridge dictionary publisher-page text was observed through web search on that date, with exact headword URLs, provisional original English/Myanmar/examples, source sense labels, editorial diagnosis, reviewer tasks and an unchanged canonical shortlist blob SHA. These are **editorial proposals only**: no independent English/Myanmar/CEFR/example review, no automatic replacement, and no modification of the 1,000-row canonical shortlist.

Four **candidate rewrites**, subject to independent fluent Myanmar, English grammar and CEFR signoff:
- A2 **business**: focus the A2 countable-company sense, not the A1 trading-activity sense; preserve the matching family-business example.
- B2 **attractive**: replace the A2 visual-design example with an original beneficial-payment-plan example appropriate to Cambridge's B2 offer sense.
- B2 **hardly**: replace the B1 near-inability-to-hear example with an original B2 emphatic-unreasonableness example.
- B1 **cash**: replace the A2 physical notes/coins example with an original broader financial-resources context.

Four **replace-or-retier holds**, with **no invented replacement**:
- B2 **appointment** (draft dental appointment is A2; Cambridge job appointment is C2, not B2);
- B2 **prepare** (draft document preparation is A2; no sourced B2 meaning found);
- C1 **implement** (draft plan-in-action sense is B2);
- C1 **upgrade** (draft software-upgrade sense is B2).

Publisher URLs and observation dates are in the JSON packet; this is *not* independent review or publisher endorsement of our proposed Myanmar glosses. The rewritten sentences and definitions are original editorial candidates, not copied dictionary text.

**Safeguards:** added [editorial candidate integrity audit](tools/audit_cefr_1000_editorial_candidates.py), which binds all eight to the canonical 1,000-entry shortlist and existing Cambridge source triage, checks source URLs and provenance, rejects approval/hold bypass and requires null proposals for unsupported target-level senses. Its eight negative-test mutations include fake signoff, forged URLs, changed examples, missing rewrites and invented replacement. Added the audit to all six A1/A2/B1/B2/C1/ALL matrix jobs in [staging workflow](.github/workflows/cefr-1000-selection-structural-qa.yml). Commits: editorial packets `4bf9e09d64c72a61a1b9985bc0b0dc7da503a86a`, audit `ef9250e62bbcfbfea480e929f3e5a6b138b4f5e1`, workflow `e526434abcc8b350f17b8fb19c708a9dccac4552`, provenance fix `3deed204987d480df3d10c67aefaa2d0dc4f0588`.

**Execution evidence:** an in-tool comparison against the actual 1,000-row shortlist and 27-record Cambridge triage found one `hardly` URL variant mismatch, which was corrected. This is a deterministic data consistency check, **not a Python test run**. The GitHub connector's commit-workflow lookup is restricted to pull-request-triggered runs and returned no runs for the new push commits; the new six-job matrix **job conclusions and logs remain UNVERIFIED**. Previously observed structural run [40504135917](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40504135917) was independently re-queried here and all six historical job conclusions were **success**; this is **not** proof of success for the new audit. Previously observed report-only documentary run [40504135690](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40504135690) was also re-queried and its job conclusion was **success**, **not a launch pass**.

**Release gates remain blocked:** 0/1,000 independent human approvals; no approved manifest; final George/Emma headword+example generation/listening not signed off; no current full browser/mobile or physical iPhone Safari QA receipts; no measured hosting usage/bandwidth approval; no final protected-production-assets receipt; no verified production deployment. Do not merge, publish, claim final QA success or notify completion.
