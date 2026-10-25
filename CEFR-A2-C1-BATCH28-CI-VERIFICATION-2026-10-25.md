# Batch28 GitHub Actions verification — 25 October 2026
**Staging only; no merge or deployment. All linguistic approvals remain zero.**

## Commits
- `9f5abefaacd0c9a10d30a96e240a3030c1908e08`: atomic commit with 63 original bilingual drafts, 63 independent-review task packets, 14 reversible candidate quarantines, level-specific auditor, parallel workflow and initial checkpoint.
- `166030bbdb051bd23196afe2afe725937cbc1803`: checkpoint documentation updated with actually observed first CI results; no draft or production content changed.
- Baseline `761b2f6c1391d0af0aa5902f545c1da4bbf7bd44`: comparison to first commit showed exactly six staging-only files added, one commit, no production changes.

## Actually observed CI
- [Initial run 40165436565](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40165436565) at `9f5abefa...`: **completed/success**. Five real jobs A2 `121085402556`, B1 `121085402432`, B2 `121085402592`, C1 `121085402566`, ALL `121085402583`: all completed/success; decoded logs inspected.
- [Checkpoint rerun 40165466823](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40165466823) at `166030bb...`: **completed/success**. Five real jobs ALL `121085490496`, A2 `121085490532`, B1 `121085490619`, B2 `121085490556`, C1 `121085490566`: all completed/success. Decoded ALL job log inspected; the exact output:
  - `UNIQUE A2-C1 A2=486 B1=497 B2=495 C1=350 total=1828; independently approved=0`
  - `A1=500; A1-C1 written=2328; first drafts outstanding=2672; legacy duplicate rows= 182`
  - `STAGING ONLY batch28 ALL PASS: 63 drafts, 14 held, zero approvals; no audio/deploy`

## Exact counts and blockers
- Written (not approved): A1 500, A2 486, B1 497, B2 495, C1 350; **2,328/5,000** total.
- Independently approved for English/Myanmar/CEFR/examples: **0/5,000**.
- Remaining unwritten: A1 0, A2 214, B1 503, B2 805, C1 1,150; **2,672** total.
- Quarantined candidate words: **440**, including 14 newly held in batch28. Legacy identical draft duplicates: **182**, excluded from unique written totals.
- **Not validated:** exact dictionary sense/POS and level sources, natural Myanmar, examples by independent reviewer, George/Emma complete audio generation and real listening, real-device iPhone Safari, browser/mobile regression for release, hosting bandwidth, or live CEFR deployment.
- GitHub Actions successes are **structural** tests only, not editorial approvals or listening tests.

## Production hold
Production branch `main` observed at `dca0db7aa30118ecc18350db8dc406e6cac91554` during batch28. No changes to production 54 lessons, IELTS 1000, George/Emma audio, privacy or publication dataset. Staging `cefr-vocabulary-data.js` still contains `entries:[]`. No merge, no deployment.
