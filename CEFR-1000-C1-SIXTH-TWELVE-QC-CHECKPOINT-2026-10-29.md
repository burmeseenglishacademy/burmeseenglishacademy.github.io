# CEFR 1,000 — C1 sixth 12-word Oxford word/POS research checkpoint (29 October 2026)

**Scope:** the USER-APPROVED **1,000 TOTAL** provisional headwords, exactly **200 each at A1/A2/B1/B2/C1**. Staging branch `cefr-5000-bilingual-qa-staging` only. This is **editorial research, not an approved release**.

## New direct publisher observations

Directly inspected the official [Oxford 3000 by CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) and [Oxford 5000 by CEFR PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf) on **2026-10-29**. The [12-entry source packet](draft/CEFR-1000-OXFORD-C1-SIXTH-TWELVE-2026-10-29.json) preserves the exact publisher short excerpt, URL, date, one-based PDF page, zero-based extracted line, frozen English/Myanmar/example and historical Git provenance for every entry.

| Provisional C1 headword | Official Oxford word/POS level | Editorial risk requiring independent exact-sense review |
| --- | --- | --- |
| popularity (noun) | B2, Oxford 3000 p12 line 3077 | Draft C1 conflicts with B2 word/POS classification |
| sacred (adjective) | C1, Oxford 5000 p7 line 1737 | Religious holiness versus figurative sacredness |
| spy (noun) | C1, Oxford 5000 p7 line 1813 | Person (noun) versus action (verb) |
| suspension (noun) | C1, Oxford 5000 p7 line 1874 | Temporary interruption versus other noun senses |
| terrorism (noun) | B2, Oxford 5000 p3 line 633 | Lower Oxford word/POS classification; neutral definition |
| upgrade (verb) | C1, Oxford 5000 p8 line 1956 | Draft definition may incorrectly require replacement for every upgrade |
| warrant (noun) | C1, Oxford 5000 p8 line 1993 | Legal document versus justify (verb) |
| asset (noun) | B2, Oxford 5000 p1 line 37 | Draft mixes owned property and valuable people; example uses person |
| burden (noun) | C1, Oxford 5000 p4 line 867 | Figurative difficulty versus physical load |
| charter (noun) | C1, Oxford 5000 p4 line 895 | Founding document versus transport rental |
| civilian (noun) | C1, Oxford 5000 p4 line 903 | **Grammar/POS mismatch:** draft example *civilian families* uses adjective, not the labelled noun |
| coalition (noun) | C1, Oxford 5000 p4 line 911 | Political alliance versus generic cooperation |

**Important:** Oxford CEFR PDF classification is at the *word/part-of-speech* level; it does **not** prove that the draft definition/example's *exact sense* is at the stated CEFR level. Three B2-versus-C1 discrepancies are not automatic retier decisions. No independent reviewers or authentic human approval receipts exist.

## Research coverage after adding this packet

| Level | First-pass written | Distinct Oxford word/POS leads | Independently approved |
| --- | ---: | ---: | ---: |
| A1 | 200 | 112 | 0 |
| A2 | 200 | 60 | 0 |
| B1 | 200 | 72 | 0 |
| B2 | 200 | 70 | 0 |
| C1 | 200 | 51 | 0 |
| **Total** | **1,000** | **365** | **0** |

There are **384 observations covering 365 distinct provisional headwords**; duplicate observations do not increase coverage. The full reviewer handoff prioritises **635** entries with no direct Oxford word/POS observation in the audited packets, **137** publisher-lower entries, **10** publisher-higher entries, **3** unlisted entries (absence is not a CEFR level), and **215** word/POS matches still requiring independent exact-sense review. The 36 historical PDF excerpt recoveries are included, not added again.

## Safeguards and release blockers

The new [C1 source auditor](tools/audit_cefr_1000_oxford_c1_sixth_twelve.py) pins all twelve publisher locators/excerpts, historical Git references, original bilingual snapshots, editorial risk tasks and zero-approval flags, with **293 adversarial mutation cases**. The cross-batch auditor, 1,000-entry reviewer handoff and six parallel A1/A2/B1/B2/C1/ALL structural jobs have been updated. The documentary workflow is **report-only** and never deploys. A cross-batch test originally depended on the last C1 packet being an *unlisted* entry; that test was repaired to reference the historical packet explicitly, while adding mutations for the new packet.

**Unresolved launch gates:** all 1,000 human-independent English, Myanmar, original-example and exact-sense source-backed CEFR signoffs; exactly 200 approved deduplicated headwords/senses per level; final British George/Emma headword and example recordings plus actual listening signoffs (**0/1,000**); desktop/mobile browser regression; physical iPhone Safari evidence; measured GitHub Pages hosting limits; protected 54 lessons, separate IELTS 1,000 bank, established production audio/privacy inventory; and verified production deployment. **BLOCKED — STAGING ONLY. No merge, no publication, no main modification.**

## Verified GitHub Actions results

- [Six-lane structural run **40836481294**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40836481294), head `ba64022dec4e6d38fef75ab46b898bae18130377`: **SUCCESS** in all A1, A2, B1, B2, C1 and ALL jobs. Actual ALL-job logs confirm **293/293** new C1 adversarial mutations rejected, **20/20** cross-batch forged-evidence mutations rejected, **145/145** full reviewer-handoff integrity mutations rejected and the full 1,000-entry review handoff artifact `cefr-1000-provisional-ALL` uploaded (artifact ID **12881010852**). No independent approval or audio listening was asserted.
- [Documentary no-deploy run **40836481145**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40836481145), same head `ba64022dec4e6d38fef75ab46b898bae18130377`: **SUCCESS AS REPORT-ONLY**, not a release approval. Actual logs confirm 293/293 new mutations rejected, launch blockers retained, and protected production assets untouched. Blocker-report artifact ID **12881385204**.
- Intermediate runs failed because the existing cross-batch negative tests implicitly treated the newest C1 packet as the old packet with an unlisted final word; the tests were corrected to bind the old unlisted case to its original packet and use meaningful mutations on the new packet. The final two successful runs above are the verified ones.

### Unapplied editorial rewrite proposals (NOT approved)

**civilian (noun):** Original example *“The shelter was opened for civilian families.”* uses **civilian** adjectivally. Suggested noun-aligned example: *“A civilian received medical treatment at the shelter.”* Keep Myanmar headword `အရပ်သား` provisionally. An independent reviewer must decide whether to revise the example or change the target POS.

**asset (noun):** The example refers to staff as a valuable person, whereas the draft definition also mentions owned property. Possible person-sense definition: *“A person or thing that is valuable or useful to someone or an organisation.”* Possible Myanmar person-sense gloss: `တန်ဖိုးရှိပြီး အကျိုးပြုသော လူ သို့မဟုတ် အရာ`. Independent source-backed exact-sense B2-versus-C1 reconciliation remains mandatory.

**upgrade (verb):** The current definition requires replacing something, which may be too narrow. Possible revision: *“To make something better or more modern, especially by improving or replacing parts.”* The original software example is grammatically suitable for the verb. No content has been changed in the shortlist or live curriculum.

All proposals are **editorial suggestions only**; they have no independent linguistic or CEFR signoff and do not change release readiness.
