# Burmese English Academy — batch24 staging checkpoint (25 October 2026, Singapore)

**UNVERIFIED ORIGINAL DRAFTS — NEVER MERGE OR PUBLISH WITHOUT INDEPENDENT REVIEW.**

## Substantive output and separate stages

- Added **48 original English learner definitions, Myanmar first-pass meanings and grammatical example drafts**: A2 **14**, B1 **14**, B2 **14**, C1 **6**, in `draft/A2-C1-EDITORIAL-BATCH24.json`. All CEFR levels and WordNet-selected senses are provisional; C1 draft labels explicitly flag likely lower-level alternatives.
- Added **48 separate five-stage source-evidence review packets** in `draft/A2-C1-REVIEW-TASKS-BATCH24.json`: (1) observed authoritative English sense/POS, (2) independently assessed Myanmar meaning, (3) independent grammar and collocation review, (4) sense-specific CEFR evidence and possible re-tiering, (5) generated George/Emma pronunciation plus actual listening and physical iPhone Safari. All tasks remain pending. Dictionary URLs are **unvisited leads**, not citations of observed findings.
- Added **12 reversible quarantines** in `draft/A2-C1-QUARANTINE-BATCH24.json`: A2 working/europe/die, B1 speaking/ill/worse, B2 jimmy/ordinary/morgan, C1 pie/soap/coin. Reasons include WordNet wrong-sense collision, inflected/rare lemmas, proper entities and obviously suspect C1 assignments. These are candidate holds, not independently adjudicated rejections.
- Added fail-closed `tools/audit_cefr_batch24_review_tasks.py` and `.github/workflows/cefr-batch24-review-qa.yml` with five parallel A2/B1/B2/C1/ALL read-only structural checks. Checks assert candidate tier/POS alignment, uniqueness, cumulative draft/hold separation, all five false review flags, empty observed-source fields and an empty staging release-data array. **Passing structural checks is not independent linguistic QA.**

## Exact unique first-pass inventory (NOT independently approved)

| Provisional level | Curriculum target | Unique written drafts | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 432 | 0 | 268 |
| B1 | 1,000 | 432 | 0 | 568 |
| B2 | 1,300 | 425 | 0 | 875 |
| C1 | 1,500 | 326 | 0 | 1,174 |
| **Total** | **5,000** | **2,115** | **0** | **2,885** |

A2–C1 first-pass unique drafts: **1,615**. Historical duplicate rows in older draft files are not counted twice. Distinct held A2–C1 candidate headwords expected after this batch: **375** (previous 363 + 12). These numbers are calculated from the prior batch23 inventory plus 48 new distinct candidates and are subject to the new batch24 cumulative CI check.

## Commit and real checks

- Data, review packets, quarantine, structural auditor and five-way CI workflow: [`e921294993a640f63da8d45b950a1068c42a78c4`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/e921294993a640f63da8d45b950a1068c42a78c4).
- Last actually inspected preceding five-job batch23 structural run: [40146442331](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40146442331), **completed/success** at commit `69a0b812`. This is **not** a batch24 result.
- **Batch24 CI result pending independent inspection** as of initial report commit. Do not treat a workflow definition, commit success, or this checkpoint as evidence that batch24 GitHub Actions passed. Record run ID, job IDs, logs and any fixes after real inspection.
- No new audio was generated or listened to. No live publication, real-device test or hosting capacity verification occurred.

## Preservation and release blockers

The change set is limited to staging `draft/`, `tools/`, `.github/workflows/` and this checkpoint. Production `main` remains separate; the 54 lessons, 1,000 IELTS entries, existing George/Emma production audio and privacy design must remain unchanged. Staging `cefr-vocabulary-data.js` must retain an empty `entries:[]` until release gates pass.

**Release remains HOLD:** 2,885 first-pass entries unwritten; 0/5,000 independently approved across English sense, Myanmar, CEFR and examples; no CEFR George/Emma full collection/listening; no complete browser/mobile/physical iPhone Safari release pass; no hosting/storage/bandwidth clearance; no verified production deployment. Do not merge, notify completion or mark verified based on green structural CI.
