# CEFR 1,000 — reproducible inventory and editorial-risk scan (2026-11-04)

**Scope:** staging only; historical frozen shortlist blob `475e68ae17ab97bd937e73e5ce4794e0dcd76551`. This is an automated heuristic audit, **not** publisher CEFR evidence, independent review, approval, or a release certificate.

## Inventory

- A1: 200 first-pass entries; 0 independently approved
- A2: 200 first-pass entries; 0 independently approved
- B1: 200 first-pass entries; 0 independently approved
- B2: 200 first-pass entries; 0 independently approved
- C1: 200 first-pass entries; 0 independently approved

Total: 1000; case-folded trimmed duplicate headwords: 0. This duplicate check is not a semantic/sense-level deduplication check. Release status: **BLOCKED**.

## Heuristic scan

Flagged records: 25 (may include false positives). Rules: lowercase first-person pronoun; definition/example civil-rights mismatch; title-case headwords; broad short person/thing definitions; examples under 12 characters; curly quotation punctuation; headword whitespace. Flags are editorial leads only; absence of a flag is not evidence of correctness.

| Level | Headword | Review trigger |
|---|---|---|
| A1 | i | first-person pronoun capitalisation |
| A1 | hello | broad definition; check sense specificity |
| A1 | home | broad definition; check sense specificity |
| A1 | have | broad definition; check sense specificity |
| A1 | people | broad definition; check sense specificity |
| A1 | man | broad definition; check sense specificity |
| A1 | give | broad definition; check sense specificity |
| A1 | make | broad definition; check sense specificity |
| A1 | friend | broad definition; check sense specificity |
| A1 | woman | broad definition; check sense specificity |
| A1 | as | broad definition; check sense specificity |
| A1 | about | broad definition; check sense specificity |
| A1 | who | broad definition; check sense specificity |
| A1 | grandmother | broad definition; check sense specificity |
| A1 | grandfather | broad definition; check sense specificity |
| A2 | nothing | broad definition; check sense specificity |
| A2 | cause | broad definition; check sense specificity |
| A2 | middle | broad definition; check sense specificity |
| B1 | civil | civil-rights example may not match civilian definition |
| B1 | condition | broad definition; check sense specificity |
| B1 | bottom | broad definition; check sense specificity |
| B1 | adult | broad definition; check sense specificity |
| B1 | produce | broad definition; check sense specificity |
| B2 | repeat | broad definition; check sense specificity |
| B2 | alongside | broad definition; check sense specificity |



## Release blockers and next action

1. Obtain dated, source-linked, exact-sense CEFR evidence per candidate; do not transfer levels across morphological relatives or rely on historical WordNet labels.
2. Independently check English, fluent Myanmar, grammar, and CEFR evidence for all 1,000 records. Preserve the existing zero approvals until real reviewer evidence exists.
3. Verify an approved manifest of exactly 200 distinct headword/sense records per level; do not treat this provisional inventory as approved.
4. Generate both George and Emma headword/example assets and retain human listening signoff; then complete browser/mobile and physical iPhone Safari evidence, hosting and production deployment checks.
5. Run six parallel GitHub Actions lanes and inspect current commit run/job conclusions and raw logs before any release decision. No CI execution is asserted for this documentation-only change.

Source: [frozen provisional shortlist](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/blob/cefr-5000-bilingual-qa-staging/draft/CEFR-1000-PROVISIONAL-SHORTLIST.json), observed 2026-11-04. Protected 54 lessons, separate IELTS bank, production audio and main must remain untouched.
