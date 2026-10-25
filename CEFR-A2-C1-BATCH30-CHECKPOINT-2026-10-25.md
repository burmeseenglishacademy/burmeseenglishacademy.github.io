# Burmese English Academy — Batch30 staging checkpoint (25 October 2026)
**HOLD: unverified first-pass bilingual drafts; never merge or publish.**

## Substantive work
- 52 distinct original English/Myanmar vocabulary drafts: **A2 8, B1 16, B2 14, C1 14**. All 52 include selected POS, a meaning, and a complete original usage sentence.
- 52 distinct **separate** independent review tasks for English dictionary sense/POS, natural Myanmar, example grammar, sense-specific CEFR and later George/Emma listening; **all remain pending**.
- 10 reversible holds for wrong WordNet senses, named entities and misleading candidate clues. No held word was counted as a draft.
- C1 candidates, plus several A2/B1/B2 candidates, are **explicitly flagged for re-tier or quarantine** because provisional pool tiers are not CEFR evidence.
- Source pages, external Myanmar reviewers, recordings, listening and real-device iPhone Safari were **not** checked.
- Increased the candidate-preview GitHub Action to 200 per level (commit `3522ff0c5aa62b08a418a2084ff254686ae20530`); inspected successful real preview run `40172476996`, job `121106056202`. Candidates selected from its unheld, undrafted preview.

## Exact unique first-pass inventory (not independently approved)
| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 502 | 0 | 198 |
| B1 | 1,000 | 523 | 0 | 477 |
| B2 | 1,300 | 521 | 0 | 779 |
| C1 | 1,500 | 376 | 0 | 1,124 |
| **Total** | **5,000** | **2,422** | **0** | **2,578** |

A2–C1 unique written = 1,922; candidate quarantine = 460 unique; earlier 182 duplicate legacy rows excluded. These figures were reconciled in the successful ALL structural CI job (see verified evidence below).

## QA, deployment and blockers
- Structural checks are implemented for A2/B1/B2/C1/ALL with no deployment job. **All five jobs were inspected and passed structural QA only; see verified evidence below.**
- Staging `cefr-vocabulary-data.js` remains `entries:[]`. No production files, 54 lessons, IELTS 1,000 bank, George/Emma existing audio or privacy systems were modified.
- Still blocked: source-based dictionary and CEFR sense review; independent Myanmar and example review; re-tier/quarantine of unsupported candidates; CEFR George/Emma audio generation and actual listening; browser/mobile and physical iPhone Safari tests; hosting limits; and verified live release.

**Not complete. Do not notify as complete.**


## Verified GitHub Actions evidence
- Atomic batch30 draft, quarantine, task, auditor, workflow and report commit: `a0a63706b44b21203f262255c324e745077ec993`.
- Actual batch30 run: [40172614783](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40172614783), **five completed successful structural jobs**.
- A2 job `121106468859`: completed / success; log says `STAGING ONLY batch30 A2 PASS`.
- B1 job `121106468785`: completed / success; log says `STAGING ONLY batch30 B1 PASS`.
- B2 job `121106468791`: completed / success; log says `STAGING ONLY batch30 B2 PASS`.
- C1 job `121106468653`: completed / success; log says `STAGING ONLY batch30 C1 PASS`.
- ALL job `121106468815`: completed / success; log reconciles **A2 502, B1 523, B2 521, C1 376 = 1,922 unique A2–C1**, A1 500, total 2,422, 2,578 unwritten, **0 independent approvals**, 182 excluded duplicate legacy rows. Each decoded job log was inspected.
- Staging branch remained isolated; checked `main` head `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from the prior checkpoint. Staging `cefr-vocabulary-data.js` still has `entries:[]`.
- The CI success is **structural QA only**, not independent evidence that any English/Myanmar meaning, CEFR tier, example or pronunciation is correct.

## Next independent editorial review blockers
Prioritise re-tiering or quarantining **all 14 provisional C1 drafts** and the flagged lower-tier words; the source candidate pool is frequency/WordNet derived and does not provide sense-specific CEFR authority. Verify POS and exact sense against an actually consulted dictionary, obtain independent Myanmar naturalness and example reviews, and record URLs, observation dates and reviewer evidence before changing any approval flag. Quarantined `yeah`, `wow` and `tattoo` require explicit sense reconciliation; named entities remain on hold. Audio must not be generated for publication until the text is approved, and listening/physical-device checks cannot be replaced by automated tests.
