#!/usr/bin/env node
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const root=path.join(__dirname,'..');
const handlers={};
const played=[];
const els={app:{innerHTML:''},cefrVocabularyPage:{}};
const ctx={
 window:{playSpeech:t=>played.push(t)},
 document:{
  addEventListener:(type,cb)=>handlers[type]=cb,
  getElementById:id=>els[id]||null,
  activeElement:null,
 },
 console,
};
vm.runInNewContext(fs.readFileSync(path.join(root,'cefr-vocabulary.js'),'utf8'),ctx);
const api=ctx.window.BEACefr;
assert.equal(api.ready(),false);
assert.match(api.render(),/undergoing accuracy and audio checks/);
const targets={A1:200,A2:200,B1:200,B2:200,C1:200};
let i=0;
const rows=[];
for(const [level,count] of Object.entries(targets)){
 for(let j=0;j<count;j++){
  const word='word'+String(++i).padStart(4,'0');
  rows.push({word,level,part_of_speech:'noun',english_definition:'A learning term',
    burmese_meaning:'သင်ယူခြင်း',example_sentence:'The '+word+' helps us learn.',
    reviewed_english:true,reviewed_burmese:true,reviewed_example:true,reviewed_level:true,reviewed_pronunciation:true,
    source_english:'https://example.org/english',source_burmese:'https://example.org/burmese',source_level:'https://example.org/levels'});
 }
}
ctx.window.CEFR_VOCAB_BANK={release_status:'VERIFIED_FOR_RELEASE',entries:rows};
const paths={};
for(const row of rows){
 const a={bm_george:'audio/bm_george/'+'a'.repeat(24)+'.mp3',bf_emma:'audio/bf_emma/'+'b'.repeat(24)+'.mp3'};
 paths[row.word]=a;
 paths[row.example_sentence]=a;
}
ctx.window.BEA_AUDIO_MANIFEST={clips:paths};
assert.equal(api.ready(),true);
const originalRows=ctx.window.CEFR_VOCAB_BANK.entries;
ctx.window.CEFR_VOCAB_BANK.entries=originalRows.slice(0,-1);
assert.equal(api.ready(),false,'Missing 1000th entry must block publication');
ctx.window.CEFR_VOCAB_BANK.entries=originalRows;
let html=api.render();
assert.match(html,/1,000 English words/);
assert.match(html,/A1 · 200/);
assert.match(html,/word0001/);
assert.doesNotMatch(html,/word0220/);
let handle=(ds)=>handlers.click({target:{closest:()=>({dataset:ds})}});
handle({cefrLevel:'A2'});
html=api.render();
assert.match(html,/word0201/);
assert.doesNotMatch(html,/word0001/);
handle({cefrSpeak:'200',part:'example'});
assert.equal(played.at(-1),'The word0201 helps us learn.');
rows[200].english_definition='<script>alert(1)</script>';
html=api.render();
assert.ok(!html.includes('<script>alert(1)</script>'));
assert.ok(html.includes('&lt;script&gt;'));
rows[800].burmese_meaning='';
assert.equal(api.ready(),false,'Empty translation must block all publication');
rows[800].burmese_meaning='သင်ယူခြင်း';
rows[800].reviewed_burmese=false;
assert.equal(api.ready(),false,'Unreviewed translation must block publication');
rows[800].reviewed_burmese=true;
delete paths[rows[800].example_sentence];
assert.equal(api.ready(),false,'Missing British voice must block publication');
paths[rows[800].example_sentence]={bm_george:'audio/bm_george/'+'a'.repeat(24)+'.mp3',bf_emma:'audio/bf_emma/'+'b'.repeat(24)+'.mp3'};
rows[1].word=rows[0].word;
assert.equal(api.ready(),false,'Duplicate vocabulary must block all publication');
console.log('PASS UI gated: 1000 entries, 5 levels, view/search, audio routing, HTML escaping, rejected empty/unreviewed/duplicate values and missing audio');
const index=fs.readFileSync(path.join(root,'index.html'),'utf8');
assert.ok(index.includes('cefr-vocabulary-data.js'));
assert.ok(index.includes('cefr-vocabulary.js'));
assert.ok(index.indexOf('cefr-vocabulary.js')<index.indexOf('script.js'));
const legacy=fs.readFileSync(path.join(root,'script.js'),'utf8');
assert.ok(legacy.includes("top==='cefr-vocabulary'"));
console.log('PASS staging route and script load order');
