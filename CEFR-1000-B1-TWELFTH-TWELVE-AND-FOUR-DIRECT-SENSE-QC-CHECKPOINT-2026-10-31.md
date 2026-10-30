# CEFR 1000 — B1 twelfth Oxford twelve, four direct dictionary sense leads (31 October 2026)

**STAGING ONLY; NO independent review, no approval, no publication.** Scope is **1,000 total** (A1/A2/B1/B2/C1 exactly 200 provisional entries each), not the superseded 5,000-word plan. Work confined to `cefr-5000-bilingual-qa-staging`. Frozen shortlist and separate reviewer tasks are unchanged.

## Direct Oxford University Press evidence

Official [Oxford 3000 by CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) directly inspected on **2026-10-31**. All twelve word/POS matches occur in that PDF. PDF page is **1-based**; extracted line is **0-based**. These are **publisher headword/POS-level** classifications, **not** independently validated exact-sense CEFR.

| Provisional B1 headword | Oxford word/POS | PDF page / extracted line | Editorial priority |
|---|---|---|---|
| achieve (verb) | A2 | 4 / 915 | Publisher lower |
| afford (verb) | B1 | 7 / 1796 | Matching POS/level; exact sense pending |
| category (noun) | B1 | 7 / 1878 | Matching POS/level; exact sense pending |
| relevant (adjective) | B2 | 12 / 3131 | Publisher higher |
| fresh (adjective) | A2 | 5 / 1235 | Publisher lower |
| scale (noun) | B2 | 12 / 3162 | Publisher higher |
| score (noun) | A2 | 6 / 1587 | Publisher lower; PDF includes noun and verb |
| smart (adjective) | B1 | 9 / 2446 | Matching POS/level; exact sense pending |
| throw (verb) | A2 | 7 / 1705 | Publisher lower |
| wedding (noun) | A2 | 7 / 1757 | Publisher lower |
| feature (noun) | A2 | 5 / 1204 | Publisher lower |
| target (noun) | A2 | 7 / 1690 | Publisher lower |

**Counts:** A2 7, B1 3, B2 2; **9** provisional B1 word/POS discrepancies. Source URLs, observation date, line/page, original English/Myanmar/example snapshots, historical Git source path/index/blob and human review tasks are preserved in [the twelve-record research packet](draft/CEFR-1000-OXFORD-B1-TWELFTH-TWELVE-AND-FOUR-DIRECT-SENSE-LEADS-2026-10-31.json).

## Four directly inspected Oxford dictionary sense leads

The following dictionary pages were opened and inspected on **2026-10-31**, independently of the CEFR PDF word/POS lookup. They support sense triage but **not** independent human approval:

- [afford, verb, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/afford), page text lines 112–125: financial ability; normally modal or negative; do not confuse with formal *afford somebody something*
- [fresh, adjective, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/fresh_1), lines 108–125: recently picked or produced food; not *fresh evidence* or *fresh air*
- [scale, noun, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/scale_1), lines 106–119: size/extent; distinguish from a numbered rating scale
- [target, noun, sense 1](https://www.oxfordlearnersdictionaries.com/definition/english/target_1), lines 105–115: an intended, often measurable result; not a shooting target

Four original Myanmar translations and grammatical example alternatives are **UNAPPROVED EDITORIAL PROPOSALS**, not replacements. Original shortlist text is unchanged. Dictionary page topic tags or unrelated Word-of-the-Day footers are not used as headword CEFR evidence.

## Source integrity and release safeguards

[Fail-closed auditor](tools/audit_cefr_1000_oxford_b1_twelfth_twelve.py) pins the research packet Git blob and frozen shortlist Git blob, all twelve publisher word/POS/page/line observations, original bilingual/examples, historical provenance, four sense locators and false-signoff controls. It contains **180 adversarial mutation cases** (15 per word). Wired to the existing **six parallel A1/A2/B1/B2/C1/ALL structural jobs** and documentary no-deployment QC. Success of structural tests is **not** independent human review or release clearance.

Expected reconciled Oxford word/POS coverage, subject to actual successful CI: **A1 195/200, A2 132/200, B1 156/200, B2 142/200, C1 111/200 = 736/1,000**; 264 unobserved, 755 observations. Reviewer priorities: 3 unlisted, 42 publisher higher, 269 publisher lower, 422 matching word/POS but exact-sense unverified, 264 without direct Oxford observations. **Do not report these as CI-verified until jobs and logs are checked.**

## Release status

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

Final British George/Emma **real headword+example listening signoffs 0/1,000**; full final audio generation/listening unverified. Independent English/Myanmar/example and exact-sense CEFR review, approved-corpus browser/mobile regression, **real physical iPhone Safari**, measured GitHub Pages size/bandwidth, confirmed production deployment and post-deploy preservation evidence all absent. The 54 production lessons, separate IELTS 1,000-word bank, established George/Emma audio and privacy are protected. **RELEASE BLOCKED / STAGING ONLY; do not merge or publish.**
