#!/usr/bin/env node
// Read-only CEFR-1000 provisional inventory audit. Never promotes or approves entries.
// Usage: node scripts/cefr1000-provisional-audit.cjs [path-to-shortlist]
const fs=require('node:fs');
const path=require('node:path');
const file=process.argv[2]||path.join(__dirname,'../draft/CEFR-1000-PROVISIONAL-SHORTLIST.json');
const levels=['A1','A2','B1','B2','C1'];
let data;
try {data=JSON.parse(fs.readFileSync(file,'utf8'));}
catch(err){console.error('BLOCKED: unreadable shortlist: '+err.message);process.exit(1);}
const errors=[],warnings=[];
const entries=Array.isArray(data.entries)?data.entries:[];
if(entries.length!==1000) errors.push('Expected 1000 entries, found '+entries.length);
const counts={},written={},approved={},held={},missingSources={},seen=new Map();
for(const level of levels){counts[level]=0;written[level]=0;approved[level]=0;held[level]=0;missingSources[level]=0;}
const norm=s=>String(s||'').normalize('NFKC').trim().toLocaleLowerCase('en');
for(const [i,e] of entries.entries()){
 if(!e||typeof e!=='object'){errors.push('Invalid entry at '+i);continue;}
 const level=e.level;
 if(!levels.includes(level)){errors.push('Unknown level at '+i+': '+level);continue;}
 counts[level]++;
 const required=['word','part_of_speech','english_definition','burmese_meaning','example_sentence'];
 if(required.every(k=>typeof e[k]==='string'&&e[k].trim())) written[level]++;
 else errors.push(level+' index '+i+': missing first-pass field');
 const key=norm(e.word)+'|'+norm(e.part_of_speech);
 if(seen.has(key)) warnings.push('Repeated headword/POS (sense adjudication required): '+key+' at '+seen.get(key)+' and '+i);
 else seen.set(key,i);
 if(e.release_approved===true||Object.keys(e).some(k=>k.startsWith('reviewed_')&&e[k]===true)) approved[level]++;
 if(e.editorial_hold===true) held[level]++;
 else errors.push(level+' index '+i+': editorial hold not true');
 if(!e.source_english||!e.source_burmese||!e.source_level) missingSources[level]++;
 if(!e.source_path||!Number.isInteger(e.source_index)||!e.source_blob_sha)
  warnings.push(level+' index '+i+': incomplete historical provenance');
}
for(const level of levels){
 if(counts[level]!==200)errors.push(level+': expected 200, found '+counts[level]);
 if(approved[level]!==0)errors.push(level+': provisional inventory unexpectedly contains approval flags');
 if(held[level]!==200)errors.push(level+': expected 200 editorial holds');
}
if(data.release_status!=='PROVISIONAL_1000_INDEPENDENT_EVIDENCE_MISSING_DO_NOT_PUBLISH')
 errors.push('Provisional do-not-publish release status missing or changed');
const report={status:errors.length?'STRUCTURAL_FAILURE':'PROVISIONAL_ONLY_NOT_RELEASE_READY',file,
 counts_by_level:counts,first_pass_written_by_level:written,entries_with_any_review_or_release_flag_by_level:approved,
 editorial_hold_by_level:held,missing_one_or_more_source_fields_by_level:missingSources,
 independent_approved_by_level:Object.fromEntries(levels.map(l=>[l,0])),
 note:'Independent approval is NOT inferred from this script. Zero is the required provisional baseline, not a verified review registry.',
 errors,warnings:warnings.slice(0,100),warning_count:warnings.length};
console.log(JSON.stringify(report,null,2));
process.exit(errors.length?1:0);
