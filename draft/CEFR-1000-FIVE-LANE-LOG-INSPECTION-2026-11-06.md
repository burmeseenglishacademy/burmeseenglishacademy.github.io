# CEFR-1000 five-lane CI log inspection and editorial handoff — 2026-11-06

**Scope:** 1,000 TOTAL provisional words, A1/A2/B1/B2/C1 exactly 200 each; not the superseded 5,000-word proposal. **Branch:** `cefr-5000-bilingual-qa-staging`. **Release decision: BLOCKED.** This report does not approve any entry or permit publishing.

## Evidence observed

GitHub Actions run [42046717593](https://github.com/burmeseenglishacademy/burmeseenglishacademy.github.io/actions/runs/42046717593), from the earlier Markdown summary fix at commit `7b7f2b206c61f9c5f31205bc0a2626f349e976e7`: retrieved job conclusions **and raw job logs** on 2026-11-06 UTC. All five jobs completed with conclusion `success`:
- A1 job `127311546420`
- A2 job `127311546856`
- B1 job `127311546927`
- B2 job `127311546941`
- C1 job `127311547198`

Each job's step summary reported successful provisional inventory checks, editorial-risk triage, rejected-release fixtures, eight adversarial fixtures and rejection of provisional entries as approved manifest. Raw logs were retrieved for all five jobs (roughly 20 KB each). The logs also contained a Node.js 20 deprecation warning for `actions/checkout@v4` and `actions/setup-node@v4`, currently forced to Node.js 24 by the runner. This is a maintenance warning, not a failed check. **The above run is not evidence that later commits passed CI.** In particular, latest changes to editorial triage must be separately run and verified.

## Inventory and review (source: staging shortlist metadata, not human verification)

| Level | First-pass written | Independently checked/approved |
|---|---:|---:|
| A1 | 200 | 0 |
| A2 | 200 | 0 |
| B1 | 200 | 0 |
| B2 | 200 | 0 |
| C1 | 200 | 0 |
| **Total** | **1,000** | **0** |

Shortlist: `draft/CEFR-1000-PROVISIONAL-SHORTLIST.json`. The separate `draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json` currently returned empty content through the connector; this is **not** proof that the file is empty. Its contents need an independent retrieval path before any task-level claims.

## Priority editorial queue

1. For each selected exact lexical sense, obtain publisher URL, publisher/entry identifier, part of speech, sense identifier or quoted sense locator, **explicit** CEFR evidence if available, and actual UTC observation date. A dictionary URL without a sense-specific CEFR label must **not** count as CEFR verification.
2. Record a separate independently authenticated English, fluent Myanmar, original example, and CEFR-level review for every entry. Self-review and heuristic triage must not increment approvals. Resolve same-headword cross-level collisions by exact sense and POS, not spelling alone.
3. Prioritize A1 `a` and `an`: distinguish vowel **sounds** from vowel letters and clarify the difference between indefinite articles, determiners and context-specific use. Existing English/Myanmar definitions and examples are first-pass only; preserve editorial hold pending external publisher evidence and independent signoff.
4. Investigate historical WordNet-derived entries, proper names and noncanonical forms. WordNet/synset metadata alone does not establish a CEFR level.
5. Maintain original source paths, source indices and blob SHAs; attach external evidence separately rather than silently changing historical provenance.

## Non-linguistic release blockers

No verified complete British George/Emma **headword plus example** audio inventory for the approved final 1,000; no genuine complete listening signoff; no verified mobile/browser regression; no physical iPhone Safari review evidence; no completed GitHub Pages hosting/capacity clearance; no verified production launch or post-launch preservation audit. Preserve the 54 production lessons, separate IELTS 1,000-word bank, existing production George/Emma audio and privacy settings. **Do not merge, publish or touch main.**

This report is a staging-only record of evidence available at the time of inspection. Structural CI success is not editorial approval, audio QA, physical device testing or production readiness.
