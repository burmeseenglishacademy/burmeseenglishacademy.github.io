# CEFR 1,000 — six held C1 Oxford-direct / Cambridge-indexed exact-sense triage

**Observed 2026-11-02 · staging only · NOT independent human review · no deployment**

The user-approved scope is **1,000 total**: 200 provisional first-pass bilingual entries each at A1/A2/B1/B2/C1, **0 independently approved at every level**. The historical 5,000-word target is superseded. The frozen shortlist blob is `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; no selected row or source task was edited.

## Publisher observations and editorial decisions still required

| Frozen C1 word | Direct Oxford headword/POS/sense observation | Cambridge publisher search-index lead | Human reviewer action |
|---|---|---|---|
| **meticulous** | Adjective, unusually attentive to every detail; Oxford *Topics Personal qualities c2* is a **topic label**, not an exact-sense C1 badge. [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/meticulous) lines 88–114 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/meticulous) indexed matching adjective **C2** | Resolve C1 versus indexed C2; preserve approving tone and accurate Myanmar |
| **mitigate** | Formal transitive verb: reduce harm/severity, not necessarily prevent it entirely. [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/mitigate) lines 88–124 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/mitigate) indexed meaning, **no observed CEFR badge** | Obtain independent exact-sense C1 source; do not mistake unrelated Oxford page footer for a level |
| **nuanced** | Adjective: showing subtle differences, not merely being complex. [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/nuanced) lines 88–107 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/nuanced) indexed meaning, **no observed CEFR badge** | Confirm that Myanmar and example capture subtle distinctions; independently substantiate level |
| **pragmatic** | Adjective: sensible, practical response to real constraints rather than fixed theory. [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/pragmatic) lines 88–123 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/pragmatic) indexed matching adjective **C2** | Resolve C1 versus indexed C2; do not confuse *pragmatic* with *pragmatics* |
| **precedent** | Noun: a prior decision/action used as model; Oxford separately lists a previous similar event and uncountable customary practice. [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/precedent) lines 88–155 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/precedent) indexed matching countable noun **C2** | Adjudicate C1/C2 and exact legal/general sense, countability and Myanmar |
| **scrutinize** | Transitive verb: inspect very closely; Oxford explicitly allows British spelling **scrutinise**. [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/scrutinize) lines 88–125 | [Cambridge](https://dictionary.cambridge.org/dictionary/english/scrutinize) indexed meaning, **no observed CEFR badge** | Independently verify C1 and decide British display spelling/pronunciation before audio freeze |

All six Oxford headword pages were **directly opened** on 2026-11-02. Cambridge publisher snippets were observable through search results, but direct Cambridge page opens returned **HTTP 403**, including the three C2-labelled words. Therefore C2 classifications are **publisher-indexed conflict leads, not direct-page verification or independent approval**. No exact-sense C1 badge was observed on the six Oxford entries. Do not treat Oxford *Topics c2*, word-list footer, Word of the Day, or unrelated nearby entries as the headword's CEFR classification.

## Staging artifacts and fail-closed checks

- [Six-card bilingual packet](draft/CEFR-1000-C1-SIX-METICULOUS-SCRUTINIZE-DIRECT-OXFORD-CAMBRIDGE-C2-2026-11-02.json) preserves frozen English definitions, Myanmar meanings, original examples, historical source file/index/blob SHA, direct Oxford URLs/line locators/UK IPA, Cambridge indexed URL/CEFR-access limits, six original **unapproved** alternatives, and independent reviewer tasks.
- [Pinned structural auditor](tools/audit_cefr_1000_c1_six_meticulous_scrutinize.py) requires the frozen 1,000-entry blob and research packet blob, exactly 200 deduplicated held words per level, honest publisher access/CEFR scope, immutable bilingual provenance, zero fabricated English/Myanmar/CEFR approvals, George/Emma listening, physical iPhone or deployment evidence. Its synthetic negative cases cannot substitute for human checks.
- Both [parallel structural QA](.github/workflows/cefr-1000-selection-structural-qa.yml) (A1/A2/B1/B2/C1/ALL) and [documentary no-deployment QC](.github/workflows/cefr-1000-go-live-qc-gate.yml) include this auditor. Check **actual** post-change run IDs, job conclusions and decoded logs before claiming CI success.

## Release blockers

**Written/independently approved:** A1 **200/0**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**. All **1,000 remain on editorial hold**. No independent exact-sense/CEFR, English, Myanmar or example signoffs; no approved manifest; no complete George/Emma headword/example recordings with actual listening receipts; no final-corpus browser/mobile or physical iPhone Safari QA; no measured GitHub Pages hosting clearance; no confirmed production deployment. **RELEASE BLOCKED — STAGING ONLY.** Keep main, 54 lessons, separate IELTS 1,000-word bank, existing production audio and privacy unchanged.


## Actual post-change GitHub Actions verification — 2026-11-02

- [Structural run **41437145678**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41437145678), SHA `61ab566327f69a623aa1621e1aaf0e83e68283f8`: **completed SUCCESS** across A1, A2, B1, B2, C1 and ALL. ALL job `125249684542` decoded logs confirmed the new six-card auditor and **203/203 synthetic adversarial mutations rejected**; ALL artifact `13137915022`.
- [Documentary run **41437150894**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41437150894), SHA `2781aa83c06873cad857696f4a332a19d470c914`: **completed SUCCESS** as a report-only, explicitly blocked release gate. Job `125249699453` decoded logs independently confirmed **203/203** synthetic rejections, **0/1,000** independent approvals, absent George/Emma real listening, final mobile/physical iPhone Safari, hosting and deployment evidence; it also confirmed protected production assets unchanged. Blocker artifact `13136937515`.
- Mechanical QA successes do **not** prove any publisher CEFR label independently, human bilingual review, physical listening, device QA or production release. The staging-only branch remains unpublished.
