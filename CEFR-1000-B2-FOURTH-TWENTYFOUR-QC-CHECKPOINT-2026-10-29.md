# CEFR 1,000 — fourth B2 24-word publisher research and fail-closed QC (29 October 2026)

**RELEASE BLOCKED / STAGING ONLY.** User-approved scope is **exactly 1,000 provisional CEFR A1–C1 entries, 200 each**, not 5,000. Work branch is `cefr-5000-bilingual-qa-staging`; branch name retained. No production merge, publication, or claim of human-independent review.

## Direct Oxford publisher observations

Directly inspected Oxford University Press's [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) on **2026-10-29**. Created [24 source-bound B2 draft observations](draft/CEFR-1000-OXFORD-B2-FOURTH-TWENTYFOUR-2026-10-29.json), with original English definitions, fluent-Myanmar draft meanings, example sentences, source Git path/index/blob, exact short Oxford entry, publisher URL, one-based PDF page, zero-based extracted text line, observation date, editorial risk and independent human review task. Shortlist frozen Git blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

**Oxford word/POS findings: 17 B2 matches, 3 B1, 3 C1, 1 not found in either inspected core list.** Seven require special reconciliation; **none is independently approved**.

| Provisional B2 word | Oxford source word/POS observation | Publisher locator | Review priority |
| --- | --- | --- | --- |
| resistance (noun) | Oxford 5000 **C1** | 7:1711 | Draft opposition-to-change sense; higher Oxford classification |
| retail (noun) | Oxford 5000 B2 | 3:534 | Retail business vs adjective |
| calm (adjective) | Oxford 3000 **B1** | 7:1871 | Lower Oxford adjective; distinguish verb and noun |
| client (noun) | Oxford 3000 **B1** | 7:1900 | Professional-service customer; lower Oxford level |
| expansion (noun) | Oxford 5000 B2 | 1:233 | Physical/business expansion |
| empire (noun) | Oxford 5000 B2 | 1:210 | Political empire vs business metaphor |
| significantly (adverb) | Oxford 3000 B2 | 12:3195 | Quantity change vs importance |
| reporting (noun) | Oxford 5000 B2 | 3:528 | Journalism vs internal reporting |
| closely (adverb) | Oxford 3000 B2 | 10:2698 | Careful attention vs physical proximity |
| constantly (adverb) | Oxford 3000 B2 | 10:2723 | Very frequently vs uninterrupted |
| contest (noun) | Oxford 3000 B2 | 10:2727 | Noun competition vs verb dispute |
| hardly (adverb) | Oxford 3000 **B1** | 8:2111 | Almost-not-at-all; lower Oxford level |
| motor (noun) | Oxford 3000 B2 | 11:3014 | Motor noun vs adjective |
| officially (adverb) | **No exact entry found in either inspected Oxford 3000/5000 PDF** | no page/line | Absence is NOT a CEFR label; separate credible exact-sense evidence needed |
| portion (noun) | Oxford 5000 B2 | 2:470 | Food serving vs general part; Myanmar gloss currently mixes both |
| peak (noun) | Oxford 5000 **C1** | 6:1568 | Maximum demand vs physical summit; higher Oxford level |
| reform (noun) | Oxford 5000 **C1** | 7:1677 | Institutional improvement; higher Oxford level |
| retirement (noun) | Oxford 5000 B2 | 3:535 | Act of retiring vs later period |
| solar (adjective) | Oxford 3000 B2 | 12:3203 | Solar energy vs general sun-related |
| somehow (adverb) | Oxford 5000 B2 | 3:576 | Unknown method vs despite difficulty |
| ultimate (adjective) | Oxford 5000 B2 | 3:663 | Final vs most important |
| unknown (adjective) | Oxford 3000 B2 | 12:3277 | Unknown cause vs unidentified person |
| automatically (adverb) | Oxford 5000 B2 | 1:46 | Machine-driven vs unthinking action |
| blind (adjective) | Oxford 3000 B2 | 10:2662 | Literal sight disability vs figurative use |

These are **publisher word/POS list observations only**; they do not verify the intended exact dictionary sense, the quality of the Myanmar gloss, example grammar, audio pronunciation, or an independently justified B2 placement. An absent core-list word is not evidence of exclusion from the English language or of any specific CEFR tier. All 24 remain held, with no automatic retiering.

## Source-integrity, human-signoff and CI safeguards

Created [fail-closed B2 source auditor](tools/audit_cefr_1000_oxford_b2_fourth_twentyfour.py) checking all 24 against frozen shortlist and original source Git blobs, publisher URLs/locators, immutable bilingual/example snapshots, 200-per-level uniqueness, risk tags, independent reviewer tasks and all false review/approval flags. Its self-test deliberately mutates each record's English, Myanmar, example, publisher URL, locator, publisher level, risk, approval, reviewer receipt and hidden reviewer field; plus nine scope/metadata/approval cases: **249 authored negative cases**.

Integrated the auditor into the existing **six parallel GitHub Actions A1/A2/B1/B2/C1/ALL structural lanes**, with negative tests in ALL, and into the **documentary no-deployment workflow**. [Structural run 40749583547](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40749583547), head `548bd8b55ee6be43fae48b7834b918702b4cb700`, **completed SUCCESS for all six jobs**; actual ALL job `123032361059` log confirms **24/24 source records checked and 249/249 mutations rejected**. This tests code and evidence integrity, not linguistic independence.

Extended [release-readiness auditor](tools/audit_cefr_1000_launch_readiness.py) with an independent content-hash-bound **24-word B2 exact-sense reconciliation requirement**. Every retained entry needs an actual human reviewer, direct publisher exact-sense B2 source and review receipt. The three lower, three higher and one unlisted Oxford observations require a separate substantive conflict/absence rationale. Added an **empty** `oxford_b2_fourth_twentyfour_review_receipts` array to [release evidence ledger](draft/CEFR-1000-RELEASE-EVIDENCE.json). A fabricated B2 receipt is tested and must fail. No approval flags were set.

A direct GitHub recursive-tree comparison against `main` on **2026-10-29** compared **4,661 protected files** (seven named production paths and all files under `audio/`): **0 changed/missing paths and 0 blob-SHA differences**. This is a current staging-to-main content check, not a guarantee of a future deployment's safety.

**Documentary no-deploy run:** [40749698886](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40749698886) was launched from head `af04201a826eb4b51d4d651a5db7521aa96c802d`. Its final job conclusion must be checked before claiming success; do not infer a pass from a queued or running status.

## Exact release counts and blockers

| Level | First-pass written | Independently approved | Editorial holds |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 200 |
| A2 | 200 | 0 | 200 |
| B1 | 200 | 0 | 200 |
| B2 | 200 | 0 | 200 |
| C1 | 200 | 0 | 200 |
| **Total** | **1,000** | **0** | **1,000** |

**Final George/Emma both-voice headword-and-example listening receipts: 0/1,000.** No human-independent English/Myanmar/example/exact-sense CEFR signoff; no complete final voice audio listening; no full desktop/mobile browser regression; no physical iPhone Safari test evidence; no measured GitHub Pages release artifact, bandwidth forecast or deployment confirmation. The 54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio and privacy assets remain protected. **No main modification, merge, publish or production launch.**
