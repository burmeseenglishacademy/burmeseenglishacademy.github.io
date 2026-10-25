# Burmese English Academy CEFR 5,000 — Batch39 staging checkpoint
**Date:** 25 October 2026 (Singapore; final CI observed 15:55 UTC)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release state:** **UNVERIFIED_DRAFT_DO_NOT_PUBLISH — NO MERGE OR COMPLETION NOTIFICATION**

## Substantive work committed
- **52 original first-pass bilingual vocabulary drafts**: A2 **0**, B1 **15**, B2 **25**, C1 **12**. Every entry has a separate English definition, natural Myanmar first-pass meaning and original grammatical usage sentence. They are **not independently verified**.
- **52 separate, uncompleted evidence-review packets** with distinct English dictionary sense/POS, Myanmar meaning, sentence grammar/originality, sense-specific CEFR and George/Emma listening/physical-iPhone stages. Cambridge URLs are **unvisited destinations**, never claimed as observed evidence.
- **20 reversible quarantine holds**: A2 **0**, B1 **8** (likely lower CEFR levels or identity/sense issues), B2 **8** (names/places and WordNet person-name senses), C1 **4** (named entity, surname, river and demonym risks). These are not proven permanent exclusions.
- A real staging-only candidate preview ran: **19** A2 undrafted/unheld candidates remain, but **0** pass the current elementary WordNet-clue suspicion filter; no A2 filler was invented. This filter is a triage heuristic, **not** an independent CEFR source.
- Self-audit corrected the **carbon** example to use the chemical element sense and improved the **craft** collocation; explicitly flagged **hybrid** (WordNet linguistic-hybrid sense versus general combination) and **breakdown** (WordNet order disruption versus communication failure) for priority independent sense review.
- A **five-job parallel level-specific GitHub Actions structural QA** now checks batch39 and the complete historical unique-word ledger, fails on unapproved evidence flags, and compares protected production content, IELTS bank, George/Emma audio and privacy files against `main`.

## Exact unique written / independently approved
| Level | Target | Written first-pass | Independently approved | Not yet written |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 521 | 0 | 179 |
| B1 | 1,000 | 715 | 0 | 285 |
| B2 | 1,300 | 724 | 0 | 576 |
| C1 | 1,500 | 462 | 0 | 1,038 |
| **Total** | **5,000** | **2,922** | **0** | **2,078** |

**Unique A2–C1 drafts:** 2,422; **unique reversible holds:** 781; **historical duplicate draft rows excluded:** 182. The A1 500 are first-pass drafts, not independently approved. Source-evidence tasks are not evidence.

## GitHub commits and actual CI evidence
- Candidate preview workflow commit: `21eed368dde36b675f5fa8317f749a8706638212`.
- 52 drafts, 52 evidence tasks, 20 holds, structural auditor and five-job workflow: `e7c4a853d5f29fc368b104e4d92fd87eea81765f`.
- Self-audit correction and high-priority sense mismatch flags: `ab644f02dc0817cbbd934fd7ffa6e5b3ae53a518`.
- Candidate preview [run 40208954903](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40208954903) **completed/success**; decoded job log inspected: `LEVEL=A2 drafted=521 remaining_unheld=19 candidate_clue_not_flagged=0`.
- Initial batch39 [run 40209161452](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40209161452) **completed/success** (five jobs).
- **Final corrected batch39** [run 40209229882](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40209229882), head `ab644f02dc0817cbbd934fd7ffa6e5b3ae53a518`: **completed/success**, all five jobs and decoded logs individually inspected:

| Level/job | GitHub job ID | Observed status | Log evidence |
|---|---:|---|---|
| A2 | `121216684431` | completed / success | `STAGING ONLY batch39 A2 PASS: 52 drafts, 20 holds, zero approvals; no audio/deploy` |
| B1 | `121216684311` | completed / success | corresponding B1 PASS |
| B2 | `121216684410` | completed / success | corresponding B2 PASS |
| C1 | `121216684158` | completed / success | corresponding C1 PASS |
| ALL | `121216684514` | completed / success | `A1-C1 written=2922; outstanding=2078; quarantine=781; legacy duplicate rows=182` and `PASS: production lesson, IELTS, George/Emma audio and privacy assets unchanged` |

These are **structural/code checks only**. They do **not** independently establish correct English senses, natural Myanmar translation, CEFR tier, example quality, recorded pronunciation or iPhone playback.

## Release blockers and production protection
1. **0/5,000 independently approved** for English sense/POS, Myanmar meaning, sentence and sense-specific CEFR level. All 52 new source review tasks are pending with `source_observed=false`; two explicit WordNet sense mismatches need priority review. Numerous C1 candidates may belong to lower levels.
2. **2,078 entries remain unwritten**, and **781** candidate holds need qualified review or replacement. A2's remaining 19 unheld candidates all fail the present suspicion heuristic; do not fill the A2 quota from weak clues.
3. **No new batch39 George/Emma audio generated or actually listened to**; existing production recordings do not validate this CEFR bank. Full CEFR pronunciation inventory and listening review remain incomplete.
4. No complete CEFR browser/mobile or **real physical iPhone Safari** checks, no final hosting storage/bandwidth approval and no verified CEFR production deployment.
5. `cefr-vocabulary-data.js` remains `entries:[]` and release-blocked. The final ALL job confirmed protected production files unchanged against `main`; production `main` head was `dca0db7aa30118ecc18350db8dc406e6cac91554` when read. Existing **54 lessons, IELTS 1,000 bank, George/Emma production audio and privacy** were preserved.

**Conclusion:** 52 useful new first-pass bilingual drafts and 20 candidate holds advanced on staging, five actual parallel CI jobs passed, and independent linguistic/audio/device/release validation remains **unfulfilled**. **NOT READY TO MERGE, PUBLISH OR NOTIFY COMPLETION.**
