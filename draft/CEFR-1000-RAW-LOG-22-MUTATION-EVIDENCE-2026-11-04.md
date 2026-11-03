# CEFR-1000 — raw-log evidence for 22-case mutation gate (2026-11-04)

Scope: USER-APPROVED **1,000 total** (A1/A2/B1/B2/C1: 200 each), **not** the obsolete 5,000-word plan. Staging branch only.

## Directly observed evidence

- GitHub Actions structural workflow run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41642178932
- ALL-lane job ID: **125938195397**; fetched decoded raw job log on **2026-11-04**.
- The raw log explicitly contains: `PASS: 22/22 synthetic note and approval forgeries rejected; no human signoff` (timestamp **2026-11-03T13:13:26.4902953Z**).
- This resolves the previous uncertainty about whether the 22-case synthetic suite actually ran in this job. It proves only that the job log reported that assertion; it is not independent audit of test completeness or approval.
- Previously reported six-lane success is separately documented; this readback examined the ALL job's raw log, not fresh logs for every other lane.
- Historical tested commit: `54745b7df955041ca672165f47385e0bcf73cb43`. This report commit is newer and **not** certified by that workflow.
- Shortlist fetched directly from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, with `counts_by_level` A1/A2/B1/B2/C1 = 200 each and `independently_approved_by_level` = 0 each.

## Truthful release state

| Level | First-pass written | Independently approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

**Editorial hold remains in force for all 1,000 entries.** Synthetic mutation rejection is structural QA, not independent English/Myanmar/example/CEFR review. Publisher-backed exact-sense evidence and genuine independent reviewer signoff remain required. Final approved manifest not established. Required George/Emma audio target: 4,000 clips (two voices × headword/example × 1,000), generation and actual listening signoff not verified. Browser/mobile regression, physical iPhone Safari QA, Pages hosting clearance, production deployment and preservation verification are also unverified. **NO RELEASE**.

No provisional shortlist or production assets modified by this documentation checkpoint. Follow-up: authenticate historical source objects in CI; verify current-head run jobs and logs; collect dated exact-sense publisher evidence and genuine independent review, then only after all audio/device/hosting gates consider deployment.
