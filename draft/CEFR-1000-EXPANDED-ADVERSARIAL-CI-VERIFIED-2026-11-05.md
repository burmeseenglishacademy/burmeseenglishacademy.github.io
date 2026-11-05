# CEFR-1000 expanded adversarial CI verification — 2026-11-05

Scope: user-approved **1,000 total** CEFR A1–C1 words, not the obsolete 5,000-word proposal. Staging branch only: `cefr-5000-bilingual-qa-staging`.

## Verified GitHub Actions execution
- Workflow: `.github/workflows/cefr-1000-release-guard-negative-qa.yml`
- Run: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41980458509
- Run ID: **41980458509**, commit: `75c6b3c71102e7b4c14a91b9ee6bbee691f26485`
- Trigger: push; created 2026-11-05 06:26:47 UTC; completed with **success**.
- Job conclusions read from the actual Actions jobs endpoint on 2026-11-05:
  - A1: 127089113372 — success
  - A2: 127089113453 — success
  - B1: 127089113365 — success
  - B2: 127089113527 — success
  - C1: 127089113429 — success
- Each job reports **success** for the five-case negative fixtures, eight-case adversarial fixtures, and rejection of the provisional shortlist as a release manifest. These are separate structural checks, **not** five independent linguistic reviews. The matrix repeats the same test scripts per level; it does not yet assert 200 independently verified lexical senses for that level.

## Editorial inventory (prior first-pass project records, not new human verification)
| Level | First-pass drafted | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

All 1,000 remain on editorial hold. The independent-review task JSON exists but the GitHub file connector returned empty content when queried; individual tasks have **not** been audited here.

## Mandatory release blockers
1. Independent human English, fluent Myanmar, original-example and publisher-backed **exact-sense** CEFR review, with evidence URLs, dates and provenance, plus cross-level lexical identity and WordNet/named-entity risk resolution.
2. Approved release manifest of exactly 200 distinct headword/POS/sense identities per level; guard must be tested against genuinely approved evidence, not fabricated attestations.
3. All 4,000 George/Emma British headword/example audio assets generated and **actually listened to**, with independent listening signoff; no audio completion claim is made.
4. Browser and mobile regression, **physical iPhone Safari** test evidence, and GitHub Pages hosting limits confirmed.
5. Production asset preservation (54 lessons, separate IELTS 1,000-word bank, established George/Emma production audio, privacy) and a verified production deployment. No production deployment has occurred under this staging task.

**Release decision: BLOCKED — staging only.** This report is evidence of CI negative-test execution, not approval, device QA, listening, or deployment. Do not merge or publish.
