# CEFR 1,000 — A2 sixteenth eleven direct Oxford publisher observations (2026-10-31)

**Scope:** User-approved **1,000 total** provisional entries, exactly 200 each at A1/A2/B1/B2/C1. This is a **STAGING-ONLY, unapproved research checkpoint**, not the superseded 5,000-word plan. Work is restricted to `cefr-5000-bilingual-qa-staging`; no main merge, production change or deployment.

## New direct publisher research

The official [Oxford 3000 by CEFR level PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) was inspected on **2026-10-31** for eleven previously unobserved A2-draft headwords. The source-bound [eleven-record packet](draft/CEFR-1000-OXFORD-A2-SIXTEENTH-ELEVEN-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json) records exact publisher word/POS lines, 1-based PDF pages, extracted text line numbers, original bilingual/exemplar snapshots, historical source indices/blob SHA and editorial holds:

| A2 draft | Oxford publisher word/POS level | PDF page | Extracted line |
| --- | --- | ---: | ---: |
| member | A1 | 2 | 477 |
| usually | A1 | 4 | 844 |
| follow | A1 | 2 | 301 |
| save | B1 | 6 | 1582 |
| round | B1 | 6 | 1568 |
| worth | B1 | 10 | 2586 |
| exactly | A2 | 5 | 1180 |
| source | B1 | 6 | 1644 |
| total | B1 | 10 | 2517 |
| result | A1 | 3 | 650 |
| share | A1 | 3 | 685 |

Thus **5 publisher A1, 1 publisher A2 and 5 publisher B1** word/POS observations; **10/11 provisional A2 level differences**. This is **not** evidence that the intended exact senses are misclassified, nor permission to retier automatically. Four direct Oxford dictionary pages were separately inspected: [save money](https://www.oxfordlearnersdictionaries.com/definition/english/save_1), [worth as monetary value](https://www.oxfordlearnersdictionaries.com/definition/english/worth_1), [total as a noun](https://www.oxfordlearnersdictionaries.com/definition/english/total_2), and [share a space](https://www.oxfordlearnersdictionaries.com/definition/english/share_1). Four proposed fluent Myanmar/example alternatives remain **unapproved**. Note the original **result** definition emphasizes a causal consequence while its example illustrates a test result/score; human exact-sense review must resolve this. Oxford topic badges and unrelated Word of the Day footers must not be used as exact-sense CEFR evidence.

## Fail-closed structural research controls

[New auditor](tools/audit_cefr_1000_oxford_a2_sixteenth_eleven.py) pins the packet blob, frozen shortlist blob and historical A2 starter source blob; validates all 11 actual upstream source indices and original English/Myanmar/examples; binds publisher CEFR/POS/page/line/excerpt and four direct dictionary sense URLs; rejects unauthorized approval fields and requires all editorial holds. Its self-test defines **142 adversarial modifications** across publisher evidence, provenance, bilingual snapshots, dictionary senses, approval and packet-level counts. These are *test definitions*, not human approvals.

The auditor is integrated into six parallel A1/A2/B1/B2/C1/ALL structural jobs and the documentary no-deployment workflow. CI run IDs, actual job conclusions and logs must be checked independently before claiming CI success.

## Source-coverage and human-review queue

The cross-batch Oxford source reconciliation now expects **A1 195, A2 179, B1 200, B2 200, C1 111 = 885/1,000** distinct publisher word/POS or explicitly unlisted observations, **904** total packet observations, **115** entries without direct Oxford observations. Source-bound reviewer priorities: **4 unlisted, 60 publisher-higher, 351 publisher-lower, 470 matching word/POS but exact-sense-unverified, 115 unobserved**. This remains an editorial triage count, not a verified learner-level CEFR manifest.

| Level | First-pass written | Independently checked and approved | Final George/Emma real listening signoffs |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |

**Release blockers:** independent human English, fluent Myanmar, example and exact-sense publisher CEFR review; approved deduplicated manifest; complete final British George/Emma headword and example audio with real listening signoffs; desktop/mobile regressions; physical iPhone Safari evidence; measured GitHub Pages deployment-artifact and bandwidth checks; preserved production assets and confirmed production deployment. Existing 54 lessons, separate IELTS 1,000 bank, George/Emma production audio and privacy remain protected. **No publication authorised while any gate is missing.**
