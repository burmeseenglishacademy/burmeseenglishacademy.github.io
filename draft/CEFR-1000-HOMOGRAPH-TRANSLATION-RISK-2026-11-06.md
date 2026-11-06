# CEFR-1000 homograph and translation-risk review packet — 2026-11-06

**Editorial investigation only. No independent verification, CEFR certification, audio listening or release approval.** Scope is the user-approved 1,000-word provisional inventory, **not** the superseded 5,000-word plan.

## Reproducible provenance

Source: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` at staging commit `438d6c885dcb066a6c9cdc2e7bd69ebd4a950a36`; Git blob SHA `475e68ae17ab97bd937e73e5ce4794e0dcd76551`; inspected 2026-11-06. Preserve each entry's `source_path`, `source_index`, and `source_blob_sha` in subsequent review. This packet is internal linguistic triage, **not external publisher evidence**. Source-backed CEFR evidence for the *exact sense and part of speech* remains to be collected.

## Eight exact entries selected for independent review

| Level | Headword | Recorded POS | Current provisional definition | Original provisional example |
|---|---|---|---|---|
| A1 | minute | noun | A period of sixty seconds. | Wait one minute, please. |
| A2 | project | noun | A planned piece of work with a particular goal. | Our class project is about saving water. |
| B1 | address | noun | Details that identify where someone lives or a place is located. | Please check the delivery address before confirming. |
| B1 | eventually | adverb | In the end, after a period of time or several difficulties. | After several attempts, she eventually solved the problem. |
| B1 | actual | adjective | Real, rather than planned, expected, or imagined. | The actual cost was lower than our estimate. |
| B1 | produce | verb | To make or create something. | The factory can produce hundreds of boxes a day. |
| B2 | conduct | verb | To organise and carry out an activity. | The team will conduct a safety inspection. |
| C1 | permit | noun | An official document giving permission for a particular activity. | The contractor applied for a permit before starting work. |

## Specific risks and human reviewer decisions

1. **A1 minute (noun)** — sixty seconds is the intended sense, not the adjective pronounced /maɪˈnjuːt/ meaning extremely small. Review the British pronunciation prompt against the noun sense. Existing Myanmar `မိနစ်` corresponds to time unit; retain only after independent check.
2. **A2 project (noun)** — planned undertaking, not the verb meaning to estimate/throw forward, with different stress. Ask reviewer to verify noun stress and whether the class project example fits the documented publisher sense.
3. **B1 address (noun)** — postal/location details, not the verb meaning to speak to or deal with a problem. Confirm British noun stress, Myanmar `လိပ်စာ`, and a publisher sense explicitly identifying location details.
4. **B1 eventually (adverb)** — means *in the end after time or difficulty*, not *possibly* or *at some future point without the outcome*. Check that the Myanmar `နောက်ဆုံးတွင်၊ အချိန်ကြာပြီးနောက်` conveys eventual result and that the example's completion is unambiguous.
5. **B1 actual (adjective)** — real/observed as opposed to estimated, not *current* in the temporal sense. Confirm `အမှန်တကယ်ဖြစ်သော` and the cost-estimate contrast; independent reviewer to check natural Myanmar explanation of an actual cost.
6. **B1 produce (verb)** — manufacture/create, not the noun *agricultural produce* (different stress). Ensure British George/Emma headword audio uses verb stress and the example matches manufacturing rather than agriculture.
7. **B2 conduct (verb)** — carry out/organise, not the noun meaning behaviour, with different stress. Confirm verb-stress pronunciation in both voices, and whether `ဆောင်ရွက်သည်၊ ပြုလုပ်သည်` is natural in the inspection context.
8. **C1 permit (noun)** — official permission document, not the verb meaning allow (stress shift). The existing example and Myanmar `တရားဝင်ခွင့်ပြုချက်လက်မှတ်` target the document sense. **High priority**: do not assume C1 for this noun merely because it was selected from a C1 source batch; obtain an explicit publisher CEFR sense citation or hold/relevel after independent review.

## Evidence collection template (one record per sense)

For each entry, record: headword; POS; exact sense/definition; source publisher and exact URL; source page's displayed CEFR level **if present**; observation date; quoted short supporting excerpt (copyright-limited); sense-to-example mapping; British IPA/stress; Myanmar explanation and context register; reviewer identity and independent signoff date. A general dictionary definition without a published CEFR level **does not establish** CEFR level. If multiple publisher sources disagree, record the conflict without silently choosing the desired level. The listed linguistic risks are self-generated hypotheses and **must not** populate independent-reviewed flags.

## Current release and CI facts

Manifest metadata: A1 200, A2 200, B1 200, B2 200, C1 200 first-pass entries; independent approvals A1 0, A2 0, B1 0, B2 0, C1 0. All remain on editorial hold. GitHub Actions run [42171173516](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42171173516) had five completed **successful negative-test jobs** (A1–C1), checked on 2026-11-06; these confirm tested rejection paths only, not editorial correctness or production readiness. Missing: human-independent five-dimension signoffs and exact-sense CEFR sources; generated and genuinely listened-to George/Emma word+example audio; browser/mobile and physical iPhone Safari QA; GitHub Pages constraints review; production deployment and protected-asset verification. **No release authorised by this packet.**
