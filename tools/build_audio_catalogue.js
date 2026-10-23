#!/usr/bin/env node
/* Extract existing Academy playback text without changing lesson data. */
'use strict';
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(process.argv[2]||'.');
const outfile=path.resolve(process.argv[3]||path.join(root,'audio-catalogue.json'));
function read(file,name){
 const context=Object.create(null);
 const source=fs.readFileSync(path.join(root,file),'utf8');
 vm.runInNewContext(source+'\n;globalThis.result='+name+';',context,{timeout:10000,filename:file});
 return context.result;
}
const lessons=read('content.js','LESSONS');
const bank=read('ielts-vocabulary-data.js','IELTS_VOCAB_BANK');
if(!Array.isArray(lessons)||lessons.length!==54)throw Error('54 lessons expected');
if(!Array.isArray(bank.entries)||bank.entries.length!==1000)throw Error('1000 IELTS words expected');
const texts=new Map();
function add(value,source){
 if(typeof value!=='string'||!value.trim())throw Error('Missing '+source);
 const text=value.trim(),id=crypto.createHash('sha256').update(text).digest('hex').slice(0,24);
 if(!texts.has(text))texts.set(text,{id,text,sources:[source]});
 else texts.get(text).sources.push(source);
}
for(const l of lessons){
 add(l.reading,'lesson:'+l.id+':reading');
 add(l.audio,'lesson:'+l.id+':audio');
 if(!Array.isArray(l.words)||l.words.length!==5)throw Error('Expected 5 words in lesson '+l.id);
 l.words.forEach((w,i)=>add(w[0],'lesson:'+l.id+':word:'+i));
}
bank.entries.forEach((e,i)=>{add(e[0],'ielts:'+i+':word');add(e[3],'ielts:'+i+':example');});
add('Good morning! Welcome to Burmese English Academy. Let us practise clear British English together.','voice:preview');
const entries=[...texts.values()].sort((a,b)=>a.id.localeCompare(b.id));
if(new Set(entries.map(e=>e.id)).size!==entries.length)throw Error('SHA collision');
const result={schema:1,voices:['bm_george','bf_emma'],source_counts:{lessons:54,ielts_words:1000},unique_texts:entries.length,recording_goal:2*entries.length,entries};
fs.writeFileSync(outfile,JSON.stringify(result,null,2)+'\n');
console.log(result.unique_texts+' unique texts, '+result.recording_goal+' recordings required');
