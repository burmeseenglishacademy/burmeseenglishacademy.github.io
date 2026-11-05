#!/usr/bin/env node
'use strict';
// Fail-closed smoke tests: these fixtures must NEVER be accepted as a release.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const {spawnSync}=require('node:child_process');
const guard=path.resolve(__dirname,'cefr1000-release-manifest-guard.cjs');
const dir=fs.mkdtempSync(path.join(os.tmpdir(),'bea-cefr-guard-'));
const fixtures=[
 ['missing entries',{}],
 ['empty provisional inventory',{entries:[],release_status:'independently_approved'}],
 ['forged approved status',{entries:Array.from({length:1000},(_,i)=>({id:String(i),level:['A1','A2','B1','B2','C1'][Math.floor(i/200)],word:'word'+i,part_of_speech:'noun',sense_id:'s1',editorial_hold:false,release_approved:true})),release_status:'independently_approved'}],
 ['invalid level',{entries:[{level:'C2'}]}]
];
try{
 for(const [name,fixture] of fixtures){
  const file=path.join(dir,name.replace(/\W+/g,'-')+'.json');
  fs.writeFileSync(file,JSON.stringify(fixture));
  const run=spawnSync(process.execPath,[guard,file],{encoding:'utf8',timeout:30000,maxBuffer:4*1024*1024});
  assert.equal(run.status,1,name+' must fail closed; status='+run.status+' stderr='+run.stderr?.slice(0,500));
  assert.match(run.stderr,/RELEASE BLOCKED|BLOCKED/,name+' must explain its rejection');
  console.log('PASS (correctly blocked): '+name);
 }
 const missing=spawnSync(process.execPath,[guard,path.join(dir,'does-not-exist.json')],{encoding:'utf8'});
 assert.equal(missing.status,1,'missing manifest must fail');
 console.log('PASS (correctly blocked): missing manifest');
}finally{fs.rmSync(dir,{recursive:true,force:true});}
