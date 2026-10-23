# CEFR Vocabulary 5,000 — implementation and publication gate

Status: **STAGING ONLY — NOT RELEASE READY**  
Date: 2026-10-23  
Production remains **Burmese English Academy v1.2.5**; no new CEFR words have been published.

## Planned bilingual content
| Level | New words | Total |
|---|---:|---:|
| A1 | 500 | 500 |
| A2 | 700 | 1,200 |
| B1 | 1,000 | 2,200 |
| B2 | 1,300 | 3,500 |
| C1 | 1,500 | 5,000 |

Maintain the 1,000-word IELTS bank separately and show overlaps accurately. These level quotas are an **Academy curriculum choice**, not a mandatory CEFR word count.

## What has been implemented
1. `tools/prepare_cefr_candidates.py` creates 5,000 **unique English lexical candidates** using word-frequency and Princeton WordNet references. It marks every English sense, Burmese translation, illustrative sentence and CEFR tier unverified. GitHub Actions [candidate audit 39977521625](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39977521625) passed. Candidates are available only as a 14-day workflow artifact, not a live page.
2. `cefr-vocabulary.js` implements five selectable levels, search, paginated English–Myanmar definition cards, original example placeholders, and George/Emma audio routing through the existing `playSpeech` function.
3. `cefr-vocabulary-data.js` explicitly contains zero published records and is marked `UNVERIFIED_DRAFT_DO_NOT_PUBLISH`; the UI displays a not-ready notice rather than fabricated vocabulary.
4. `tools/validate_cefr_release.py` fails if there are not exactly 5,000 unique headwords with all bilingual glosses, contextual examples, exact level counts, traceable reference URLs and independently confirmed QA flags. The optional audio gate checks SHA-based filename mapping and MP3 validity. This validator **has not passed on complete content** because complete content does not exist.
5. The [UI unit regression](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39978290393) succeeded with synthetic 5,000-entry fixtures and demonstrated rejection of blank translations and duplicate headwords. This is a software test, **not a review of genuine word meanings**.

## Evaluated source references and legal considerations
- Oxford Learner's Dictionaries [Oxford 3000/5000](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000) and Cambridge [English Vocabulary Profile](https://englishprofile.org/?menu=english-vocabulary-profile) provide important level/sense **cross-checks**; neither list is automatically republished or scraped.
- [Princeton WordNet](https://wordnet.princeton.edu/license-and-commercial-use) provides openly distributable dictionary sense references subject to attribution. The first WordNet sense of a polysemous word can be **incorrect for a learner example**.
- [wordfreq](https://pypi.org/project/wordfreq/) supports frequency-based candidate selection under its code and dataset attribution/share-alike terms. Frequency rank is not itself a CEFR assignment.
- [Myanmar Open Wordnet](https://wordnet.burmese.sg/) is CC BY 4.0, but its early release has only 1,041 word types; it cannot provide all 5,000 bilingual headwords.
- The [EngMyanDictionary repository](https://github.com/soeminnminn/EngMyanDictionary) exposes 21,984 reference entries. A read-only schema check ran in [reference audit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39978498512). Its README says Apache 2.0, while the repository's root LICENSE file contains GPL-2.0; therefore **no definitions were copied, shipped or treated as licensed for this project** pending resolution.

## Why the content is not yet deployable
- 5,000 contextual English definitions and 5,000 Burmese meaning matches require sense-level bilingual editorial review; the English list produced so far is a ranked starting pool only.
- At least 5,000 original example sentences require grammatical/sense QA and source traceability.
- George and Emma must have recordings for every headword and example sentence (nominally 20,000 new recordings before deduplication); none of those recordings were generated yet. Full audio size and GitHub Pages bandwidth have not been validated for the expansion.
- An MP3 passing decoding/file checks is **not equivalent** to a pronunciation specialist approving every spoken recording.
- Chromium/WebKit regression of the staging version should be re-run after data arrives. Physical iPhone Safari testing of the *new* vocabulary is not yet possible.
- Privacy: no additional account systems, analytics, learner storage, paid speech API or production Firebase services were introduced.

## Mandatory publication order
1. Cross-check word-level CEFR and English senses against authoritative reference works without copying protected text.
2. Draft original clear English definitions and examples, match each Burmese meaning to the same sense, and verify every entry with evidence.
3. Run the fail-closed content validator and retain a per-entry QC record.
4. Create offline Kokoro British recordings after the text has been frozen; validate complete manifests, codecs, durations, sampled listening and total size.
5. Run browser regressions, actual user-device tests, privacy checks and confirm GitHub Pages budget limits.
6. **Only then** create and merge the verified release into `main`, deploy and test the public URL. No automated source-audit workflow here performs deployment.

No claim is made that the full 5,000-word bilingual product is completed, double-checked or live.
