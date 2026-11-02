# BEA CEFR-1000: eight held B1 foundational senses — publisher-indexed conflict QC

**Observed:** 2026-11-02 (Singapore). **Branch:** `cefr-5000-bilingual-qa-staging` only. **Scope:** user-approved 1,000 TOTAL (A1/A2/B1/B2/C1 = 200 each), NOT the superseded 5,000-word plan. **Status:** editorial research, NOT independent human review, NOT release.

## Source-access evidence and important limitations

Cambridge Dictionary publisher search results were readable on 2026-11-02. Subsequent direct `open` attempts for all eight publisher pages returned **HTTP 403**. These are **publisher-indexed exact-sense leads**, not independently confirmed direct publisher-page observations. Source links, observed date and frozen shortlist provenance are retained in the [eight-card research packet](draft/CEFR-1000-B1-EIGHT-FOUNDATIONAL-CAMBRIDGE-INDEXED-SENSE-TRIAGE-2026-11-02.json). Do not claim that an AI search-index observation is independent editorial approval. No Oxford word-list membership or WordNet first sense can substitute for exact-sense CEFR review.

| Frozen B1 entry | Cambridge indexed same-sense level | Triage and concrete risk |
|---|---|---|
| **independent**, adjective | **B2** NOT INFLUENCED | Frozen not-controlled sense aligns with B2; Cambridge B1 NOT HELPED/financial independence is a different sense. [Cambridge](https://dictionary.cambridge.org/dictionary/english/independent) |
| **weekend**, noun | **A1** | Saturday/Sunday sense is A1. Original `at the weekend` is natural British English, but its grammatical correctness does not justify B1 placement. [Cambridge](https://dictionary.cambridge.org/dictionary/english/weekend) |
| **cash**, noun | **A2** COINS | Notes-and-coins definition aligns with A2, whereas B1 MONEY is a broader distinct sense; noun is uncountable. [Cambridge Learner's](https://dictionary.cambridge.org/dictionary/learner-english/cash) |
| **effort**, noun | **B1** | Positive alignment control for physical/mental energy. C2 `be an effort` is a different idiom; no approval inferred. [Cambridge](https://dictionary.cambridge.org/dictionary/english/effort) |
| **civil**, adjective | **C1** ORDINARY | Ordinary citizens versus military/religious is indexed C1; frozen `civil rights` example does not unambiguously demonstrate that contrast. Legal civil is another sense. [Cambridge](https://dictionary.cambridge.org/dictionary/english/civil) |
| **ship**, noun | **A2** BOAT | Sea-going vessel is A2; unrelated shipping verb and fan relationship meanings cannot justify B1. [Cambridge](https://dictionary.cambridge.org/dictionary/english/ship) |
| **operation**, noun | **C1** WORK | Frozen warehouse-running sense is C1 work/business operation, not the B1 medical-operation noun. Countability and collocations need checking. [Cambridge](https://dictionary.cambridge.org/dictionary/english/operation) |
| **analysis**, noun | **B2** | Detailed-examination noun is indexed B2; plural `analyses` needs separate audio attention. [Cambridge](https://dictionary.cambridge.org/dictionary/english/analysis) |

**Result:** 7 potential exact-sense B1 level conflicts; 1 indexed B1 alignment. These are research priorities, not automatic retiering instructions. Each card preserves the original English definition, Myanmar meaning, example, historical source path/index/blob, dated publisher URL and a separate **unapproved** original English/Myanmar/example alternative. For example, the original `civil rights` sentence is quarantined for exact-sense mismatch review; the alternative uses `civil authorities`. No original content has been replaced.

## Mechanical release protection

The new [fail-closed packet auditor](tools/audit_cefr_1000_b1_eight_foundational_indexed.py) binds each card to the frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, checks all five level quotas and 1,000 unique headwords, requires all editorial and release flags to remain held, and rejects fabricated source-access, CEFR, reviewer, George/Emma listening, physical iPhone or production claims. It also provides synthetic mutation tests. Its integration is staged in both the six-lane parallel structural workflow and documentary no-deployment gate. **A test success proves structural integrity only, not human linguistic verification.**

## Exact stage counts and unresolved release gates

| CEFR | First-pass written | Independently approved | Both voices really listened | Released |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 0 | 0 |
| A2 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 0 | 0 |
| C1 | 200 | 0 | 0 | 0 |

**BLOCKED:** independent English, fluent Myanmar, grammar and source-backed exact-sense CEFR review for every entry; approved 1,000-word release manifest; all British George/Emma headword and example recordings and **actual individual listening** receipts; browser/mobile regression; **physical iPhone Safari** evidence; measured GitHub Pages site size/bandwidth/deploy limits; protected 54 lessons, separate IELTS 1,000 bank, existing audio and privacy; confirmed production release. No main merge, publication, production modification, iPhone test or human signoff has occurred.

**CI verification:** The actual post-repair runs and job logs are recorded below. No structural test is an independent linguistic or listening review.


## Actual CI recovery and verified evidence — 2026-11-02

The first new structural run [41428288787](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41428288787) and documentary run [41428294566](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41428294566) failed because the auditor demanded an explicit `not independent` source caveat while the initial packet said `not direct ... or independent review`. The source evidence itself did not change; the repair made both HTTP 403 and **not independent human review** explicit. The staging-only repair commit was `6b2fdc52ab0b721a6ec2b0a9283c1adad148526d`.

**Post-repair confirmed GitHub Actions at that SHA:**

- [Structural run 41428395120](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41428395120): all six actual jobs **A1/A2/B1/B2/C1/ALL SUCCESS**. ALL job `125220519687` logs confirmed **234/234 synthetic adversarial mutations rejected**, 1,000 held, 0 independently approved and no production drift. ALL artifact `13133695417`.
- [Documentary no-deployment run 41428395138](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41428395138): job `125220519927` **SUCCESS**, confirming **234/234 mock mutations rejected**, unchanged protected production assets and explicit missing real independent word reviews (0/1,000), approved manifest, George/Emma listening, desktop/mobile regressions, physical iPhone Safari, hosting and final release evidence. Blocker artifact `13132279580`.

A workflow's successful **documentary/report-only** check is not permission to release; it confirms the release remains **BLOCKED**. Comparison against the prior staging checkpoint `cd61cca29e3e3dbf32059e84469fd8d6f584d67f` showed eight commits affecting only six staging research, auditor, workflow and documentation paths, with no protected production changes.
