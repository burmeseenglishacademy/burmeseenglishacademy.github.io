# Burmese English Academy — CEFR 5,000 batch36 staging checkpoint
**Date:** 25 October 2026, Singapore time (21:40)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release decision:** **UNVERIFIED — DO NOT MERGE, DEPLOY OR NOTIFY COMPLETION**

## Actual new work
- Prepared **60 original bilingual first-pass drafts** with separately labelled English definitions, natural Myanmar gloss drafts and grammatical original example sentences: **A2 0, B1 28, B2 25, C1 7**. No filler, no copied dictionary definitions, no placeholders. These are **NOT independently checked or CEFR-approved**.
- Added **60 distinct source-evidence and editorial review tasks** for exact dictionary sense/POS, Myanmar meaning, original example, sense-specific CEFR and eventual George/Emma listening. Cambridge lookup links are **unvisited references**, not observed evidence.
- Reversibly quarantined **45 additional candidates** (**A2 0, B1 10, B2 15, C1 20**) for named entities, WordNet sense/POS mismatches, nonstandard forms, gerunds, plural-only senses, specialist meanings, questionable tier assignments and potentially dated register. Holds are **not independently confirmed exclusions**.
- The current candidate preview found **no unflagged A2 candidates among the 19 remaining unheld A2 clues**. Consequently no A2 filler was written; A2 expansion requires evidence-based replacement or re-tiering rather than manufacturing a draft.
- Added a current-corpus candidate triage workflow and a five-job read-only, no-deploy structural audit; checked actual job logs and fixed two audit bugs (stale BATCH35 file paths and zero-A2 Counter handling) plus the `commit` example that lacked the exact headword. Earlier failing runs remain visible as genuine failures, not retroactively marked successful.

## Exact unique written versus independently approved
| Provisional level | Target | Written first drafts | Independently checked and approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 521 | 0 | 179 |
| B1 | 1,000 | 666 | 0 | 334 |
| B2 | 1,300 | 656 | 0 | 644 |
| C1 | 1,500 | 423 | 0 | 1,077 |
| **Total** | **5,000** | **2,766** | **0** | **2,234** |

**A2–C1 unique drafts:** 2,266. **Unique held candidates:** 721. **Historical duplicate draft rows excluded:** 182. No approvals were inferred from passing automated checks. All levels and exact senses remain provisional.

## GitHub staging commits
- Candidate triage workflow: `94737b20da16ec1f6302d6d64439888156d9abc8`.
- 60 bilingual drafts: `4b7139673dad9202462ea36582a4eee8a3783576`; independent review packets: `1cd6548f4619b1e30413512d392467b21a391c01`.
- 45 candidate holds: `edeb0cc9c44d7b368402f857076fd1f7088f5fac`.
- Cumulative and level-specific auditor: `6b69cd43299b5de214f932524b13355f84024b76`.
- Five-way workflow: `24cbda493708d7e58f0ddf46332e2fa83d46a2cd`.
- Corrected workflow path filters: `da5e54048d896c3ed20e4923c453d73c4196c0d6`.
- Corrected auditor file paths: `5111a9335fa72689e8da1cd41781395e67a38bd2`; zero-count logic: `c1c26a7b8affaf07a30800f7b1bc89ba612c70b3`.
- Corrected original example for `commit`: `211000b4774f4cdbe6461f7d306a6eaa1ab506c2`.

## Real GitHub Actions results and decoded log checks
Candidate triage run **40198338582** completed **success**; log showed A2=0 unflagged, B1=155, B2=406 and C1=743 unflagged candidate clues before this batch, and confirmed the CEFR loader remained empty. These are **not verified usable word counts**.

[Batch36 final structural workflow run](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40198670783) tested commit `211000b4774f4cdbe6461f7d306a6eaa1ab506c2` and finished **completed / success** (25 October 2026 13:40:29 UTC). Decoded individual logs:
| Level job | Job ID | Result | Log confirmation |
|---|---:|---|---|
| A2 | `121184958562` | completed / success | `STAGING ONLY batch36 A2 PASS: 60 drafts, 45 held, zero approvals; no audio/deploy` |
| B1 | `121184958816` | completed / success | `STAGING ONLY batch36 B1 PASS: 60 drafts, 45 held, zero approvals; no audio/deploy` |
| B2 | `121184958601` | completed / success | `STAGING ONLY batch36 B2 PASS: 60 drafts, 45 held, zero approvals; no audio/deploy` |
| C1 | `121184958470` | completed / success | `STAGING ONLY batch36 C1 PASS: 60 drafts, 45 held, zero approvals; no audio/deploy` |
| ALL | `121184958621` | completed / success | `UNIQUE A2-C1 A2=521 B1=666 B2=656 C1=423 total=2266; independently approved=0`; `A1=500; A1-C1 written=2766; outstanding=2234; quarantine=721; legacy duplicate rows=182` |

**Prior failures:** workflow runs `40198563659`, `40198573001`, `40198605498`, and `40198635715` failed during development. The first runs read old batch35 paths or incorrectly expected zero-A2 Counter keys; the last had an example containing only `committed` rather than the exact lemma `commit`. Corrections were committed and the final five-way run passed. A green CI result means **structural checks only**, not linguistic approval.

## Unresolved editorial, audio, device and hosting blockers
1. **0 of 5,000** independently approved for English sense/POS, natural Myanmar gloss, original example and sense-specific CEFR; all 60 new evidence packets pending. URLs were not visited or independently reviewed.
2. **2,234** entries still need original first drafts; **721** held candidates need evidence-based re-tiering, replacement or rejection. The 182 duplicate historical rows remain excluded from counts.
3. New high-risk drafts needing priority review: B1 `corporation`, `resolution` (formal decision), `random`; B2 `genetic`, `arena` (figurative field), `compensation`, `density`; C1 `chancellor` (UK office), `combine` (harvester), `controller` (finance), `damages` (legal), `haven`, `mechanics`, `reportedly`. Their level assignments may be wrong even if the sentences are grammatical.
4. No new CEFR George/Emma pronunciation collection was generated or listened to in this batch. Existing production recordings must not be confused with validated new CEFR audio.
5. Full browser/mobile corpus regression, real physical iPhone Safari playback and pronunciation checks, hosting storage/bandwidth clearance, and verified production CEFR deployment **have not passed**.

## Production isolation
Production `main` was observed at `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from batch35. Batch36 changed only staging drafts, review tasks, holds, QA scripts/workflows and this report. The unpublished CEFR loader remains `entries:[]`; no production 54-lesson content, IELTS 1,000 bank, existing George/Emma audio or privacy feature was edited. **No merge or live deployment.**

**Outcome:** 60 substantive first-pass bilingual drafts and 45 reversible candidate holds, with five actual parallel CI successes and all independent editorial/audio/device/hosting release gates still closed.
