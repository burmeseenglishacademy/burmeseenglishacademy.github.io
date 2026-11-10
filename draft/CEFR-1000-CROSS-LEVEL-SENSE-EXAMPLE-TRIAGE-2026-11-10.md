# CEFR-1000 cross-level sense and example triage — 2026-11-10

**Scope:** 1,000-total approved target, 200 per A1/A2/B1/B2/C1. **Status:** editorial proposals only; no independent review or publisher CEFR verification. **Observed:** 2026-11-10, staging branch `cefr-5000-bilingual-qa-staging`, shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Source records below were read directly from `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`. No external dictionary page was accessed for this dossier; do not treat the proposed CEFR levels as externally supported.

## Priority sense-level corrections (proposals, NOT applied)

| Current level / headword | Source index | Observed issue | Editorial proposal requiring independent reviewer |
|---|---:|---|---|
| A2 **rather** | 473 | English definition “To a noticeable degree, often more than expected”; example “The instructions were rather difficult to follow.” Myanmar “အတော်လေး၊ ထင်ထားသည်ထက်ပို၍” may overstate surprise as inherent. | Retain degree-adverb sense; consider “အတော်လေး” without mandatory surprise, verify example’s register and A2 sense assignment. |
| A2 **either** | 471 | “One or the other of two things or people” is appropriate to determiner/pronoun usage, but `part_of_speech` and the example “either colour” must be checked together to prevent an adverb reading (“not ... either”). | Annotate the determiner sense explicitly; do not generalize to all senses of *either*. |
| B1 **application** | 368 | Definition and example target a formal request, not software or practical use. | Bind CEFR evidence to the formal-request noun sense; Myanmar “လျှောက်လွှာ၊ တရားဝင်လျှောက်ထားမှု” covers document and process, so reviewer should decide whether to split. |
| B1 **primary** | 364 | “Most important or coming first in order” combines importance and sequence; “Safety is our primary concern” proves importance, not chronological first. | Narrow the entry to *main/most important*; verify CEFR for that sense separately from primary school and first-in-order. |
| B2 **theatre** | 384 | Definition “A building where plays are performed” and booked-seats example target the venue, not drama as an art form; British spelling already used. | Keep venue sense and source its CEFR independently; avoid importing evidence for the art-form sense. |
| B2 **plastic** | 389 | Definition and recycled-container example target material noun, not “plastic” adjective or payment card. | Lock material noun sense, confirm countability and Myanmar “ပလတ်စတစ်ပစ္စည်း” naturalness in context. |
| C1 **identical** | 462 | Example “The two documents looked identical, but one had a missing signature” explicitly shows they were *not* identical. This illustrates appearance only and weakens the definition “Exactly the same in every detail.” | Replace with “The two copies are identical, including every page and signature.” Myanmar “လုံးဝတူညီသော” is plausible but needs independent fluency review. |
| C1 **legally** | 463 | “The agreement is not legally binding until both parties sign” depends on jurisdiction and contract terms; signing is not universally a condition for legal enforceability. | Use a less categorical illustration, e.g. “The company is legally required to keep these records.” Independently check the legal sense and CEFR assignment. |
| C1 **permit** | 569 | Current noun definition is an official document and example “applied for a permit”; potential confusion with verb *permit* (allow), with distinct pronunciation and CEFR. | Explicitly mark noun sense and stress pattern; independently verify noun-specific CEFR, British George/Emma pronunciation and Myanmar meaning. |
| C1 **usage** | 498 | Current definition is linguistic usage only, not consumption/amount used. | Keep linguistic sense, require publisher sense-level CEFR evidence; avoid borrowing general “use” level. |

All ten observations originate in `draft/A2-C1-EDITORIAL-STARTER.json`, source blob SHA `b04dd85db5cfae131c25aa4c73109778991b6fdc`. Source indices above are zero-based values recorded in the shortlist. They are provenance pointers, not verified dictionary references.

## Independent reviewer evidence checklist

For each entry, capture (1) publisher URL and retrieval date, (2) exact headword, POS, numbered sense and publisher CEFR label if explicitly shown, (3) English definition quality, (4) fluent Myanmar sense alignment, (5) example grammar and semantic entailment, (6) cross-level collisions including homographs, and (7) separate human identity, timestamp and content-bound attestation. A generic headword-level CEFR label does not establish the chosen sense's level. If publisher CEFR evidence is absent, mark **unsubstantiated** rather than guessing. Publisher resources to check independently: https://dictionary.cambridge.org/ , https://www.oxfordlearnersdictionaries.com/ . These are *research starting points only*, not sources inspected for this dossier.

## Release boundary

Provisional first-pass inventory observed: A1=200, A2=200, B1=200, B2=200, C1=200. Independently approved: A1=0, A2=0, B1=0, B2=0, C1=0 (per shortlist metadata; not an audit of human identities). No reviewed flags changed. No George/Emma audio, listening evidence, physical iPhone evidence, hosting verification or production deployment established by this dossier. Main, 54 lessons, separate IELTS bank, existing production audio and privacy assets untouched. **DO NOT PUBLISH.**
