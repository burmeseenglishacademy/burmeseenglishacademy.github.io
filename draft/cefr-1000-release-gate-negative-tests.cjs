#!/usr/bin/env node
// Negative-path regression for the CEFR-1000 release preflight. No production writes.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {spawnSync} = require('node:child_process');
const gate = path.join(__dirname,'cefr-1000-release-gate.cjs');
const dir = fs.mkdtempSync(path.join(os.tmpdir(),'bea-cefr-gate-'));
let checks=0;
function run(label, manifest, evidence, expected) {
  const m=path.join(dir,'manifest.json'), e=path.join(dir,'evidence.json');
  fs.writeFileSync(m,JSON.stringify(manifest));
  fs.writeFileSync(e,JSON.stringify(evidence));
  const p=spawnSync(process.execPath,[gate,m,e],{encoding:'utf8'});
  assert.equal(p.status,1,label+': gate must fail closed');
  const result=JSON.parse(p.stdout);
  assert.equal(result.status,'BLOCK',label);
  assert.ok(result.errors.some(x=>x.includes(expected)),label+': expected blocker '+expected);
  checks++;
}
try {
  run('empty',{}, {},'Expected exactly 1000');
  run('provisional-shaped', {entries:[{entry_id:'A1-1',level:'A1',headword:'school'}]}, {},'missing final');
  run('missing independent review', {entries:[{entry_id:'A1-1',level:'A1',headword:'school',part_of_speech:'noun',sense_id:'n1',english_definition:'a place to learn',myanmar_meaning:'ကျောင်း',original_example:'She goes to school.'}]}, {entries:[{entry_id:'A1-1',content_sha256:'invalid'}]}, 'invalid independent english signoff');
  run('fake CI', {entries:[],release_candidate_sha:'a'.repeat(40)}, {release_gates:{release_candidate_sha:'a'.repeat(40),ci_jobs:{}}}, 'Missing validated current-SHA CI job A1/structural');
  run('no physical iPhone', {entries:[],release_candidate_sha:'a'.repeat(40)}, {release_gates:{release_candidate_sha:'a'.repeat(40),ci_jobs:{}}}, 'Missing release gate physical_iphone_safari');
  console.log(JSON.stringify({result:'NEGATIVE_PATH_PASS',checks,scope:'blocking tests only; NOT positive release qualification'},null,2));
} finally { fs.rmSync(dir,{recursive:true,force:true}); }
