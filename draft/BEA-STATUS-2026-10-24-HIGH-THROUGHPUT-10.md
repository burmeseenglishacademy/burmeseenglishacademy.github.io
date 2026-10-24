# Burmese English Academy staging batch10 — 2026-10-24

STAGING ONLY. NOT APPROVED. NOT DEPLOYED.

Authored 40 distinct original bilingual first-pass drafts: 10 per provisional A2/B1/B2/C1. Independent English sense, Myanmar translation, example, CEFR and George/Emma listening approvals all remain false. The separate review-task file lists source URLs as unvisited leads only. All C1 labels are high-risk, including words likely to belong at lower levels; reclassify or replace based on real source review.

| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 216 | 0 | 484 |
| B1 | 1000 | 216 | 0 | 784 |
| B2 | 1300 | 216 | 0 | 1084 |
| C1 | 1500 | 216 | 0 | 1284 |
| TOTAL | 5000 | 1364 | 0 | 3636 |

English definitions, Myanmar glosses, original examples, independent source-evidence tasks, and audio review remain separately recorded. The 21 prior source observations, 8 flagged level conflicts, and 119 quarantined candidates are unchanged. No new independent evidence or listening review was performed.

Pre-commit JS structural preflight: 40 distinct nonduplicate words, 10 per provisional level, example/headword substring, Myanmar script and example length. This is not grammar or semantic verification. A five-job GitHub Actions workflow was added for A2/B1/B2/C1/ALL; inspect real run status and logs after triggering. No release workflow, audio generation or production edit was performed.

Blockers: 0 of 5000 independently approved; 3636 still unwritten; candidate/CEFR risks; complete George/Emma audio generation and listening; browser/mobile/physical iPhone Safari; hosting limits; live production deployment. Existing 54 lessons, IELTS 1000, George/Emma production audio and privacy remain untouched.

## Actual commits and GitHub Actions results

- Batch10 content, review tasks, integrated master, five-way workflow: 403a5abfce3b6857cade01cea0757d6b2fad02d3.
- Initial batch10 run 40090006398: COMPLETED / FAILURE. Its matrix auditor incorrectly retained the batch09 expectation of 20 words per level; the actual new batch is 10 per level. This was a test-code error, not a successful test.
- Fix commit 5d2630bc7243acb43bf5ab73e803d9f7966ebd5b corrected the expected per-level count to 10.
- Corrected batch10 run 40090062454: A2, B1, B2, C1 and ALL jobs each COMPLETED / SUCCESS. ALL job 120860748614 log confirms 40 original bilingual drafts and explicitly NOT APPROVED / NOT DEPLOYED.
- Existing bilingual/source structural run 40090006442: COMPLETED / SUCCESS. Job 120860581716 log confirms 864 A2-C1 first drafts (216 each), 21 source observations, 8 provisional CEFR conflicts, 0 independent approvals and unpublished CEFR data.
- Other push regression workflows (batch05–09, quarantine, four-level QC, candidate triage, editorial previews and 45 packet preparation) completed successfully at 403a5abf. None is independent bilingual or pronunciation validation.
- Production release and independent listening were not attempted. No live deployment occurred.
