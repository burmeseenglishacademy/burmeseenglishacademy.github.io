# CEFR-1000 staging raw CI log verification — 2026-11-19

**Scope:** approved 1,000-total provisional CEFR A1–C1 plan only; staging branch `cefr-5000-bilingual-qa-staging`. This is a CI evidence supplement, not independent language review, release authorization, or deployment.

## Observed GitHub evidence

- Workflow run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44409591205
- Observation date: 2026-11-19 (Singapore).
- The GitHub Actions jobs API returned ten **completed/success** jobs, five level-specific structural QA jobs and five level-specific adversarial regression jobs.
- Unlike the earlier API-only report, raw job logs were **actually fetched and inspected** for C1 structural job ID `135173837279` and C1 adversarial job ID `135173837407`. Raw logs for the other eight jobs were not examined in this observation.
- C1 structural log explicitly printed `Provisional counts: {'A1': 200, 'A2': 200, 'B1': 200, 'B2': 200, 'C1': 200}`, `PASS: 1000 matching PENDING tasks (200/level), provenance intact; ZERO independently reviewed`, and `PASS: C1 provisional structural checks only; NOT independently reviewed or release-ready`.
- The C1 staging-gate JSON printed `"mode": "structural"`, `"level": "C1"`, `"errors": []`, and `"independent_approval_inferred": false`.
- C1 adversarial log printed `Ran 224 tests in 10.815s` followed by `OK`. Visible tests included cross-level duplicate detection, forged approval and release status rejection, invalid provenance/source indices, unrelated-level changes, and release rejection without external signoffs. This is evidence for this specific job, **not** an assertion that every level's raw logs were checked.
- Both inspected logs also displayed a Node.js 20 deprecation warning concerning checkout@v4 and setup-python@v5 running under Node.js 24. This warning did not fail these jobs; consider upgrading action versions in a separate staging-only change after checking compatibility.

## Inventory and release decision

| Level | First-pass English | First-pass Myanmar | First-pass examples | Independently approved |
|---|---:|---:|---:|---:|
| A1 | 200 | 200 | 200 | 0 |
| A2 | 200 | 200 | 200 | 0 |
| B1 | 200 | 200 | 200 | 0 |
| B2 | 200 | 200 | 200 | 0 |
| C1 | 200 | 200 | 200 | 0 |

Shortlist provenance blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. First-pass content remains editorially held. No independently approved entry or source-backed human signoff was found in these CI observations.

**BLOCK release.** The final manifest requires independent English, fluent Myanmar, example and exact-sense CEFR reviews (0/1,000 approved); full final-manifest British George/Emma headword/example audio and real listening signoff (not established); browser/mobile and physical iPhone Safari evidence (not established); GitHub Pages hosting and privacy checks (not established); confirmed production deployment and verification of 54 lessons, separate IELTS 1,000-word bank and established production audio (not established). No protected production assets or approval flags changed in this documentation update. Structural green CI cannot satisfy these gates.
