# CEFR-1000 example–headword morphological coverage audit — 2026-11-04

**Status: staging-only editorial work; NOT independent verification or release approval.**

## Scope and reproducibility
Read `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` at blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551` on branch `cefr-5000-bilingual-qa-staging`. Observation date: 2026-11-04. All 1,000 records scanned using case-insensitive whole-word exact headword matching against `example_sentence`; **995/1,000** contain their literal headword and **5/1,000** do not. This is a narrow mechanical signal, **not** an assessment of semantic correctness or CEFR. The five examples below use grammatically valid inflections; they are not automatically errors.

## Five reviewable exceptions (source-index provenance)

| Level | Headword / POS | Original example | Source path / index | Reason and proposed editorial action |
|---|---|---|---|---|
| A1 | hand / noun | Please wash your hands. | `draft/A1-EDITORIAL-STARTER.json` / 172 | Plural *hands* is natural. Candidate lemma-visible example: **Please raise your hand.** Myanmar example translation: **ကျေးဇူးပြု၍ လက်မြှောက်ပါ။** Decide whether inflected examples are allowed. |
| A1 | eye / noun | I have two eyes. | `draft/A1-EDITORIAL-STARTER.json` / 173 | Plural *eyes* is natural. Candidate: **My left eye hurts.** Myanmar: **ကျွန်တော့်/ကျွန်မရဲ့ ဘယ်ဘက်မျက်လုံး နာနေတယ်။** |
| B2 | manage / verb | We managed to finish the work before the deadline. | `draft/A2-C1-EDITORIAL-STARTER.json` / 101 | Past *managed* accurately exemplifies *manage to + infinitive*. Candidate: **Can you manage to finish before Friday?** Myanmar: **သောကြာနေ့မတိုင်ခင် အပြီးလုပ်နိုင်မလား။** |
| B2 | destroy / verb | The fire destroyed the old warehouse. | `draft/A2-C1-EDITORIAL-STARTER.json` / 253 | Past *destroyed* is grammatical. Candidate: **A large fire can destroy a warehouse.** Myanmar: **မီးကြီးလောင်ရင် ဂိုဒေါင်တစ်လုံး ပျက်စီးသွားနိုင်တယ်။** |
| B2 | grab / verb | She grabbed her bag and ran outside. | `draft/A2-C1-EDITORIAL-STARTER.json` / 256 | Past *grabbed* is grammatical. Candidate: **Grab your coat before you leave.** Myanmar: **မထွက်ခင် အပေါ်အင်္ကျီကို အမြန်ယူလိုက်ပါ။** |

**Source blob provenance:** A1 starter `ff1e93f60828ef2f94c9146522ce94075183b0ae`; A2–C1 starter provenance is recorded per original shortlist entry. The frozen shortlist itself is unchanged.

## Proposed safeguard and reviewer decisions
1. Do **not** introduce a blanket rule requiring literal headwords in examples: that would falsely reject legitimate plural, past tense and conjugated forms, and could degrade teaching quality.
2. Add a future advisory report that accepts an explicit inflection map (e.g., `hand→hands`, `manage→managed`, `grab→grabbed`), while failing closed on truly unexemplified words when preparing an **approved** release manifest. Require human review for ambiguous homographs and multiword expressions.
3. Ask independent English and fluent Myanmar reviewers to choose between original and proposed examples, check the example’s exact intended sense, and record reviewer identity, evidence and date. Proposed Myanmar renderings are drafts, not independently validated.
4. Source-supported CEFR labels for these exact senses remain **unverified**; do not infer CEFR from this audit. For final CEFR decisions, collect publisher URLs, exact sense/POS labels, access dates and independent reviewer signoff.
5. Final George/Emma audio must be regenerated only from the approved text, followed by actual listening signoff. No audio was generated or listened to for this audit.

## Release status
First-pass shortlist: A1 200, A2 200, B1 200, B2 200, C1 200. Independently approved: **0 at every level**. All editorial holds remain. No independent source-backed CEFR review, full approved audio/listening, browser/mobile regression, physical iPhone Safari evidence, hosting signoff or confirmed production deployment is established by this report. CI outcomes for this report commit are not yet verified. **Do not merge, publish, change main or touch production assets.**
