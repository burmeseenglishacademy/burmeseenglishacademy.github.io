# BEA CEFR 5,000 — Batch68 staging checkpoint
**27 October 2026, approximately 05:15 Singapore time. STAGING ONLY — NOT APPROVED, NOT MERGED, NOT DEPLOYED.**

## Substantive authoring and integrity work
- Prepared **226 independently proposed candidate headwords** for preflight: A2 **47**, B1 **47**, B2 **46**, C1 **86**. These are a screening list, not approved entries or word-count progress.
- Authored **60 original first-pass bilingual draft records** with separate English definitions, natural Myanmar meanings, and original grammatical examples: A2 **12**, B1 **12**, B2 **12**, C1 **24**. Added **60 separate independent-review task packets** and **60 reversible quarantine records**. The independent dictionary/CEFR, Myanmar, example and pronunciation fields remain unsigned and unobserved.
- The **initial** four-level preflight run [40402674131](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40402674131) completed with **A2 SUCCESS, C1 SUCCESS, B1 FAILURE, B2 FAILURE**. Actual decoded logs were read: A2 **31 clear / 16 held** out of 47, C1 **59 clear / 27 held** out of 86. B1/B2 failed at `grep` because an escaped matrix variable became `^\\B1|` / `^\\B2|`; no B1/B2 candidate verdict is inferred from that run. The workflow expression was corrected in commit `952fcb0e721a8926e2e3c097a240e5f606c6d7cf`. The corrected run's job statuses were **not directly observed at report time**; do not call it green.
- Compared the drafted A2/C1 headwords against **real initial preflight job logs**, identified **13 earlier-authored collisions** (4 A2, 9 C1) and **replaced all 13** with original entries whose headwords had returned `CLEAR` in those same A2/C1 logs. Therefore **all 36 currently drafted A2/C1 headwords had a preflight-clear observation against the earlier authored corpus**. This is *only* a mechanical headword screen, not a dictionary sense, CEFR, Burmese, or editorial approval. The 24 B1/B2 headwords await independently observed successful preflight.
- **All 60 new records remain explicitly held** until the complete cross-corpus check and source-based linguistic review. Do not add any of these 60 to the cumulative structurally eligible written ledger, even where an earlier mechanical preflight was clear. No duplicate or weak candidate is counted as approved.
- Added `tools/audit_cefr_batch68_recovery.py` and a five-job A2/B1/B2/C1/ALL nondeploy structural GitHub Actions workflow. The auditor requires exactly 60 matching drafts/tasks/reversible holds, empty evidence, false approval fields, original examples, no named-entity headwords, and checks prior-authored collisions, provisional pool-tier conflicts and suspect WordNet clues. ALL also guards the empty production CEFR bank; the workflow additionally checks protected 54 lessons, IELTS 1,000, George/Emma audio and privacy files for drift. **A newly triggered batch68 structural workflow is not claimed passed until its actual job statuses and logs are inspected.**

## Exact cumulative eligible-written ledger (new 60 excluded pending evidence)
| Level | Target | Previously structurally eligible written | Batch68 newly eligible | Current eligible written | Independently approved | Remaining eligible-writing slots |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | **500** | **0** | 0 |
| A2 | 700 | 654 | 0 | **654** | **0** | 46 |
| B1 | 1,000 | 947 | 0 | **947** | **0** | 53 |
| B2 | 1,300 | 1,133 | 0 | **1,133** | **0** | 167 |
| C1 | 1,500 | 956 | 0 | **956** | **0** | 544 |
| **TOTAL** | **5,000** | **4,190** | **0** | **4,190** | **0** | **810** |

The 60 newly authored, fully held draft records are *additional provisional files*, not 60 eligible words and not 60 approvals. The pre-existing larger corpus has historical collisions and held words; raw row totals are not approved educational vocabulary.

## Actual commits and QA observations
- Candidate headwords: `38165d96531cfa49e754c4e8fe0211067681b9cf`.
- Candidate preflight workflow: `275c40409e9ac887e7539b03d2f7970bc8487e26`; expression repair: `952fcb0e721a8926e2e3c097a240e5f606c6d7cf`.
- Initial bilingual drafts/tasks/holds: `f7071d4a6da940143d5fbb244b1df8e8dfdc6e0c`, `0583328392a516b7df56a4157e4736f06a4446d3`, `3f7525237ea0c63213d2ce2f64cf9df90653dfb3`.
- 13 observed-collision replacements in drafts/tasks/holds: `78f2222ffc379f711bb99cbe6e8ad9fa8b9a85ec`, `c6116bf74ea39693c2aed20b64116ff66560edff`, `700ae58877bde8097fe158e422257d052fe00da2`.
- Structural audit creation and escape repair: `4439a4862ee284ad9d60f3c66abc19deae2119fb`, `96eaaf7fd5cb3b2e73b62cd1a7fed4fa1f0c0ed3`.
- Five-job nondeploy structural workflow and matrix-condition repair: `e53ed7f16bb34e2301522f3fa3a09be260667104`, `706f73983817802f9125408cd9dd37ee67d67bba`.
- Previous batch67 exact-head [run 40396605958](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40396605958) was **reinspected this run**: A2, B1, B2, C1 and ALL were all `completed/success`. This is regression context for the *previous* content, **not** evidence that batch68 passed.

## Release blockers
- **0/5,000** entries independently approved for exact English sense/POS, natural Myanmar translation, sense-specific CEFR level and grammatical example.
- Batch68 B1/B2 preflight success not independently observed; batch68 five-job structural statuses/logs not independently observed.
- New 5,000-word George/Emma audio collection not fully generated or real-listening validated; existing production audio remains unchanged.
- Browser/mobile and real-device iPhone Safari validation, hosting/storage/bandwidth pass, and confirmed production deployment are outstanding.
- **Do not merge, publish, or send a completion notification.** Next iteration: inspect actual corrected preflight and structural jobs, quarantine all collisions and tier conflicts, then convert only genuinely clear and linguistically reviewed entries to eligible/approved states.

## Subsequent real failure diagnosis and staging-only repairs
- Initial batch68 structural jobs **did not all pass**. At [run 40403437217](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40403437217), actual job inspection showed B1/B2/C1 **completed/success**, but A2 and ALL **completed/failure**. Earlier [run 40403391919](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40403391919) had the same split. Decoded A2/ALL traceback identified the exact cause: auditor required at least four letters for a headword, rejecting legitimate three-letter **mop**. This was a **test-rule defect**, not a bad Myanmar translation. Fixed in staging commit `99c4bc1fcfb378d22c2dc39001b147aee0f539dc` to allow three or more lowercase letters. The subsequent corrected structural run's actual status must still be inspected; **do not label it passed without evidence**.
- To make retrospective B1/B2 preflight meaningful *after* the 60 new drafts were staged, added a narrowly scoped `--exclude-current-batch68` option to the general preflight checker. This excludes only the current batch68 file from the **prior** authored index; other authored files and all candidate-pool tier warnings remain checked. Script commit `c07707bf4b0374fc6606f5aecf2c8b600eea539c`, workflow update `501d1a441953d95a1233c3fc1acae29c7a6ffcc7`. Do not mistake a self-collision for an earlier authored duplicate. The newly triggered retrospective four-level run is **not yet observed completed**.
