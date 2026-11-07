#!/usr/bin/env node
// CEFR-1000 staging-only evidence ledger. Never grants approval or changes input.
import { readFileSync } from 'node:fs';
const path = 'draft/CEFR-1000-PROVISIONAL-SHORTLIST.json';
const inventory = JSON.parse(readFileSync(path, 'utf8'));
const levels = ['A1','A2','B1','B2','C1'];
const entries = inventory.entries ?? [];
const reviewFields = ['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'];
const evidenceFields = ['source_english','source_burmese','source_level'];
const problems = [];
const counts = {};
const seen = new Map();
const exampleGroups = new Map();
const sourcePaths = new Map();
const riskFlags = [];
for (const level of levels) {
  const subset = entries.filter(e => e.level === level);
  const checked = subset.filter(e => reviewFields.every(k => e[k] === true));
  counts[level] = {
    written_first_pass: subset.length,
    independently_checked_claims: checked.length,
    independently_approved_claims: subset.filter(e => e.release_approved === true).length,
    editorial_holds: subset.filter(e => e.editorial_hold === true).length,
    missing_source_fields: Object.fromEntries(evidenceFields.map(k => [k, subset.filter(e => !String(e[k] ?? '').trim()).length])),
    missing_review_flags: Object.fromEntries(reviewFields.map(k => [k, subset.filter(e => e[k] !== true).length]))
  };
  if (subset.length !== 200) problems.push(`${level}: expected exactly 200 entries, got ${subset.length}`);
}
for (const [i,e] of entries.entries()) {
  const key = String(e.word ?? '').normalize('NFKC').trim().toLocaleLowerCase('en');
  if (!key) problems.push(`entry ${i}: empty headword`);
  if (seen.has(key)) problems.push(`duplicate headword ${key}: entries ${seen.get(key)} and ${i}`);
  else seen.set(key,i);
  const example = String(e.example_sentence ?? '').normalize('NFKC').trim().replace(/\\s+/g,' ').toLocaleLowerCase('en');
  if (!example) problems.push(`entry ${i}: missing example sentence`);
  else exampleGroups.set(example, [...(exampleGroups.get(example) ?? []), {index:i,level:e.level,word:e.word}]);
  for (const field of ['part_of_speech','english_definition','burmese_meaning','source_path','source_blob_sha']) {
    if (!String(e[field] ?? '').trim()) problems.push(`entry ${i}: missing ${field}`);
  }
  if (!Number.isInteger(e.source_index) || e.source_index < 0) problems.push(`entry ${i}: invalid source_index`);
  if (e.source_blob_sha && !/^[0-9a-f]{40}$/i.test(e.source_blob_sha)) problems.push(`entry ${i}: invalid source_blob_sha`);
  if (e.source_path) sourcePaths.set(e.source_path,(sourcePaths.get(e.source_path)??0)+1);
  if (/\\b(?:wordnet|named.entity|proper.noun)\\b/i.test(JSON.stringify(e))) riskFlags.push({index:i,level:e.level,word:e.word,reason:'historical lexical/named-entity marker; requires manual inspection'});
  if (!e.editorial_hold) problems.push(`entry ${i}: editorial hold absent`);
  if (e.release_approved || reviewFields.some(k => e[k] === true)) problems.push(`entry ${i}: approval/review assertion requires external evidence`);
}
if (entries.length !== 1000) problems.push(`expected 1000 entries, got ${entries.length}`);
const repeatedExampleGroups = [...exampleGroups.entries()].filter(([,items])=>items.length>1).map(([example,items])=>({example,items}));
const blockers = [
  'Independent English, Myanmar, example, CEFR and pronunciation review records not verified',
  'Exact-sense source provenance not complete',
  'British George and Emma headword/example audio with actual listening attestations not verified',
  'Browser/mobile regression and physical iPhone Safari evidence not verified',
  'GitHub Pages hosting clearance and production preservation/deployment not verified'
];
const result = {
  scope:'CEFR-1000 staging evidence inventory only',
  source:path,
  release_ready:false,
  inventory_structurally_consistent:problems.length===0,
  counts_by_level:counts,
  problems,
  advisory_repeated_example_groups:repeatedExampleGroups,
  advisory_historical_risk_markers:riskFlags,
  source_path_entry_counts:Object.fromEntries([...sourcePaths.entries()].sort((a,b)=>a[0].localeCompare(b[0]))),
  blockers,
  note:'A true structural result is NOT independent approval. This tool never asserts release readiness.'
};
console.log(JSON.stringify(result,null,2));
// Fail closed as a release gate. Use --inventory-audit to permit zero exit for informational staging audits only.
if (process.argv.includes('--inventory-audit')) process.exitCode = problems.length ? 1 : 0;
else process.exitCode = 1;
