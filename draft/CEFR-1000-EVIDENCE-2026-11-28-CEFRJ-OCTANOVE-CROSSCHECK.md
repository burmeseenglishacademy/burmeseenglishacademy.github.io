# CEFR-1000 lexical-profile cross-check and exact-sense audit

**Observation date:** 2026-11-28  
**Scope:** CEFR-1000 only; author-side evidence collection and risk triage. This is not independent review, a CEFR decision, or release approval.  
**Branch:** `cefr-5000-bilingual-qa-staging`  
**Shortlist blob SHA:** `475e68ae17ab97bd937e73e5ce4794e0dcd76551`  
**Independent-review task blob SHA:** `77abf35146825f05e3e58cfdd7a73b3c7302c967`

## 1. Reproducible lexical-profile comparison

Compared each shortlist entry against two public lexical-profile datasets by case-normalized exact headword plus part of speech:

1. **CEFR-J Vocabulary Profile 1.5** (7,799 data rows), blob SHA `e89799a7f91a8ae5540e722874edf9158ef8685b`.
2. **Octanove Vocabulary Profile C1/C2 1.0** (2,136 data rows), blob SHA `3a0505e98c9a6ef92be32466e43de4b7f14683d0`.

Source repository and dataset descriptions: https://github.com/openlanguageprofiles/olp-en-cefrj  
CEFR-J 1.5 CSV: https://github.com/openlanguageprofiles/olp-en-cefrj/blob/master/cefrj-vocabulary-profile-1.5.csv  
Octanove C1/C2 1.0 CSV: https://github.com/openlanguageprofiles/olp-en-cefrj/blob/master/octanove-vocabulary-profile-c1c2-1.0.csv  
Official CEFR-J resource page: https://cefr-j.org/download_eng

The comparison classifies an entry as:
- **same-level hit**: at least one exact headword/POS row matches its provisional level;
- **other-level-only**: one or more rows exist, but none matches the provisional level;
- **no profile match**: no exact headword/POS row appears in either dataset.

| Provisional level | Written | Same-level hit | Other-level-only | No profile match |
|---|---:|---:|---:|---:|
| A1 | 200 | 171 | 6 | 23 |
| A2 | 200 | 74 | 112 | 14 |
| B1 | 200 | 63 | 134 | 3 |
| B2 | 200 | 53 | 139 | 8 |
| C1 | 200 | 18 | 88 | 94 |
| **Total** | **1,000** | **379** | **479** | **142** |

**Interpretation limit:** These are lexical-profile cross-checks, not exact-sense adjudications. The CEFR-J Wordlist is corpus-derived and assigns levels by headword/POS; its own documentation notes that different parts of speech may receive different levels and that the list can contain errors. A match or mismatch is a review lead, not a reason to change a shortlist level automatically. The CEFR-J project now lists Wordlist 1.6 as its latest version (updated 2020-03-24); this run used the 1.5 CSV mirrored in Open Language Profiles, so repeat against 1.6 before final CEFR classification.

## 2. High-priority C1 level conflicts

The following are direct headword/POS matches to a different level in the cited profiles. Keep each entry on editorial hold until an independent reviewer checks the exact sense and the relevant current profile/dictionary source.

| Shortlist C1 entry | External profile result | Source row | Triage |
|---|---|---:|---|
| benevolent (adjective) | B2 in CEFR-J 1.5 | 645 | Strong level-conflict flag; Cambridge meaning supports the shortlist sense “kind and helpful”, but does not establish C1 |
| legitimate (adjective) | B2 in CEFR-J 1.5 | 3871 | Strong level-conflict flag |
| regulatory (adjective) | C2 in Octanove 1.0 | 1319 | C1/C2 boundary risk |
| integration (noun) | C2 in Octanove 1.0 | 1418 | C1/C2 boundary risk |
| belligerent (adjective) | C2 in Octanove 1.0 | 1135 | C1/C2 boundary risk |
| brevity (noun) | C2 in Octanove 1.0 | 1440 | C1/C2 boundary risk |
| disseminate (verb) | C2 in Octanove 1.0 | 1584 | C1/C2 boundary risk |
| ephemeral (adjective) | C2 in Octanove 1.0 | 1684 | C1/C2 boundary risk |
| fallacy (noun) | C2 in Octanove 1.0 | 1674 | C1/C2 boundary risk |
| incongruous (adjective) | C2 in Octanove 1.0 | 2103 | C1/C2 boundary risk |
| meticulous (adjective) | C2 in Octanove 1.0 | 1820 | C1/C2 boundary risk |
| stringent (adjective) | C2 in Octanove 1.0 | 1933 | C1/C2 boundary risk |
| tenacious (adjective) | C2 in Octanove 1.0 | 1225 | C1/C2 boundary risk |
| vindicate (verb) | C2 in Octanove 1.0 | 1168 | C1/C2 boundary risk |
| conjecture (noun) | C2 in Octanove 1.0 | 1281 | C1/C2 boundary risk |
| disparage (verb) | C2 in Octanove 1.0 | 1738 | C1/C2 boundary risk |
| irrevocable (adjective) | C2 in Octanove 1.0 | 1509 | C1/C2 boundary risk |
| superfluous (adjective) | C2 in Octanove 1.0 | 1680 | C1/C2 boundary risk |

A further direct Cambridge conflict: the Cambridge Advanced Learner’s Dictionary labels **pragmatic (adjective) C2**, while the shortlist places it at C1. Source: https://dictionary.cambridge.org/dictionary/english/pragmatic. The entry’s sense is practical problem-solving that fits real conditions rather than following fixed theories or rules. This is an explicit level conflict and should not be hidden by a general definition match.

Only 18 of the 200 C1 shortlist headword/POS pairs had a C1 row in these two datasets; 88 had profile data only at other levels and 94 had no match. This does **not** prove that the 182 remaining items are wrongly assigned; it shows that C1 needs much stronger source-backed review than a generic word-list lookup.

## 3. Cross-level triage examples

- **need (A1 verb):** Cambridge Learner’s Dictionary labels the transitive necessity sense A1 and distinguishes other constructions/senses at higher levels. Source: https://dictionary.cambridge.org/us/dictionary/learner-english/need. CEFR-J 1.5 lists the verb at A2 (row 4447). This is a real source conflict to resolve at exact-sense level, not an automatic reallocation.
- **support (A2 verb):** CEFR-J 1.5 lists the verb at B1 (row 6712).
- **imagine (B1 verb):** CEFR-J 1.5 lists the verb at A1 (row 3382).
- **multiple (B1 adjective):** CEFR-J 1.5 lists the adjective at B2 (row 4369).
- **benefit (B1 verb):** CEFR-J 1.5 lists the verb at B2 (row 643).
- **prepare (B2 verb):** CEFR-J 1.5 lists the verb at A2 (row 5215).
- **operate (B2 verb):** CEFR-J 1.5 lists the verb at A2 (row 4662).

The same headword may have different senses, collocations, or frequency profiles across sources. Each conflict therefore needs dictionary guideword/sense evidence and an example that selects that sense.

## 4. Cambridge exact-sense and example audit: selected C1 entries

| Entry | Source-backed sense check | Example and editorial finding |
|---|---|---|
| ambivalence | Cambridge Advanced Learner’s Dictionary: two opposing feelings at the same time, or uncertainty about one’s feelings. https://dictionary.cambridge.org/dictionary/english/ambivalence | “She felt ambivalence about accepting the promotion abroad.” is grammatical and natural; `ambivalence about` is well selected. The English definition should say **feelings**, not merely attitudes. Current Myanmar already uses `ခံစားချက်`, which is aligned with this distinction. |
| benevolent | Cambridge: kind and helpful; also giving money or help to people/organisations in need. https://dictionary.cambridge.org/dictionary/english/benevolent | “A benevolent donor paid for the village library.” selects the charitable/helping sense and is natural. The B2 profile result is a level flag, not a meaning error. |
| corroborate | Cambridge: add proof to an account, statement or idea using new information. https://dictionary.cambridge.org/dictionary/english/corroborate | “The photographs helped corroborate the witness’s account.” is grammatical; `corroborate an account` is a natural collocation. Myanmar proposal for review: `သက်သေအထောက်အထားများ ထပ်မံဖြည့်စွက်၍ ထွက်ဆိုချက်တစ်ခု မှန်ကန်ကြောင်း အတည်ပြုသည်။` |
| juxtapose | Cambridge: put things that are not similar next to each other. https://dictionary.cambridge.org/dictionary/english/juxtapose | “Curators juxtapose old photographs with recent ones to show how the town has changed.” is grammatical and clearly selects the comparison-by-placement sense. `juxtapose A with B` is the useful pattern. |
| meticulous | Cambridge: giving or showing careful attention to every detail. https://dictionary.cambridge.org/us/dictionary/learner-english/meticulous | “Her meticulous records helped the auditors trace every payment.” is grammatical and natural. Exact sense fits; Octanove assigns the headword/POS to C2, so C1 remains disputed. |
| mitigate | Collins: make or become milder, less severe, less rigorous or less painful. https://www.collinsdictionary.com/dictionary/english/mitigate | “Planting trees can help mitigate extreme summer heat.” is understandable and selects the less-severe-effects sense. Review whether `mitigate the effects of extreme summer heat` is a more precise collocation for the intended claim. |
| pragmatic | Cambridge explicitly labels the adjective C2 and defines the real-conditions/practical-solutions sense. https://dictionary.cambridge.org/dictionary/english/pragmatic | “They took a pragmatic approach to the budget shortage.” is grammatical and natural. The example fits, but the C1 label conflicts with Cambridge’s explicit C2 tag. |
| stringent | Cambridge: very severe or extremely limiting; laws, tests and rules must be obeyed. https://dictionary.cambridge.org/dictionary/english/stringent | “The laboratory follows stringent hygiene rules.” is natural and selects the rules/requirements sense. Octanove lists this adjective at C2. |
| obfuscate | Cambridge: make something less clear and harder to understand, especially intentionally. https://dictionary.cambridge.org/us/dictionary/english/obfuscate | “Technical jargon can obfuscate the real reasons for a delay.” is grammatical and natural. The definition and example select the intended clarity-obscuring sense, not the separate computing or online-tracking senses. |
| vindicate | Cambridge: prove that someone’s statement/action was right or true after others thought it wrong; also prove someone is not guilty. https://dictionary.cambridge.org/dictionary/english/vindicate | Current example “The successful trial helped vindicate the engineer’s design.” is understandable but less direct. Better example proposal: “The test results vindicated the engineer’s decision to use the new material.” Octanove lists the verb at C2. |
| acquiescence | Cambridge: accepting or agreeing to something, often unwillingly. https://dictionary.cambridge.org/dictionary/english/acquiescence | “Her silence was mistaken for acquiescence to the new policy.” is grammatical and naturally shows inferred, possibly reluctant acceptance. |
| ameliorate | Cambridge: make a bad or unpleasant situation better. https://dictionary.cambridge.org/dictionary/english/ameliorate | “The new drainage system should ameliorate flooding in the village.” is understandable, but `ameliorate the effects of flooding` is the more precise proposal because the system improves the consequences/conditions rather than making the event itself “better”. |
| equanimity | Cambridge Academic Content Dictionary: a calm mental state, especially after shock, disappointment or in a difficult situation. https://dictionary.cambridge.org/dictionary/english/equanimity | “She handled the unexpected criticism with remarkable equanimity.” is natural. Current English definition adds “self-control”; consider narrowing it to calmness of mind. Myanmar proposal for review: `ခက်ခဲသော အခြေအနေများတွင် စိတ်တည်ငြိမ်အေးချမ်းနေခြင်း။` |
| salience | Cambridge: the fact of being important to or connected with what is happening or being discussed. https://dictionary.cambridge.org/dictionary/english/salience | “The salience of safety concerns increased after the accident.” is grammatical and fits formal/academic use. Myanmar proposal for review: `အခြေအနေတစ်ခုတွင် အထူးအရေးပါပြီး သက်ဆိုင်နေမှု။` This is more precise than treating salience as visibility alone. |

**Profile coverage note:** `ambivalence`, `corroborate`, `juxtapose`, `mitigate`, `acquiescence`, `ameliorate`, `equanimity`, `obfuscate` and `salience` did not produce an exact headword/POS row in either profile dataset used in this run. Their exact meanings are supported by the dictionary sources above, but their C1 level is still unverified by these sources.

## 5. Dataset provenance and limitations

- CEFR-J official resource page states that Wordlist 1.6 is based on English textbook corpora, supplemented by comparison with the English Vocabulary Profile; it includes POS and level labels and carries a warning that the list may be incomplete or contain errors. It permits research/commercial use with proper acknowledgement. The 1.5 mirror used here is older than the official 1.6 release.
- Open Language Profiles describes its CEFR-J 1.5 dataset as supplied by the CEFR-J project and its Octanove C1/C2 1.0 dataset as created by Octanove Labs. Its README records the dataset references and licensing: CEFR-J data requires attribution; Octanove C1/C2 1.0 is CC BY-SA 4.0.
- Dictionary definitions establish meanings and sometimes an explicit CEFR tag; they do not establish the Academy’s final teaching-level decision by themselves.
- The cross-check is author-side, not independent. No reviewer identity, independent decision, or approval is inferred from this research.

## 6. Integrity and release status at observation

- Shortlist: exactly 1,000 entries; 200 at each level; no normalized duplicate headwords across levels; all first-pass English definitions, Myanmar meanings and examples are populated.
- The shortlist’s `source_english`, `source_burmese` and `source_level` fields remain empty for all 1,000 entries; this cross-check does not silently populate them.
- Review tasks: exactly 1,000; all 1,000 remain `PENDING_INDEPENDENT_REVIEW`; 0 assigned reviewers, 0 tasks with source URLs, 0 approvals.
- No shortlist or task fields were changed. All entries remain on editorial hold. No production assets or main-branch files were changed.
- These notes do not count as independent English, Myanmar, example, CEFR, pronunciation or listening signoff.
