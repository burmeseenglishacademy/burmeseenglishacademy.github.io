# CEFR-1000 historical CI failure triage — 2026-11-22

Scope: **1,000 provisional entries only**, 200 each at A1/A2/B1/B2/C1. Branch: `cefr-5000-bilingual-qa-staging`. This document is author-side engineering triage, **not** independent review or release authorization.

## Evidence observed

- GitHub Actions run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44811286785
- Inspected A2 job ID **136548182394** decoded logs on **2026-11-22**. The checkout in that job was commit `0382d80749037ba484003480b635871b66d4abbf` (2026-11-20). Node 22.23.5 failed with `AssertionError [ERR_ASSERTION]: Unexpected or out-of-range task ID CEFR1000-A2-0201` at `scripts/cefr-1000-level-structural-qa.cjs:84`. The job exited 1.
- API job conclusions for the same historical run: A2 job **136548182394**, B1 **136548182133**, B2 **136548182423**, C1 **136548182486** all `completed/failure`; A1 **136548182598** returned the inconsistent pair `in_progress/success`. Do not treat A1 as a completed pass.
- Current staging validator blob SHA inspected on 2026-11-22: `d78091d1685709612d395abc203d963115ed90fa`. It now computes `levelOffset = levels.indexOf(level)*200` and expects A2 IDs 0201–0400. Thus the observed *historical* A2 failure is consistent with a stale validator's task-ID range, **not proof of corrupt A2 data**. This is a code-reading diagnosis, not a verified new CI success.
- Current workflow blob SHA inspected on 2026-11-22: `d58707e9d5b06525b6653bae4e78e26970695cba`. Its matrix runs Python and Node structural QA per level and isolated swapped-ID negative tests. Actual job logs/conclusions for the current staging commit have **not** been established.

## Next executable checks (must be observed, not assumed)

1. Identify the workflow run for the **current branch HEAD SHA**, not the historical 2026-11-20 checkout. Check each Python/Node matrix job, mutation tests, release blockers and logs, including that swapped-ID negatives fail for the intended assertion.
2. If the new workflow fails, fix the precise failure in staging and rerun; never weaken expected failure semantics to obtain a green check.
3. Keep release blocked independently of structural CI: 1,000/1,000 human-independent English, Myanmar, example, pronunciation and exact-sense CEFR approvals; deduplicated final 200-per-level manifest; 4,000 real George/Emma recordings and human listening evidence; browser/mobile and physical iPhone Safari evidence; GitHub Pages hosting clearance; protected assets checked; and confirmed production deployment are not established.
4. No change to provisional entries, independent review decisions, protected 54 lessons, separate IELTS bank, production audio or `main` is authorized by this triage.

## Inventory snapshot

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Counts are from the staging shortlist's declared inventory and review state, not an independent lexical review. Release status: **BLOCKED / STAGING ONLY**.
