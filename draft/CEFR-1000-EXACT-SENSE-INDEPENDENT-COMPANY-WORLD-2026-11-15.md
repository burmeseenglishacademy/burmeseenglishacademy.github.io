# CEFR-1000 exact-sense research: independent, company, world

Observed: 2026-11-15 (Singapore). Status: **research only; editorial hold remains; no independent review or approval**.

Scope: user-approved 1,000 total (A1/A2/B1/B2/C1 = 200 each). Provisional shortlist blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Source entries below originate from `draft/A2-C1-EDITORIAL-STARTER.json` blob `b04dd85db5cfae131c25aa4c73109778991b6fdc`. Source pages are external lexical evidence, **not independent signoff**.

## B1 independent — urgent exact-sense/level mismatch
- Source index 11; adjective; first-pass English: “Not controlled by another person or organisation.” Myanmar: “အမှီအခိုကင်းသော၊ လွတ်လပ်သော”; example: “The team made an independent decision.”
- Cambridge labels **NOT INFLUENCED / not controlled** sense **B2**, while **NOT HELPED / not relying on help or money** sense is **B1**. https://dictionary.cambridge.org/us/dictionary/english/independent (observed 2026-11-15).
- **Conflict:** first-pass definition and team decision example fit the B2 sense, despite B1 slot. This is a substantive sense-level mismatch, not merely spelling or duplicate-headword risk. Do not silently relabel without preserving exactly 200 per level and cross-level sense deduplication.
- B1 sense candidate for editorial consideration only: “Able to manage without depending on other people for help or money.” Myanmar candidate: “အခြားသူများ၏ အကူအညီ သို့မဟုတ် ငွေကြေးထောက်ပံ့မှုကို မမှီခိုဘဲ ကိုယ့်အားကိုယ်ကိုးနိုင်သော”. Original example candidate: “After getting a job, she became financially independent.” This requires a human independent check of the English sense, natural Myanmar, example and CEFR match. Alternatively move the original sense to B2 and find a genuinely supported B1 replacement; neither change is approved here.
- Distinguish political independence, an independent business, and independent clauses before any approval.

## A2 company — source-supported business sense, polysemy hazard
- Source index 160; noun; first-pass business definition: “A business that sells goods or services.” Myanmar: “ကုမ္ပဏီ၊ လုပ်ငန်း”; example: “She works for a small company.”
- Cambridge Learner's Dictionary explicitly marks the **BUSINESS** noun sense **A2**; the **PEOPLE/companionship** sense **B2**. https://dictionary.cambridge.org/us/dictionary/learner-english/company (observed 2026-11-15).
- Proposed sense tag: `company|noun|business-organisation`. Example is grammatical and consistent with this sense on preliminary editorial inspection, **not independently checked**. Do not treat other senses as A2 automatically. Myanmar meaning should be independently checked for the precise business entity sense.

## A2 world — level evidence remains unresolved
- Source index 7; noun; first-pass English: “The Earth and all the people and places on it.” Myanmar: “ကမ္ဘာကြီး”; example: “People around the world speak different languages.”
- Cambridge general dictionary supports the Earth/people definition but the consulted excerpt does **not establish a CEFR label** for that exact sense. https://dictionary.cambridge.org/dictionary/english/world (observed 2026-11-15).
- Some third-party vocabulary sites assign A1 (e.g. https://lexupapp.com/words/world/ observed 2026-11-15), but this is not sufficient to settle the A2 allocation; provenance/CEFR methodology not independently established. Do **not** promote third-party or unlabeled definitions into authoritative exact-sense CEFR evidence.
- Escalate to a CEFR-labeled learner dictionary or documented curriculum mapping; verify whether A2 is justified or an A1 displacement is necessary.

## Release-control implications
- All three entries remain provisional, editorial_hold=true, independently approved=false. This document is **self-authored research**, not an independent English, Myanmar, example or CEFR review.
- Never populate `source_english`, `source_burmese`, `source_level` or review flags merely from this document without the prescribed provenance and independent-review process.
- On any eventual replacement/releveling, audit the 1,000-entry manifest for exactly 200 distinct canonical headword/sense pairs per level, semantic collisions across levels, and source-index integrity.
- The broader blockers remain: independent bilingual and exact-sense CEFR signoff, 4,000 final George/Emma headword/example audio assets plus real listening signoff, browser/mobile regression, physical iPhone Safari evidence, current-commit five-job CI, GitHub Pages hosting verification and confirmed production deployment. Production 54 lessons, separate IELTS bank, existing George/Emma audio and privacy must remain untouched.
