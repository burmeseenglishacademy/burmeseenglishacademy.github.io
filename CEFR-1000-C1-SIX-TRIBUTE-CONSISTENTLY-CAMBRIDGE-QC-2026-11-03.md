# BEA CEFR 1000 — C1 six-word Cambridge sense checkpoint (3 November 2026)

**Staging only; no release or independent signoff.** This work concerns the user-approved **1,000 total words**, not the obsolete 5,000-word plan. The branch name `cefr-5000-bilingual-qa-staging` is retained intentionally.

## Evidence and exact-sense outcomes

| Frozen C1 word | Cambridge Advanced Learner's Dictionary badge | Editorial interpretation |
|---|---|---|
| tribute (respectful-action noun) | **C2** | Same-sense C1/C2 conflict; frozen concert example is a respectful tribute, not historical payment |
| trigger (transitive verb, cause to start) | **C1** | Matching C1 research lead; do not confuse with gun-part noun or trauma-related use |
| racism (uncountable noun, race-based unfair treatment) | **B2** | Same-sense C1/B2 conflict; distinguish systemic discrimination from belief-based conduct |
| signature (countable noun, handwritten name) | **B1** | Same-sense C1/B1 conflict; not the technical characteristic or adjectival sense |
| abortion (intentional ending of pregnancy, countable/uncountable noun) | **C1** | Matching C1 research lead; distinguish from medically specialised spontaneous abortion |
| consistently (adverb, without change over time) | **C2** | Same-sense C1/C2 conflict; frozen quality-target example fits this meaning |

Publisher pages inspected through search-engine crawled text on **2026-11-03**: [tribute](https://dictionary.cambridge.org/us/dictionary/english/tribute), [trigger](https://dictionary.cambridge.org/dictionary/english/trigger), [racism](https://dictionary.cambridge.org/dictionary/english/racism), [signature](https://dictionary.cambridge.org/us/dictionary/english/signature), [abortion](https://dictionary.cambridge.org/dictionary/english/abortion), [consistently](https://dictionary.cambridge.org/dictionary/english/consistently). The labels were observed in publisher-owned page excerpts, **not signed off by an independent human reviewer**. No inference from unrelated senses or word families was accepted.

## Bilingual review handoff

[Source-bound JSON packet](draft/CEFR-1000-C1-SIX-TRIBUTE-CONSISTENTLY-CAMBRIDGE-SENSE-2026-11-03.json) contains six exact frozen English definitions, original Myanmar glosses and examples, historical source paths and indexes **31, 32, 71, 75, 78, 110**, publisher URLs, observation dates, British IPA references, separate **unapproved** Myanmar gloss proposals and original example candidates. The reviewer must confirm grammar, exact sense, pronunciation, natural Burmese, and whether to replace or relevel each conflict while preserving all 200 slots per level. No existing shortlist word, CEFR label, example, or approval field was changed.

## Mechanical QA and remaining gates

[Fail-closed auditor](tools/audit_cefr_1000_c1_six_tribute_consistently.py) pins Git blob SHA for the packet `1a4b91e0239045309119e74dea478f1951f9ccb9`, frozen shortlist `475e68ae17ab97bd937e73e5ce4794e0dcd76551` and historical source `b04dd85db5cfae131c25aa4c73109778991b6fdc`. It checks six source-bound cards, global uniqueness, 200 provisional entries in each of five levels, zero approval flags, honest publisher provenance, and synthetic forgery rejection for reviewer, CEFR, George/Emma listening, iPhone and release claims. **83 synthetic mutations are programmed; their GitHub Actions execution is not yet verified.**

Both staging-only workflows were updated: `.github/workflows/cefr-1000-selection-structural-qa.yml` (six parallel A1/A2/B1/B2/C1/ALL lanes) and `.github/workflows/cefr-1000-go-live-qc-gate.yml` (documentary no-deployment gate). Workflow commits: `677e59cafc2f956b7d93a36b712e1876b54b852e` and `5e097ddc3718fc947d8bc5291897e2bfbf8cbf8b`. GitHub readback verified both workflow insertions and zero mismatches in the six frozen/historical records. Comparison from prior checkpoint `64baf4e5e61d60feddd5928b6f0d2472023a6637` to `5e097ddc3718fc947d8bc5291897e2bfbf8cbf8b` found **4 commits and only 4 staging research/auditor/workflow paths changed**. No protected production paths changed.

Previous actual GitHub Actions [structural run 41535606132](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41535606132) had A1/A2/B1/B2/C1/ALL jobs SUCCESS; ALL job `125586533625` logs showed **168/168 earlier synthetic mutations rejected**. Previous [documentary run 41535606131](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41535606131) job `125586532410` SUCCESS with explicit release blockers and unchanged protected assets. **These runs predate this six-card auditor. New push-triggered run IDs, final job conclusions and logs were not retrievable via the available commit-run lookup (which returned no PR-associated runs). Do not claim new CI passed.**

| CEFR | First-pass written | Independently checked and approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**RELEASE BLOCKED / STAGING ONLY.** Required before public launch: genuine independent English/Myanmar/example/source-backed CEFR review and 200 deduplicated approved slots per level; complete British George/Emma headword and example audio with actual listening receipts; desktop/mobile browser regressions; physical iPhone Safari and British audio testing; measured GitHub Pages hosting clearance; confirmed production deployment and preserved 54 lessons, separate IELTS bank, existing audio and privacy. Nothing was merged, published or marked approved.
