# CEFR-1000 historical provenance full-source readback — 2026-11-04

**Scope:** staging-only evidence; no approval, publication, or independent linguistic validation. Observed 2026-11-04 (SGT). Provisional inventory blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

## Direct readback results

Fetched all seven historical source JSON files from the existing staging branch using GitHub file reads, compared returned blob SHA with the per-entry historical SHA, and compared all 1,000 provisional entries at their recorded source indices across word, part of speech, English definition, Burmese gloss, example sentence, and level. All seven current source blobs match the recorded SHA. **904/1,000 entries match all six compared fields; 96/1,000 retain the same lexical content but differ in level.** Every level difference is in a recovery batch; none is evidence of CEFR validation. No other compared field differs. This authenticates current blob-to-shortlist consistency, not publisher CEFR evidence or independent review.

| Historical source | Source blob SHA | Selected | Level differences |
|---|---|---:|---:|
| [draft/A1-EDITORIAL-STARTER.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A1-EDITORIAL-STARTER.json) | `ff1e93f60828ef2f94c9146522ce94075183b0ae` | 200 | 0 |
| [draft/A2-C1-EDITORIAL-STARTER.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-EDITORIAL-STARTER.json) | `b04dd85db5cfae131c25aa4c73109778991b6fdc` | 704 | 0 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json) | `da7df62123acfac89a0acedad4652ec499c7ed3d` | 32 | 32 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json) | `228c772697e4879f6b8a30f85709d188a1df266c` | 8 | 8 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json) | `96d54ddb6fdc204e8cbea45e8c97a6c98fb17b11` | 5 | 5 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json) | `6a10ae41eb41370a9a5b74d907fa395bb43e18d8` | 9 | 9 |
| [draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json) | `7eaf88b9ed7687b26ccde713262f10fb209743a8` | 42 | 42 |

### Level-change transitions

- undefined → A2: 21 entries
- undefined → C1: 75 entries

### All 96 source-to-shortlist level discrepancies (not approvals)

| Headword | Source level | Shortlist level | Source path / index |
|---|---|---|---|
| \\|r\\|a\\|i\\|n\\|c\\|o\\|a\\|t\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#0` |
| \\|l\\|u\\|n\\|c\\|h\\|b\\|o\\|x\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#1` |
| \\|t\\|o\\|o\\|t\\|h\\|a\\|c\\|h\\|e\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#2` |
| \\|s\\|u\\|n\\|s\\|c\\|r\\|e\\|e\\|n\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#3` |
| \\|a\\|c\\|q\\|u\\|i\\|e\\|s\\|c\\|e\\|n\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#20` |
| \\|a\\|m\\|e\\|l\\|i\\|o\\|r\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#21` |
| \\|a\\|n\\|t\\|a\\|g\\|o\\|n\\|i\\|s\\|t\\|i\\|c\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#22` |
| \\|a\\|r\\|b\\|i\\|t\\|r\\|a\\|r\\|i\\|n\\|e\\|s\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#23` |
| \\|a\\|s\\|s\\|i\\|d\\|u\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#24` |
| \\|c\\|a\\|t\\|h\\|a\\|r\\|s\\|i\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#25` |
| \\|c\\|i\\|r\\|c\\|u\\|m\\|v\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#26` |
| \\|c\\|o\\|a\\|l\\|e\\|s\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#27` |
| \\|c\\|o\\|n\\|j\\|e\\|c\\|t\\|u\\|r\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#28` |
| \\|c\\|o\\|n\\|s\\|c\\|i\\|e\\|n\\|t\\|i\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#29` |
| \\|c\\|u\\|l\\|p\\|a\\|b\\|i\\|l\\|i\\|t\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#31` |
| \\|d\\|i\\|s\\|p\\|a\\|r\\|a\\|g\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#32` |
| \\|d\\|i\\|s\\|p\\|r\\|o\\|p\\|o\\|r\\|t\\|i\\|o\\|n\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#33` |
| \\|d\\|i\\|s\\|s\\|o\\|n\\|a\\|n\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#34` |
| \\|e\\|l\\|u\\|c\\|i\\|d\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#35` |
| \\|e\\|n\\|t\\|r\\|e\\|n\\|c\\|h\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#36` |
| \\|e\\|q\\|u\\|a\\|n\\|i\\|m\\|i\\|t\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#37` |
| \\|e\\|q\\|u\\|i\\|v\\|o\\|c\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#38` |
| \\|e\\|x\\|t\\|r\\|a\\|p\\|o\\|l\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#39` |
| \\|f\\|o\\|r\\|t\\|i\\|t\\|u\\|d\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#40` |
| \\|i\\|n\\|a\\|d\\|v\\|e\\|r\\|t\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#41` |
| \\|i\\|r\\|r\\|e\\|v\\|o\\|c\\|a\\|b\\|l\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#43` |
| \\|m\\|i\\|s\\|c\\|o\\|n\\|s\\|t\\|r\\|u\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#44` |
| \\|o\\|b\\|f\\|u\\|s\\|c\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#45` |
| \\|p\\|e\\|r\\|p\\|e\\|t\\|u\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#46` |
| \\|r\\|e\\|l\\|i\\|n\\|q\\|u\\|i\\|s\\|h\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#47` |
| \\|s\\|u\\|p\\|e\\|r\\|f\\|l\\|u\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#48` |
| \\|s\\|a\\|l\\|i\\|e\\|n\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json#49` |
| \\|s\\|h\\|o\\|e\\|l\\|a\\|c\\|e\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#0` |
| \\|b\\|o\\|o\\|k\\|s\\|h\\|e\\|l\\|f\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#1` |
| \\|d\\|o\\|o\\|r\\|m\\|a\\|t\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#3` |
| \\|a\\|b\\|s\\|t\\|r\\|u\\|s\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#25` |
| \\|a\\|c\\|r\\|i\\|m\\|o\\|n\\|i\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#26` |
| \\|a\\|d\\|u\\|l\\|a\\|t\\|i\\|o\\|n\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#27` |
| \\|a\\|f\\|f\\|a\\|b\\|l\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#28` |
| \\|a\\|l\\|a\\|c\\|r\\|i\\|t\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH59.json#29` |
| \\|s\\|h\\|o\\|e\\|b\\|o\\|x\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json#0` |
| \\|s\\|a\\|u\\|c\\|e\\|p\\|a\\|n\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json#1` |
| \\|w\\|a\\|s\\|h\\|c\\|l\\|o\\|t\\|h\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json#2` |
| \\|p\\|o\\|s\\|t\\|c\\|a\\|r\\|d\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json#3` |
| \\|s\\|u\\|n\\|f\\|l\\|o\\|w\\|e\\|r\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH60.json#4` |
| \\|d\\|u\\|s\\|t\\|b\\|i\\|n\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#1` |
| \\|b\\|a\\|t\\|h\\|r\\|o\\|b\\|e\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#3` |
| \\|s\\|n\\|o\\|w\\|m\\|a\\|n\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#6` |
| \\|h\\|a\\|i\\|r\\|b\\|r\\|u\\|s\\|h\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#8` |
| \\|t\\|o\\|o\\|t\\|h\\|b\\|r\\|u\\|s\\|h\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#9` |
| \\|c\\|r\\|o\\|s\\|s\\|r\\|o\\|a\\|d\\|s\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#11` |
| \\|w\\|h\\|e\\|e\\|l\\|b\\|a\\|r\\|r\\|o\\|w\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#12` |
| \\|g\\|r\\|e\\|e\\|n\\|h\\|o\\|u\\|s\\|e\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#13` |
| \\|b\\|a\\|c\\|k\\|s\\|e\\|a\\|t\\| | undefined | A2 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH61.json#15` |
| \\|a\\|m\\|b\\|i\\|v\\|a\\|l\\|e\\|n\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#8` |
| \\|a\\|n\\|a\\|c\\|h\\|r\\|o\\|n\\|i\\|s\\|m\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#9` |
| \\|a\\|n\\|t\\|i\\|p\\|a\\|t\\|h\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#10` |
| \\|a\\|r\\|b\\|i\\|t\\|r\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#11` |
| \\|b\\|e\\|l\\|l\\|i\\|g\\|e\\|r\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#12` |
| \\|b\\|e\\|n\\|e\\|v\\|o\\|l\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#13` |
| \\|b\\|r\\|e\\|v\\|i\\|t\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#14` |
| \\|c\\|i\\|r\\|c\\|u\\|m\\|s\\|p\\|e\\|c\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#15` |
| \\|c\\|o\\|e\\|r\\|c\\|i\\|o\\|n\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#16` |
| \\|c\\|o\\|n\\|u\\|n\\|d\\|r\\|u\\|m\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#18` |
| \\|c\\|o\\|r\\|r\\|o\\|b\\|o\\|r\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#19` |
| \\|c\\|r\\|e\\|d\\|e\\|n\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#20` |
| \\|d\\|e\\|f\\|e\\|r\\|e\\|n\\|c\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#21` |
| \\|d\\|e\\|l\\|i\\|n\\|e\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#22` |
| \\|d\\|i\\|c\\|h\\|o\\|t\\|o\\|m\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#23` |
| \\|d\\|i\\|s\\|s\\|e\\|m\\|i\\|n\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#25` |
| \\|e\\|c\\|l\\|e\\|c\\|t\\|i\\|c\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#26` |
| \\|e\\|f\\|f\\|i\\|c\\|a\\|c\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#27` |
| \\|e\\|m\\|b\\|e\\|l\\|l\\|i\\|s\\|h\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#28` |
| \\|e\\|n\\|d\\|e\\|m\\|i\\|c\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#29` |
| \\|e\\|n\\|i\\|g\\|m\\|a\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#30` |
| \\|e\\|p\\|h\\|e\\|m\\|e\\|r\\|a\\|l\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#31` |
| \\|e\\|x\\|a\\|c\\|e\\|r\\|b\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#32` |
| \\|e\\|x\\|o\\|n\\|e\\|r\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#33` |
| \\|f\\|a\\|l\\|l\\|a\\|c\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#34` |
| \\|f\\|e\\|r\\|v\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#35` |
| \\|g\\|a\\|l\\|v\\|a\\|n\\|i\\|z\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#36` |
| \\|i\\|n\\|c\\|o\\|n\\|g\\|r\\|u\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#37` |
| \\|i\\|n\\|t\\|r\\|o\\|s\\|p\\|e\\|c\\|t\\|i\\|o\\|n\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#38` |
| \\|j\\|u\\|x\\|t\\|a\\|p\\|o\\|s\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#39` |
| \\|m\\|e\\|t\\|i\\|c\\|u\\|l\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#40` |
| \\|m\\|i\\|t\\|i\\|g\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#41` |
| \\|n\\|u\\|a\\|n\\|c\\|e\\|d\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#42` |
| \\|p\\|r\\|a\\|g\\|m\\|a\\|t\\|i\\|c\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#43` |
| \\|p\\|r\\|e\\|c\\|e\\|d\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#44` |
| \\|s\\|c\\|r\\|u\\|t\\|i\\|n\\|i\\|z\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#45` |
| \\|s\\|t\\|r\\|i\\|n\\|g\\|e\\|n\\|t\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#46` |
| \\|t\\|e\\|n\\|a\\|c\\|i\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#47` |
| \\|u\\|b\\|i\\|q\\|u\\|i\\|t\\|o\\|u\\|s\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#48` |
| \\|v\\|i\\|n\\|d\\|i\\|c\\|a\\|t\\|e\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#49` |
| \\|v\\|i\\|l\\|i\\|f\\|y\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#50` |
| \\|w\\|h\\|i\\|m\\|s\\|i\\|c\\|a\\|l\\| | undefined | C1 | `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH57.json#51` |

## Required safeguards and editorial next steps

1. Treat the 96 remapped levels as **explicit unresolved editorial conflicts**, requiring source-backed exact-sense CEFR justification and human-independent review; do not silently treat historical source levels or provisional levels as authoritative.
2. Add an automated staging gate comparing all historical source records and their immutable Git blob SHAs, with a documented, separately approved exception ledger for level remaps. A plain six-field equality requirement would currently fail for 96 known remaps; it must not auto-approve them.
3. Require original publisher URLs, observed dates, specific sense/POS, evidence quality and fluent Myanmar/example review for every entry. Historical source files and WordNet are not CEFR authorities.
4. Continue to block release: A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0 first-pass written/independently approved; all 1,000 held. Audio (4,000 George/Emma headword/example recordings) and actual listening signoff, browser/mobile and physical iPhone Safari review, Pages hosting, and confirmed deployment remain unverified. Preserve production 54 lessons, separate IELTS bank, existing audio and privacy.

**Reproducibility:** Fetch `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` and each distinct `source_path` at branch `cefr-5000-bilingual-qa-staging`; verify fetched blob SHA equals `source_blob_sha`; compare `source.entries[source_index]` against the shortlist entry for six fields listed above. This is a current-branch GitHub API readback; independently pinned historical commits and a protected exception ledger remain future gates.
