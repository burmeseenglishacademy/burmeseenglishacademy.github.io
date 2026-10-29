# CEFR 1,000 B2 sixth Oxford research and four direct dictionary sense leads — 30 October 2026

**STAGING ONLY — RELEASE BLOCKED.** This is the USER-APPROVED **1,000 TOTAL**, not the superseded 5,000-word plan. Keep the existing branch name `cefr-5000-bilingual-qa-staging`. The frozen `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` remains 200 first-pass bilingual entries per A1/A2/B1/B2/C1 level, with **0 independently approved**. No publisher research here is an independent human review.

## Twelve new directly inspected Oxford 5000 word/POS observations

The official [Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) was directly inspected on **2026-10-30**. Twelve previously unobserved **B2-draft** headwords have B2 publisher word/POS entries; the PDF is not an exact-sense CEFR source.

| B2 draft | Oxford PDF page (1-based) / extracted line (0-based) | Review focus |
| --- | --- | --- |
| extensive | 1 / 238 | Large-scale damage versus geographical coverage |
| formation | 2 / 260 | Establishing a committee versus other noun senses |
| partnership | 2 / 455 | Cooperative arrangement versus legal business entity |
| principal | 2 / 481 | Main/primary adjective versus principal noun and principle |
| steam | 3 / 597 | Hot water vapour, visible condensation, steam power |
| commander | 1 / 106 | Military leadership versus other command roles |
| monthly | 2 / 401 | Recurring meeting adjective versus salary/payment sense |
| barely | 1 / 52 | Almost unable to hear; negative-polarity grammar |
| psychological | 2 / 495 | Mind/emotions adjective, avoid unsupported clinical implications |
| overcome | 2 / 443 | Successfully deal with fear versus passive emotion use |
| highway | 2 / 304 | Road classification; avoid automatic British motorway equivalence |
| jury | 2 / 358 | Court jury versus competition judging panel |

The [source packet](draft/CEFR-1000-OXFORD-B2-SIXTH-TWELVE-2026-10-30.json) preserves the dated publisher URL, precise PDF page/line and short word/POS excerpts, original English/Myanmar/example snapshots, historical source file/index/Git blob provenance and an independent-review task for each word. **No frozen shortlist, review flags or approved dataset was modified.**

## Four directly opened Oxford dictionary pages

Direct publisher-page inspections on **2026-10-30** were added to the [four-sense review packet](draft/CEFR-1000-OXFORD-B2-SIXTH-FOUR-DIRECT-SENSE-LEADS-2026-10-30.json):

- [principal adjective](https://www.oxfordlearnersdictionaries.com/definition/english/principal_1), page text lines 88–112: pre-nominal *most important/main* sense fits the draft's “principal reason”; distinguish the principal noun and the homophone *principle*. The dictionary displays Oxford 3000 B2 while the Oxford 5000 PDF also lists B2, a list-membership surface discrepancy **without a level disagreement**.
- [monthly adjective](https://www.oxfordlearnersdictionaries.com/definition/english/monthly_1), lines 88–120: the draft's monthly meeting uses the recurring-frequency sense, not the salary/calculation sense. The dictionary also displays Oxford 3000 B2 while the Oxford 5000 PDF lists B2.
- [barely adverb](https://www.oxfordlearnersdictionaries.com/definition/english/barely), lines 88–147: the draft “could barely hear” uses the just-possible-with-difficulty sense, not quantity or immediate-sequence senses. Check Myanmar fluency and negative-polarity grammar.
- [steam noun](https://www.oxfordlearnersdictionaries.com/definition/english/steam_1), lines 88–174: the dictionary distinguishes hot gaseous water, steam-generated power and condensed droplets. The visible plume above soup merits an independently chosen learner-friendly definition and Burmese meaning.

These are **direct sense descriptions and editorial research leads only**. Neither the dictionary's topic tags nor a wordlist badge is accepted as an independently reviewed **exact-sense CEFR** judgement. No independent human translation, grammar, pronunciation or level signoff has occurred.

## Fail-closed CI and evidence integrity

Added `tools/audit_cefr_1000_oxford_b2_sixth_twelve.py` (151 adversarial cases) and `tools/audit_cefr_1000_oxford_b2_four_sense_leads.py` (53 cases), binding the new evidence to frozen shortlist snapshots and historical provenance, rejecting forged source/translation/approval mutations. Integrated both in the existing **six parallel A1/A2/B1/B2/C1/ALL** structural jobs and the documentary no-deploy workflow; updated cross-batch source coverage and human-review handoff expectations.

**Verified CI code head `060fad4cf87ae03e2719fa9a3572a279e28bf575`:** [structural run 40953733136](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40953733136) **SUCCESS across all six jobs**. Actual ALL logs confirm **151/151** new B2 PDF and **53/53** direct-sense forged mutations rejected, **145/145** independent-handoff mutations rejected, and protected production assets unchanged. [Documentary no-deployment run 40953732985](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40953732985) **SUCCESS as report-only**; actual logs explicitly retain independent-review, final audio/listening, desktop/mobile browser, physical iPhone Safari, hosting, preservation and launch blockers. Earlier failed runs at intermediate heads (invalid YAML step placement and a Burmese-to-Myanmar snapshot-key mismatch) were repaired and are **not** counted as passes.

Verified staging-only comparison against prior head `42d0f08e9563ceb411fa432bc2542d51e510a017`: eight research, auditor and workflow files changed before documentation; no 54-lesson content, IELTS 1,000-word bank, established George/Emma audio, privacy or production assets changed. No merge, main edit or public deployment.

## Exact staging counts and remaining gates

| CEFR level | First-pass written | Distinct Oxford word/POS observed | Human independently approved | Real George/Emma listening signoffs |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 195 | 0 | 0 |
| A2 | 200 | 84 | 0 | 0 |
| B1 | 200 | 84 | 0 | 0 |
| B2 | 200 | 82 | 0 | 0 |
| C1 | 200 | 63 | 0 | 0 |
| **Total** | **1,000** | **508** | **0** | **0** |

There are **527 Oxford word/POS observations** including repeats and **492 provisional headwords without direct Oxford observation**. Review priority: **3 unlisted (not a CEFR label), 15 publisher-higher, 158 publisher-lower, 332 word/POS matches still needing exact-sense verification, 492 without observation**. **36 historical excerpts** are separately source-recovered, not additional distinct headwords.

All **1,000 remain editorial holds**. Still required: genuine independent human English/Myanmar/example/CEFR and source signoff; a separately approved exactly 200-per-level deduplicated sense manifest; full George/Emma headword+example audio generated and *really listened to*; approved-corpus desktop/mobile regression; physical iPhone Safari evidence; measured GitHub Pages limits; final preservation/privacy check; and a confirmed live production deployment. **Release: BLOCKED / STAGING ONLY.**
