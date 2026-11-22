# CEFR-1000 B1 `weekend`: source-backed A1 conflict (author research; NOT independent review)

Observed: 2026-11-22 (Singapore date). Scope: **user-approved 1,000 TOTAL**, 200 each A1/A2/B1/B2/C1. Branch: `cefr-5000-bilingual-qa-staging`. No production release authorised by this document.

## Immutable staging record / provenance
- Review task: `CEFR1000-B1-0403`; status `PENDING_INDEPENDENT_REVIEW`, approval `false`, reviewer identity/signature absent.
- Provisional entry: `weekend`, B1, noun; English: “Saturday and Sunday, when many people do not work.”; Myanmar: “သီတင်းပတ်ကုန်”; example: “We visited our grandparents at the weekend.”
- Source: `draft/A2-C1-EDITORIAL-STARTER.json`, index 12, blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`.
- Shortlist `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; review tasks `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` blob `77abf35146825f05e3e58cfdd7a73b3c7302c967`.

## Direct dictionary observations (2026-11-22)
1. Cambridge Learner's Dictionary, https://dictionary.cambridge.org/us/dictionary/learner-english/weekend : noun [C], **A1** for Saturday/Sunday, when many people do not work. This is the same core sense as the provisional B1 definition.
2. Cambridge English Dictionary, https://dictionary.cambridge.org/us/dictionary/english/weekend : **A1** for the ordinary Saturday/Sunday (sometimes Friday evening–Sunday night) sense; separately lists weekend visits/holidays and regional prepositional patterns. Do not silently transfer A1 evidence to all derived uses.
3. Cambridge pronunciation reference, https://dictionary.cambridge.org/pronunciation/english/weekend : UK /ˌwiːkˈend/, US /ˈwiːk.end/. This is written reference evidence only, **not** evidence that George or Emma recordings were generated or listened to.

## Editorial analysis, not an approval
The provisional B1 placement conflicts with two explicit A1 labels for the *same noun sense*. A source-backed reviewer should adjudicate movement to A1, or document another distinct B1 sense with direct level evidence. Never simply relabel the existing entry: A1 already contains 200 provisional items and migration requires a balanced replacement, global sense-level deduplication, preserved task provenance and independent signoff.

- English candidate: “Saturday and Sunday, the two days at the end of the week when many people have time off work or school.” This is author-proposed wording, not a quotation or reviewer-approved final text.
- Myanmar candidate: “စနေ၊ တနင်္ဂနွေ နှစ်ရက်ပါဝင်သော သီတင်းပတ်ကုန်” (retain natural short display meaning “သီတင်းပတ်ကုန်” where appropriate). Myanmar fluency and contextual accuracy require an independent Myanmar-language reviewer.
- Original example candidate: “We usually visit our grandparents at the weekend.” Myanmar candidate: “သီတင်းပတ်ကုန်မှာ အဘိုးအဘွားတွေဆီ ကျွန်တော်တို့ ပုံမှန် သွားလည်တတ်ကြတယ်။” These are newly authored candidates; independent grammar, register, translation and originality checks remain pending.
- The existing “at the weekend” example is normal British English; “on the weekend” is a common US counterpart. Do not flag the existing British example as an error.
- A1 source level is a dictionary classification of the sense, not an independently reviewed decision for this curriculum.

## Mandatory next checks / fail-closed
1. Independent reviewer verifies the dictionary sense/CEFR label and source access date, English and Myanmar wording, original example, part of speech and pronunciation. Record external reviewer identity and verifiable attestation outside author self-evaluation.
2. Check whether `weekend` or its equivalent sense is already present elsewhere, including variant headwords, and plan a balanced 200-for-200 level swap if adjudicated.
3. Do not update `reviewed_*`, `approval`, release manifest or public data based on this research note.
4. Preserve all 54 lessons, separate IELTS bank, existing George/Emma production assets and privacy policy. No audio or iPhone listening claims.
5. Current evidence status: five levels contain 200 provisional written records each; independently approved 0/200 in each. Final shortlist audio (2 voices × headword/example × 1,000 = 4,000 recordings) and listening signoff unverified; browser/mobile, physical iPhone Safari, GitHub Pages hosting and deployment gates unverified. Stay on staging.
