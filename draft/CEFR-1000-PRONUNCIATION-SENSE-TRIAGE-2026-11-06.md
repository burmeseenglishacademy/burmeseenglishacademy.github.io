# CEFR-1000 pronunciation and sense QA: read, progress, contest, suspect, graduate — 2026-11-06

**Status:** staging-only editorial triage; not publisher-backed CEFR confirmation, independent review, or audio listening evidence. Provisional inventory: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`). Inspected 2026-11-06. All entries retain editorial hold and unapproved flags.

| Word | Level / POS | Original example | Specific risk requiring independent assessment |
|---|---|---|---|
| read | A1 / verb | I read a book every night. | Present /riːd/ vs past /red/ are written identically. “Every night” implies habitual present, but TTS headword and example pronunciation must be checked independently. |
| progress | B1 / noun | The students made good progress this term. | Noun /ˈprəʊ.ɡres/ vs verb /prəˈɡres/ (British stress). Do not synthesize verb stress for the noun. |
| contest | B2 / noun | She entered a photography contest. | Noun typically first-syllable stress; verb “contest” typically second-syllable stress. Distinguish competition from disputing a decision. |
| suspect | B2 / verb | The technician began to suspect a faulty cable. | Verb stress differs from the noun/adjective “suspect”; confirm that the selected voice reads the verb. “Suspect” means infer without certainty, not necessarily accuse a person. |
| graduate | B2 / verb | She hopes to graduate from university next year. | Verb vs noun pronunciation and sense require checking; avoid noun reading in headword audio. Myanmar translation must capture successful completion, not merely attendance. |

## Original provisional wording and provenance

- **read**: definition “To look at written words and understand them.”; Myanmar “ဖတ်သည်”; source `draft/A1-EDITORIAL-STARTER.json` index 30, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- **progress**: definition “Movement towards a better or more complete result.”; Myanmar “တိုးတက်မှု”; source index 616.
- **contest**: definition “A competition in which a winner is chosen.”; Myanmar “ပြိုင်ပွဲ”; source index 146.
- **suspect**: definition “To think something may be true without being certain.”; Myanmar “သံသယရှိသည်၊ ဖြစ်နိုင်သည်ဟု ထင်မြင်သည်”; source index 390.
- **graduate**: definition “To complete a course of study and receive a qualification.”; Myanmar “သင်တန်း သို့မဟုတ် ဘွဲ့သင်တန်းပြီးဆုံး၍ အောင်မြင်သည်”; source index 489.

For the latter four, the exact original source path/blob SHA remain in the provisional inventory and must be copied into any independently signed review record; do not infer them from index alone.

## External evidence queue (not yet observed in this run)

Publisher lookup targets, **not citations asserting verified CEFR**:
- https://dictionary.cambridge.org/dictionary/english/read
- https://dictionary.cambridge.org/dictionary/english/progress
- https://dictionary.cambridge.org/dictionary/english/contest
- https://dictionary.cambridge.org/dictionary/english/suspect
- https://dictionary.cambridge.org/dictionary/english/graduate

Reviewer must record exact publisher sub-sense, CEFR badge if actually displayed, UK IPA, observation date, and whether that badge applies to the provisional POS and meaning. A headword-level search result is insufficient. Independently check grammar and idiomatic Myanmar for each sentence; separately listen to both George and Emma headword and full example audio. No source URLs above have been independently checked as evidence by this triage.

## Release gate

Counts remain A1=200, A2=200, B1=200, B2=200, C1=200 first-pass entries; independently approved=0 at each level. This note neither changes entries nor establishes CEFR, human review, generated audio, listening, device QA, hosting or deployment. Keep release blocked and protect existing 54 lessons, separate IELTS vocabulary and production audio.
