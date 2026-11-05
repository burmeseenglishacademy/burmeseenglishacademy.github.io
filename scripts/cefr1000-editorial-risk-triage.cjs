'use strict';
// Staging-only editorial triage. Heuristics identify work; they NEVER verify CEFR or language quality.
const fs=require('node:fs');
const data=JSON.parse(fs.readFileSync('draft/CEFR-1000-PROVISIONAL-SHORTLIST.json','utf8'));
const levels=['A1','A2','B1','B2','C1'];
const counts=Object.fromEntries(levels.map(l=>[l,{written:0,independently_checked:0,risks:0}]));
const findings=[];
const headwordOwners=new Map();
const normalizeHeadword=w=>String(w||'').normalize('NFKC').trim().toLowerCase().replace(/\s+/g,' ');
const tokens=s=>String(s||'').toLowerCase().match(/[a-z]+(?:'[a-z]+)?/g)||[];

function flag(e,i,code,detail) {
  findings.push({index:i,level:e.level,headword:e.word,code,detail,source_path:e.source_path,source_index:e.source_index,source_blob_sha:e.source_blob_sha});
  counts[e.level].risks++;
}
for(const [i,e] of data.entries.entries()){
  if(!counts[e.level]) throw Error('Unknown level at '+i);
  counts[e.level].written++;
  const canonical=normalizeHeadword(e.word);
  if(!canonical) flag(e,i,'EMPTY_HEADWORD','Missing lexical headword');
  else {
    const previous=headwordOwners.get(canonical);
    if(previous) flag(e,i,'CROSS_LEVEL_HEADWORD_CONFLICT',
      'Same normalized headword at index '+previous.index+' ('+previous.level+'); check exact sense and POS');
    else headwordOwners.set(canonical,{index:i,level:e.level});
  }
  if(!e.part_of_speech || !String(e.english_definition||'').trim() ||
     !String(e.burmese_meaning||'').trim() || !String(e.example_sentence||'').trim())
    flag(e,i,'INCOMPLETE_LEXICAL_ENTRY','Check POS, English definition, Myanmar meaning and example');
  const lemma=tokens(e.word);
  const example=tokens(e.example_sentence);
  if(lemma.length===1 && lemma[0].length>2 &&
     !example.some(t=>t===lemma[0] || t===lemma[0]+'s' ||
       t===lemma[0]+'ed' || t===lemma[0]+'ing'))
    flag(e,i,'HEADWORD_NOT_OBVIOUS_IN_EXAMPLE',
      'Check irregular inflection or example sense; heuristic may be a false positive');

  // Never count self-assessment or an unverified boolean as independent approval.
  if(e.release_approved || e.reviewed_level || e.reviewed_burmese || e.reviewed_english || e.reviewed_example)
    flag(e,i,'UNSUPPORTED_REVIEW_CLAIM','Review flags require separate independently authenticated evidence');
  if(!e.source_level || !e.source_english || !e.source_burmese)
    flag(e,i,'NO_EXACT_SENSE_SOURCE_ATTESTATION','Collect publisher URL, sense/POS, CEFR observation date and independent bilingual evidence');
  if(/wordnet|wn[0-9]|synset/i.test([e.source_path,e.english_definition,e.status].join(' ')))
    flag(e,i,'WORDNET_PROVENANCE_REVIEW','Historical WordNet-derived content is not publisher CEFR evidence');
  if(/^[A-Z][a-z]+(?: [A-Z][a-z]+)*$/.test(e.word) || /(?:inc\.|ltd\.|university|city|country)/i.test(e.word))
    flag(e,i,'POSSIBLE_NAMED_ENTITY','Check common lexical headword versus proper name');
  if(!/[.!?][”"']?$/.test(String(e.example_sentence||'').trim()))
    flag(e,i,'EXAMPLE_PUNCTUATION','Check original example grammar and sentence completeness');
  if(/\b(?:something|someone|somebody|thing|person)\b/i.test(e.english_definition))
    flag(e,i,'GENERIC_DEFINITION','Check sense specificity and bilingual alignment manually');
}
const output={
  schema:1,kind:'PROVISIONAL_EDITORIAL_TRIAGE_NOT_INDEPENDENT_REVIEW',
  generated_on:new Date().toISOString(),branch_expected:'cefr-5000-bilingual-qa-staging',
  per_level:counts,findings,
  required_independent_evidence:['publisher_url','publisher_observed_on','headword','part_of_speech','exact_sense','source_CEFR_level','english_reviewer','myanmar_reviewer','example_reviewer','independent_signoff_provenance'],
  caveat:'Heuristics may yield false positives and false negatives; zero findings does not mean approved.'
};
process.stdout.write(JSON.stringify(output,null,2)+'\n');
