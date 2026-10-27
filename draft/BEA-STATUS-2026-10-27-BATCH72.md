# BEA CEFR 5,000 — Batch72 staging report
**27 October 2026, Singapore. STAGING ONLY. NOT APPROVED, MERGED, DEPLOYED OR RELEASED.**

## Substantive original bilingual drafting
- Authored **40 new original English/Myanmar first-pass vocabulary drafts**: A2 **8**, B1 **8**, B2 **9**, C1 **15**. Each has an English sense-specific definition, a first-pass natural Myanmar meaning and an original grammatical example. No filler or placeholders were counted as a draft.
- Prepared **40 separate independent English/Myanmar/example/CEFR review-task records** and **40 reversible editorial quarantine records**. All 40 are held, not approved or published. None of the 40 has generated or listening-validated George/Emma recordings.
- Discovered and replaced **16 duplicate candidate headwords** using actual GitHub Actions collision reports rather than inflating counts. The final 40 headwords have **zero prior-authored collisions** in the five-way structural audit.
- Audited **167 extra candidate words** in four parallel level-specific GitHub Actions jobs plus ALL: A2 **50 screened / 22 mechanically clear / 28 held**; B1 **54 / 36 / 18**; B2 **53 / 18 / 35**; C1 **10 / 10 / 0**. Total **86 mechanically clear-only / 81 held**. The final 40 drafts consist of **21 clear-only from the earlier observed Batch70 preflight** and **19 clear-only from the corrected Batch72 preflight**. These are mechanical checks, **not CEFR or linguistic approvals**.
- Added **29 targeted editorial-risk flags** (rare/derived words, technical or legal senses, provisional CEFR tier, register and polysemy). All 40 remain held even if not individually flagged.
- Inspected actual Cambridge Dictionary pages for **oversleep** and **surreptitious** and Oxford's explanation of CEFR vocabulary-list alignment. Saved preliminary source-observation notes separately. Neither word has independently approved English/Myanmar/CEFR/examples, and no listening was done. Source pages: https://dictionary.cambridge.org/dictionary/english/oversleep ; https://dictionary.cambridge.org/dictionary/english/surreptitious ; https://www.oxfordlearnersdictionaries.co.uk/about/wordlists/cefr .

## Exact cumulative counts — two different ledgers
| Level | Target | Existing structurally eligible first-pass written | All staged unique headwords at proposed level, **including held** | Independently checked/approved |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 500 | 0 |
| A2 | 700 | 654 | 747 | 0 |
| B1 | 1,000 | 947 | 1,024 | 0 |
| B2 | 1,300 | 1,133 | 1,227 | 0 |
| C1 | 1,500 | 956 | 1,134 | 0 |
| **Total** | **5,000** | **4,190** | **4,632 level-headword memberships** | **0** |

**Global distinct staged wordforms: 4,608**, because **24 headwords occur in two proposed CEFR levels**. The level counts are not 4,632 approved words. The full historical corpus has **566 repeated file occurrences** (not 566 independently confirmed semantic errors). Added a separate **24-word reversible cross-level hold ledger** with exact words and competing provisional levels. These must be resolved through independently documented sense-specific CEFR evidence before release.

The previous structurally eligible ledger remains **4,190/5,000**, with **810 eligible slots still unfilled**. Quarantined drafts in Batches 68–72, including the new 40, are not added to that ledger. **Zero entries** have independent full English/Myanmar/sense/CEFR/example approval.

## Observed GitHub Actions and corrections
- Batch71 predecessor run **40426914247**: all A2/B1/B2/C1/ALL jobs completed **success**, 72 held drafts and production guard pass.
- Batch72 first structural run **40427450298**: **failure**, correctly found 16 collision headwords; also exposed an incorrectly escaped ALL audit expression. Both issues were repaired. Intermediate failed runs are retained in GitHub history; no failed run is described as passing.
- First extra candidate run **40427541316**: all five jobs **success**, but screened 164 before three more candidate words were added.
- Intermediate candidate run **40427685774**: all five jobs **success** but incorrectly counted the current Batch72 drafts as earlier-authored collisions; preflight was corrected to exclude its own batch.
- Corrected candidate run **40427761888**: **A2, B1, B2, C1 and ALL completed/success**; decoded logs confirmed **167 screened, 86 clear-only, 81 held**. Persisted actual log-derived results in `draft/BATCH72-EXTRA-CANDIDATE-TRIAGE.json`.
- Final strengthened structural run **40428029134**, commit `7711bf5d43f8d56bfe7520ec99e3a304ffcddb4a`: **all five jobs completed/success**. Actual ALL job **121938583129** logged **40 checked; 21 earlier-preflight-clear-only; 19 current-preflight-clear-only; zero cross-corpus problems; 4,608 distinct staged headwords; 24 cross-level wordforms; 566 repeated file occurrences; PASS: protected production assets unchanged**. This is a structural-only success.

## Staging commits and files
- Original draft/review/quarantine commits: `f0e7a4a554074ef98ec6cf4dd5fb5983acf2d4b8`, `8f4505186ace598970510262e68a44ca4720fa0c`, `aa6320f17296125687d69487192c78e0b50dfbf1`.
- Duplicate replacement and review/quarantine synchronisation: `be3f9a7a1c22fd127ea0c52e5536216393ceeebd`, `6c94ef4c92a28ba921b904b75d6962ac3122ccb9`, `50a073dac55bb5cefa25e3fa43b1a5023f8bbc8b`.
- Corrected candidate preflight and persisted actual result: `d0d3fb9e43af78b3bde1bdc836d3de5135842090`, `d9e89a5189ac8595509aff7ed5aec371b9ec133f`.
- Targeted risks `de3df4ddd72aa6245e1adb74cdddab74e08d610d`; source observations `8f18aa07f6b3c29254d8a494d3a88cc3ad396fa6`; historical cross-level quarantine `0785f3931288f971b69897aad52456921e32ed9f`.
- Final audit hardening `ede7bd007c028d2589c229275fa2a36783280356`; workflow trigger guard `7711bf5d43f8d56bfe7520ec99e3a304ffcddb4a`.
- Data and tasks: `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH72.json`, `draft/A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH72.json`, `draft/A2-C1-SOURCE-RECOVERY-QUARANTINE-BATCH72.json`.
- QA: `tools/audit_cefr_batch72_recovery.py`, `tools/audit_cefr_batch72_candidates.py`, `.github/workflows/cefr-batch72-structural-qa.yml`, `.github/workflows/cefr-batch72-candidate-preflight.yml`.

## Release blockers and safety
The 54 production lessons, existing IELTS 1,000-word bank, George/Emma production audio and privacy assets were not edited; final ALL job's protected-assets diff guard passed. Staging CEFR publication data remains empty/blocked. No merge or live production deployment.

Outstanding: source-supported CEFR classification for exact senses, independent fluent Myanmar and English editorial approval, independent example review, 5,000 fully approved entries, George/Emma collection generation and real listening validation, browser/mobile and physical iPhone Safari tests, hosting storage/bandwidth validation, and confirmed live production deployment. No completion notification is warranted.
