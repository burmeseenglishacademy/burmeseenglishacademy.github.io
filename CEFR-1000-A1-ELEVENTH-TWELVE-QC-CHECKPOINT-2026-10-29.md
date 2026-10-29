# CEFR 1,000 — A1 eleventh twelve direct Oxford noun observations (staging only)

**Observed:** 2026-10-29. **Branch:** `cefr-5000-bilingual-qa-staging`. **Approved scope:** exactly 1,000 first-pass entries (A1/A2/B1/B2/C1: 200 each), not the abandoned 5,000-word plan. **Release: BLOCKED / STAGING ONLY.**

## Publisher evidence, not independent exact-sense signoff

Directly inspected [Oxford University Press, *The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-29**. The 12 following *new* A1 draft words appear in the A1 portion of the PDF as nouns. The locators are **one-based PDF pages / zero-based extracted web lines**, and are preserved with the short original word/POS excerpt, source URL/date, exact draft English/Myanmar/example snapshots, and original Git source path/index/blob in [the research packet](draft/CEFR-1000-OXFORD-A1-ELEVENTH-TWELVE-2026-10-29.json).

| Draft word | PDF page / line | Exact short Oxford word/POS excerpt | Independent reviewer focus |
|---|---:|---|---|
| key | 2 / 418 | `key n., adj.` | Physical lock key versus adjective, musical key and other senses |
| shirt | 3 / 688 | `shirt n.` | Shirt versus T-shirt; natural Myanmar garment name |
| shoe | 3 / 689 | `shoe n.` | Singular shoe versus pair; original example grammar |
| bed | 1 / 72 | `bed n.` | Bed versus mattress/bedding in Myanmar |
| room | 3 / 658 | `room n.` | Enclosed room versus available space |
| kitchen | 2 / 421 | `kitchen n.` | Natural Myanmar term for food-preparation room |
| bathroom | 1 / 65 | `bathroom n.` | British bathroom/toilet usage and draft definition |
| clock | 1 / 154 | `clock n.` | Clock versus watch |
| desk | 1 / 203 | `desk n.` | Study/work desk versus general table |
| head | 2 / 356 | `head n.` | Anatomical sense versus figurative leader/top |
| hand | 2 / 347 | `hand n.` | Hand versus arm; plural hands in example |
| eye | 2 / 263 | `eye n.` | Anatomical eye versus metaphorical uses; plural eyes |

The publisher PDF is **word/POS/level evidence only**. It does not independently certify the *exact intended sense*, fluent Myanmar translation, example correctness or a human review. No first-pass definitions, Myanmar meanings or examples were silently rewritten. All 12 remain on editorial hold, without any reviewer receipts.

## Source-integrity safeguards and verification limits

Added [the eleventh A1 fail-closed auditor](tools/audit_cefr_1000_oxford_a1_eleventh_twelve.py) with deterministic frozen-shortlist reconstruction and 238 adversarial forged-evidence mutations. Integrated it into the six parallel A1/A2/B1/B2/C1/ALL structural workflow lanes, including ALL-lane self-tests, and the documentary no-deployment workflow. Reconciled cross-batch Oxford source coverage and full reviewer handoff priority counts. **GitHub Actions run IDs, actual job conclusions and logs for this new commit were not accessible through the available commit-run lookup**; therefore CI completion or success is **not asserted**. Static connector read-back confirmed packet schema, twelve publisher locators, audit/workflow references and absence of protected production-file changes. Final workflow code commit: [`cf5c0bf5284b31d6506d90dbda6051ecb1b891c5`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/cf5c0bf5284b31d6506d90dbda6051ecb1b891c5).

| Level | First-pass written | Distinct direct Oxford word/POS observed | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 160 | 0 |
| A2 | 200 | 72 | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **437** | **0** |

There are **456 Oxford observations** covering **437 distinct** provisional headwords (19 repeated observations); **563** remain without direct Oxford word/POS observations. The review queue is **152 publisher-lower, 13 publisher-higher, three unlisted, 269 word/POS matches requiring exact-sense review and 563 without direct observations**. No Oxford word/POS match is a human-independent approval.

**Outstanding mandatory gates:** all 1,000 independently signed English/Myanmar/example/exact-sense CEFR reviews, approved release manifest and 200 unique headwords/senses per level, complete final British George/Emma headword+example audio and **0/1,000 real listening signoffs**, approved-corpus desktop/mobile regression, physical iPhone Safari review evidence, measured GitHub Pages limits, preserved production asset verification and confirmed live production deployment. No merge, main modification or publication. **BLOCKED / STAGING ONLY.**

## Additional Cambridge exact-sense leads (indexed source, not direct-page verification)

On **2026-10-29**, Cambridge Dictionary's publisher-owned search results exposed **A1-labelled specific senses** for three of these entries, but attempts to open each full publisher page returned **HTTP 403**. Accordingly, these are **source-indexed editorial leads only**, not completed direct-page verification or independent signoff. The immutable Oxford packet above retains each original English/Myanmar/example and historical Git provenance.

- **key** — [Cambridge English dictionary](https://dictionary.cambridge.org/dictionary/english/key): **A1 noun, LOCK sense**, consistent with the draft's physical lock-opening object. Cambridge separately labels the keyboard/musical-instrument **PART** sense B2 and the important/central adjective B2. Independent reviewer must preserve the lock-specific noun meaning and not infer that all senses of *key* are A1.
- **desk** — [Cambridge English dictionary](https://dictionary.cambridge.org/dictionary/english/desk): **A1 noun, TABLE sense**, a work/study table. Service-counter and newsroom uses are separate senses; draft example `My books are on the desk.` fits the work/study sense, pending human review.
- **bathroom** — [Cambridge English dictionary](https://dictionary.cambridge.org/dictionary/english/bathroom): **A1 noun**, a room with a bath and/or shower, often a toilet. The publisher separately notes US *bathroom* for a toilet-only room versus UK *toilet*. Draft Myanmar `ရေချိုးခန်း၊ အိမ်သာပါသောအခန်း` and English definition should be reviewed for a clear British-English learner sense; **no automatic correction was applied**.

All three Cambridge search-indexed observations retain the original publisher URLs and date here. Their evidence scope is `PUBLISHER_SEARCH_INDEX_ONLY_FULL_PAGE_HTTP_403_NOT_INDEPENDENT_REVIEW`; they do not change the 437 distinct Oxford word/POS count or the zero independently approved count.
