# CEFR 1000 — Eight B1 exact-sense triage cards (2 November 2026)

**Status: RESEARCH ONLY / STAGING / EDITORIAL HOLD / DO NOT PUBLISH.** This is the user-approved **1,000-total** curriculum, not the superseded 5,000-word proposal. The branch is `cefr-5000-bilingual-qa-staging` (unchanged). No human-independent review, production edit, voice-listening signoff or deployment is claimed.

## Eight source-backed sense comparisons

All eight original cards are in the frozen B1 first-pass shortlist. Oxford Advanced Learner's Dictionary pages were **directly opened** on 2 November 2026 to inspect the relevant English senses and grammar. Cambridge Dictionary pages appeared in **public publisher search-index results** with CEFR labels, but direct opening of the cited Cambridge URLs returned **HTTP 403**. These labels are **indexed publisher research leads**, not independently verified human signoffs. Oxford topical CEFR labels (e.g. Scientific research b1, Houses and homes c1) **must not be mistaken for word-level or exact-sense CEFR labels**.

| Frozen B1 word | Cambridge indexed sense/level | Triage | Direct Oxford sense locator | Cambridge indexed source |
| --- | --- | --- | --- | --- |
| **analysis** | detailed examination **B2** | B1 → B2 conflict | [Oxford lines 119–138](https://www.oxfordlearnersdictionaries.com/definition/english/analysis) | [Cambridge](https://dictionary.cambridge.org/dictionary/english/analysis) |
| **impact** | strong effect **B2** | B1 → B2 conflict | [Oxford lines 103–120](https://www.oxfordlearnersdictionaries.com/definition/english/impact_1) | [Cambridge](https://dictionary.cambridge.org/dictionary/english/impact) |
| **independent** | not controlled/influenced **B2** | B1 → B2 conflict; distinguish B1 self-reliant person | [Oxford lines 174–188](https://www.oxfordlearnersdictionaries.com/definition/english/independent_1) | [Cambridge Learner](https://dictionary.cambridge.org/dictionary/learner-english/independent) |
| **primary** | main/most important **B2** | B1 → B2 conflict; not primary-school sense | [Oxford lines 115–123](https://www.oxfordlearnersdictionaries.com/definition/english/primary_1) | [Cambridge Learner](https://dictionary.cambridge.org/dictionary/learner-english/primary) |
| **ship** | large sea-going boat **A2** | B1 → A2 conflict; not verb or fandom noun | [Oxford lines 105–129](https://www.oxfordlearnersdictionaries.com/definition/english/ship_1) | [Cambridge](https://dictionary.cambridge.org/dictionary/english/ship) |
| **cash** | coins and banknotes **A2** | B1 → A2 conflict; distinguish broader B1 money sense | [Oxford lines 103–116](https://www.oxfordlearnersdictionaries.com/definition/english/cash_1) | [Cambridge Learner](https://dictionary.cambridge.org/dictionary/learner-english/cash) |
| **fan** | air-moving device **B1** | same-level sense-alignment control | [Oxford lines 171–178](https://www.oxfordlearnersdictionaries.com/definition/english/fan_1) | [Cambridge](https://dictionary.cambridge.org/dictionary/english/fan) |
| **male** | adjective describing male sex **B1** | same-level POS control; noun separately B2 | [Oxford lines 105–138](https://www.oxfordlearnersdictionaries.com/definition/english/male_1) | [Cambridge Learner](https://dictionary.cambridge.org/dictionary/learner-english/male) |

The [eight-card JSON research packet](draft/CEFR-1000-B1-EIGHT-CAMBRIDGE-INDEXED-EXACT-SENSE-TRIAGE-2026-11-02.json) preserves **all original English definitions, Myanmar meanings, original examples, source paths, source indices, historical Git blob SHAs, source URLs, direct Oxford line locators, observation dates, indexed access limitations, eight proposed unapproved Myanmar/example alternatives, and explicit false approval flags**. The frozen shortlist was not edited. An independent English/Myanmar/exact-sense reviewer must decide whether to retain, replace or relocate each entry without violating exactly 200 reviewed headwords/senses per level.

## Fail-closed structural safeguards

The [pinned research auditor](tools/audit_cefr_1000_b1_eight_indexed_sense.py) checks the immutable packet Git blob SHA `8e71b2acc0ae4c347053ce8039b916e675c1d9eb`, frozen shortlist Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, exact original bilingual/example/provenance snapshots, eight word/POS/sense source URL bindings, date, Cambridge indexed-only access status, zero approvals and release holds. Its **214 programmed adversarial mutations** target forged publisher levels, URLs, source access, translations, examples, historical provenance, release status and human-review receipts. The structural workflow invokes the audit in all six parallel A1/A2/B1/B2/C1/ALL lanes, with negative tests in ALL. The documentary no-deployment workflow also invokes the negative tests.

**CI evidence boundary:** The previous [six-lane structural run 41347371667](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41347371667), ALL job `124969979895`, was checked and succeeded at earlier SHA `fa302048c82da8d5f2c93cee1941000c4d73c6b2`. Its actual logs showed earlier 166/166 and 150/150 mutation tests passed. **That run predates these eight new cards and does not verify this auditor.** Commit-run lookup for new staging pushes returned no retrievable PR-triggered runs and combined statuses were empty; new run IDs, job conclusions and logs remain **UNVERIFIED**, and **214/214 passed is not claimed**. Inspect actual new jobs/logs and repair failures on the next feasible run.

## Release blockers and protected production

| Level | First-pass written | Independently checked/approved | Held |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

Final George/Emma headword and example audio generated for the approved manifest: **not established**; genuine final real-listening signoffs: **0/1,000**. Independent English, fluent Myanmar, example grammar and exact-sense CEFR review, approved manifest, full voice recordings/listening, browser/mobile regression, **physical iPhone Safari** evidence, GitHub Pages hosting measurements, privacy/preservation verification and production deployment remain missing. Protect the **54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy**. No merge, main change or publication. **RELEASE BLOCKED — STAGING ONLY.**
