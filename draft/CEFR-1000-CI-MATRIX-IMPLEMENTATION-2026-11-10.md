# CEFR-1000 parallel staging CI implementation (2026-11-10)

Scope: **1,000 total, 200 each A1/A2/B1/B2/C1**. Target branch: `cefr-5000-bilingual-qa-staging`. This is an implementation specification, **not a claim that GitHub Actions ran**.

## Five parallel level jobs

Use `strategy.matrix.level: [A1, A2, B1, B2, C1]`, `fail-fast: false`, checkout staging, Python 3.11. Each job runs `python3 scripts/audit_cefr1000_provisional.py`, then reads `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` and asserts exactly 200 entries for its level, all explicitly `editorial_hold == true`, `release_approved == false`, and `independently_approved_by_level[level] == 0`. The whole-inventory auditor checks total 1,000, normalization and required fields. Any exception must fail the job; no `continue-on-error`.

## Separate adversarial and semantic-hold jobs

Run `python3 -m unittest discover -s tests -p 'test_cefr1000_*.py' -v`. Separately run `scripts/cefr1000_editorial_risk_queue.py`, require its *expected* exit code 2 while known semantic risks remain, parse JSON, and require `release_ready == false` and at least ten documented risks. Treat a zero exit as a potential safety regression requiring investigation, not as release clearance.

## Release is a different gate

Structural CI passing is **not** independent English/Myanmar/example/CEFR review. Release requires a separate immutable approved manifest with exactly 200 distinct lexical senses per level, signed independently sourced exact-sense CEFR evidence (URL and observation date), real George/Emma headword and example recordings with listened-to signoff, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages limits, production deployment verification and preservation of 54 lessons, IELTS bank, existing audio and privacy. Never infer any of these from synthetic tests. Existing `a`/`an` allomorph collision must be adjudicated before release.

## Execution status

This file documents a proposed CI matrix; it does not install a workflow or certify any run. GitHub workflow file creation must be attempted with appropriate `workflow` permission and actual run/job IDs, conclusions and logs verified before reporting CI green. Current first-pass written counts: A1 200, A2 200, B1 200, B2 200, C1 200. Independently checked: 0 for each. Audio and all physical-device/release gates unverified; staging-only.
