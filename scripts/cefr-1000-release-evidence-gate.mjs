#!/usr/bin/env node
// CEFR-1000 staging-only release gate. Never writes approval or publishes.
// Evidence must be supplied by independent reviewers and real-device/audio testers.
import { readFileSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
const levels=['A1','A2','B1','B2','C1'], voices=['George','Emma'], kinds=['headword','example'];
const inventoryPath='draft/CEFR-1000-PROVISIONAL-SHORTLIST.json';
const evidencePath='draft/CEFR-1000-RELEASE-EVIDENCE.json';
const failures=[];
const read=p=>JSON.parse(readFileSync(p,'utf8'));
const inventory=read(inventoryPath);
const entries=inventory.entries;
if(!Array.isArray(entries)) throw Error('Invalid inventory entries');
const sha=s=>createHash('sha256').update(s).digest('hex');
const inventoryHash=sha(readFileSync(inventoryPath));
const nonempty=s=>typeof s==='string'&&s.trim().length>0;
const https=s=>{try{const u=new URL(s);return u.protocol==='https:'&&!!u.hostname&&!['example.com','example.org','example.net'].includes(u.hostname)}catch{return false}};
const dated=s=>typeof s==='string'&&/^\\d{4}-\\d{2}-\\d{2}T/.test(s)&&Number.isFinite(Date.parse(s))&&Date.parse(s)<=Date.now();
const fileHash=p=>{try{if(!nonempty(p)||p.startsWith('/')||p.includes('..')||!existsSync(p))return null;return sha(readFileSync(p))}catch{return null}};
const approved=e=>e.release_approved===true && ['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'].every(k=>e[k]===true);
const key=e=>[e.level,String(e.word??'').normalize('NFKC').trim().toLowerCase(),String(e.part_of_speech??'').trim().toLowerCase(),String(e.english_definition??'').normalize('NFKC').trim().toLowerCase()].join('|');
const perLevel={};
for(const level of levels){
 const subset=entries.filter(e=>e?.level===level);
 perLevel[level]={written:subset.length,independently_checked:0,approved:subset.filter(approved).length};
 if(subset.length!==200) failures.push(level+': expected 200 entries');
 if(new Set(subset.map(key)).size!==subset.length) failures.push(level+': duplicate exact senses');
}
if(entries.length!==1000) failures.push('Expected exactly 1000 entries');
if(entries.some(e=>!levels.includes(e?.level))) failures.push('Unknown level');
if(new Set(entries.map(key)).size!==1000) failures.push('Duplicate exact sense across levels');
if(inventory.release_status!=='APPROVED_FOR_RELEASE') failures.push('Inventory release status not approved');
if(!existsSync(evidencePath)) failures.push('Missing independent release evidence manifest: '+evidencePath);
else {
 const evidence=read(evidencePath);
 if(evidence.inventory_sha256!==inventoryHash) failures.push('Evidence bound to wrong inventory hash');
 if(!Array.isArray(evidence.entry_reviews)) failures.push('Missing entry_reviews array');
 else {
  const seen=new Set();
  for(const review of evidence.entry_reviews){
   if(!nonempty(review.entry_key)||seen.has(review.entry_key)){failures.push('Duplicate/empty entry review key');continue;}
   seen.add(review.entry_key);
   const entry=entries.find(e=>key(e)===review.entry_key);
   if(!entry){failures.push('Review refers to unknown entry');continue;}
   const checks=['english','myanmar','example','cefr','pronunciation'];
   if(!nonempty(review.source_cefr_url)||!https(review.source_cefr_url)||!dated(review.source_observed_at)) failures.push('Missing dated publisher CEFR evidence: '+review.entry_key);
   if(!checks.every(c=>review[c]?.reviewer_id!==review.author_id && review[c]?.reviewer_id!==review.generator_id)) failures.push('Reviewer not distinct from content author/generator: '+review.entry_key);
   if(!checks.every(c=>nonempty(review[c]?.reviewer_id)&&dated(review[c]?.signed_at)&&https(review[c]?.evidence_url)&&review[c]?.decision==='approved')) failures.push('Incomplete independent review: '+review.entry_key);
   else perLevel[entry.level].independently_checked++;
   if(!approved(entry)) failures.push('Inventory approval flags missing: '+review.entry_key);
  }
  if(seen.size!==1000) failures.push('Expected 1000 independently reviewed entry keys');
 }
 const audio=evidence.audio;
 if(!Array.isArray(audio)) failures.push('Missing audio attestations');
 else {
  const audioKeys=new Set();
  for(const a of audio){
   const k=[a.entry_key,a.voice,a.kind].join('|');
   if(audioKeys.has(k)) failures.push('Duplicate audio attestation: '+k);
   audioKeys.add(k);
   if(!entries.some(e=>key(e)===a.entry_key)||!voices.includes(a.voice)||!kinds.includes(a.kind)||!nonempty(a.file_path)||!/^([a-f0-9]{64})$/i.test(a.file_sha256??'')||fileHash(a.file_path)!==a.file_sha256?.toLowerCase()||!nonempty(a.listener_id)||!dated(a.listened_at)||a.listener_id===a.generator_id||a.listening_decision!=='pass') failures.push('Invalid audio/listening attestation: '+k);
  }
  if(audioKeys.size!==4000) failures.push('Expected 4000 distinct George/Emma headword/example listening attestations');
 }
 for(const gate of ['browser_regression','mobile_regression','physical_iphone_safari','github_pages_hosting','production_deployment','production_asset_preservation']){
  const v=evidence.gates?.[gate];
  if(v?.decision!=='pass'||!nonempty(v?.tester_id)||!dated(v?.tested_at)||!https(v?.evidence_url)) failures.push('Missing evidenced gate: '+gate);
 }
}
for(const level of levels) if(perLevel[level].independently_checked!==200||perLevel[level].approved!==200) failures.push(level+': independent review/approval count below 200');
console.log(JSON.stringify({kind:'CEFR-1000 release readiness, not self-approval',inventory_sha256:inventoryHash,per_level:perLevel,release_ready:failures.length===0,blockers:failures.slice(0,50),blocker_count:failures.length},null,2));
if(failures.length) process.exitCode=1;
