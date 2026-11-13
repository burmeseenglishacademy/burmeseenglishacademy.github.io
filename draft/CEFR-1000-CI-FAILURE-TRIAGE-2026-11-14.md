# CEFR-1000 staging CI triage — 2026-11-14

This investigation concerns only the user-approved 1,000-total A1–C1 project. No independent review, publication, or production modification is claimed.

## Verified GitHub Actions evidence

- Staging branch head before this document: `bcceff1bae51d1d9b6e3d8b685b46dba51cd3c8b`.
- Push [run 43460226531](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/43460226531) at `93b6c49798b51b844fdc37947f5360933b4a44ef`: completed **failure**.
- Five level-specific jobs reported. A1 job `132004845285` and B2 job `132004845817` failed at **Exercise editorial queue fail-closed mutation tests**. Syntax checks and eight release-gate negative scenarios passed in those jobs; downstream checks were skipped.
- Connected GitHub fetch rejected the job-logs endpoint. Therefore the exact failing assertion is unverified; stdout truncation remains a hypothesis, not a confirmed root cause.

## Staging-only debugging protocol

1. Reproduce with Node 20: `node scripts/cefr1000-entry-review-queue-negative-tests.cjs` and retain stderr, exit code, and first failing assertion.
2. Inspect the unmutated baseline for structural errors before changing tests. Never weaken fail-closed assertions to achieve a green CI result.
3. For each mutation verify nonzero exit, `STRUCTURAL_FAILURE`, `release_allowed:false`, and a nonempty error array.
4. Re-run the five parallel Actions jobs and record the new run ID, per-job conclusions and logs. Prior runs cannot certify later commits.

## Truthful editorial inventory (provisional metadata)

| Level | First-pass written | Independently approved | Audio listening signoff |
|---|---:|---:|---|
| A1 | 200 | 0 | Not evidenced |
| A2 | 200 | 0 | Not evidenced |
| B1 | 200 | 0 | Not evidenced |
| B2 | 200 | 0 | Not evidenced |
| C1 | 200 | 0 | Not evidenced |

Independent English, fluent Myanmar, original-example and source-backed exact-sense CEFR review, cross-level sense deduplication, British George/Emma audio generation and actual listening signoff, browser/mobile and physical iPhone Safari QA, GitHub Pages hosting clearance, production preservation and deployment verification all remain gates. Protect 54 lessons, separate IELTS bank, production voices and privacy. **Remain staging only.**
