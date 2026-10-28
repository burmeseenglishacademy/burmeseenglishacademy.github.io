# CEFR 1,000 — six unlabelled Cambridge C1 source leads and release-safeguard checkpoint (2026-10-28)

**Release decision: BLOCKED / STAGING ONLY.** Approved scope is **exactly 1,000 total** bilingual CEFR entries: A1 200, A2 200, B1 200, B2 200, C1 200. The former 5,000-word plan is superseded. Work was restricted to `cefr-5000-bilingual-qa-staging`. No merge, main change, live deployment, independent approval, or physical iPhone/audio listening is claimed.

## Six substantive publisher-indexed C1 editorial investigations

[New source packet](draft/CEFR-1000-CAMBRIDGE-UNLABELLED-C1-SIX-2026-10-28.json) binds six existing C1 drafts to the **unchanged** provisional shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. The packet includes original English definitions, Myanmar meanings, examples, historical source paths/indices/blob hashes, publisher headword URLs, observation date **2026-10-28**, source-access caveat, editorial risks and independent reviewer tasks. These are not six new words and do not raise the written total.

| C1 draft | Cambridge publisher-indexed sense observation | Independent editorial work still needed |
| --- | --- | --- |
| [abstruse](https://dictionary.cambridge.org/dictionary/english/abstruse) | Formal adjective: complex/difficult to understand; **no visible CEFR label** | Check whether Myanmar gloss unnecessarily restricts use to ideas; independent C1 exact-sense proof |
| [equivocate](https://dictionary.cambridge.org/dictionary/english/equivocate) | Formal intransitive verb: intentionally evasive speech; **no visible CEFR label** | Distinguish concealing truth from merely not giving a direct answer; Myanmar nuance and example grammar |
| [obfuscate](https://dictionary.cambridge.org/dictionary/english/obfuscate) | Formal verb: makes information less clear, often intentionally; separate internet/data and code senses; **no visible CEFR label** | Draft asserts deliberateness but its jargon example can describe unintentional obscurity; align definition/example/translation |
| [fortitude](https://dictionary.cambridge.org/dictionary/english/fortitude) | Formal uncountable noun: sustained courage under hardship; **no visible CEFR label** | Review whether draft's extra “patience” is semantically necessary and verify natural Myanmar |
| [alacrity](https://dictionary.cambridge.org/dictionary/english/alacrity) | Formal uncountable noun: eager, prompt action; **no visible CEFR label** | Draft adds “cheerful/happy”; confirm whether Myanmar `ပျော်ရွှင်စွာ` overtranslates |
| [salience](https://dictionary.cambridge.org/dictionary/english/salience) | Formal uncountable noun: importance/relevance in a discussion; **no visible CEFR label** | Draft blends importance with being noticeable; choose exact sense and adjust example/Myanmar if needed |

**Source limitation:** Cambridge publisher-owned search-indexed excerpts were available, but direct publisher full-page requests returned **HTTP 403**. No source CEFR label was visible for these six entries. **Do not infer C1 from formal register, corpus usage, dictionary inclusion or the draft's existing C1 placement.** No publisher text was copied into final learner definitions. The observations are research leads, not human-independent English, Myanmar, example, pronunciation or CEFR verification.

## Fail-closed staging work

- [New source-provenance auditor](tools/audit_cefr_1000_unlabelled_c1_six.py) checks all six fixed headwords, exact provisional bilingual/example snapshots and historical provenance, Cambridge URL, date and search-index/403 caveat, and **null** CEFR source label. It defines **20 negative mutation cases** for invented CEFR labels, false reviewer approvals, source/snapshot drift, duplicate evidence and missing holds. These are **written tests, not claimed execution results** until actual CI logs are inspected.
- [Parallel A1/A2/B1/B2/C1/ALL structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) includes the new auditor per job and 20 negative cases in ALL. [Documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml) also includes the auditor.
- [Launch-readiness gate](tools/audit_cefr_1000_launch_readiness.py) now requires a separate **genuine independent human** direct-publisher **exact-sense C1** CEFR receipt and reviewed-content hash for each retained flagged word. An unlabelled Cambridge snippet cannot itself supply that proof. Unchanged definition/example combinations for `obfuscate` and `salience` are blocked pending sense alignment. A receipt schema cannot authenticate a person by itself; independent human provenance must be confirmed outside code.
- [Release evidence ledger](draft/CEFR-1000-RELEASE-EVIDENCE.json) adds `cambridge_unlabelled_c1_six_review_receipts: []` with **zero** invented reviews.

**GitHub execution evidence:** Previously verified structural run [40637802552](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40637802552) concluded success for all six jobs, and documentary run [40637802594](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40637802594) concluded success as report-only. **Both predate this new six-word audit and gate.** The GitHub connector's commit-run lookup exposes only PR-triggered runs; it returned no new push-run IDs for the new commits. **Actual new CI job conclusions/logs are UNVERIFIED.** Do not count the new 20 tests as passed or claim a release gate PASS until fresh runs are inspected.

## Exact progress and blockers

| Level | First-pass English/Myanmar/example written | Independently approved | Final both-voice real-listening completion |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

**Mandatory release blockers:** independent English, fluent Myanmar, original example and source-backed exact-sense CEFR human signoff for all 1,000; historical WordNet/named-entity/level conflicts and 120 shared IELTS headword decisions; final 200-per-level deduplicated approved manifest; generated George/Emma headword and example recordings with real human listening; full desktop/mobile regressions and physical iPhone Safari evidence; measured GitHub Pages hosting/site/audio budgets; final preservation verification for 54 lessons, separate IELTS bank, existing production George/Emma audio and privacy; confirmed production deployment. Official [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) are reference policy, not measured hosting evidence.

**No publication or completion notice.** Remain staging-only until all gates are genuinely evidenced and production is independently confirmed live.
