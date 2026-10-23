# Burmese English Academy — A1 500 vocabulary first-draft checkpoint
**Status:** EDITORIAL DRAFT ONLY — NOT PUBLISHED / NOT MEANING-VERIFIED  
**Date:** 23 October 2026 (Singapore)  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Live production:** v1.2.5, unchanged.

## Accurate scope
- The first-draft A1 word bank has **500 unique A1 headwords**, each with an original English learner definition, Burmese draft meaning, original example sentence and part of speech.
- The 500 are integrated into an independent **5,000-headword A1–C1 *candidate* corpus** (A1 500, A2 700, B1 1,000, B2 1,300, C1 1,500). All 5,000 CEFR placements are provisional pending sense-level cross-checks; they are not a validated official Oxford/Cambridge list.
- 500/500 entries have **independent Myanmar translation verification still pending**. Machine tests do not establish that meanings, spelling, sentence style or CEFR assignments are linguistically correct.
- 500/500 entries remain explicitly `DRAFT_PENDING_INDEPENDENT_REVIEW`; all five review flags remain false.
- English-sense source checks: 11 earlier British Council/Cambridge checks; 10 earlier Oxford level/POS spot checks; none extrapolated to all 500.
- Myanmar Open Wordnet: 53 weak lemma alignments among the earlier 227-entry draft; **not** evidence that 53 translations are correct. The 500-entry list requires another reference pass.
- Exact A1 vs IELTS vocabulary overlap: **3 headwords**: `family`, `market`, `cloud`. In particular `cloud` means a weather cloud in A1 and an IT cloud in the existing IELTS bank, so different senses/translation must not be collapsed. See `draft/A1-IELTS-SENSE-OVERLAPS.json`.

## Executed test evidence
- GitHub [500-record A1 mechanical draft validation](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39989612024): **success**; 0 automatically detected structural defects, 0 heuristic warnings. This is neither human proofreading nor official exam-level certification.
- GitHub [integrated A1 staging QA](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39989791984): **success**. Checks all 500 editorial records match the generated 5,000 provisional corpus; JavaScript route and 5,000-record synthetic fixture; original 54 lessons, existing 1,000 IELTS word bank, exact 4,652 original MP3 mappings and privacy regressions.
- GitHub [5,000 candidate source audit](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39989310325): **success**, reconstructs the draft word pool. Important: does not independently approve meanings.
- Prior [Chromium and mobile WebKit regression](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39978608997): **success** for the staging UI, but mobile WebKit emulation is not a physical iPhone.
- The [40-MP3 Kokoro George/Emma technical pilot](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/39984640181) **completed successfully** as a GitHub Actions job. Its artifact `a1-kokoro-british-technical-pilot-UNREVIEWED` (artifact ID `12516654132`, archive 487,980 bytes) exists and is unexpired as checked on 24 October 2026; scheduled expiry 6 November 2026. The 40-clip sample set is **not independently pronunciation-listened or approved**. No new CEFR audio has been delivered to the live site.

## Remaining work before go-live
1. Independently proofread each of 500 Burmese meanings and every example and confirm exact English sense; continue with A2, B1, B2, C1 to reach 5,000 reviewed words.
2. Verify headword/POS/meaning-specific CEFR levels with credible reference materials; frequency ranking alone is inadequate.
3. Freeze reviewed texts, produce George and Emma word/exemplar recordings with local Kokoro, decode-check each file and conduct pronunciation listening QA.
4. Assess total static site storage and realistic traffic, then run site integrity, browser and physical iPhone testing on all revised playback routes.
5. Merge only the complete verified release into `main`, check GitHub Pages deploy and the live URL.

## Source provenance and rights
- British Council grammar/pronouns: https://learnenglish.britishcouncil.org/
- Cambridge Dictionary: https://dictionary.cambridge.org/
- Oxford 3000/5000 CEFR references: https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000
- Princeton WordNet license: https://wordnet.princeton.edu/license-and-commercial-use
- wordfreq frequency data: https://github.com/rspeer/wordfreq
- Myanmar Open Wordnet CC BY 4.0: https://github.com/myanmaropenwordnet/mow

**No unreviewed draft headwords, translations or incomplete audio have been published.** 
