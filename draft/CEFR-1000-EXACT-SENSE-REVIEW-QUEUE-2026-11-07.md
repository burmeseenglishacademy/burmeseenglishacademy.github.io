# CEFR-1000 release-risk triage: exact-sense and provenance queue (2026-11-07)

**Scope:** user-approved 1,000 total, A1/A2/B1/B2/C1 × 200. Staging only. This document is self-audit and reviewer handoff, **not** an independent review or a release approval.

## Reproducible baseline
Read `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` from `cefr-5000-bilingual-qa-staging` on 2026-11-07, blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Parsed `entries` and counted level, Boolean flags, empty evidence fields and case-folded headwords. A1=200, A2=200, B1=200, B2=200, C1=200; 1,000/1,000 editorial holds; 1,000 distinct case-folded headword strings (this **does not** prove sense-level deduplication). All five reviewed flags and `release_approved`: 0 true. All 1,000 entries lack each of `source_english`, `source_burmese`, `source_level` (3,000 empty evidence fields). Written first-pass=200 per level; independently checked=0 per level.

## High-priority independent sense/level adjudication
Each line reproduces the provisional entry's exact sense and sentence, not a new approved classification. Consult publisher pages for **the specific part of speech and meaning**, capture the dated publisher wording and any CEFR label, and have a separate qualified reviewer sign off on English, fluent Myanmar, example grammar and level. The publisher links below are research targets, **not newly verified source observations**.

| Provisional level | Headword | Provisional definition / example | Specific issue for reviewer | Publisher lookup |
|---|---|---|---|---|
| A1 | minute (noun) | “A period of sixty seconds.” / “Wait one minute, please.” | Duration of 60 seconds vs idiomatic “a moment” reading; align example with sense | https://dictionary.cambridge.org/dictionary/english/minute |
| A2 | project (noun) | “A planned piece of work with a particular goal.” / “Our class project is about saving water.” | School project sense vs broader planned-work sense | https://dictionary.cambridge.org/dictionary/english/project |
| B1 | actual (adjective) | “Real, rather than planned, expected, or imagined.” / “The actual cost was lower than our estimate.” | Check B1/B2 exact-sense mismatch; never translate as “current” | https://dictionary.cambridge.org/dictionary/english/actual |
| B1 | eventually (adverb) | “In the end, after a period of time or several difficulties.” / “After several attempts, she eventually solved the problem.” | Check B1/B2 mismatch and natural Myanmar time progression | https://dictionary.cambridge.org/dictionary/english/eventually |
| B2 | grab (verb) | “To take hold of something suddenly or quickly.” / “She grabbed her bag and ran outside.” | Physical grasp vs other figurative B2 senses | https://dictionary.cambridge.org/dictionary/english/grab |
| B2 | historic (adjective) | “Important enough to be remembered as part of history.” / “The agreement was a historic moment for the town.” | B1/B2 publisher conflict; distinguish *historical* | https://dictionary.cambridge.org/dictionary/english/historic |
| B2 | graduate (verb) | “To complete a course of study and receive a qualification.” / “She hopes to graduate from university next year.” | University degree completion vs broader training completion; pronunciation depends on POS | https://dictionary.cambridge.org/dictionary/english/graduate |
| B2 | conduct (verb) | “To organise and carry out an activity.” / “The team will conduct a safety inspection.” | Verb sense, not noun behaviour or musical direction | https://dictionary.cambridge.org/dictionary/english/conduct |
| B2 | sensitive (adjective) | “Needing careful handling because it may cause offence or harm.” / “The manager discussed the sensitive issue privately.” | Topic/issue sense vs emotional/physical sensitivity | https://dictionary.cambridge.org/dictionary/english/sensitive |
| C1 | permit (noun) | “An official document giving permission for a particular activity.” / “The contractor applied for a permit before starting work.” | Official document noun vs permission verb; assess B2/C1 publisher disagreement | https://dictionary.cambridge.org/dictionary/english/permit |

The 10 entries above were located in the current provisional JSON; earlier staging research documents describe some publisher observations. This handoff does not re-certify those observations, and no source field or reviewer flag has been changed.

## Fail-closed reviewer evidence contract
For **each** approved headword+sense, require stable ID; normalized headword and POS; exact publisher sense and CEFR observation with URL, date and quoted/identified sense; independently signed English definition, idiomatic Myanmar translation, original example and pronunciation; reviewer identity distinct from the draft author; recorded decision and timestamp; and immutable provenance to source entry. Conflicting or absent publisher labels must remain unresolved, not silently treated as approvals. A cross-level move must preserve 200 entries per level and global headword+sense uniqueness after independently reviewed replacements.

Release gate must reject: missing or self-attested reviewer signoff; any evidence field empty; ambiguous exact sense; wrong level counts or duplicate sense IDs; missing George/Emma headword **or** example audio; missing *actual listening* signoff for both voices; missing browser/mobile regression or physical iPhone Safari evidence; GitHub Pages size/hosting clearance; absent confirmed production deployment; or changes to the 54 lessons, separate IELTS 1,000 bank, existing production George/Emma audio or privacy policies. A green structural-negative test is not proof of any of these positive gates.

## Current blockers and next actions
- All five levels: 200 first-pass written, **0 independently checked**, **0 approved**.
- Final-list George/Emma headword/example audio: not evidenced complete; listening signoff: none established.
- Browser/mobile regression, physical iPhone Safari, Pages limits, production deployment and production asset preservation: not established.
- Independent-review task file `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` was fetched at blob SHA `88f472e4c79e5e9b6ae5957f5244f9cb60dc0ef2`, but the connector returned an empty content string; its substantive contents cannot be validated in this run.
- Next: collect *observed* publisher evidence for each exact sense and independent bilingual review; integrate signed evidence into fail-closed release manifest only after review. Verify fresh per-job Actions conclusions and logs for any future test commit. **No launch.**
