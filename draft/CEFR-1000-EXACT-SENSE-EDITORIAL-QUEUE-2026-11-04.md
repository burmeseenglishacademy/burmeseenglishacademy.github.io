# CEFR-1000 exact-sense editorial corrections queue — 2026-11-04

**Status:** staging-only candidate edits; NOT independently reviewed, NOT publisher-backed CEFR confirmation, NOT a production release. Frozen shortlist unchanged. Scope remains 200 entries each A1/A2/B1/B2/C1, all 1,000 on hold and independently approved 0/200 in every level.

## Reproducible observation and provenance

Observed on 2026-11-04 from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`, staging branch `cefr-5000-bilingual-qa-staging`. All source indexes below are the **entry's own source_index**, not the position in the 1,000-item shortlist. Original source records are in the indicated `source_path`; the provisional JSON also contains per-entry `source_blob_sha`. Candidate sentences are original editorial proposals, not quotations or independently approved text.

| Level / entry | Observed concern | Proposed action for independent review |
|---|---|---|
| A1 `i` (pronoun), `draft/A1-EDITORIAL-STARTER.json` index 3 | Headword is lowercase `i` although the first-person singular pronoun is conventionally written `I`; the example correctly uses `I`. | Candidate canonical headword `I`. Keep the source unchanged until identity/provenance and audio filenames are reconciled. |
| A1 `is` (verb), same source index 120 | The definition describes a present form of `be`, but `is` is an inflected form, not a new independent lexical sense. | Ask the reviewer to decide whether to keep an explicitly labelled high-frequency form, or replace it with a distinct headword; do not infer a CEFR grade from the form alone. |
| A1 `train` (noun), same source index 90 | Railway vehicle noun is distinct from the verb `train` and A2 noun `training`. | Preserve the railway-vehicle sense in any sense ID and examples; do not merge with job-skills training. |
| A2 `training` (noun), `draft/A2-C1-EDITORIAL-STARTER.json` index 603 | Work-skills learning noun is morphologically related to the verb `train`, not the A1 railway-vehicle noun. | Review as its own sense; the sentence `New workers receive safety training.` fits the definition. |
| A1 `like` (verb), `draft/A1-EDITORIAL-STARTER.json` index 41 | Enjoyment verb is not the same lexical sense as A2 `likely` adjective. | Keep separate; no cross-level duplicate should be inferred from the shared letters. |
| A2 `likely` (adjective), `draft/A2-C1-EDITORIAL-STARTER.json` index 833 | Probability adjective; `It is likely to rain before evening.` is grammatically aligned. | Keep the probability sense distinct from `like`; independently check CEFR for this specific adjective use. |
| B1 `civil` (adjective), `draft/A2-C1-EDITORIAL-STARTER.json` index 51 | Definition: `Connected with ordinary citizens rather than the military.` Example: `The group works to protect civil rights.` The example invokes civil rights, a legal/social-rights use that does not clearly exemplify the civilian-versus-military contrast. | Candidate example for the existing definition: `The military handed control to a civil administration.` Alternatively retain the civil-rights example only after rewriting the definition and documenting that distinct sense. Independent Myanmar wording and CEFR source needed for either option. |
| A2 `fine` (adjective), `draft/A2-C1-EDITORIAL-STARTER.json` index 864 | Definition `Good enough or acceptable in quality.` Example `The weather was fine for our picnic.` may convey pleasant weather, not merely acceptable quality. | Candidate tighter example: `This copy is fine for our records.` Independently review naturalness and whether `fine` means satisfactory/acceptable in this context. |
| B1 `critical` (adjective), `draft/A2-C1-EDITORIAL-STARTER.json` index 480 | Current definition/example use `extremely important`; other senses include adverse judgement and dangerous medical condition. | Explicitly label importance sense; do not import other senses' CEFR evidence. Current example `Clean drinking water is critical during an emergency.` is aligned. |
| B2 `conduct` (verb), `draft/A2-C1-EDITORIAL-STARTER.json` index 250 | `carry out` verb differs from behaviour noun `conduct`, including stress and pronunciation differences. | Keep verb POS and source sense explicit for audio scripts and CEFR evidence; `The team will conduct a safety inspection.` matches. |

## Evidence acquisition requirements — none asserted completed here

For each row, an independent reviewer must capture a real publisher/dictionary page identifying the **same part of speech and sense**, its explicit CEFR indication if present, the actual observation date, URL, source-sense wording and evidence reference. Starting points for *future consultation*, not consulted or verified in this audit: https://dictionary.cambridge.org/ and https://www.oxfordlearnersdictionaries.com/. An entry without a publisher-backed sense-specific CEFR level remains held even if its example and Myanmar translation look correct.

Independently check Burmese meanings for sense, register and natural usage, then English definition and example grammar. Record the actual human reviewer's identity and approval separately in `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` or the approved evidence workflow, not in this document. **No reviewer flags or release approvals have been set.**

## Release gate remains closed

A1 200 first-pass / 0 independent; A2 200/0; B1 200/0; B2 200/0; C1 200/0. Final four clips per entry (George/Emma × headword/example), actual listening signoff, browser/mobile regression, physical iPhone Safari evidence, GitHub Pages limits, privacy, 54 existing lessons, separate IELTS bank and established production audio preservation, and confirmed deployment remain unverified. Do not merge or publish.
