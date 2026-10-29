# CEFR 1,000 — A1 twelfth Oxford twelve source/POS QC checkpoint

**Observed:** 2026-10-30 (Singapore local date). **Branch:** `cefr-5000-bilingual-qa-staging`. **Scope:** the user-approved 1,000 total (200 each A1/A2/B1/B2/C1), not 5,000. **Release:** BLOCKED / STAGING ONLY.

## Source-supported research — not human-independent exact-sense verification

Directly inspected [Oxford University Press, *The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-30**. The following **12 previously unobserved A1 draft nouns** appear in its A1 word/POS list. Locators are **one-based PDF page / zero-based web extracted line**. The [immutable research packet](draft/CEFR-1000-OXFORD-A1-TWELFTH-TWELVE-2026-10-30.json) retains the exact publisher excerpt, URL, observation date, original shortlist English/Myanmar/example snapshot, and original Git source path/index/blob SHA. These observations support the *word/POS A1 label*, not the intended exact sense or independent bilingual approval.

| Draft word | PDF page / extracted line | Oxford word/POS excerpt | Human review focus |
|---|---:|---|---|
| ear | 1 / 230 | `ear n.` | Anatomical ear; one-ear example; distinguish other senses |
| nose | 2 / 530 | `nose n.` | Body part versus figurative uses |
| mouth | 2 / 500 | `mouth n.` | Imperative example; natural Myanmar and body-part sense |
| face | 2 / 264 | `face n.` | Anatomical noun, not verb or clock face |
| hair | 2 / 345 | `hair n.` | Mass noun in example versus individual hairs |
| foot | 2 / 303 | `foot n.` | Foot versus leg and measurement unit; Myanmar breadth |
| cat | 1 / 134 | `cat n.` | Domestic animal sense |
| dog | 1 / 218 | `dog n.` | Domestic animal; barking description not universal |
| bird | 1 / 88 | `bird n.` | Bird is not defined by flight ability |
| fish | 2 / 294 | `fish n.` | Living animal versus food; plural morphology |
| horse | 2 / 375 | `horse n.` | Animal versus sport/chess/figurative senses |
| cow | 1 / 180 | `cow n.` | Adult female bovine versus broad Myanmar နွား |

**Unapplied editorial concerns:** `foot` currently has Myanmar `ခြေဖဝါး၊ ခြေထောက်`; the latter can refer to the leg more broadly. `cow` has Myanmar `နွား`, which may not distinguish an adult female bovine from cattle generally. `fish` needs living-animal versus food sense separation; `hair` needs mass/count grammar; body-part words have figurative senses. All original examples and Myanmar meanings remain unchanged, unapproved and on editorial hold.

## Reconciliation and CI verification

| Level | First-pass written | Distinct Oxford word/POS observed | Human-independently approved |
|---|---:|---:|---:|
| A1 | 200 | 172 | 0 |
| A2 | 200 | 72 | 0 |
| B1 | 200 | 84 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **449** | **0** |

There are **468 publisher observations for 449 distinct provisional headwords** (19 repeated observations), and **551** without direct Oxford observations. Full handoff priorities: **152 publisher-lower, 13 publisher-higher, three unlisted (not CEFR labels), 281 matching word/POS but exact sense unverified, 551 without direct observations**. All 1,000 retain independent-review holds. The 36 historical locator-only entries have separate excerpt recovery references; none is human signoff.

The new [fail-closed twelfth A1 auditor](tools/audit_cefr_1000_oxford_a1_twelfth_twelve.py) reconstructs the 12 source records from the frozen shortlist and fixed directly inspected PDF anchors, rejects count-preserving source/translation/example/provenance/receipt mutations, and runs **238 adversarial negative tests**. Both six-lane [structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml) include the packet and auditor. Updated cross-batch coverage and 1,000-item independent reviewer handoff reconciliation.

- [Structural run 40912634216](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40912634216): **SUCCESS across A1, A2, B1, B2, C1, ALL** on code commit `106e26ceea50c9ccb4c18623d4d7d755913529d3`. Actual ALL-job logs confirm **238/238** new adversarial mutations rejected, **145/145** full-handoff integrity mutations rejected, 449 distinct Oxford observations and protected production assets unchanged.
- [Documentary run 40912633512](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40912633512): **SUCCESS as report-only**, on the same commit, explicitly retaining human/audio/iPhone/hosting blockers; no deployment. Actual logs confirm the twelfth auditor, updated reviewer priority counts and protected production assets PASS.
- Earlier intermediate runs [40912589535](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40912589535) and [40912600123](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40912600123) **FAILED** because the handoff validation retained the stale `563` missing-evidence assertion after the new `551` count. Corrected in `106e26ceea50c9ccb4c18623d4d7d755913529d3`; subsequent final runs above succeeded. Do not conceal these intermediate failures.

## Mandatory launch blockers

**A1/A2/B1/B2/C1 written / independently approved:** 200/0 each. **Final British George/Emma real listening signoffs:** 0/1,000. Missing: genuine independent human English/Myanmar/original-example/exact-sense and source-backed CEFR signoff for all 1,000; an approved deduplicated 200-per-level release manifest; full final headword and example audio for both voices with actual human listening; approved-corpus desktop/mobile regression; real physical iPhone Safari evidence; measured GitHub Pages site/audio bundle and deployment/bandwidth limits; preserved 54 lessons, separate IELTS 1,000 bank, established production audio and privacy at launch; and confirmed live production deployment. **No merge, main modification, publishing, simulated reviewer, or simulated device/listening evidence. STAGING ONLY.**
