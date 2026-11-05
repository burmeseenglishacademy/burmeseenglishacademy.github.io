'use strict';
/* Staging-only per-level inventory checks; NOT CEFR or linguistic approval. */
const fs = require('node:fs');
const assert = require('node:assert/strict');
const level = process.argv[2];
const levels = ['A1','A2','B1','B2','C1'];
if (!levels.includes(level)) throw Error('Explicit valid CEFR level required');
const doc = JSON.parse(fs.readFileSync('draft/CEFR-1000-PROVISIONAL-SHORTLIST.json','utf8'));
assert.equal(doc.release_status,'PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH');
assert.equal(doc.entries.length,1000);
assert.deepEqual(doc.scope_target,Object.fromEntries(levels.map(l=>[l,200])));
const allKeys = new Set();
for(const entry of doc.entries) {
  assert.ok(levels.includes(entry.level),'Unknown level');
  assert.equal(typeof entry.word,'string');
  assert.ok(entry.word.trim(),'Empty word');
  const key=entry.word.normalize('NFC').trim().toLocaleLowerCase('en');
  assert.ok(!allKeys.has(key),'Cross-level duplicate headword: '+key);
  allKeys.add(key);
}
const selected=doc.entries.filter(e=>e.level===level);
assert.equal(selected.length,200,level+' must have 200 provisional entries');
assert.equal(doc.counts_by_level[level],200);
assert.equal(doc.independently_approved_by_level[level],0,'No independent approvals may be inferred');
for(const [i,e] of selected.entries()){
  for(const field of ['part_of_speech','english_definition','burmese_meaning','example_sentence','source_path','source_blob_sha']){
    assert.equal(typeof e[field],'string',level+' '+i+' missing '+field);
    assert.ok(e[field].trim(),level+' '+i+' blank '+field);
  }
  assert.ok(/[\u1000-\u109f]/u.test(e.burmese_meaning),level+' '+i+' lacks Myanmar script');
}
console.log('PASS '+level+': 200 provisional entries; 0 independently approved; structural checks only');
