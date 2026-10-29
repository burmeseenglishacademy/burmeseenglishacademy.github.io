# CEFR 1,000 — B2 fifth twelve direct Oxford publisher word/POS observations (29 October 2026)

**STAGING ONLY — NO independent approvals, audio listening, device testing or deployment.** Branch `cefr-5000-bilingual-qa-staging`. Shortlist Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Oxford 3000/5000 official PDFs were inspected directly on 2026-10-29; each observation preserves the publisher URL, one-based PDF page, zero-based extracted text line and exact short word/POS excerpt. Source PDF lists indicate word/POS teaching levels, **not exact-sense CEFR**.

## Twelve new non-overlapping B2-draft entries

- `breath` — Oxford 3000 **B2**, PDF page 10, line 2666, `breath n.`. Noun breath versus verb breathe; breathing air, not metaphorical relief.
- `brief` — Oxford 3000 **B2**, PDF page 10, line 2667, `brief adj.`. Short duration adjective versus noun legal brief; intended temporal sense.
- `conduct` — Oxford 3000 **B2**, PDF page 10, line 2714, `conduct v., n.`. Verb organising/carrying out versus directing music or conducting electricity.
- `decade` — Oxford 3000 **B1**, PDF page 8, line 1961, `decade n.`. B1 publisher word/POS label conflicts with provisional B2; ordinary ten-year sense.
- `external` — Oxford 3000 **B2**, PDF page 11, line 2844, `external adj.`. Physical outside versus outside an organisation; definition may conflate senses.
- `fantasy` — Oxford 5000 **B2**, PDF page 1, line 244, `fantasy n.`. Imagined situation versus literary genre; example must express intended sense.
- `grab` — Oxford 3000 **B2**, PDF page 11, line 2892, `grab v.`. Sudden physical taking versus metaphorical grabbing attention.
- `immediate` — Oxford 3000 **B1**, PDF page 8, line 2134, `immediate adj.`. B1 publisher label conflicts with B2; without delay versus closest relationship.
- `introduction` — Oxford 3000 **A2**, PDF page 5, line 1315, `introduction n.`. A2 publisher label conflicts with B2; opening section versus introducing people.
- `presidential` — Oxford 5000 **C1**, PDF page 6, line 1609, `presidential adj.`. C1 publisher word/POS label conflicts with B2; political-office sense requires independent CEFR review.
- `recognize` — Oxford 3000 **A2**, PDF page 6, line 1535, `recognize v.`. A2 publisher label conflicts with B2; identification from familiarity versus formal recognition; US/UK spelling.
- `regularly` — Oxford 3000 **B1**, PDF page 9, line 2360, `regularly adv.`. B1 publisher label conflicts with B2; repeated frequency versus uniformity.

Official sources: [Oxford 3000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf); [Oxford 5000](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf). No unverified Cambridge indexed snippet is represented as directly accessed.

## Coverage and reviewer handoff

A1 **112/200**, A2 **60/200**, B1 **72/200**, B2 **70/200**, C1 **39/200**; **353/1,000 distinct observed** and **647 without direct Oxford word/POS evidence** in the audited packets. Provisional level mismatches: **134 lower**, **10 higher**, **3 unlisted**; **206 matching word/POS**, still requiring independent exact-sense review. Twelve new B2 observations: 5 lower (A2 2, B1 3), 6 matching B2, 1 higher C1. These are observations, not corrections or independent approvals.

Exact first-pass written / independently approved: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. Final George/Emma real listening signoffs **0/1,000**. Human-independent English/Myanmar/example/exact-sense source review, final both-voice headword/example audio and listening, desktop/mobile regression, physical iPhone Safari evidence, measured GitHub Pages limits, protected-production verification and confirmed production deployment remain launch blockers.

New `tools/audit_cefr_1000_oxford_b2_fifth_twelve.py` checks all 12 frozen bilingual examples, historical Git provenance, publisher evidence and editorial holds; 132 negative mutation cases. The cross-batch Oxford coverage and reviewer-handoff integrity audits have updated expectations. CI job conclusions and logs must be verified after this commit; passing structural/documentary jobs **does not** establish release readiness.

**Do not merge, publish or change main. Protect the 54 lessons, separate IELTS 1,000 bank, George/Emma production audio and privacy. RELEASE BLOCKED / STAGING ONLY.**
