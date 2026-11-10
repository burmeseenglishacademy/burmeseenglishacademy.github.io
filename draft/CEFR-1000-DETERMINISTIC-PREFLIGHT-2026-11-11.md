# CEFR-1000 deterministic shortlist preflight — 2026-11-11

**Status:** staging-only; NOT a release approval, independent review, publisher CEFR check, or human listening test.

## Input provenance

- Repository: `burmeseenglishacademy/burmeseenglishacademy.github.io`; branch: `cefr-5000-bilingual-qa-staging`.
- Input: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; Git blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Observed on 2026-11-11 (Singapore date), by direct GitHub connector read.
- Scope is the user-approved 1,000, not the retired 5,000 plan.

## Machine observations (not editorial verification)

| Level | Provisional entries | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

- Exact lowercased headword collisions across all levels: **0**. This is a surface-form test only; it cannot validate sense deduplication.
- Entries requiring manual inspection under conservative literal headword/example heuristic: **41**. Inflected forms, pronouns, articles and other grammatical variation can trigger false positives.
- Approval flags remain untouched; metadata says all 1,000 on editorial hold.

## Sample manual editorial triage (proposals, not approvals)

1. **A1 `i` (pronoun)**: Headword is lowercase in machine data but conventional English standalone pronoun is capital **I**. Normalize learner display, audio text and search key separately; require independent English review before changing release manifest. Current example: “I am a student.”
2. **A2 `maybe` (adverb)**: Current Myanmar `ဖြစ်နိုင်သည်၊ ဖြစ်ကောင်းဖြစ်မည်` is closer to finite predicate/modal phrasing than a discourse adverb in some contexts. Independently review whether `ဖြစ်ကောင်းဖြစ်နိုင်တယ်` or `ဖြစ်နိုင်တာပေါ့` is natural for the particular sentence; do not apply mechanically.
3. **B1 `doubt` (noun)**: “I have some doubt about the figures.” is possible but may sound less idiomatic than “I have doubts about the figures.” A change to plural requires matching the noun sense and teaching note.
4. **B2 `portion` (noun)**: Current definition includes general part/amount, while example concerns a serving of rice. Require sense-specific food-serving gloss and publisher CEFR evidence for that exact sense, not the general part sense.
5. **C1 `integrity` (noun)**: Current example concerns moral honesty; distinguish from structural/data integrity. Any publisher CEFR claim must explicitly match moral sense, not another noun sense.

## Follow-up machine-flag queue

- A1 `i`: case-sensitive display form: I, not i
- A1 `mother`: short definition manual clarity check
- A1 `father`: short definition manual clarity check
- A1 `or`: short definition manual clarity check
- A1 `me`: short definition manual clarity check
- A1 `one`: short definition manual clarity check
- A1 `people`: short definition manual clarity check
- A1 `two`: short definition manual clarity check
- A1 `here`: short definition manual clarity check
- A1 `man`: short definition manual clarity check
- A1 `little`: short definition manual clarity check
- A1 `three`: short definition manual clarity check
- A1 `small`: short definition manual clarity check
- A1 `big`: short definition manual clarity check
- A1 `happy`: short definition manual clarity check
- A1 `girl`: short definition manual clarity check
- A1 `boy`: short definition manual clarity check
- A1 `woman`: short definition manual clarity check
- A1 `four`: short definition manual clarity check
- A1 `five`: short definition manual clarity check
- A1 `six`: short definition manual clarity check
- A1 `seven`: short definition manual clarity check
- A1 `eight`: short definition manual clarity check
- A1 `nine`: short definition manual clarity check
- A1 `ten`: short definition manual clarity check
- A1 `today`: short definition manual clarity check
- A1 `tomorrow`: short definition manual clarity check
- A1 `yesterday`: short definition manual clarity check
- A1 `week`: short definition manual clarity check
- A1 `brother`: short definition manual clarity check
- A1 `sister`: short definition manual clarity check
- A1 `wake`: short definition manual clarity check
- A1 `speak`: short definition manual clarity check
- A2 `large`: short definition manual clarity check
- B1 `easily`: short definition manual clarity check

## Fail-closed release requirements

This preflight cannot satisfy any human or publisher evidence gate. Require 200 independently approved unique word/sense records at each level, external exact-sense CEFR evidence with source URL and observation date, independently checked English/Myanmar/example grammar, content-bound signoffs, 4,000 George/Emma headword/example audio files and genuine listening attestations, browser/mobile plus physical iPhone Safari evidence, current-HEAD CI job logs, GitHub Pages clearance, and post-launch asset integrity checks. Do not merge or publish while any gate is missing. Preserve existing 54 lessons, separate IELTS bank, production voices, and privacy protections.
