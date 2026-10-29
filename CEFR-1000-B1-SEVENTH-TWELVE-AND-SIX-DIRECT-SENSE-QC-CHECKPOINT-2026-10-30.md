# CEFR 1,000 — B1 seventh Oxford batch and six directly opened sense leads (30 October 2026)

**STAGING ONLY — RELEASE BLOCKED.** This concerns the user-approved **1,000 TOTAL** words (A1/A2/B1/B2/C1 **200 each**), not the superseded 5,000. The frozen shortlist, 54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio, privacy controls and `main` were not edited. No independent human review, audio listening, iPhone test or deployment is claimed.

## Twelve new B1-draft Oxford word/POS observations

The official [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) was directly inspected **2026-10-30**. Each row is a word/part-of-speech observation, **not an exact-sense CEFR certification**. PDF pages are 1-based and extracted text lines 0-based. These 12 are distinct from the previously recorded 84 B1 observations.

| Draft B1 | Publisher word/POS level | PDF page / line | Editorial concern |
| --- | --- | --- | --- |
| queen, noun | A2 | 6 / 1519 | Sovereign versus king's wife, chess piece or insect |
| heat, noun | A2 | 5 / 1268 | Hot-weather feeling versus energy/verb |
| truly, adverb | B2 | 12 / 3267 | Sincere appreciation versus quality/intensity emphasis |
| mission, noun | B2 | 11 / 3007 | Assigned rescue task versus institutional/religious mission |
| mass, noun | B2 | 11 / 2991 | Large grouping of clouds versus scientific mass |
| hall, noun | A2 | 5 / 1263 | Event room versus entrance corridor/building |
| cell, noun | B2 | 10 / 2685 | Biological unit versus prison/electrical/spreadsheet senses |
| catch, verb | A2 | 4 / 1030 | Catching a ball versus illness/transport |
| sick, adjective | A1 | 3 / 696 | Ill versus British 'be sick' (vomit) |
| touch, verb | A2 | 7 / 1711 | Physical contact versus emotional impact |
| separate, adjective | A2 | 6 / 1598 | Separate boxes versus verb 'separate' |
| remain, verb | B1 | 9 / 2372 | 'Remain seated' linking verb versus residual quantity |

Publisher distribution: **A1 1, A2 6, B1 1, B2 4**. Thus **11 of 12** provisional B1 placements differ from the publisher's word/POS list; this is a reviewer-priority signal, not an automatic reclassification. The [immutable evidence packet](draft/CEFR-1000-OXFORD-B1-SEVENTH-TWELVE-AND-SIX-SENSE-LEADS-2026-10-30.json) preserves original English/Myanmar/example snapshots, source URL/date/page/line/excerpt, historical source path/index/Git blob SHA, editorial risks and separate reviewer tasks. No source excerpt is treated as an independently approved translation.

## Six directly opened Oxford dictionary sense leads

The following Oxford Advanced Learner's Dictionary pages were directly inspected on **2026-10-30**; line ranges refer to the web text extraction, not dictionary sense IDs.

- [queen](https://www.oxfordlearnersdictionaries.com/definition/english/queen), lines 106–151: female sovereign versus king's wife; the draft's national address implies sovereign. The same page shows A2 topic labels, which are **not** independent exact-sense CEFR signoff.
- [truly](https://www.oxfordlearnersdictionaries.com/definition/english/truly), lines 116–140: sincere feeling versus emphasizing quality/accuracy; the draft 'truly appreciate' points to sincerity.
- [mission](https://www.oxfordlearnersdictionaries.com/definition/english/mission), lines 106–127: official assigned job includes a rescue mission; do not conflate with religious/institutional mission.
- [mass](https://www.oxfordlearnersdictionaries.com/definition/english/mass_1), lines 107–160: shapeless grouping versus large quantity/number; 'a mass of clouds' needs sense-specific Myanmar and countability review.
- [cell](https://www.oxfordlearnersdictionaries.com/definition/english/cell), lines 105–188: biological unit versus prison, electrical and spreadsheet senses; the draft is biological.
- [remain](https://www.oxfordlearnersdictionaries.com/definition/english/remain), lines 103–163: 'remain seated' is the continued-state linking-verb sense; the dictionary notes formal usage and normally non-progressive construction.

These are **editorial interpretations**, not independently validated English, Myanmar, example grammar or CEFR levels. Human-independent content-bound signoff remains mandatory.

## Integrity safeguards and verified CI

Created `tools/audit_cefr_1000_oxford_b1_seventh_twelve.py`, pinning the frozen shortlist Git blob, exact publisher locators and dates, six sense leads, bilingual/example snapshots, original source provenance and all review holds. The **177/177** negative tests reject forged publisher levels, changed Myanmar/example/provenance, fabricated sense URLs, additional fields and fake reviewer receipts. Integrated the auditor into the six parallel A1/A2/B1/B2/C1/ALL structural lanes and documentary no-deploy gate. Updated cross-batch coverage and reviewer-priority reconciliation.

**Verified CI:** [structural run 40966899376](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40966899376) **SUCCESS in all six jobs** at commit `037d6d51ed912ee632c935edaa2642215c4e99f9`. Actual ALL logs confirm 177/177 forged mutations rejected, **520 distinct Oxford-observed entries**, **539 observations**, and protected production assets unchanged. [Documentary no-deploy run 40966906794](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40966906794) **SUCCESS report-only** at commit `0a9b842f573e0f3d684f1ad39ea6f985c9846118`; actual logs explicitly retain independent-review, final audio/listening, browser/mobile, physical iPhone Safari, measured hosting, preservation and deployment blockers. Earlier intermediate CI failures at `74434cc` occurred before all reconciliation/workflow updates and are not counted as passes.

## Exact status after this batch

| Level | First-pass written | Distinct Oxford word/POS observed | Independently approved | Final George/Emma listening signoffs |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 195 | 0 | 0 |
| A2 | 200 | 84 | 0 | 0 |
| B1 | 200 | 96 | 0 | 0 |
| B2 | 200 | 82 | 0 | 0 |
| C1 | 200 | 63 | 0 | 0 |
| **Total** | **1,000** | **520** | **0** | **0** |

**480** entries lack direct Oxford observations in audited packets. Reviewer queue: **3 unlisted (not a CEFR level), 19 publisher-higher, 165 publisher-lower, 333 matching word/POS but exact-sense unverified, 480 without direct observations**. All 1,000 remain editorial holds. The independent bilingual/grammar/CEFR reviewer, complete final dual-voice headword+example generation and *real listening*, approved-corpus desktop/mobile browser regression, physical iPhone Safari QA, measured GitHub Pages hosting, preservation/privacy release check and confirmed live deployment are all still missing. **No merge, main edit or publication. BLOCKED / STAGING ONLY.**


## Six bilingual editorial rewrite candidates — **not applied, not independently reviewed**

These are suggested sense-specific alternatives for a qualified independent English/Myanmar reviewer to accept, revise or reject. They do **not** overwrite the frozen shortlist, change review flags, or establish an independently approved CEFR placement.

| Word | Proposed English sense | Proposed fluent Myanmar gloss | Example review |
| --- | --- | --- | --- |
| queen | A woman who rules a country as its monarch. | နိုင်ငံကို အုပ်ချုပ်သော ဘုရင်မ | Retain “The queen addressed the nation on television.”; distinguish a ruling queen from a queen consort |
| truly | Used to emphasize that a feeling is sincere. | စိတ်ရင်းမှန်ဖြင့်၊ တကယ်တမ်း | Retain “I truly appreciate your help.”; check emphasis and British intonation |
| mission | An important task given to a person or group. | အရေးကြီးသော အထူးတာဝန် | Retain “The rescue team's mission was to find the hikers.”; avoid a religious-mission interpretation |
| mass | A large quantity or group gathered together. | အစုအဝေးကြီး၊ အမြောက်အမြား | Consider “A mass of dark clouds covered the mountain.”; check mass-of countability and cloud collocation |
| cell | The smallest basic unit of a living thing. | ဆဲလ်၊ သက်ရှိ၏ အခြေခံဖွဲ့စည်းယူနစ် | Retain “Every cell in the body needs energy.”; distinguish prison and spreadsheet senses |
| remain | To continue to be in the same state. | အခြေအနေတစ်ခုအတိုင်း ဆက်လက်ရှိနေသည် | Retain “Please remain seated until the bus stops.”; review formal linking-verb usage |

The reviewer must check these Myanmar proposals for natural classroom language, precise meaning, appropriate learner level, and original example grammar. Oxford's wordlist labels are not sense-level approval, and none of these proposals has been independently signed off.
