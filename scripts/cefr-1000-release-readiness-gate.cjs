#!/usr/bin/env node
'use strict';
// Fail-closed release gate. This is a staging-only readiness checker; it never deploys.
// All evidence files must be independently produced and traceable, not self-attested.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..');
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
  for(const e of entries){
   const key=String(e.headword||'').normalize('NFKC').trim().toLocaleLowerCase('en');
   check(key.length>0,'empty approved headword');
   check(!unique.has(key),'duplicate approved headword '+key);unique.add(key);
   check(levels.includes(e.level),'invalid approved level '+e.level);
   const t=tasksById.get(e.task_id);
   check(!!t&&t.level===e.level&&t.headword===e.headword,'missing/mismatched original review task '+e.task_id);
   for(const field of ['part_of_speech','english_definition','myanmar_meaning','example_sentence','exact_sense','reviewer_id','reviewer_signed_at','source_observed_on','source_url','source_excerpt_reference']){
    check(typeof e[field]==='string'&&e[field].trim().length>0,'missing '+field+' for '+e.task_id);
   }
   check(typeof e.source_url==='string'&&/^https:\/\//.test(e.source_url),'non-HTTPS CEFR source '+e.task_id);
   check(e.independent_english_review===true&&e.independent_myanmar_review===true&&e.independent_example_review===true&&e.independent_cefr_review===true,'incomplete independent review '+e.task_id);
   check(e.reviewer_id!==e.author_id&&!!e.author_id,'reviewer must differ from author '+e.task_id);
  }
  for(const level of levels)check(entries.filter(e=>e.level===level).length===200,'approved '+level+' != 200');
  const required=['george_headword','emma_headword','george_example','emma_example'];
  const audio=ev.audio||{};
  for(const kind of required){
   const records=Array.isArray(audio[kind])?audio[kind]:[];
   check(records.length===1000,kind+' must contain 1000 audio records');
   const ids=new Set();
   for(const r of records){
    check(!!r.task_id&&!ids.has(r.task_id),'duplicate/missing audio task id '+kind);ids.add(r.task_id);
    check(typeof r.path==='string'&&r.path.startsWith('draft/')&&!r.path.includes('..')&&exists(r.path),'missing staging audio file '+kind+' '+r.task_id);
    if(typeof r.path==='string'&&exists(r.path)&&typeof r.sha256==='string'){
     const digest=crypto.createHash('sha256').update(fs.readFileSync(path.join(root,r.path))).digest('hex');
     check(digest===r.sha256,'audio checksum mismatch '+kind+' '+r.task_id);
    }else check(false,'missing audio checksum '+kind+' '+r.task_id);
    check(r.listened===true&&typeof r.listener_id==='string'&&!!r.listener_id&&typeof r.listened_at==='string'&&!!r.listened_at,'real listening signoff missing '+kind+' '+r.task_id);
   }
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
