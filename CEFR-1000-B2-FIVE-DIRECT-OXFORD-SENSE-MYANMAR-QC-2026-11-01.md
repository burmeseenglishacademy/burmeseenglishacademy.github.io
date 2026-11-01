# CEFR 1,000 — B2 five directly observed Oxford sense / Myanmar QC (1 November 2026)

**Scope:** user-approved 1,000 TOTAL, A1/A2/B1/B2/C1 = 200 each. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Status:** EDITORIAL HOLD / RELEASE BLOCKED. No merge, main edit, recording, audio listening, iPhone test or publication.

## Direct publisher research (Oxford Advanced Learner's Dictionary)

Five live Oxford publisher pages were opened and their relevant entry lines inspected on **2026-11-01**. The five original frozen entries, their Myanmar glosses and their original examples remain unchanged. All examples are grammatical. This is editorial **research**, not independent human approval or independently verified exact-sense CEFR classification.

| Frozen B2 headword | Direct publisher URL and observed lines | Evidence / exact-sense distinction | Editorial follow-up |
| --- | --- | --- | --- |
| relief (noun) | [Oxford relief](https://www.oxfordlearnersdictionaries.com/definition/english/relief), lines 104–139, 170–175, 214–228 | Emotional relief differs from reducing pain and from humanitarian aid. Original missing-bag example demonstrates emotional relief. Oxford *Feelings b2* is a topic tag, not a separate exact-sense CEFR signoff. | Check whether the Myanmar gloss conveys emotional relief and verify B2 with an independent direct exact-sense publisher CEFR receipt. |
| resistance (noun) | [Oxford resistance](https://www.oxfordlearnersdictionaries.com/definition/english/resistance), lines 119–129, 163–168, 204–215 | Opposition to a proposed change differs from armed resistance and resistance to disease. The directly observed *Preferences and decisions c1* topic tag raises a **B2-versus-C1** review question, not an automatic relevel. | Obtain independent exact-sense CEFR proof. Do not borrow the B2 self-restraint sense of the **verb** *resist* as evidence for this noun. |
| retail (noun) | [Oxford retail](https://www.oxfordlearnersdictionaries.com/definition/english/retail_1), lines 88–117, 130–141 | Uncountable noun for direct-to-public goods selling, contrasted with wholesale; other *retail* adverb/verb entries are distinct. | Independently check sector-specific Myanmar wording and exact-sense CEFR. |
| shame (noun) | [Oxford shame](https://www.oxfordlearnersdictionaries.com/definition/english/shame_1), lines 107–120, 143–166 | *A shame* (a disappointment) differs from uncountable shame (internal guilt or embarrassment). The original lying-to-a-friend example is noun sense 2. | Original Burmese **အရှက်ကွဲမှု** can suggest public loss of face; review a private-guilt gloss. Keep any replacement example a **noun** use, not *ashamed* adjective. |
| somewhat (adverb) | [Oxford somewhat](https://www.oxfordlearnersdictionaries.com/definition/english/somewhat), lines 88–117 | Rather formal degree modifier meaning *to some degree*; the original *somewhat more practical* is grammatical. | Review **တစ်စိတ်တစ်ပိုင်း** for possible physical-part ambiguity; consider **အတန်အသင့် / အနည်းငယ်** depending on context. |

Cambridge direct dictionary opens for the five words returned **HTTP 403** on this run. A search-index Cambridge result for *relief* displays B2 for the emotional sense, but indexed text is **not** an independently inspected publisher page or an authenticated independent review. No CEFR flags were changed.

## Reproducible staging evidence

- [Five-record source packet](draft/CEFR-1000-B2-FIVE-DIRECT-OXFORD-SENSE-AND-MYANMAR-TRIAGE-2026-11-01.json): original frozen definition, Myanmar gloss, example, historical `source_path`, `source_index`, `source_blob_sha`, directly observed Oxford URL, date, line locator, risk and **unapproved** teaching alternative.
- [Fail-closed auditor](tools/audit_cefr_1000_b2_five_direct_sense.py): immutable source-packet comparison; original shortlist Git-blob pin; exactly 1,000 held words and 200 per level; zero independent flags; historical Git source-blob/index checks; negative mutation tests for source, English, Myanmar, example, provenance, false human approval and false listening.
- Both [six-lane structural QC](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deployment QC](.github/workflows/cefr-1000-go-live-qc-gate.yml) invoke the auditor. The five CEFR lanes and ALL remain parallel. A passing documentary job is **not** a release signoff.

## Release blockers (unchanged)

First-pass written / independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. All 1,000 remain on editorial hold. Independent human English, Myanmar, original-example and exact-sense CEFR review; deduplicated approved manifest; both George/Emma headword and example audio with **real listening**; browser/mobile regression; physical iPhone Safari; measured GitHub Pages limits; independent protected-asset/privacy checks and confirmed production deployment are missing. **DO NOT PUBLISH.**

**CI note:** Actual new workflow run conclusions, job logs and commit SHA must be appended only after retrieval. Historical successful runs do not verify this packet.

## Actual GitHub Actions verification (not linguistic signoff)

At tested SHA `5b193d2e3a2f187be3c74fc16e55d8f54b2e0534`, [six-lane structural run 41311661417](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41311661417) completed **SUCCESS** for A1, A2, B1, B2, C1 and ALL. Actual ALL job `124863138760` logs confirmed **90/90** adversarial mutations rejected by the new auditor and 5/5 B2 research records source-bound, with 0 independent approvals. ALL artifact ID `13086080134`.

[Documentary no-deployment run 41311661271](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41311661271) completed **SUCCESS (report-only)** at the same SHA; actual job `124863137939` logs confirmed **90/90** mutations rejected, the independently reviewed word packets remain **0/1,000**, and protected production assets check passed. Blocker artifact ID `13085920316`. These tests check source/provenance and reporting integrity; they do **not** authenticate external humans, listen to George/Emma audio, test a physical iPhone, measure production hosting or confirm deployment.

The five files changed since previous staging checkpoint are solely two QC workflows, one new research JSON, one new source auditor and this documentation; production files were not edited. **STAGING ONLY / RELEASE BLOCKED.**
