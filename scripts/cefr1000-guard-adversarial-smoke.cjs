#!/usr/bin/env node
/**
 * Staging-only adversarial smoke tests for the CEFR-1000 release guard.
 * Run: node scripts/cefr1000-guard-adversarial-smoke.cjs
 * Every deliberately unapproved fixture MUST fail closed, without uncaught JS exceptions.
 */
'use strict';
const {spawnSync}=require('node:child_process');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const assert=require('node:assert/strict');
const guard=path.resolve(__dirname,'cefr1000-release-manifest-guard.cjs');
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'cefr1000-negative-'));
const cases=[
 ['empty object',{}],
 ['null',null],
 ['missing entries',{release_status:'independently_approved'}],
 ['wrong inventory',{entries:[],release_status:'independently_approved'}],
 ['invalid level',{entries:[{id:'bad',level:'Z9'}]}],
 ['malformed review date',{entries:[{id:'bad',level:'A1',word:'hello',part_of_speech:'interjection',sense_id:'greeting',english_definition:'A greeting',burmese_meaning:'မင်္ဂလာပါ',example_sentence:'Hello!',independent_reviews:{english:{reviewed_at:42}}}]}],
 ['malformed gate date',{entries:[],release_gates:{physical_iphone_safari:{passed:true,checked_at:42}}}],
 ['fabricated approvals',{release_status:'independently_approved',approved_manifest_sha256:'0'.repeat(64),entries:[{id:'fabricated',level:'A1',release_approved:true,editorial_hold:false}]}]
];
let failures=0;
try{
 for(let i=0;i<cases.length;i++){
  const [label,fixture]=cases[i];
  const file=path.join(tmp,'fixture-'+i+'.json');
  fs.writeFileSync(file,JSON.stringify(fixture));
  const r=spawnSync(process.execPath,[guard,file],{encoding:'utf8',timeout:15000});
  const output=(r.stdout||'')+'\n'+(r.stderr||'');
  const blocked=r.status===1&&output.includes('RELEASE BLOCKED');
  const clean=!/TypeError:|ReferenceError:|SyntaxError:|at Object\.<anonymous>/.test(output);
  if(!blocked||!clean){
   failures++;
   console.error('FAIL '+label+' exit='+r.status+'\n'+output.slice(0,600));
  }else console.log('PASS fail-closed: '+label);
 }
}finally{fs.rmSync(tmp,{recursive:true,force:true});}
assert.equal(failures,0,failures+' adversarial cases failed');
console.log('All '+cases.length+' negative fixtures rejected cleanly; this does not establish release readiness.');
