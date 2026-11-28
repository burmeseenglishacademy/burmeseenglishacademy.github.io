#!/usr/bin/env node
'use strict';
// Synthetic schema/adversarial tests only. These fixture bytes and reviewer URLs
// are never written to the repository's release evidence or production assets.
const assert=require('node:assert/strict');
const crypto=require('node:crypto');
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const {spawnSync}=require('node:child_process');

const repoRoot=path.resolve(__dirname,'..');
const gatePath=path.join(__dirname,'cefr-1000-release-readiness-gate.cjs');
const tempRoot=fs.mkdtempSync(path.join(os.tmpdir(),'cefr1000-release-gate-'));
const draft=path.join(tempRoot,'draft');
fs.mkdirSync(draft,{recursive:true});
const shortlist=JSON.parse(fs.readFileSync(path.join(repoRoot,'draft/CEFR-1000-PROVISIONAL-SHORTLIST.json'),'utf8'));
const tasks=JSON.parse(fs.readFileSync(path.join(repoRoot,'draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json'),'utf8'));
fs.writeFileSync(path.join(draft,'CEFR-1000-PROVISIONAL-SHORTLIST.json'),JSON.stringify(shortlist));
fs.writeFileSync(path.join(draft,'CEFR-1000-INDEPENDENT-REVIEW-TASKS.json'),JSON.stringify(tasks));

const manifest={
 scope:'CEFR-1000 ONLY',
 entries:shortlist.entries.map((source,index)=>{
  const task=tasks.tasks[index];
  return {
   headword:source.word,level:source.level,task_id:task.task_id,part_of_speech:source.part_of_speech,
   english_definition:source.english_definition,myanmar_meaning:source.burmese_meaning,
   example_sentence:source.example_sentence,exact_sense:'Synthetic fixture sense for '+source.word,
   reviewer_id:'fixture-independent-reviewer',author_id:'fixture-original-author',
   reviewer_signed_at:'2026-11-28T08:00:00Z',source_observed_on:'2026-11-28',
   source_url:'https://fixture.invalid/source/'+encodeURIComponent(source.word),
   source_excerpt_reference:'synthetic fixture excerpt '+index,
   independent_english_review:true,independent_myanmar_review:true,
   independent_example_review:true,independent_cefr_review:true
  };
 })
};
fs.writeFileSync(path.join(draft,'CEFR-1000-APPROVED-RELEASE-MANIFEST.json'),JSON.stringify(manifest));

const kinds=['george_headword','emma_headword','george_example','emma_example'];
const audio={};
for(const kind of kinds){
 const voice=kind.startsWith('george')?'George':'Emma';
 const textField=kind.endsWith('_headword')?'headword':'example_sentence';
 audio[kind]=manifest.entries.map(entry=>{
  const relative='draft/audio/'+kind+'/'+entry.task_id+'.mp3';
  const absolute=path.join(tempRoot,relative);
  fs.mkdirSync(path.dirname(absolute),{recursive:true});
  const bytes=Buffer.from('ID3 synthetic fixture only '+kind+' '+entry.task_id);
  fs.writeFileSync(absolute,bytes);
  return {
   task_id:entry.task_id,path:relative,format:'mp3',sha256:crypto.createHash('sha256').update(bytes).digest('hex'),
   spoken_text:entry[textField],listened:true,listener_id:'fixture-listener',
   listened_at:'2026-11-28T08:00:00Z',listening_evidence_url:'https://fixture.invalid/listening/'+kind+'/'+entry.task_id,
   generator_provenance_url:'https://fixture.invalid/generation/'+kind+'/'+entry.task_id,
   voice_id:voice,locale:'en-GB'
  };
 });
}
const gates=['desktop_browser_regression','mobile_browser_regression','physical_iphone_safari',
 'github_pages_limits','protected_54_lessons','protected_ielts_bank',
 'protected_production_audio','privacy','production_deployment'];
const evidence={audio,production_commit_sha:'a'.repeat(40)};
for(const gate of gates)evidence[gate]={
 passed:true,evidence_url:'https://fixture.invalid/evidence/'+gate,
 checked_at:'2026-11-28T08:00:00Z',reviewer_id:'fixture-independent-reviewer'
};
const evidencePath=path.join(draft,'CEFR-1000-INDEPENDENT-RELEASE-EVIDENCE.json');
const writeEvidence=()=>fs.writeFileSync(evidencePath,JSON.stringify(evidence));
writeEvidence();

function runGate(){
 const result=spawnSync(process.execPath,[gatePath],{
  cwd:repoRoot,encoding:'utf8',
  env:{...process.env,CEFR1000_GATE_ROOT:tempRoot}
 });
 assert.equal(result.stderr,'','Release gate emitted unexpected stderr');
 const report=JSON.parse(result.stdout);
 return {status:result.status,report};
}
try{
 const baseline=runGate();
 assert.equal(baseline.status,0,'Synthetic complete schema fixture should pass schema validation');
 assert.equal(baseline.report.release,'EVIDENCE_SCHEMA_CHECK_PASSED_NOT_DEPLOYMENT_AUTHORIZATION');
 console.log('PASS: complete synthetic fixture satisfies evidence schema only (not deployment authorization)');

 const first=evidence.audio.george_headword[0];
 first.spoken_text='wrong spoken item';
 writeEvidence();
 const wrongText=runGate();
 assert.equal(wrongText.status,1,'Wrong audio transcript must be rejected');
 assert.ok(wrongText.report.blockers.some(x=>x.includes('audio spoken text mismatch george_headword')));
 console.log('PASS: audio that does not speak the approved headword is rejected');

 evidence.audio.george_headword[0].spoken_text=manifest.entries[0].headword;
 const duplicateA=evidence.audio.george_headword[0];
 const duplicateB=evidence.audio.george_headword[1];
 const bytesA=fs.readFileSync(path.join(tempRoot,duplicateA.path));
 fs.writeFileSync(path.join(tempRoot,duplicateB.path),bytesA);
 duplicateB.sha256=duplicateA.sha256;
 writeEvidence();
 const duplicate=runGate();
 assert.equal(duplicate.status,1,'Identical audio bytes in different slots must be rejected');
 assert.ok(duplicate.report.blockers.some(x=>x.includes('audio content digest reused across all voice/utterance slots')));
 console.log('PASS: duplicate audio content across different tasks is rejected');

 fs.writeFileSync(path.join(tempRoot,duplicateA.path),Buffer.from('not an audio file'));
 duplicateA.sha256=crypto.createHash('sha256').update(fs.readFileSync(path.join(tempRoot,duplicateA.path))).digest('hex');
 writeEvidence();
 const badFormat=runGate();
 assert.equal(badFormat.status,1,'Invalid audio file signature must be rejected');
 assert.ok(badFormat.report.blockers.some(x=>x.includes('unrecognised audio format/signature')));
 console.log('PASS: invalid audio format/signature is rejected');
 console.log('All release-gate audio evidence tests passed; no real review or audio evidence was created.');
}finally{
 fs.rmSync(tempRoot,{recursive:true,force:true});
}
