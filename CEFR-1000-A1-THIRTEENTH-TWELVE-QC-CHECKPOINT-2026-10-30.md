# CEFR 1000 A1 thirteenth direct Oxford research — 30 October 2026

**STAGING ONLY — no approval or deployment.** User-approved scope is 1,000 words total (A1/A2/B1/B2/C1 = 200 each). The branch name remains `cefr-5000-bilingual-qa-staging` and the original provisional shortlist and independent-review tasks remain unchanged.

## New directly observed publisher evidence

On 2026-10-30 the [official Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) was inspected. The 12 new A1 word/POS observations below have one-based PDF pages and zero-based web-extracted lines. They **do not independently establish exact-sense CEFR, English/Myanmar quality, example correctness or signoff**.

| Draft word | POS | PDF page | Extracted line | Oxford excerpt | Human editorial focus |
|---|---|---:|---:|---|---|
| rice | noun | 3 | 652 | `rice n.` | Draft Myanmar ဆန်၊ ထမင်း spans uncooked grain and cooked rice; example refers to cooked rice at lunch. Require exact-sense bilingual decision. |
| bread | noun | 1 | 106 | `bread n.` | Bread is usually an uncountable mass noun in general food use; do not automatically use a bread for a loaf. |
| egg | noun | 1 | 235 | `egg n.` | Draft definition treats egg as food, while the noun also denotes an animal's egg; countable an egg example is grammatical. |
| milk | noun | 2 | 483 | `milk n.` | Milk is normally uncountable as a substance; distinguish dairy milk from plant-based milk and servings. |
| chicken | noun | 1 | 144 | `chicken n.` | Example uses a living farm bird, not chicken meat; Myanmar ကြက် does not distinguish these senses alone. |
| banana | noun | 1 | 60 | `banana n.` | Banana is countable in example; distinguish fruit from plant and check description of ripeness. |
| potato | noun | 3 | 613 | `potato n.` | The potato is hot describes a cooked or heated potato; distinguish food from plant and botanical terminology. |
| soup | noun | 3 | 724 | `soup n.` | Soup in example is usually a mass noun; ဟင်းချို versus စွပ်ပြုတ် depends on recipe and Myanmar usage. |
| walk | verb | 4 | 855 | `walk v., n.` | Oxford A1 lists both verb and noun; draft targets verb move on foot. Example We walk to school is grammatical; avoid noun or figurative senses. |
| run | verb | 3 | 661 | `run v.` | Draft refers to running on foot, not operating a business/machine, flowing liquid, or racing an event. |
| sit | verb | 3 | 701 | `sit v.` | Example Please sit here is grammatical; distinguish sitting from taking an examination or being located. |
| stand | verb | 3 | 734 | `stand v.` | Draft targets upright posture, not tolerate, remain valid, or support a position; Myanmar မတ်တတ်ရပ်သည် is physical sense. |

All 12 records retain original English definition, Myanmar meaning, original example, historical source file/index/blob SHA, Oxford URL/date/page/line and a separate independent human reviewer task. See `draft/CEFR-1000-OXFORD-A1-THIRTEENTH-TWELVE-2026-10-30.json`. The `rabbit` A1 draft word is **not classified** by this observation: the inspected Oxford 3000 PDF search did not locate a rabbit noun entry; absence from one publisher core list does not establish a CEFR level or invalidate a word.

## Structural safeguards and exact counts

The source-bound auditor `tools/audit_cefr_1000_oxford_a1_thirteenth_twelve.py` reconstructs this packet from the frozen shortlist and hardcoded directly observed PDF anchors; it rejects count-preserving tampering, invented independent review receipts, changed Myanmar/examples and publisher locator drift. The 238 adversarial mutations are test cases, not human approvals. Six parallel A1/A2/B1/B2/C1/ALL structural lanes and the documentary no-deployment gate have been updated. Actual CI conclusions must be recorded only after runs finish.

Expected Oxford word/POS coverage after the packet: **A1 184/200, A2 84/200, B1 84/200, B2 70/200, C1 51/200; 473/1,000 distinct**, 492 total observations. Unobserved: 527. Review queue expected: 3 unlisted, 15 publisher-higher, 157 publisher-lower, 298 word/POS matches still exact-sense-unverified, 527 without direct observations. The 1,000 first-pass entries remain **200 written / 0 independently approved per level**. George/Emma final listening signoffs **0/1,000**.

**Blocking release gates:** genuine independent bilingual/example/exact-sense/CEFR review, final George and Emma headword/example audio plus real listening signoff, desktop/mobile browser regression, physical iPhone Safari evidence, measured GitHub Pages limits, protected production asset verification and confirmed live production deployment. No merge or publication permitted.

## Direct Oxford dictionary sense research — additional evidence, not signoff

On **2026-10-30**, four official Oxford Advanced Learner's Dictionary pages were directly inspected and recorded in [the separate four-sense source packet](draft/CEFR-1000-OXFORD-A1-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json). Each preserves frozen draft English/Myanmar/example content, historical source path/index/blob SHA, official URL, date, zero-based extracted lines and a human review task:

- [rice](https://www.oxfordlearnersdictionaries.com/definition/english/rice), lines 103–118: uncountable food/grain/plant usage; original example means cooked rice, while Myanmar draft includes both ဆန် (uncooked rice) and ထမင်း (cooked rice).
- [chicken](https://www.oxfordlearnersdictionaries.com/definition/english/chicken_1), lines 107–161: countable live bird versus uncountable meat. The draft garden example refers to a living bird.
- [bread](https://www.oxfordlearnersdictionaries.com/definition/english/bread), lines 103–114: common food sense is uncountable; a loaf/slice/piece of bread are appropriate quantity expressions.
- [walk](https://www.oxfordlearnersdictionaries.com/definition/english/walk_1), lines 103–141: first verb sense covers moving on foot without running, with a school-walking example compatible with the draft.

**Important rabbit risk:** the A1 provisional `rabbit` noun was not found in the inspected [Oxford 3000 PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) or [Oxford 5000 supplement](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) by text search on 2026-10-30. Oxford's [rabbit noun dictionary entry](https://www.oxfordlearnersdictionaries.com/definition/english/rabbit_1), lines 105–133, distinguishes countable animal from uncountable meat and shows *Animals a2* and *Food a2* **topic labels**. These topic labels are **not automatically a CEFR rating of the exact draft sense**; independent reviewer must resolve provisional A1 placement, source-backed exact-sense teaching rationale and Myanmar/example before any approval. This rabbit research does **not** add an Oxford core-list word/POS observation or alter the frozen shortlist.

## Verified GitHub Actions evidence and corrections

- Initial thirteenth-batch CI [structural 40931442255](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931442255) and [documentary 40931442421](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931442421) **FAILED**: new auditor incorrectly referenced the previous twelfth packet. Fixed in commit `eb9c9f0281ab536e138831064576d4d26d85188d`; subsequent [structural 40931611164](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931611164) and [documentary 40931611139](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931611139) **SUCCEEDED**.
- Four-sense evidence auditor initially used an incorrectly escaped Git-blob delimiter; corrected in commit `80e90b53820a78412818f7dfea803a4e2021d2d9`. The intermediate [documentary 40931790822](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931790822) **FAILED** and was not treated as a pass.
- **Final verified code SHA:** `80e90b53820a78412818f7dfea803a4e2021d2d9`. [Structural run 40931824963](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931824963): **SUCCESS for all six A1/A2/B1/B2/C1/ALL jobs**. ALL-job logs confirm **238/238** thirteenth word/POS tamper mutations, **68/68** four-sense tamper mutations and **145/145** full reviewer-handoff mutations rejected. [Documentary run 40931825030](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40931825030): **SUCCESS report-only**, with actual logs showing zero approvals/listening signoffs and unchanged protected production assets. Neither workflow deploys.
- Coverage audited in the final ALL logs: **A1 184, A2 84, B1 84, B2 70, C1 51 = 473/1,000 distinct**, **492 observations** (19 repeat observations); **527** without direct Oxford word/POS evidence. Reviewer priorities: **3 unlisted, 15 publisher-higher, 157 publisher-lower, 298 word/POS matches needing exact-sense review, 527 without direct observations**. Source sense leads do not add to this Oxford core-list coverage.

**Per-level written / independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Final George/Emma real listening signoffs **0/1,000**. Full independent review, final voice generation and listening, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages readiness, and confirmed production deployment remain outstanding. **BLOCKED — STAGING ONLY.** No merge, main-branch change or publication.
