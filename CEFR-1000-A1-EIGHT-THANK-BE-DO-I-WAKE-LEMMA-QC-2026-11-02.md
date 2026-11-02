# CEFR 1,000 — A1 eight-card lemma, grammar and exact-sense triage (2026-11-02)

**STAGING ONLY — RELEASE BLOCKED.** Branch: `cefr-5000-bilingual-qa-staging`. This is an AI-prepared research packet and mechanical audit, **not independent human linguistic review**. It does not alter the frozen shortlist, 54 production lessons, separate IELTS 1,000-word bank, George/Emma production audio, privacy controls, `main`, or published site.

## Source and scope

Frozen shortlist: [draft/CEFR-1000-PROVISIONAL-SHORTLIST.json](draft/CEFR-1000-PROVISIONAL-SHORTLIST.json), Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. Original A1 starter: `draft/A1-EDITORIAL-STARTER.json`, blob `ff1e93f60828ef2f94c9146522ce94075183b0ae`. Research: [eight-card bilingual packet](draft/CEFR-1000-A1-EIGHT-THANK-BE-DO-I-WAKE-LEMMA-SENSE-2026-11-02.json), blob `dc2e4ff1f83758e77fe704684781f743eccf7c15`. Auditor: [A1 held-lemma fail-closed audit](tools/audit_cefr_1000_a1_eight_function_lemma_senses.py).

Cambridge Dictionary and Cambridge Grammar Today publisher search-index extracts were observed **2026-11-02**. Direct publisher page requests returned **HTTP 403**. All links below are source locations for independent follow-up, **not proof of direct publisher page inspection or human approval**. CEFR labels are exact-sense and part-of-speech specific; morphological forms do not automatically receive independent headword CEFR labels.

| Frozen A1 word | Publisher research lead / issue | Required independent editorial decision |
| --- | --- | --- |
| **thank** | [Cambridge thank](https://dictionary.cambridge.org/dictionary/english/thank): transitive verb indexed **A2**; [thank you](https://dictionary.cambridge.org/dictionary/learner-english/thank-you) is a separate A1 formula | Resolve A1 versus A2 exact verb sense; do not borrow A1 from *thank you* |
| **is** | [Cambridge be grammar](https://dictionary.cambridge.org/grammar/british-grammar/be-): inflected present form of *be* | Decide whether forms count as independent lexical headwords; *be* is already in A1 |
| **are** | Same [be grammar](https://dictionary.cambridge.org/grammar/british-grammar/be-) source | Same lemma collision; verify person/number and Burmese grammar explanation |
| **do** | [Cambridge do](https://dictionary.cambridge.org/dictionary/learner-english/do): A1 main verb for performing tasks; A1 auxiliary is a separate function | Verify the chosen main-verb sense and Myanmar/example; A1 alignment lead |
| **does** | [Cambridge do grammar](https://dictionary.cambridge.org/grammar/british-grammar/do): present third-person auxiliary form | Do not count a second independent *do* lemma without explicit policy |
| **did** | Same [do grammar](https://dictionary.cambridge.org/grammar/british-grammar/do) source: past auxiliary | Frozen Myanmar mentions questions but omits negative statements; alternative corrects this |
| **i** | [Cambridge I](https://dictionary.cambridge.org/dictionary/essential-british-english/i): A1 subject pronoun, canonically written **I** | Correct displayed case after approval; preserve frozen key and provenance until then |
| **wake** | [Cambridge wake](https://dictionary.cambridge.org/dictionary/essential-british-english/wake): A1 sleep-ending verb | Confirm intransitive sense, natural example, Myanmar and British audio; exclude unrelated noun senses |

## Concrete blocker revealed

The frozen list has 200 **distinct casefolded orthographic strings** in A1, but `is` and `are` are inflections of existing `be`, and `does` and `did` are inflections of existing `do`. Therefore **200 independently deduplicated lexical headwords/senses is not yet established**, even though 200 distinct strings are present. An independent editor must explicitly decide whether to count grammatical forms as separately teachable entries or replace them while retaining the 200-per-level quota. Do not change the frozen selection before that decision. The draft also has an uppercase-display issue for `i`.

## Safeguards and evidence status

The new auditor binds the eight cards to their exact frozen bilingual examples and source indexes, validates 1,000 held entries / 200 per level / 0 approvals, rejects source spoofing and fabricated linguistic, George/Emma, physical iPhone and deployment signoffs, and runs synthetic negative mutations. Both [six-lane structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) and [documentary no-deployment workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml) invoke it. **New run conclusions and logs were not available at documentation time; no new CI success is claimed.** Previous pre-change structural run [41447491218](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41447491218) succeeded in A1/A2/B1/B2/C1/ALL, and documentary run [41447498617](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41447498617) succeeded mechanically. They **do not** validate this new auditor.

**First-pass written / independently approved:** A1 **200 / 0**, A2 **200 / 0**, B1 **200 / 0**, B2 **200 / 0**, C1 **200 / 0**. All 1,000 held. New packet records: **8 researched, 0 independently checked**. George/Emma final headword/example listening signoffs **0**, physical iPhone Safari signoffs **0**, production deployment **false**. No claim is made that audio files are generated or browser/mobile/hosting gates passed.

**Next work:** retrieve post-change GitHub Actions job conclusions/logs and repair any failures; seek genuine independent bilingual and exact-sense review; settle lemma policy; only then produce an approved 200-per-level manifest and complete George/Emma recordings/listening, browser/mobile, physical iPhone, hosting and production-preservation gates. **NO MERGE / NO PUBLICATION.**
