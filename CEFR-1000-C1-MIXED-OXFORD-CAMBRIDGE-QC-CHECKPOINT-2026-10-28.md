# CEFR 1,000 — C1 Oxford/Cambridge source and QA checkpoint (2026-10-28)

**Scope:** User-approved **1,000 TOTAL**, 200 each A1/A2/B1/B2/C1, staging branch `cefr-5000-bilingual-qa-staging` only. The obsolete 5,000-word proposal is not in scope. **BLOCKED / STAGING ONLY.**

## Direct Oxford publisher evidence (12 more C1 drafts)

On **28 October 2026**, inspected official Oxford University Press [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf). **Eight** C1-draft words match Oxford C1 word/POS level; **three** appear under Oxford B2 word/POS; `premises` was **not listed in either inspected core list**, which is not evidence of its CEFR level.

| Provisional C1 word | Oxford word/POS | Direct PDF locator | Editorial risk to resolve |
|---|---|---|---|
| `verdict` | C1 | Oxford 5000 by CEFR level p.8, line 1971 | jury verdict vs general court decision and myanmar legal precision |
| `abandon` | B2 | Oxford 3000 by CEFR level p.10, line 2593 | same sense oxford b2 conflict with c1 draft |
| `accommodate` | B2 | Oxford 5000 by CEFR level p.1, line 9 | b2 source and mixed capacity vs adjustment definition |
| `aesthetic` | C1 | Oxford 5000 by CEFR level p.3, line 744 | aesthetic appeal collocation vs adjective sense |
| `algorithm` | C1 | Oxford 5000 by CEFR level p.3, line 752 | algorithm technical scope and myanmar teaching gloss |
| `complexity` | C1 | Oxford 5000 by CEFR level p.4, line 941 | complexity abstract noun example naturalness |
| `deliberately` | B2 | Oxford 3000 by CEFR level p.11, line 2770 | same sense oxford b2 conflict with c1 draft |
| `dignity` | C1 | Oxford 5000 by CEFR level p.5, line 1084 | dignity respect vs self respect sense |
| `ideology` | C1 | Oxford 5000 by CEFR level p.5, line 1305 | ideology belief system vs political movement context |
| `inclusion` | C1 | Oxford 5000 by CEFR level p.5, line 1318 | social inclusion vs general include sense |
| `isolation` | C1 | Oxford 5000 by CEFR level p.6, line 1378 | physical separation vs social loneliness and wellbeing |
| `premises` | Not in inspected lists | Oxford 3000 + 5000 full-list search | not in inspected oxford core lists not cefr proof plural only noun |

Full per-word **unchanged original English definitions, fluent-Myanmar draft meanings, original examples, Git source path/index/blob, dated publisher URL and PDF page/line/excerpt** are preserved in [source packet](draft/CEFR-1000-OXFORD-C1-MIXED-TWELVE-2026-10-28.json). Source shortlist blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No provisional entry, review flag, level or production file was changed.

## Publisher-indexed Cambridge sense leads — important cross-publisher nuance

Direct Cambridge full-page requests returned **HTTP 403**. The following **publisher-owned search-indexed snippets**, observed 2026-10-28, are useful *research leads*, not direct full-page verification or independent approval.

- [**abandon — STOP**](https://dictionary.cambridge.org/us/dictionary/english/abandon): Cambridge Advanced Learner's Dictionary indexed **C1** for stopping an activity/plan, aligning with the draft's intended stop-plan sense, while Oxford 3000 gives the verb word/POS **B2**. This is a meaningful sense-versus-word-level distinction; **do not automatically retier**.
- [**deliberately — INTENTIONALLY**](https://dictionary.cambridge.org/dictionary/english/deliberately): Cambridge indexed **B2** and Oxford 3000 word/POS **B2**. The provisional C1 intentional sense needs a genuine independent C1 teaching justification or editorial replacement.
- [**premises — LAND AND BUILDINGS**](https://dictionary.cambridge.org/dictionary/english/premises): Cambridge indexed **C1** and a **plural noun** for organisational land/buildings, despite absence from the two Oxford core lists. Verify the plural-only grammar, natural Myanmar meaning and example with an independent reviewer.
- [**accommodate — CAPACITY / SUIT**](https://dictionary.cambridge.org/us/dictionary/english/accommodate): Cambridge indexed distinct senses but **no visible CEFR label** for the inspected senses. The draft definition blends capacity and adjustment, whereas its hall example illustrates capacity only. Oxford 5000 word/POS is B2; independent exact-sense disambiguation is essential.

## Executed structural and documentary QC

The new source-integrity auditor checks all 12 source-bound bilingual/example snapshots, publisher URLs/dates/PDF locators, three B2 conflicts, the unlisted case, unchanged editorial holds, four Cambridge index-only leads, and absent independent receipts. It rejects **33/33 forged publisher, Myanmar, example, provenance, Cambridge-label and false-signoff mutations**.

- [Parallel structural run 40716769413](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40716769413): **all six** A1, A2, B1, B2, C1 and ALL jobs **success**; ALL log confirms 33/33 mutation rejection and protected production diff PASS.
- [Documentary no-deploy run 40716564379](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40716564379): **success as report-only**, not release approval. Log confirms 33/33 mutations rejected, forged C1 mixed review receipt rejected, protected production diff PASS and release blockers retained.
- New content-bound launch gate requires human-independent exact-sense C1, English, Myanmar and example review, with explicit Oxford B2 or absent-list reconciliation. Receipt collection remains empty. Source/auditor commit `60d0ea09c8a04ee74c472cbbd5c236d35df7ec44`; release gate commit `a8bbae3ed5e4086262a31d21eac4c571594e8983`.

## Exact counts and release blockers

| Level | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**George/Emma final headword-and-example listening signoffs: 0/1,000 words.** Independently approved manifest: absent. Independent bilingual and CEFR exact-sense signoff: absent. Real audio generation/listening evidence, desktop/mobile browser regression, **physical iPhone Safari**, GitHub Pages measured hosting/bandwidth limits and confirmed production deployment: not complete. Existing 54 lessons, separate IELTS 1,000 vocabulary, George/Emma production audio and privacy paths were checked unchanged by the staging CI diff; this is not proof of full end-user functionality or complete audio listening.

**No main merge, no public release, no production modification. The launch remains BLOCKED / STAGING ONLY until all real evidence gates pass.**
