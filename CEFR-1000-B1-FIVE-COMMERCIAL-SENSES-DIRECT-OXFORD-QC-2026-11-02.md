# CEFR 1,000 — five B1 commercial / everyday exact-sense investigations

**Observation date:** 2026-11-02. **Scope:** user-approved 1,000 total, A1/A2/B1/B2/C1 = 200 each; never the superseded 5,000 plan. **Branch:** `cefr-5000-bilingual-qa-staging`. **Release:** BLOCKED, STAGING ONLY.

## Directly inspected publisher evidence and review questions

| Frozen B1 card | Direct Oxford sense/grammar | Cambridge publisher search-index lead (direct HTTP 403) | Editorial consequence (not approved) |
| --- | --- | --- | --- |
| **demand**, noun | [Oxford customer-demand sense](https://www.oxfordlearnersdictionaries.com/definition/english/demand_1), lines 182–190: uncountable/singular buyer need/desire, distinct from a strong request and plural job demands | [Cambridge demand](https://dictionary.cambridge.org/dictionary/english/demand): indexed **B2** for noun NEED | **B1 vs indexed B2**. Frozen packaging example matches commercial demand, but English definition says the *amount* of goods wanted rather than the buyer need/desire. Independently adjudicate exact sense, level and definition. |
| **supply**, noun | [Oxford supply](https://www.oxfordlearnersdictionaries.com/definition/english/supply_1), lines 109–115 and 165–203: countable available quantity, distinct from plural emergency supplies and uncountable act of supplying | [Cambridge supply](https://dictionary.cambridge.org/dictionary/english/supply): **no reliable exact-sense badge observed** | Frozen water example illustrates `a limited supply`; Myanmar `ထောက်ပံ့ပစ္စည်း` can mean the items, not the available quantity. Retain level on hold. |
| **feature**, noun | [Oxford feature](https://www.oxfordlearnersdictionaries.com/definition/english/feature_1), lines 103–117 and 156–160: distinctive characteristic, distinct from facial features | [Cambridge feature](https://dictionary.cambridge.org/dictionary/english/feature): **no reliable exact-sense badge observed** | Frozen phone-battery example illustrates a beneficial characteristic, not necessarily an independently operable software function. Myanmar and English alternatives are editorial only. |
| **apply**, verb | [Oxford apply](https://www.oxfordlearnersdictionaries.com/definition/english/apply), lines 110–128 and 133–155: formal request; separate `apply to` relevance and practical use | [Cambridge apply](https://dictionary.cambridge.org/dictionary/english/apply): indexed **B1** for REQUEST, versus C1 USE | Indexed **B1 alignment control**, not an approval. Oxford Working life `a2` is a topic label, not an exact-sense CEFR assignment. |
| **authority**, noun | [Oxford authority](https://www.oxfordlearnersdictionaries.com/definition/english/authority), lines 108–116, 150–159 and 181–187: uncountable right/power, distinct from permission and plural officials | [Cambridge authority](https://dictionary.cambridge.org/dictionary/english/authority): indexed **B2** POWER | **B1 vs indexed B2**; frozen manager's right to approve a request fits the power/right construction. Myanmar should express `လုပ်ပိုင်ခွင့်`, not the official person. Independently adjudicate. |

The Oxford pages were opened directly on 2026-11-02. Cambridge dictionary pages returned HTTP 403 when opened directly; search-index snippets are useful leads only, **not direct-page observation, human verification or exact-sense CEFR signoff**. No dictionary definitions or examples were copied into the final curriculum. Five original English/Myanmar/example alternatives were drafted but remain explicitly unapproved.

## Provenance and mechanical QC

- [Five-card held research packet](draft/CEFR-1000-B1-FIVE-DEMAND-SUPPLY-FEATURE-APPLY-AUTHORITY-SENSE-TRIAGE-2026-11-02.json) preserves original first-pass content, source indices **381, 605, 690, 693, 694**, historical source Git blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`, direct Oxford URLs/line locators, Cambridge indexed access limitations and observation date.
- Frozen 1,000 shortlist Git blob: `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; five-card packet Git blob: `156f61c533e13e243f64dd8470a1cde9d85242af`. [Pinned fail-closed auditor](tools/audit_cefr_1000_b1_five_commercial_senses.py) verifies these, exact 200-per-level quota, casefold headword deduplication, historical bilingual provenance, all held review flags, source-access claims and proposed examples.
- Auditor has **146 programmed synthetic negative mutations**: 28 per record plus 6 packet-wide. These are not human reviews. All six CEFR structural lanes invoke the source audit, with the ALL lane invoking the synthetic tests. Documentary no-deploy QC also invokes the self-test.
- Structural run [41361487328](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41361487328) at SHA `09f8c33d9d76198877bf2c45bd9ad882c627aeb2` and documentary run [41361494717](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41361494717) at SHA `427345caffdea5f5fb8852b4bc40d82c8c9d38b7` were started; **actual final conclusions/logs require verification before claiming a pass**.

## Truthful counts and release gates

| Level | First-pass written | Independently checked/approved |
| --- | ---: | ---: |
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

**Release blocked.** Independently authenticated English, fluent Myanmar, original example, exact-sense CEFR and pronunciation signoff; 1,000-entry approved manifest; generated final George/Emma headword+example audio with real listening receipts; browser/mobile regressions; physical iPhone Safari listening; measured GitHub Pages limits; protected 54 lessons, separate IELTS bank, existing production audio/privacy preservation; and confirmed public deployment are all outstanding. No merge, main edit or public launch authorised until every gate has real evidence.
