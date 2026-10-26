# Burmese English Academy — batch50 high-throughput staging report

**Date:** 2026-10-26 (Singapore time)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release status:** **UNVERIFIED — STAGING ONLY — DO NOT MERGE OR DEPLOY**

## Original bilingual drafting completed
- **45** original English-definition + natural Myanmar first-pass gloss + original-example drafts: **A2 1, B1 5, B2 9, C1 30**. Drafts retain their source-pool part of speech; **none** has a verified CEFR tier, dictionary sense, Myanmar editorial approval, or pronunciation approval.
- **45** separate independent review-task packets, with distinct English dictionary sense/POS, fluent Myanmar translation, example grammar/collocation, sense-specific CEFR and George/Emma listening + physical iPhone Safari tasks. Cambridge dictionary links are **unvisited lookup leads**, not observations.
- **15** reversible heuristic candidate holds: A2 5, B1 4, B2 4, C1 2. These are primarily single-letter/chemical symbols, contractions and ambiguous abbreviations; **no** held candidate was counted as a drafted word.
- Structural auditor and parallel A2/B1/B2/C1/ALL no-deploy GitHub Actions workflow were added. The ALL check recursively counts historical drafts, checks duplicate exclusions and quarantine disjointness, confirms every approval flag is false, and compares protected production assets to `main`.

## Exact unique first-pass inventory

| Provisional tier | Target | Written unique first-pass drafts | Independently checked/approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 534 | 0 | 166 |
| B1 | 1,000 | 778 | 0 | 222 |
| B2 | 1,300 | 927 | 0 | 373 |
| C1 | 1,500 | 699 | 0 | 801 |
| **Total** | **5,000** | **3,438** | **0** | **1,562** |

- A2–C1 unique written: **2,938**; earlier historical duplicate draft records: **182** (not counted twice).
- Reversible quarantined headwords: **1,109**; no overlap with drafted headwords. This is a hold count, **not** a count of independently rejected words.
- All **5,000** source-pool headwords remain **provisional**; their WordNet first-sense clues are not reliable CEFR approvals.
- No audio generated or listened to during this batch. George/Emma collection completion, pronunciation validation and iPhone Safari real-device tests **not established**.

## Actual GitHub commits and CI evidence
- Atomic five-file content/QA commit: `7951daa72c7941cfff6d287d5317206024337b43` (45 drafts, 45 tasks, 15 holds, Python auditor and workflow).
- QA correction commit: `3711f1ad3500163d25527e1cc0eaf1f0d5aab1ea` (chain ALL recursive checks through batch49 instead of skipping it).
- GitHub Actions run `40262128837` on initial commit `7951daa7`: **completed/success**, five jobs successful; ALL log includes `A1-C1 written=3438; outstanding=1562; quarantine=1109` and `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged`.
- GitHub Actions run `40262146877` on corrected commit `3711f1ad`: **completed/success**, started 2026-10-26T03:03:25Z, finished 2026-10-26T03:03:38Z; inspected actual jobs and ALL job log. [Inspect corrected run](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40262146877).
- unpublished-structural-review (ALL): **completed / success**, job `121376608768`.
- unpublished-structural-review (A2): **completed / success**, job `121376608878`.
- unpublished-structural-review (B1): **completed / success**, job `121376608889`.
- unpublished-structural-review (B2): **completed / success**, job `121376608932`.
- unpublished-structural-review (C1): **completed / success**, job `121376608993`.
- Corrected ALL job log explicitly contains `STAGING ONLY batch49 ALL PASS: 40 drafts, 15 holds, zero approvals; no audio/deploy`, then `A1=500; A1-C1 written=3438; outstanding=1562; quarantine=1109; historical duplicate rows excluded=182`, then `STAGING ONLY batch50 ALL PASS: 45 drafts, 15 holds, zero approvals; no audio/deploy` and `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged`.
- **Green CI means structural correctness only**: schema, source-pool POS, text presence, example surface form, review-flag integrity, duplicate/quarantine accounting and production-asset drift. It is **not** independent English/Myanmar linguistic, graded CEFR, pronunciation, browser or iPhone certification.

## Specific editorial review blockers
1. **Sense-specific CEFR re-tier is urgent:** many source-pool C1 assignments appear substantially too advanced for common senses (e.g. `forecast`, `approve`, `predict`, `sketch`, `supportive`, `temporarily`), while A2 `minister` (religious office), B1 `premier` (government head), and B2 `alien` (legal immigration term) may also be mis-tiered. These are unverified draft levels, **not** claims of source-supported C1/A2/B1/B2.
2. **Part of speech / morphology:** B2 gerund nouns (`focusing`, `printing`, `feeding`, `editing`, `counting`, `traveling`) require independent lemma-policy and dictionary-entry decisions. C1 `judging` likewise requires a nominal sense check.
3. **Usage/register:** B1 political `conservative`/`liberal`, B2 `alien` and `lover`, C1 `bust`, `foul`, `ignorant` and `blessing` need context, register, and potential ambiguity checks before any approval. `meantime` example uses the fixed phrase `in the meantime`, which should be explicitly checked against the nominal sense.
4. **Independent evidence still absent:** no direct learner-dictionary pages were inspected for this batch, no independent fluent Myanmar reviewer signed off, and no sense-specific graded CEFR source was attached. Review URLs are not evidence of observation.
5. **Remaining 1,562 entries** lack original drafts; much of the unheld source pool contains misleading first WordNet senses, names, abbreviations or lower-level words. Replace or re-tier weak candidates rather than fill quotas.
6. **Release gate not satisfied:** full George/Emma audio generation and real listening, mobile/browser regressions, physical iPhone Safari testing, hosting storage/bandwidth assessment, and confirmed live deployment remain incomplete or unverified. `cefr-vocabulary-data.js` still contains `entries:[]` in staging.
7. **Production preservation:** `main` commit `dca0db7aa30118ecc18350db8dc406e6cac91554` was inspected and not modified by batch50. Existing 54 lessons, IELTS 1,000 bank, George/Emma production audio and privacy assets remain protected by CI drift checks.

**Next useful iteration:** expand with only semantically clear headwords; prioritize source-backed CEFR re-tier and source-observation tasks, independently review fluent Myanmar, and keep unpublished drafts isolated. Do not merge or notify completion until the entire 5,000-entry and audio/device/hosting/live release gate is met.
