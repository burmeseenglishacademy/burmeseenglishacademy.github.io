# BEA A2–C1 bilingual vocabulary progress checkpoint — 24 October 2026 (SGT)

**Status: STAGING / DRAFT ONLY. Full completion and learner release are NOT verified.** Do not merge unverified CEFR vocabulary or incomplete audio into `main`.

## Changes actually made

- Extended `draft/A2-C1-EDITORIAL-STARTER.json` from **120 to 160 original first-draft bilingual entries**, exactly **40 drafts per provisional level** (A2/B1/B2/C1), with English learner definitions, Burmese meaning drafts, and original example sentences. All are AI-assisted **editorial drafts** with English sense, Burmese translation, grammatical accuracy, CEFR assignment and pronunciation **independently unapproved**.
- Expanded `draft/A2-C1-SOURCE-EVIDENCE-REVIEW.json` to **17** word-specific Cambridge observations, all provisional and unapproved. New pages observed for `state`, `marriage`, `constantly`, `municipal`. The **state** draft is provisionally A2 but the cited US-state/regional-government noun sense is **B1** in Cambridge. This is a flagged conflict, not an approved level. Total flagged conflicts across 17 records: **7**.
- Added `tools/list_cefr_next_candidates.py` and GitHub Actions `cefr-preview-next.yml` for read-only next-candidate discovery. **Important discovery:** the frequency + first WordNet sense list includes poor sense matching and named entities, e.g. `it's` with an IT sense, `let` with an acronym sense and personal names. Do **not** auto-publish this pool or infer its assigned CEFR levels are accurate.
- Added `tools/triage_cefr_candidate_quality.py` and `cefr-candidate-triage.yml` to prioritize review. [CI run 40051938346](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40051938346) **success**: flagged **1,990/4,500** A2–C1 candidates for at least one **heuristic** issue, including 7 documented CEFR-source conflicts, 38 contraction flags, 12 likely named entities, 611 morphological-form flags, 10 known first-sense/register risks, 121 short/function-word flags, and all 1,500 C1 entries for a high-frequency level recheck (some multiple flags). Unflagged words are also unverified. Artifact: `CEFR-A2-C1-UNVERIFIED-CANDIDATE-TRIAGE` (ID 12542859605).
- [Bilingual structural/source regression 40051876599](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40051876599) **success** on the new 160-entry / 17-source staging state.
- [45 unpublished 100-word editorial work packets 40051876600](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40051876600) **success**: **4,500** provisional A2–C1 entries in review queues, preserving the 160 bilingual first drafts. These are NOT 4,500 translated or verified entries.

## Release blockers, not yet done

- A2: **40/700 initial drafts**; B1: **40/1,000**; B2: **40/1,300**; C1: **40/1,500**. **0 independently approved**.
- Remaining original first drafts needed: **4,340**. New word-level source/CEFR evidence and second-pass English/Burmese editorial review remain necessary on all headwords.
- George and Emma recordings for the new vocabulary and example sentences remain incomplete, along with individual pronunciation listening and full MP3/manifest coverage.
- Physical iPhone Safari check, full real-device accessibility checks, live deployment and live production verification for CEFR expansions remain incomplete.
- The original website in `main` remains **v1.2.5** at `dca0db7aa30118ecc18350db8dc406e6cac91554`. It retains the existing 54 lessons, separate 1,000 IELTS word bank and existing audio library. `main` was **not modified** in this iteration.

## Editorial safeguards

- These draft words are expressly marked `UNVERIFIED_DRAFT_DO_NOT_PUBLISH`; `reviewed_english`, `reviewed_burmese`, `reviewed_example`, `reviewed_level`, and `reviewed_pronunciation` remain `false`.
- Dictionary observations do not independently verify Burmese translations or settle sense-specific CEFR labels.
- Automated structural tests do not substitute for human listening, detailed independent translation review, or real iPhone testing.
- No completion notification or release claim is warranted yet.

**Only issue a completion notice after independent full 5,000-word content approval, complete British George/Emma audio coverage and listening QA, browser and physical mobile verification, a successful production deployment, and live QA.**
