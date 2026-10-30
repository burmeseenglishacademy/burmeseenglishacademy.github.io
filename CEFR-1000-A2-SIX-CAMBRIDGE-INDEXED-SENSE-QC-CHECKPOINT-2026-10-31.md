# CEFR 1000: six A2-draft Cambridge compound senses — 31 October 2026

**STAGING ONLY.** This is source-supported editorial research, **not** independent linguistic review or publication approval. Branch: `cefr-5000-bilingual-qa-staging`; scope: **1,000 total** (A1/A2/B1/B2/C1: 200 each), not 5,000.

## Source method and limitations

Cambridge University Press's dictionary **search-index entries** were inspected on **2026-10-31**. Direct page opens returned HTTP **403**, so this packet does **not** claim full live-page inspection, listening, pronunciation review, or independently verified exact-sense CEFR placement. The individual canonical URLs, observed badges, sense paraphrases, countability, frozen English/Myanmar/example snapshots, source-path/index/blob and proposed rewrites are in [the six-record research packet](draft/CEFR-1000-CAMBRIDGE-A2-SIX-COMPOUND-INDEXED-SENSE-TRIAGE-2026-10-31.json).

| A2-draft word | Observed Cambridge badge | Publisher sense / editorial issue |
|---|---|---|
| [saucepan](https://dictionary.cambridge.org/us/dictionary/english/saucepan) | **B1** | Countable deep cooking pan; draft A2/B1 conflict, no automatic retiering |
| [postcard](https://dictionary.cambridge.org/dictionary/english/postcard) | **A2** | Countable card sent without envelope; image optional, original translation should not imply required picture |
| [toothbrush](https://dictionary.cambridge.org/dictionary/english/toothbrush) | **A2** | Countable brush for teeth; toothpaste not intrinsic to the noun |
| [dustbin](https://dictionary.cambridge.org/dictionary/english/dustbin) | **B1** | Mainly British outdoor household rubbish container; original kitchen-door example may imply indoor bin |
| [crossroads](https://dictionary.cambridge.org/dictionary/english/crossroads) | **B2** | Literal road junction vs decision-point idiom; singular/plural form both `crossroads` |
| [doormat](https://dictionary.cambridge.org/dictionary/english/doormat) | **No badge observed** | Literal mat at door vs figurative person; do not manufacture an A2 CEFR label |

**Publisher-index outcomes:** A2 badge 2, publisher-higher B1/B2 badges 3, no observed badge 1. This **does not change** the existing Oxford direct word/POS observation metric (A1 195/200, A2 132/200, B1 144/200, B2 142/200, C1 111/200; **724/1,000**, 276 without direct Oxford observation). Oxford and Cambridge are different evidence sources; do not combine their counts as independent approvals.

Six original Myanmar/example rewrites are *unapproved proposals*, not replacements. Original first-pass content and all editorial holds remain unchanged. Source attribution is to the headword entry only; do not repeat the earlier unrelated Oxford site-wide Word-of-the-Day footer attribution error.

## Safeguards and evidence

[Fail-closed auditor](tools/audit_cefr_1000_cambridge_a2_six_indexed.py) pins the original shortlist blob, all six publisher URLs/badges/grammar/sense notes, original snapshots and Git provenance, and rejects forged signoff/hold removal. It includes **90 adversarial mutation cases** (15 per word), scheduled in the existing six parallel A1/A2/B1/B2/C1/ALL structural jobs and documentary **no-deployment** gate. A successful structural run is not a human independent review.

At initial checkpoint authoring, the new CI conclusions were **pending**; do not claim success without checking actual job conclusions/logs. Report any failure and fix it on staging.

## Release state (no change)

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Final George/Emma headword + example audio generated/listened/independently signed off: **not verified; 0/1,000 real listening signoffs**. Independent exact-sense English/Myanmar/example/CEFR reviews, final dual-voice audio, approved-corpus browser/mobile regression, **physical iPhone Safari**, measured GitHub Pages hosting readiness, and production deployment/preserved-assets verification remain blocked. Existing 54 lessons, separate IELTS 1,000, George/Emma production audio, and privacy must not change. **No merge, no main modification, no publish.**
