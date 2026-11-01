# CEFR 1000 — British orthography and capital-I source-bound QC (1 November 2026)

Scope: **1,000 total**, 200 first-pass A1/A2/B1/B2/C1; all on editorial hold, **0 independently approved**. Branch `cefr-5000-bilingual-qa-staging` only. This is editorial research, not human signoff.

## Findings from the frozen shortlist

- **A1 `i` is a genuine display/headword case error:** stored as lowercase `i` although its original example correctly says `I am a student.` British Council directly states that the first-person singular pronoun **I** is always capitalised. Cambridge indexed learner entry shows **I pronoun A1** but direct Cambridge access returned HTTP 403. Proposed display `I` is **UNAPPROVED**; frozen shortlist unchanged. A reviewer must confirm any approved release display/search key and actually listen to George/Emma headword and example audio. No audio defect is asserted without listening.
- **A1 `a` and `me`** are negative controls: do not uppercase all one-letter words or all pronouns. British Council rule is specifically for `I`.
- **B1 `realize`, B2 `recognize`, C1 `galvanize` and `scrutinize`** use **-ize**. This is **not inherently an American-English error**. The directly opened University of Oxford style guide explicitly distinguishes its preference for -ise from Oxford University Press's -ize convention. Cambridge search-indexed entries for realize, galvanize and scrutinize say UK usually -ise; their direct dictionary pages returned HTTP 403. Proposed UK -ise alternatives are **unapproved**. Do not retier CEFR or alter British TTS merely from spelling.
- **B2 `theatre`, `defence`, `colour`** follow conventional British spellings supported by the University of Oxford's directly opened style guide. Do not automatically replace with US spellings.

Source URLs and observation date (2026-11-01) are preserved per record in [the ten-record research packet](draft/CEFR-1000-UK-ORTHOGRAPHY-CAPITAL-I-AND-SPELLING-TEN-2026-11-01.json). Direct publisher/style sources: [British Council capitalisation](https://takeielts.britishcouncil.org/blog/capital-letters-in-english-common-errors-and-how-to-fix-them) (lines 86–94) and [University of Oxford word usage/spelling](https://www.ox.ac.uk/about/the-university/brand/style-guide/words) (lines 84–90 and 136–158). Cambridge indexed leads are separately marked **INDEX_ONLY_DIRECT_403**, not direct inspection. Historical Git source paths/indices/blob SHAs and exact original English/Myanmar/examples are preserved. The [fail-closed auditor](tools/audit_cefr_1000_uk_orthography.py) checks immutable packet and shortlist blobs, exact source bindings, original bilingual content, all review holds and forged signoff mutations.

## Release readiness

First-pass written/independently approved: **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. Oxford word/POS observations **995/1,000**, with five documented A1 morphology/rabbit exceptions. Final George/Emma listening receipts **0/1,000**. Missing independent exact-sense CEFR/English/Myanmar/example review, approved deduplicated manifest, final dual-voice generation and listening, desktop/mobile browser regression, real physical iPhone Safari evidence, measured Pages hosting limits, production deployment confirmation and preserved-assets signoff. **RELEASE BLOCKED — STAGING ONLY.**

CI conclusions must be verified from actual GitHub Actions job results and logs after this staging commit; a passing research auditor does **not** imply independent linguistic or device QC.
