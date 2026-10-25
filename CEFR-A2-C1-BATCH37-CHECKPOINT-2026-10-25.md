# CEFR 5,000 — batch37 staging checkpoint (25 October 2026)
**Branch:** `cefr-5000-bilingual-qa-staging`. **Decision: UNVERIFIED — DO NOT MERGE OR DEPLOY.**

## Actual substantive additions
- 44 original bilingual drafts: A2 0, B1 14, B2 18, C1 12. Distinct original English definition, Myanmar meaning and grammatical example fields.
- 44 independent review packets for exact dictionary sense/POS, Myanmar, example, CEFR tier and George/Emma listening. Lookup URLs are **unvisited** and not evidence.
- 20 reversible risk holds: A2 0, B1 7, B2 7, C1 6, for named entities, nonstandard POS, rare senses, abbreviations and dated register. Not independently reviewed exclusions.
- No unheld unflagged A2 candidates in the preceding preview; no A2 filler was invented.
- No changes to production 54 lessons, IELTS 1000, audio, privacy or site loader.

## Exact unique first-pass draft and independent approval totals
| Level | Target | Written | Independently approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 521 | 0 | 179 |
| B1 | 1000 | 680 | 0 | 320 |
| B2 | 1300 | 674 | 0 | 626 |
| C1 | 1500 | 435 | 0 | 1065 |
| **Total** | **5000** | **2810** | **0** | **2190** |

A2–C1 unique written 2310; held 741; historical duplicate draft rows excluded 182. No new audio was generated or listened to; no iPhone Safari, browser/mobile or hosting release approval. The C1 provisional levels, especially observation, prospect, retreat, curriculum and variable, need sense-specific evidence; re-tier if unsupported. No dictionary pages or independent Myanmar reviewer consulted. GitHub Actions checks are structural only. Batch37 commit and job IDs are to be checked from GitHub; **CI pending** at commit creation.

## Verified GitHub commit and real CI inspection (25 October 2026)
- Batch37 staging source commit: `f66754e5500d94252d82ef0ff3b3bbac233ee43c` (44 drafts, 44 review packets, 20 holds, level auditor, workflow and this report).
- GitHub Actions run [40202944557](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40202944557): **completed / success** at inspection. All five individual jobs and decoded logs inspected:
  - A2 job `121197771930`: completed/success, `STAGING ONLY batch37 A2 PASS: 44 drafts, 20 held, zero approvals; no audio/deploy`.
  - B1 job `121197771811`: completed/success, corresponding B1 PASS log.
  - B2 job `121197771936`: completed/success, corresponding B2 PASS log.
  - C1 job `121197771918`: completed/success, corresponding C1 PASS log.
  - ALL job `121197772022`: completed/success; `A2=521 B1=680 B2=674 C1=435 total=2310`; `A1-C1 written=2810; outstanding=2190; quarantine=741; legacy duplicate rows=182`.
- Structural QA passing **does not** imply any independent English, Myanmar, CEFR, example or pronunciation approval. Production remains untouched.
