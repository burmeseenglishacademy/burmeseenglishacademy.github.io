# CEFR 1,000 — irregular forms and exact-sense review queue (2026-11-05)

**Status:** staging editorial work only. No independent review, CEFR publisher verification, audio signoff, or release approval is asserted.

## Immutable input and scope
- Provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, inspected 2026-11-05.
- Source evidence here is **internal provenance only**, not publisher-backed CEFR evidence. Every candidate requires external sense-specific source URL, date observed, reviewer identity, and independent English/Myanmar/example/level decisions before approval.
- 200 first-pass entries at each of A1, A2, B1, B2, C1; zero independently approved at every level. No shortlist or approval flags changed.

## Targeted morphology and exact-sense cases
| Entry | Level; original source index | Existing definition / example | Editorial finding and independent review question |
|---|---|---|---|
| people (plural noun) | A1; `draft/A1-EDITORIAL-STARTER.json` #43 | “More than one person.” / “Many people are here.” | Irregular plural of *person*; A2 *person* separately selected (#191). Check whether this is a justified lexical-sense progression or a duplicate lemma policy exception. Myanmar “လူတွေ၊ လူများ” is colloquial/neutral alternatives, not a singular gloss. |
| child (noun) | A1; same source #87 | “A young person who is not yet an adult.” / “The child is sleeping.” | Record plural *children* for future audio/example inflection handling, but do not create a new approved headword or count it toward 200. Myanmar “ကလေး” matches singular. |
| foot (noun) | A1; same source #179 | “The part of the body at the end of a leg.” / “My left foot hurts.” | Irregular plural *feet*; gloss “ခြေဖဝါး၊ ခြေထောက်” spans sole/foot/leg. Independently decide precise sense and natural Myanmar, then ensure audio uses approved sense. |
| run (verb) | A1; same source #196 | “To move on foot faster than walking.” / “I run in the park.” | *Ran* (past), *run* (participle), *running* (progressive). Avoid assuming an inflection represents a different CEFR lexical item. Review British audio pronunciation in example context. |
| better (adjective) | A2; `draft/A2-C1-EDITORIAL-STARTER.json` #86 | “Of a higher quality or more suitable than something else.” / “The second plan is better for our budget.” | Comparative of *good* (already A1). Decide explicit morphology exception vs distinct comparative-sense syllabus item; “ပိုကောင်းသော” is plausible but requires human review. |
| person (noun) | A2; same source #191 | “One human being considered as an individual.” / “Only one person can enter at a time.” | Relationship to A1 *people* must be resolved as an irregular plural/lexical usage exception, not silently treated as independent lemma. |
| thought (noun) | A2; same source #506 | “An idea or opinion that comes into your mind.” / “One thought kept me awake last night.” | The written form also serves as past/past participle of *think*. Here **noun**, so a blanket irregular-form deduper would wrongly reject it. Require noun-sense evidence, and separately verify noun pronunciation/audio. |
| worst (adjective) | B1; same source #57 | “The least good or most unpleasant of a group.” / “That was the worst storm of the year.” | Superlative of *bad*, with potentially distinct meaning/use from *worse*. Do not infer B1 CEFR from form or morphology; require publisher sense-specific evidence. |

## Proposed fail-closed implementation acceptance tests (not claimed implemented)
1. Preserve `(normalised headword, part_of_speech, exact sense)` and a separately reviewed `lemma_family`; never auto-collapse *thought* noun into *think* verb.
2. If two entries share a lemma family across levels, require a recorded human reviewer decision and source-supported distinct-sense/teaching justification; otherwise fail release, without changing provisional inventory.
3. Inflection mappings are for editorial alerts, not authoritative CEFR assignment; require documented exception for *person/people*, *good/better*, and similar irregulars.
4. Match example inflections through reviewed morphological forms; never auto-replace grammatically valid examples solely to force literal headword spelling.
5. Require British George and Emma headword/example audio against immutable approved text and hashes, with actual independent listening records; presence of generated files alone must fail.
6. Missing publisher URL, observation date, exact-sense CEFR label, reviewer identity or independent decision must fail release.
7. Preserve production 54 lessons, separate IELTS 1,000 bank, existing production George/Emma audio, and privacy policy.

## Remaining gates
A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0 (first-pass/independently approved). Audio: final 4,000 expected voice×headword/example assets unverified and not listened. Browser/mobile regression, physical iPhone Safari evidence, GitHub Pages hosting clearance, production asset-preservation verification and deployment unverified. Existing earlier five-lane CI results cannot be treated as validation of this documentation commit.

**Editorial next action:** obtain publisher-specific exact-sense URLs and observation dates for these eight cases; request independent bilingual/CEFR review and formal lemma-family decisions. Keep all 1,000 on hold.
