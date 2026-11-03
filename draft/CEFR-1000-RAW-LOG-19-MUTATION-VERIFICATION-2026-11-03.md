# CEFR-1000 staging CI raw-log verification — 2026-11-03 (19:51 SGT)

**Scope:** USER-APPROVED 1,000 total (A1/A2/B1/B2/C1: 200 each). Staging only; no independent linguistic approval, release, or production edits.

## Directly inspected GitHub Actions evidence

- Structural workflow run [41607329248](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41607329248), tested commit `fe08206955bb05511ebc542aecf708f6725f445f`: all six job conclusions **success**. Jobs: ALL `125820327690`, A2 `125820327970`, B2 `125820327999`, B1 `125820328011`, A1 `125820328040`, C1 `125820328055`.
- Documentary workflow run [41607329238](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41607329238), same tested commit: documentary job `125820327495` conclusion **success**.
- **Previously unresolved evidence gap closed:** downloaded raw ALL-job log, timestamp `2026-11-03T08:59:04.4457659Z`: `PASS: 19/19 synthetic inventory and approval forgeries rejected; no independent signoff`. Next line: `PASS: provisional 1000 inventory structure and zero-approval hold only.` This establishes execution of all 19 mutation cases in the ALL job, **not** human verification. Raw A2 and documentary logs were also inspected; no inference that every individual lane executed 19 cases is needed.
- Source checker path `tools/check_cefr_1000_provisional_inventory.py`, fetched staging blob `ce87d190a6bb5395e4e9e8e22ceaebc3b6c8fda8`. Its code has 19 named adversarial mutations, checks 200 per level, editorial hold, false approval flags, and provisional-only release status.

## Important checker limitation / next engineering work

The checker currently validates `source_blob_sha` **format** (40 lowercase hex characters), not that the SHA identifies the correct immutable source file. `source_path` is checked for nonempty text, not verified existence/content. `source_index` is checked as nonnegative integer, not cross-checked against source records. Consequently a well-formed invented SHA/path/index could pass this specific checker. Add source-path allowlists and immutable blob/content cross-checks with tests before treating historical provenance as authenticated. Likewise casefold headword uniqueness does not itself prove sense-level deduplication or genuine CEFR placement.

## Counts and release blockers

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

All 1,000 remain on editorial hold. Independently verified exact-sense English, Myanmar, example and CEFR signoff; approved manifest; 4,000 George/Emma headword/example audio assets and real listening review; browser/mobile regression; physical iPhone Safari QA; GitHub Pages limits; production asset preservation and deployment confirmation are **not established** by these runs. **NO MERGE, NO PUBLISH, NO PRODUCTION CHANGE.** This report is documentary and itself is not certified by the cited earlier runs.
