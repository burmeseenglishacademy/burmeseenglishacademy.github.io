# CEFR 1,000 staging checkpoint — five direct Oxford C1 sense leads

**Observed 2026-10-27, approximately 23:29 SGT. Release: BLOCKED / STAGING ONLY.** User-approved scope is exactly **1,000 total**, not 5,000. Branch remains `cefr-5000-bilingual-qa-staging`. No main change, merge, publication, or real-world device/listening verification is claimed.

| CEFR | First-pass English/Myanmar drafts written | Independently English+Myanmar+example+CEFR approved | Final George+Emma real listening signed off |
|---|---:|---:|---:|
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |
| **Total** | **1,000** | **0** | **0** |

All 1,000 remain editorial holds. Written count means first-pass provisional content, **not** independently checked, ready-to-teach or approved.

## Five newly inspected publisher dictionary entries (all C1 shortlist, none approved)

Direct Oxford Advanced Learner's Dictionary web text inspected **2026-10-27**, with 0-based viewer line references, recorded in [the five-entry source packet](CEFR-1000-OXFORD-C1-FIVE-DIRECT-SENSE-LEADS-2026-10-27.json). The exact original English/Myanmar/example strings and pinned shortlist blob SHA are stored per record. These are **dictionary source observations**, not CEFR-level certifications or independent human reviews.

1. [meticulous](https://www.oxfordlearnersdictionaries.com/definition/english/meticulous) (lines 88–114): careful attention to details; Oxford *Personal qualities c2* **topic** tag, not a wordlist CEFR assignment. [Cambridge publisher indexed page](https://dictionary.cambridge.org/us/dictionary/english/meticulous) separately labels the careful-detail adjective **C2**, based on publisher search-indexed text (direct Cambridge fetch 403). **High-priority C1-versus-C2 exact-sense conflict**, pending independent reviewer decision; never silently relabel C2 as C1.
2. [nuanced](https://www.oxfordlearnersdictionaries.com/definition/english/nuanced) (lines 88–105): slight distinctions in meaning or expression; draft *nuanced view* plausible, but no exact-sense C1 label observed. Unrelated sidebar Word-of-the-Day labels are not evidence.
3. [tenacious](https://www.oxfordlearnersdictionaries.com/definition/english/tenacious) (lines 88–114): determined person who does not give up versus persistence of an illness. The researcher example selects determination; formal register and exact-sense C1 source require independent review.
4. [mitigate](https://www.oxfordlearnersdictionaries.com/definition/english/mitigate) (lines 88–121): formal transitive harm-reduction verb; draft heat-related example merits a precision check (mitigate heat vs mitigate its effects). Oxford page lacks an observed exact-sense CEFR label.
5. [ubiquitous](https://www.oxfordlearnersdictionaries.com/definition/english/ubiquitous) (lines 88–115): very common or seemingly everywhere, usually attributive, formal/humorous. Draft predicative use and Myanmar fluency require independent review; no word-specific C1 label observed.

**Source limitations:** Oxford pages were directly inspected via web text viewer; line locators may change. The Cambridge meticulous C2 observation came from publisher-owned search-indexed text, not a directly fetched full page. No copyrighted dictionary definition was copied into learner-facing content. The canonical 1,000-row shortlist was not modified.

## Added safeguards and actual CI evidence

- New `tools/audit_cefr_1000_oxford_c1_five.py` pins all five source URLs, original snapshots, POS, source scope, page-line locators, observation dates, unchanged Git blob SHA, and zero-approval editorial holds. Nine negative mutations test forged signoff, tampered URL/CEFR scope/date, altered examples, missing records, false Cambridge C1, and removed hold.
- Wired to all **six parallel** A1/A2/B1/B2/C1/ALL GitHub Actions jobs, plus the separate documentary launch gate. New `oxford_c1_five_sense_review_receipts` ledger remains **empty**. Release auditor requires separate independent, content-hash-bound exact-sense C1 receipts for any of these retained entries, including a documented C2 conflict resolution for *meticulous*.
- First structural run [40531220995](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40531220995), SHA `bb55736abd34bb99177f032de5eda0e5faaef1b1`, **FAILED** all six jobs because the new test anchor omitted initial “The” in the real *meticulous* observation. The test mismatch was repaired in commit [adf7725792af40feedf5cc55d75a388465fabb89](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/adf7725792af40feedf5cc55d75a388465fabb89).
- Corrected structural run [40531344255](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40531344255), SHA `adf7725792af40feedf5cc55d75a388465fabb89`, **COMPLETED SUCCESS**, all six actual jobs A1/A2/B1/B2/C1/ALL. ALL job **122284671142** log confirms **five source records, zero independent approvals, nine negative tests passed**, 120 CEFR/IELTS shared headwords with **zero** independently resolved same-sense decisions, and protected production diff PASS. This is a **structural test pass only**.
- Latest documentary blocker run [40531371890](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40531371890), SHA `7ab02e63c344e143eab0a4e0e2b8bf6e0a7b2311`, **COMPLETED SUCCESS** as **report-only**, job **122284769844**. Log confirms the new five-source negative tests passed, but launch remains **BLOCKED**: no separately approved manifest, 0/1,000 human independent packets, 0 real George/Emma listening receipts, no matched browser/mobile WebKit regression receipts, no physical iPhone Safari signoff, no measured Pages hosting receipt, no final protected-asset approval or deployment confirmation.

## Remaining launch gates

Require genuine independent English sense, fluent Myanmar, original example and **publisher exact-sense CEFR** review for all 1,000 (with replacements for unsupported levels while retaining 200 each); resolve the five new C1 leads and existing Oxford/Cambridge/WordNet/named-entity and IELTS overlaps; generate the final headword+example audio for both George/Emma and **actually listen** with signed receipts; run real browser/mobile and physical iPhone Safari QA; measure GitHub Pages storage/bandwidth; verify 54 lessons, separate IELTS bank, existing production audio, privacy; then confirm actual live deployment **only after all gates pass**.

**No public launch and no completion announcement.**
