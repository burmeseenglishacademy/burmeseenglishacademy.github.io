# Burmese English Academy — Batch31 staging checkpoint (2026-10-25)
**HOLD: not independently verified; never merge or publish.**

## New editorial work
- **60** original first-pass bilingual drafts: A2 **8**, B1 **18**, B2 **18**, C1 **16**; original English sense definitions, natural Myanmar meaning drafts, complete example sentences. These are NOT independently checked.
- **60** separate independent source/evidence review tasks (English sense/POS, Myanmar naturalness, example grammar, sense-specific CEFR, both-voice listening), all pending. Reference URLs are **not observed sources**.
- **12** new reversible candidate holds for WordNet mismatches, specialised senses, named entities, acronyms and unsupported lexical forms.
- C1 assignments are especially unreliable: all 16 provisional C1 drafts explicitly flagged for **re-tier or quarantine**. No CEFR approval is inferred from a pool label.
- No source pages were consulted, no audio was generated or listened to, and no real iPhone Safari testing was performed.

## Exact unique written inventory (first drafts only)
| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 510 | 0 | 190 |
| B1 | 1,000 | 541 | 0 | 459 |
| B2 | 1,300 | 539 | 0 | 761 |
| C1 | 1,500 | 392 | 0 | 1,108 |
| **Total** | **5,000** | **2,482** | **0** | **2,518** |

A2–C1 unique written **1,982**; quarantine **472** unique; **182** legacy duplicate rows excluded. Counts to be independently checked by GitHub Actions, not self-certified.

## Staging safety
- `cefr-vocabulary-data.js` stays `entries:[]`; all new files are under `draft/`, `tools/`, `.github/workflows/` and this report.
- Workflow uses A2/B1/B2/C1/ALL matrix with **no deployment job** and read-only permissions.
- Production 54 lessons, IELTS 1,000 bank, existing George/Emma recordings and privacy code remain untouched by this batch.
- CI structural success **does not** mean linguistic accuracy or real listening.
- Outstanding: external source-based CEFR and English review; independent Myanmar/example review; re-tiering; all CEFR audio generation/listening; browser/mobile and physical iPhone Safari; hosting capacity; verified live deployment.

## GitHub Actions evidence
- Atomic batch31 content/workflow/auditor/report commit: `43cfe4107909da213efd6735dd226ace8e40b751`.
- Actual [batch31 GitHub Actions run 40178016350](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40178016350): **completed / success**, five matrix jobs inspected.
- A2 job `121122823084`: completed / success; decoded log `STAGING ONLY batch31 A2 PASS`.
- B1 job `121122823071`: completed / success; decoded log `STAGING ONLY batch31 B1 PASS`.
- B2 job `121122823057`: completed / success; decoded log `STAGING ONLY batch31 B2 PASS`.
- C1 job `121122823198`: completed / success; decoded log `STAGING ONLY batch31 C1 PASS`.
- ALL job `121122822896`: completed / success; decoded log reconciles **A2 510, B1 541, B2 539, C1 392**, A2–C1 **1,982**, A1–C1 **2,482**, **2,518** outstanding, **182** legacy duplicate rows excluded and **0** independent approvals.
- All five decoded job logs were inspected. These are **structural checks only**: no independent linguistic verification, actual audio listening, physical iPhone Safari test or production deployment.

