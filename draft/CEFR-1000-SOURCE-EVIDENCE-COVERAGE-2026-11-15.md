# CEFR-1000 source-evidence coverage and editorial blockers — 2026-11-15

**Scope:** User-approved 1,000 total entries, 200 per A1/A2/B1/B2/C1. Staging-only observation, not independent review or approval.

## Reproducible provenance
- Inspected `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` on branch `cefr-5000-bilingual-qa-staging` on **2026-11-15 (SGT)**.
- Observed shortlist Git blob SHA: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.
- Repository source URL: https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json
- Method: parsed all 1,000 JSON entries, counted nonblank `source_english`, `source_burmese`, and `source_level` fields by level; inspected distinct `source_path` values and Unicode-NFKC/case-folded headword collisions. This is a structural inspection, **not external source verification**.

| Level | First-pass written | Independently approved | Nonblank source_english | Nonblank source_burmese | Nonblank source_level | Editorial hold |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 | 0 | 0 | 200 |
| A2 | 200 | 0 | 0 | 0 | 0 | 200 |
| B1 | 200 | 0 | 0 | 0 | 0 | 200 |
| B2 | 200 | 0 | 0 | 0 | 0 | 200 |
| C1 | 200 | 0 | 0 | 0 | 0 | 200 |
| **Total** | **1,000** | **0** | **0** | **0** | **0** | **1,000** |

**Interpretation:** Every entry has first-pass English definition, Myanmar meaning, and example text, but none carries a nonblank entry-level source English/Myanmar/CEFR field in the inspected shortlist. This does not prove that no research notes exist elsewhere. In particular, `source_path` and `source_blob_sha` point to internal draft source material; they do **not** establish independent CEFR or lexical evidence. No entry should be promoted by inference from a source path, from a dictionary's general coverage, or from the first-pass example.

## Concrete editorial triage
1. **A1 `a` / `an` (indices 0, 1):** both currently occupy distinct headword slots. Independently adjudicate whether the intended release counts inflectional/phonological article variants as distinct senses or as one article lemma with two surface forms. Preserve the existing indices until adjudicated. Require vowel-*sound* rather than letter-based usage checks and corresponding fluent Myanmar glosses.
2. **A1 `i` (index 3):** lowercase headword requires canonical orthographic `I` for the English first-person pronoun. This is an editorial proposal only, not a change to the approved manifest.
3. **Cross-level deduplication:** the inspected 1,000 entries had zero collisions under NFKC + lowercase + trim, but this does not establish **sense-level** uniqueness. A distinct spelling can still be a near-synonym or article variant; a reused lemma can have legitimately distinct senses, subject to independent review.
4. **Exact-sense CEFR evidence:** source-backed level assignment must attach a specific lexical sense, part of speech, URL, observed date and a reviewer identity/signoff. Blank `source_level` fields mean the current manifest cannot meet that gate.
5. **Historical WordNet and named-entity risks:** source recovery or WordNet sense IDs alone cannot certify CEFR or Myanmar fluency. Check proper nouns, spurious lemma extraction, and mismatched parts of speech against contemporary learner dictionaries and CEFR-tagged sense evidence before independent adjudication.

## Next staging-only work
- Populate a **separate, unapproved evidence queue** with source URL, exact sense, observed date, source quotation/paraphrase within rights limits, proposed English/Myanmar/example correction, conflict flags and provenance digest.
- Request genuine independent English, Myanmar, example and CEFR review of each item; do not set approval flags from self-review.
- Require final manifest SHA-bound review and 4,000 George/Emma headword/example audio artifacts with human listening signoff, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages hosting clearance and production preservation checks.
- Current-commit GitHub Actions job conclusions/logs must be checked independently. A historical successful run does not validate a new commit.

**Release decision:** BLOCKED. No independent approvals, verified audio listening, physical iPhone QA, hosting clearance or deployment evidence is claimed. Production's 54 lessons, separate IELTS bank, existing George/Emma audio and privacy settings remain out of scope.
