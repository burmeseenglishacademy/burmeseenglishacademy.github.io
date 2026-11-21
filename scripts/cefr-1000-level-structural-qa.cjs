#!/usr/bin/env node
// Structural staging QA only. Passing this test is NOT CEFR or independent approval.
'use strict';
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const root=path.resolve(__dirname,'..');
const load=f=>JSON.parse(fs.readFileSync(path.join(root,'draft',f),'utf8'));
const shortlist=load('CEFR-1000-PROVISIONAL-SHORTLIST.json');
const review=load('CEFR-1000-INDEPENDENT-REVIEW-TASKS.json');
const levels=['A1','A2','B1','B2','C1'];
const level=process.env.CEFR_LEVEL;
assert.ok(levels.includes(level),'CEFR_LEVEL must be one of A1 A2 B1 B2 C1');
assert.equal(shortlist.entries.length,1000,'Total shortlist inventory');
assert.equal(review.tasks.length,1000,'Total review task inventory');
assert.equal(review.source_shortlist_blob_sha,'475e68ae17ab97bd937e73e5ce4794e0dcd76551','Pinned shortlist provenance');
assert.equal(shortlist.release_status,'PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH','Shortlist release hold');
assert.equal(review.release_status,'ALL_PENDING_NOT_INDEPENDENTLY_REVIEWED_DO_NOT_PUBLISH','Review release hold');
assert.equal(review.scope,'CEFR-1000 ONLY','Reject superseded 5000-word scope');
assert.equal(shortlist.stages.audio,'NOT_GENERATED_FOR_FINAL_SHORTLIST_NOT_LISTENED','Audio evidence cannot be presumed');
assert.equal(shortlist.stages.production,'UNMODIFIED','Production must remain untouched');
const normalize=x=>String(x).normalize('NFKC').trim().toLocaleLowerCase('en');
const key=(l,w,p)=>[l,normalize(w),normalize(p)].join('|');
// Global inventory is validated by every matrix job: one level cannot hide an
// overfilled or unknown level elsewhere in the manifest.
for(const l of levels){
 assert.equal(shortlist.entries.filter(e=>e.level===l).length,200,'Actual shortlist count '+l);
 assert.equal(review.tasks.filter(t=>t.level===l).length,200,'Actual task count '+l);
 assert.equal(shortlist.scope_target[l],200,'Declared scope '+l);
 assert.equal(shortlist.counts_by_level[l],200,'Declared shortlist count '+l);
 assert.equal(review.counts_by_level[l],200,'Declared review count '+l);
 assert.equal(shortlist.independently_approved_by_level[l],0,'No independently approved shortlist '+l);
 assert.equal(review.independently_approved_by_level[l],0,'No independently approved review tasks '+l);
}
assert.ok(shortlist.entries.every(e=>levels.includes(e.level)),'Unknown shortlist CEFR level');
assert.ok(review.tasks.every(t=>levels.includes(t.level)),'Unknown review-task CEFR level');
assert.equal(new Set(review.tasks.map(t=>t.task_id)).size,1000,'Globally duplicated task IDs');
// The approved 1,000-word scope requires globally deduplicated headwords.
// Check across all five levels, not merely within a matrix job's level.
const globalHeadwords=new Map();
for(const e of shortlist.entries){
 assert.ok(typeof e.word==='string'&&e.word.trim(),'Missing global headword');
 const normalized=normalize(e.word);
 assert.ok(!globalHeadwords.has(normalized),
  'Cross-level duplicate headword '+normalized+' ('+globalHeadwords.get(normalized)+' / '+e.level+')');
 globalHeadwords.set(normalized,e.level);
}
assert.equal(globalHeadwords.size,1000,'Global unique headword count');
const entries=shortlist.entries.filter(e=>e.level===level);
const tasks=review.tasks.filter(t=>t.level===level);
assert.equal(entries.length,200,level+' must have 200 entries');
assert.equal(tasks.length,200,level+' must have 200 review tasks');
assert.equal(shortlist.counts_by_level[level],200);
assert.equal(review.counts_by_level[level],200);
assert.equal(shortlist.independently_approved_by_level[level],0,'Do not infer independent approval');
assert.equal(review.independently_approved_by_level[level],0,'Do not infer independent approval');
// A task's source must point to an internal, version-pinned editorial source,
// never a URL, traversal path or production file.
const safeSource=p=>typeof p==='string'&&/^draft\/[A-Za-z0-9][A-Za-z0-9._/-]*\.json$/.test(p)&&!p.split('/').includes('..')&&!p.split('/').includes('.');
const seen=new Set();
const entryByKey=new Map();
for(const e of entries){
 for(const f of ['word','part_of_speech','english_definition','burmese_meaning','example_sentence','source_path','source_blob_sha'])
  assert.ok(typeof e[f]==='string'&&e[f].trim(),level+' missing '+f);
 assert.ok(Number.isSafeInteger(e.source_index)&&e.source_index>=0,'Invalid source index');
 assert.match(e.source_blob_sha,/^[a-f0-9]{40}$/,'Invalid source blob SHA');
 assert.ok(safeSource(e.source_path),'Unsafe editorial source path');
 assert.ok(!/[\u0000-\u001f\u007f]/u.test(e.word),'Control character in headword');
 const k=key(e.level,e.word,e.part_of_speech);
 assert.ok(!seen.has(k),'Duplicate provisional level/headword/POS: '+k);
 seen.add(k);
 entryByKey.set(k,e);
 assert.equal(e.editorial_hold,true,'Entry must remain on editorial hold: '+k);
 assert.equal(e.release_approved,false,'Unverified release flag: '+k);
 for(const f of ['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'])
  assert.equal(e[f],false,'Unverified reviewer flag: '+k+' '+f);
}
const ids=new Set(), targets=new Set();
// Task IDs use GLOBAL 1–1000 sequence, not 1–200 restarted per level.
const levelOffset=levels.indexOf(level)*200;
const expectedTaskIds=new Set(Array.from({length:200},(_,i)=>'CEFR1000-'+level+'-'+String(levelOffset+i+1).padStart(4,'0')));
for(const t of tasks){
 assert.ok(typeof t.task_id==='string'&&t.task_id.startsWith('CEFR1000-'+level+'-'),'Malformed task ID');
 assert.ok(!ids.has(t.task_id),'Duplicate task ID '+t.task_id);
 ids.add(t.task_id);
 assert.ok(expectedTaskIds.has(t.task_id),'Unexpected or out-of-range task ID '+t.task_id);
 const k=key(t.level,t.headword,t.part_of_speech);
 assert.ok(seen.has(k),'Orphan task '+k);
 assert.ok(!targets.has(k),'Duplicate task target '+k);
 targets.add(k);
 assert.equal(t.shortlist_blob_sha,review.source_shortlist_blob_sha,'Mismatched task shortlist provenance');
 assert.equal(t.source_path,entryByKey.get(k).source_path,'Task source path mismatch');
 assert.equal(t.source_index,entryByKey.get(k).source_index,'Task source index mismatch');
 assert.equal(t.source_blob_sha,entryByKey.get(k).source_blob_sha,'Task source blob mismatch');
 assert.equal(t.approval,false,'Task cannot self-approve');
 for(const f of ['reviewer_identity','reviewer_signed_at','source_observed_on','reviewer_assigned'])
  assert.equal(t[f],null,'Unverified independent reviewer metadata: '+k+' '+f);
 for(const f of ['english_definition_review','myanmar_meaning_review','original_example_review','exact_sense_cefr_review','pronunciation_review'])
  assert.equal(t[f],'PENDING','Review decision cannot be self-declared: '+k+' '+f);
 assert.equal(t.review_status,'PENDING_INDEPENDENT_REVIEW','Task must remain pending until genuine independent evidence');
 assert.deepEqual(t.source_evidence_urls,[],'Source evidence must not be invented');
}
assert.equal(targets.size,seen.size,'Unmatched provisional entries');
assert.equal(ids.size,expectedTaskIds.size,'Missing sequential review task IDs');
// Enforce canonical task-to-shortlist positional identity, not just a valid set
// of global IDs. Two tasks with exchanged IDs must fail even when all counts,
// headwords, sources and ID ranges remain individually valid.
const levelEntries=shortlist.entries.filter(e=>e.level===level);
const levelTasks=review.tasks.filter(t=>t.level===level);
for(let i=0;i<200;i++){
 const entry=levelEntries[i], task=levelTasks[i];
 const canonicalId='CEFR1000-'+level+'-'+String(levelOffset+i+1).padStart(4,'0');
 assert.equal(task.task_id,canonicalId,'Task ID out of canonical shortlist order at '+level+' index '+i);
 assert.equal(key(task.level,task.headword,task.part_of_speech),
              key(entry.level,entry.word,entry.part_of_speech),
              'Task-to-shortlist positional mismatch at '+level+' index '+i);
}
// This deliberately does not claim independent source-backed sense validation.
// Editorial holds and zero approval are mandatory until external review exists.
console.log(JSON.stringify({level,provisional_written:entries.length,review_tasks:tasks.length,independently_verified:0,release:'BLOCKED',scope:'STRUCTURAL_ONLY_NOT_APPROVAL'}));
