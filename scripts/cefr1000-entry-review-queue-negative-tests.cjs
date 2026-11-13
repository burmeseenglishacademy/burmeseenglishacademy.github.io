#!/usr/bin/env node
// Staging-only mutation tests: never modify the real shortlist.
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const cp=require('node:child_process');
const assert=require('node:assert/strict');
const input=path.join(__dirname,'../draft/CEFR-1000-PROVISIONAL-SHORTLIST.json');
const script=path.join(__dirname,'cefr1000-entry-review-queue.cjs');
const baseline=JSON.parse(fs.readFileSync(input,'utf8'));
const dir=fs.mkdtempSync(path.join(os.tmpdir(),'cefr1000-queue-negative-'));
function run(mutator){
 const doc=structuredClone(baseline);
 mutator(doc);
 const file=path.join(dir,'fixture.json');
 fs.writeFileSync(file,JSON.stringify(doc));
 const p=cp.spawnSync(process.execPath,[script,file],{encoding:'utf8'});
 assert.ok(p.stdout,'Queue must return machine-readable JSON');
 return {code:p.status,report:JSON.parse(p.stdout)};
}
try{
 const ok=run(()=>{});
 assert.equal(ok.code,0);
 assert.equal(ok.report.status,'EDITORIAL_HOLD_NOT_RELEASE_READY');
 assert.equal(ok.report.release_allowed,false);
 for(const level of ['A1','A2','B1','B2','C1']){
  assert.equal(ok.report.counts[level].written,200);
  assert.equal(ok.report.counts[level].independently_approved,0);
 }
 const cases=[
  ['editorial hold removed',d=>{d.entries[999].editorial_hold=false;}],
  ['self approval inserted',d=>{d.entries[999].reviewed_level=true;}],
  ['release approval inserted',d=>{d.entries[999].release_approved=true;}],
  ['shortlist truncated',d=>{d.entries.pop();}],
  ['level moved',d=>{d.entries[999].level='A1';}],
  ['release status falsified',d=>{d.release_status='READY';}]
 ];
 for(const [name,change] of cases){
  const r=run(change);
  assert.notEqual(r.code,0,name+' must fail');
  assert.equal(r.report.status,'STRUCTURAL_FAILURE',name);
  assert.equal(r.report.release_allowed,false,name);
  assert.ok(r.report.errors.length,name+' must explain failure');
  console.log('PASS: '+name+' blocked');
 }
 const surface=run(d=>{d.entries[999].burmese_meaning='English only';});
 assert.equal(surface.code,0);
 assert.equal(surface.report.release_allowed,false);
 assert.ok(surface.report.queue.some(q=>q.index===999&&q.code==='MYANMAR_SCRIPT'));
 console.log('PASS: missing Myanmar script surfaced without false independent signoff');
 console.log('PASS: all editorial queue negative tests; production untouched');
}finally{fs.rmSync(dir,{recursive:true,force:true});}
