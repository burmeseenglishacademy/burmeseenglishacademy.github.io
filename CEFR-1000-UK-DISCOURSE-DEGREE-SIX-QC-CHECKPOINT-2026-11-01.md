# CEFR 1,000 — UK discourse and degree adverbs, six direct Oxford sense checks (1 November 2026)

**STAGING ONLY — RELEASE BLOCKED.** User-approved scope remains **1,000 total**: A1/A2/B1/B2/C1 = **200 each**. The frozen first-pass shortlist and independent review task list were not edited. The [six-record source packet](draft/CEFR-1000-UK-DISCOURSE-DEGREE-SIX-2026-11-01.json) retains the original English definitions, Myanmar meanings, example sentences, historical source paths, indices and Git blob SHAs, with unapproved bilingual/example alternatives.

## Directly inspected publisher evidence

All six Oxford Advanced Learner's Dictionary headword pages were directly opened on **2026-11-01**. Dictionary sense explanations and usage examples support **research observations only**. Oxford topic CEFR badges and publisher word/POS lists are **not exact-sense CEFR certification**.

| Held headword | Source and observed lines | Exact-sense / Myanmar teaching issue |
|---|---|---|
| **quite** (A2 adverb) | [Oxford quite](https://www.oxfordlearnersdictionaries.com/definition/english/quite), lines 107–115, 129–139 | British **quite long** can mean fairly long, but **quite impossible / quite sure** can mean completely. The original Myanmar gloss conveys moderate degree only. Proposed nuance is held, not a correction approved for release. |
| **rather** (A2 adverb) | [Oxford rather](https://www.oxfordlearnersdictionaries.com/definition/english/rather_1), lines 107–132 | Degree adverb may convey surprise, mild criticism or disappointment; differs from **rather than**. Original example is grammatical; no forced rewrite. |
| **actually** (A2 adverb) | [Oxford actually](https://www.oxfordlearnersdictionaries.com/us/definition/english/actually), lines 105–128 and later usage note | Fact/expectation contrast and polite correction; **not** a synonym for **currently**. Original example correctly contrasts weekdays. |
| **however** (A2 adverb) | [Oxford however](https://www.oxfordlearnersdictionaries.com/definition/english/however_1), lines 105–122 | Contrastive linking adverb versus **however carefully** (whatever degree). Original semicolon construction is appropriate; don't teach it as a direct conjunction replacing *but* in a comma splice. |
| **therefore** (B1 adverb) | [Oxford therefore](https://www.oxfordlearnersdictionaries.com/definition/english/therefore), lines 105–114 | Logical consequence, not contrast. Original semicolon construction is appropriate. |
| **eventually** (B1 adverb) | [Oxford eventually](https://www.oxfordlearnersdictionaries.com/definition/english/eventually), lines 105–119 | Outcome after time/events; **finally** is preferable for the final point in a list. Cambridge indexed B2 versus provisional B1 remains an **unresolved lead**, not an approved level change. |

Supplementary publisher grammar references inspected on **2026-11-01**: [Cambridge quite](https://dictionary.cambridge.org/grammar/british-grammar/quite), [Cambridge actual and actually](https://dictionary.cambridge.org/us/grammar/british-grammar/actually), and [Cambridge eventually](https://dictionary.cambridge.org/grammar/british-grammar/eventually). Direct Cambridge dictionary access for *eventually* returned **HTTP 403**; its indexed B2 label must not be represented as direct-page verification or independent exact-sense CEFR review.

## Staging safeguards and verification boundary

The [immutable six-record auditor](tools/audit_cefr_1000_uk_discourse_degree_six.py) checks source-bound research fields, historical bilingual/example/provenance snapshots, the exact **200/level** provisional counts, all **1,000 editorial holds**, and **zero independent approvals**. Its adversarial self-test mutates individual packet fields, inserts forged independent review, deletes records, changes metadata, alters hold/review flags and changes a held Myanmar meaning. **Passing this auditor cannot substitute for a human reviewer or real listening.**

Wired into the [six-lane structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) for A1/A2/B1/B2/C1/ALL and the [documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml). Staging commits: research packet `e94437a813191e3da24aa7667eb33a8346e7fce6`; auditor `4da45704cd47b524e22d4ba24323a6799903df4a`; structural workflow `50b3a6f1ef1b28131b154737a79a59cbfcfb3b2f`; documentary workflow `18ed6665c338ae99c7c17b36589c7e0189a81acd`.

**CI run conclusions and logs for these changes: NOT VERIFIED.** The connected commit-run query returns PR-triggered runs only and found none for the latest staging push; combined commit statuses were empty. No GitHub Actions SUCCESS or mutation-pass count is claimed. Comparison with prior staging checkpoint `a26d11b744591a51e99d2ad26cef3b53addc690b` showed **four commits affecting only the packet, auditor and two staging workflows**. No production assets changed in that comparison.

## Exact release blockers (unchanged)

| CEFR level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Oxford word/POS research coverage remains **995/1,000**, not independently checked. Final George/Emma actual listening signoffs **0/1,000**. Still missing: genuine independent human English/Myanmar/example/exact-sense CEFR review, approved deduplicated manifest, complete British George/Emma headword and example audio plus real listening, desktop/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting readiness, protected-production verification at launch and confirmed live deployment. **Do not merge, alter main, deploy or claim completion.**
