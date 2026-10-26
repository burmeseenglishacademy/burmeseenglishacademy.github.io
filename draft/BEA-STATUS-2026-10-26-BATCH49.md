# Burmese English Academy — batch49 high-throughput staging report
**Date:** 2026-10-26, Singapore time  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release status:** **UNVERIFIED — STAGING ONLY — DO NOT MERGE OR DEPLOY**

## Substantive changes
- Created **40 original bilingual first-pass drafts**: A2 **4**, B1 **8**, B2 **12**, C1 **16**. Each has a separately identified English definition, Myanmar gloss and original usage example. All source fields and independent approval flags remain empty/false.
- Created **40 independent review packets** with separate English sense/POS, natural Myanmar, example grammar, sense-specific CEFR and George/Emma real-listening tasks. Cambridge dictionary links are **unvisited lookup leads**, not source observations or approvals.
- Added **15 reversible quarantines**: A2 **5**, B1 **4**, B2 **3**, C1 **3**. These cover contractions misread as headwords, WordNet wrong first senses, proper-name ambiguities, abbreviation policy, misleading part of speech and unsupported provisional levels. Holds are not final rejections.
- Added a staging-only Python structural auditor and five parallel A2/B1/B2/C1/ALL GitHub Actions jobs, with no publish/deploy step. The ALL job also recursively audits earlier batches and compares protected production assets against `main`.
- **Editorial warning:** Some candidate-tier assignments are very likely too high or too low, e.g. A2 `nobody` (pejorative sense), B1 `appropriate` (budget allocation), B2 `moderate` (political noun), C1 `creativity`, `adequate` and `surgical`. They are **not approved CEFR labels**. The `bout` draft offers two senses in one definition and needs a single-sense rewrite before any approval. The `passive` grammar and `intermediate` chemistry senses require specialised learner evidence. No fabricated evidence was attached.

## Exact unique draft inventory (historical duplicate records excluded)
| Provisional tier | Target | Written first-pass drafts | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 533 | 0 | 167 |
| B1 | 1,000 | 773 | 0 | 227 |
| B2 | 1,300 | 918 | 0 | 382 |
| C1 | 1,500 | 669 | 0 | 831 |
| **TOTAL** | **5,000** | **3,393** | **0** | **1,607** |

- Unique A2–C1 written drafts: **2,893**. Historical repeated rows across batches: **182**, excluded from the unique count.
- Reversible quarantined candidate headwords: **1,094**. No held headword overlaps a written draft.
- Independent English/Myanmar/sense/CEFR/example approval: **0 / 5,000**. Pronunciation listening approvals: **not established**; no new audio was generated or independently listened to during this batch.
- The candidate pool's 5,000 headwords and WordNet clues are **not** 5,000 publishable graded entries.

## GitHub commit, actual CI run and log evidence
- Atomic staging content + QA commit: `6fcc54967b39f578fcfd52f0a06d67a83fa887eb` (5 new files: editorial drafts, review tasks, quarantine, Python auditor, Actions workflow).
- GitHub Actions run **40258687436**, commit `6fcc549...`, created **2026-10-26 02:21:22 UTC**, **completed / success** at **02:21:34 UTC**: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40258687436
- Inspected actual job status and steps, not inferred from a workflow definition:
  - A2 job `121366049969`: **completed / success**.
  - B1 job `121366049940`: **completed / success**.
  - B2 job `121366049920`: **completed / success**.
  - C1 job `121366049781`: **completed / success**.
  - ALL job `121366050039`: **completed / success**, including the production asset drift check.
- Inspected actual ALL job log: `UNIQUE A2-C1 {'A2': 533, 'B1': 773, 'B2': 918, 'C1': 669} total=2893; independently approved=0`; `A1=500; A1-C1 written=3393; outstanding=1607; quarantine=1094; historical duplicate rows excluded=182`; `STAGING ONLY batch49 ALL PASS: 40 drafts, 15 holds, zero approvals; no audio/deploy`; `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged`.
- **Meaning of green CI:** syntactic, schema, inventory, duplicate/quarantine, flag and protected-file drift checks only. It does **not** independently verify dictionary senses, fluent Myanmar, grammar, CEFR evidence, or audio.

## Release and review blockers
1. **1,607** entries still lack first-pass drafts. The remaining unheld pool contains a high proportion of weak candidates, including abbreviations, names and wrong first WordNet senses; do not pad batches with them.
2. **0** entries have complete independent source-based sense, Myanmar, grammar, CEFR and example sign-off. Review packet URLs have not been inspected and must not be represented as observed source evidence.
3. New George/Emma full pronunciation collection generation, per-file listening validation, and audio coverage remain **incomplete/unverified**.
4. Final corpus browser/mobile regression, **real physical iPhone Safari acceptance**, actual hosting size/bandwidth compliance and live production deployment remain **incomplete/unverified**.
5. Staging `cefr-vocabulary-data.js` still contains `entries:[]`. `main` remains at `dca0db7aa30118ecc18350db8dc406e6cac91554`; production's 54 lessons, IELTS 1,000 vocabulary bank, George/Emma audio and privacy files were not changed by batch49.
6. The staging branch has no release approval; no production merge, new vocabulary publication or completion notification is justified.

**Next useful work:** prioritise source-backed sense and CEFR re-tier triage for ambiguous draft rows and curate additional strong A2–C1 candidate headwords; maintain the no-deployment barrier.
