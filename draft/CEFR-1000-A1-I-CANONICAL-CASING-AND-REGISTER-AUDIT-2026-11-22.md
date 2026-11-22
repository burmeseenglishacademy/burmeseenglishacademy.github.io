# CEFR-1000 A1 pronoun “I”: canonical casing, bilingual register and fail-closed QA
Observed 2026-11-22. AUTHOR-ONLY investigation; **not** independent review or approval.

## Exact pinned inventory
- Provisional shortlist blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Independent-review tasks blob: `77abf35146825f05e3e58cfdd7a73b3c7302c967`.
- A1 source `draft/A1-EDITORIAL-STARTER.json`, index 3, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Task `CEFR1000-A1-0004`, pending independent review.
- Actual provisional headword: `i` (lowercase); POS pronoun. Definition: “The person who is speaking or writing.” Myanmar: “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”. Example: “I am a student.”

## Findings requiring human editorial adjudication
1. **Display-form mismatch.** In standard written English the first-person singular subject pronoun is `I`, capitalised even mid-sentence. The shortlist stores `i`, whereas its example uses `I`. A case-insensitive deduplication check is appropriate, but a **separate canonical display-form check** is needed; normalising every headword to lowercase for uniqueness must not be used as an excuse to publish `i` as the learner-facing spelling.
2. **Definition precision.** The current definition identifies the speaker/writer, but does not say the word is a *subject pronoun* (contrast `me`, `my`, `mine`). Candidate author-only English definition: “The subject pronoun a speaker or writer uses to refer to themselves.” Proposed original example: “I live in Yangon.” Contrast (not a candidate entry): “My brother called me.” Do not replace the record until independently checked.
3. **Myanmar register.** `ကျွန်တော်` and `ကျွန်မ` are common self-reference options, but Myanmar first-person choice depends on speaker, relationship, register and context; they are not interchangeable universal equivalents. Candidate explanatory note: “စကားပြောသူက မိမိကိုယ်ကို ရည်ညွှန်းသည့် ကတ္တားနာမ်စား။ အခြေအနေနှင့် ပြောဆိုပုံအလိုက် ‘ကျွန်တော်’၊ ‘ကျွန်မ’ စသည်ဖြင့် သုံးနိုင်သည်။” Require an independent fluent Myanmar reviewer to judge clarity, naturalness and classroom suitability.
4. **Pronunciation boundary.** Uppercase `I` and lowercase `i` must not silently produce different learner audio identities. Final George/Emma audio filenames and manifest keys should use a stable canonical identifier separate from the display spelling; check collision handling before regeneration. No audio was generated or listened to here.

## Source and CEFR evidence status
- Cambridge Learner's Dictionary lookup candidate: https://dictionary.cambridge.org/dictionary/learner-english/i
- British Council English grammar resource for pronouns (navigation candidate): https://learnenglish.britishcouncil.org/grammar/english-grammar-reference/personal-pronouns
- URLs are **research leads, not verified source observations in this run**; do not claim that either page explicitly assigns A1 to this exact sense. The current entry has empty `source_level` and `source_english` fields. An independent reviewer must inspect the precise subject-pronoun sense, capture the actual dictionary label and observation date, and decide whether the level is justified.

## Suggested regression cases (not executed)
- Reject final published display headword `i` when the intended pronoun is `I`; accept canonical `I` while preserving a case-folded duplicate key.
- Reject a final manifest containing both `I` and `i` as two entries, even across CEFR levels.
- Require reviewer signoff on canonical casing, English sense, Myanmar register, original example, exact-sense CEFR source, and pronunciation; author-only notes never count as reviewer attestations.
- Confirm headword and sentence George/Emma audio resolve after casing correction without overwriting established production audio.
- If a candidate is corrected, recompute all five 200-entry quotas, provenance, reviewer-task alignment and deduplication before authorising release.

## Release status
A1/A2/B1/B2/C1 each have 200 **provisional first-pass written entries**; independently checked/approved: **0/0/0/0/0**. No independent listening, physical iPhone Safari, hosting or production evidence is supplied by this audit. Keep all 1,000 on editorial hold; do not merge or publish.
