# CEFR-1000 A1 first-person pronoun orthography and audio-token risk — 2026-11-20

**Scope:** user-approved 1,000-total shortlist, staging only. **Finding:** one concrete A1 headword orthography defect requiring editorial correction before any approved manifest/audio generation. This is author research, not independent verification.

## Reproducible source provenance
Read the entire `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` from branch `cefr-5000-bilingual-qa-staging` on 2026-11-20, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, and filtered entries for `word === "i"` and uppercase-initial headwords. Exactly one lowercase standalone `i` headword was found, and no uppercase-initial headword was found. This is an orthography scan, **not** evidence that other entries are linguistically correct.

Affected record: A1, `word: "i"`, `part_of_speech: "pronoun"`, `source_path: "draft/A1-EDITORIAL-STARTER.json"`, `source_index: 3`, `source_blob_sha: ff1e93f60828ef2f94c9146522ce94075183b0ae`. Stored English definition: “The person who is speaking or writing.” Stored Myanmar meaning: “ကျွန်တော်၊ ကျွန်မ (မိမိကိုယ်ကို ရည်ညွှန်းသောစကား)”. Stored example: “I am a student.” The example uses correct uppercase `I`, unlike the headword.

## External source-backed finding
- Cambridge English Dictionary, [I, i / personal pronouns](https://dictionary.cambridge.org/us/dictionary/english/i?topic=personal-pronouns), observed 2026-11-20: the first-person subject pronoun is presented as `I` and contrasted with object form `me`; the listed usage examples use uppercase `I`. The dictionary page alone is not treated as independent CEFR-level attestation.
- Pearson English [Punctuation: Upper and lowercase letters](https://qualifications.pearson.com/content/dam/pdf/GCSE/English/raisingskills/block5/U4_04d_Booster%204.pdf), observed 2026-11-20: explicitly instructs that the first-person pronoun `I` is capitalised in every sentence position, including contractions. This supports correcting the *displayed headword* to `I`, without changing its provisional A1 assignment or claiming CEFR verification.

## Editorial and technical consequences
1. **Proposed correction, not applied:** display `I` as the canonical English headword; preserve case-insensitive matching only for search and duplicate detection. The `i` string is a different written form (letter or stylisation), not the ordinary first-person pronoun headword. Independently confirm the lexical identity, A1 level, English definition and Myanmar registers before changing the approved manifest.
2. For Myanmar learner clarity, the existing “ကျွန်တော်၊ ကျွန်မ” should be independently checked for speaker register and appropriate gender/context; do not collapse those alternatives into one compulsory form.
3. Audio-generation inputs must use the independently accepted canonical headword, not blindly pass the lowercase JSON token to George/Emma TTS. This audit generated **no audio** and performed **no listening**.
4. Future structural tests should flag a standalone `i` with `part_of_speech=pronoun`, while accepting lowercase letters in unrelated words and preserving deliberate branded spellings. A test must not silently uppercase arbitrary lexical items.
5. Keep exact 200-per-level counts, source-index provenance and distinct review tasks; if an editorial correction is approved, regenerate derived assets only in staging, require reviewer attestations and rerun parallel level checks. Case-folded deduplication must still treat `I` and `i` as one lexical collision candidate.

## Release gate status
Provisional first-pass entries: A1 200; A2 200; B1 200; B2 200; C1 200. Independently approved: 0 at every level. No independent English/Myanmar/example/CEFR signoff, no complete new George/Emma headword/example audio or actual listening signoff, no browser/mobile or physical iPhone Safari evidence, no GitHub Pages hosting clearance, and no confirmed production deployment. No shortlist, review flags, main, production lessons, IELTS bank, established audio or privacy files changed. Current-commit GitHub Actions job logs are **not** verified by this audit. **Remain staging only.**
