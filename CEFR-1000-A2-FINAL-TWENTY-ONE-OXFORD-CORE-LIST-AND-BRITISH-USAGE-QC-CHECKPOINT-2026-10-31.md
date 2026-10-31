# CEFR 1,000 — final 21 provisional A2 compound headwords: direct Oxford source triage (2026-10-31)

**STAGING ONLY — editorial research, not approval.** User-approved scope is 1,000 total, exactly 200 provisional words at each A1/A2/B1/B2/C1. Work remains on `cefr-5000-bilingual-qa-staging`, not the superseded 5,000-word plan. The frozen shortlist, 54 production lessons, separate IELTS 1,000 bank, existing George/Emma production audio and privacy settings were not edited.

## Direct publisher source observations

On **2026-10-31**, directly inspected the official [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) (12 pages) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) (8 pages). All 21 provisional A2 headwords had lacked an audited direct Oxford core-list observation. The publisher lists **greenhouse n. at B2**, Oxford 5000 PDF page **2**, extracted line **292**. **The other 20 headwords were not found in either inspected core list.** Their absence is *not* a CEFR level or proof that A2 is incorrect; no automatic retiering is permitted.

| Official Oxford 5000 B2 | Not found in either inspected Oxford core list (20) |
| --- | --- |
| greenhouse (noun, page 2, extracted line 292) | raincoat, lunchbox, toothache, sunscreen, shoelace, bookshelf, doormat, shoebox, saucepan, washcloth, postcard, sunflower, dustbin, bathrobe, snowman, hairbrush, toothbrush, crossroads, wheelbarrow, backseat |

Four official Oxford Advanced Learner's Dictionary entries were also directly inspected on **2026-10-31**: [greenhouse](https://www.oxfordlearnersdictionaries.com/definition/english/greenhouse) (glass structure for growing plants, lines 88–109), [crossroads](https://www.oxfordlearnersdictionaries.com/definition/english/crossroads) (road intersection versus figurative decision point, lines 88–123), [raincoat](https://www.oxfordlearnersdictionaries.com/definition/english/raincoat) (rain-protective coat, lines 88–104), and [washcloth](https://www.oxfordlearnersdictionaries.com/definition/english/washcloth) (North American usage; British English *facecloth* or *flannel*, lines 88–111). **Dictionary topic badges are not automatically exact-sense CEFR labels**, and unrelated page footers/Word of the Day entries are excluded.

## Independent reviewer priorities and original Myanmar/example issues

- **greenhouse:** provisional A2 conflicts with direct Oxford 5000 B2 word/POS; human reviewer must determine the intended sense and a defensible teaching level.
- **washcloth:** Oxford explicitly marks it North American; British English alternatives *facecloth/flannel* require a deliberate learner-curriculum choice.
- **crossroads:** same singular/plural form; do not mix the literal junction with the figurative life-choice sense.
- **wheelbarrow:** provisional Myanmar `ပစ္စည်းလေးများ` suggests small items, whereas a wheelbarrow commonly carries heavy loads such as soil.
- **bookshelf:** example `highest bookshelf` may sound less natural than `top shelf of the bookcase`; grammatical/pedagogical review required.
- **sunscreen, saucepan, dustbin:** previous publisher-indexed leads suggest higher-level exact senses; no direct human-independent source-backed A2 approval exists.

The [21-record packet](draft/CEFR-1000-OXFORD-A2-FINAL-TWENTY-ONE-COMPOUNDS-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json) preserves all 21 original English definitions, Myanmar meanings, examples, source paths/indices and historical Git blob SHAs, dated official PDF source URLs and four directly observed dictionary page/line ranges. Five separate bilingual/example rewrite candidates remain **unapproved**. No provisional learner-facing content was changed.

The [fail-closed auditor](tools/audit_cefr_1000_oxford_a2_final_twentyone.py) checks all 21 against the frozen shortlist and four actual historical source files, verifies 20 explicit two-list absence observations and greenhouse's exact publisher PDF page/line, and defines **265 negative mutations** against forged source, bilingual content, provenance, false approvals, dictionary leads and rewrite status. Integrated into all six parallel A1/A2/B1/B2/C1/ALL structural QA lanes and the documentary no-deployment workflow. CI must be inspected for actual run conclusions and logs before declaring this new auditor verified.

## Consolidated staging-only review handoff (pending final CI confirmation)

The source coverage code now expects **A1 195/200, A2 200/200, B1 200/200, B2 200/200, C1 111/200 = 906/1,000** distinct entries with direct Oxford word/POS observations **or explicitly documented two-list absence**, over **925** research observations. **94** entries remain without an audited Oxford observation. The 906 are *not* 906 publisher-validated exact senses: 24 are explicitly absent from inspected lists, and all 906 still require independent exact-sense review. Priority categories are **24 unlisted, 61 publisher-higher, 351 publisher-lower, 470 word/POS matches still exact-sense-unverified, 94 unobserved**.

| CEFR level | Provisional first-pass written | Independently reviewed/approved | Final George/Emma real listening signoffs |
| --- | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 |
| A2 | 200 | 0 | 0 |
| B1 | 200 | 0 | 0 |
| B2 | 200 | 0 | 0 |
| C1 | 200 | 0 | 0 |

**Release blocked:** independent human exact-sense CEFR, English, fluent Myanmar, original-example and pronunciation review; content-bound approved manifest with exactly 200 unique senses/headwords per level; final British George/Emma headword/example audio generated and *actually listened to*; desktop/mobile browser regression; physical iPhone Safari QA; measured GitHub Pages release artifact/hosting; preservation of production assets and verified production deployment. **No merge, main-branch modification or publication.**
