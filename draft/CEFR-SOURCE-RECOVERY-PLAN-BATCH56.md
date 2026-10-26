# CEFR 5,000 — Evidence-first source recovery after batch56
**Staging only. 26 October 2026. No candidate counts may be increased without new real headwords and sense records.**

## Why a new source is mandatory
The initial 5,000-row WordNet/frequency pool has 3,667 unique first-pass drafts and 1,333 reversibly held candidates, including named entities, acronyms, possessives, rare first senses, morphological duplicates and unsupported original CEFR labels. Its apparent A1–C1 assignment is not graded sense-specific evidence. The remaining writing deficits are **A2 122, B1 162, B2 299, C1 750** (A1 0), totalling **1,333**. Never treat held candidates as accepted just to fill a quota.

## Intake rules for replacement candidate sourcing
1. Use reputable **graded learner-vocabulary references** and independently check licence/terms before bulk reuse. Oxford 3000/5000, Cambridge English Vocabulary Profile and learner dictionaries are *candidate research leads*, not permission to copy their explanations or examples. Keep source URL, access date, precise sense/POS, evidence summary and licence note.
2. Candidate must be an English lexical headword (or a deliberately justified multiword expression) with one clearly identified teaching sense and POS. Reject automatic lowercasing of names, abbreviations, symbols and possessives. Preserve British vs American spelling and register notes.
3. Deduplicate casefolded headwords and sense IDs against all **3,667** existing unique drafts and **1,333** held source candidates. A held candidate may be reopened only with documented sense/CEFR evidence; reopening does not itself count as writing or approval.
4. Keep **four separate editorial stages**: (a) independently composed English definition, (b) natural Burmese translation, (c) grammatical original example, (d) source-evidence and independent review task. The CEFR level is provisional until sense-specific graded evidence is observed.
5. Add separate **pronunciation production** only after editorial approval. Generate George/Emma files, record file hashes and voice settings, independently listen to each, then validate mobile and real iPhone Safari. Neither generated files nor automated duration/size checks count as listening.
6. Run level-specific A2/B1/B2/C1 structural CI and protected production drift checks before any staging commit is treated as QA-tested. Never allow incomplete drafts, unreviewed audio or review packets into the public CEFR bank or the live deployment.
7. Publish a transparent per-level ledger with **written**, **English-checked**, **Myanmar-checked**, **example-checked**, **CEFR-evidence-approved**, **both-voices-listened**, **real-device-checked** as separate non-interchangeable fields. Include observed sources, reviewers, timestamps, commit SHAs and real job statuses.

## Practical next work packages
- **Source discovery and licensing:** identify legally reusable graded headword/sense sources; capture source URLs and evidence without copying proprietary definitions/examples.
- **Small graded intake pilot:** 20–40 *new source candidates* with documented POS/sense and provisional CEFR, screened for duplicates and named entities before drafting; this is not a claimed written batch.
- **High-throughput bilingual drafting:** aim for 40–100 original drafts per iteration only after sufficiently clear candidate senses exist. Quarantine dubious words rather than inventing definitions or levels.
- **Independent editorial and audio review:** separate from drafting and GitHub CI; cannot be automatically marked complete.
- **Release:** only after all 5,000 entries and every George/Emma recording pass actual reviews, real-device tests and hosting checks.

**This plan is an intake protocol, not a source licence, completed dictionary review, audio test, CEFR validation or production approval.**
