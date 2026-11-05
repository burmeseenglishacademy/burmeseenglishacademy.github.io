'use strict';
/* Staging-only inventory checks. These never imply independent linguistic approval. */
const fs = require('node:fs');
const assert = require('node:assert/strict');
const level = process.argv[2];
const levels = ['A1','A2','B1','B2','C1'];
assert.ok(levels.includes(level), 'Explicit valid CEFR level required');
const doc = JSON.parse(fs.readFileSync('draft/CEFR-1000-PROVISIONAL-SHORTLIST.json','utf8'));
assert.equal(doc.release_status,'PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH');
assert.equal(doc.entries.length,1000);
assert.deepEqual(doc.scope_target,Object.fromEntries(levels.map(l=>[l,200])));
assert.deepEqual(doc.counts_by_level,doc.scope_target);
assert.deepEqual(doc.independently_approved_by_level,Object.fromEntries(levels.map(l=>[l,0])));
assert.equal(doc.stages.independent_source_evidence,'NOT_OBSERVED');
assert.equal(doc.stages.production,'UNMODIFIED');
const keys = new Set();
const sourcePointers = new Set();
const counts = Object.fromEntries(levels.map(l=>[l,0]));
const reviewFlags=['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation','release_approved'];
for (const [i,e] of doc.entries.entries()) {
  assert.ok(levels.includes(e.level),'Unknown level at '+i);
  counts[e.level]++;
  for(const field of ['word','part_of_speech','english_definition','burmese_meaning','example_sentence','source_path','source_blob_sha']) {
    assert.equal(typeof e[field],'string',i+' missing '+field);
    assert.ok(e[field].trim(),i+' blank '+field);
  }
  assert.ok(/[\u1000-\u109f]/u.test(e.burmese_meaning),i+' lacks Myanmar script');
  assert.ok(/^[a-f0-9]{40}$/i.test(e.source_blob_sha),i+' invalid source blob SHA');
  assert.ok(/^draft\/[a-zA-Z0-9._/-]+\.json$/.test(e.source_path) && !e.source_path.includes('..'),i+' unsafe source path');
  assert.ok(Number.isSafeInteger(e.source_index) && e.source_index>=0,i+' invalid source index');
  const key=e.word.normalize('NFC').trim().toLocaleLowerCase('en');
  assert.ok(!keys.has(key),'Duplicate headword across levels: '+key);
  keys.add(key);
  const sourceKey=e.source_path+'#'+e.source_index;
  assert.ok(!sourcePointers.has(sourceKey),'Repeated source entry pointer: '+sourceKey);
  sourcePointers.add(sourceKey);
  assert.equal(e.editorial_hold,true,i+' must remain on editorial hold');
  assert.equal(e.status,'PROVISIONAL_SHORTLIST_INDEPENDENT_REVIEW_PENDING',i+' unsupported status');
  for(const flag of reviewFlags) assert.equal(e[flag],false,i+' unsupported approval flag '+flag);
  for(const field of ['source_english','source_burmese','source_level']) assert.equal(e[field],'',i+' unsupported source attestation '+field);
}
assert.deepEqual(counts,doc.scope_target,'Actual per-level counts differ');
console.log('PASS '+level+': 200 provisional entries; 0 independently approved; global hold and provenance checks; structure only');
