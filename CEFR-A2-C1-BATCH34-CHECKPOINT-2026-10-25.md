# Burmese English Academy — Batch34 high-throughput staging checkpoint
**Date:** 25 October 2026 (Singapore time)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Release status:** **UNVERIFIED — DO NOT MERGE, DEPLOY OR NOTIFY COMPLETION**

## Substantive work performed
- Prepared **95 new original bilingual first-pass drafts**, after deliberately rejecting two weak candidates from an initial 97: **A2 3, B1 47, B2 40, C1 5**. Every entry contains separate English definition, Myanmar gloss and original grammatical usage example. These are **not** independent linguistic approvals.
- Created **95 independent review/evidence packets** with distinct pending tasks for exact English sense/POS, natural Myanmar meaning, example grammar, sense-specific CEFR and George/Emma real listening and physical iPhone Safari. Dictionary links are **unvisited lookup destinations**, not evidence observed.
- Placed **82 additional provisional candidate words in reversible quarantine**: A2 13, B1 26, B2 28, C1 15. Reasons include named entities, inflected forms, misleading WordNet senses, obsolete or offensive wording, cultural/register mismatch, unsupported level and rare nominalisations. Two weak draft candidates (`supporting`, `seed`) were removed and quarantined rather than inflating the draft count.
- Refined several English senses and examples against the **unverified candidate pool clue**, especially `labour`, `incredibly`, `contribute` and `reverse`. This internal correction is **not** independent source-based review. All five provisional C1 additions remain **high-risk for CEFR reassignment**.
- Ran a fresh current-corpus candidate preview before drafting; the [preview run 40189507774](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40189507774) completed successfully, job `121157296205`. It reported 516/569/572/409 A2/B1/B2/C1 previously drafted and 40/306/583/863 remaining unheld candidates, respectively. This preview did not establish authoritative sense or CEFR.
- No audio was generated, no review flags were set true, and no public CEFR data was populated.

## Exact unique inventory — confirmed by the batch34 ALL job
| CEFR | Curriculum target | Unique first drafts | Independently approved | Still unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 519 | 0 | 181 |
| B1 | 1,000 | 616 | 0 | 384 |
| B2 | 1,300 | 612 | 0 | 688 |
| C1 | 1,500 | 414 | 0 | 1,086 |
| **Total** | **5,000** | **2,661** | **0** | **2,339** |

A2–C1 **2,161 unique first drafts**, **591 unique quarantined candidate headwords**, **182 historical duplicate draft rows excluded**. Quarantined words do **not** count as written or approved. Candidate tier labels are unverified and may require replacements outside the current provisional pool.

## Actual staging commits
1. Candidate-preview workflow: `7e02f54c784913a2a24a0c483247a99cfb1bd285`.
2. Initial 97 draft rows: `dbb0a0e05d8ba9824c02ff466236f72f6e966145`.
3. Remove two weak senses, refine definitions and examples, leave **95** drafts: `d32174b2cdaa9bfaa9e72755c60e363251a1c1b7`.
4. Independent-review packets: `6a3e7fbd144431175e6ed517da667e4d71b2d75f`.
5. Quarantine records: `b574f2a645e3f83371c060a0cc98ecfa92e774d2`.
6. Fail-closed cumulative/level-specific structural audit: `c153fc5104a9934e2dfd3c45ee2b84f0be77273f`.
7. Five-way no-deploy GitHub Actions workflow: `ccc8940392b512df92333eb1e3733f18cdd755e9`.

## Real GitHub Actions status and decoded job-log evidence
[Batch34 run 40189787932](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40189787932) on head `ccc8940392b512df92333eb1e3733f18cdd755e9`: **completed / success**. The five job records and decoded logs were inspected individually:

| Matrix job | Job ID | Actual conclusion | Log evidence |
|---|---:|---|---|
| A2 | `121158133352` | completed / success | `STAGING ONLY batch34 A2 PASS: 95 drafts, 82 new held, zero approvals; no audio/deploy` |
| B1 | `121158133172` | completed / success | `STAGING ONLY batch34 B1 PASS: 95 drafts, 82 new held, zero approvals; no audio/deploy` |
| B2 | `121158133369` | completed / success | `STAGING ONLY batch34 B2 PASS: 95 drafts, 82 new held, zero approvals; no audio/deploy` |
| C1 | `121158133361` | completed / success | `STAGING ONLY batch34 C1 PASS: 95 drafts, 82 new held, zero approvals; no audio/deploy` |
| ALL | `121158133445` | completed / success | `UNIQUE A2-C1 A2=519 B1=616 B2=612 C1=414 total=2161; independently approved=0`; `A1=500; A1-C1 written=2661; first drafts outstanding=2339; unique quarantine=591; legacy duplicate rows=182` |

These are **structural, deduplication, provenance-flag and quarantine checks**, not independent validation of linguistic quality, CEFR, pronunciation, real-device behaviour or hosting.

## Release blockers and production preservation
1. **0/5,000** independently checked and approved for exact English sense/POS, natural Myanmar translation, example grammar and sense-specific CEFR. The 95 new review tasks are pending and the provisional corpus contains many suspect senses. 591 candidate words require replacement or independent disposition.
2. **2,339** first drafts still unwritten; 182 historical duplicate draft rows excluded from inventory. No placeholders or quarantined words counted as completion.
3. **No complete new CEFR George/Emma audio collection**, no recording-by-recording listening validation, no complete audio manifest or final pronunciation sign-off.
4. **No final browser/mobile or physical iPhone Safari acceptance**, and no confirmed GitHub Pages storage/bandwidth clearance for the expanded corpus.
5. Production `main` was read as `dca0db7aa30118ecc18350db8dc406e6cac91554`, unchanged from the prior checkpoint. Production 54 lessons, IELTS 1,000 bank, current George/Emma recordings and privacy protections were **not edited**. Staging public loader `cefr-vocabulary-data.js` was read and remains `entries:[]` with unpublished status. No merge, publication or completion notification.

**Outcome:** 95 substantive first drafts and 82 quarantine decisions added to staging; real five-job structural CI passed; editorial/audio/device/hosting/release gates remain closed.
