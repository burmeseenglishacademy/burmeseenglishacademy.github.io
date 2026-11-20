# CEFR-1000 staging: independently observed GitHub Actions conclusions (20 November 2026)

**Scope:** user-approved 1,000 provisional bilingual vocabulary records (A1/A2/B1/B2/C1: 200 each). This is a CI observation, **not** linguistic approval or launch clearance.

## GitHub Actions evidence

- Workflow: `.github/workflows/cefr-1000-structural-qa.yml`
- Observed through GitHub REST `GET /repos/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44603665487` and `GET /repos/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44603665487/jobs?per_page=100` on **2026-11-20**.
- [Run 44603665487](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/44603665487), push event, **completed / success**, commit `39214de5f6cfc3bf4127556f449c4acc17b6d2f4`, attempt 1, created 2026-11-19 19:57:33 UTC; updated 19:57:46 UTC.
- Structural integrity / A1: job **135841507141**, success.
- Structural integrity / A2: job **135841507188**, success.
- Structural integrity / B1: job **135841506894**, success.
- Structural integrity / B2: job **135841507155**, success.
- Structural integrity / C1: job **135841507191**, success.
- Reject corrupted provisional data (16 negative cases): job **135841506263**, success.
- Assert unverified release remains blocked: job **135841506716**, success.
- GitHub job metadata reported every named execution step above as success. **Raw job logs were not downloaded or independently inspected.** This evidence confirms GitHub-reported conclusions, not manual inspection of each test assertion.

## Exact inventory and release state

The staging shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551` reports 200 first-pass entries per level and zero independently approved for every level. Review-task blob `77abf35146825f05e3e58cfdd7a73b3c7302c967` reports the same per-level counts, with independent reviewer identities and signoffs absent. Both blobs were fetched on 2026-11-20. These 1,000 are **provisional written first-pass records**, not independently checked records.

| Level | Provisional written | Independently approved | Final George/Emma headword + example audio listened/signed |
|---|---:|---:|---|
| A1 | 200 | 0 | No evidence |
| A2 | 200 | 0 | No evidence |
| B1 | 200 | 0 | No evidence |
| B2 | 200 | 0 | No evidence |
| C1 | 200 | 0 | No evidence |
| **Total** | **1,000** | **0** | **Not signed off** |

## What the successful CI does not prove

The passing structural workflow only verifies the current structural checks and deliberately blocked release condition at the **historical workflow commit** `39214de5...`. It does not certify exact-sense CEFR classifications, fluent Myanmar translations, originality and grammar of all examples, real human independent review, generated George/Emma audio or real listening, browser/mobile regressions, physical iPhone Safari evidence, GitHub Pages hosting capacity, deployment, or preservation of production lessons/IELTS/audio.

Later staging branch head observed on 2026-11-20: `3ff3c518a94985adab403fc8f6483022e6c507fc`. **Do not attribute the historical CI run to this later head.** The workflow's push path filter does not include Markdown evidence documents, so a documentation-only commit is not itself expected to trigger these checks.

## Remaining release blockers

Keep the editorial hold for all 1,000 entries. Require reviewer-identified independent English, Myanmar, example, pronunciation and source-backed exact-sense CEFR signoff; resolve the documented cross-level and sense conflicts; build and actually listen to both British voices for every final headword and example; obtain browser/mobile and real physical iPhone Safari evidence; validate hosting limits and protected production asset integrity; only then consider a separate authorised production deployment with live verification. No staging document or green structural CI may substitute for these gates.

**Production/main not modified by this report. No approval flags changed. Release status: BLOCKED.**
