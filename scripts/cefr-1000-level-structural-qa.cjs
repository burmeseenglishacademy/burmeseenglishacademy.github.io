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
const normalize=x=>String(x).normalize('NFKC').trim().toLocaleLowerCase('en');
const key=(l,w,p)=>[l,normalize(w),normalize(p)].join('|');
// Global inventory is validated by every matrix job: one level cannot hide an
// overfilled or unknown level elsewhere in the manifest.
for(const l of levels){
 assert.equal(shortlist.entries.filter(e=>e.level===l).length,200,'Actual shortlist count '+l);
 assert.equal(review.tasks.filter(t=>t.level===l).length,200,'Actual task count '+l);
}
assert.ok(shortlist.entries.every(e=>levels.includes(e.level)),'Unknown shortlist CEFR level');
assert.ok(review.tasks.every(t=>levels.includes(t.level)),'Unknown review-task CEFR level');
assert.equal(new Set(review.tasks.map(t=>t.task_id)).size,1000,'Globally duplicated task IDs');
const entries=shortlist.entries.filter(e=>e.level===level);
const tasks=review.tasks.filter(t=>t.level===level);
assert.equal(entries.length,200,level+' must have 200 entries');
assert.equal(tasks.length,200,level+' must have 200 review tasks');
assert.equal(shortlist.counts_by_level[level],200);
assert.equal(review.counts_by_level[level],200);
assert.equal(shortlist.independently_approved_by_level[level],0,'Do not infer independent approval');
assert.equal(review.independently_approved_by_level[level],0,'Do not infer independent approval');
const seen=new Set();
for(const e of entries){
 for(const f of ['word','part_of_speech','english_definition','burmese_meaning','example_sentence','source_path','source_blob_sha'])
  assert.ok(typeof e[f]==='string'&&e[f].trim(),level+' missing '+f);
 assert.ok(Number.isSafeInteger(e.source_index)&&e.source_index>=0,'Invalid source index');
 assert.match(e.source_blob_sha,/^[a-f0-9]{40}$/,'Invalid source blob SHA');
 assert.ok(!/[\u0000-\u001f\u007f]/u.test(e.word),'Control character in headword');
 const k=key(e.level,e.word,e.part_of_speech);
 assert.ok(!seen.has(k),'Duplicate provisional level/headword/POS: '+k);
 seen.add(k);
 assert.equal(e.editorial_hold,true,'Entry must remain on editorial hold: '+k);
 assert.equal(e.release_approved,false,'Unverified release flag: '+k);
 for(const f of ['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'])
  assert.equal(e[f],false,'Unverified reviewer flag: '+k+' '+f);
}
const ids=new Set(), targets=new Set();
for(const t of tasks){
 assert.ok(typeof t.task_id==='string'&&t.task_id.startsWith('CEFR1000-'+level+'-'),'Malformed task ID');
 assert.ok(!ids.has(t.task_id),'Duplicate task ID '+t.task_id);
 ids.add(t.task_id);
 const k=key(t.level,t.headword,t.part_of_speech);
 assert.ok(seen.has(k),'Orphan task '+k);
 assert.ok(!targets.has(k),'Duplicate task target '+k);
 targets.add(k);
 assert.equal(t.shortlist_blob_sha,review.source_shortlist_blob_sha,'Mismatched task shortlist provenance');
 assert.equal(t.source_path,entries.find(e=>key(e.level,e.word,e.part_of_speech)===k).source_path,'Task source path mismatch');
 assert.equal(t.source_index,entries.find(e=>key(e.level,e.word,e.part_of_speech)===k).source_index,'Task source index mismatch');
 assert.equal(t.source_blob_sha,entries.find(e=>key(e.level,e.word,e.part_of_speech)===k).source_blob_sha,'Task source blob mismatch');
 assert.equal(t.approval,false,'Task cannot self-approve');
 for(const f of ['reviewer_identity','reviewer_signed_at','source_observed_on','reviewer_assigned'])
  assert.equal(t[f],null,'Unverified independent reviewer metadata: '+k+' '+f);
 for(const f of ['english_definition_review','myanmar_meaning_review','original_example_review','exact_sense_cefr_review','pronunciation_review'])
  assert.equal(t[f],'PENDING','Review decision cannot be self-declared: '+k+' '+f);
 assert.equal(t.review_status,'PENDING_INDEPENDENT_REVIEW','Task must remain pending until genuine independent evidence');
 assert.deepEqual(t.source_evidence_urls,[],'Source evidence must not be invented');
}
assert.equal(targets.size,seen.size,'Unmatched provisional entries');
// This deliberately does not claim independent source-backed sense validation.
// Editorial holds and zero approval are mandatory until external review exists.
console.log(JSON.stringify({level,provisional_written:entries.length,review_tasks:tasks.length,independently_verified:0,release:'BLOCKED',scope:'STRUCTURAL_ONLY_NOT_APPROVAL'}));
