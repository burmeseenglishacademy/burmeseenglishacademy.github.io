# CEFR-1000 complete historical source readback — 2026-11-04

**Scope:** staging-only documentary evidence, observed 2026-11-04 SGT. No independent approval, CEFR validation, audio signoff, or publication. Provisional shortlist blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

## Verified source-to-shortlist structural consistency

Read all seven historical JSON sources from the existing staging branch using GitHub file reads, and compared each returned Git blob SHA with every shortlist entry's `source_blob_sha`. At each recorded `source_index`, compared the source record's word, part of speech, English definition, Burmese gloss, example sentence and CEFR proposal against the shortlist. **All 1,000 of 1,000 records matched all six fields**, and **all seven historical source blobs matched their recorded SHAs**. No missing source indices or mismatched lexical fields were observed.

**Critical schema detail:** The original A1 and A2–C1 starter files store CEFR proposal in `level`. The five source-recovery batches store it in `proposed_level`. The 96 selected recovery records (21 A2, 75 C1) match the shortlist's `level` when the correct field is used. They are **not** 96 CEFR reassignments. An initial comparison incorrectly treated their missing `level` field as a mismatch; that interpretation was corrected in this report on the same day.

| Source path | Blob SHA | Selected records | Six-field mismatches |
|---|---|---:|---:|
| `draft/A1-EDITORIAL-STARTER.json` | `ff1e93f60828ef2f94c9146522ce94075183b0ae` | 200 | 0 |
| `draft/A2-C1-EDITORIAL-STARTER.json` | `b04dd85db5cfae131c25aa4c73109778991b6fdc` | 704 | 0 |
| `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json` | `7eaf88b9ed7687b26ccde713262f10fb209743a8` | 42 | 0 |
| `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json` | `da7df62123acfac89a0acedad4652ec499c7ed3d` | 32 | 0 |
| `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json` | `228c772697e4879f6b8a30f85709d188a1df266c` | 8 | 0 |
| `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json` | `96d54ddb6fdc204e8cbea45e8c97a6c98fb17b11` | 5 | 0 |
| `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json` | `6a10ae41eb41370a9a5b74d907fa395bb43e18d8` | 9 | 0 |

## What this does not establish

The sources are historical first-pass drafts, not independent publisher evidence. Git blob readback proves the current historical source bytes agree with recorded source SHA, not that proposed CEFR levels, Burmese glosses, English senses or examples are correct. Original Git commit pinning, publisher URLs with observation dates, independent human signoff and a CI-enforced source readback gate remain needed.

## Release gates and preservation

First-pass written / independently approved: A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0. All 1,000 remain held. Final approved manifest, 4,000 George/Emma headword-and-example audio assets with real listening review, browser/mobile regression, physical iPhone Safari evidence, Pages hosting clearance, confirmed production deployment and preserved production assets remain unverified. Never change main, the 54 lessons, separate IELTS bank, existing production audio or privacy protections to bypass these gates.

## Reproduction

Read `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` and every unique `source_path` from branch `cefr-5000-bilingual-qa-staging`. Compare fetched source blob SHA with `source_blob_sha`; index into source `entries[source_index]`; compare the six fields above, mapping `proposed_level` to shortlist `level` only for recovery-batch schemas. Treat missing or conflicting level fields as errors, not as approvals.
