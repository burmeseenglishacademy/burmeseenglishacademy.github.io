# CEFR 1,000 — C1 sixteenth twelve: official Oxford core-list absence and eight direct sense leads

**Observed:** 2026-11-01. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Status:** STAGING ONLY / RELEASE BLOCKED. This is the USER-APPROVED 1,000-total plan (200 each A1–C1), **not** the superseded 5,000-word plan.

## Direct publisher research and limits

Official publisher sources directly inspected on 2026-11-01:

- [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), 12-page PDF.
- [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf), 8-page PDF.

Exact word/POS combinations **not found in either inspected core list**: meticulous (adj.), nuanced (adj.), pragmatic (adj.), scrutinize (v.), stringent (adj.), tenacious (adj.), ubiquitous (adj.), vindicate (v.), vilify (v.), whimsical (adj.), acquiescence (n.), ameliorate (v.). These are **12 source-absence observations, not twelve C1 confirmations**. No inferred CEFR label, invented PDF locator, or human approval is recorded.

Eight directly opened Oxford Advanced Learner's Dictionary pages supply **sense/grammar leads only**, not CEFR labels:

| Draft word | Direct official dictionary | Evidence inspected | Editorial issue |
|---|---|---|---|
| meticulous | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/meticulous) | page lines 88–114 | careful attention to details; the *Personal qualities C2* topic label is not a headword level |
| nuanced | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/nuanced) | lines 88–107 | subtle differences of meaning/expression, UK pronunciation; unrelated footer B2 is not the headword level |
| pragmatic | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/pragmatic) | lines 88–123 | practical sensible problem solving, `approach to` and `pragmatic about` |
| scrutinize | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/scrutinize) | lines 88–123 | British variant **scrutinise** is explicitly listed; maintain consistent British editorial/audio policy |
| vindicate | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/vindicate) | lines 88–118 | `vindicate something` = justify decision/belief, versus `vindicate somebody` = show innocence |
| whimsical | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/whimsical) | lines 88–107 | unusual/playful can be amusing **or annoying**; first-pass meaning is exclusively positive |
| acquiescence | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/acquiescence) | lines 88–115 | formal, uncountable acceptance despite doubt; **silence is not automatically consent**; page's unrelated topic/footer badges are not CEFR |
| ameliorate | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/ameliorate) | lines 88–123 | formal transitive verb for improving a bad/insufficient state; C2 topic badge is not headword CEFR |

Source-bound [12-record JSON research packet](draft/CEFR-1000-OXFORD-C1-SIXTEENTH-TWELVE-AND-EIGHT-DIRECT-SENSE-LEADS-2026-11-01.json) preserves all frozen English definitions, fluent-Myanmar first-pass meanings, original examples, historical Git blob SHA/row indices (Batch57 and Batch58), direct publisher URLs, observation dates, dictionary line locators, and **eight explicitly unapproved** bilingual/example alternatives. No original shortlist entry was edited.

## Fail-closed checks

[New pinned auditor](tools/audit_cefr_1000_oxford_c1_sixteenth_twelve.py) validates the immutable packet and historical source blobs, original shortlist snapshots, 12 source-absence records, eight actual dictionary-page leads, editorial holds and zero signoffs. It defines **210 adversarial mutations** against fabricated Oxford CEFR classifications/locators, historical provenance, English/Myanmar/example changes, false review/approval, dictionary access and listening. Wired into the A1/A2/B1/B2/C1/ALL parallel structural workflow and documentary no-deployment QC.

Code reconciliation target after this batch (not independent approval): **A1 195/200, A2 200/200, B1 200/200, B2 200/200, C1 171/200 = 966/1,000 distinct Oxford observations**, across **985 observations**; 34 without these direct Oxford observations. The independent-review priority queue becomes **82 core-list-unlisted, 61 publisher-higher, 352 publisher-lower, 471 matching word/POS but exact-sense-unverified, 34 unobserved**. Word/POS and core-list-absence observations are **not** exact-sense CEFR review.

**Human review:** A1 200 written/0 independently approved; A2 200/0; B1 200/0; B2 200/0; C1 200/0. **Final George/Emma actual listening:** 0/1,000. Approved manifest, genuine independent English/Myanmar/example/exact-sense CEFR review, dual-voice generation/listening, browser/mobile regression, real physical iPhone Safari, measured GitHub Pages artifact and hosting, protected-assets verification at final launch, and confirmed production deployment remain mandatory blockers. No branch merge, main edit, publishing, or fake listening/device signoff.

**CI verification:** Await actual completed GitHub Actions job conclusions and logs for latest staging code; a workflow being queued/in progress does **not** count as SUCCESS.
