# CEFR 1,000 — nine cross-level irregular forms and quantifier senses (1 November 2026)

**STAGING ONLY / RELEASE BLOCKED.** Scope is the user-approved 1,000 total, **200 A1 + 200 A2 + 200 B1 + 200 B2 + 200 C1**, not the superseded 5,000-word proposal. Frozen first-pass entries and the independent review task queue remain untouched. No independent approval, real George/Emma listening, iPhone testing, merge or publication is represented here.

## Direct publisher observations, 1 November 2026

| Frozen held entries | Directly inspected evidence | Source-bound editorial finding |
| --- | --- | --- |
| **good** A1 / **better** A2 | [Oxford good adjective](https://www.oxfordlearnersdictionaries.com/definition/english/good_1) lines 88–135; [Oxford better adjective](https://www.oxfordlearnersdictionaries.com/definition/english/better_1) lines 88–113 | **better** is explicitly the comparative of **good**; held A2 quality comparison is not a separate lexeme. A1 good remains a valid base adjective control. |
| **bad** A2 / **worst** B1 | [Oxford bad adjective](https://www.oxfordlearnersdictionaries.com/definition/english/bad_1) lines 88–137; [Oxford worst adjective](https://www.oxfordlearnersdictionaries.com/definition/english/worst_1) lines 88–111 | **worst** is explicitly the superlative of **bad**, not an independent lexeme in its frozen sense. Original worst-storm example is grammatical. |
| **little** A1 / **less**, **least** A2 | [Oxford little adjective](https://www.oxfordlearnersdictionaries.com/definition/english/little_1) lines 88–134; [Oxford less determiner](https://www.oxfordlearnersdictionaries.com/definition/english/less_1) lines 88–110; [Oxford least determiner](https://www.oxfordlearnersdictionaries.com/definition/english/least_1) lines 88–113 | Held **little dog** describes *size*; **less sugar** and **least effort** are quantity determiners. Oxford states *smaller/smallest* are usual for size comparison. Do **not** falsely ban less/least as identical to the size-adjective card; human POS/sense/CEFR review is still required. |
| **people** A1 / **person** A2 | [Oxford people](https://www.oxfordlearnersdictionaries.com/definition/english/people_1) lines 88–115; [Oxford person](https://www.oxfordlearnersdictionaries.com/definition/english/person) lines 88–115 | Oxford explicitly identifies **people** as the ordinary plural of **person**. A1 plural versus A2 singular is a cross-level pedagogical/counting question, not automatically an error or CEFR retiering. |
 
Nine frozen rows (**A1 3, A2 5, B1 1**) and 16 direct publisher page observations are preserved in [the source-bound research packet](draft/CEFR-1000-CROSSLEVEL-IRREGULAR-COMPARATIVES-AND-QUANTIFIERS-NINE-2026-11-01.json), including original English/Myanmar/examples, source path/index/blob SHA, observed URLs, dates and line locators. All nine Myanmar teaching notes and example alternatives are **UNAPPROVED**. None of the Oxford dictionary entries supplies independent exact-sense CEFR or bilingual signoff. Oxford topic/footer labels must not be misattributed to these senses.

## Concrete fail-closed improvement

The existing [final-manifest validator](tools/validate_cefr_release.py) already rejects A1 inflections **is/are** (of be) and **does/did** (of do). It now also rejects the frozen comparative **better** (good) and superlative **worst** (bad) as independently counted lexical headwords, while allowing the different size/quantity and person/people senses to proceed to genuine independent human review. This does **not** automatically select replacement vocabulary, alter quotas or approve any entry.

The [nine-card integrity auditor](tools/audit_cefr_1000_crosslevel_irregular_nine.py) freezes all source observations and original bilingual snapshots, checks the full 1,000-entry Git blob, per-level quotas, unique provisional headwords and false approval flags, exercises synthetic final-manifest inflection regressions, and rejects adversarial source/provenance/grammar/Myanmar changes. Both staging-only GitHub Actions workflows now run it: six parallel A1/A2/B1/B2/C1/ALL structural lanes and documentary no-deployment QC. Release regression tests also check that less/least/little/person/people are not over-banned.

## Independent handoff and remaining gates

An independent human reviewer must decide how to replace or restructure **better/worst** without losing the exactly 200 genuine independently reviewed lexical senses per level, and document a rationale for **person/people** and the different **little/less/least** senses. A valid UK George/Emma recording requires the **approved** sense and correct example, with actual per-voice listening signoff; no recording/listening receipt has been fabricated.

Written first-pass / independently approved remains **A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0**. Final approved manifest absent; independent word receipts **0**; final George/Emma real listening receipts **0**; automated browser receipts **0**; physical iPhone Safari, measured GitHub Pages hosting, privacy/preservation human signoff and production confirmation missing. Protect the 54 lessons, separate IELTS 1,000-word bank, existing George/Emma audio and privacy. **NO MERGE / NO MAIN EDIT / NO PUBLICATION.**

CI run IDs and conclusions must be appended only after reading actual GitHub Actions jobs and logs. A successful structural or report-only run never means release approval.
