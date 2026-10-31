# CEFR 1,000 — C1 seventeenth 12 Oxford source observations and seven direct dictionary sense leads
**Observed 1 November 2026 | Staging only | No human approval | No production changes**

## Approved scope and source method
User-approved **1,000 total** words, exactly **A1 200 / A2 200 / B1 200 / B2 200 / C1 200**; the old 5,000-word plan is superseded. Branch remains `cefr-5000-bilingual-qa-staging`. The frozen shortlist is `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; separate independent-review tasks remain pending.

Directly inspected the official [Oxford 3000 by CEFR](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) (12 pages) and [Oxford 5000 by CEFR](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) (8 pages). Both PDF text indexes returned **no match** for each of the 12 C1-draft headwords: **antagonistic, arbitrariness, assiduous, catharsis, circumvent, coalesce, conjecture, conscientious, culpability, disparage, dissonance, elucidate**. These are **twelve documented core-list absence observations, not twelve Oxford C1 classifications**. The words' exact-sense CEFR levels remain unverified.

## Seven direct dictionary sense leads
- [antagonistic](https://www.oxfordlearnersdictionaries.com/definition/english/antagonistic), lines 88–107: formal adjective, often *antagonistic to/towards*; distinguish hostile opposition from neutral disagreement
- [arbitrariness](https://www.oxfordlearnersdictionaries.com/definition/english/arbitrariness), lines 88–116: uncountable noun; decisions lacking a rational system versus unchecked power; the draft definition is too narrow
- [catharsis](https://www.oxfordlearnersdictionaries.com/definition/english/catharsis), lines 88–120: specialist noun for emotional release, countable or uncountable; plural *catharses*
- [circumvent](https://www.oxfordlearnersdictionaries.com/definition/english/circumvent), lines 88–119: transitive verb; evading a rule/difficulty versus physically going around an obstacle
- [coalesce](https://www.oxfordlearnersdictionaries.com/definition/english/coalesce), lines 88–113: formal intransitive verb, commonly *coalesce into* a larger whole
- [conscientious](https://www.oxfordlearnersdictionaries.com/definition/english/conscientious), lines 88–107: careful, thorough and responsible in duties; distinguish from *conscious*
- [disparage](https://www.oxfordlearnersdictionaries.com/definition/english/disparage), lines 88–112: formal transitive verb for belittling someone/something, not ordinary criticism

The seven dictionary pages were inspected directly. **Topic badges and Word-of-the-Day/footer CEFR labels belong to other contextual elements and cannot establish a headword or exact-sense CEFR level.** Seven original English/Myanmar/example rewrites were prepared solely as unapproved editorial alternatives; the frozen shortlist, 1,000 independent-review tasks, and reviewer flags were not changed.

## Provenance, safeguards and counts
The [12-record source-bound packet](draft/CEFR-1000-OXFORD-C1-SEVENTEENTH-TWELVE-AND-SEVEN-DIRECT-SENSE-LEADS-2026-11-01.json) retains each frozen English definition, Myanmar meaning, original example, historical Batch58 Git source path, row index and blob SHA `da7df62123acfac89a0acedad4652ec499c7ed3d`. The [fail-closed packet auditor](tools/audit_cefr_1000_oxford_c1_seventeenth_twelve.py) pins the packet Git blob and original shortlist, checks the historical row text and provenance, rejects fabricated source CEFR labels, reviewer receipts and listening claims, and defines **210 negative mutations**. Six parallel CEFR structural lanes and documentary no-deployment QC now invoke the new audit (C1 and ALL for the additional C1-specific check).

Consolidated *research coverage targets* after this packet: **A1 195/200, A2 200/200, B1 200/200, B2 200/200, C1 183/200 = 978/1,000 distinct**; **997** source observations, **22** without audited Oxford observations. Review priority expected: **94 core-list unlisted; 61 publisher-higher; 352 publisher-lower; 471 matching word/POS but exact sense unverified; 22 unobserved**. These are **source research counts, not linguistic approvals**; final numbers must be confirmed from actual GitHub Actions logs.

First-pass written / independently approved remain **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0**. Final British George/Emma headword-and-example listening signoffs remain **0/1,000**. Missing gates: genuine independent English/Myanmar/example/exact-sense CEFR reviews, 1,000-entry deduplicated approved manifest, full final dual-voice audio generated and actually listened to, browser/mobile regression, physical iPhone Safari evidence, measured GitHub Pages hosting limits, preserved-production-asset verification at release, and confirmed live deployment.

**Release BLOCKED — STAGING ONLY. No merge, main-branch modification, publication or deployment.**
