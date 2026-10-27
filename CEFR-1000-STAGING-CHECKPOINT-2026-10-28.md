# CEFR 1,000 — 2026-10-28 staging source and release-safeguard checkpoint

**Release decision: BLOCKED; staging only.** Scope is the user-approved **1,000 total** CEFR A1–C1 bilingual entries, **not 5,000**. Work remains exclusively on `cefr-5000-bilingual-qa-staging`. No merge, main modification, production deployment or final human signoff is claimed.

## Exact content, independent verification and audio counts

| Level | First-pass English + Myanmar + example written | Independently reviewed/approved | New 2026-10-28 publisher-indexed sense leads | Final George/Emma real listening receipts |
| --- | ---: | ---: | ---: | ---: |
| A1 | 200 | 0 | 0 | 0 |
| A2 | 200 | 0 | 0 | 0 |
| B1 | 200 | 0 | 0 | 0 |
| B2 | 200 | 0 | 0 | 0 |
| C1 | 200 | 0 | 10 | 0 |
| **Total** | **1,000** | **0** | **10** | **0** |

The shortlist `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` remains pinned at Git blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. **All 1,000 remain on editorial hold**. The 10 source observations are not new curriculum entries, not independently checked words, and not an approved rewrite. Separate IELTS 1,000 vocabulary entries are not counted in this quota.

## Ten new Cambridge publisher sense-level leads, observed 2026-10-28

Source packet: [CEFR-1000-CAMBRIDGE-C1-TEN-SENSE-LEADS-2026-10-28.json](draft/CEFR-1000-CAMBRIDGE-C1-TEN-SENSE-LEADS-2026-10-28.json), committed as `d61aec2c8404619c5babc349a0a051c33f240923`.

**Three same-sense CEFR discrepancies requiring independent resolution:**
- **tribute (C1 draft):** [Cambridge respectful action/statement noun sense](https://dictionary.cambridge.org/us/dictionary/english/tribute) carries **C2**; the draft concert for a late musician uses this respect sense. Human editor must find credible independent exact-sense C1 support or independently replace/retier.
- **popularity (C1 draft):** [Cambridge being widely liked noun sense](https://dictionary.cambridge.org/dictionary/english/popularity) carries **B2**; the draft `grew in popularity` is the ordinary B2 sense.
- **controversial (C1 draft):** [Cambridge causing disagreement adjective sense](https://dictionary.cambridge.org/dictionary/english/controversial) carries **B2**; the draft proposal example does not demonstrate a different C1 sense.

**One definition/example sense-alignment risk:**
- **asset (C1):** [Cambridge](https://dictionary.cambridge.org/dictionary/english/asset) separates a useful person/quality from financial/property assets, both **C1**. The draft definition blends the senses while the example calls reliable staff an asset. Require independently reviewed narrower definition and natural Myanmar gloss before retaining.

**Six publisher-level C1-supporting leads, still without independent signoff:**
- [exclusively](https://dictionary.cambridge.org/dictionary/english/exclusively) (adverb only): clarify Myanmar nuance between `solely` and `private`.
- [sacred](https://dictionary.cambridge.org/dictionary/english/sacred) (holy/religious adjective): avoid mixing with the figurative C2 importance sense.
- [neutral](https://dictionary.cambridge.org/us/dictionary/english/neutral) (not taking sides): mediator example aligns, but Myanmar/exact context needs human review.
- [noble](https://dictionary.cambridge.org/dictionary/english/noble) (morally admirable): distinguish moral quality from social rank in Myanmar.
- [burden](https://dictionary.cambridge.org/dictionary/english/burden) (difficult responsibility): financial-cost example is figurative C1, not literal carried weight.
- [dominant](https://dictionary.cambridge.org/dictionary/english/dominant) (stronger or more important): company-market example is general C1, not specialist genetics.

**Provenance limitation:** these are publisher-owned **search-indexed** Cambridge page excerpts observed on **2026-10-28**. Attempts to open the full Cambridge pages returned **HTTP 403**. They are not direct full-page checks, publisher endorsement, or independent English/Myanmar/grammar/CEFR review. Source URLs, dates, exact provisional English/Myanmar/example snapshots, source labels, access limitation and reviewer tasks are retained in the packet. No dictionary definition was copied into learner content.

## Fail-closed staging safeguards added

- [New source-integrity auditor](tools/audit_cefr_1000_cambridge_c1_ten.py), commit `f9f3f54c869b61e66b19a3ee60ec9f9f71fda8cf`: binds all ten leads to the unchanged 1,000-row shortlist blob, validates source URL/date/label/part of speech and original bilingual/example snapshots, insists on editorial hold and zero approvals, and defines eight tamper/fake-signoff negative tests.
- [Six-job structural matrix workflow](.github/workflows/cefr-1000-selection-structural-qa.yml), commit `f2d17710b6a4c523991b9c4017f66e71292e014b`: new audit runs for A1, A2, B1, B2, C1 and ALL, with ALL negative tests and per-job artifacts.
- [Launch-readiness auditor](tools/audit_cefr_1000_launch_readiness.py), commit `aa9e18746ac6e8dfd532059f3cd8de1c2ff659f9`: for every retained flagged sense, requires a separate genuine human independent direct-publisher C1 exact-sense receipt with reviewed-content hash, source-scope rationale and conflict resolution; unchanged mixed-sense `asset` definition cannot be signed off. **This is a documentary gate, not proof that an identity or observation is genuine.**
- [Release evidence ledger](draft/CEFR-1000-RELEASE-EVIDENCE.json), commit `7ab314db5ab9b1dd3935a058f55ce54204efdf50`: new receipt array is empty, not fabricated.
- [Documentary no-deploy workflow](.github/workflows/cefr-1000-go-live-qc-gate.yml), commit `3ee09dbc442fe2f919e9bab928dc3f86ad3f9bd0`: includes new negative tests and staging-only release blockers.

**Actual execution verification:** an in-connector deterministic readback checked all ten source packets against the original English, Myanmar and example strings (**0 mismatches**), confirmed the hold flags and exact 200-per-level first-pass counts, and checked that new workflow and release-auditor hooks are present. **This does not mean the new Python or GitHub Actions jobs passed.** The available GitHub commit-to-workflow lookup returns only PR-triggered runs; it returned **no new push run IDs** for the new workflow commit. New CI conclusions/logs must be marked **UNVERIFIED**, not assumed successful.

**Historical real Actions evidence (not for the new code):** [structural run 40523520139](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40523520139) has six actual **success** job conclusions, including ALL job `122256725035` log showing 1,000 provisional rows, 0 approvals, 120 shared IELTS headwords and protected-production diff PASS. [Documentary run 40523612424](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40523612424), job `122257054302`, concluded **success** as report-only, with log explicitly blocking launch for missing human approvals, final audio listening, device tests, hosting measurements and deployment evidence. Neither run tested the new 2026-10-28 code.

## GitHub Pages policy and still-missing launch gates

[Official GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), checked **2026-10-28**: source repository **recommended** size limit 1 GB, published site **maximum** 1 GB, **soft** bandwidth limit 100 GB/month, deployment timeout 10 minutes, and soft 10 builds/hour (custom Actions deployments exempt from the last build-rate cap). These are **policy observations only**; no final site build bytes, full repository size, voice-file count/bytes, forecast traffic, or measured usage receipts were produced.

**Mandatory blockers:** 0/1,000 genuine independent English, Myanmar, example and source-backed CEFR review receipts; no approved manifest; unresolved Oxford, Cambridge and IELTS cross-bank review flags; no complete final George/Emma headword-and-example audio with real human listening receipts; missing full desktop/mobile browser regressions, physical iPhone Safari evidence, hosting measurements, final protected-asset audit and confirmed live deployment. The original 54 lessons, protected IELTS bank, established George/Emma production audio and privacy remain outside this staging-only work.

**Do not publish or notify completion.** The user has authorised eventual public launch **only after every required gate is independently evidenced and production verified**.

## 2026-10-28 CI failure investigation and verified staging repair (18:55 UTC)

**Actual prior failures inspected (not inferred):** structural run [40555067288](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40555067288) failed because the eight A2 Cambridge source packet snapshots used `myanmar_meaning`, while the canonical 1,000 shortlist stores Myanmar under `burmese_meaning`. This was a schema-mapping bug in the auditor, not evidence of changed Myanmar content. The C1 auditor also rejected the valid concise heading `adverb (only)` for `exclusively` solely because it was fewer than 15 characters. Documentary gate run [40555126410](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40555126410) failed for the same C1 length check.

**Staging-only fixes committed:** [45ae52f02699f0beea0772febe43517b9073cc98](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/45ae52f02699f0beea0772febe43517b9073cc98) corrected the A2 snapshot mapping to the canonical `burmese_meaning` key without modifying the shortlist or the source observations. [18c64356d7a17e7bd2eb8e21a4cf497e16d67b1d](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/18c64356d7a17e7bd2eb8e21a4cf497e16d67b1d) permits concise C1 sense headings of five or more characters while preserving the 15-character substantive-observation and risk thresholds, and adds a negative mutation test that rejects an empty heading.

**Real post-fix GitHub Actions verification:** [structural run 40564426957](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40564426957), head `18c64356d7a17e7bd2eb8e21a4cf497e16d67b1d`, concluded **success**. Its six actual job conclusions were **A1 success, A2 success, B1 success, B2 success, C1 success, ALL success** (job IDs 122401750428, 122401751093, 122401750775, 122401751019, 122401750916, 122401751235 respectively). This verifies structural checks and negative tests, **not** publisher-backed independent CEFR or bilingual approval. The intermediate structural run [40564411877](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40564411877) used the A2-only fix and retained the C1 failure, confirming the separate second fix was needed.

[Documentary launch-gate run 40564426819](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40564426819), job `122401750375`, concluded **success** as a **report-only, no-deploy** check. Its real log reports **0/1,000** independent review packets and **0/1,000** both-voice listening receipts, with missing physical iPhone, mobile/desktop, hosting measurements, approved manifest and production confirmation. The job also reported protected production assets untouched by staging, and uploaded a blocker artifact (ID `12762118198`). A successful documentary-gate workflow **does not mean release readiness**.

**Counts remain unchanged:** A1 200 written/0 independently checked; A2 200/0; B1 200/0; B2 200/0; C1 200/0; total **1,000 provisional, 0 independently approved**. No final George/Emma listening or physical iPhone evidence is claimed. **Release remains BLOCKED / STAGING ONLY; main and production are not modified.**
