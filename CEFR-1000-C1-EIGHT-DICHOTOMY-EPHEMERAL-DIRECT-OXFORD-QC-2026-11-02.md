# CEFR 1000 C1 eight direct Oxford exact-sense research — 2 November 2026

**Scope:** Approved 1,000 TOTAL CEFR words, A1/A2/B1/B2/C1 = 200 each; existing branch `cefr-5000-bilingual-qa-staging` only. **Research is unapproved.** Frozen shortlist and independent-review tasks are unchanged; no human signoff is asserted.

## Direct publisher observations and editorial questions

All eight **Oxford Advanced Learner's Dictionary English headword pages** were opened directly on **2026-11-02**. Their source URL, observed lines, British IPA, frozen English/Myanmar/example, original source file/index/blob SHA and a clearly unapproved proposed alternative are recorded in [the eight-card research packet](draft/CEFR-1000-C1-EIGHT-DIRECT-OXFORD-DICHOTOMY-EPHEMERAL-SENSE-TRIAGE-2026-11-02.json).

| Frozen C1 word | Oxford page and observed lines | Exact-sense risk for independent reviewer |
|---|---|---|
| **dichotomy** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/dichotomy), 101–107 | Usually singular, formal, **two sharply opposed** groups; growth versus conservation could imply a false exhaustive choice |
| **disseminate** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/disseminate), 101–116 | Formal **transitive** spreading of information/knowledge; distinguish from physically distributing goods |
| **eclectic** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/eclectic), 101–113 | A **selection or mixture from varied styles/ideas**, not merely a large collection |
| **efficacy** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/efficacy), 93–109 | **Uncountable**, outcome effectiveness rather than resource efficiency; OPAL W is not a CEFR badge |
| **embellish** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/embellish), 101–117 | Oxford has **decoration** and **potentially untrue story detail** senses; frozen definition combines them, example teaches story |
| **endemic** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/endemic), 101–112 | **Disease persistently present in an area** versus **species endemic to an area** (restricted distribution); frozen example is disease |
| **enigma** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/enigma), 101–109 | Mysterious person/thing/situation, not merely any hard task |
| **ephemeral** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/ephemeral), 101–108 | **Short-lived** or briefly used, not necessarily fragile/disposable; frozen ice sculpture is plausible |

**Publisher evidence boundary:** No exact-sense **C1 CEFR classification** was observed on these Oxford pages. The unrelated Oxford footer's topic/Word-of-the-Day CEFR labels must not be attributed to these headwords. Direct Cambridge English headword requests returned **HTTP 403** on 2026-11-02; Cambridge CEFR ratings are **not** claimed. The eight pages support dictionary POS/sense/collocation/pronunciation research only, not a human-independent CEFR decision.

**Review handoff:** A genuinely independent reviewer must separately assess each word's exact sense and C1 level with a suitable source, English definition, fluent Myanmar meaning, original example grammar and naturalness, and British pronunciation. In particular, request explicit choices on the merged `embellish` senses, `endemic in` versus `endemic to`, `efficacy` versus `efficiency`, and the potential false dichotomy. None of the suggested rewrites is approved. No new George/Emma recordings or actual listening tests were performed.

## Staging-only mechanical controls

Added [a source-bound auditor](tools/audit_cefr_1000_c1_eight_dichotomy_ephemeral.py) that pins the eight-card research Git blob `54935a003fec14108490a91f17253c5018a88714` and frozen shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; checks exactly 200 deduplicated held headwords per level; compares the eight original bilingual/example/POS/source-provenance fields; requires canonical Oxford URLs, observation dates, line locators, British IPA and truthful absence of CEFR badges; and rejects forged independent reviewer, listening, iPhone and deployment claims. The auditor includes **236 programmed synthetic adversarial mutations**; actual CI conclusions and logs must be checked before claiming their pass.

Wired the auditor into six parallel A1/A2/B1/B2/C1/ALL structural lanes, with synthetic mutation self-test in ALL, and into documentary **no-deployment** QC. This is a research-integrity check, **not** independent human approval.

## Release status

| CEFR | First-pass written | Independently checked and approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Still blocked:** independently approved English/Myanmar/examples/exact-sense CEFR, approved release manifest, final British George/Emma headword+example audio and real listening receipts, browser/mobile regression, physical iPhone Safari review, measured GitHub Pages hosting readiness, confirmed production deployment and protected production asset readback. **STAGING ONLY; no merge, main edit or publication.**
