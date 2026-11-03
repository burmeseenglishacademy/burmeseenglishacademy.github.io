# CEFR-1000 historical provenance: first authenticated source checkpoint — 2026-11-03

**Scope:** approved 1,000-total project only (200 each A1/A2/B1/B2/C1). Staging documentary evidence, **not** independent editorial review or release clearance.

## Direct GitHub repository readback

Fetched `draft/A1-EDITORIAL-STARTER.json` from `cefr-5000-bilingual-qa-staging` through the connected GitHub repository API on 2026-11-03. GitHub returned blob SHA `ff1e93f60828ef2f94c9146522ce94075183b0ae`, exactly matching the `source_blob_sha` on provisional A1 entries `a`, `an` and `be` (and the visible `i` entry). Fetched `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; GitHub returned blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`.

Verified the first three provisional source slots against the returned historical JSON record sequence:
- `a`: source index 0; A1 article; English definition “Used before one person or thing when it is not specified.”; Myanmar “တစ်ခု၊ တစ်ယောက် (မသတ်မှတ်ရသေးသော)”; example “I have a book.”
- `an`: source index 1; A1 article; English definition “Used before one person or thing when the next word starts with a vowel sound.”; Myanmar “တစ်ခု၊ တစ်ယောက် (သရသံဖြင့်စသော စကားလုံးရှေ့တွင်)”; example “She has an apple.”
- `be`: source index 2; A1 verb; English definition “To exist or to have a particular quality or identity.”; Myanmar “ဖြစ်သည်၊ ရှိသည်”; example “I want to be a teacher.”

These are **historical copy/provenance comparisons only**, not evidence that any sense, CEFR classification, translation, or example has been independently validated. The original source's own flags explicitly remain false. Its publisher and British Council references are leads, not proof of exact-sense independent review.

## Residual work and fail-closed interpretation

This authenticates **one currently retrievable source file's GitHub blob identity and three directly compared source slots**, not all seven source files or all 1,000 records. The source blob is retrieved at the staging branch; an independently controlled immutable historical ref/lockfile is still required to prevent a coordinated rewrite of source and shortlist. Next: enumerate all source-path/blob pairs, retrieve each Git object, verify all 1,000 indexed record fields and source slots, pin an independently governed historical lock, and test negative cases (wrong SHA, wrong index, altered Myanmar, source record mismatch). Do not conflate repository consistency with publisher CEFR evidence.

Counts remain **A1 200/0, A2 200/0, B1 200/0, B2 200/0, C1 200/0** (first-pass written / independently approved). All entries remain on editorial hold. No final approved manifest, 4,000 fully listened-to George/Emma audio assets, physical iPhone Safari evidence, mobile regression signoff, hosting clearance or production deployment has been established. **Release BLOCKED.** No production files changed.

## Links

- [Historical source](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/A1-EDITORIAL-STARTER.json)
- [Frozen provisional shortlist](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json)
- [Historical provenance gate specification](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-HISTORICAL-PROVENANCE-AUTHENTICATION-GATE-2026-11-03.md)
