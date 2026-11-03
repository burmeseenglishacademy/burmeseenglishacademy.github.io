# CEFR-1000 cross-level morphological and exact-sense collision audit — 2026-11-04

**Scope:** frozen 1,000-entry provisional shortlist, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. **Status:** staging-only editorial research queue; NOT an independent review, publisher CEFR verification, or release approval.

## Method
Case-folded the 1,000 headwords and compared endings `ly, ness, ment, tion, ity, er, ing, ed, s` against existing headwords, allowing a naive trailing-e/y reconstruction. This is deliberately a *candidate generator*, not a morphological analyser. 18 cross-level pairs surfaced. Each needs exact-sense review; a shared root does not imply equal CEFR, and accidental string overlaps must not be treated as a word family.

## Genuine morphological families requiring exact-sense / CEFR source review
| Derived (proposed) | Base (proposed) | Editorial question |
|---|---|---|
| actually A2 | actual B1 | Discourse-marker 'actually' differs pragmatically from adjectival 'actual'; assess publisher sense evidence separately |
| exactly A2 | exact B2 | Common conversational response versus precise adjective; source-backed level needed for each |
| clearly B1 | clear A2 | Manner adverb versus adjective; verify examples and senses |
| reality B1 | real A2 | Abstract noun versus adjective; do not automatically inherit level |
| truly B1 | true A2 | Sincerity/genuineness versus factual truth |
| reporting B2 | report A2 | Activity/industry noun versus report noun; compare exact noun senses |
| effectively B2 | effective B1 | Manner/result adverb versus adjective |
| improvement B2 | improve B1 | Result/process noun versus verb |
| monthly B2 | month A1 | Periodic adjective/adverb versus time noun; verify high B2 placement |
| speaker B2 | speak A1 | Person noun versus speech verb; common senses may have different CEFR levels |
| consistently C1 | consistent B2 | Adverb versus adjective; source-backed evidence for C1 needed |
| complexity C1 | complex B1 | Abstract noun versus adjective; C1 placement needs direct support |

## False positives or distinct senses: do not merge
| Candidate | Why naive derivation is misleading |
|---|---|
| news A2 / new A1 | 'news' is a lexicalised mass noun, not ordinary plural 'new' |
| training A2 / train A1 | A1 'train' is a railway vehicle noun; A2 'training' refers to skill learning, not that noun sense |
| likely A2 / like A1 | Not productive 'like + ly' with the listed 'enjoy' verb sense |
| comment B1 / come A1 | String overlap only, not the listed word's derivation |
| engineer B2 / engine B1 | Historical relation does not justify assigning equivalent sense/CEFR |
| server B2 / serve B1 | Computing server noun versus food-service verb; semantic mismatch |

## Reviewer tasks
1. Record **exact publisher URL, observed date, headword, part of speech, sense and CEFR label** where actually available. Dictionary existence alone does not substantiate a CEFR assignment.
2. Check English definition, natural Myanmar translation, original example and collocation for each word **individually**, not by transferring its family member's grade.
3. For `training/train`, `server/serve`, and `likely/like`, explicitly mark the source-sense mismatch in independent review worksheets.
4. Keep all 1,000 provisional entries on hold; do not change flags, levels, production audio or main. Human-independent signoff remains required.

## Evidence and limits
Input: [frozen shortlist](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json), retrieved 2026-11-04. The 18 pairs above were computed from its recorded headwords and English definitions. No publisher pages were fetched for this audit; **zero new external CEFR citations** are claimed.

## Release state
First-pass written / independently approved: A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. Required final George/Emma 4,000 audio files and actual listening signoff, browser/mobile regression, physical iPhone Safari QA, hosting clearance and confirmed production deployment are not evidenced by this work. The previously verified 22/22 synthetic mutation result on run `41642178932` applies to earlier commit `54745b7df955041ca672165f47385e0bcf73cb43`, **not** to this documentation change. No publication authorised until every release gate is independently evidenced.
