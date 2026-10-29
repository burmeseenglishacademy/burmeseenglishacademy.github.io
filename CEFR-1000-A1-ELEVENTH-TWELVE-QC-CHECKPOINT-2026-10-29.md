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
