#!/usr/bin/env node
'use strict';
// Fail-closed release gate. This is a staging-only readiness checker; it never deploys.
// All evidence files must be independently produced and traceable, not self-attested.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
// The root override is used only by the synthetic adversarial test fixture.
const root=process.env.CEFR1000_GATE_ROOT?path.resolve(process.env.CEFR1000_GATE_ROOT):path.resolve(__dirname,'..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const levels=['A1','A2','B1','B2','C1'];
const errors=[];
const check=(condition,message)=>{if(!condition)errors.push(message)};
const manifestPath='draft/CEFR-1000-APPROVED-RELEASE-MANIFEST.json';
const evidencePath='draft/CEFR-1000-INDEPENDENT-RELEASE-EVIDENCE.json';
const shortlist=read('draft/CEFR-1000-PROVISIONAL-SHORTLIST.json');
const tasks=read('draft/CEFR-1000-INDEPENDENT-REVIEW-TASKS.json');
const exists=p=>fs.existsSync(path.join(root,p));
check(shortlist.entries.length===1000,'provisional inventory must contain 1000');
check(tasks.tasks.length===1000,'independent task inventory must contain 1000');
for(const level of levels){
 check(shortlist.entries.filter(e=>e.level===level).length===200,level+' provisional inventory != 200');
 check(tasks.tasks.filter(t=>t.level===level).length===200,level+' review task inventory != 200');
}
check(exists(manifestPath),'missing independently approved release manifest');
check(exists(evidencePath),'missing independent evidence register');
if(exists(manifestPath)&&exists(evidencePath)){
 try{
  const m=read(manifestPath),ev=read(evidencePath);
  const entries=Array.isArray(m.entries)?m.entries:[];
  check(m.scope==='CEFR-1000 ONLY','approved manifest scope mismatch');
  check(entries.length===1000,'approved manifest must contain exactly 1000 entries');
  const unique=new Set(),tasksById=new Map(tasks.tasks.map(t=>[t.task_id,t]));
  const manifestIds=new Set(),sourceByHeadword=new Map(shortlist.entries.map(e=>[String(e.word).normalize('NFKC').trim().toLocaleLowerCase('en'),e]));
  check(sourceByHeadword.size===1000,'source shortlist contains duplicate or empty headwords');
  check(tasksById.size===1000,'duplicate review task IDs in source inventory');
  for(const e of entries){
   const key=String(e.headword||'').normalize('NFKC').trim().toLocaleLowerCase('en');
   check(key.length>0,'empty approved headword');
   check(!unique.has(key),'duplicate approved headword '+key);unique.add(key);
   check(levels.includes(e.level),'invalid approved level '+e.level);
   check(typeof e.task_id==='string'&&!manifestIds.has(e.task_id),'duplicate or missing manifest task ID '+e.task_id);
   manifestIds.add(e.task_id);
   const t=tasksById.get(e.task_id);
   check(!!t&&t.level===e.level&&t.headword===e.headword,'missing/mismatched original review task '+e.task_id);
   const original=sourceByHeadword.get(key);
   check(!!original&&original.level===e.level&&original.part_of_speech===e.part_of_speech,'approved entry does not match original shortlist identity '+e.task_id);
   check(!!t&&!!original&&t.source_path===original.source_path&&t.source_index===original.source_index&&t.source_blob_sha===original.source_blob_sha,'original task provenance mismatch '+e.task_id);
   check(!!original&&original.editorial_hold===true&&original.release_approved===false,'source shortlist editorial hold unexpectedly changed '+e.task_id);
   for(const field of ['part_of_speech','english_definition','myanmar_meaning','example_sentence','exact_sense','reviewer_id','reviewer_signed_at','source_observed_on','source_url','source_excerpt_reference']){
    check(typeof e[field]==='string'&&e[field].trim().length>0,'missing '+field+' for '+e.task_id);
   }
   check(typeof e.source_url==='string'&&/^https:\/\//.test(e.source_url),'non-HTTPS CEFR source '+e.task_id);
   check(e.independent_english_review===true&&e.independent_myanmar_review===true&&e.independent_example_review===true&&e.independent_cefr_review===true,'incomplete independent review '+e.task_id);
   check(e.reviewer_id!==e.author_id&&!!e.author_id,'reviewer must differ from author '+e.task_id);
  }
  for(const level of levels)check(entries.filter(e=>e.level===level).length===200,'approved '+level+' != 200');
  check(manifestIds.size===tasksById.size&&[...tasksById.keys()].every(id=>manifestIds.has(id)),'approved manifest must cover each original task exactly once');
  const required=['george_headword','emma_headword','george_example','emma_example'];
  const audio=ev.audio||{};
  const manifestByTask=new Map(entries.map(e=>[e.task_id,e]));
  const audioPaths=new Set(); // Each voice/utterance slot needs its own file.
  const audioDigests=new Set(); // Distinct files must also contain distinct audio bytes globally.
  const supportedFormats=new Set(['mp3','wav','ogg','flac']);
  const hasAudioSignature=(buffer,format)=>{
   if(format==='mp3')return buffer.length>=3&&(buffer.subarray(0,3).toString()==='ID3'||(buffer[0]===0xff&&(buffer[1]&0xe0)===0xe0));
   if(format==='wav')return buffer.length>=12&&buffer.subarray(0,4).toString()==='RIFF'&&buffer.subarray(8,12).toString()==='WAVE';
   if(format==='ogg')return buffer.length>=4&&buffer.subarray(0,4).toString()==='OggS';
   if(format==='flac')return buffer.length>=4&&buffer.subarray(0,4).toString()==='fLaC';
   return false;
  };
  for(const kind of required){
   const records=Array.isArray(audio[kind])?audio[kind]:[];
   check(records.length===1000,kind+' must contain 1000 audio records');
   const ids=new Set();
   for(const r of records){
    check(!!r.task_id&&!ids.has(r.task_id)&&manifestIds.has(r.task_id),'duplicate/unknown/missing audio task id '+kind+' '+r.task_id);ids.add(r.task_id);
    const approved=manifestByTask.get(r.task_id);
    const expectedText=approved?(kind.endsWith('_headword')?approved.headword:approved.example_sentence):null;
    check(typeof r.spoken_text==='string'&&r.spoken_text===expectedText,'audio spoken text mismatch '+kind+' '+r.task_id);
    const safePath=typeof r.path==='string'&&/^draft\/[a-zA-Z0-9_./-]+$/.test(r.path)&&!r.path.split('/').includes('..')&&path.resolve(root,r.path).startsWith(path.resolve(root,'draft')+path.sep);
    check(safePath&&exists(r.path),'missing or unsafe staging audio file '+kind+' '+r.task_id);
    if(safePath){
     check(!audioPaths.has(r.path),'audio file reused across voice/utterance slots '+r.path);
     audioPaths.add(r.path);
    }
    if(safePath&&exists(r.path)&&typeof r.sha256==='string'&&/^[a-f0-9]{64}$/.test(r.sha256)){
     const stat=fs.lstatSync(path.join(root,r.path));
     check(stat.isFile()&&!stat.isSymbolicLink()&&stat.size>0,'empty, non-regular or symlinked audio '+kind+' '+r.task_id);
     if(stat.isFile()&&!stat.isSymbolicLink()){
      const bytes=fs.readFileSync(path.join(root,r.path));
      const digest=crypto.createHash('sha256').update(bytes).digest('hex');
      check(digest===r.sha256,'audio checksum mismatch '+kind+' '+r.task_id);
      check(!audioDigests.has(digest),'audio content digest reused across all voice/utterance slots '+kind+' '+r.task_id);
      audioDigests.add(digest);
      const format=typeof r.format==='string'?r.format.toLowerCase():'';
      const extension=path.extname(r.path).slice(1).toLowerCase();
      check(supportedFormats.has(format)&&format===extension&&hasAudioSignature(bytes,format),'unrecognised audio format/signature '+kind+' '+r.task_id);
     }
    }else check(false,'missing audio checksum '+kind+' '+r.task_id);
    check(r.listened===true&&typeof r.listener_id==='string'&&!!r.listener_id.trim()&&typeof r.listened_at==='string'&&!Number.isNaN(Date.parse(r.listened_at))&&typeof r.listening_evidence_url==='string'&&/^https:\/\//.test(r.listening_evidence_url),'traceable listening signoff missing '+kind+' '+r.task_id);
    check(typeof r.generator_provenance_url==='string'&&/^https:\/\//.test(r.generator_provenance_url)&&r.voice_id===(kind.startsWith('george')?'George':'Emma')&&r.locale==='en-GB','British voice and generation provenance missing '+kind+' '+r.task_id);
   }
   check(ids.size===manifestIds.size&&[...manifestIds].every(id=>ids.has(id)),kind+' audio must cover each approved task exactly once');
  }
  for(const gate of ['desktop_browser_regression','mobile_browser_regression','physical_iphone_safari','github_pages_limits','protected_54_lessons','protected_ielts_bank','protected_production_audio','privacy','production_deployment']){
   const g=ev[gate];
   check(!!g&&g.passed===true&&typeof g.evidence_url==='string'&&/^https:\/\//.test(g.evidence_url)&&typeof g.checked_at==='string'&&!!g.checked_at&&typeof g.reviewer_id==='string'&&!!g.reviewer_id,'missing externally evidenced '+gate);
  }
  check(typeof ev.production_commit_sha==='string'&&/^[a-f0-9]{40}$/.test(ev.production_commit_sha),'missing verified production commit');
 }catch(err){errors.push('cannot validate release evidence: '+err.message)}
}
const report={scope:'CEFR-1000 ONLY',release:errors.length?'BLOCKED':'EVIDENCE_SCHEMA_CHECK_PASSED_NOT_DEPLOYMENT_AUTHORIZATION',provisional_by_level:Object.fromEntries(levels.map(l=>[l,shortlist.entries.filter(e=>e.level===l).length])),independent_approvals_claimed_by_provisional:Object.fromEntries(levels.map(l=>[l,shortlist.independently_approved_by_level[l]])),blockers:errors};
console.log(JSON.stringify(report,null,2));
if(errors.length)process.exitCode=1;
