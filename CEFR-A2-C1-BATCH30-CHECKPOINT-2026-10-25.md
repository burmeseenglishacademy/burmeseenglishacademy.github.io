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

A2–C1 unique written = 1,922; candidate quarantine = 460 unique; earlier 182 duplicate legacy rows excluded. These figures require CI structural confirmation.

## QA, deployment and blockers
- Structural checks are implemented for A2/B1/B2/C1/ALL with no deployment job. **No CI result is claimed until its real run and logs are inspected.**
- Staging `cefr-vocabulary-data.js` remains `entries:[]`. No production files, 54 lessons, IELTS 1,000 bank, George/Emma existing audio or privacy systems were modified.
- Still blocked: source-based dictionary and CEFR sense review; independent Myanmar and example review; re-tier/quarantine of unsupported candidates; CEFR George/Emma audio generation and actual listening; browser/mobile and physical iPhone Safari tests; hosting limits; and verified live release.

**Not complete. Do not notify as complete.**
