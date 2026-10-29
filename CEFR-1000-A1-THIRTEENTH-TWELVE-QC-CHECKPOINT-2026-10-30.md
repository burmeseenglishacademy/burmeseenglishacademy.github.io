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
