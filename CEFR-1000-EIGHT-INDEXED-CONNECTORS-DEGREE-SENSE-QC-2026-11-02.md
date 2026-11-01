# CEFR 1,000 — Eight publisher-indexed connector/degree exact-sense triage cases (2 November 2026)

**STAGING ONLY — EDITORIAL HOLD — NOT independently verified — NO RELEASE.** Approved target is **1,000 total** (A1/A2/B1/B2/C1 exactly 200 each), not the superseded 5,000. Frozen provisional shortlist `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. All eight original English/Myanmar/example fields and source Git provenance are preserved in [the research packet](draft/CEFR-1000-CROSSLEVEL-CONNECTORS-AND-DEGREE-EIGHT-2026-11-02.json); suggestions are **unapproved**.

## Source observations and exact-sense issues

Publisher search-index observations were examined on **2026-11-02**. Direct Cambridge page requests may return HTTP 403; no direct page access, independent human reviewer or source-backed CEFR signoff is claimed. Publisher-indexed labels are research leads only.

| Draft word/level | Publisher-indexed sense evidence | Independent review question |
|---|---|---|
| apparently / B1 | [Cambridge apparently](https://dictionary.cambridge.org/dictionary/english/apparently), reported/inferred information, **B2** | Should the draft B1 card be moved, replaced or redefined? Preserve uncertainty in Myanmar. |
| critical / B1 | [Cambridge critical](https://dictionary.cambridge.org/dictionary/english/critical), adjective **IMPORTANT B2** | Draft meaning matches importance, not disapproval or medical severity; review B1–B2 conflict. |
| rather / A2 | [Cambridge rather](https://dictionary.cambridge.org/dictionary/english/rather), degree adverb **B1** | Draft degree wording may overstate intensity; distinguish from *rather than* preference. |
| fine / A2 | [Cambridge fine](https://dictionary.cambridge.org/dictionary/english/fine), **A1 SATISFACTORY** (typically predicative) versus **B1 SUNNY** (mainly UK) | Draft definition fits satisfactory A1, but the weather example is ambiguous: it could mean acceptable conditions or sunny/dry B1. Do not infer B1 automatically. |
| otherwise / B1 | [Cambridge otherwise](https://dictionary.cambridge.org/dictionary/english/otherwise), conditional-result connector **B1 conjunction**, distinct from **B2 adverb** meaning excluding a stated exception | Draft calls it an adverb; grammar label requires independent adjudication rather than automatic correction. |
| however / A2 | [Cambridge learner however](https://dictionary.cambridge.org/us/dictionary/learner-english/however), contrast **A2**, distinct from **B2** degree construction | Keep contrastive use separate from *however difficult/fast*; A2 indexed alignment is not approval. |
| therefore / B1 | [Cambridge therefore](https://dictionary.cambridge.org/dictionary/english/therefore), logical consequence **B1** | B1 indexed alignment is not approval; distinguish logical result from *otherwise* conditional warning. |
| quite / A2 | [Cambridge British Grammar: quite](https://dictionary.cambridge.org/grammar/british-grammar/quite), moderate with gradable adjectives but sometimes complete with non-gradable adjectives; **NO CEFR rating on grammar page** | Avoid an absolute *not completely* definition; retain A2 level as unverified. |

**New editorial risks:** three candidate level conflicts (*apparently, critical, rather*), one ambiguous *fine* weather-sense example (not a proven level error), a conditional-connector part-of-speech issue (*otherwise*), and a meaning-scope issue (*quite*). These are flagged for independent review; no automatic reassignment or approval.

## Mechanical safeguards and testing

- New [frozen research auditor](tools/audit_cefr_1000_crosslevel_connectors_degree_eight.py) pins the exact source packet and shortlist Git blob; checks all eight original bilingual/examples/source provenance, exact publisher URLs and observation date, rejects false review flags and release claims.
- Synthetic negative tests mutate 20 fields on each of eight records plus four root-level release/provenance fields (**164 planned mutations**); these are **mechanical tests**, not independent linguistic approval.
- Integrated into [six-lane structural QA](.github/workflows/cefr-1000-selection-structural-qa.yml) for A1, A2, B1, B2, C1 and ALL. CI run IDs, conclusions and logs for this change must be verified before marking the new test as CI-passed. Do not equate prior successful runs with this revision.

## Release blockers

First-pass written/independently checked: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. All 1,000 remain held; no independently approved manifest. Final George/Emma headword and example audio and **real human listening receipts**, automated browser/mobile regression, **physical iPhone Safari** review, measured GitHub Pages hosting readiness, final preservation check of 54 lessons and separate IELTS 1,000-word bank, and confirmed production deployment are still missing. Existing George/Emma production audio and privacy assets must not be touched. No main-branch edit, merge or deployment is authorised until every gate has true evidence.
