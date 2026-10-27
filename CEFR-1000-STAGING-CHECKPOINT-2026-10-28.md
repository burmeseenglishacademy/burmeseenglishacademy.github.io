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

## Additional B1 publisher exact-sense triage and staging CI — 2026-10-28

**Scope and counts unchanged:** A1 **200 written / 0 independently checked**; A2 **200/0**; B1 **200/0**; B2 **200/0**; C1 **200/0**. Total **1,000 provisional bilingual entries, 0 independently approved**. Every entry remains on editorial hold. No new approved manifest, voice listening receipts, real physical iPhone Safari checks, hosting measurement, or production deployment.

New [twelve-word B1 Cambridge source packet](draft/CEFR-1000-CAMBRIDGE-B1-TWELVE-SENSE-LEADS-2026-10-28.json) committed at `216fc0771d246e4f95f8c394a4447a4bc88d1508`. Publisher-owned Cambridge search-indexed page excerpts observed **2026-10-28** (direct dictionary pages returned HTTP 403; not independent or full-page verification):

| B1 draft word | Cambridge source label observed | Specific editorial issue |
| --- | --- | --- |
| independent | B2 NOT INFLUENCED | The draft's independent decision invokes autonomy from control, not B1 self-sufficiency |
| impact | B2 EFFECT | The draft policy's impact on businesses is the B2 effect sense |
| effective | B2 SUCCESSFUL | Regular practice as an effective method is the B2 achieving-results sense |
| analysis | B2 detailed examination | Survey-results analysis uses the B2 careful-study sense |
| complex | B2 connected parts / hard to understand | Both aspects of the draft adjective are B2 |
| critical | B2 IMPORTANT | Emergency drinking water is the B2 importance sense, not critical illness |
| necessary | B1 NEEDED | Matching sense lead; still needs independent Myanmar/example/CEFR review |
| equipment | B1 uncountable tools | Matching sense lead; independently check uncountable grammar |
| application | B1 REQUEST | Distinguish the formal request from the B2 computer-program sense |
| purpose | B1 REASON | Distinguish the meeting's aim from idiomatic `on purpose` |
| solution | B1 ANSWER | Distinguish solving a problem from a chemical solution |
| otherwise | B1 conditional **conjunction**, B2 adverb EXCEPT | Draft conditional `otherwise` is recorded as an **adverb**; exact POS needs independent resolution |

Publisher URLs, dates, exact original English/Myanmar/example snapshots, observed sense headings and individual reviewer tasks are stored in the JSON packet. These are **12 source leads, not 12 approved entries**. Six same-sense higher-source-level discrepancies and one explicit POS mismatch remain editorial blockers, not grounds for automatic retiering.

New [B1 structural auditor](tools/audit_cefr_1000_cambridge_b1_twelve.py), commit `f4b874394736acae7fbc87a54df5f9dfd1ffcef4`, binds the 12 observations to the pinned shortlist blob, verifies original bilingual/POS/example snapshots, URLs and source labels, and rejects false independent approval with **13 negative mutations**. [Six-job parallel matrix](.github/workflows/cefr-1000-selection-structural-qa.yml) updated at `59749d80d3c80917485ae0ba71321bcc7cf2b783`. [Release auditor](tools/audit_cefr_1000_launch_readiness.py) updated at `57060db81d10984ff42862fbb9c7e20fb67bbeec` to require separate real independent B1 exact-sense, conflict and POS resolution receipts for retained entries; [release ledger](draft/CEFR-1000-RELEASE-EVIDENCE.json) at `8d5298d141b3d3ceb7e06c87343abf7e9c542883` contains **zero** B1 receipts. Documentary no-deploy workflow updated at `2be5b2e85f0049d059f99940143bb9eaa31d7d23`.

**Actual GitHub Actions evidence:** [structural run 40578791052](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40578791052), head `59749d80d3c80917485ae0ba71321bcc7cf2b783`, concluded **success** across A1, A2, B1, B2, C1 and ALL jobs. The actual ALL job `122452295318` log reports **12 B1 source leads / 0 independent approvals / 0 errors**, **13 negative mutations rejected**, and protected production assets unchanged. This verifies structural safeguards, **not** human linguistic review or physical listening.

The newer [documentary launch gate run 40578849751](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40578849751) for head `2be5b2e85f0049d059f99940143bb9eaa31d7d23` was **in progress at this checkpoint**, so no success or failure is claimed. The documentary workflow has no deploy step; a future successful report-only conclusion cannot prove release readiness.

**Release remains BLOCKED / STAGING ONLY.** Main, 54 lessons, protected IELTS 1,000 bank, production George/Emma recordings and privacy settings have not been edited in this work. Independent reviewer, both-voice human listening, browser/mobile, physical iPhone Safari, hosting, final asset-preservation and confirmed live deployment evidence remain absent.

### Post-checkpoint verified documentary CI conclusion

The above pending documentary workflow has now **completed successfully as a report-only gate**: [run 40578849751](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40578849751), job **122452502524**, head `2be5b2e85f0049d059f99940143bb9eaa31d7d23`. Actual job log shows Python syntax compilation, B1 **13 negative mutations rejected**, UI syntax/regression mock checks, release-gate negative tests, and protected-production diff PASS. Its truthful blocker output still reads **0/1,000 independently source-reviewed** and **0/1,000 both-voice listening**, with no approved manifest, physical iPhone, browser/device regression evidence, measured hosting or production confirmation. Blocker artifact ID **12768671847**. The workflow success means **the no-deploy blocker report executed correctly**, NOT that the product passed release QC. Other intermediate documentary runs **40578820389** and **40578834425** also have actual successful job conclusions; the latest run supersedes them for this checkpoint. Production remains unchanged and release **BLOCKED**.

### Final source-text tamper-hardening verification

The B1 auditor was strengthened at commit [`aee33708020c78a49779f6297671357e77780973`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/aee33708020c78a49779f6297671357e77780973) to pin the exact publisher-indexed sense headings and observation text, not just source URLs and field lengths. An added non-empty invented-evidence mutation is rejected: **14 negative tests** in total.

**Real latest post-change GitHub Actions:** [structural run 40578987990](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40578987990) at that SHA completed with **all six jobs successful** (A1 `122452985177`, A2 `122452985004`, B1 `122452985359`, B2 `122452985077`, C1 `122452984605`, ALL `122452985007`). Actual ALL log confirms 12 B1 leads, zero approvals, zero source-audit errors, 14 fake/altered-evidence mutations rejected and protected-production diff PASS.

[Latest documentary no-deploy run 40578987997](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40578987997), job `122452984729`, also **concluded success as a blocker-report workflow**, not a launch approval. Its actual log still states **0/1,000 independent source reviews**, **0/1,000 both-voice listening receipts**, missing approved manifest, physical iPhone, browser/mobile, hosting and final production verification. The staging-only release decision remains **BLOCKED**.

## Additional direct A1 Oxford word/POS audit and orthography release guard — 2026-10-28

**Scope unchanged:** A1 200 first-pass / **0 independently approved**; A2 200/0; B1 200/0; B2 200/0; C1 200/0. Exactly **1,000 provisional / 0 independent approvals**. All remain on editorial hold, with no final audio listening, physical iPhone Safari, hosting measurements, approved manifest, or production deployment.

**New directly inspected publisher evidence:** [Oxford University Press, *The Oxford 3000 by CEFR level*](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf), inspected **2026-10-28**. Twelve A1 headword/POS observations were added to [the immutable-snapshot editorial packet](draft/CEFR-1000-OXFORD-A1-TWELVE-DIRECT-PDF-2026-10-28.json) at commit [`44a188687abfbd64e8a1bc044b6b5e43bc80f0d3`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/44a188687abfbd64e8a1bc044b6b5e43bc80f0d3). The entries are **i, be, you, we, the, this, that, he, she, please, goodbye, thank**. The packet preserves the original English definition, Myanmar meaning and example for each, the official source URL, observation date, one-based PDF page, extracted text-line locator, short source label, POS, editorial risk and independent review task. **These are word/POS references, not independent exact-sense CEFR, fluent Myanmar or example-grammar approvals.**

Two material editorial risks emerged:
- **i / I:** The provisional shortlist uses lowercase `i`, whereas the Oxford A1 PDF records uppercase **I pron.** (PDF page 2, extracted line 386). English standalone first-person singular pronoun is capitalised. The canonical shortlist was **not** silently edited; a future independently approved manifest must use uppercase **I** with corresponding review/source binding updates.
- **please:** The draft's POS is `politeness marker`; Oxford labels **exclamation** (PDF page 3, extracted line 604). An independent editor must decide how to reconcile pedagogical function with the canonical lexical POS. Other records flag pronoun register, definition/example scope, and the naturalness of the `thank` and `goodbye` examples/glosses.

**Fail-closed QA:** New [A1 direct-source auditor](tools/audit_cefr_1000_oxford_a1_twelve.py), commit `90fc3b66e6967c701394ce832a325050f97ed95e`, pins all twelve locators/source labels, original draft snapshots and zero-approval hold status. It rejects **15** synthetic tampering/fake-signoff mutations. The six-way A1/A2/B1/B2/C1/ALL [parallel structural workflow](.github/workflows/cefr-1000-selection-structural-qa.yml) was updated at commit `7fca8db749e08f01cde9ffdd80af4fe33a994748`.

**Real Actions conclusions and logs:** [Structural run 40583922186](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583922186), head `7fca8db749e08f01cde9ffdd80af4fe33a994748`, completed **success** for all six jobs: B1 `122470268889`, ALL `122470269054`, A2 `122470269092`, B2 `122470269123`, A1 `122470269173`, C1 `122470269182`. Actual ALL job log says **12 direct A1 PDF word/POS observations, 0 approvals, 0 errors; 15 negative mutations rejected** and **protected production assets unchanged**. These are executed structural checks, not human editorial review.

**Future approved-release orthography safeguard:** [`tools/validate_cefr_release.py`](tools/validate_cefr_release.py) now explicitly rejects a lowercase `i` headword and requires display **I** for the first-person singular pronoun (commit `e397455b6f14ade9ba72c2f30951b3f36c19d5ee`). Its [negative and positive regression test](tests/cefr-release-evidence-gate.py) was added at commit `4807a082f4cc26b37984ce5909a8c7068b81dd0f`. [Real release regression run 40583973894](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583973894), job `122470446177`, head `4807a082f4cc26b37984ce5909a8c7068b81dd0f`, completed **success**; the log confirms Python compilation and execution of the negative-release tests. A successful regression does not make the provisional content releasable.

**Remaining blockers:** genuine independent human English/Myanmar/example/exact-sense CEFR review for all 1,000; any needed editorial revisions and independently approved release manifest; actual final George/Emma headword and example generation and **real listening signoff**; desktop/mobile and **physical iPhone Safari** QA; measured GitHub Pages site/repository/traffic budgets; protected-assets audit and confirmed live production deployment. No main-branch changes, merges, public release, or completion claim were made. **BLOCKED / STAGING ONLY.**

### Verified post-orthography documentary QC and regression conclusions

At the final check, [A1 draft regression run 40583973685](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583973685), [release evidence regression run 40583973894](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583973894), and [documentary no-deploy run 40583973797](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583973797) all had actual **completed/success** conclusions for head `4807a082f4cc26b37984ce5909a8c7068b81dd0f`. The release regression job ID is `122470446177`; documentary job ID is `122470446572`. The documentary log explicitly reports **0/1,000 independent source reviews, 0/1,000 both-voice listening receipts**, no approved manifest, missing desktop/mobile and physical iPhone evidence, no measured hosting receipt and no production confirmation. Its blocker-report artifact ID is `12770558856`. The same log confirms the protected production diff PASS. **These are successful fail-closed staging/report workflows, not an approval or a deployment.**


## Additional Oxford direct-PDF A2-draft cross-level audit — 2026-10-28

**Release remains BLOCKED / STAGING ONLY.** The user-approved scope remains A1 **200 written / 0 independently approved**, A2 **200/0**, B1 **200/0**, B2 **200/0**, C1 **200/0**: exactly **1,000 provisional bilingual entries, 0 independent human approvals**. The original shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551` and separate IELTS bank are unchanged.

**New publisher source evidence, not exact-sense approval:** Directly inspected the [Oxford University Press *Oxford 3000 by CEFR level* PDF](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) on **2026-10-28**. Twelve A2 provisional entries now have independently locatable publisher **word/POS-level** observations, original English/Myanmar/example snapshots and distinct reviewer tasks in [the source packet](draft/CEFR-1000-OXFORD-A2-TWELVE-DIRECT-PDF-2026-10-28.json), commit [`bba6b6891da7ab191fe46414630f30f9c54c2a0b`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/bba6b6891da7ab191fe46414630f30f9c54c2a0b). The source PDF lists **11 of these provisional A2 headwords at A1 word/POS level**: `world` (page 4, line 893), `life` (2:439), `through` (3:798), `part` (3:574), `better` (1:82), `team` (3:768), `someone` (3:716), `must` (2:507), `show` (3:694), `company` (1:165) and `group` (2:340). `while` is Oxford **A2 conjunction** (page 7, line 1762), matching the draft's word/POS. **This is not a verdict on the exact senses:** each entry needs separate publisher exact-sense A2 evidence, fluent Myanmar/English/example review and a genuine independent human decision before retention or replacement.

**Safeguards added, staging only:** [`tools/audit_cefr_1000_oxford_a2_twelve.py`](tools/audit_cefr_1000_oxford_a2_twelve.py) pins all 12 publisher PDF line locators, source CEFR word/POS labels, the immutable shortlist blob, original bilingual/example snapshots, zero approvals and hold flags; it defines **15 synthetic tamper/fake-review negative tests**. Its latest POS-mutation repair is commit [`4297bc411e4a6aa366cc8f0249cfad57b88c7f4c`](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/commit/4297bc411e4a6aa366cc8f0249cfad57b88c7f4c). The six-way [structural Actions matrix](.github/workflows/cefr-1000-selection-structural-qa.yml) includes the new source audit and ALL negative tests (commit `f220bf0e4513d6d37dd7155d4a98cdd3f788f72a`). [Release-readiness auditor](tools/audit_cefr_1000_launch_readiness.py) now requires separately attested **A2 exact-sense** and Oxford A1/A2 word/POS discrepancy resolution for retained entries (commit `64b8e82302e43866f636ef201027848bbf325544`). The [evidence ledger](draft/CEFR-1000-RELEASE-EVIDENCE.json) has an explicitly **empty** `oxford_a2_twelve_review_receipts` array (commit `5ada4c405f07312b10e423b670eb0331e5a41e3a`). The documentary no-deploy workflow includes the same auditor and negative tests (commit `007d033f8b2e09a747027537ec67260eedaa922d`).

**Verification boundary:** An in-connector readback checked the 12 records against the unchanged canonical English, Myanmar, POS and example strings (**0 mismatches**), 11 A1/1 A2 publisher word/POS counts, pinned shortlist blob and source-audit/CI hooks. The GitHub connector's commit-workflow lookup only covers PR-triggered runs and returned no new push run IDs. **New Python test execution, GitHub Actions job conclusions and logs remain UNVERIFIED** for these new changes; do not inherit previous CI PASS results. Earlier real [structural run 40583922186](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583922186) and [documentary run 40583973797](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/40583973797) predate this code and do not validate it.

**Essential launch blockers remain:** 0/1,000 independent source-backed English/Myanmar/example/CEFR approvals, no approved release manifest, no final both-voice George/Emma generated-and-really-listened receipts, no desktop/mobile and physical iPhone Safari evidence, no measured GitHub Pages hosting budget, no final complete protected-asset audit and no confirmed live production deployment. Main, the 54 lessons, IELTS bank, production audio and privacy remain outside this staging-only work. **No merge, deploy or completion notification.**
