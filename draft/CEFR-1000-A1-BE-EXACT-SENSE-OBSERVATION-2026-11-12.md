# CEFR-1000 A1 “be” exact-sense audit — 2026-11-12

**Scope:** USER-APPROVED 1,000 total (200 A1, 200 A2, 200 B1, 200 B2, 200 C1), not the retired 5,000-word scope. **Status: research only; no independent review or release approval.**

## Reproducible provenance

- Provisional shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`; observed Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551` (read 2026-11-12).
- Original entry: `word: be`, `level: A1`, `part_of_speech: verb`, definition “To exist or to have a particular quality or identity.”, Myanmar “ဖြစ်သည်၊ ရှိသည်”, example “I want to be a teacher.” Source `draft/A1-EDITORIAL-STARTER.json`, index 2, source blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`.
- Manifest review flags are false; entry is on editorial hold. This audit must not be counted as independent approval.

## Primary dictionary observations (accessed 2026-11-12)

1. Cambridge Learner's Dictionary, https://dictionary.cambridge.org/us/dictionary/learner-english/be — explicitly labels **be verb (DESCRIBE)** A1 (giving identity/qualities), **be verb (POSITION)** A1, and **there is/are** existence construction A1. Its **auxiliary be** for continuous and passive is A2. A broad headword label is not sufficient: grammatical function changes the rated sense.
2. Cambridge English Dictionary, https://dictionary.cambridge.org/us/dictionary/english/be — labels **be verb (DESCRIPTION)** A1 and **be auxiliary verb (CONTINUE/PASSIVE)** A2. It separately lists a formal/literary intransitive **EXIST** sense without an explicit A1 label in the consulted excerpt. Do not transfer the A1 label from the description sense to that literary sense.

## Editorial analysis (NOT independent verification)

The original example “I want to be a teacher.” illustrates a prospective **identity/job** complement, not bare existential “to exist.” The current English definition combines two meanings and its Myanmar translation likewise mixes `ဖြစ်သည်` and `ရှိသည်`. The A1 source-backed identity sense is defensible, but **the entry as written is overbroad**. Proposed narrower learner-facing definition: “Used to say what someone or something is, or what someone becomes.” Suggested Myanmar for this *specific example*: “တစ်စုံတစ်ယောက် သို့မဟုတ် အရာတစ်ခု၏ အမျိုးအစား၊ အလုပ်အကိုင်၊ အခြေအနေကို ဖော်ပြရာတွင် သုံးသည်။” Proposed original illustrative example: “My sister wants to be a nurse.” Myanmar example translation: “ကျွန်တော့်အစ်မက သူနာပြု ဖြစ်ချင်တယ်။” These are draft suggestions requiring native-fluent independent review for naturalness and register.

**Sense decision required:** specify a stable source-linked identifier for Cambridge `be verb (DESCRIPTION)` (not an invented Cambridge ID); if the product needs a separate existential `be` sense, treat it as a distinct candidate requiring its own level evidence, rather than silently bundling it. Also require example-to-sense matching and a part-of-speech/function discriminator: main linking verb vs auxiliary verb.

## Concrete fail-closed regression cases for implementation

- Reject an A1 `be` record that claims the A2 auxiliary-continuous sense on the strength of an A1 main-verb citation.
- Reject an A1 `be` record that cites only the headword URL without an independently verified **exact sense** and level observation.
- Reject a release manifest that carries `reviewed_english`, `reviewed_burmese`, `reviewed_example`, `reviewed_level`, `reviewed_pronunciation`, or `release_approved` without authenticated, independent, attributable signoff and immutable source/sense evidence.
- Reject a release manifest with any level other than exactly 200 deduplicated approved headword+sense identities; passing structural tests on provisional content does not lift the editorial hold.
- Require George and Emma headword+example audio files and separately attributable *actual listening* signoff; a file-exists test alone is insufficient.
- Require evidenced browser/mobile and physical iPhone Safari QA, GitHub Pages hosting checks, and confirmed production verification; never infer these from a passing unit test.

## Remaining blockers

A1–C1 remain at **200 first-pass written / 0 independently approved per level**, per the provisional manifest (not a fresh full recount). All 1,000 remain held. No final audio generation/listening signoff, independent exact-sense review, physical iPhone Safari evidence, or production deployment is claimed. No production files, main branch, IELTS bank, existing 54 lessons or George/Emma production assets changed by this research document.
