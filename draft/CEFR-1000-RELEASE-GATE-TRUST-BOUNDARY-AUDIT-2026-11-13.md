# CEFR-1000 release-gate trust-boundary audit — 2026-11-13

Status: **STAGING RESEARCH ONLY — NOT INDEPENDENT REVIEW OR RELEASE AUTHORISATION**.

## Scope and provenance
Inspected the actual staging versions of `scripts/cefr1000-release-gate.cjs`, `scripts/cefr1000-release-gate-negative-tests.cjs`, and `.github/workflows/cefr-1000-provisional-release-regression.yml` on 2026-11-13 through the authenticated GitHub connector. This audit does not modify the provisional shortlist or review-task records. Target is **1,000 total** (A1/A2/B1/B2/C1: 200 each), never 5,000.

## Concrete weaknesses requiring fail-closed remediation
1. **Reviewer independence is not authenticated.** The validator accepts any nonempty `reviewer_id`, `signed_at`, HTTPS `evidence_url`, and `decision: approved`. A manifest author could self-assert these fields. An HTTPS URL is not proof that a human independently checked the exact entry. Require an externally controlled reviewer registry and evidence attestations bound to the manifest digest, lexical-sense ID, review domain, reviewer identity, and signed decision. Validate reviewer separation from entry author; never auto-generate or self-approve reviewer evidence.
2. **Source URLs are syntactically checked, not inspected.** `cefr_sources` requires HTTPS, nonempty observation date, exact-sense string and matching level, but the code cannot verify whether the cited page assigns that level to the exact sense. Require independently adjudicated source excerpts/locator, publisher, retrieval date, sense/POS match and reviewer attestation. Cambridge/Collins URLs alone must not be treated as evidence of a particular level.
3. **Dates are unchecked strings.** `signed_at`, `observed_on`, `listened_at` and `checked_at` accept arbitrary nonempty strings. Require ISO-8601 parseable dates, chronology checks and reviewer provenance; prohibit future-dated evidence.
4. **Listening signoff is self-asserted.** `listening_reviewer` and `listening_result: pass` are sufficient when an audio file exists and matches its checksum. Hashes prove file integrity, not a human actually listening or correct British George/Emma pronunciation. Require independently recorded, attributable listening session evidence per voice and per headword/example, bound to the exact SHA-256.
5. **QA and deployment evidence are self-asserted.** A `pass` field plus HTTPS URL and timestamp does not prove physical iPhone Safari use, GitHub Pages limits, live deployment, or preservation of 54 lessons, the separate IELTS 1,000 bank and existing production George/Emma audio. Verify immutable external run/device/hosting/deployment artifacts, production commit, and pre/post asset hashes. Keep release blocked until actual checks.
6. **Lexical duplication may be disguised.** The uniqueness key combines headword, POS and arbitrary `sense_id`. Two entries representing the same meaning can evade detection by using different IDs. Add editorial cross-level semantic collision review; structural uniqueness is necessary but insufficient.
7. **Regression coverage is exclusively negative.** Eight cases ensure blocking but do not prove a genuinely complete signed manifest can pass. Add an explicitly synthetic positive fixture only after external-evidence trust checks are implemented; synthetic evidence must never be reused as real approval.

## Workflow observations
The five-level matrix is configured with `fail-fast: false`, read-only permissions and staging-branch push triggers. Each level currently executes the same eight negative scenarios, rather than level-specific negative fixtures. This is a useful baseline but not proof of actual GitHub Actions execution or per-level source/linguistic QC. The current workflow is also path-filtered, so documentation-only commits do not necessarily trigger it.

## Required release state
A1: 200 provisional, 0 independently approved; A2: 200, 0; B1: 200, 0; B2: 200, 0; C1: 200, 0. These are the established baseline, **not a newly verified full inventory execution**. All 1,000 remain on editorial hold. Audio generation/listening, browser/mobile/physical iPhone, GitHub Pages, and production preservation/deployment are not verified in this audit.

## Next implementation priorities
Implement a separate immutable evidence-attestation verifier and per-level reviewer/source coverage report, with negative fixtures for forged reviewer IDs, nonexistent source citations, invalid dates, duplicate semantic senses, missing audio/listening proof and unverified device/deployment claims. Then execute the tests locally and inspect the actual five GitHub Actions job conclusions/logs. Never publish or merge while any gate remains unverified.
