# BEA Batch32 — inspected GitHub Actions evidence (2026-10-25)

**Status: STAGING HOLD.** These checks are structural only, not linguistic approval, audio listening or deployment.

## Exact first-draft inventory, confirmed by actual ALL-job decoded log
| CEFR | Target | Unique first drafts | Independently checked/approved | Unwritten |
|---|---:|---:|---:|---:|
| A1 | 500 | 500 | 0 | 0 |
| A2 | 700 | 513 | 0 | 187 |
| B1 | 1,000 | 550 | 0 | 450 |
| B2 | 1,300 | 552 | 0 | 748 |
| C1 | 1,500 | 407 | 0 | 1,093 |
| **Total** | **5,000** | **2,522** | **0** | **2,478** |

Batch32 adds **40 unique first-pass bilingual drafts** (A2 3 / B1 9 / B2 13 / C1 15), **40 independent review packets pending**, and **7 newly quarantined candidate words**. Total unique A2–C1 drafts **2,022**, unique quarantines **479**, excluded historical duplicate rows **182**. Sixteen proposed draft candidates already existed in batch30 and were removed before counting. Five proposed quarantine candidates were already held and were likewise excluded.

## Inspected CI run
- Actual GitHub Actions run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40181993261
- Head commit tested: `820975426430797902f2e23b3f13e93c14c5d45e`
- ALL job `121134790410`: **completed / success**. Decoded log: `UNIQUE A2-C1 A2=513 B1=550 B2=552 C1=407 total=2022; independently approved=0`; `A1=500; A1-C1 written=2522; first drafts outstanding=2478; legacy duplicate rows= 182`; `STAGING ONLY batch32 ALL PASS: 40 drafts, 7 new held, zero approvals; no audio/deploy`.
- A2 job `121134790367`: **completed / success**; decoded log `STAGING ONLY batch32 A2 PASS`.
- B1 job `121134790354`: **completed / success**; decoded log `STAGING ONLY batch32 B1 PASS`.
- B2 job `121134790319`: **completed / success**; decoded log `STAGING ONLY batch32 B2 PASS`.
- C1 job `121134790177`: **completed / success**; decoded log `STAGING ONLY batch32 C1 PASS`.
- All five actual job conclusions and relevant decoded log lines were inspected.

## Corrective staging commits and failure history (not hidden)
- Initial content/workflow commit `93fb68bcc27241ae3f0996f7bff31d4f269adf39`: failed structural QA because duplicate quarantines existed.
- Editorial wording correction `24fcb6ebee971696cb20f5b25d87b6066ca19c94`: refined seven draft senses/examples.
- Diagnostics `0c9440e7dc80a897a76ed7639301301329073527`: identified five duplicate holds.
- Quarantine correction `a23dabb99064e7d9bbdd1a1f8ae284fe2c8f1e70`: excluded five already-held words.
- Draft diagnostics `3587bb6c5f92e740c197127668b6adbf71eda9f6`: identified sixteen previously drafted candidates from stale preview output.
- Deduplication `fcba2befa88d6a68c07b59b652c862b4d289a62d`: retained 40 genuinely new drafts and 40 review tasks.
- Legacy quarantine-schema compatibility fix `820975426430797902f2e23b3f13e93c14c5d45e`: retained prior source references; five-way structural QA subsequently passed.
- Earlier failed workflow runs `40181817153`, `40181841990`, `40181863355`, `40181898842`, `40181921268`, `40181969716` were superseded by the inspected successful run above. Their failures are **not** counted as passes.

## Editorial and release blockers
- English POS/sense definitions are original drafts, not independently source-checked. Cambridge links in task packets are **future reference destinations**, not observations.
- Myanmar naturalness, example grammar and sense-specific CEFR assignments have **zero** independently approved entries; provisional C1 especially needs re-tiering.
- George/Emma CEFR audio generation and real listening, browser/mobile and physical iPhone Safari tests, GitHub Pages hosting/storage/bandwidth checks and verified production deployment are **not completed** by this batch.
- All files are staging-only; the public vocabulary loader remains `entries:[]`. No lesson, IELTS bank, existing audio, privacy code or live site was changed.

**No merge, no publication, no completion notification.**
