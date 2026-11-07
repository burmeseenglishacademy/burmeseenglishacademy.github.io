#!/usr/bin/env node
// Staging-only lexical collision and provenance audit. Read-only; never approves entries.
import { readFileSync } from 'node:fs';
const file = 'draft/CEFR-1000-PROVISIONAL-SHORTLIST.json';
const doc = JSON.parse(readFileSync(file, 'utf8'));
if (!Array.isArray(doc.entries)) throw new Error('Fail closed: entries must be an array');
const levels = ['A1','A2','B1','B2','C1'];
const clean = s => String(s ?? '').normalize('NFKC').trim().replace(/\s+/g,' ').toLocaleLowerCase('en');
const byHeadword = new Map(), bySense = new Map(), bySource = new Map(), risks = [];
const valid = /^[0-9a-f]{40}$/i;
for (const [index, e] of doc.entries.entries()) {
  if (!e || typeof e !== 'object' || Array.isArray(e)) throw new Error('Invalid entry '+index);
  const headword = clean(e.word);
  const pos = clean(e.part_of_speech);
  const sense = clean(e.english_definition);
  const key = [headword,pos,sense].join('|');
  const sourceKey = [e.source_path,e.source_index,e.source_blob_sha].join('|');
  for (const [map,k] of [[byHeadword,headword],[bySense,key],[bySource,sourceKey]])
    map.set(k,[...(map.get(k)??[]),{index,level:e.level,word:e.word,pos:e.part_of_speech,definition:e.english_definition}]);
  const flags = [];
  if (!levels.includes(e.level)) flags.push('unknown-level');
  if (!headword || !pos || !sense) flags.push('missing-exact-sense-identity');
  if (!valid.test(String(e.source_blob_sha??''))) flags.push('invalid-source-blob-sha');
  if (!Number.isInteger(e.source_index)||e.source_index<0) flags.push('invalid-source-index');
  if (!String(e.source_path??'').startsWith('draft/')) flags.push('unexpected-source-path');
  if (/\b(?:wordnet|named[._ -]entity|proper[._ -]noun)\b/i.test(JSON.stringify(e))) flags.push('historical-wordnet-or-entity-marker');
  if (/^[A-Z][a-z]+(?: [A-Z][a-z]+)*$/.test(String(e.word??'')) && !['I'].includes(e.word)) flags.push('possible-named-entity');
  if (flags.length) risks.push({index,level:e.level,word:e.word,flags});
}
const duplicates = map => [...map.entries()].filter(([key,rows])=>key && rows.length>1).map(([key,rows])=>({key,rows}));
const sameHeadword = duplicates(byHeadword);
const sameSense = duplicates(bySense);
const sameSource = duplicates(bySource);
const perLevel = Object.fromEntries(levels.map(level=>[level,{
  first_pass:doc.entries.filter(e=>e.level===level).length,
  independent_approvals_observed:doc.entries.filter(e=>e.level===level && e.release_approved===true).length,
  flagged_risks:risks.filter(e=>e.level===level).length
}]));
const structuralProblems = [];
for (const level of levels) if (perLevel[level].first_pass!==200) structuralProblems.push(level+' count is not 200');
if (doc.entries.length!==1000) structuralProblems.push('total count is not 1000');
if (sameSense.length) structuralProblems.push('duplicate exact-sense keys');
if (sameSource.length) structuralProblems.push('duplicate source provenance pointers');
if (doc.entries.some(e=>e.editorial_hold!==true || e.release_approved!==false)) structuralProblems.push('provisional hold/approval invariant violated');
const output = {
  kind:'CEFR-1000 provisional lexical/provenance diagnostic; NOT release authorization',
  file, per_level:perLevel,
  same_headword_groups:sameHeadword,
  exact_sense_collisions:sameSense,
  repeated_source_provenance:sameSource,
  risk_candidates:risks,
  structural_problems:structuralProblems,
  release_ready:false,
  note:'A shared headword may represent different legitimate senses; all cross-level groups require independent exact-sense CEFR review. Heuristics are advisory only.'
};
console.log(JSON.stringify(output,null,2));
if (process.argv.includes('--inventory-audit')) process.exitCode=structuralProblems.length?1:0;
else process.exitCode=1;
