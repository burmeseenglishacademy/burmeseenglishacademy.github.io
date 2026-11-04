# CEFR-1000 lemma, morphology and cross-level sense queue — 2026-11-04

**Status:** staging-only original editorial analysis, NOT independent review or publisher CEFR verification. Frozen source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected 2026-11-04. Original `source_index` values below refer to source starter files, not shortlist array offsets. All 1,000 remain held; 200 provisional / 0 independently approved per level.

## Concrete headword-versus-inflection candidates

| Current entry | Original source | Observed exact content / risk | Original proposed editorial disposition (unapproved) |
|---|---|---|---|
| `be` A1 verb | `draft/A1-EDITORIAL-STARTER.json#2` | Lemma `be` already occupies an A1 vocabulary slot. | Retain canonical lemma pending independent review. |
| `is` A1 verb | `draft/A1-EDITORIAL-STARTER.json#120` | Definition explicitly says present form of `be`; example `She is at home.` is grammatical. Counting as a separate lexical headword could inflate vocabulary inventory. | Teach `is` in a grammar/conjugation panel linked to `be`, and independently select a genuinely distinct A1 sense to fill the slot if lemma-only policy adopted. |
| `are` A1 verb | `draft/A1-EDITORIAL-STARTER.json#121` | Definition explicitly says present form of `be`; example `They are friends.` is grammatical. Same lemma policy issue as `is`. | Treat as conjugation of `be`, not automatically as an independently counted lexical headword. |
| `do` A1 verb | `draft/A1-EDITORIAL-STARTER.json#122` | Lexical action verb: `I do my homework.` | Keep lexical `do` distinct from auxiliary grammar usage. |
| `does` A1 auxiliary verb | `draft/A1-EDITORIAL-STARTER.json#123` | Third-person auxiliary `do` in `Does he work here?`; grammatical, but not an independent lemma. | Link to auxiliary `do`; independently decide whether lexical and auxiliary senses each merit a slot, rather than counting the inflection as a new lemma. |
| `did` A1 auxiliary verb | `draft/A1-EDITORIAL-STARTER.json#124` | Past auxiliary `do` in `Did you eat breakfast?`; grammatical, but not an independent lemma. | Link to auxiliary `do`; review grammar-vocabulary boundary before any replacement. |
| `good` A1 adjective | `draft/A1-EDITORIAL-STARTER.json#44` | Positive degree, `That is a good idea.` | Retain as a base adjective; distinguish grammar forms from genuinely separate senses. |
| `better` A2 adjective | `draft/A2-C1-EDITORIAL-STARTER.json#86` | Comparative form can derive from `good` or `well`; current definition `Of a higher quality or more suitable than something else.` and example `The second plan is better for our budget.` | Ask independent reviewer whether comparative morphology qualifies as separate A2 lexical headword; do not auto-remove or assume source CEFR. |

## Related but not automatically duplicate

- `people` A1 **plural noun** (`draft/A1-EDITORIAL-STARTER.json#43`) is glossed `More than one person.`, with `Many people are here.`; `person` A2 **noun** (`draft/A2-C1-EDITORIAL-STARTER.json#191`) means one human individual, with `Only one person can enter at a time.` The entries are semantically related and level-inverted by everyday teaching expectations, but `people` also has collective lexical use; do not mechanically collapse or relocate without sense-specific learner-dictionary evidence and reviewer decision.
- The current CI duplicate check normalises **headword + part of speech**, so `be/is/are` and `do/does/did` all pass that check even though a lemma-only counting policy could disallow them. This is a policy/semantic blind spot, **not** evidence that the existing structural test is broken.

## Independent evidence tasks and decision log template

For each proposed decision, record: original word, level, POS, exact sense, source path/index/blob, publisher name and direct sense URL, page observation date, verbatim short CEFR label (if explicitly shown), whether the label belongs to this **exact** POS/sense, reviewer identity independent of author, English/Myanmar/example/pronunciation decisions, accepted replacement candidate and its independent evidence, and any unresolved disagreement. A publisher page showing only a generic headword is insufficient to certify the target sense. These entries have **no new publisher-backed CEFR evidence** in this workpack; their current levels remain hypotheses.

A replacement must preserve exactly 200 independently accepted distinct headword/sense entries per level and must not silently change the frozen provisional shortlist. Candidate Burmese instructions: `is/are` → `be ကြိယာ၏ ပစ္စုပ္ပန်ကာလ ပုံစံများ`; `does/did` → `မေးခွန်းနှင့် အငြင်းဝါကျများတွင် သုံးသော do ၏ ပုံစံများ`. These are editorial suggestions, not independent Burmese signoff.

## Release constraints

No `reviewed_*` or `release_approved` flags changed; no shortlist replacement made. The frozen first-pass counts are A1 200/0 approved, A2 200/0, B1 200/0, B2 200/0, C1 200/0. George/Emma final audio generation and **real** listening signoff, independent English/Myanmar/example/CEFR review, browser/mobile and physical iPhone Safari QA, GitHub Pages hosting evidence, production asset-preservation checks and confirmed deployment are still required. Preserve 54 lessons, separate IELTS 1,000-word bank, existing George/Emma production audio and privacy. No production launch is authorised until every gate has genuine evidence.
