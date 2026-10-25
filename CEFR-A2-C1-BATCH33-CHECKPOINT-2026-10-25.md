# Burmese English Academy — Batch33 staging editorial and QA checkpoint
**Date:** 25 October 2026 (SGT)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Status:** **UNVERIFIED STAGING HOLD — DO NOT MERGE OR PUBLISH**

## Substantive additions
- **44** newly drafted bilingual headwords, not approvals: A2 **3**, B1 **19**, B2 **20**, C1 **2**. Separate original English definitions, first-pass natural Myanmar glosses, original grammatical English examples.
- **44** separate source-evidence and independent editorial review tasks. All remain pending: English POS/sense, Myanmar exact meaning, example grammar, sense-specific CEFR, George/Emma listening and real iPhone Safari. Cambridge dictionary URLs are unvisited lookup destinations, **not observed source evidence**.
- **28** newly quarantined headwords for bad WordNet sense, named entities, abbreviations, unsupported tiers or harmful/outdated pool wording. These are reversible holds; no dictionary review or CEFR approval is claimed.
- Candidate preview was generated from the current post-batch32 staging checkout, not a stale preview. Actual GitHub Actions preview run [40182582252](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40182582252), job `121136570008`, completed/success. Its log showed A2 513, B1 550, B2 552, C1 407 already drafted; 46/332/614/874 remaining unheld candidates respectively. The preview does not independently validate WordNet sense or CEFR.
- Only **2** C1 entries drafted because most previewed C1 candidates have obviously unsupported or lower-level senses. Both new C1 entries remain marked high-risk for re-tiering. Quality takes precedence over a balanced-looking count.

## Exact unique first-draft inventory (confirmed by GitHub Actions ALL job)
| CEFR | Target | Written first drafts | Independently checked and approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 516 | 0 | 184 |
| B1 | 1,000 | 569 | 0 | 431 |
| B2 | 1,300 | 572 | 0 | 728 |
| C1 | 1,500 | 409 | 0 | 1,091 |
| **TOTAL** | **5,000** | **2,566** | **0** | **2,434** |

Unique A2–C1 first drafts **2,066**; unique quarantined candidate headwords **507**; historical duplicate draft rows **182** excluded. Quarantined items are **not** counted as written. The provisional pool's level labels are **not** independently validated CEFR evidence.

## Actual commits
- New staging-only candidate-preview workflow: `0d5b5fb4d28587d6af6f176f9fefca43bb7ef7b3`.
- New batch33 original editorial JSON: `a045e27a8083fad829e2b658958a2523f776733b`.
- Separate independent-review task JSON: `05c1faf3cd12258b17703c83c7e9c8470dc18217`.
- Reversible quarantine JSON: `c98a6676b52d59fa6128b52d52502b1d08e4ed4d`.
- Batch33 structural auditor: `3f44a15c97c654793f180dd8b4094fa8513dd778`.
- Five-way no-deploy workflow: `b467ffa4572c57cfeb7fd5de01f8bddc783a55c8`.

## Inspected CI — not a linguistic review
Actual [GitHub Actions batch33 run 40182718833](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40182718833), commit `b467ffa4572c57cfeb7fd5de01f8bddc783a55c8`. All five job statuses and decoded logs were inspected:
- A2 job `121136980911`: **completed/success**; `STAGING ONLY batch33 A2 PASS`.
- B1 job `121136980917`: **completed/success**; `STAGING ONLY batch33 B1 PASS`.
- B2 job `121136980883`: **completed/success**; `STAGING ONLY batch33 B2 PASS`.
- C1 job `121136980712`: **completed/success**; `STAGING ONLY batch33 C1 PASS`.
- ALL job `121136980870`: **completed/success**; `UNIQUE A2-C1 A2=516 B1=569 B2=572 C1=409 total=2066; independently approved=0`; `A1=500; A1-C1 written=2566; first drafts outstanding=2434; unique quarantine=507; legacy duplicate rows= 182`; `STAGING ONLY batch33 ALL PASS: 44 drafts, 28 new held, zero approvals; no audio/deploy`.
- Structural checks enforce duplicate exclusion, candidate POS and provisional tier alignment, Myanmar script presence, original example headword, false approval flags, pending independent review tasks, quarantine separation and empty public CEFR loader. **They do not prove language quality, source authenticity or pronunciation.**

## Editorial and release blockers
1. **0/5,000** independently approved for English exact sense/POS, natural Myanmar meaning, grammatical example, and sense-specific CEFR. Many candidates have bad WordNet senses; 507 are held and must be replaced or independently re-tiered as appropriate. Review the high-risk B2 nominalised forms and C1 `sometime` / `strictly` before acceptance.
2. **2,434** first drafts unwritten. Existing 182 legacy duplicate rows must remain excluded and resolved before any eventual corpus consolidation.
3. No complete new CEFR George/Emma recordings, no recording-by-recording listening approval, no complete audio manifest validation.
4. No full final-corpus browser/mobile test, **no physical iPhone Safari acceptance**, no final GitHub Pages storage/bandwidth clearance, no verified production deployment.
5. Production 54 lessons, existing IELTS 1,000 bank, current George/Emma audio and privacy systems were not modified. Public `cefr-vocabulary-data.js` remains `entries:[]`. All changes are staging-only, no merge, no publication, no completion notification.

**Result: useful editorial progress with a strict release hold.**
