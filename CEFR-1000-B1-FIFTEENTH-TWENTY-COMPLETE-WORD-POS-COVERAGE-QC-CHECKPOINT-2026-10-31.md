# CEFR 1,000 — B1 fifteenth Oxford source batch, 20 word/POS observations and four direct dictionary senses

**Observed:** 31 October 2026. **Branch:** `cefr-5000-bilingual-qa-staging`. **Release status:** BLOCKED / STAGING ONLY. **Target:** 1,000 total, exactly 200 draft words in each A1, A2, B1, B2 and C1. The old 5,000-word scope is superseded.

## Publisher research (not independent CEFR approval)

Directly inspected Oxford University Press's official [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on 2026-10-31. The final 20 previously unobserved **provisional B1** headwords/POS now have publisher word/POS observations. PDF page and extracted-line locators, publisher excerpts, observation dates, original English/Myanmar/example snapshots and historical Git source paths, indexes and blob SHAs are in [the frozen 20-record packet](draft/CEFR-1000-OXFORD-B1-FIFTEENTH-TWENTY-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json). **None of these publisher word/POS levels establishes the draft's intended exact-sense CEFR.**

| Publisher word/POS level | Words | Count |
|---|---|---:|
| A1 | adult, artist | 2 |
| A2 | hill, metal, profile, pull, push, seat, memory, ring (ring1 noun), rise, silver, prison, produce | 12 |
| B1 | spread | 1 |
| B2 | fund, edition, apparently, handle, leadership | 5 |

**19/20** provisional B1 classifications differ from the Oxford word/POS label; the matching `spread` remains exact-sense-unverified. Special ambiguity: `ring1` jewellery noun is distinct from `ring2` verb; `adult` noun is A1 but the adjective is separately A2; `produce` verb is not the noun; `handle` verb is not a door-handle noun; `memory` remembered event is not general memory ability or computer memory. Do not retier mechanically without independent intended-sense review.

Four **directly inspected Oxford dictionary sense leads**, all **unapproved**, with original Myanmar/example proposals in the packet:

- [fund, noun sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/fund_1), page-text lines 105–112: a countable purpose-specific pool of money; distinguish plural available `funds` and investment firm.
- [memory, noun sense 3](https://www.oxfordlearnersdictionaries.com/definition/english/memory), lines 170–182: a countable recollection; distinguish ability to remember and computer storage.
- [handle, verb sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/handle_1), lines 110–125: transitive dealing with a situation; distinguish physical handling and noun.
- [leadership, noun sense 2](https://www.oxfordlearnersdictionaries.com/definition/english/leadership), lines 151–173: uncountable leadership ability/qualities; distinguish a position and the leaders as a group.

The dictionary's topic badges and unrelated site-wide Word of the Day footer must **not** be presented as publisher exact-sense CEFR evidence. English grammar, Myanmar fluency and examples still need independent human editorial review. All original shortlist entries retain `editorial_hold=true`, all reviewed/approved flags false and no independent receipt.

## Fail-closed controls

[Source/provenance auditor](tools/audit_cefr_1000_oxford_b1_fifteenth_twenty.py) pins the shortlist and source-packet Git blob SHAs; verifies exact word/POS/PDF URL/page/line/excerpt, historical source path/index/blob, English/Myanmar/example snapshots, the four dictionary sense URLs and locators, and zero independent review. It runs **221 adversarial mutations** for forged publisher levels, lines, bilingual text, source history, reviewer receipts and premature promotion. Integrated into the six parallel A1/A2/B1/B2/C1/ALL structural QA lanes and documentary no-deployment QC.

An intermediate CI failure exposed a real pre-existing negative-test assumption: the reviewer handoff integrity test attempted to forge a missing-source row in B1 even though **all 200 B1 entries now have direct Oxford observations**. Repaired the self-test to skip missing-source mutations only when that level's audited direct observation count is exactly 200; other levels continue to test missing-source forgery. Reconciled the cross-batch source auditor and source-bound reviewer handoff, including the stale hardcoded 784/216 counts.

**CI evidence:** [documentary no-deploy run 41166094830](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41166094830), code SHA `0ff503ac93df812c12a5c2f2402a5d17bb0a9532`, **SUCCESS**; actual job log confirms **221/221** new forged-evidence mutations rejected, release still blocked and protected production paths unchanged. [Structural run 41166161978](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41166161978) and [documentary run 41166161921](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41166161921) were queued/in progress when this checkpoint was drafted; their final conclusions must be checked, not assumed.

## Truthful totals after this research

| Level | First-pass written | Direct Oxford word/POS observed | Human-independent approved |
|---|---:|---:|---:|
| A1 | 200 | 195 | 0 |
| A2 | 200 | 156 | 0 |
| B1 | 200 | **200** | 0 |
| B2 | 200 | 166 | 0 |
| C1 | 200 | 111 | 0 |
| **Total** | **1,000** | **828** | **0** |

**847** direct Oxford packet observations covering **828** distinct words; **172** have no direct Oxford observation. Human queue: **3** not listed in inspected Oxford core lists (not a CEFR level), **52** publisher-higher, **324** publisher-lower, **449** matching word/POS but intended sense unverified, and **172** without direct observation. These five groups total 1,000. Real final George/Emma listening signoffs: **0/1,000**.

**Essential release gates still missing:** independently signed English, fluent Myanmar, original example, exact-sense source-backed CEFR and British pronunciation review for every item; exactly 200 independently approved deduplicated headword/senses per level; final British George/Emma headword and example audio generation and **real human listening**; approved-corpus browser/mobile regression; physical iPhone Safari evidence; measured GitHub Pages hosting constraints; confirmed production deployment and preservation of 54 lessons, separate IELTS 1,000 bank, established George/Emma production audio and privacy. No merge, no main modification and no public launch are authorized before every gate passes.
