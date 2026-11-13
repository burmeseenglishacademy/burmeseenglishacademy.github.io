#!/usr/bin/env node
// Negative regression tests for the CEFR-1000 release gate. No approval data is modified.
const {spawnSync}=require('node:child_process');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const assert=require('node:assert/strict');
const gate=path.join(__dirname,'cefr1000-release-gate.cjs');
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'cefr1000-negative-'));
const levels=['A1','A2','B1','B2','C1'];
function run(label,manifest,expect) {
 const p=path.join(temp,'fixture.json');
 fs.writeFileSync(p,JSON.stringify(manifest));
 const result=spawnSync(process.execPath,[gate,p],{encoding:'utf8',maxBuffer:8*1024*1024});
 assert.equal(result.status,1,label+': must fail closed');
 const output=JSON.parse(result.stdout);
 assert.equal(output.result,'BLOCKED',label);
 if(expect) assert.ok([...output.blockers,...(output.structural_blockers||[])].some(b=>b.includes(expect)),label+': expected blocker '+expect);
 console.log('PASS (blocked as intended): '+label+'; '+output.blocker_count+' blockers');
}
try {
 run('missing entries',{},'entries array missing');
 run('empty inventory',{entries:[]},'expected exactly 1000');
 const entries=levels.flatMap(level=>Array.from({length:200},(_,i)=>({
   word:level.toLowerCase()+'_'+i,level,part_of_speech:'noun',sense_id:'sense_1',
   english_definition:'Placeholder definition',burmese_meaning:'စမ်းသပ်မှု',
   example_sentence:'This is a test.',editorial_hold:true,release_approved:false
 })));
 const baseline={entries};
 run('exactly 200 per level but no independent evidence',baseline,'editorial hold/approval not cleared');
 const dup=structuredClone(baseline);
 dup.entries[1].word=dup.entries[0].word;
 run('duplicate lexical sense',dup,'duplicate lexical sense');
 const wrong=structuredClone(baseline);
 wrong.entries[0].level='C2';
 run('unknown level',wrong,'unknown CEFR level');
 const short=structuredClone(baseline);
 short.entries.pop();
 run('missing one C1 item',short,'C1: expected 200');
 const forged=structuredClone(baseline);
 forged.entries[0].editorial_hold=false;
 forged.entries[0].release_approved=true;
 for(const f of ['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation']) forged.entries[0][f]=true;
 run('approval booleans without independent signatures',forged,'independently signed english evidence absent');
 const fakeSource=structuredClone(baseline);
 fakeSource.entries[0].cefr_sources=[{url:'http://invalid.example',observed_on:'2026-11-13',exact_sense:'noun',level:'A1'}];
 run('non-HTTPS CEFR evidence',fakeSource,'source-backed exact-sense CEFR evidence absent');
 console.log('All 8 negative release-gate regression scenarios blocked.');
} finally {fs.rmSync(temp,{recursive:true,force:true});}
