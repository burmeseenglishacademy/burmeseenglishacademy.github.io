# CEFR-1000 inflected-example audit — 2026-11-06

**Scope:** staging-only, user-approved 1,000 total (200 each A1/A2/B1/B2/C1). Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, branch `cefr-5000-bilingual-qa-staging`, inspected at commit `28dc03677533d6f660b0d423590c013d061706cc`. This is an automated literal-token screen followed by editorial triage, **not independent review**. No publisher CEFR evidence was collected in this audit.

## Method and result

All 1,000 provisional entries were parsed. The screen looked for the literal headword as a whole case-insensitive alphabetic token within its example sentence. **995/1,000** passed literal-token presence; **5/1,000** did not. A literal mismatch is not proof of an incorrect example: plural and past-tense forms are valid pedagogical uses. No entries or signoff flags were changed.

| Level | Headword | Provisional example | Why literal matching fails | Editorial disposition |
|---|---|---|---|---|
| A1 | hand | Please wash your hands. | regular plural `hands` | Plausible; verify the singular/plural meaning and beginner suitability independently |
| A1 | eye | I have two eyes. | regular plural `eyes` | Plausible; independently check natural Myanmar example translation |
| B2 | manage | We managed to finish the work before the deadline. | past tense `managed` | Plausible sense 'succeed in doing'; check whether CEFR publisher labels this *sense*, not general management |
| B2 | destroy | The fire destroyed the old warehouse. | past tense `destroyed` | Plausible; check British pronunciation, example naturalness, Myanmar accuracy and publisher level |
| B2 | grab | She grabbed her bag and ran outside. | doubled-consonant past tense `grabbed` | Plausible; check intended sudden/quick action sense and publisher level |

## Traceable provisional source records

- `hand` A1: `draft/A1-EDITORIAL-STARTER.json` index 172, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`; English: “The part of the body at the end of the arm.” Myanmar: “လက်”.
- `eye` A1: same source index 173, same blob; English: “The part of the body used for seeing.” Myanmar: “မျက်လုံး”.
- `manage` B2: `draft/A2-C1-EDITORIAL-STARTER.json` index 101, blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`; English: “To succeed in doing something difficult.” Myanmar: “အခက်အခဲရှိသော်လည်း အောင်မြင်စွာ လုပ်နိုင်သည်”.
- `destroy` B2: same source index 253, same blob; English: “To damage something so badly that it no longer exists or works.” Myanmar: “ဖျက်ဆီးသည်”.
- `grab` B2: same source index 256, same blob; English: “To take hold of something suddenly or quickly.” Myanmar: “အလျင်အမြန်ဆုပ်ကိုင်သည်”.

## Safeguard recommendation

Do **not** fail an example solely because the uninflected headword is absent. Instead, store a reviewed target-token span and its lemma/morphological analysis (e.g. `grabbed → grab, past tense`) alongside a separately reviewed sense ID. A future validator should fail closed when the span, lemma, grammatical category, target sense, or independent reviewer evidence is missing, rather than auto-approving a match based on suffix heuristics. Require a human independent check of English, fluent Myanmar, example grammar, exact-sense publisher URL and observation date before approval.

## Release status

Written first-pass: A1 200, A2 200, B1 200, B2 200, C1 200. Independently approved: **0 per level**. Final George/Emma headword/example audio generation and real listening signoff: **unverified/incomplete**. Browser/mobile regression, physical iPhone Safari, GitHub Pages hosting gate, and production deployment: **not evidenced**. Protect the existing 54 lessons, separate IELTS 1,000 bank, production audio and privacy. **Staging only; do not merge or publish.**
