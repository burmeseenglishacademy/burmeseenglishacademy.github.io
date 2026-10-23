#!/usr/bin/env node
/* Browser QA: desktop Chromium and simulated mobile Safari engine (WebKit).
   WebKit here is NOT a physical iPhone. Native Audio play() is mocked only for
   route/voice selection checks. HTTP MP3 requests are checked separately.
*/
'use strict';
const assert=require('node:assert/strict');
const {chromium,webkit,devices}=require('playwright');
const base='http://127.0.0.1:8765/';
const tabs=['overview','reading','listening','speaking','writing','grammar','vocab','quiz'];
async function check(engine,label,options,allRoutes){
 const browser=await engine.launch({headless:true});
 const context=await browser.newContext(options);
 const page=await context.newPage();
 const exceptions=[];
 page.on('pageerror',e=>exceptions.push(e.message));
 await page.addInitScript(()=>{
  window.__audioEvents=[];
  window.Audio=function(){
   const fake={src:'',preload:'',playbackRate:1,preservesPitch:false,
    play(){window.__audioEvents.push({kind:'play',src:this.src,rate:this.playbackRate});return Promise.resolve();},
    pause(){window.__audioEvents.push({kind:'pause'});},
    removeAttribute(n){if(n==='src')this.src='';},
    load(){},onerror:null,onended:null};
   return fake;
  };
 });
 try{
  const response=await page.goto(base,{waitUntil:'load',timeout:30000});
  assert.equal(response.status(),200);
  await page.locator('#app .home-page').waitFor({timeout:15000});
  const state=await page.evaluate(()=>({
   version:SITE_META.version,
   lessons:LESSONS.length,
   vocab:IELTS_VOCAB_BANK.entries.length,
   clips:Object.keys(window.BEA_AUDIO_MANIFEST.clips).length,
   loaded:typeof window.playSpeech==='function',
   hero:document.querySelector('h1')?.innerText,
  }));
  assert.equal(state.version,'1.2.5');
  assert.equal(state.lessons,54);assert.equal(state.vocab,1000);
  assert.equal(state.clips,2326);assert.ok(state.loaded);
  const routes=allRoutes?Array.from({length:54},(_,i)=>i+1):[1,2,10,18,19,31,44,54];
  for(const id of routes)for(const tab of tabs){
   const output=await page.evaluate(({id,tab})=>{
    history.replaceState(null,'','#lesson/'+id+'/'+tab);route();
    return {failed:document.querySelector('#app')?.textContent?.includes('Something went wrong'),
     navs:document.querySelectorAll('.skills-tabs a').length,lesson:document.querySelector('.lesson-header .tag')?.textContent};
   },{id,tab});
   assert.ok(!output.failed,label+': lesson '+id+'/'+tab+' crashed');
   assert.equal(output.navs,8,label+': missing tabs');
   assert.ok(output.lesson?.includes(String(id).padStart(2,'0')),label+': wrong lesson');
  }
  // Validate all 20 topic filters and search/reset.
  await page.evaluate(()=>{history.replaceState(null,'','#ielts-vocabulary');route();});
  const count=await page.evaluate(()=>getWordBankEntries().length);
  assert.equal(count,1000);
  await page.locator('#ieltsVocabSearch').fill('accommodation');
  assert.ok((await page.locator('#wordBankResults').innerText()).includes('accommodation'));
  await page.locator('[data-action="word-bank-reset"]').count().then(async n=>{
   if(n)await page.locator('[data-action="word-bank-reset"]').click();
   else await page.locator('#ieltsVocabSearch').fill('');
  });
  assert.ok((await page.locator('#wordBankResults').innerText()).includes('1,000 of 1,000 words'));
  const topics=await page.locator('#ieltsVocabTopic option').count();
  assert.equal(topics,21);
  for(let i=0;i<20;i++){
   await page.locator('#ieltsVocabTopic').selectOption(String(i));
   assert.ok((await page.locator('#wordBankResults').innerText()).includes('50 of 1,000 words'),label+' topic '+i);
  }
  await page.locator('#ieltsVocabTopic').selectOption('all');

  // Actual site handlers: verify voice choice and audio URL via mock. Do not claim audible playback.
  await page.locator('#voiceSettingsToggle').click();
  await page.locator('#voicePreview').click();
  let heard=await page.evaluate(()=>window.__audioEvents.filter(x=>x.kind==='play').at(-1)?.src);
  assert.match(heard,/audio\/bm_george\/[a-f0-9]{24}\.mp3$/,label+' George preview');
  await page.locator('#voiceGender').selectOption('female');
  await page.locator('#voicePreview').click();
  heard=await page.evaluate(()=>window.__audioEvents.filter(x=>x.kind==='play').at(-1)?.src);
  assert.match(heard,/audio\/bf_emma\/[a-f0-9]{24}\.mp3$/,label+' Emma preview');
  await page.locator('[data-action="word-bank-say"]').first().click();
  heard=await page.evaluate(()=>window.__audioEvents.filter(x=>x.kind==='play').at(-1)?.src);
  assert.match(heard,/audio\/bf_emma\/[a-f0-9]{24}\.mp3$/,label+' vocabulary playback');
  await page.evaluate(()=>{history.replaceState(null,'','#lesson/1/listening');route();});
  await page.locator('[data-action="say"][data-text="audio"]').first().click();
  heard=await page.evaluate(()=>window.__audioEvents.filter(x=>x.kind==='play').at(-1)?.src);
  assert.match(heard,/audio\/bf_emma\/[a-f0-9]{24}\.mp3$/,label+' lesson playback');
  const before=await page.evaluate(()=>window.__audioEvents.filter(x=>x.kind==='pause').length);
  await page.locator('[data-action="say-stop"]').click();
  const after=await page.evaluate(()=>window.__audioEvents.filter(x=>x.kind==='pause').length);
  assert.ok(after>before,label+' stop action');

  assert.deepEqual(await context.cookies(),[],label+' added cookies');
  const browserStorage=await page.evaluate(()=>({local:localStorage.length,session:sessionStorage.length}));
  assert.deepEqual(browserStorage,{local:0,session:0},label+' unexpectedly persists learners');
  assert.deepEqual(exceptions,[],label+' JS errors');
  console.log('PASS '+label+': '+routes.length*tabs.length+' lessons/tabs, IELTS search & filters, male/female playback, stop, privacy');
 }finally{
  await browser.close();
 }
}
async function main(){
 await check(chromium,'Chromium desktop',{viewport:{width:1300,height:900}},true);
 await check(webkit,'WebKit iPhone emulation',devices['iPhone 13'],false);
 const browser=await chromium.launch({headless:true});
 try{
  const ctx=await browser.newContext();
  const p=await ctx.newPage();await p.goto(base);
  const samples=await p.evaluate(()=>{
   const arr=Object.values(window.BEA_AUDIO_MANIFEST.clips),indices=[0,1,10,200,500,1000,1500,2000,2325];
   return indices.flatMap(i=>Object.values(arr[i]));
  });
  for(const sample of samples){
   const response=await ctx.request.get(base+sample);
   assert.equal(response.status(),200,'MP3 unavailable: '+sample);
   const body=await response.body();
   assert.ok(body.length>500,'Truncated MP3: '+sample);
  }
  console.log('PASS '+samples.length+' sample MP3 HTTP GETs');
 }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
