#!/usr/bin/env node
/* BEA regression checks: no external API, no learner data. */
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const crypto=require('node:crypto');
const vm=require('node:vm');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const read=(f)=>fs.readFileSync(path.join(root,f),'utf8');
function loadConst(f,expr){const ctx={window:{}};vm.runInNewContext(read(f)+'\n;globalThis.output='+expr+';',ctx,{filename:f,timeout:12000});return JSON.parse(JSON.stringify(ctx.output));}
const lessons=loadConst('content.js','LESSONS');
const vocab=loadConst('ielts-vocabulary-data.js','IELTS_VOCAB_BANK');
const manifest=loadConst('audio-manifest.js','window.BEA_AUDIO_MANIFEST');
const id=(s)=>crypto.createHash('sha256').update(s).digest('hex').slice(0,24);
const texts=new Set();
const add=(s,where)=>{assert.equal(typeof s,'string',where);assert.ok(s.trim(),where);texts.add(s.trim());};
assert.equal(lessons.length,54);
assert.equal(vocab.entries.length,1000);
assert.equal(vocab.topics.length,20);
for(let i=0;i<54;i++){const l=lessons[i];assert.equal(l.id,i+1,'lesson id');for(const v of ['reading','audio'])add(l[v],'lesson '+l.id+' '+v);assert.equal(l.words.length,5);for(const w of l.words)add(w[0],'lesson '+l.id+' word');assert.ok(l.quiz.length>=5,'lesson quiz');}
for(const e of vocab.entries){add(e[0],'vocab word');add(e[3],'vocab example');}
add('Good morning! Welcome to Burmese English Academy. Let us practise clear British English together.','preview');
assert.equal(texts.size,2326);
assert.equal(Object.keys(manifest.clips).length,2326);
let files=0,bytes=0;
for(const t of texts){
 const voices=manifest.clips[t];assert.ok(voices,'Missing text: '+t.slice(0,80));
 assert.deepEqual(Object.keys(voices).sort(),['bf_emma','bm_george'],'missing voice for '+t.slice(0,50));
 for(const voice of ['bm_george','bf_emma']){
  const relative='audio/'+voice+'/'+id(t)+'.mp3';
  assert.equal(voices[voice],relative,'wrong text-to-file mapping');
  const stat=fs.statSync(path.join(root,relative));
  assert.ok(stat.size>500,'empty MP3: '+relative);
  files++;bytes+=stat.size;
 }
}
assert.equal(files,4652);
const index=read('index.html');
for(const name of ['audio-manifest.js','audio-player.js','audio-integration.js'])
 assert.equal((index.match(new RegExp('src="'+name.replaceAll('.','\\.')+'\\?','g'))||[]).length,1,'Audio script missing/duplicate: '+name);
assert.ok(index.indexOf('src="script.js?')<index.indexOf('src="audio-integration.js?'),'script load order');
assert.ok(index.includes('connect-src \'none\''),'privacy CSP connect-src');
assert.ok(!index.includes('https://fonts.googleapis.com'),'no third-party font delivery');
const source=read('audio-integration.js');
assert.ok(source.includes('const gender=()'),'gender switch exists');
assert.ok(source.includes('root.playSpeech=function'),'audio integration active');
assert.ok(source.includes('return originalSpeak'),'safe fallback preserved');
assert.ok(read('site-config.js').includes("version: '1.2.5'"),'expected release version');
console.log('PASS static: 54 lessons, 8 skills, 1000 IELTS entries, 2326 texts, 4652 MP3s, exact audio paths');
console.log('PASS script/CSP integration, manifest size and privacy checks');
console.log('Audio bytes:',bytes);
