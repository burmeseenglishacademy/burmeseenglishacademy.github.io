# CEFR-1000: exact Myanmar gloss collisions requiring semantic review
Observed: 2026-11-20 (SGT). Scope: staging research only; not independent signoff.

## Provenance and method
- Source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json
- Source Git blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Independent review task source: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json ; blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- Parsed all 1,000 `entries`; grouped by identical Myanmar gloss after Unicode NFKC normalization and trimming leading/trailing whitespace. This is an **exact-string** check, not semantic similarity detection. Seven collision groups involving 14 entries were found. Zero exact duplicate English definition strings were found (case-insensitive, trimmed). No inference of independent review, CEFR validity, or correctness is made.

## Seven collision groups and editorial distinctions
| Level / headword | Shared provisional Myanmar gloss | Editorial distinction to test (author hypothesis, not independently checked) |
| --- | --- | --- |
| A1 **need** / B1 **require** (verbs) | လိုအပ်သည် | *Need* may express personal necessity; *require* can mean a rule or situation formally demands something. Check if the examples require a more explicit Myanmar distinction. |
| A2 **deal** / B1 **agreement** (nouns) | သဘောတူညီချက် | *Deal* often denotes an arrangement or transaction; *agreement* can mean consent or a negotiated understanding. Verify the particular intended noun sense. |
| A2 **finally** / B1 **eventually** (adverbs) | နောက်ဆုံးတွင်၊ အချိန်ကြာပြီးနောက် | *Finally* can mark the last step or an anticipated ending; *eventually* highlights the outcome after a delay. Do not teach them as universally interchangeable. |
| B1 **protect** / B2 **defend** (verbs) | ကာကွယ်သည် | *Protect* emphasizes preventing harm; *defend* can mean resisting an attack or supporting a position. The latter may need a different Myanmar phrase depending on its example. |
| B1 **competition** / B2 **contest** (nouns) | ပြိုင်ပွဲ | Both can refer to a competition; review the examples and whether a distinguishable exact sense exists. Do not manufacture a difference solely to satisfy unique-gloss checks. |
| B1 **mental** / B2 **psychological** (adjectives) | စိတ်ပိုင်းဆိုင်ရာ | Both can describe the mind; *psychological* may be technical or describe psychological processes. Check whether register or context warrants a distinct Burmese rendering. |
| B2 **calm** / B2 **stable** (adjectives) | တည်ငြိမ်သော | *Calm* may describe quiet emotions/conditions; *stable* may describe lack of change or structural firmness. Shared gloss risks conflating these. |

## Independent review intake
For each of the 14 entries, an independent bilingual reviewer should check: (1) exact English sense and part of speech; (2) whether the existing Myanmar gloss is fluent and context-appropriate; (3) whether the example actually illustrates that sense; (4) independent exact-sense CEFR evidence with URLs and observation dates; (5) whether the entry remains distinct from the other headword. Reviewers may legitimately approve identical Myanmar glosses when justified: gloss uniqueness is **not** a release requirement. Suggested additions must be checked against the original example, not silently applied.

## Fail-closed release policy
Treat this report as a **warning queue**, not an approval record. Preserve all `editorial_hold` and reviewer fields. Do not count any of these 14 as independently reviewed. The target remains exactly 200 entries per A1/A2/B1/B2/C1 (1,000 provisional first-pass entries, 0 independently approved). Release still requires independent English/Myanmar/example/exact-sense CEFR evidence, complete British George and Emma headword/example audio with real listening signoff, browser/mobile and physical iPhone Safari evidence, GitHub Pages hosting verification, protected production asset checks, and confirmed live deployment. Do not modify main, the 54 lessons, separate IELTS bank, existing production audio, or privacy controls.
