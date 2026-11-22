# CEFR-1000 British spelling and canonical headword audit — 2026-11-22

**Scope:** Approved 1,000-total project only; author-side triage, not independent review or approval. **Release:** BLOCKED. Observation date: 2026-11-22 (Singapore). Branch: `cefr-5000-bilingual-qa-staging`.

## Reproducible provenance

- Provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Independent tasks: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`, Git blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- The five levels each contain 200 provisional written entries (A1/A2/B1/B2/C1 = 200/200/200/200/200); independently approved = 0/0/0/0/0. This is a count, not an assertion of linguistic correctness.

## Exact records needing editorial decision

| Level | Provisional headword | Existing example | Concern | Original candidate / action |
|---|---|---|---|---|
| A1 | `i` (pronoun) | “I am a student.” | Headword is lower-case although the first-person singular pronoun is conventionally capitalised. A lower-case canonical key may be deliberate for search normalization, but learner-facing display should not teach lower-case `i`. | Preserve stable machine key if needed; render `I` in UI/audio transcript; test case-insensitive lookup and capitalised display. |
| B1 | `organization` (noun) | “The organization provides free classes for adults.” | UK standard editorial spelling generally `organisation`; `organization` is also accepted in Oxford British spelling. Not an unconditional mistake. | If choosing UK -ise style: “The organisation provides free classes for adults.” Myanmar meaning `အဖွဲ့အစည်း` is a plausible first-pass equivalent, not independently reviewed. |
| B1 | `realize` (verb) | “I didn't realize the door was locked.” | UK -ise style normally `realise`; Oxford British style allows `realize`. | UK -ise candidate: “I didn't realise the door was locked.” Myanmar `သဘောပေါက်သည်` requires contextual check against 'become aware'. |
| B2 | `recognize` (verb) | “I did not recognize the street after the renovation.” | UK -ise style normally `recognise`; Oxford British style allows `recognize`. | UK -ise candidate: “I did not recognise the street after the renovation.” Myanmar `မှတ်မိသည်၊ ခွဲခြားသိရှိသည်` requires independent exact-sense review. |

Original source provenance for `i`: `draft/A1-EDITORIAL-STARTER.json` index 3, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`. The three -ize entries originate from `draft/A2-C1-EDITORIAL-STARTER.json` blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`, indices 94 (`organization`), 773 (`realize`) and 317 (`recognize`).

## External orthography evidence observed 2026-11-22

1. Singapore Speak Good English Movement, *Let's Connect* booklet, chapter “Singapore English, British English and American English”, page 35: explicitly explains that -ize is used by some British publishers, including Oxford and Longman, so -ize is **not exclusively American**. URL: https://www.languagecouncils.sg/goodenglish/-/media/sgem/document/pdfs/lets-connect-booklet.pdf
2. IUCN *Style Manual*, June 2025, page 10: specifies -ise/-isation as its **own** British editorial preference while recognising Oxford alternatives and preserving official names. URL: https://iucn.org/sites/default/files/2025-06/gl.kmp_.4_iucn_style_manual_june2025_0.pdf
3. University of Barcelona, *Spelling at the UB*: compares standard British, Oxford and US conventions, including `organise/organize` and `recognise/recognize`. URL: https://www.ub.edu/llibre-estil/criteri.php?id=3536

These sources substantiate spelling conventions **only**, not CEFR levels or independent review. Exact-sense CEFR evidence is still absent for these four entries in this audit.

## Fail-closed next actions

1. Independently select a consistent learner-facing British orthography policy (e.g. UK -ise or Oxford -ize) and document exceptions. Do not automatically mark all -ize forms wrong or replace all `z` with `s`.
2. Keep stable IDs and the 200-per-level target when proposing any headword display change. Preserve search aliases and check the exact audio script against approved display text before generating George/Emma recordings.
3. Add a display/headword test for the pronoun `I`, and an explicit policy-driven spelling linter with negative fixtures. Treat this report as a triage queue, not a reviewer signature.
4. Require human-independent English, Myanmar, example and exact-sense CEFR review with source URLs, observation dates, reviewer identity and timestamp. Do not flip approval fields on author inspection.
5. Current GitHub Actions conclusions for this report's commit, complete audio listening signoff, real physical iPhone Safari, browser/mobile regression, Pages hosting and production deployment are **not verified**. No protected production assets or main-branch files were changed.

**Editorial status:** all 1,000 remain on hold; publication is prohibited.
