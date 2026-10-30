# CEFR 1000 — eighth B2 twelve Oxford word/POS observations and four dictionary sense leads (30 October 2026)

**STAGING ONLY — NO HUMAN-INDEPENDENT APPROVAL, NO MERGE, NO DEPLOYMENT.** The authorised target remains exactly **1,000 total (A1/A2/B1/B2/C1: 200 each)**, not 5,000. Frozen provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`); separate independent-review tasks remain unchanged. This packet is **editorial research**, not a release manifest.

## Direct publisher evidence

On **2026-10-30**, inspected [Oxford University Press, *The Oxford 5000 by CEFR level* (8-page PDF)](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf). Each locator below is a **one-based PDF page / zero-based extracted web-text line**, not a dictionary sense identifier. The [source-bound JSON packet](draft/CEFR-1000-OXFORD-B2-EIGHTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json) retains the exact publisher excerpt, original English definition, Myanmar meaning, original example, upstream `source_path`, `source_index`, `source_blob_sha`, risk, reviewer task and unapproved flags.

| B2 draft headword | Oxford word/POS | PDF page / extracted line | Independent editorial question |
|---|---|---|---|
| convention (noun) | B2 | 1 / 130 | Professional conference, not social convention or treaty |
| equivalent (adjective) | B2 | 1 / 216 | Adjective comparison, not noun equivalent |
| universal (adjective) | B2 | 3 / 672 | Shared concern versus literal universality |
| infrastructure (noun) | B2 | 2 / 332 | Systems/utilities as well as buildings |
| recognition (noun) | B2 | 2 / 515 | Public appreciation versus identification |
| mechanism (noun) | B2 | 2 / 390 | Abstract operational process versus physical machine |
| acquisition (noun) | **C1** | 3 / 727 | **Publisher-higher conflict**; business purchase versus skill acquisition |
| outstanding (adjective) | B2 | 2 / 442 | Excellent versus unpaid/unfinished |
| primarily (adverb) | B2 | 2 / 480 | Mainly, not exclusively |
| circuit (noun) | B2 | 1 / 92 | Electrical path versus track or itinerary |
| healthcare (noun) | B2 | 2 / 299 | Services and systems, not only treatment |
| membership (noun) | B2 | 2 / 393 | Membership status versus fee or member count |

**Source classification:** 11 B2 and 1 C1. Oxford word/POS evidence **does not independently establish the draft's exact sense or CEFR**, and does not validate English definition, fluent Myanmar, example grammar, British pronunciation or listening. **Acquisition must not be silently re-tiered**: its B2 provisional placement remains on hold pending independent reviewer decision.

## Direct dictionary sense observations (2026-10-30)

- [convention, noun](https://www.oxfordlearnersdictionaries.com/definition/english/convention), extracted lines 148–179: sense 2 covers a large professional/political gathering; sense 1 (lines 105–123) is a social custom, sense 3 (181–191) is an international agreement.
- [equivalent, adjective](https://www.oxfordlearnersdictionaries.com/definition/english/equivalent_2), lines 88–123: comparable in value, amount, meaning or importance. The [separate noun entry](https://www.oxfordlearnersdictionaries.com/definition/english/equivalent_1) is not evidence for the draft adjective.
- [acquisition, noun](https://www.oxfordlearnersdictionaries.com/definition/english/acquisition), lines 136–150: business acquisition sense 3 matches the smaller-firm example; skill/knowledge acquisition is a separate sense at 105–108.
- [outstanding, adjective](https://www.oxfordlearnersdictionaries.com/definition/english/outstanding), lines 105–129: excellent service sense 1; unpaid/unfinished sense 2 appears at 142–151.

These are directly observed **sense leads**, not independent source-backed exact-sense CEFR approval. Dictionary page badges and topic labels are not automatically interchangeable with PDF word/POS classification.

## Unapproved Myanmar/editorial alternatives — for independent human review only

| Word | Proposed Myanmar meaning | Original English example and proposed Myanmar rendering |
|---|---|---|
| convention | တူညီသော လုပ်ငန်းနယ်ပယ် သို့မဟုတ် အဖွဲ့အစည်းမှ လူများ စုဝေးသည့် ညီလာခံ | *The annual convention attracted teachers from many countries.* — နှစ်ပတ်လည် ညီလာခံသို့ နိုင်ငံအများအပြားမှ ဆရာ၊ ဆရာမများ လာရောက်တက်ရောက်ခဲ့ကြသည်။ |
| equivalent (adj.) | တန်ဖိုး၊ အဆင့်အတန်း သို့မဟုတ် အဓိပ္ပာယ် တူညီသော | *The two qualifications are considered equivalent.* — အဆိုပါ အရည်အချင်းလက်မှတ်နှစ်ခုကို အဆင့်အတန်းတူညီသည်ဟု သတ်မှတ်ကြသည်။ |
| acquisition (business noun) | ကုမ္ပဏီ သို့မဟုတ် လုပ်ငန်းတစ်ခုကို ဝယ်ယူလွှဲပြောင်းရယူခြင်း | *The acquisition of the smaller firm took six months.* — ကုမ္ပဏီငယ်ကို ဝယ်ယူလွှဲပြောင်းရယူသည့် လုပ်ငန်းစဉ်သည် ခြောက်လကြာမြင့်ခဲ့သည်။ |
| outstanding (excellent) | ထူးကဲကောင်းမွန်သော၊ အထူးထူးချွန်သော | *The team received an award for outstanding service.* — အဖွဲ့သည် ထူးချွန်သော ဝန်ဆောင်မှုကြောင့် ဆုရရှိခဲ့သည်။ |

**None of these proposed translations was written back to the frozen shortlist.** Independent bilingual reviewers must accept, amend or reject them with dated, content-bound receipts; they must also check example naturalness and register, and distinguish draft wording from new proposed wording.

## Structural QA and release blockers

New fail-closed [eighth B2 auditor](tools/audit_cefr_1000_oxford_b2_eighth_twelve.py) checks publisher locators/excerpts, frozen bilingual/example snapshots, historical provenance, human-review holds and dictionary sense lead immutability, and exercises adversarial mutations. It is wired into six parallel A1/A2/B1/B2/C1/ALL structural jobs and the documentary no-deployment gate. **A successful structural check is never a linguistic approval or a release authorisation.**

Expected coverage after this batch, **subject to fresh successful CI**: A1 195/200, A2 108/200, B1 108/200, B2 106/200, C1 87/200 = **604/1,000** distinct Oxford word/POS observations across **623** observations; **396** lack direct Oxford observations. Expected priority counts: 3 unlisted, 24 publisher-higher, 200 publisher-lower, 377 word/POS matches needing independent exact-sense review and 396 without observation.

Written / independently approved: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. George/Emma **final real listening signoffs: 0/1,000**. Full independently approved release manifest, dual-voice headword and example audio with actual listening, desktop/mobile browser regression, real physical iPhone Safari evidence, measured GitHub Pages capacity and confirmed production deployment remain absent. Existing 54 lessons, separate IELTS 1,000-word bank, established production George/Emma audio and privacy assets are protected. **BLOCKED / STAGING ONLY.**
