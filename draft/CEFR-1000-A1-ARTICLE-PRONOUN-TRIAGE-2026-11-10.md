# CEFR-1000 staging: provenance and exact-sense editorial blockers (2026-11-10)

Status: **editorial research only; zero independent approvals**. Scope is the approved 1,000-total project (200 each A1–C1), not the abandoned 5,000-word proposal. Observed directly from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` on the staging branch on 2026-11-10; shortlist blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. No external publisher CEFR evidence was obtained for the following entries in this pass.

## Directly observed candidate issues

| Entry | Level | Source index | Observed content | Editorial action required |
| --- | --- | --- | --- | --- |
| `a` (article) | A1 | 0 | “Used before one person or thing when it is not specified.”; example “I have a book.” | Sense description omits the sound-conditioned distribution of the indefinite article; compare `an` as a distinct surface form vs one lexical article lemma. Independently determine counting policy before approval. |
| `an` (article) | A1 | 1 | “Used before one person or thing when the next word starts with a vowel sound.”; example “She has an apple.” | Definition omits indefinite/non-specific meaning; establish how `a/an` are counted and whether separate headwords are justified under the exactly-200 constraint. |
| `i` (pronoun) | A1 | 3 | Lowercase headword `i`; example “I am a student.” | Standard English first-person singular pronoun is capitalized `I`. Propose display headword `I`, preserve case-folded duplicate detection, and require independent English signoff. |
| `it` (pronoun) | A1 | 11 | “A thing or animal already mentioned.”; example “It is a small cat.” | Example introduces a cat rather than unambiguously referring back to one. Propose “I saw a small cat. It was sleeping.”, subject to independent example/grammar review. |

Source paths for these four entries are `draft/A1-EDITORIAL-STARTER.json` and their recorded source blob SHA is `ff1e93f60828ef2f94c9146522ce94075183b0ae`. Source indices above are indices in that original starter, not independently verified dictionary sense IDs. No source-backed CEFR classification is asserted.

## Release-verifier integration risk

The current release verifier binds the pronunciation review hash to the `word` field but not to a normalized spoken form, IPA, voice, or audio asset; separately, listening attestations are structurally checked without binding their `content_sha256` to the audio file bytes. This allows an unchanged-looking signoff record to be copied to another audio item unless independently detected. Require content-addressed listening attestations bound to `entry ID + voice + kind + file SHA-256`, and external verification of the listener's identity and actual listening. A matching digest is *not* evidence that listening occurred.

The verifier also permits `http://` evidence URLs, checks their string form rather than fetching/verifying publisher content, and does not authenticate reviewer identity. These are blockers to trusting a schema-pass as release authorization. Never connect this validator alone to production publication.

## Independent-review checklist

For each entry, independently verify the exact part of speech and sense against a dated authoritative dictionary/CEFR publisher page; record exact source URL, observed date, relevant sense identifier, and reviewer identity outside self-generated evidence. Review Myanmar naturalness and the original example's grammar and sense alignment. Keep all review and release flags false until independent human signoff. Do not generate or claim audio listening, physical iPhone testing, or production deployment from this dossier.

## Inventory and gating

A1/A2/B1/B2/C1 each have 200 provisional first-pass records and **0 independently approved**, as recorded in the shortlist. The entire 1,000 remains on editorial hold. British George/Emma headword/example recordings and real listening signoff, browser/mobile and physical iPhone Safari QA, GitHub Pages hosting verification, production asset preservation and confirmed deployment remain unverified. Production main, 54 lessons, IELTS bank, established production voices, and privacy controls must remain unchanged.
