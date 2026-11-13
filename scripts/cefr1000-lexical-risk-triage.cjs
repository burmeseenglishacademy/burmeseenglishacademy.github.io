#!/usr/bin/env node
// Read-only lexical-risk triage for the 1,000-entry provisional shortlist.
// Heuristics produce REVIEW CANDIDATES, never CEFR evidence or independent approval.
const fs=require('node:fs');
const path=require('node:path');
const file=process.argv[2]||path.join(__dirname,'../draft/CEFR-1000-PROVISIONAL-SHORTLIST.json');
const levels=['A1','A2','B1','B2','C1'];
let doc;
try {doc=JSON.parse(fs.readFileSync(file,'utf8'));}
catch(e){console.error('BLOCKED: '+e.message);process.exit(1);}
const entries=doc.entries;
if(!Array.isArray(entries)||entries.length!==1000){console.error('BLOCKED: expected 1,000 entries');process.exit(1);}
const counts=Object.fromEntries(levels.map(l=>[l,{entries:0,first_pass_complete:0,independently_approved:0,missing_cefr_source:0,risks:0}]));
const risks=[],seen=new Map(),errors=[];
const norm=s=>String(s||'').normalize('NFKC').trim().toLocaleLowerCase('en');
function flag(i,e,code,detail){risks.push({index:i,level:e.level,word:e.word,part_of_speech:e.part_of_speech,code,detail,source_path:e.source_path,source_index:e.source_index,source_blob_sha:e.source_blob_sha});counts[e.level].risks++;}
for(const [i,e] of entries.entries()){
 if(!e||!levels.includes(e.level)){errors.push('Invalid level or entry at '+i);continue;}
 const c=counts[e.level];c.entries++;
 if(['word','part_of_speech','english_definition','burmese_meaning','example_sentence'].every(k=>typeof e[k]==='string'&&e[k].trim()))c.first_pass_complete++;
 if(e.release_approved===true||Object.keys(e).some(k=>k.startsWith('reviewed_')&&e[k]===true))errors.push('Unexpected approval flag at '+i);
 if(e.editorial_hold!==true)errors.push('Missing editorial hold at '+i);
 if(!e.source_level)c.missing_cefr_source++;
 if(!/^[a-f0-9]{40}$/.test(e.source_blob_sha||'')||!e.source_path||!Number.isInteger(e.source_index))flag(i,e,'PROVENANCE_INCOMPLETE','Check historical source path/index/blob SHA');
 const key=norm(e.word)+'|'+norm(e.part_of_speech);
 if(seen.has(key))flag(i,e,'DUPLICATE_HEADWORD_POS','Compare exact lexical sense with entry '+seen.get(key));
 else seen.set(key,i);
 if(typeof e.word==='string'&&e.word==='i'&&e.part_of_speech==='pronoun')flag(i,e,'ENGLISH_ORTHOGRAPHY','Standalone pronoun I requires uppercase display');
 if(typeof e.burmese_meaning==='string'&&!/[\u1000-\u109f]/u.test(e.burmese_meaning))flag(i,e,'MYANMAR_SCRIPT_ABSENT','Check whether Myanmar meaning is genuine Burmese');
 if(typeof e.example_sentence==='string'){
   if(!/[.!?]["']?\s*$/.test(e.example_sentence))flag(i,e,'EXAMPLE_PUNCTUATION','Example lacks sentence-ending punctuation');
   if(/\s{2,}/.test(e.example_sentence))flag(i,e,'EXAMPLE_SPACING','Repeated whitespace');
 }
 if(typeof e.word==='string'&&/^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$/.test(e.word)&&!['I'].includes(e.word))flag(i,e,'POSSIBLE_NAMED_ENTITY','Verify common lexical item rather than a proper name');
}
for(const l of levels)if(counts[l].entries!==200)errors.push(l+' count not 200');
const output={scope:'CEFR-1000 provisional lexical triage, staging only',status:errors.length?'STRUCTURAL_FAILURE':'EDITORIAL_HOLD_NOT_RELEASE_READY',input:file,counts,risks,errors,method:'Automated surface heuristics; no external CEFR verification, no Myanmar fluency signoff, no independent approval. All flags are review candidates.',release_allowed:false};
console.log(JSON.stringify(output,null,2));
process.exit(errors.length?1:0);
