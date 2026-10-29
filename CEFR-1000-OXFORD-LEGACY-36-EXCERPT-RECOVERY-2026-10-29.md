# CEFR 1,000 — direct Oxford excerpt recovery for 36 historical locator-only observations (29 October 2026)

**Scope and branch:** USER-APPROVED **1,000 total**, not the abandoned 5,000-word target. A1/A2/B1/B2/C1 remain **200 first-pass entries each**. All 1,000 remain on editorial hold; **zero** independently approved. Work is confined to `cefr-5000-bilingual-qa-staging`. No production release, merge or main change.

## Substantive source recovery

Directly re-opened Oxford University Press's [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) (12 pages) and [Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) (8 pages) on **2026-10-29**. Recovered **36 literal word/part-of-speech source excerpts** from real page/line locations for three earlier historical packets that recorded locators but lacked quotations. Recovery comprises **B1 draft: 12** (Oxford A1 ×6, A2 ×5, B1 ×1), **B2 draft: 12** (Oxford A1 ×1, A2 ×4, B1 ×5, B2 ×2), and **C1 draft: 12** (Oxford B2 ×12). These source classifications are word/POS research, not exact-sense validation or independent reviewer approval.

The recovered excerpts are stored in `draft/CEFR-1000-OXFORD-LEGACY-THIRTYSIX-EXCERPT-RECOVERY-2026-10-29.json`, each linked to the **original packet path, original immutable Git blob SHA, original row index, source URL, 1-based PDF page, zero-based extracted line, observation date, and explicit no-approval flags**. The original historical packets and the frozen shortlist were **not rewritten**. For examples of real source discrepancies, Oxford lists `address n.` at A1 against a B1 draft, `plastic n., adj.` at A2 against a B2 draft, and `sustainable adj.` at B2 against a C1 draft. Exact senses, Myanmar translation choices and example alignment still require independent review.

This is **not 36 new headwords**: all 36 were already included in the previous **324 observations / 305 distinct observed headwords** consolidation. The original three packets still have 36 excerpt-less historical rows; a separate supplemental recovery now supplies 36 directly observed quotations. Distinct source coverage remains **A1 100/200, A2 48/200, B1 60/200, B2 58/200, C1 39/200**, with **129** publisher word/POS discrepancies or unlisted cases requiring human exact-sense reconciliation. No automatic CEFR retiering or edits to provisional definitions, Myanmar meanings or original examples occurred.

## Fail-closed staging safeguards

Added `tools/audit_cefr_1000_oxford_legacy_excerpt_recovery.py`. It requires exactly **12 recovery records per B1/B2/C1 draft level**, binds all rows to the three **fixed historical Git blob SHAs**, compares exact word, POS, source level, source URL, PDF page and extracted-line locators to historical records, checks source observation dates, rejects duplicate/missing rows and rejects any human-review or release-approval claim. It includes **20 deliberately forged mutation cases** for evidence, provenance, level, locators, duplicate rows, status and reviewer receipts. The recovery auditor is wired into **six parallel A1/A2/B1/B2/C1/ALL structural lanes** and the separate documentary **no-deployment** release-readiness workflow. These checks validate the recorded source evidence's internal integrity; they cannot replace a publisher's exact-sense entry or an independent human linguistic review.

## Exact status and outstanding gates

| CEFR level | First-pass written | Independently approved | Distinct Oxford word/POS observed | New recovered historical excerpts |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 0 | 100 | 0 |
| A2 | 200 | 0 | 48 | 0 |
| B1 | 200 | 0 | 60 | 12 |
| B2 | 200 | 0 | 58 | 12 |
| C1 | 200 | 0 | 39 | 12 |
| **Total** | **1,000** | **0** | **305** | **36** |

Final George/Emma **real listening signoffs 0/1,000**. Still required: independently signed English, fluent Myanmar, example-grammar and exact-sense CEFR evidence for all 1,000; genuinely generated and listened-to British George/Emma headword and example audio; browser/mobile regression; **physical iPhone Safari** evidence; GitHub Pages measured size/bandwidth/hosting constraints; preserved production lessons (54), separate IELTS 1,000 bank, existing production George/Emma audio and privacy; and confirmed production deployment. Any absent gate **blocks** launch. No human approval, iPhone test, listening test or deployment is asserted here.

**Release status: BLOCKED / STAGING ONLY.**

## Executed GitHub Actions verification

- [Six parallel structural jobs, run **40796226985**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40796226985), workflow commit `313bb578cce211d10454aeb2b5bada11eaa18a53`: **SUCCESS** for A1, A2, B1, B2, C1 and ALL. The actual ALL job `123193239046` logs recovered **36/36** publisher lines, **20/20** forged-source and fake-signoff mutations rejected, and protected production diff **PASS**.
- [Documentary no-deploy run **40796235361**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40796235361), workflow commit `a1df9b10f53ed18a11ea00647eb569a636f593d6`: **SUCCESS as report-only**, actual job `123193267042` logs recovered **36/36**, **20/20** rejected, `source-reviewed 0/1000`, `both-voice listening 0/1000`, explicit missing release evidence, and protected production diff **PASS**. This is **not** a release-ready result; the workflow intentionally passes when it correctly reports blockers.
- The structural run predates the final documentary workflow and documentation commits; the new auditor and its source recovery file were already present in both tested workflow heads. Later changes were confined to the documentary workflow and staging documentation. **No main merge, release or production deployment.**
