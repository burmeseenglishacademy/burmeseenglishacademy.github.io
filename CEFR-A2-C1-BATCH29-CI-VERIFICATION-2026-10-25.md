# Batch29 staging-only CI verification — 25 October 2026

**Status: structural QA passed after a real failed first run. No linguistic or audio approval. Never deploy these drafts.**

## Actual GitHub commits and scope
- First atomic commit [de1a931e5d52a983957ad4ea62fb73f4b69c3c41](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/de1a931e5d52a983957ad4ea62fb73f4b69c3c41): attempted 52 drafts, but duplicated previously used Batch26 candidates. Its CI failure is retained in history.
- Corrective commit [6958fd8520f7dbd64c8ec5d6c995625c80ad5a78](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/6958fd8520f7dbd64c8ec5d6c995625c80ad5a78): removed 27 already-drafted words and 12 already-held words, authored 17 fresh bilingual drafts and 5 fresh reversible holds. Corrected result: **42 distinct drafts and 9 distinct holds**.
- Compared baseline `7708cbd06a44f22e164338044a8ba2d89565ab49` against corrective commit: two commits, exactly six changed staging-only paths (draft, review, quarantine, auditor, CI workflow, checkpoint); **no production site files changed**.

## Observed GitHub Actions runs and decoded logs
- [Initial run 40167162660](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40167162660): **completed/failure**. Inspected five failed jobs, including ALL job `121090469880` and A2 `121090469863` decoded logs: `AssertionError: draft duplicates` at the duplicate-prevention check. This failure prompted the corrective commit.
- [Corrected run 40167276196](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40167276196): five actual job objects **completed/success**, and all five decoded logs inspected:
  - A2 `121090794538` — structural PASS.
  - B1 `121090794527` — structural PASS.
  - B2 `121090794412` — structural PASS.
  - C1 `121090794204` — structural PASS.
  - ALL `121090794430` — structural PASS, reporting `UNIQUE A2-C1 A2=494 B1=507 B2=507 C1=362 total=1870; independently approved=0`, `A1=500; A1-C1 written=2370; first drafts outstanding=2630; legacy duplicate rows= 182`, and `STAGING ONLY batch29 ALL PASS: 42 drafts, 9 held, zero approvals; no audio/deploy`.

## Exact unique written totals, NOT independently approved
| Level | Target | Written first drafts | Independently approved | Remaining unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 494 | 0 | 206 |
| B1 | 1,000 | 507 | 0 | 493 |
| B2 | 1,300 | 507 | 0 | 793 |
| C1 | 1,500 | 362 | 0 | 1,138 |
| **Total** | **5,000** | **2,370** | **0** | **2,630** |

A2–C1 distinct drafts: 1,870. Reversible quarantines: 449 cumulative. The prior 182 identical legacy draft duplicates are not included in unique counts.

## Release blockers and strict evidence boundaries
- Original English definitions, natural Myanmar meanings and grammatical examples are only AI-assisted **drafts**. No independent dictionary sense/POS/CEFR source page was observed or reviewer approval recorded.
- Several frequency-derived CEFR labels, especially C1 common words, are suspect and must be sense-specifically re-tiered or quarantined; a structural pass cannot establish CEFR truth.
- George/Emma CEFR pronunciation collection not fully generated or human listening-validated. Physical iPhone Safari, browser/mobile release regression and GitHub Pages storage/bandwidth sign-off remain unverified.
- Staging `cefr-vocabulary-data.js` was actually inspected and still has `entries:[]`; staging cannot publish these drafts through that data file.
- Production `main` was observed unchanged at `dca0db7aa30118ecc18350db8dc406e6cac91554`. Existing 54 lessons, IELTS 1,000 bank, existing George/Emma audio and learner privacy were not modified by Batch29.

**Do not merge, deploy, announce completion or mark linguistic/audio review as passed.**
