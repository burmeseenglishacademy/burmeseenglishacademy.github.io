# CEFR-1000 exact-sense and part-of-speech triage — 2026-11-06

**Status: editorial investigation only; not independent review, not CEFR certification, not publication approval.** Source inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected 2026-11-06. Original upstream provenance remains in each entry's `source_path`, `source_index`, and `source_blob_sha`. No external dictionary was consulted for the judgments below; no CEFR grade is asserted from this audit.

## Structural observations

Parsed 1000 entries. Level counts: A1 200; A2 200; B1 200; B2 200; C1 200. Exact case-folded headword collisions across levels: 0. **This does not establish sense-level uniqueness**, source-backed level correctness, or editorial approval. Independent approvals reported in manifest: {"A1":0,"A2":0,"B1":0,"B2":0,"C1":0}. All entries remain on hold.

## Priority human-review queue (actual provisional entries)

| Level | Headword | Recorded POS | Provisional English definition | Provisional example |
|---|---|---|---|---|
| A2 | public | noun | People in a community or society in general. | The library is open to the public. |
| A2 | company | noun | A business that sells goods or services. | She works for a small company. |
| A2 | case | noun | A particular situation or example of something. | In this case, we should wait. |
| A2 | party | noun | A social event where people meet to enjoy themselves. | We invited our neighbours to a birthday party. |
| A2 | better | adjective | Of a higher quality or more suitable than something else. | The second plan is better for our budget. |
| B1 | cancer | noun | A serious illness in which some cells in the body grow without control. | The doctor explained how cancer treatment works. |
| B1 | ship | noun | A large boat used to carry people or goods across water. | The ship arrived at the port this morning. |
| B1 | band | noun | A group of musicians who perform together. | The band played at the school festival. |
| B1 | fan | noun | A device that moves air to help cool a room or person. | She turned on the fan because the room was warm. |
| B1 | fighting | noun | Physical conflict or an attempt to stop an opponent. | The fighting stopped before sunrise. |
| B2 | print | noun | Letters or words that appear on a printed surface. | The print on the label is too small to read. |
| B2 | reporting | noun | The activity of giving information about events. | Accurate reporting helps the public understand events. |
| B2 | motor | noun | A machine that produces movement or power. | The motor stopped when the power failed. |
| C1 | signature | noun | A person's name written in their own handwriting. | Please add your signature at the bottom of the form. |
| C1 | upgrade | verb | To improve something by replacing it with a newer or better version. | We will upgrade the software next month. |
| C1 | warrant | noun | An official legal document giving authority to take a particular action. | The police obtained a warrant to search the building. |
| C1 | spy | noun | A person who secretly collects information for another organisation. | The spy passed information to another country. |
| C1 | divine | adjective | Connected with a god or a religious power. | The painting shows a divine figure. |
| A1 | the | article | Used to refer to a particular person or thing. | The book is on the table. |
| A1 | that | determiner | Used to point to a person or thing farther away. | That house is big. |

## Concrete review questions / risks

- **A2 public (noun)**: check whether the definition/example really illustrate the collective noun *the public*, not adjective *public*. Demand sense-specific dictionary evidence and a natural Myanmar rendering.
- **A2 company, case, party**: each is polysemous; capture the exact meaning used in the example and avoid applying a publisher's CEFR grade from another sense.
- **A2 better**: distinguish adjective comparative from adverb and verb; check the comparison and target grammatical sense.
- **B1 cancer**: medical term requires factual, sensitive wording and accurate Myanmar equivalent; no assumed CEFR from frequency.
- **B1 ship, band, fan, fighting**: check noun-versus-verb and multiple noun senses; particularly *fan* (supporter vs air-moving device), *band* (music vs strip), and *ship* (vessel vs send).
- **B2 print (noun), reporting (noun), motor (noun)**: confirm examples actually demonstrate the listed POS and lexical sense; beware derived forms being matched as unrelated lemmas.
- **C1 signature, upgrade, warrant, spy, divine**: highly polysemous or potentially common at lower levels in certain senses; publisher evidence must match the exact POS and sense, not just the spelling.
- **A1 the / that**: previously researched determiner and article uses require careful disambiguation from conjunction, relative pronoun and degree adverb uses; see separate dated publisher-evidence notes in `draft/`.

## Required next evidence for each queued entry

Record publisher URL, access date, publisher's explicit CEFR label (or **not stated**), exact dictionary sense and POS, observed example or sense cue, original upstream file/index/blob SHA, reviewer-independent English check, fluent Myanmar check, original-example grammatical check, and cross-level-conflict decision. A dictionary's generic word page or a historical WordNet gloss is **not** evidence that the shortlisted sense has the requested CEFR grade. If publisher CEFR is absent or ambiguous, keep the entry blocked. This report is only a reproducible triage; do not flip any `reviewed_*`, `editorial_hold`, or `release_approved` flags.

## Release gates unchanged

Written first-pass: A1/A2/B1/B2/C1 = 200/200/200/200/200. Independently checked: 0/0/0/0/0. George/Emma headword+example audio and actual listening signoff: unverified. Browser/mobile regression, physical iPhone Safari, hosting and deployment: unverified. Remain staging only. Preserve 54 lessons, separate IELTS vocabulary bank, existing production audio and privacy policy.
