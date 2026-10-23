> **Superseded checkpoint notice (24 October 2026):** This file records the *earlier 227-draft milestone*, not current totals. Current A1 editorial draft contains **500 unique entries**, all still unverified; 5,000 CEFR candidates remain unapproved. See [CEFR-A1-500-DRAFT-CHECKPOINT.md](CEFR-A1-500-DRAFT-CHECKPOINT.md) and [CEFR-5000-STAGING-QA.md](CEFR-5000-STAGING-QA.md). Audio pilot workflow **succeeded** and archived 40 unreviewed clips; that does not constitute auditory pronunciation approval. Do not merge this branch into production on this evidence alone.

# CEFR 5,000 bilingual vocabulary — QA checkpoint (23 October 2026)

**Status: not released.** Production is still Academy v1.2.5. This branch contains editorial drafts, not certified learner material.

## Completed this checkpoint
- Full 5,000-word candidate file `draft/UNVERIFIED_CEFR_CANDIDATES.json` (all word-level and learner-level assignments provisional). Strict split: A1 500; A2 700; B1 1000; B2 1300; C1 1500.
- `draft/A1-EDITORIAL-STARTER.json`: **227 originally written A1 English definitions, Burmese draft meanings and example sentences**. All bilingual meanings and pronunciation still flagged pending independent verification; none published.
- English-sense spot checks on 11 A1 entries use British Council's A1/A2 articles and beginner pronouns guides and Cambridge's `book` noun entry. This verifies only supporting English explanations, not Burmese meaning precision for those entries.
- Weak independent vocabulary reference: Myanmar Open Wordnet v0.1.3 (CC BY 4.0), applied to 227 draft headwords through provisional Princeton WordNet synset IDs. **53/227** had at least one aligned MOW lemma. This is a **candidate/sense-alignment count**, not evidence that 53 Myanmar translations are correct. [MOW audit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39985344421) passed with `reviewed_burmese=false` for all 227.
- [Candidate source audit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39984975038): success.
- [A1 structural draft QA](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39985143152): success.
- [5,000 synthetic word UI regression](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39984335381): success; explicitly tests rejection of incomplete review/source/audio data.
- [Chromium/WebKit existing site regression](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39978608997): success.
- Kokoro audio technical pilot configured for 10 A1 headwords and their example sentences in both George and Emma voices, for 40 temporary clips; workflow [39984640181](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39984640181). A running/technically passing workflow is not a verified-pronunciation or live-website result.

## Important verified limits
- Total independently accepted Burmese meanings: **0/5,000**; there are **227 editorial drafts, not verified translations**.
- All examples and level judgements still require sense-aware proofreading and an independent bilingual editorial pass.
- CEFR is a proficiency framework, not a fixed official word-count quota. Oxford Learner's Dictionaries' 3000/5000 and English Vocabulary Profile can guide level decisions without copying their protected database. Frequency order alone **does not** establish CEFR level.
- No newly generated CEFR word or example MP3 has been merged into the live Academy catalogue. Existing Kokoro recordings belong only to previously released lessons and IELTS 1,000 words.
- The CEFR Word Bank JavaScript refuses to show any content unless all 5,000 entries have positive review flags, adequate references, level quotas, and both audio filenames. The backend release validator also demands all files and MP3 format verification. This prevents accidental exposure of half-checked material.
- Browser tests and ffprobe checks are valuable but cannot approve accent clarity or individual Burmese lexical nuance. iPhone real-device test of new CEFR words is not yet available.

## Authoritative references used for targeted checks
- British Council, A1/A2 articles: https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2-grammar/articles-a-an-the
- British Council, beginner pronouns: https://learnenglish.britishcouncil.org/grammar/english-grammar-reference/personal-pronouns
- Cambridge Dictionary, book: https://dictionary.cambridge.org/dictionary/english/book
- Oxford core CEFR word lists: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000
- Princeton WordNet and terms: https://wordnet.princeton.edu/license-and-commercial-use
- Myanmar Open Wordnet v0.1.3 CC BY 4.0: https://github.com/myanmaropenwordnet/mow
- Word-frequency research (not authoritative CEFR placement): https://github.com/rspeer/wordfreq

## Go-live condition
**Do not release this branch** until meaning/POS/level/example crosschecks are finished for every candidate, 5,000 Burmese translations are independently checked in context, all required George and Emma clips exist and pass technical plus listening QA, the total static site size and host quota are assessed, and staging regression and live mobile browser checks are complete.
