# Burmese English Academy — CEFR 1,000 scope migration and review preparation
**27 October 2026 (Singapore) · STAGING ONLY · NO INDEPENDENT APPROVAL OR DEPLOYMENT**

## User-approved revised scope
The CEFR expansion now targets **1,000 TOTAL vocabulary headword/sense entries**, in five equal **A1 200 / A2 200 / B1 200 / B2 200 / C1 200** quotas. The existing **IELTS 1,000-word bank is a separate preserved collection**. Historical Batch76 figures relating to the former 5,000-word target are **not** the new completion metric.

## Substantive completed changes
- Changed the fail-closed release validator `tools/validate_cefr_release.py` and its negative tests to **exactly 1,000** entries, with **200 per level**, retaining independent review, source-specific citation, duplicate detection, bilingual text checks and optional George/Emma MP3 existence/decoding gate. The `--audio` mode now also explicitly blocks when no root directory is supplied.
- Updated **only** the staging CEFR placeholder target to 200 per level. `cefr-vocabulary-data.js` still declares `UNVERIFIED_DRAFT_DO_NOT_PUBLISH` with `entries:[]`; **no CEFR vocabulary is live**.
- Built `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`: **1,000 actual, bilingual first-pass records** selected from existing authored staging sources, each with an exact source file, row index and Git blob SHA. Entries retain original English definition, Myanmar meaning, part of speech and original example. Every entry has independent-review flags **false**, source-evidence URL fields empty, editorial hold **true**, release approval **false**.
- Built `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json`: **1,000 separate stage-by-stage review tasks**, one for each selected word, covering exact sense/POS and English source, fluent Myanmar, example grammar/meaning, source-supported CEFR placement and post-lock George/Emma generation plus real listening. Every task is pending.
- Built `draft/CEFR-1000-SELECTION-TRIAGE.json`, preserving screened candidate paths, historical conflict holds, reversible curriculum/CEFR concerns and skipped rows. **2,225 candidate-level source rows** were examined from 14 existing draft files. **20 cross-level conflicting wordforms** were observed within this source selection pool; source/historical holds and duplicate wordforms were excluded. **46 unique historically held wordforms** were imported from the existing Batch72/74/76 hold files. Screening recorded **303 skipped candidate-row occurrences before quotas** (197 explicit curriculum/sense-level doubts, 58 existing candidate/cross-level holds, 40 duplicates, 8 malformed source records). The remaining unselected source rows were not adjudicated or marked rejected.
- Created `tools/audit_cefr_1000_shortlist.py` and a six-job parallel `cefr-1000-selection-structural-qa.yml` workflow. It checks exactly 200 distinct source-linked drafts per level; no duplicate headwords; historical holds; complete Myanmar/English/example fields; source-blob integrity; 1:1 review-task parity; false approval/listening flags; empty publication placeholder; and no modifications to protected production assets. Negative tests intentionally corrupt source hold, approval and duplicate fields to ensure detection.

### Exact new-scope counts
| Proposed level | Provisional bilingual selected (NOT approved) | Independent linguistic/CEFR review completed | George/Emma listening approved | Released |
|---|---:|---:|---:|---:|
| A1 | 200 | 0 | 0 | 0 |
| A2 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 0 | 0 |
| C1 | 200 | 0 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** | **0** |

**CRITICAL:** The 1,000 are a reversible provisional **review shortlist**, **not** independent bilingual, pronunciation or CEFR approvals. A mechanically complete shortlist can still contain questionable senses, levels, context/collocations, or translations. Every row is on hold until documented source-based review. The formerly reported 4,190 first-pass eligible drafts out of 5,000 and 4,864 distinct historical staged wordforms are historical inventory metrics only.

## GitHub commits and actual verification
- Scope decision: `b1e25ab9f8a56e27697509410fc88fa588caf882`.
- Validator/quota: `c942bfb22ba21513d414f88b9424c6c4f7c62e24`; test update: `995a48764648d761535fe4c8a8418c4e82538375`; unpublished placeholder: `9655cd527e7d1f1665f6f8618ad8104b6f5354b6`.
- Provisional data: `0e1a14eb6a64e631062ef49deca757d583d1a614`; review tasks: `2f15da6d4484d4a5d0c243e6f63b0e51e83292ea`; triage: `0ae602c4c9c69b6e842b1002ea3d1e59538e7a1f`.
- Structural auditor: `5dbe3b78cfd6f7e5623b31daeb57b08e0df4037b`; parallel workflow: `ab066723e83b48983ca448065ef43418b0d31a19`.
- Actual [new 1,000-word selection QA run **40451436877**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40451436877) **completed with all six jobs success**: A1 `122014837297`, A2 `122014837499`, B1 `122014837522`, B2 `122014837453`, C1 `122014837497`, ALL `122014837440`.
- Actual decoded ALL-job log stated: `PASS: ALL 1000 staged review candidates; per-level counts {'A1': 200, 'A2': 200, 'B1': 200, 'B2': 200, 'C1': 200}; 1000 linked review tasks; 0 independently approved; NEVER PUBLISH`. Negative tests passed for fake approval, duplicate headword and premature quarantine removal. Production-asset diff against `origin/main`: `PASS: protected production assets unchanged; no deploy`. ALL-job structural artifact uploaded as [ID 12710672538](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40451436877/artifacts/12710672538).
- After validator and unit tests were brought into alignment, actual release-negative-test run [**40450955712**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40450955712) succeeded. Staging automated UI run **40450958827**, automated browser regression **40450958705** and historical A1-500 draft-regression run **40450958824** also succeeded. **Earlier intermediate validator changes** briefly caused runs **40450951680** and **40450951651** to fail; later corrected revisions passed. Historical A1-500 QA remains a legacy draft test, **not** an A1-200 release target or a reviewed milestone.
- Node 20 deprecation warnings were observed in the structural ALL log for `actions/checkout@v4` and `actions/upload-artifact@v4` (forced to Node 24 by GitHub). Jobs still succeeded; version modernisation remains a maintenance item.

## Remaining blockers and release policy
**0 of 1,000 independently approved.** Independent English dictionary exact-sense checks, fluent Myanmar review, example grammar, independent sense-specific CEFR evidence, cross-level sense arbitration, George/Emma final-collection generation and real listening, browser/mobile completion, real-device iPhone Safari, hosting limits and live deployment are **not complete**. Automated browser workflow success is not real-device testing.

The staging list must not be merged, shipped or attached to the live site. Existing production **54 lessons**, independent **IELTS 1,000 bank**, established **George/Emma audio**, and **privacy protections** remain preserved.

**Next work:** Let independent reviewers assess the separate stage-by-stage tasks, resolve suspect CEFR placements rather than force 200, replace/hold any low-quality entry with evidence-backed candidates, record signed source observations and real listening outcomes, and only then consider an approved 1,000-entry dataset for the strict release validator. The hourly automation cadence does not need to increase. No completion notification until all defined conditions, including live production confirmation, are met.
