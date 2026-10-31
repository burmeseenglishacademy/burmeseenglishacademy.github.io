# CEFR 1,000 — C1 eighteenth twelve + final five Oxford source and sense QC
**Observed 2026-11-01 | STAGING ONLY | NO INDEPENDENT APPROVAL | NO DEPLOYMENT**

## Scope and provenance
The USER-APPROVED total is **1,000** provisional bilingual entries, exactly 200 per A1/A2/B1/B2/C1. This checkpoint covers the remaining **17 C1 entries**, not any superseded 5,000-word proposal. Frozen source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. All seventeen trace to historical Batch58 or Batch59 Git blobs; each packet records exact source path, index, blob SHA, original English, Myanmar and example. Frozen shortlist and review tasks remain unchanged.

Source-bound packets: [eighteenth twelve](draft/CEFR-1000-OXFORD-C1-EIGHTEENTH-TWELVE-AND-SIX-DIRECT-SENSE-LEADS-2026-11-01.json) and [final five](draft/CEFR-1000-OXFORD-C1-FINAL-FIVE-AND-THREE-DIRECT-SENSE-LEADS-2026-11-01.json). Each word was searched in both directly inspected official Oxford PDFs:
- [Oxford 3000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf)
- [Oxford 5000 by CEFR level](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf)

All seventeen exact headwords were absent from both inspected core lists. **Absence does not establish C1, another CEFR level, or any independent review.** These are source-scope observations only.

## Eighteenth C1 set (12)
entrench; equanimity; equivocate; extrapolate; fortitude; inadvertent; irrevocable; misconstrue; obfuscate; relinquish; superfluous; salience.

Six direct dictionary observations:
- [entrench](https://www.oxfordlearnersdictionaries.com/definition/english/entrench) (lines 101–114): usually passive; sometimes disapproving; common *entrenched in* pattern.
- [equivocate](https://www.oxfordlearnersdictionaries.com/definition/english/equivocate) (lines 101–113): formal, deliberately evasive/unclear; *equivocate on* construction.
- [extrapolate](https://www.oxfordlearnersdictionaries.com/definition/english/extrapolate) (lines 101–115): extrapolation *from* evidence *to* another situation; warns against over-generalisation.
- [inadvertent](https://www.oxfordlearnersdictionaries.com/definition/english/inadvertent) (lines 101–104): accidental/unintentional; unrelated B2 footer must not be assigned to headword.
- [obfuscate](https://www.oxfordlearnersdictionaries.com/definition/english/obfuscate) (lines 101–111): *usually* deliberately, not necessarily always. The provisional English definition states intent as mandatory; independent sense review needed.
- [salience](https://www.oxfordlearnersdictionaries.com/definition/english/salience) (lines 101–108): uncountable/singular; *salience for* construction. The C1 Oxford 5000 footer labels unrelated *applicable*, not *salience*.

Six English/Myanmar/example alternatives are explicitly **unapproved editorial proposals**, not substitutions in the frozen shortlist.

## Final C1 set (5)
abstruse; acrimonious; adulation; affable; alacrity.

Three direct dictionary observations:
- [abstruse](https://www.oxfordlearnersdictionaries.com/definition/english/abstruse) (lines 101–106): formal, often disapproving; an abstruse argument is difficult to understand, not merely unfamiliar.
- [affable](https://www.oxfordlearnersdictionaries.com/definition/english/affable) (lines 101–105): pleasant, friendly, easy to talk to. **Personal qualities c2** is a topic label, not a CEFR label for the word; the unrelated B2 footer must also be ignored.
- [alacrity](https://www.oxfordlearnersdictionaries.com/definition/english/alacrity) (lines 101–106): formal, uncountable, enthusiasm or happiness, often *with alacrity*. The provisional emphasis on speed may overstate the inspected exact sense.

Three additional English/Myanmar/example alternatives are unapproved.

## Coverage reconciliation (source observations, not approvals)
| Level | First-pass written | Distinct Oxford observations | Independently approved |
|---|---:|---:|---:|
| A1 | 200 | 195 | 0 |
| A2 | 200 | 200 | 0 |
| B1 | 200 | 200 | 0 |
| B2 | 200 | 200 | 0 |
| C1 | 200 | 200 | 0 |
| **Total** | **1,000** | **995** | **0** |

There are **1,014 research observations** including historical duplicate observations; **5 A1 entries** (is, are, does, did, rabbit) still lack audited exact word/POS Oxford core-list observations. These have previously documented lemma/inflection and rabbit A2 sense risks. The priority queue now has **111 unlisted**, **61 publisher-higher**, **352 publisher-lower**, **471 matching word/POS but exact-sense-unverified**, **5 unobserved**; these five categories sum to 1,000. Even all 995 observed words remain unapproved.

## Fail-closed staging QC
- [Eighteenth packet auditor](tools/audit_cefr_1000_oxford_c1_eighteenth_twelve.py): pins immutable packet Git blob and historical Batch58 provenance; 210 negative mutations defined.
- [Final-five packet auditor](tools/audit_cefr_1000_oxford_c1_final_five.py): pins immutable packet Git blob and historical Batch59 provenance; 91 negative mutations defined.
- Integrated both into six parallel A1/A2/B1/B2/C1/ALL structural lanes (new packet audit restricted to C1/ALL, mutation testing on ALL), and documentary no-deploy workflow.
- Consolidated Oxford coverage and independent-review handoff expect **995/1,000** research observations and **0 human approvals**. Structural CI PASS must not be confused with a human review.

**Release remains BLOCKED / STAGING ONLY** until independent exact-sense/CEFR/English/Myanmar/example signoff, 200 deduplicated approved entries per level, all final British George/Emma headword+example files actually generated and listened to, desktop/mobile regression, physical iPhone Safari evidence, measured GitHub Pages limits, production asset preservation and verified live deployment. No main changes, merge, publication, real listening or device verification is claimed.
