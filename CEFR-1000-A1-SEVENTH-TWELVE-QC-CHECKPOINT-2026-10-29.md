# CEFR 1,000 — A1 seventh Oxford twelve, source-integrity and CI checkpoint (29 October 2026)

**BLOCKED / STAGING ONLY.** User-approved scope is **1,000 TOTAL** entries, not the abandoned 5,000 target. Exactly 200 provisional first-pass entries each at A1, A2, B1, B2 and C1. All 1,000 are on editorial hold; **zero** independently approved. Work and CI were restricted to `cefr-5000-bilingual-qa-staging`. No main change, merge, publication, production audio replacement or privacy change.

## Direct publisher source observations

On **2026-10-29**, directly inspected Oxford University Press's official [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and added **12 previously unobserved A1 provisional words** to [the seventh A1 packet](draft/CEFR-1000-OXFORD-A1-SEVENTH-TWELVE-2026-10-29.json). All twelve have Oxford A1 **word/POS** observations, not independently verified **exact-sense** CEFR. PDF pages below are **1-based** and extracted lines **0-based**, as recorded in the research packet.

| Provisional word | Oxford PDF word/POS excerpt | PDF page / extracted line | Human editorial risk |
|---|---|---:|---|
| `to` | to prep., infinitive marker | 3 / 804 | `TO_DESTINATION_VS_INFINITIVE` |
| `from` | from prep. | 2 / 316 | `FROM_ORIGIN_VS_START_TIME` |
| `with` | with prep. | 4 / 886 | `WITH_ACCOMPANIMENT_VS_INSTRUMENT` |
| `for` | for prep. | 2 / 305 | `FOR_BENEFICIARY_VS_PURPOSE` |
| `of` | of prep. | 3 / 541 | `OF_POSSESSION_VS_PARTITIVE` |
| `at` | at prep. | 1 / 50 | `AT_TIME_VS_LOCATION` |
| `as` | as prep. | 1 / 48 | `AS_ROLE_VS_COMPARISON` |
| `by` | by prep. | 1 / 120 | `BY_TRANSPORT_VS_PASSIVE_AGENT` |
| `about` | about prep., adv. | 1 / 5 | `ABOUT_TOPIC_VS_APPROXIMATION` |
| `after` | after prep. | 1 / 17 | `AFTER_TIME_PREP_VS_A2_CONJ_ADV` |
| `before` | before prep. | 1 / 75 | `BEFORE_TIME_PREP_VS_A2_CONJ_ADV` |
| `how` | how adv. | 2 / 381 | `HOW_QUESTION_WORD_VS_ADVERB_TAXONOMY` |

**Critical sense/POS distinctions:** `after` and `before` are A1 **prepositions** in Oxford but have separate A2 conjunction/adverb classifications; `as` has an A1 preposition versus A2 adverb/conjunction distinction; `to` combines destination preposition and infinitive marker; `by` draft definition mixes transport means and passive agent; `at` mixes time and location; `how` is labelled “question word” in the draft but **adverb** in Oxford. These are explicit **independent reviewer tasks**, not automated corrections. Four original English/Myanmar/example rewrite suggestions (`at`, `by`, `of`, `how`) were added to the packet as **UNREVIEWED_UNAPPLIED_PROPOSAL**; no frozen shortlist entry was changed.

Each source record binds the original English definition, Myanmar meaning and example sentence to the historical source path/index/Git blob SHA and the frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. It also stores the official publisher URL, observation date, PDF page/line and literal short word/POS excerpt. **A publisher word/POS list cannot independently prove a particular dictionary sense, Myanmar translation, example correctness or reviewer approval.**

## Exact audited research and human-review counts

| Level | First-pass written | Independently approved | Distinct direct Oxford word/POS observations |
|---|---:|---:|---:|
| A1 | 200 | 0 | **112** |
| A2 | 200 | 0 | 60 |
| B1 | 200 | 0 | 60 |
| B2 | 200 | 0 | 58 |
| C1 | 200 | 0 | 39 |
| **Total** | **1,000** | **0** | **329** |

The cross-batch auditor now processes **23 Oxford research packets**, containing **348 source observations** and **329 distinct provisional headwords** (19 repeated observations, not extra words). The full 1,000-entry reviewer handoff categorizes **671 without direct Oxford observations, 124 publisher-lower provisional-level discrepancies, 7 publisher-higher discrepancies, 3 absent from inspected core lists, and 195 matching word/POS labels**. These sum to 1,000; all 1,000 still need independent **exact-sense English/Myanmar/example/CEFR** review. “Unlisted” is **not** a CEFR classification. The 36 historical recovered PDF excerpts remain supplements, not additional headwords.

## Fail-closed checks actually executed

Created [the seventh A1 integrity auditor](tools/audit_cefr_1000_oxford_a1_seventh_twelve.py) to bind all 12 research records, English/Myanmar/examples, source locators, original Git provenance, fixed editorial risks and four unapplied rewrites. It rejects duplicate coverage against the prior six A1 packets and forged independent receipts. **250/250 deliberate adversarial mutations were rejected in actual ALL-job and documentary logs**, including source changes, falsified Myanmar/examples, forged human approval, manipulated dates/pages and false editorial signoff.

Updated cross-batch [Oxford coverage auditor](tools/audit_cefr_1000_oxford_coverage.py), [human review-handoff generator](tools/audit_cefr_1000_review_priority.py), [parallel six-lane structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deployment gate](.github/workflows/cefr-1000-go-live-qc-gate.yml).

- [Structural run **40814579134**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40814579134), head `7af6a97531a5ffe9823338ee6e7c09c4b4516593`: **SUCCESS**, with all six A1/A2/B1/B2/C1/ALL jobs **success**. Actual ALL job `123252556949` logs **250/250** new mutation rejections, **329** distinct Oxford research headwords, the updated complete reviewer handoff, **145/145** handoff tamper tests rejected, and protected production assets **PASS unchanged**.
- [Documentary no-deployment run **40814584848**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40814584848), head `b63067d9e1acb5cf6a4ece99a880ccbb9d5cfd2e`: **SUCCESS as report-only**, actual job `123252575063`. Logs show **250/250** new negative tests rejected, 329/1,000 source observations, **0/1,000** independent review, **0/1,000** final George/Emma listening, missing release evidence correctly **BLOCKED**, protected production assets **PASS unchanged**, and no deployment.

An earlier intermediate run at `a680695` failed while the coverage table and handoff counts were still being updated; subsequent full runs above were actually executed and passed. The verified structural code was not changed after its successful run; the later commit only modified the documentary workflow.

## Unresolved release blockers

**Still missing:** independent human-signed, content-bound English, fluent Myanmar, original-example and exact-sense CEFR review for every final entry; approved exactly-200-per-level deduplicated manifest; generated British George **and** Emma headword **and** example audio with **real listening signoffs** (currently **0/1,000**); full approved-corpus browser/mobile regression; real physical iPhone Safari QA evidence; measured GitHub Pages hosting constraints; final preserved-production inventory and authenticated confirmation of live deployment. GitHub Actions success means **structural and fail-closed checks passed**, not release approval. The protected 54 lessons, separate IELTS 1,000-word bank, existing production George/Emma audio and privacy safeguards were not modified.

**Release decision: BLOCKED / STAGING ONLY. Do not merge, publish, modify main, or claim deployment.**
