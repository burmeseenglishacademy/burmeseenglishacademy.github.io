# CEFR-1000: independent evidence capture and adjudication protocol (staging only)

Observed 2026-11-11. Scope is **exactly 1,000 provisional senses**, A1/A2/B1/B2/C1 **200 each**, not the retired 5,000-word plan. Source of record: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` (blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`); separate reviewer worklist: `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` (blob `88f472e4c79e5e9b6ae5957f5244f9cb60dc0ef2`). The source metadata says **zero independently approved per level**. This protocol is not a review or approval.

## Mandatory per-entry reviewer evidence (never infer from a headword alone)

1. Immutable source identity: shortlist blob SHA, source path/index/blob SHA, headword (Unicode-normalized and case-sensitive display), part of speech, **explicit sense gloss**, intended level, example, Myanmar meaning and content-author identity.
2. **English reviewer**: independent named human reviewer, review date, corrected sense-specific definition, word class and usage/register, original example grammar/collocation/idiomaticity, exact correction or explicit acceptance, and reviewer attestation.
3. **Myanmar reviewer**: independent fluent human reviewer, date, natural contextual translation (not just literal dictionary equivalence), script/orthography, semantic equivalence to the *same* sense and example, correction or explicit acceptance, and attestation.
4. **CEFR evidence**: named publisher or authoritative learner resource, stable HTTPS URL, page title, observed date (ISO YYYY-MM-DD), headword, POS, **exact sense or clearly identified sense group**, displayed CEFR marker and whether marker applies to the intended sense or only a topic/entry. Store brief observation in own words, no large quotations. If sense-level attribution is unavailable, record **unsubstantiated**, not approved.
5. **Conflict resolution**: identify other levels containing same normalized headword/POS/sense; distinguish polysemy from accidental duplicates; document publisher disagreements and adjudicator decision. Named entities, historical WordNet-derived material and unsupported level assignments require explicit hold rationale.
6. **Audio evidence**: final text hash and artifact checksum for each George/Emma × headword/example (four per entry = **4,000 total**), generation provenance, British voice identity, and a **separate real listener** with timestamp, artifact identifier, verdict on pronunciation, clipping, pauses and exact-text match. Merely generating, hashing, or automated checking does not count as listening.
7. **Release evidence**: per-level structural CI job ID/conclusion and raw log availability; browser/mobile regression report; physical iPhone Safari device/model/iOS/browser, tester/date and reproducible screenshots or signed observations; GitHub Pages file-size/bandwidth/hosting assessment; preserved 54 lessons, separate IELTS bank, established production George/Emma audio and privacy; confirmed deployed production commit and live smoke test.

## Fail-closed adjudication

An entry remains on editorial hold if **any** of English, Myanmar, original example, exact-sense CEFR, reviewer independence, cross-level uniqueness or audio/listening evidence is absent, ambiguous, self-attested or contradicted. A publisher's topic label is **not** automatically a CEFR level for a particular sense. A reviewer cannot approve their own authored content. Different senses under one headword require explicit sense IDs and defensible levels. Do not convert a lexical first pass into an independently checked count.

The release gate must reject if level totals are not exactly 200, any cross-level normalized headword/POS/sense duplicates exist, any required review evidence is absent, any of 4,000 final audio files or independent listening records is absent, physical iPhone evidence is absent, or production asset preservation cannot be proven. CI success proves only the checks it actually ran.

## Prioritized independent adjudication queue

- **C1 anachronism**: separate object-out-of-period from chronological error; verify sense-specific publisher level, including prior observed Oxford C2 topic classification.
- **C1 integrity**: moral honesty versus structural wholeness; do not transfer a level from the wrong sense.
- **B2 portion**: part/share versus serving of food; check both English example and natural Myanmar equivalents.
- **A2 maybe**: possibility adverb versus tentative suggestion; check example pragmatics and publisher disagreements.
- **B1 doubt**: ensure natural example collocation and correct noun/verb sense.
- **B2 historic, clinical, sample, introduction** and **C1 copyright, functional, divine, sacred**: explicitly distinguish technical, everyday and figurative senses before assigning level.

These are review *tasks*, not independently checked entries. Earlier staging editorial triage and publisher reconciliation reports should be linked in each future evidence record rather than treated as signoff.

## Current gate inventory

| Level | First-pass written | Independently checked | Release status |
|---|---:|---:|---|
| A1 | 200 | 0 | HOLD |
| A2 | 200 | 0 | HOLD |
| B1 | 200 | 0 | HOLD |
| B2 | 200 | 0 | HOLD |
| C1 | 200 | 0 | HOLD |

Audio: no final 4,000-file generation or genuine listening signoff established. Physical iPhone Safari: not established. Production deployment: **not authorized until every gate passes**. Existing historical CI success must not be presented as validation of this new documentation commit. No changes to main or production are authorized by this protocol.
