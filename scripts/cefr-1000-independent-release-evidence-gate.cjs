#!/usr/bin/env node
// CEFR-1000 staging-only independent evidence intake gate.
// This is a *release* gate, not a provisional shortlist structural check.
// Fail closed: no self-attestation, no inferred signoff, no bypass flag.
const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const load = name => JSON.parse(fs.readFileSync(path.join(root,'draft',name),'utf8'));
const shortlist = load('CEFR-1000-PROVISIONAL-SHORTLIST.json');
const intake = load('CEFR-1000-INDEPENDENT-REVIEW-TASKS.json');
const levels = ['A1','A2','B1','B2','C1'];
const problems = [];
const fail = (id, why) => problems.push(id+': '+why);
const entries = shortlist.entries || [];
const tasks = intake.tasks || [];
const key = (level,word,pos) => [level,String(word).normalize('NFKC').toLocaleLowerCase('en'),String(pos).normalize('NFKC').toLocaleLowerCase('en')].join('|');
if (entries.length!==1000) fail('shortlist','expected exactly 1000 entries');
if (tasks.length!==1000) fail('tasks','expected exactly 1000 review tasks');
if (intake.source_shortlist_blob_sha !== '475e68ae17ab97bd937e73e5ce4794e0dcd76551') fail('provenance','review tasks not tied to the known source shortlist blob; revalidate provenance before changing this pin');
const nonemptyEntry = x => typeof x === 'string' && x.trim().length > 0;
const seen = new Set();
const globalHeadwords = new Map();
const entryKeys = new Set();
for (const level of levels) {
 const es=entries.filter(x=>x.level===level), ts=tasks.filter(x=>x.level===level);
 if(es.length!==200) fail(level,'shortlist count '+es.length+' != 200');
 if(ts.length!==200) fail(level,'review-task count '+ts.length+' != 200');
}
for (const e of entries) {
 if(!levels.includes(e.level) || !nonemptyEntry(e.word) || !nonemptyEntry(e.part_of_speech) || !nonemptyEntry(e.english_definition) || !nonemptyEntry(e.burmese_meaning) || !nonemptyEntry(e.example_sentence)) fail('entry','missing required first-pass fields or unknown CEFR level');
 const k=key(e.level,e.word,e.part_of_speech);
 entryKeys.add(k);
 const normalizedWord=String(e.word).normalize('NFKC').toLocaleLowerCase('en').trim();
 if(globalHeadwords.has(normalizedWord)) fail(k,'cross-level headword recurrence: independently distinguish exact senses before any release; earlier '+globalHeadwords.get(normalizedWord));
 else globalHeadwords.set(normalizedWord,e.level);
 if(seen.has(k)) fail(k,'duplicate normalized level/headword/POS; exact-sense duplicates also require independent semantic review');
 seen.add(k);
}
const taskIds=new Set(), taskKeys=new Set();
const nonempty = x=>typeof x==='string' && x.trim().length>0;
const reviewed = x=>x==='APPROVED' || x==='PASS';
const validObservationDate = x => { if(typeof x!=='string' || !/^\d{4}-\d{2}-\d{2}$/.test(x)) return false; const d=new Date(x+'T00:00:00Z'); return !Number.isNaN(d.valueOf()) && d.toISOString().slice(0,10)===x && d.valueOf()<=Date.now(); };
for (const t of tasks) {
 const id=t.task_id || '(missing-id)';
 if(taskIds.has(id)) fail(id,'duplicate task ID');
 taskIds.add(id);
 const k=key(t.level,t.headword,t.part_of_speech);
 if(taskKeys.has(k)) fail(id,'duplicate review target');
 taskKeys.add(k);
 if(!seen.has(k)) fail(id,'task does not map to a provisional entry');
 if(t.review_status!=='INDEPENDENTLY_APPROVED' || t.approval!==true) {fail(id,'not independently approved');continue;}
 if(!nonempty(t.reviewer_identity) || !nonempty(t.reviewer_signed_at) || !nonempty(t.reviewer_assigned)) fail(id,'missing independently attributable reviewer and timestamp');
 for(const field of ['english_definition_review','myanmar_meaning_review','original_example_review','exact_sense_cefr_review','pronunciation_review']) if(!reviewed(t[field])) fail(id,'missing independent '+field);
 if(!Array.isArray(t.source_evidence_urls)||!t.source_evidence_urls.length||!t.source_evidence_urls.every(x=>typeof x==='string' && /^https:\/\//.test(x))) fail(id,'missing valid source URL evidence');
 if(!validObservationDate(t.source_observed_on)) fail(id,'missing, invalid, or future source observation date');
}
for(const k of entryKeys) if(!taskKeys.has(k)) fail(k,'provisional entry has no matching independent-review task');
// Reviewer identity fields alone cannot prove reviewer independence or source/sense validity.
// These MUST be verified against signed external evidence, never inferred by this script.
const externalGates = ['independent_reviewer_identity_and_signatures','source_sense_cefr_review','george_emma_headword_and_example_audio_files','george_emma_real_listening_signoff','browser_mobile_regression','physical_iphone_safari_evidence','github_pages_hosting_clearance','production_asset_preservation','confirmed_production_deployment'];
for(const gate of externalGates) fail('external:'+gate,'independent evidence not machine-verifiable from the provisional JSON; requires separately authenticated evidence');
const summary={status:'BLOCKED',scope:'CEFR-1000 ONLY',written:Object.fromEntries(levels.map(l=>[l,entries.filter(e=>e.level===l).length])),independently_verified:Object.fromEntries(levels.map(l=>[l,0])),claimed_independent_approvals_unverified:Object.fromEntries(levels.map(l=>[l,tasks.filter(t=>t.level===l&&t.approval===true&&t.review_status==='INDEPENDENTLY_APPROVED').length])),blocker_count:problems.length,blocker_samples:problems.slice(0,12),note:'Claimed approvals are NOT independently verified. No automatic approval or deployment. This guard intentionally cannot pass without externally authenticated release gates.'};
console.log(JSON.stringify(summary,null,2));
process.exitCode=1;
