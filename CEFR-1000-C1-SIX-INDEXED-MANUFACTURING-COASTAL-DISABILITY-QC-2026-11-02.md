# CEFR 1,000 — six C1 Cambridge-indexed exact-sense leads (2 November 2026)

**Scope:** approved **1,000 total**, exactly 200 first-pass words at A1/A2/B1/B2/C1. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Status:** editorial hold; zero independent approvals; no deployment.

## Source-supported observations (publisher search-index only)

Cambridge Advanced Learner's Dictionary English headword results were observed on **2026-11-02**. Direct page opening returned **HTTP 403** for checked Cambridge entries. Search-index snippets are publisher-attributed research leads, **not** directly inspected pages or human independent CEFR verification.

| Frozen C1 word | Indexed Cambridge sense and level | Exact-sense question / provisional consequence |
| --- | --- | --- |
| [manufacturer](https://dictionary.cambridge.org/dictionary/english/manufacturer) (noun) | **B2**, large-scale goods-producing company | Frozen definition includes a *person*, broader than the labelled company sense; **C1 vs indexed B2** and noun-sense breadth need human review |
| [coastal](https://dictionary.cambridge.org/dictionary/english/coastal) (adjective) | **B2**, near/relating to coast | Frozen coastal-communities example matches B2 sense; **C1 vs indexed B2** |
| [disability](https://dictionary.cambridge.org/dictionary/english/disability) (noun) | **B2**, condition affecting activities | Frozen condition sense resembles indexed B2; **C1 vs indexed B2**; refine fluent and respectful Myanmar phrasing without overstating limitations |
| [permit](https://dictionary.cambridge.org/dictionary/english/permit) (noun) | **C1**, official permission document | **C1 alignment control**. Distinct from B1 transitive verb 'allow' and C1 intransitive verb 'make possible'. British noun /ˈpɜː.mɪt/ vs verb /pəˈmɪt/ creates **POS-specific real audio listening requirement** |
| [transaction](https://dictionary.cambridge.org/dictionary/english/transaction) (noun) | **C1**, buying/selling or money exchange | **C1 alignment control**. Distinguish bank transfer from a vague exchange of any services |
| [probability](https://dictionary.cambridge.org/dictionary/english/probability) (noun) | **C1**, degree of likelihood | **C1 alignment control**. Do not conflate with the separate C2 idiom *in all probability* or assume numerical statistics in every context |

All six source URLs, observation date, historical draft indices (**456, 457, 458, 569, 660, 729**), frozen English definitions, Myanmar glosses, original examples and unapproved rewritten teaching alternatives are preserved in [the six-card held research packet](draft/CEFR-1000-C1-SIX-CAMBRIDGE-MANUFACTURER-COASTAL-DISABILITY-2026-11-02.json). Frozen shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; original A2–C1 draft Git blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`; research packet Git blob `2a9a7e88025d2c6d50e103ed5383474995730bf7`.

## Structural safeguards and review handoff

The [fail-closed research auditor](tools/audit_cefr_1000_c1_six_cambridge_manufacturing_coast.py) checks exact 200-per-level quotas, 1,000 casefold-unique headwords, zero review approvals, historical source index and bilingual equivalence, publisher domain, dated index-only access, word/POS-specific badges, original examples and held alternatives. It includes **94 programmed synthetic adversarial mutations** (14 per card, plus 10 global) that are mechanical forgery tests, not linguistic review. Six parallel A1/A2/B1/B2/C1/ALL structural QA lanes and the documentary no-deployment gate invoke the auditor. Actual GitHub Actions conclusions and logs must be checked before claiming a pass.

Human-independent reviewers must adjudicate all three B2-vs-C1 conflicts and all three controls for exact meaning, CEFR, grammar, fluent Myanmar, and natural examples. George/Emma British pronunciation must be generated and **actually listened to**, particularly noun `permit`. No flags have been changed.

| CEFR level | First-pass written | Independently checked/approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Release remains blocked.** Final independently approved manifest, complete George/Emma headword and example recordings with listening receipts, browser/mobile regressions, real physical iPhone Safari review, measured GitHub Pages hosting limits, protected 54 lessons and separate IELTS 1,000-word bank and production audio/privacy verification, and confirmed production deployment are all missing. No merge, main edit or publication.
