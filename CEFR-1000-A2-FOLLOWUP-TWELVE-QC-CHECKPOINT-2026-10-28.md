# CEFR 1,000 — A2 Oxford follow-up source and staging QC checkpoint (2026-10-28)

**Scope:** Exactly 1,000 provisional bilingual entries: A1 200, A2 200, B1 200, B2 200, C1 200. **No independent approvals. No live deployment.** Work performed exclusively on `cefr-5000-bilingual-qa-staging`. The older 5,000-word target is superseded.

## Publisher evidence actually observed

On **2026-10-28**, directly inspected the official Oxford University Press [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), using its extracted text with recorded **1-based PDF pages and 0-based extracted line numbers**. Added twelve *previously unpacketised* provisional A2 entries to [the source-provenance packet](draft/CEFR-1000-OXFORD-A2-FOLLOWUP-TWELVE-2026-10-28.json), including exact current English definition, original Myanmar meaning, original example, upstream source path/index/blob SHA, source URL, observation date, reviewer tasks and specific editorial risks. These are **word/part-of-speech CEFR observations, not independent exact-sense CEFR classifications**.

| Provisional A2 | Oxford word/POS label | Official PDF locator (page, line) | Editorial risk |
|---|---|---|---|
| case (noun) | A2 n. | 4, 1027 | `in this case` situation sense requires separate direct-sense evidence |
| person (noun) | A1 n. | 3, 586 | Basic individual-human sense appears lower-level |
| change (verb) | A1 v., n. | 1, 139 | Basic change-meeting-time verb; separate transitive sense needed |
| enough (determiner) | A1 det., pron., adv. | 1, 245 | Determiner quantity use, Myanmar grammatical naturalness |
| believe (verb) | A1 v. | 1, 79 | Belief-in-truth vs trust/religious senses |
| job (noun) | A1 n. | 2, 410 | Basic paid-work sense, factory example not A2 proof |
| later (adverb) | A1 adv. | 2, 428 | Ordinary `call you later` use |
| line (noun) | A1 n. | 2, 444 | Drawing mark vs queue/phone/product-line polysemy |
| order (noun) | A1 n., v. | 3, 559 | Purchase request vs command; Oxford list lacks exact-sense separation |
| service (noun) | A2 n. | 6, 1602 | Shuttle transport service vs generic customer assistance definition |
| season (noun) | A2 n. | 6, 1590 | Rainy-season June timing is region-dependent |
| area (noun) | A1 n. | 1, 41 | Visitor-reserved spatial area vs broader geographic region |

**Summary:** 9 lower Oxford A1 word/POS classifications, 3 Oxford A2 matches, 0 human-independent exact-sense approvals. No automatic re-tiering or shortlist edits.

## Safeguards and real execution

- New [fail-closed source/snapshot auditor](tools/audit_cefr_1000_oxford_a2_followup_twelve.py) compares all twelve source locators and original English/Myanmar/example snapshots against the immutable canonical shortlist blob. It rejects false approvals, missing holds, altered publisher metadata and mismatched source data.
- **24/24 negative source/approval mutation cases rejected** in the actual GitHub Actions [parallel structural run 40687281815](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40687281815), run head `3e9549570a94a1a9287e80d141a43bc9ca2fe886`. All six **A1/A2/B1/B2/C1/ALL** jobs concluded **success**. ALL-job ID `122812786536` explicitly logs `negative_mutations_rejected: 24` and zero approvals.
- Actual [documentary no-deploy run 40687356539](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40687356539), head `7fb5a5609ad6d555d999818bb4a7c181c97b9946`, job `122813041105`, concluded **success as report-only**. Logs explicitly say **0/1,000 source-reviewed**, **0/1,000 both-voice listened**, and **production confirmed false**. Protected production paths passed the Git diff check.
- The release auditor now requires separate, independently attested, content-hash-bound **A2 exact-sense publisher evidence** and explicit reconciliation for all nine retained Oxford A1 differences. A dedicated negative test rejects an unknown/fabricated A2 follow-up receipt. That *additional negative-test commit* must be covered by a subsequent CI run; the earlier runs do not validate it.

## Exact counts and remaining launch blockers

| CEFR level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Final British George and Emma headword+example audio generation/listening remains unverified; final real listening receipts **0/1,000**. Desktop/mobile regression, **physical iPhone Safari**, measured GitHub Pages site/repository bytes and bandwidth, independent English/Myanmar/example/CEFR review, approved release manifest and confirmed production deployment are still missing. The 54 existing lessons, separate IELTS 1,000-word bank, established production George/Emma audio and privacy files remain protected; this run did **not** modify main, merge, or publish.

**RELEASE BLOCKED — STAGING ONLY.** Source observation and CI success do not constitute human signoff, real listening, device testing or live deployment.
