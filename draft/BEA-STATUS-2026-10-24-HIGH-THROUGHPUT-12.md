# Burmese English Academy — high-throughput batch12 checkpoint — 24 October 2026 (SGT)

**STAGING ONLY. UNVERIFIED. NOT RELEASE READY. NEVER MERGE UNAPPROVED DATA.**

## New substantive work

- Authored **80 original first-pass English/Myanmar vocabulary drafts** in `draft/A2-C1-EDITORIAL-BATCH12.json`: **A2 20, B1 20, B2 20, C1 20**. Each has a part of speech, newly written English learner definition, Burmese gloss and grammatical illustrative sentence. All level labels are **provisional frequency-derived candidate placements**, not independently verified CEFR assignments. C1 drafts are explicitly high-risk for sense-level CEFR review.
- Authored 80 distinct **independent source-evidence / Burmese-language / example / CEFR / audio review tasks** in `draft/A2-C1-REVIEW-TASKS-BATCH12.json`. Dictionary URLs are **unvisited lookup leads**, not checked sources. No reviewer signatures or checked evidence were invented. All approval flags remain false.
- Avoided drafting the inflected plural `minutes` and an American-spelling candidate `center` in this British-English editorial batch; substituted candidate headwords `main` and `role` after checking candidate-pool membership. Neither substitution is CEFR approval.
- Quarantined **20 additional proper-name or demonym candidates** from provisional C1, increasing held candidates **136 → 156**. These are review holds, not definitive rejections or validated reclassifications.
- Added `tools/audit_cefr_batch12_review_tasks.py` and `.github/workflows/cefr-batch12-review-qa.yml` with **five parallel jobs** (A2, B1, B2, C1 and ALL). The audit checks candidate-pool membership, level alignment, draft/quarantine exclusion, example headword presence, original content fields, unreviewed source fields and non-publication. It **does not check linguistic correctness**.

## Exact written / independently approved inventory

The previous integrated `A2-C1-EDITORIAL-STARTER.json` holds 926 A2–C1 drafts; batch12 is a separate **unintegrated staging-only** 80-entry file. The table counts unique written entries across both files (the batch12 audit rejects duplicate headwords against the starter). A1 is the separate existing 500-draft inventory.

| Provisional level | Target | Written drafts | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 256 | 0 | 444 |
| B1 | 1000 | 256 | 0 | 744 |
| B2 | 1300 | 256 | 0 | 1044 |
| C1 | 1500 | 238 | 0 | 1262 |
| **Total** | **5000** | **1506** | **0** | **3494** |

**The 5,000-headword candidate pool is not a completed 5,000-entry bilingual dictionary.** All drafts are unpublished and require word/sense/POS/level, Burmese and example review.

## Actual commits and GitHub Actions results

- Batch12 draft commit: `44018fb7d295b4867cb7aa4b1b28c73598b68df6`.
- Batch12 independent review-task commit: `3e10f19ef182c1fe5ff88666a289ad7111a1e3ac`.
- Editorial lemma substitution commits: `f6dbf2af78f73e937592d65202ef66c5b0e6512e`, `4bd5494a1d0287884540eae0d911d192325973d0`.
- New structural auditor commit: `e64192636ffae1dbfc6c09dbcdbed289153fd50b`; workflow commit: `a2c8fc339a02e3b1b0a1ee1b838677ae73c9de7d`.
- Quarantine expansion commit: `1d14bf45c2fb288eade2145e88043d389fd0981b`.
- Initial batch12 run [40099003950](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40099003950): **FAILURE** in A2 and ALL; B1/B2/C1 passed. Real A2 log: `AssertionError: sound` because the validator incorrectly rejected a legitimate short Burmese gloss `အသံ` based on character count. The content was not padded; the validator was repaired to require nonempty Myanmar-script text instead.
- A subsequent batch12 run [40099058921](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40099058921) also failed before the same fix was committed. These failures remain visible in Actions history.
- QA correction commit: `7e419eb23cb9e49a2de0072683df5c08c52f5b59`.
- Corrected batch12 run [40099085833](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40099085833): **COMPLETED / SUCCESS**. Inspected actual job statuses: **A2 SUCCESS, B1 SUCCESS, B2 SUCCESS, C1 SUCCESS, ALL SUCCESS**. Inspected ALL job `120887337834` log: `STAGING ONLY: batch12 ALL structure PASS; 80 drafts, 0 approvals; no audio or deploy`.
- Expanded quarantine run [40099058933](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40099058933): **COMPLETED / SUCCESS**; holdout-validation job `120887261842` succeeded. This is quarantine bookkeeping, not independent dictionary review.
- Existing earlier batch05–11 structural checks observed on the quarantine push also succeeded. No real audio listening or physical-device test is inferred.

## Release blockers and production isolation

- **0 of 5,000 entries independently approved** for the exact English sense, natural Myanmar meaning, part of speech, grammatical example, CEFR level and pronunciation. Automated QA success is not editorial verification.
- Batch12 entries have not yet been merged into the 926-entry editorial starter or 45 review-packet artefacts; do not double-count them or imply the integrated dataset contains 1,006 A2–C1 entries.
- No newly generated or listening-validated complete George/Emma CEFR vocabulary audio set. The existing production audio is preserved.
- No complete final-corpus browser/mobile regression, **physical iPhone Safari acceptance test**, GitHub Pages storage/bandwidth acceptance or production release of the new vocabulary.
- The live site, production **54 lessons**, separate **IELTS 1,000** bank, existing George/Emma files and privacy behaviour were not changed in this iteration. The CEFR published data module remains empty by design.
- Next useful work: prepare another independently reviewable 40–100+ candidate-aligned first-pass drafts with stronger sense-specific CEFR triage; expand human/source review evidence; integrate vetted drafts into packets without weakening release gates.

**No full-completion notification is justified.**
