# CEFR 1000 — eighth C1 Oxford research + three directly opened sense leads (2026-10-30)

**STAGING ONLY. NO HUMAN INDEPENDENT APPROVAL. NO PRODUCTION DEPLOYMENT.**

Scope: the **user-approved 1,000 total**, 200 each at A1, A2, B1, B2 and C1. This is not the superseded 5,000-word plan. Research branch: `cefr-5000-bilingual-qa-staging`. Frozen shortlist Git blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Frozen shortlist and independent reviewer task flags remain unchanged.

## Direct Oxford publisher word/POS research

Source: [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf), directly opened and inspected **2026-10-30**. Page numbers below are 1-based; extracted text lines are 0-based. Exact excerpt, original English/Myanmar/example snapshot, historical source path/index/blob, reviewer task and hold flags are preserved in [the 12-record research packet](draft/CEFR-1000-OXFORD-C1-EIGHTH-TWELVE-2026-10-30.json).

| C1 provisional entry | POS | Oxford word/POS | PDF page, extracted line | Editorial priority |
|---|---|---|---|---|
| subsequently | adverb | B2 | 3, 604 | Lower publisher label; sequencing sense |
| privilege | noun | C1 | 6, 1619 | Special right versus other privilege senses |
| unity | noun | B2 | 3, 671 | Lower publisher label; solidarity sense |
| usage | noun | B2 | 3, 674 | Lower publisher label; linguistic usage sense |
| threshold | noun | C1 | 7, 1904 | Numeric trigger versus doorway; dictionary badge conflict |
| consecutive | adjective | C1 | 4, 966 | Uninterrupted succession |
| preliminary | adjective | C1 | 6, 1600 | Initial findings versus final assessment |
| backing | noun | C1 | 4, 815 | Practical/financial support, not physical backing |
| respective | adjective | C1 | 7, 1712 | Distributive each-person/each-department reference |
| scenario | noun | B2 | 3, 551 | Lower publisher label; planning scenario |
| trace | verb | B2 | 3, 649 | **Critical:** C1 noun `trace` on page 7 line 1920 cannot support draft verb |
| bias | noun | B2 | 1, 61 | Lower publisher label; unfair preference in hiring |

**New observations: 12 distinct C1-draft headwords, six Oxford B2 and six Oxford C1 word/POS labels.** The six B2 discrepancies are not automatic retiering decisions; independent reviewers must establish a defensible exact-sense rationale or revise/reselect the frozen release candidate through a separate approved process.

## Three directly opened Oxford dictionary exact-sense leads

The following source pages were directly opened **2026-10-30**. They are independent *publisher research observations*, **not independent human reviewer signoffs**.

1. **trace (verb)** — [Oxford dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/trace_1), lines 136–145, explicitly covers discovering the origin or cause of something; the draft's faulty-material origin example is aligned with that verb sense. The same page displays an Oxford 3000 **B2** badge (lines 232–236). Oxford 5000 separately lists `trace n.` at **C1**, but that noun entry cannot justify the provisional **C1 verb**. The [noun page](https://www.oxfordlearnersdictionaries.com/definition/english/trace_2), lines 88–91 and 205–209, itself displays a B2 word-list badge, an unresolved publisher-surface discrepancy with the 5000 PDF.
2. **scenario (noun)** — [Oxford dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/scenario), lines 107–125, confirms a description of how events might unfold in the future and shows collocations including *consider* and *construct* a scenario. The dictionary's B2 word-list badge (lines 161–165) matches the official PDF B2 word/POS. Draft `prepared a scenario for a supply shortage` merits a human grammar/collocation check; do not claim a C1 exact-sense label.
3. **threshold (noun)** — [Oxford dictionary](https://www.oxfordlearnersdictionaries.com/definition/english/threshold), lines 120–145, confirms a level at which an effect starts, with *reach*, *above*, *below* and *threshold value* collocations. The dictionary displays a B2 word-list badge (lines 172–176), **conflicting with the Oxford 5000 PDF C1 noun listing**. The doorway sense has C1 topic tags (lines 105–110), which do not establish that the draft's quantitative sense is C1. Preserve both sources for independent resolution.

### Unapproved bilingual/example alternatives for human consideration

These are **original editorial proposals only**, not changes to the frozen shortlist, not independently reviewed, and not evidence of CEFR level.

| Word | Proposed English example | Proposed Myanmar translation |
|---|---|---|
| scenario | The team considered a supply-shortage scenario before placing new orders. | အော်ဒါအသစ်များ မတင်မီ ပစ္စည်းပြတ်လပ်နိုင်သည့် အခြေအနေတစ်ရပ်ကို အဖွဲ့က ကြိုတင်စဉ်းစားခဲ့သည်။ |
| threshold | The alarm sounds when the temperature exceeds the safety threshold. | အပူချိန်သည် ဘေးကင်းရေးအတွက် သတ်မှတ်ထားသော အဆင့်ကို ကျော်လွန်သည့်အခါ သတိပေးစနစ် မြည်လာသည်။ |
| trace | Investigators traced the faulty material back to its supplier. | စုံစမ်းစစ်ဆေးသူများက အရည်အသွေးမပြည့်မီသော ပစ္စည်း၏ မူလပေးသွင်းသူကို ခြေရာခံရှာဖွေခဲ့သည်။ |

Independent reviewer must decide natural Myanmar wording, intended exact sense, example grammar, British pronunciation, and source-backed level before any content replacement or signoff.

## Provisional coverage reconciliation (requires fresh successful CI)

A1 **195/200**, A2 **96/200**, B1 **96/200**, B2 **94/200**, C1 **75/200** direct Oxford word/POS observations: **556/1,000 distinct**, **575 total source observations**, **444 without direct observations**. Human-review priorities: **3 unlisted**, **22 publisher-higher**, **183 publisher-lower**, **348 word/POS matches still exact-sense-unverified**, **444 without direct observation**.

First-pass written / independently checked: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real final George/Emma listening signoffs **0/1,000**. Complete final headword/example dual-voice audio, real listening, desktop/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting, preserved-production verification at launch and confirmed production deployment remain outstanding.

New [source-bound eighth C1 auditor](tools/audit_cefr_1000_oxford_c1_eighth_twelve.py) has **294 adversarial mutation cases** and is wired into six parallel structural CEFR lanes and the documentary no-deploy gate. CI results must be verified from actual job conclusions and logs; a successful report-only documentary job is never release authorisation.

**Release: BLOCKED / STAGING ONLY. Do not merge, modify main, publish, generate fake independent receipts or claim listening/device testing.**
