# CEFR-1000 — six C1 direct-Oxford exact-sense research leads (3 November 2026)

**Scope:** USER-APPROVED **1,000 TOTAL**, not the superseded 5,000. Staging branch `cefr-5000-bilingual-qa-staging` only. **RELEASE BLOCKED; NO DEPLOYMENT.** Research is AI-assisted editorial triage, **not independent human verification**.

## Source observation and exact-sense issues

On **2026-11-03**, directly opened the following Oxford Advanced Learner's Dictionary headword pages, recording their publisher URLs, source-line ranges and British IPA in the [six-card source-bound research packet](draft/CEFR-1000-C1-SIX-ANTAGONISTIC-COALESCE-DIRECT-OXFORD-2026-11-03.json). No page established an exact-sense **C1** CEFR badge. Topic labels (e.g. Oxford `Personal qualities c2`, `Success c2`) and OPAL lists are **not** headword-specific CEFR evidence.

| Held C1 headword | Direct publisher source | Sense / English–Myanmar–example review risk |
|---|---|---|
| **antagonistic** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/antagonistic), lines 88–107 | Formal adjective `antagonistic to/towards`; opposition need not always be active hostility. Frozen definition may be too narrow. |
| **arbitrariness** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/arbitrariness), lines 88–114 | Uncountable noun; absence of a reason/system and unchecked exercise of power are separate senses. Frozen 'personal choice' oversimplifies. |
| **assiduous** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/assiduous), lines 88–109 | Hard, careful work; frozen 'over a long period' adds a possible unnecessary restriction. Oxford `Personal qualities c2` is a topic tag. |
| **catharsis** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/catharsis), lines 88–120 | Emotional **release process**, not merely a feeling afterward; countable/uncountable, irregular plural `catharses` and British /kəˈθɑːsiːz/. |
| **circumvent** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/circumvent), lines 88–115 | Transitive avoid-rule/difficulty versus literal go-around-obstacle senses. The frozen safety-check example fits the former. Topic `c2` is not an exact-sense CEFR label. |
| **coalesce** | [Oxford](https://www.oxfordlearnersdictionaries.com/definition/english/coalesce), lines 88–113 | Formal **intransitive** verb, especially `coalesce into`. Frozen `coalesce around the proposal` is a figurative collocation needing independent usage review, not an established error. |

Six **unapproved** English definition, fluent Myanmar meaning and original example alternatives are stored separately from the immutable frozen originals. These are proposed teaching leads only; the independent editor must check grammar, register, collocation, pronunciation and source-backed exact-sense CEFR, and may reject any proposal.

## Integrity and CI

Frozen shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`, Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. All six historical originals are at indices **22–27** of `draft/A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH58.json`, Git blob `da7df62123acfac89a0acedad4652ec499c7ed3d`. New research packet Git blob `ba68cf9ec47b79a39a82c4493f48f96f87379da3`.

Added [fail-closed source/provenance/CEFR/reviewer/audio/iPhone auditor](tools/audit_cefr_1000_c1_six_antagonistic_coalesce.py), including synthetic adversarial rejection tests. Added it to the **A1/A2/B1/B2/C1/ALL** parallel structural lanes and documentary no-deploy workflow. **Do not claim CI pass until actual GitHub Actions run conclusions and logs are checked.** Research commit `297b1d91c6363ba8276bf691505e8427a0f312ae`; auditor `9894dd203463f4ff13cae52d266f8b057a9b47bb`; structural workflow `b509847b294aa12b266f3428ca504ee0a57ca347`; documentary workflow `7939154c488ea1901ef521dfec9a2b376f9137dc`.

## Truthful release status

| CEFR | First-pass written | Independently approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |

**All 1,000 on editorial hold.** Exact-sense source-backed independent English/Myanmar/example/CEFR approvals, final approved 200-per-level deduplicated manifest, full George/Emma British headword/example audio with **actual listening** signoffs, browser/mobile regression, real physical iPhone Safari evidence, measured GitHub Pages limits, preservation checks and confirmed production deployment are missing. No approval flags, source corpus, production assets, IELTS 1,000-word bank, 54 lessons, production George/Emma audio, privacy files, main branch, or publication were changed.

## CI follow-up — actual job steps/logs inspected (3 November 2026)

At this checkpoint, [structural run **41486672330**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41486672330) is **IN PROGRESS** at SHA `b509847b294aa12b266f3428ca504ee0a57ca347`. Actual GitHub job conclusions already show **SUCCESS** for A1 job `125418746518`, C1 job `125418746848`, B2 job `125418746915` and ALL job `125418747425`; B1 and A2 jobs have **not** reached a final conclusion. The completed **ALL** job's decoded log explicitly reports **178/178 synthetic Oxford source, CEFR, Myanmar, historical provenance, human, George/Emma, physical iPhone and release forgeries rejected**, and the six-card research audit PASS. This is mechanical source/structure verification only, **not independent human linguistic review**.

[Documentary no-deploy run **41486697252**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41486697252) is also **IN PROGRESS** at SHA `7939154c488ea1901ef521dfec9a2b376f9137dc`; actual documentary job `125418835495` shows the new six-card forged-signoff step and the **Protect production lessons, IELTS vocabulary, George Emma and privacy** step completed **SUCCESS**, but artifact upload/final job conclusion and decoded complete log were not yet available. Do **not** claim whole-workflow success until every job conclusion and log is checked. Recheck and repair any actual failures on the next feasible run.

**A1 200/0; A2 200/0; B1 200/0; B2 200/0; C1 200/0. RELEASE BLOCKED — STAGING ONLY.**

### Documentary gate final verification (3 November 2026)

[Documentary run **41486697252**](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/41486697252) completed **SUCCESS** at SHA `7939154c488ea1901ef521dfec9a2b376f9137dc`. Actual documentary job `125418835495` decoded log confirmed **178/178** synthetic six-card Oxford/source/CEFR/reviewer/audio/iPhone/deployment forgeries rejected and **PASS: protected production assets untouched by staging migration**. The same log explicitly recorded **BLOCK** for 0/1000 independent reviews, missing approved manifest, missing actual George/Emma listening, missing desktop/mobile Chromium/WebKit regression, missing physical iPhone Safari, missing measured GitHub Pages hosting clearance and missing final production release approval. Documentary success means the **no-deploy blocker is working**, not that public launch is allowed. Structural run `41486672330` had A1/C1/B2/ALL jobs SUCCESS, with B1/A2 still IN PROGRESS at the last check; no whole-structural-run conclusion is asserted.
