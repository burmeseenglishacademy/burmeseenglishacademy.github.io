#!/usr/bin/env node
// Staging-only read-only review queue. Heuristics are NOT CEFR evidence or signoff.
const fs=require('node:fs');
const path=require('node:path');
const input=process.argv[2]||path.join(__dirname,'../draft/CEFR-1000-PROVISIONAL-SHORTLIST.json');
let doc;
try{doc=JSON.parse(fs.readFileSync(input,'utf8'));}catch(e){console.error('BLOCKED: '+e.message);process.exit(1);}
const levels=['A1','A2','B1','B2','C1'];
const errors=[],queue=[],seenExamples=new Map(),seenHeadwords=new Map();
const counts=Object.fromEntries(levels.map(x=>[x,{written:0,independently_approved:0,source_backed_cefr:0,review_candidates:0}]));
if(!Array.isArray(doc.entries)||doc.entries.length!==1000)errors.push('Expected exactly 1000 entries');
for(const l of levels){
 if(doc.scope_target?.[l]!==200||doc.counts_by_level?.[l]!==200)errors.push('Declared inventory mismatch '+l);
 if(doc.independently_approved_by_level?.[l]!==0)errors.push('Unverified independent approval metadata '+l);
}
if(!doc.stages||doc.stages.independent_source_evidence!=='NOT_OBSERVED'||doc.stages.production!=='UNMODIFIED')errors.push('Unverified evidence or production stage metadata');
if(doc.stages?.audio!=='NOT_GENERATED_FOR_FINAL_SHORTLIST_NOT_LISTENED')errors.push('Unverified audio/listening stage metadata');
for(const [index,e] of (doc.entries||[]).entries()){
 if(!e||!levels.includes(e.level)){errors.push('Invalid entry/level '+index);continue;}
 const c=counts[e.level];
 if(['word','part_of_speech','english_definition','burmese_meaning','example_sentence'].every(k=>typeof e[k]==='string'&&e[k].trim()))c.written++;
 if(e.editorial_hold!==true||e.release_approved!==false||['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'].some(k=>e[k]!==false)||Object.keys(e).some(k=>k.startsWith('reviewed_')&&!['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'].includes(k)))errors.push('Unexpected release/review state '+index);
 if(!['word','part_of_speech','english_definition','burmese_meaning','example_sentence'].every(k=>typeof e[k]==='string'&&e[k].trim()))errors.push('Missing required first-pass field '+index);
 const flag=(code,detail)=>{queue.push({index,level:e.level,word:e.word,code,detail,source_path:e.source_path,source_index:e.source_index,source_blob_sha:e.source_blob_sha});c.review_candidates++;};
 const head=String(e.word||'').normalize('NFKC').toLowerCase().trim();
 const example=String(e.example_sentence||'').normalize('NFKC').toLowerCase().replace(/\s+/g,' ').trim();
 if(seenHeadwords.has(head))flag('CROSS_LEVEL_HEADWORD','Compare sense and level with index '+seenHeadwords.get(head));else seenHeadwords.set(head,index);
 if(seenExamples.has(example))flag('REUSED_EXAMPLE','Compare original example with index '+seenExamples.get(example));else seenExamples.set(example,index);
 if(head==='i'&&e.part_of_speech==='pronoun')flag('PRONOUN_CASE','Standalone English pronoun must display as I');
 if(!/[.!?][”"']?$/.test(String(e.example_sentence||'').trim()))flag('SENTENCE_END','Check sentence punctuation');
 if(!/[\u1000-\u109f]/u.test(String(e.burmese_meaning||'')))flag('MYANMAR_SCRIPT','Meaning lacks Myanmar script');
 if(!e.source_level)flag('CEFR_EVIDENCE_MISSING','No entry-specific independently verified exact-sense CEFR source; do not infer level');
 if(!e.source_english||!e.source_burmese)flag('LINGUISTIC_SOURCE_MISSING','English/Myanmar source provenance missing');
}
for(const l of levels)if((doc.entries||[]).filter(e=>e&&e.level===l).length!==200)errors.push('Count mismatch '+l);
if(doc.release_status!=='PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH')errors.push('Provisional do-not-publish marker missing');
const result={status:errors.length?'STRUCTURAL_FAILURE':'EDITORIAL_HOLD_NOT_RELEASE_READY',input,counts,errors,queue,release_allowed:false,limitations:'Automated surface triage only; no independent review, no source-backed CEFR approval, no audio listening or device testing.'};
console.log(JSON.stringify(result,null,2));process.exit(errors.length?1:0);
