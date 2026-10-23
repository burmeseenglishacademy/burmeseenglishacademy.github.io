# A2–C1 CEFR Vocabulary — QA checkpoint, 24 October 2026 (SGT)

**State: STAGING ONLY. Not content-approved, audio-complete or live.**

## Candidate inventory and original editorial drafting

- A2: **700** provisional headword candidates.
- B1: **1,000** provisional headword candidates.
- B2: **1,300** provisional headword candidates.
- C1: **1,500** provisional headword candidates.
- Combined A2–C1: **4,500** unique candidate headwords; the curricular frequency-derived CEFR assignment is **not** an authoritative dictionary-level claim.
- `tools/build_cefr_a2_c1_review_packets.py` prepares **45 batches of 100 entries each** and incorporates previously authored editorial starters rather than discarding progress.
- `draft/A2-C1-EDITORIAL-STARTER.json` currently contains **40 original AI-assisted bilingual first drafts (10 per level)**, with an English definition, Myanmar draft gloss, POS and original example each. These are **unverified**, intentionally have no independent reference URLs and have all five reviewer flags false. **4,460 entries** still lack original first drafts.
- No A2–C1 entry has completed an independently corroborated sense, Myanmar translation, example, CEFR placement or pronunciation review. Some candidate words are proper names, colloquial forms or markedly lower CEFR levels and require editorial rejection/reclassification rather than copying rank-based placement.

## Actual GitHub Actions evidence

- [A2–C1 4,500-word batch preparation, run 40001586180](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40001586180): **success** for blank review packets and full candidate counts.
- [A2–C1 first 40 original draft checks, run 40002167269](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40002167269): **success** for draft content structure and candidate-level alignment only; no independent translation review.
- [A2–C1 progress-preserving packet QA, run 40002356521](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40002356521): **success** across all 45 batches and original draft preservation.
- The intermediate packet run 40002314091 **failed** because the older test wrongly demanded every English and Burmese draft field remain empty after new drafts existed. The subsequent workflow update fixed that test and run 40002356521 passed. Do not conflate this fixed regression with bilingual approval.

## Remaining tasks and release conditions

- Write original English learner explanations, Burmese sense-appropriate translations and illustrative examples for remaining **4,460 A2–C1 entries**, rejecting or reclassifying unsuitable candidates.
- Independently verify **all 4,500** entries' meanings, source references, POS, usage examples and **sense-specific CEFR placements**; also finish the separate **500 A1** review.
- Once text is reviewed/frozen, generate and verify both British George and Emma audio for each word and each example; MP3 decoding alone is insufficient for pronunciation accuracy.
- Measure site storage and bandwidth, perform final content/security/regression checks, test a physical iPhone Safari device, and deploy only when the complete fail-closed release gate passes.
- The existing `main` v1.2.5 website and its 54 lessons, IELTS 1,000 words and legacy audio have **not** been modified by this staged work.

**No full completion, production release or notification of project completion is supported by these tests.**
