# CEFR-1000 exact-sense and example audit — 2026-11-05

**Scope:** user-approved 1,000 total, not historical 5,000. Staging only. Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, read 2026-11-05. This is an **internal editorial triage**, not independent review, not external CEFR verification. No publisher CEFR source was newly consulted in this pass; do not treat suggested level placements as confirmed.

## Inventory and release posture
| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1000** | **0** |

All 1,000 remain on editorial hold. The following are candidate changes for a qualified independent reviewer to evaluate against **exact senses** and independent dated publisher evidence, not edits to the frozen manifest.

## Concrete entries and reviewer decisions

1. **A1 `i` (pronoun; source index 3).** The stored lowercase headword conflicts with standard English orthography; the original example is correctly capitalised: “I am a student.” Candidate canonical headword: **I**. Myanmar `ကျွန်တော်၊ ကျွန်မ` is appropriate as speaker-dependent alternatives; review inclusive/contextual rendering. Avoid applying a blanket title-case transformation to `a` and `an`. Obtain independently verified CEFR evidence for the pronoun sense.
2. **A2 `better` (adjective; source index 86).** Definition “Of a higher quality or more suitable than something else” and example “The second plan is better for our budget” are coherent. But record explicit comparative relation `good → better` and independently determine whether teaching the irregular comparative as a distinct headword/sense is allowed; do not silently deduplicate by spelling or lemma.
3. **A2 `thought` (noun; source index 506).** The example “One thought kept me awake last night” illustrates an idea, while the same surface form is the past tense of `think`. Preserve noun POS and verify source CEFR for noun rather than verb; candidate Myanmar `အတွေး၊ စိတ်ကူး` is context-dependent.
4. **A2 `training` (noun; source index 603).** “New workers receive safety training” uses an uncountable activity noun; distinguish from the present participle of `train`. Candidate Myanmar `လေ့ကျင့်သင်ကြားမှု` needs a natural workplace-context check; potential alternative `သင်တန်းပေးခြင်း` changes emphasis and should not be adopted automatically.
5. **A2 `likely` (adjective; source index 833).** “It is likely to rain before evening” demonstrates the `be likely to + infinitive` construction. Independently check this grammatical pattern and CEFR sense, not merely the unqualified lemma. Candidate Myanmar `ဖြစ်နိုင်ခြေများသော` needs review for natural phrasing in the full sentence.
6. **A2 `fine` (adjective; source index 864).** Definition “Good enough or acceptable in quality” is not unequivocally demonstrated by “The weather was fine for our picnic,” which can mean pleasant weather rather than merely acceptable quality. Candidate replacement: “This plan is fine for now, but we may improve it later.” Reviewer must select one intended sense, align English definition/Myanmar gloss/example and source-backed level.
7. **B1 `civil` (adjective; source index 51).** Definition “Connected with ordinary citizens rather than the military” versus “The group works to protect civil rights” is a **sense mismatch risk**: `civil rights` is a fixed rights-related collocation, not a transparent military/civilian contrast. Candidate example: “The military handed control to a civil government.” This may still require a `civilian` versus `civil` usage check. Earlier staging publisher research reports Cambridge C1 for an ordinary/non-military sense; re-open exact entry and date/source before asserting level. **Do not approve B1** based on generic word familiarity.
8. **B1 `worst` (adjective; source index 57).** “That was the worst storm of the year” supports a superlative sense, but link irregular comparison `bad → worse → worst`; independently review separate-lemma policy and pronunciation, without conflating `worst` with the noun.
9. **B2 `conduct` (verb; source index 250).** “The team will conduct a safety inspection” matches organise/carry out. Preserve verb stress/pronunciation distinct from noun `conduct`; earlier staging Cambridge research supports B2 only for this activity sense, not the reflexive verb or noun. Obtain exact dated source citation and independently check.
10. **C1 `permit` (noun; source index 569).** “The contractor applied for a permit before starting work” matches official authorisation document; noun pronunciation/stress differs from verb `permit`. Independently confirm noun-sense CEFR, not verb or generic permission; Myanmar `တရားဝင်ခွင့်ပြုချက်လက်မှတ်` may be verbose and needs native-speaker review.

## Fail-closed regression proposals
- Canonical orthography and POS-sensitive identity must be checked against reviewer-approved sense records, with a targeted first-person `I` rule; avoid false positives for articles.
- A sense record must bind immutable source URL, observation date, quoted/paraphrased sense identifier, publisher level evidence, reviewer identity/time, Myanmar and English review, example review, and pronunciation review. Missing or conflicting data must block approval.
- Morphological relations and homographs must be explicit reviewer-resolved metadata, not automatically collapsed or silently allowed. Include `thought` noun/verb, `training` noun/verb, `better` comparative, `worst` superlative, `conduct` noun/verb, `permit` noun/verb.
- Before release, require exactly 200 **independently approved** non-duplicate headword/sense records per level, 4,000 manifest-matched British George/Emma audio assets (headword + example per voice), actual human listening signoff, browser/mobile regression, physical iPhone Safari evidence, hosting checks, deployment verification, and production-asset preservation. A green structural CI run is not linguistic approval.

## Outstanding evidence
Independent English, Myanmar, example, CEFR-source and pronunciation review: **0/1,000**. Final George/Emma audio generated/listened: **not verified**. Physical iPhone Safari: **not verified**. Browser/mobile, Pages hosting and live deployment: **not verified**. No new CI run/job conclusion was verified for this document. No production files or approvals changed.
