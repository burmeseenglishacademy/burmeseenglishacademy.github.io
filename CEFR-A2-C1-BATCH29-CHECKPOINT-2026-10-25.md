# Burmese English Academy — Batch29 corrected staging checkpoint (25 October 2026)
**HOLD: unverified first-pass drafts only; never merge or publish.**

## Real QA finding and correction
The first Batch29 CI run [40167162660](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40167162660) failed all five level-specific jobs at the duplicate-prevention assertion. Inspected decoded ALL and A2 logs; the original candidate preview preceded Batch26, so 27 proposed drafts and 12 proposed holds had already been used in Batch26. The draft/quarantine collisions were **removed**, not counted twice. Added 17 new original bilingual drafts and 5 new distinct reversible holds. The original failing run remains historical evidence, not a pass.

## This corrected iteration
- **42 distinct original bilingual drafts:** A2 8, B1 10, B2 12, C1 12.
- **42 separate review packets:** English definition/POS, natural Myanmar, grammatical example, sense-specific CEFR and audio/listening, all pending.
- **9 distinct reversible candidate holds:** named/capitalisation problems, wrong WordNet senses, slang/register and unsuitable POS.
- Candidate WordNet senses and provisional levels are NOT authoritative. C1 contains likely lower-level words explicitly flagged for re-tier or quarantine.

## Exact unique written inventory — not independently checked
| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 494 | 0 | 206 |
| B1 | 1,000 | 507 | 0 | 493 |
| B2 | 1,300 | 507 | 0 | 793 |
| C1 | 1,500 | 362 | 0 | 1,138 |
| **Total** | **5,000** | **2,370** | **0** | **2,630** |

A2–C1 unique written 1,870; quarantine 449 total (440 prior + 9 distinct new); 182 prior identical legacy duplicates excluded.

## Quality and release blockers
No independent dictionary/POS/CEFR source observations, Myanmar sign-off, example sign-off, full new CEFR George/Emma generation, listening, real-device iPhone Safari, hosting-limit sign-off or live deployment. GitHub Actions check structure, not linguistic correctness.
Staging `cefr-vocabulary-data.js` stays `entries:[]`. No production lesson, IELTS, existing audio, privacy or main changes.

## CI
The corrected atomic staging commit triggers five parallel jobs A2/B1/B2/C1/ALL; their real status and decoded logs must be checked before marking structural QA successful.
