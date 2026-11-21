# CEFR-1000 CI failure triage — 2026-11-22

Scope: approved **1,000-total** project, 200 provisional entries each at A1, A2, B1, B2, C1. This is staging-only engineering analysis, **not** linguistic approval or release evidence.

## Observed failure and provenance

GitHub Actions run [44811286785](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44811286785), job [136548182394](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44811286785/job/136548182394), checked out staging commit `0382d80749037ba484003480b635871b66d4abbf` on 2026-11-20 at 20:25 UTC. The Node A2 job failed in `scripts/cefr-1000-level-structural-qa.cjs:84` with `Unexpected or out-of-range task ID CEFR1000-A2-0201`. Job statuses returned for that run: A2/B1/B2/C1 **failure**; A1 has contradictory `in_progress` status and `success` conclusion, so treat A1 as **not conclusively verified** until a coherent completed run is observed.

## Root cause and current state

The historical validator treated every level's 200 task IDs as if they restarted at 0001, although the register uses global numbering: A1 0001–0200, A2 0201–0400, B1 0401–0600, B2 0601–0800, C1 0801–1000. Thus A2's first valid ID `CEFR1000-A2-0201` was falsely rejected. The current staging validator (Git blob `241a501e5a89a472c0777d4264db57161dd4f970`, observed 2026-11-22) already computes `levelOffset=levels.indexOf(level)*200` and constructs the expected global IDs from that offset. **Do not reintroduce per-level numbering** or renumber source tasks. The failing run predates this corrected blob and cannot be used to judge the current code.

## Required follow-through

1. Obtain a **new staging-commit GitHub Actions run** for the workflow `.github/workflows/cefr-1000-structural-qa.yml` (its push paths do not include Markdown audit-only changes). Record run ID, exact head SHA, completion status, each of the five Python structural jobs, each of the five Node structural jobs, both mutation and release-blocker jobs, and any failing job's log excerpts. A workflow definition is not evidence of execution.
2. Confirm every level emits `provisional_written: 200`, `review_tasks: 200`, `independently_verified: 0`, and `release: BLOCKED`. A passing *release-denial* job is evidence only that release remains blocked.
3. Add regression mutations for valid boundary IDs (A1 0200, A2 0201, B1 0401, B2 0601, C1 0801, C1 1000) and invalid swapped, duplicate or out-of-range IDs; verify actual job conclusions before claiming a fix.
4. Independently adjudicate source-backed exact senses, English, Myanmar and original examples. Maintain separate, attributable human review and observation dates. No author audit can mark `reviewed_*` or `approval` true.
5. Keep the release blocked until 4,000 actual George/Emma headword/example audio assets have real listening evidence, browser/mobile and physical iPhone Safari QA are evidenced, hosting limits and preserved production assets are checked, and the deployed site is actually confirmed.

## Inventory and release interpretation

The staging shortlist metadata inspected 2026-11-22 declares A1=200, A2=200, B1=200, B2=200, C1=200 and independently approved A1=0, A2=0, B1=0, B2=0, C1=0. These are metadata claims, not independent content signoff. Audio generation/listening, mobile/iPhone, hosting and deployment are **not verified**. The 54 existing lessons, separate IELTS bank, established production voices, main branch and privacy protections must remain untouched.
