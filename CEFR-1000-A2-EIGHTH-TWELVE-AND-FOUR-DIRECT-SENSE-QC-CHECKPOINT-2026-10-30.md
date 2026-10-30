# CEFR 1000 — A2 eighth Oxford research and four directly opened dictionary senses (2026-10-30)

**STAGING ONLY / RELEASE BLOCKED.** This is the user-approved **1,000 total** (A1/A2/B1/B2/C1 = 200 first-pass entries each), not 5,000. Branch: `cefr-5000-bilingual-qa-staging`. Frozen shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No independent human approval, audio listening receipt, physical iPhone review or production deployment.

## Direct official publisher research

Directly inspected [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **30 October 2026**. PDF pages are 1-based, extracted text lines 0-based. The [source-bound twelve-record research packet](draft/CEFR-1000-OXFORD-A2-EIGHTH-TWELVE-AND-FOUR-SENSE-LEADS-2026-10-30.json) records the verbatim word/POS excerpt, URL, date, page/line, English/Myanmar/example snapshot, historical Git path/index/blob, editorial risk and independent-review task for every item.

| Provisional A2 word | POS | Oxford word/POS CEFR | PDF page / line | Editorial distinction |
|---|---|---|---|---|
| plan | noun | A1 | 3 / 599 | Intended Saturday visit, not a diagram |
| available | adjective | A2 | 4 / 971 | Room free to use at a time, not product stock |
| chance | noun | A2 | 4 / 1036 | Opportunity versus likelihood or luck |
| experience | noun | A2 | 5 / 1185 | Uncountable work skill versus a countable event |
| example | noun | A1 | 2 / 256 | Illustration of a rule, not a model person |
| price | noun | A1 | 3 / 621 | Retail amount versus overall cost |
| account | noun | B1 | 7 / 1787 | Savings-bank account versus story or online account |
| include | verb | A1 | 2 / 395 | Include a phone number on a form |
| report | noun | A1 | 3 / 648 | School written assignment versus verb/news |
| clear | adjective | A2 | 4 / 1049 | Easy to understand versus visible |
| cost | noun | A1 | 1 / 175 | Expense versus cost as a verb |
| project | noun | A1 | 3 / 626 | School assignment versus business/construction project |

These **12 previously unobserved A2-draft headwords** have publisher word/POS classifications **A1 seven, A2 four, B1 one**. The eight publisher-versus-provisional discrepancies remain unresolved. Oxford word/POS evidence does **not** establish the draft's exact sense, an independently verified teaching level or bilingual accuracy. No shortlist entries or review flags changed.

## Four directly opened Oxford dictionary sense leads

- [plan](https://www.oxfordlearnersdictionaries.com/definition/english/plan_1), lines 106–190: distinguish intention (sense 1) and detailed arrangement (sense 2); the museum-visit example is a personal plan, not a technical drawing.
- [chance](https://www.oxfordlearnersdictionaries.com/definition/english/chance_1), lines 165–178: the school-team example concerns a suitable **opportunity** to join, not merely the probability of success (sense 1).
- [experience](https://www.oxfordlearnersdictionaries.com/definition/english/experience_1), lines 105–129: the draft's work-related knowledge/skill is **uncountable**; an individual event/experience is a different countable sense. The Oxford page's working-life topic A2 label must not be treated as independent exact-sense CEFR signoff.
- [account](https://www.oxfordlearnersdictionaries.com/definition/english/account_1), lines 105–120: the draft targets a **savings bank account**; not a social-media account, a bill, or a narrative. Oxford's word/POS B1 classification conflicts with provisional A2, and independent exact-sense level review is required.

## Original, unapproved bilingual editorial suggestions

The following are suggestions for a separate independent human reviewer, **not** edits to the frozen 1,000 shortlist and **not** evidence of independent linguistic approval.

| Word | Proposed original English example | Suggested fluent Myanmar |
|---|---|---|
| plan | We made a plan to visit the museum on Saturday. | ကျွန်တော်တို့ စနေနေ့မှာ ပြတိုက်ကို သွားဖို့ အစီအစဉ်တစ်ခု ချထားပါတယ်။ |
| chance | She has a chance to join the school team. | သူမမှာ ကျောင်းအသင်းထဲ ဝင်ဖို့ အခွင့်အရေးရှိပါတယ်။ |
| experience | He has experience working in a small shop. | သူ့မှာ ဆိုင်ငယ်တစ်ဆိုင်မှာ အလုပ်လုပ်ဖူးတဲ့ အတွေ့အကြုံရှိပါတယ်။ |
| account | She opened a savings account last month. | သူမက ပြီးခဲ့တဲ့လမှာ ငွေစုဘဏ်စာရင်းတစ်ခု ဖွင့်ခဲ့ပါတယ်။ |
| include | Please include your phone number on the form. | ဖောင်မှာ သင့်ဖုန်းနံပါတ်ကို ထည့်ရေးပေးပါ။ |

## Safeguards and truthful release state

The [new fail-closed A2 eighth auditor](tools/audit_cefr_1000_oxford_a2_eighth_twelve.py) pins the frozen shortlist Git blob, publisher excerpts and locators, bilingual/example snapshots, historical provenance and editorial hold. It is wired into six parallel A1/A2/B1/B2/C1/ALL structural jobs and report-only documentary no-deploy checks, with an early Python syntax preflight. **Fresh CI job conclusions and actual logs must be inspected before calling these changes verified.**

Expected direct Oxford word/POS coverage after this packet: **A1 195/200, A2 108/200, B1 108/200, B2 94/200, C1 87/200 = 592/1,000 distinct** across **611 observations**, leaving **408 without direct observations**. Expected reviewer queue: **3 unlisted, 23 publisher-higher, 200 publisher-lower, 366 matching word/POS but exact-sense-unverified, 408 without observations**. These counts require fresh successful cross-batch CI confirmation.

First-pass written / independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Real final George/Emma listening signoffs **0/1,000**. Independent English/Myanmar/grammar/exact-sense CEFR review, final dual-voice headword/example audio generation and real listening, browser/mobile regression, physical iPhone Safari QA, measured GitHub Pages hosting readiness, protected production-asset verification at release and confirmed live deployment remain missing. **NO MERGE / NO MAIN CHANGE / NO PUBLICATION.**
