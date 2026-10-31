# CEFR 1000 — B2 fifteenth Oxford source and independent-review handoff checkpoint

**Observation date:** 2026-10-31. **Branch:** `cefr-5000-bilingual-qa-staging` only. **Release:** BLOCKED / STAGING ONLY. The original 1,000-entry bilingual shortlist remains frozen, with no independent approvals or real listening signoffs.

## Direct Oxford 3000/5000 word/POS research

Twelve previously unobserved provisional B2 entries have new publisher PDF word/POS observations. Official publisher lists: [Oxford 3000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), [Oxford 5000 CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf). Pages below are **1-based**; text lines are **zero-based** as exposed by the PDF extractor. Word/POS CEFR is *not* an exact-sense CEFR label, independent editorial signoff, or permission to retier automatically.

| Frozen B2 draft | Oxford word/POS | Source PDF | Page | Extracted line | Human review priority |
|---|---|---|---:|---:|---|
| administrative (adj.) | C1 | 5000 | 3 | 737 | Higher publisher word/POS; office duties vs authority |
| argue (v.) | A2 | 3000 | 4 | 955 | Lower publisher word/POS; reasoned proposition vs quarrel |
| colour (n.) | A1 | 3000 | 1 | 162 | Lower publisher word/POS; simple hue sense |
| defend (v.) | B2 | 3000 | 11 | 2767 | Legal representation vs generic protection |
| element (n.) | B1 | 3000 | 8 | 2010 | Component of whole vs chemical element |
| extension (n.) | B2 | 5000 | 1 | 237 | Deadline extension vs physical/telephone/software extension |
| extent (n.) | B2 | 3000 | 11 | 2843 | Degree/scale vs geographic area; Myanmar nuance |
| harm (n.) | B2 | 3000 | 11 | 2899 | Uncountable injury/damage vs verb; ecological harm |
| hunt (v.) | B1 | 3000 | 8 | 2127 | Animals hunting prey vs human sport/search |
| impressive (adj.) | B1 | 3000 | 8 | 2140 | Everyday admiration vs advanced usage |
| moral (adj.) | B2 | 3000 | 11 | 3013 | Ethical principles adjective vs moral noun |
| offensive (adj.) | B2 | 3000 | 11 | 3038 | Insulting language vs military/sports offensive |

Publisher distribution: **A1 1, A2 1, B1 3, B2 6, C1 1**. Six provisional B2 placements differ from Oxford word/POS classifications. None has been independently accepted, rejected, or retiered.

Four additional Oxford dictionary **publisher-indexed sense leads**, observed 2026-10-31, are recorded separately with exact URLs and source-access caveats: [administrative adjective](https://www.oxfordlearnersdictionaries.com/definition/english/administrative), [colour noun](https://www.oxfordlearnersdictionaries.com/definition/english/colour_1), [harm noun](https://www.oxfordlearnersdictionaries.com/definition/english/harm_1), and [moral adjective](https://www.oxfordlearnersdictionaries.com/definition/english/moral_1). These identify office administration, the basic visual hue, uncountable injury/damage, and right/wrong principles. Oxford topic badges and indexed snippets do **not** substitute for independently verified exact-sense CEFR. Four original Myanmar/example rewrite alternatives are **UNAPPROVED**; the frozen originals remain intact.

[Immutable 12-record evidence packet](draft/CEFR-1000-OXFORD-B2-FIFTEENTH-TWELVE-AND-FOUR-DICTIONARY-SENSE-LEADS-2026-10-31.json) preserves the publisher source URL, observation date, PDF page/line/excerpt, original bilingual text, historical Git source path/index/blob SHA, editorial risks, and null reviewer receipts. [Fail-closed source auditor](tools/audit_cefr_1000_oxford_b2_fifteenth_twelve.py) pins publisher and historical source records and defines **220 adversarial mutations** (12 × 17 source/review changes + 4 × 4 dictionary/rewrite changes). It is wired into all six parallel structural lanes and the documentary no-deploy workflow; successful CI must be established from actual job conclusions/logs, not inferred from wiring.

## Reconciled source coverage and reviewer priorities

| Level | First-pass written | Direct Oxford word/POS observations (distinct) | Still lacking direct Oxford observations | Independently approved |
|---|---:|---:|---:|---:|
| A1 | 200 | 195 | 5 | 0 |
| A2 | 200 | 168 | 32 | 0 |
| B1 | 200 | 200 | 0 | 0 |
| B2 | 200 | 190 | 10 | 0 |
| C1 | 200 | 111 | 89 | 0 |
| **Total** | **1,000** | **864** | **136** | **0** |

Across source packets, **883 observations** now cover 864 distinct provisional entries (19 repeated observations). Source-bound human review priorities: **3 unlisted/not a CEFR level, 53 publisher-higher, 342 publisher-lower, 466 matching word/POS but exact sense unverified, 136 without direct Oxford observation**. These five categories total 1,000. Counts are updated in staging auditors and **confirmed by actual successful GitHub Actions jobs and logs**.

## Actual CI verification (source code SHA `7657dcd2efbdd99b3b01e4dc164c3d2eb4067f9e`)

- [Parallel structural run 41196579571](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41196579571): **SUCCESS for all six A1/A2/B1/B2/C1/ALL jobs**. ALL job `124523844897` log confirmed **864 distinct / 883 Oxford observations**, reviewer queue counts **3 unlisted, 53 publisher-higher, 342 publisher-lower, 466 matching word/POS and 136 unobserved**, **25/25** cross-batch mutations rejected, **143/143** source-bound handoff mutations rejected, and **220/220** B2 fifteenth forged source/Myanmar/provenance/review mutations rejected. ALL artifact ID `13040831962`.
- [Documentary no-deploy run 41196579625](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41196579625): **SUCCESS, report-only**. Job `124523844970` log confirmed **220/220** new adversarial mutations rejected and protected production assets untouched. Blocker artifact ID `13041177591`. A successful report-only documentary job is **not** a successful release-readiness gate.
- [Source-scope run 41196573053](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41196573053): **SUCCESS** on prior code SHA `4bc951e5e094bfe80e022702370790630d1e8ec2`; actual log recorded 864 distinct publisher word/POS observations, 136 still unobserved, exactly 200 first-pass draft entries per level and zero independent approvals.
- Intermediate structural/documentary runs `41196572873` and `41196573900` **FAILED** because Oxford coverage was updated before the reviewer-handoff expected counts; reconciled in commit `7657dcd2efbdd99b3b01e4dc164c3d2eb4067f9e` before final successful CI. Do not treat these intermediate failures as passed.
- The remaining **ten B2 draft headwords without direct Oxford word/POS observations** are `package, pride, province, railway, relative, repeat, server, shock, silence, superior`. This is a research queue, not an invitation to infer their CEFR levels.

## Release remains blocked

All 1,000 bilingual entries remain on editorial hold: **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0** written/independently approved. No independent human exact-sense CEFR, English, fluent Myanmar, example, pronunciation or reviewer-identity signoff was created. Final George/Emma headword and example audio generation and **actual listening** remain unverified (**0/1,000 listening signoffs**). Approved deduplicated 200-per-level manifest, browser/mobile regression, real physical iPhone Safari, measured GitHub Pages release artifact/limits and production deployment confirmation remain missing. Preserve 54 live lessons, separate IELTS 1,000-word bank, established production George/Emma audio and privacy. **No merge, no main modification, no publication.**
