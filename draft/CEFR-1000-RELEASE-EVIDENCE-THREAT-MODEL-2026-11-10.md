# CEFR-1000 release gate security review — 2026-11-10

Status: **STAGING ONLY / NOT A RELEASE APPROVAL**. Scope: approved 1,000 total (A1–C1: 200 each), not the abandoned 5,000-word target. Inspected `scripts/check_cefr1000_release_evidence.py` on staging on 2026-11-10. This is a code-level threat assessment, **not** a human independent vocabulary, listening or device review.

## Confirmed structural strengths
- Requires exactly 1,000 manifest entries and declared 200 per level, independently recomputes per-level counts, and detects normalized cross-level headword/sense duplicates.
- Requires five per-entry review domains and four audio variants (George/Emma × headword/example) plus listening attestations.
- Requires nine global gate records; absent manifest or evidence fails closed.
- Validates audio paths remain under the checkout and compares their bytes against declared SHA-256 values.

## Critical evidence-authenticity gaps — all BLOCKING
1. **Self-asserted reviewer independence.** `valid_attestation` trusts JSON booleans `independent: true`, `self_evaluation: false`, and a caller-supplied reviewer ID. A fabricated reviewer identity or a second alias of the author can satisfy schema checks. Require externally authenticated identities, reviewer roster, separation-of-duties policy and immutable reviewer signatures tied to each exact reviewed artifact. Human signoff remains mandatory.
2. **Hash not bound to reviewed entry.** `content_sha256` is only checked for 64 hex characters, not recomputed from canonical English definition, Myanmar meaning, example, sense and CEFR decision. A review can be replayed after content edits. Define canonical serialization and recompute digest; bind the attestation to manifest commit SHA, entry ID, reviewed fields and reviewer signature. Any post-signoff edit must invalidate review.
3. **Evidence URLs not validated.** Any HTTP(S) prefix passes. Require source-specific exact-sense CEFR URLs, observed date, quotation/paraphrase, source title, source licence/usage compliance and human verification. URL accessibility alone is not proof of CEFR.
4. **Audio content not authenticated by listening.** Any file with a matching hash is accepted, even if silent, wrong-language, wrong-voice or wrong text; JSON listening signoff can be fabricated. Validate format, duration, sample rate and non-silence as preflight only; independently listen to each George/Emma headword and example and bind signed listening records to the actual file hash and script text.
5. **Global gate attestations are self-declared.** Physical iPhone Safari, browser/mobile regressions, GitHub Pages limits, privacy and production preservation can be marked passed in JSON without external run/device/deployment proof. Require authenticated CI run IDs and conclusions, physical device make/model/iOS/Safari/date/tester and recordings, Pages limits assessment, deployment commit and live HTTP verification, plus before/after hashes for 54 lessons, separate IELTS 1,000-word bank and existing George/Emma assets.
6. **No publication interlock demonstrated.** The verifier prints a warning even on schema success; a workflow could publish independently. Protect production environment and main branch, enforce required checks and human approval at the deployment boundary; staging-only CI must never trigger publication.

## Suggested adversarial fixtures for future implementation
- Reviewer ID alias or forged `independent` flag; altered definition after attestation; replay of another entry's review hash.
- Same file bytes reused across all four audio slots; zero-byte/silent audio; plausible MP3 name containing unrelated speech; listening record referring to old SHA.
- URL pointing to unrelated source; publisher page supporting a different sense or no CEFR; date absent.
- Fake physical iPhone record; successful CI on a different commit; fake production URL; production assets with changed hashes.
- Duplicate headword/sense differing only by Unicode compatibility or whitespace; differing POS/sense aliases requiring editorial adjudication.

## Evidence inventory at observation time
| CEFR | First-pass written shortlist | Independently checked |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Source: staging `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json` metadata read 2026-11-10. First-pass written means provisional English/Myanmar/example fields, not reviewed correctness.

## CI and release state
GitHub Actions run [42741499287](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42741499287) has ten confirmed successful jobs (five per-level provisional audits and five adversarial regressions). This run does **not** independently verify language, audio or deployment. Complete George/Emma shortlist audio and genuine listening signoff, physical iPhone Safari, browser/mobile acceptance, Pages hosting and production launch are **not verified**. Preserve existing production and do not merge or publish.

## Next safe implementation sequence
First bind reviews to immutable per-entry content digests and authenticated human reviewer identities; then bind audio signoff to file hashes and exact spoken text; then enforce signed device/hosting/deployment evidence and a protected deployment interlock. Keep every new requirement fail-closed, with synthetic negative tests and explicit independent review before any production release.
