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

const digest=value=>crypto.createHash('sha256').update(value).digest('hex');
const signoff=(dimension,authorId,payload)=>({
 decision:'APPROVED',
 reviewer_id:'fixture-independent-reviewer-'+dimension,
 reviewer_profile_url:'https://fixture.invalid/reviewer/'+dimension,
 qualification_evidence_url:'https://fixture.invalid/qualification/'+dimension,
 evidence_url:'https://fixture.invalid/review/'+dimension,
 signed_at:'2026-11-28T08:00:00Z',
 reviewed_content_sha256:digest(payload)
});
const manifest={
 scope:'CEFR-1000 ONLY',
 entries:shortlist.entries.map((source,index)=>{
  const task=tasks.tasks[index];
  const authorId='fixture-original-author';
  const cefrPayload=JSON.stringify({
   headword:source.word,level:source.level,
   url:'https://fixture.invalid/cefr/'+encodeURIComponent(source.word),
   excerpt:source.word+': CEFR '+source.level+' synthetic exact-sense label',
   reference:'synthetic CEFR excerpt '+index,observed_on:'2026-11-28'
  });
  return {
   headword:source.word,level:source.level,task_id:task.task_id,part_of_speech:source.part_of_speech,
   english_definition:source.english_definition,myanmar_meaning:source.burmese_meaning,
   example_sentence:source.example_sentence,exact_sense:'Synthetic fixture sense for '+source.word,
   reviewer_id:'fixture-independent-reviewer',author_id:authorId,
   reviewer_signed_at:'2026-11-28T08:00:00Z',source_observed_on:'2026-11-28',
   source_url:'https://fixture.invalid/source/'+encodeURIComponent(source.word),
   source_excerpt_reference:'synthetic fixture excerpt '+index,
   source_cefr_level:source.level,
   source_cefr_evidence_excerpt:source.word+': CEFR '+source.level+' synthetic exact-sense label',
   source_cefr_url:'https://fixture.invalid/cefr/'+encodeURIComponent(source.word),
   source_cefr_excerpt_reference:'synthetic CEFR excerpt '+index,
   source_cefr_observed_on:'2026-11-28',
   independent_english_review:true,independent_myanmar_review:true,
   independent_example_review:true,independent_cefr_review:true,
   independent_review_signoffs:{
    english:signoff('english',authorId,source.english_definition),
    myanmar:signoff('myanmar',authorId,source.burmese_meaning),
    example:signoff('example',authorId,source.example_sentence),
    cefr:signoff('cefr',authorId,cefrPayload)
   }
  };
 })
};
const manifestPath=path.join(draft,'CEFR-1000-APPROVED-RELEASE-MANIFEST.json');
const writeManifest=()=>fs.writeFileSync(manifestPath,JSON.stringify(manifest));
writeManifest();

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

 const firstManifestEntry=manifest.entries[0];
 const myanmarSignoff=firstManifestEntry.independent_review_signoffs.myanmar;
 const originalMyanmarReviewer=myanmarSignoff.reviewer_id;
 myanmarSignoff.reviewer_id=firstManifestEntry.author_id;
 writeManifest();writeEvidence();
 const selfMyanmar=runGate();
 assert.equal(selfMyanmar.status,1,'A Myanmar reviewer who is also the author must be rejected');
 assert.ok(selfMyanmar.report.blockers.some(x=>x.includes('independent myanmar reviewer must be identified and differ from author')));
 console.log('PASS: author self-review is rejected for a review dimension');
 myanmarSignoff.reviewer_id=originalMyanmarReviewer;
 writeManifest();

 const exampleSignoff=firstManifestEntry.independent_review_signoffs.example;
 const originalExampleHash=exampleSignoff.reviewed_content_sha256;
 exampleSignoff.reviewed_content_sha256='0'.repeat(64);
 writeManifest();writeEvidence();
 const staleExample=runGate();
 assert.equal(staleExample.status,1,'An independent example signoff bound to stale text must be rejected');
 assert.ok(staleExample.report.blockers.some(x=>x.includes('stale or mismatched independent example content hash')));
 console.log('PASS: review signoff is invalidated when reviewed example text changes');
 exampleSignoff.reviewed_content_sha256=originalExampleHash;
 writeManifest();

 const cefrSignoff=firstManifestEntry.independent_review_signoffs.cefr;
 const originalCefrDecision=cefrSignoff.decision;
 cefrSignoff.decision='PENDING';
 writeManifest();writeEvidence();
 const pendingCefr=runGate();
 assert.equal(pendingCefr.status,1,'A pending CEFR review must be rejected');
 assert.ok(pendingCefr.report.blockers.some(x=>x.includes('missing independent cefr approval')));
 console.log('PASS: pending exact-sense CEFR signoff is rejected');
 cefrSignoff.decision=originalCefrDecision;
 writeManifest();writeEvidence();

 const originalCefrLevel=firstManifestEntry.source_cefr_level;
 firstManifestEntry.source_cefr_level='C2';
 writeManifest();
 writeEvidence();
 const wrongCefrLevel=runGate();
 assert.equal(wrongCefrLevel.status,1,'A CEFR label that differs from the approved level must be rejected');
 assert.ok(wrongCefrLevel.report.blockers.some(x=>x.includes('source-backed CEFR label does not match approved level')));
 console.log('PASS: a source CEFR label that conflicts with the manifest level is rejected');

 firstManifestEntry.source_cefr_level=originalCefrLevel;
 writeManifest();
 const originalCefrExcerpt=firstManifestEntry.source_cefr_evidence_excerpt;
 firstManifestEntry.source_cefr_evidence_excerpt='Generic Oxford word-list landing page; no individual headword level is shown';
 writeManifest();
 writeEvidence();
 const genericCefrSource=runGate();
 assert.equal(genericCefrSource.status,1,'A generic word-list URL without a headword-level excerpt must be rejected');
 assert.ok(genericCefrSource.report.blockers.some(x=>x.includes('CEFR evidence excerpt must identify the headword and exact approved level')));
 console.log('PASS: a generic list reference without an exact headword/level excerpt is rejected');

 firstManifestEntry.source_cefr_evidence_excerpt=originalCefrExcerpt;
 writeManifest();
 writeEvidence();

 const first=evidence.audio.george_headword[0];
 first.spoken_text='wrong spoken item';
 writeEvidence();
 const wrongText=runGate();
 assert.equal(wrongText.status,1,'Wrong audio transcript must be rejected');
 assert.ok(wrongText.report.blockers.some(x=>x.includes('audio spoken text mismatch george_headword')));
 console.log('PASS: audio that does not speak the approved headword is rejected');

 evidence.audio.george_headword[0].spoken_text=manifest.entries[0].headword;

 // The shortlist contains repeated example strings. The same exact text may
 // share one file within one voice, but every task still has its own audio record.
 const duplicateExamples=new Map();
 let duplicateExamplePair=null;
 for(let i=0;i<manifest.entries.length;i++){
  const text=manifest.entries[i].example_sentence;
  if(duplicateExamples.has(text)){duplicateExamplePair=[duplicateExamples.get(text),i];break;}
  duplicateExamples.set(text,i);
 }
 assert.ok(duplicateExamplePair,'The source shortlist should contain repeated example text for reuse testing');
 const [reuseIndexA,reuseIndexB]=duplicateExamplePair;
 const reuseA=evidence.audio.george_example[reuseIndexA];
 const reuseB=evidence.audio.george_example[reuseIndexB];
 const reuseBOriginal={path:reuseB.path,sha256:reuseB.sha256};
 reuseB.path=reuseA.path;
 reuseB.sha256=reuseA.sha256;
 writeEvidence();
 const exactReuse=runGate();
 assert.equal(exactReuse.status,0,'Exact same text and same voice may share one audio asset');
 console.log('PASS: exact same text + same voice may reuse one recording across duplicate slots');
 reuseB.path=reuseBOriginal.path;
 reuseB.sha256=reuseBOriginal.sha256;
 writeEvidence();

 // A path must never be reused for a different spoken text or voice.
 const pathA=evidence.audio.george_headword[0];
 const pathB=evidence.audio.george_headword[1];
 const pathBOriginal={path:pathB.path,sha256:pathB.sha256};
 pathB.path=pathA.path;
 pathB.sha256=pathA.sha256;
 writeEvidence();
 const pathReuse=runGate();
 assert.equal(pathReuse.status,1,'One audio path reused for different text must be rejected');
 assert.ok(pathReuse.report.blockers.some(x=>x.includes('audio file reused across different voice/utterance content')));
 console.log('PASS: one audio path cannot be reused for different spoken content');
 pathB.path=pathBOriginal.path;
 pathB.sha256=pathBOriginal.sha256;
 writeEvidence();

 // Distinct paths with the same bytes are also rejected when their text differs.
 const duplicateA=evidence.audio.george_headword[0];
 const duplicateB=evidence.audio.george_headword[1];
 const duplicateBBytes=fs.readFileSync(path.join(tempRoot,duplicateB.path));
 const duplicateBHash=duplicateB.sha256;
 const bytesA=fs.readFileSync(path.join(tempRoot,duplicateA.path));
 fs.writeFileSync(path.join(tempRoot,duplicateB.path),bytesA);
 duplicateB.sha256=duplicateA.sha256;
 writeEvidence();
 const duplicate=runGate();
 assert.equal(duplicate.status,1,'Identical audio bytes for different spoken text must be rejected');
 assert.ok(duplicate.report.blockers.some(x=>x.includes('audio content digest reused across different spoken text or voice')));
 console.log('PASS: duplicate audio bytes across different spoken text are rejected');
 fs.writeFileSync(path.join(tempRoot,duplicateB.path),duplicateBBytes);
 duplicateB.sha256=duplicateBHash;
 writeEvidence();

 // Even identical text cannot reuse the same recording across George and Emma.
 const george=evidence.audio.george_headword[0];
 const emma=evidence.audio.emma_headword[0];
 const emmaBytes=fs.readFileSync(path.join(tempRoot,emma.path));
 const emmaHash=emma.sha256;
 fs.writeFileSync(path.join(tempRoot,emma.path),fs.readFileSync(path.join(tempRoot,george.path)));
 emma.sha256=george.sha256;
 writeEvidence();
 const crossVoice=runGate();
 assert.equal(crossVoice.status,1,'A George recording reused for Emma must be rejected');
 assert.ok(crossVoice.report.blockers.some(x=>x.includes('audio content digest reused across different spoken text or voice')));
 console.log('PASS: same text still requires the correct George/Emma voice');
 fs.writeFileSync(path.join(tempRoot,emma.path),emmaBytes);
 emma.sha256=emmaHash;
 writeEvidence();

 const first=evidence.audio.george_headword[0];
 const firstBytes=fs.readFileSync(path.join(tempRoot,first.path));
 const firstHash=first.sha256;
 fs.writeFileSync(path.join(tempRoot,first.path),Buffer.from('not an audio file'));
 first.sha256=crypto.createHash('sha256').update(fs.readFileSync(path.join(tempRoot,first.path))).digest('hex');
 writeEvidence();
 const badFormat=runGate();
 assert.equal(badFormat.status,1,'Invalid audio file signature must be rejected');
 assert.ok(badFormat.report.blockers.some(x=>x.includes('unrecognised audio format/signature')));
 console.log('PASS: invalid audio format/signature is rejected');
 fs.writeFileSync(path.join(tempRoot,first.path),firstBytes);
 first.sha256=firstHash;
 writeEvidence();
 console.log('All release-gate audio evidence tests passed; no real review or audio evidence was created.');
}finally{
 fs.rmSync(tempRoot,{recursive:true,force:true});
}
