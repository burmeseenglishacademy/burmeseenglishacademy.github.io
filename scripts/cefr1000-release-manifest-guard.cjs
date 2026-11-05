#!/usr/bin/env node
/**
 * CEFR-1000 release manifest guard (staging). Node 18+, no dependencies.
 * Usage: node scripts/cefr1000-release-manifest-guard.cjs path/to/manifest.json
 * Intentionally FAIL CLOSED when manifest or evidence is missing.
 * Does not certify human review, audio listening, physical device testing, or deployment.
 */
'use strict';
const fs=require('node:fs');
const crypto=require('node:crypto');
const nodePath=require('node:path');
const levels=['A1','A2','B1','B2','C1'];
const failures=[];
function fail(s){failures.push(s);}
function text(v){return typeof v==='string'&&v.trim().length>0;}
function sha(v){return typeof v==='string'&&/^[a-f0-9]{64}$/i.test(v);}
function datePart(v){return typeof v==='string'?v.slice(0,10):null;}
function date(v){if(typeof v!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(v))return false;const d=new Date(v+'T00:00:00Z');return !Number.isNaN(d.getTime())&&d.toISOString().slice(0,10)===v&&v<=new Date().toISOString().slice(0,10);}
function url(v){if(!text(v))return false;try{const u=new URL(v);return u.protocol==='https:'&&u.hostname.includes('.')&&!/^(github\.com|raw\.githubusercontent\.com)$/i.test(u.hostname);}catch{return false;}}
function distinctReview(r,kind,entryId){
 if(!r||typeof r!=='object')return fail(entryId+': missing '+kind+' independent review');
 if(!text(r.reviewer_id)||!date(datePart(r.reviewed_at))||!text(r.author_id)||r.decision!=='approved'||r.independent!==true||r.reviewer_id===r.author_id||!url(r.evidence_url))
   fail(entryId+': invalid '+kind+' independent review attestation');
}
function audioCheck(a,kind,entryId,expectedText,manifestHash){
 if(!a||typeof a!=='object')return fail(entryId+': missing '+kind+' audio');
 if(!text(a.path)||!sha(a.sha256)||a.text!==expectedText||a.manifest_sha256!==manifestHash)
   fail(entryId+': audio identity/hash mismatch for '+kind);
 if(text(a.path)){
   const root=nodePath.resolve(process.cwd());
   const resolved=nodePath.resolve(root,a.path);
   let safe=false;
   try{safe=resolved.startsWith(root+nodePath.sep)&&fs.statSync(resolved).isFile()&&fs.realpathSync(resolved).startsWith(fs.realpathSync(root)+nodePath.sep);}catch{}
   if(!safe)fail(entryId+': audio file missing or unsafe path for '+kind);
   else if(crypto.createHash('sha256').update(fs.readFileSync(resolved)).digest('hex').toLowerCase()!==a.sha256.toLowerCase())fail(entryId+': actual audio bytes SHA256 mismatch for '+kind);
 }
 const l=a.listening;
 if(!l||l.passed!==true||!text(l.listener_id)||!date(datePart(l.listened_at))||!text(l.device)||!url(l.evidence_url)||l.audio_sha256!==a.sha256)
   fail(entryId+': no bound real-listening attestation for '+kind);
}
const path=process.argv[2];
if(!path){console.error('Usage: node scripts/cefr1000-release-manifest-guard.cjs MANIFEST.json');process.exit(2);}
let m;
try{m=JSON.parse(fs.readFileSync(path,'utf8'));}catch(e){console.error('BLOCKED: missing/unreadable manifest: '+e.message);process.exit(1);}
if(!m||typeof m!=='object'||!Array.isArray(m.entries))fail('manifest entries missing');
if(!sha(m?.approved_manifest_sha256))fail('approved manifest SHA256 missing');
// Bind the approval digest to the canonical entry payload, not an arbitrary 64-hex string.
if(Array.isArray(m?.entries)){
 const actual=crypto.createHash('sha256').update(JSON.stringify(m.entries)).digest('hex');
 if(m.approved_manifest_sha256!==actual)fail('approved manifest digest does not match canonical JSON entries');
}
if(!text(m?.shortlist_git_blob_sha)||!/^[a-f0-9]{40}$/i.test(m.shortlist_git_blob_sha))fail('shortlist provenance missing');
if(m?.release_status!=='independently_approved')fail('manifest release status not independently approved');
const entries=Array.isArray(m?.entries)?m.entries:[];
if(entries.length!==1000)fail('expected exactly 1000 entries; observed '+entries.length);
const counts=Object.fromEntries(levels.map(l=>[l,0]));
const seen=new Set(), audioPaths=new Set();
for(const [i,e] of entries.entries()){
 const id=e?.id||'entry['+i+']';
 if(!levels.includes(e?.level)){fail(id+': invalid level');continue;}
 counts[e.level]++;
 for(const field of ['word','part_of_speech','sense_id','english_definition','burmese_meaning','example_sentence'])
   if(!text(e[field]))fail(id+': missing '+field);
 const key=String(e?.word||'').normalize('NFKC').trim().toLocaleLowerCase('en')+'|'+String(e?.part_of_speech||'').trim().toLowerCase()+'|'+String(e?.sense_id||'').trim();
 if(seen.has(key))fail(id+': duplicate headword/POS/sense across levels');seen.add(key);
 if(e?.editorial_hold!==false||e?.release_approved!==true)fail(id+': editorial hold or missing approval');
 for(const kind of ['english','myanmar','example','cefr','pronunciation'])distinctReview(e?.independent_reviews?.[kind],kind,id);
 // These are five separate review tasks, not five aliases of a single attestation.
 const reviewEvidence=new Set();
 for(const kind of ['english','myanmar','example','cefr','pronunciation']){
   const review=e?.independent_reviews?.[kind];
   if(text(review?.evidence_url)){
     if(reviewEvidence.has(review.evidence_url))fail(id+': reused independent review evidence URL');
     reviewEvidence.add(review.evidence_url);
   }
 }
 const ev=e?.cefr_evidence;
 if(!ev||!url(ev.publisher_url)||!date(ev.observed_on)||!text(ev.publisher_sense_id)||ev.level!==e.level||ev.sense_id!==e.sense_id||!text(ev.level_evidence_excerpt)||!text(ev.publisher_name))
   fail(id+': publisher exact-sense CEFR evidence missing or unbound');
 for(const voice of ['George','Emma'])for(const type of ['headword','example']){
   const kind=voice+'_'+type, a=e?.audio?.[kind];
   audioCheck(a,kind,id,type==='headword'?e.word:e.example_sentence,m.approved_manifest_sha256);
   if(text(a?.path)){if(audioPaths.has(a.path))fail(id+': reused audio path '+a.path);audioPaths.add(a.path);}
 }
}
for(const l of levels)if(counts[l]!==200)fail(l+': expected 200; observed '+counts[l]);
if(audioPaths.size!==4000)fail('expected 4000 distinct audio paths; observed '+audioPaths.size);
const gates=m?.release_gates;
for(const k of ['browser_regression','mobile_regression','physical_iphone_safari','github_pages_hosting','production_asset_preservation','confirmed_production_deployment']){
 const g=gates?.[k];
 if(!g||g.passed!==true||!url(g.evidence_url)||!date(datePart(g.checked_at))||!text(g.reviewer_id))fail('missing release gate '+k);
}
if(failures.length){
 console.error('RELEASE BLOCKED ('+failures.length+' findings):\n'+failures.slice(0,30).join('\n')+(failures.length>30?'\n...remaining omitted':''));
 process.exit(1);
}
console.log('STRUCTURAL GATE PASS: 200 per CEFR level, 1000 distinct senses, 4000 audio references and required attestations present. Independently verify all evidence before release.');
