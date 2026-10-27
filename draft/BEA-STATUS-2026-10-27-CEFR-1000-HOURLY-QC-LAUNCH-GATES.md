# BEA CEFR 1,000 — ongoing QC / conditional go-live checkpoint
**2026-10-27, Asia/Singapore · STAGING ONLY · NO PUBLISH · NO INDEPENDENT APPROVALS**

## User decision and recurring schedule
User explicitly approved a new **1,000 TOTAL CEFR A1–C1** target (A1/A2/B1/B2/C1: **200 each**) and an eventual **live release ONLY AFTER all QC gates have passed**. The previously existing enabled hourly `BEA High-Throughput Build` recurring automation was **updated** to `BEA 1000 QC & Launch`, retaining the same hourly RRULE and the same automation ID `6adba54e7c8881919db2da2d339cb11c`; it prioritises independent English/Myanmar/CEFR/example review, authentic George/Emma listening, real-device iPhone testing, hosting, preservation and conditional production release. No extra, duplicate or faster schedule was created. **No progress notifications should be sent; the only eventual user alert is after independent QC and confirmed actual live deployment.**

## Substantive staging implementation
1. **UI matches the new approved scope.** `cefr-vocabulary.js` now requires exactly **1,000** release-approved entries, exactly **200 per level**, full bilingual fields, review flags and audio routes before rendering; its inaccessible-during-review fallback stays visible otherwise. Screen title now says **1,000 English words**. Updated `tests/cefr-ui.cjs` to generate 1,000 synthetic test rows and added an explicit missing-last-entry negative test. Renamed synthetic QA labels to 1,000. None of these changes attaches real unreviewed content.
2. **Separate publication proof ledger.** `draft/CEFR-1000-RELEASE-EVIDENCE.json` is an EMPTY fail-closed document for a separately approved frozen manifest, 1,000 independent linguistic review receipts (English exact learner sense, natural fluent Myanmar, original example, sense-specific CEFR), real listening receipts for George/Emma word+example per text and voice, desktop/mobile WebKit/Chromium testing, physical iPhone Safari + actual audio playback, measured GitHub Pages hosting limits, preservation of production assets and live deployment. It marks all evidence absent, without manufactured reviewer IDs, URLs, listening or device claims.
3. **Auditable gate.** `tools/audit_cefr_1000_launch_readiness.py` validates the evidence ledger separately from `tools/validate_cefr_release.py`; it checks human receipts against a content fingerprint so silently changed wording invalidates prior review, checks evidence URLs/observation dates, compares logged audio fingerprints against actual files, and requires a release manifest distinct from drafts. Only documented independent testers may supply human/device/listening attestations; these structural checks do not independently prove the authenticity of a person's signature or an external URL. CLI `--report-only` records truthful blockers without incorrectly treating their existence as a workflow failure; strict invocation fails until every pre-launch prerequisite is present. `--after-deployment` additionally requires actual production confirmation. False-ready negative tests prevent a changed status flag from bypassing missing evidence.
4. **Dedicated GitHub Actions QC.** Added `.github/workflows/cefr-1000-go-live-qc-gate.yml` (staging-only, NEVER deploy): runs UI/validator negative tests, the launch-evidence proof and a production-asset diff, uploads a blockers artifact. A user/manual `workflow_dispatch` option can demand **strict enforcement** of every gate but cannot itself deploy.
5. **Protected existing IELTS bank and improved overlap triage.** Mechanical case-insensitive comparison of actual 1,000 selected CEFR wordforms with unchanged actual IELTS 1,000 entries identified **120 shared spellings**: **A1 1, A2 7, B1 27, B2 48, C1 37**. Added `draft/CEFR-1000-IELTS-OVERLAP-REVIEW.json` with one separate, **unapproved** semantic/CEFR usefulness task for each. Wordform overlap is not, by itself, a duplicated sense or editorial error. Added `tools/audit_cefr_1000_ielts_overlap.py` and a step in the existing six-job `cefr-1000-selection-structural-qa.yml` workflow to detect drift and fake approvals.
6. **Legacy tests reconciled.** `.github/workflows/cefr-a1-final-gate.yml` now recognises that its historical A1-500 and 5,000-candidate tests are **legacy draft inventory regressions, NOT the new release goal**, and reruns when the revised 1,000-entry synthetic UI tests change.

## Verified GitHub runs / actual decoded logs
- **[40453106910](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40453106910)**: final six-job CEFR A1/A2/B1/B2/C1/ALL structural QA **completed / success**. ALL job `122020141309` decoded log: **1,000 source-linked bilingual first-pass review candidates, exactly 200 per level, 1,000 matched independent review tasks, 0 independently approved, NEVER PUBLISH**. Negative tests rejected fake independent approval, duplicate and premature hold removal. New overlap auditor logged **120 actual cross-bank overlaps** with zero semantic decisions approved, and `PASS: protected production assets unchanged; no deploy`. Structural artifact uploaded **12711276073**.
- **[40452780641](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40452780641)**: final go-live QC gate workflow **completed / success** as an **expected-blocked evidence report**, NOT a release-ready result. ALL job `122019131704` decoded log: source-reviewed **0/1,000**, voice-listening-approved **0/1,000**, production confirmation **false**. Correctly identifies missing independently approved manifest, human review receipts, actual listening, browser evidence linked to final corpus, physical iPhone Safari test, hosting measurements, preservation release signoff and release-candidate authorization. Negative false-ready test passed; protected assets unchanged. Uploaded blocker artifact **12711685253**. Note: initial intermediate run **40452719788** failed due to a negative test asserting the wrong wording for missing audio; repaired and rerun successfully.
- **[40452184505](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40452184505)**: revised 1,000-word UI test **success**. **[40452346208](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40452346208)**: historical A1 QA including corrected UI test **success**. **[40452170434](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40452170434)**: automated staging WebKit/Chromium browser regression **success**. A transitional UI-only commit generated failing historical jobs **40452170486** and **40452170337** before tests were updated; subsequent corrected runs passed.
- The production branch `main` SHA observed in this iteration: `dca0db7aa30118ecc18350db8dc406e6cac91554`. All changes above were committed only to staging; no PR, main merge or GitHub Pages publish performed.

## Changed file commits
| Change | Staging commit |
|---|---|
| 1,000-word CEFR renderer | `5735406a7f0b0d9b39d64bc02d2a3fcd8ea7512c` |
| Revised UI tests | `9bc798b8799bf03e17739d4227e72484384840c3` |
| Updated UI workflow label | `fe5875a5afe32ab583e392fb3d00080c847d9f97` |
| A1 legacy test integration | `9a95607b43a2a85e5f81862866e1a2eab01cd961` |
| Empty human/launch proof ledger | `4da5a440058a90db48b89494c2bd8c84e961f9b4` |
| Readiness auditor and corrections | `fdc9280bcbb8ffe5c81583f07f4c60b9dbc69d49`, `20f0a9a543c9172afc930b3314dc4a6ce34c80ce`, `ca7b1e4eb5ed18e7198282f457ee1eeb5ca48ad0` |
| Go-live evidence QA workflow | `babd20a9be75a3e5b1764e43d01c776669992c1e` |
| IELTS overlap ledger | `c6f0f3bb0b7a7be69ac7005b4023c19b1e0b6162` |
| IELTS overlap auditor | `e3099f78c867a2367f1f92bbfee2f16d7abfb7e1` |
| Six-job workflow with cross-bank QA | `15bdf9c54d236b8d67b972de12830741bac7ed9d` |

## Exact per-level counts — revised 1,000 total
| Level | Provisional bilingual selected | Independently English/Myanmar/CEFR/example approved | Both voices really listened | Production released |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 0 | 0 |
| A2 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 0 | 0 |
| C1 | 200 | 0 | 0 | 0 |
| **TOTAL** | **1,000** | **0** | **0** | **0** |

## Blockers, next work and production policy
1. Obtain **real independent** English/part-of-speech/learner-sense source checks, fluent Myanmar meaning checks, sentence grammar/intent checks and sense-specific CEFR evidence for all 1,000; change/quarantine unsupported entries instead of misrepresenting 200-per-level certainty. Existing 120 IELTS/CEFR shared headwords have additional pending semantic/usefulness reviews.
2. Once a genuinely approved manifest is fixed, generate all missing final-corpus George/Emma word and example MP3 files; run decoding and real individual listening on both voices; log identifiable review receipts. Never infer real listening from existence checks.
3. Re-run desktop/mobile WebKit/Chromium tests on the *approved integrated version*; obtain a tester's real physical iPhone Safari playback and UI report, and verify actual GitHub Pages hosting limits and preserved privacy/lessons/IELTS/audio.
4. After complete QC, prepare **a narrow reviewed release PR** rather than merging historical 5,000-word draft corpus wholesale. Require strict go-live evidence gate, review exact diff against production and integrate only approved CEFR dataset/audio/UI. Then merge/publish on `main` only with valid release authorization, observe deployed GitHub Pages run, verify the real live website and record public deployment SHA.
5. User notification is due **only once** after all final release conditions, including confirmed production deployment, are evidenced.

**Present result: automation continues hourly, structural checks pass, release proof deliberately blocks go-live. No production changes.**
