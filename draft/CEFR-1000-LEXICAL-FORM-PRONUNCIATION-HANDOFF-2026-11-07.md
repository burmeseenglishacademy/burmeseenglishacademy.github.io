# CEFR-1000 lexical-form and pronunciation ambiguity handoff — 2026-11-07

**Status:** editorial research only; not independent review or CEFR verification. **Scope:** approved 1,000-total project, NOT 5,000. **Inventory blob SHA:** `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Observation date: 2026-11-07 (inventory inspection). All proposed changes require independent English, Myanmar, example, exact-sense CEFR and British pronunciation verification before approval.

## Four entries requiring form-aware review

| Entry | Existing first-pass definition and example | Concrete review issue | Proposed reviewer task |
| --- | --- | --- | --- |
| A1 **read** (verb; source index 30, `draft/A1-EDITORIAL-STARTER.json`) | “To look at written words and understand them.” / “I read a book every night.” / Myanmar: “ဖတ်သည်” | The written form **read** is ambiguous between present /riːd/ and past /red/. “Every night” favours habitual present, but a grapheme-only audio pipeline can select the wrong pronunciation. | Specify tense in the speech manifest; independently listen to George and Emma headword AND example. Test explicit past-tense variant separately if later introduced. Do not use the spelling alone to decide phonemes. |
| B1 **produce** (verb; source index 889) | “To make or create something.” / “The factory can produce hundreds of boxes a day.” / Myanmar: “ထုတ်လုပ်သည်၊ ဖန်တီးသည်” | The noun **produce** (agricultural goods) differs in stress and meaning from the verb. A bare-headword audio request can use noun stress even though the example uses the verb. | Bind part of speech and intended sense to British headword audio, review verb stress and factory-production sense; check whether both Myanmar glosses fit the same example. |
| B1 **address** (noun; source index 98) | “Details that identify where someone lives or a place is located.” / “Please check the delivery address before confirming.” / Myanmar: “လိပ်စာ” | **Address** has noun/verb readings and variable stress; the delivery example unambiguously uses the location noun. | Require noun-specific British pronunciation, verify example translation and source-backed CEFR for this *sense*, not an unrelated verb meaning “deal with”. |
| A2 **actually** (adverb; source index 287) | “Used to say what is true, especially when it differs from what someone expected.” / “I thought it was Tuesday, but it is actually Wednesday.” / Myanmar: “တကယ်တော့၊ အမှန်တကယ်” | Discourse-correction usage differs from intensifying or generic “in reality” uses. A broad bilingual gloss may conceal that distinction. | Independently verify the corrective discourse sense, natural Myanmar sentence-level rendering, and publisher CEFR label for that exact usage. |

## Source and provenance discipline

The entries above were read directly from the provisional shortlist on 2026-11-07; their original `source_path`, `source_index` and `source_blob_sha` remain authoritative in the JSON. Publisher research targets (not independently inspected or established as CEFR evidence in this handoff):

- Cambridge dictionary, read: https://dictionary.cambridge.org/dictionary/english/read
- Cambridge dictionary, produce: https://dictionary.cambridge.org/dictionary/english/produce
- Cambridge dictionary, address: https://dictionary.cambridge.org/dictionary/english/address
- Cambridge dictionary, actually: https://dictionary.cambridge.org/dictionary/english/actually

A reviewer must record publisher, page URL, exact sense, part of speech, observed CEFR annotation (or explicit absence), access date, and the reviewer identity/date. A general dictionary entry URL alone is **not** a CEFR attestation.

## Release safeguard

A future audio manifest should store `entry_id`, level, headword, part of speech, exact sense, example, British voice (George/Emma), headword/example file paths and hashes, generation provenance, and **separate human listening attestations** for each asset. Any missing or mismatched field must fail closed. For the four entries here, a plain-word lookup is insufficient for headword pronunciation. This is a proposed specification, **not an implemented or passed test**.

## Current release status

A1/A2/B1/B2/C1 each contain 200 first-pass entries; independently checked: 0/0/0/0/0; approved: 0/0/0/0/0. All 1,000 remain on editorial hold. Source-backed independent linguistic review, George/Emma final audio plus real listening, browser/mobile regression, physical iPhone Safari QA, GitHub Pages clearance, production verification and preservation of the 54 lessons and separate IELTS bank remain blocked/unverified. **No deployment permitted.**
