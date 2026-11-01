# CEFR 1,000: discourse/degree negative-test repair and whole-shortlist integrity

**Observed:** 2026-11-01 (Singapore time). **Scope:** user-approved 1,000 total words, 200 per CEFR level, staging branch `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / NO DEPLOYMENT.

## Root cause and corrective work

GitHub Actions [structural run 41275951783](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41275951783) failed in the **ALL** lane; A1/A2/B1/B2/C1 level-specific lanes succeeded. [Documentary run 41275954468](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41275954468) also failed. Actual job logs identified `AssertionError: FAIL OPEN: changed_held_myanmar` in `tools/audit_cefr_1000_uk_discourse_degree_six.py`. The adversarial test modified `shortlist["entries"][0]` (the unrelated A1 article **a**), while the packet's per-row source snapshot compares only six A2/B1 discourse words. Thus the injected mutation was outside that auditor's per-row comparison; the failed self-test was real and was not a linguistic approval or a deployment event.

Corrected the self-test to mutate the actual six source-bound shortlist rows (**quite, rather, actually, however, therefore, eventually**) for English definition, Myanmar meaning, example, POS, CEFR level, source path, source index and historical source blob SHA. Added exact full-file Git-blob SHA-1 verification against the frozen provisional shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, so **any** on-disk shortlist modification outside the six selected words also invalidates the research audit. Added release-status, approved-scope, declared-count and unique-headword guards, plus a tampered-blob negative test. The frozen shortlist, independent-review tasks and source packet were **not edited**. Code commit: [`8b798f3c1a5906f959eafd8ab464bf4c55e6e402`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/8b798f3c1a5906f959eafd8ab464bf4c55e6e402).

## Actual post-fix GitHub Actions evidence

- [Structural run 41282211638](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41282211638): **completed SUCCESS**, all six jobs A1, A2, B1, B2, C1 and ALL. ALL job `124776244879`; structural ALL artifact `13074340283`. The actual ALL log reported **213 adversarial mutations rejected** by the repaired six-word auditor.
- [Documentary no-deploy run 41282211667](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41282211667): **completed SUCCESS, report-only**. Job `124776244676`, blocker-report artifact `13073702155`; log also reported **213 mutations rejected** by that auditor, and explicitly recorded release blockers.
- Both runs tested the same **code SHA `8b798f3c1a5906f959eafd8ab464bf4c55e6e402`**. Git comparison from the prior staging checkpoint `7111fce249c5a7959d7842353e0ac0207a475868` to that code SHA showed exactly **one modified staging audit file**, 37 additions and 3 deletions. Documentary log: `PASS: protected production assets untouched by staging migration`. This automated comparison is not independent physical/device or production-preservation signoff.

## Frozen release-blocker counts

| Level | First-pass written | Independently approved | Editorial hold |
|---|---:|---:|---:|
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

The source-observation ledger previously reported Oxford word/POS coverage **995/1,000** (A1 195; A2/B1/B2/C1 200 each), including five A1 inflection/sense exceptions. That is research coverage, **not** independently checked English, Myanmar, original example or exact-sense CEFR. No new publisher source observation was claimed by this repair. The separate IELTS 1,000-word bank and the existing 54 lessons remain protected.

Final George/Emma **real listening signoffs: 0/1,000**; no completed approved dual-voice manifest. Independent human review receipts, deduplicated approved release manifest, complete headword/example audio with actual listening, browser/mobile regression, physical iPhone Safari review, measured GitHub Pages hosting, independent preservation/privacy signoff and confirmed production deployment are missing. The documentary gate's **SUCCESS means its fail-closed report completed**, not that the release passed. **No merge, main change, publication or launch.**
