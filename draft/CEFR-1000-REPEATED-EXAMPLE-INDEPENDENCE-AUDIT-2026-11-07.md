# CEFR-1000 repeated-example independence audit — 2026-11-07

Status: editorial research only; **no independent signoff or CEFR publisher validation**. Branch: `cefr-5000-bilingual-qa-staging`. Inventory blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Analysis date: 2026-11-07 (Singapore).

## Reproducible finding
Parsed 1,000 provisional entries; grouped example sentences after Unicode NFKC normalization, English lowercase, outer trim and internal whitespace collapse. Found **3 repeated sentence groups involving 7 entries**. This is not a claim of plagiarism or grammar error. All groups are A1. Unique sentence strings: 996.

### Group 1: “The book is on the table.”

- **the** (A1, article): Used to refer to a particular person or thing. | Myanmar: အတိအကျသတ်မှတ်ထားသော အရာကို ညွှန်းသည့်စကား | provenance: `draft/A1-EDITORIAL-STARTER.json` index 6, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`
- **table** (A1, noun): A piece of furniture with a flat top and legs. | Myanmar: စားပွဲ | provenance: `draft/A1-EDITORIAL-STARTER.json` index 94, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`

Editorial risk: shared examples are grammatical, but independent example review must confirm that the intended sense and target word are sufficiently salient for **each** entry. Do not auto-reject a repeated sentence; require an explicit example-specific reviewer decision.

### Group 2: “What is your name?”

- **your** (A1, determiner): Belonging to the person being spoken to. | Myanmar: သင့်၊ မင်းရဲ့ | provenance: `draft/A1-EDITORIAL-STARTER.json` index 13, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`
- **name** (A1, noun): A word or words used to identify someone. | Myanmar: အမည်၊ နာမည် | provenance: `draft/A1-EDITORIAL-STARTER.json` index 78, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`
- **what** (A1, question word): Used to ask about a thing or information. | Myanmar: ဘာ၊ ဘယ်အရာ | provenance: `draft/A1-EDITORIAL-STARTER.json` index 116, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`

Editorial risk: shared examples are grammatical, but independent example review must confirm that the intended sense and target word are sufficiently salient for **each** entry. Do not auto-reject a repeated sentence; require an explicit example-specific reviewer decision.

### Group 3: “Please sit here.”

- **here** (A1, adverb): In this place. | Myanmar: ဒီမှာ၊ ဤနေရာတွင် | provenance: `draft/A1-EDITORIAL-STARTER.json` index 51, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`
- **sit** (A1, verb): To rest with your body supported by a chair or the ground. | Myanmar: ထိုင်သည် | provenance: `draft/A1-EDITORIAL-STARTER.json` index 197, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`

Editorial risk: shared examples are grammatical, but independent example review must confirm that the intended sense and target word are sufficiently salient for **each** entry. Do not auto-reject a repeated sentence; require an explicit example-specific reviewer decision.

## Suggested independent-review handoff

For `the` and `table`, verify article definiteness and furniture meaning separately. For `your`, `name`, and `what`, verify possessive determiner, noun, and interrogative use separately. For `here` and `sit`, verify locative adverb and imperative verb separately. Where distinct examples would improve instruction, propose original examples and obtain independent English/Myanmar review before replacing inventory text.

## Release-safety implications

A fail-closed validator should require a signed, entry-specific review for English definition, Myanmar meaning, example grammar/semantic fit, CEFR sense with observed source URL and date, and pronunciation. Duplicate example strings should generate an advisory review queue, **not** be equated with duplicate headwords or automatically approved. The provisional 1,000 must remain on hold: A1/A2/B1/B2/C1 = 200/200/200/200/200 written first-pass, independently checked = 0/0/0/0/0. Audio generation/listening, physical iPhone Safari evidence, browser/mobile regression, hosting and production gates are not established by this audit.

No changes to provisional inventory, review flags, production files, audio, main branch or release state.