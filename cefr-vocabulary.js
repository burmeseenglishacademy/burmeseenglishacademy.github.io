/* BEA CEFR Word Bank — pure client-side rendering; no API, tracking or storage.
 * This module is intentionally not linked from the production site until all
 * 5000 entries and British recordings pass the release QC gate.
 */
(function(root){
 'use strict';
 const GOALS={A1:500,A2:700,B1:1000,B2:1300,C1:1500};
 const order=Object.keys(GOALS),size=24;
 let level='A1',query='',page=0;
 function safe(value){
  return String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 }
 function ready(){
  const data=root.CEFR_VOCAB_BANK;
  if(!data||data.release_status!=='VERIFIED_FOR_RELEASE'||!Array.isArray(data.entries)||data.entries.length!==5000)return false;
  const levels={A1:0,A2:0,B1:0,B2:0,C1:0},seen=new Set();
  for(const row of data.entries){
   if(!row||!Object.hasOwn(levels,row.level)||!row.word||!row.english_definition||!row.burmese_meaning||!row.example_sentence||!row.part_of_speech)return false;
   if(!['reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation'].every(flag=>row[flag]===true))return false;
   if(!['source_english','source_burmese','source_level'].every(field=>typeof row[field]==='string'&&row[field].startsWith('https://')))return false;
   if(!/[\u1000-\u109F\uAA60-\uAA7F]/.test(row.burmese_meaning))return false;
   const clips=root.BEA_AUDIO_MANIFEST?.clips;
   if(!clips)return false;
   for(const text of [row.display_word||row.word,row.example_sentence]){
    const voices=clips[text];
    if(!voices||!['bm_george','bf_emma'].every(v=>{
     const prefix='audio/'+v+'/';
     return typeof voices[v]==='string'&&voices[v].startsWith(prefix)&&/^[a-f0-9]{24}\.mp3$/.test(voices[v].slice(prefix.length));
    }))return false;
   }
   levels[row.level]++;
   if(seen.has(row.word.toLowerCase()))return false;
   seen.add(row.word.toLowerCase());
  }
  return order.every(x=>levels[x]===GOALS[x]);
 }
 function results(){
  return root.CEFR_VOCAB_BANK.entries.filter(e=>
   e.level===level&&(!query||[e.word,e.english_definition,e.burmese_meaning,e.example_sentence]
    .some(v=>String(v).toLocaleLowerCase().includes(query.toLocaleLowerCase()))));
 }
 function card(e){
  const i=root.CEFR_VOCAB_BANK.entries.indexOf(e);
  return `<article class="panel" data-cefr-card="${i}" style="margin:0">
    <div class="split"><h3 style="margin:0">${safe(e.display_word||e.word)}</h3><span class="level-pill">${safe(e.level)} · ${safe(e.part_of_speech||'')}</span></div>
    <p>${safe(e.english_definition)}</p><p class="mm" lang="my">${safe(e.burmese_meaning)}</p>
    <p class="muted"><em>${safe(e.example_sentence)}</em></p>
    <div class="toolbar-actions">
     <button type="button" class="btn soft sm" data-cefr-speak="${i}" data-part="word" aria-label="Speak word in selected British voice">🔊 Word</button>
     <button type="button" class="btn outline sm" data-cefr-speak="${i}" data-part="example" aria-label="Speak example in selected British voice">▶ Example</button>
    </div>
   </article>`;
 }
 function render(){
  if(!ready())return `<div class="page"><h1>CEFR Vocabulary</h1><p>This word bank is undergoing accuracy and audio checks. The current Academy lessons and IELTS words remain available.</p><a class="btn outline" href="#home">Back to Academy</a></div>`;
  const items=results(),maxPage=Math.max(1,Math.ceil(items.length/size));
  page=Math.min(page,maxPage-1);
  const cards=items.slice(page*size,(page+1)*size);
  return `<div class="page" id="cefrVocabularyPage"><div class="eyebrow">ENGLISH + မြန်မာ · A1–C1</div>
   <h1>5,000 English words. Five steps forward.</h1>
   <p>English definitions, Burmese meanings and original example sentences. Choose George or Emma from <strong>Voices</strong> to hear prerecorded British audio.</p>
   <p class="mm" lang="my">အဆင့်အလိုက် ဝေါဟာရများကို ရှာဖွေဖတ်ရှုပြီး George သို့မဟုတ် Emma အသံကို ရွေးချယ်နားထောင်နိုင်ပါတယ်။</p>
   <div class="toolbar-actions" role="group" aria-label="Choose vocabulary level">
   ${order.map(l=>`<button class="btn ${l===level?'primary':'outline'}" type="button" data-cefr-level="${l}" aria-pressed="${l===level?'true':'false'}">${l} · ${GOALS[l].toLocaleString()}</button>`).join('')}</div>
   <div class="word-bank-controls" style="margin:18px 0"><div class="word-bank-search-field">
    <label for="cefrSearch">Search words, definitions or Burmese meaning</label>
    <input class="search" id="cefrSearch" type="search" autocomplete="off" spellcheck="false" value="${safe(query)}" placeholder="Search this level…">
   </div></div>
   <p class="muted" id="cefrResultCount">${items.length.toLocaleString()} words · ${level} · Page ${page+1} of ${maxPage}</p>
   <div class="word-bank-grid">${cards.length?cards.map(card).join(''):'<p>No matching words in this level.</p>'}</div>
   <nav class="word-bank-pagination" aria-label="CEFR vocabulary pages">
    <button type="button" class="btn outline" data-cefr-page="previous" ${page===0?'disabled':''}>← Previous</button>
    <span>Page ${page+1} of ${maxPage}</span>
    <button type="button" class="btn outline" data-cefr-page="next" ${page+1>=maxPage?'disabled':''}>Next →</button>
   </nav><p class="note-small">Level labels are editorial curriculum selections, not an official CEFR certificate. No learner progress, preferences or results are stored.</p>
  </div>`;
 }
 function mount(){
  const app=document.getElementById('app');if(!app)return;
  app.innerHTML=render();
 }
 function click(ev){
  const target=ev.target?.closest?.('[data-cefr-level],[data-cefr-page],[data-cefr-speak]');
  if(!target||!document.getElementById('cefrVocabularyPage'))return;
  if(target.dataset.cefrLevel){level=target.dataset.cefrLevel;query='';page=0;mount();return;}
  if(target.dataset.cefrPage){page=Math.max(0,page+(target.dataset.cefrPage==='next'?1:-1));mount();return;}
  if(target.dataset.cefrSpeak){
   const i=Number(target.dataset.cefrSpeak),word=root.CEFR_VOCAB_BANK.entries[i];
   if(!word||!root.playSpeech)return;
   root.playSpeech(target.dataset.part==='example'?word.example_sentence:(word.display_word||word.word));
  }
 }
 function input(ev){
  if(ev.target?.id!=='cefrSearch')return;
  query=ev.target.value;page=0;
  const selection=document.activeElement===ev.target;
  const caret=selection?ev.target.selectionStart:0;
  mount();
  const el=document.getElementById('cefrSearch');
  if(selection&&el){el.focus();try{el.setSelectionRange(caret,caret)}catch(e){}}
 }
 document.addEventListener('click',click);
 document.addEventListener('input',input);
 root.BEACefr={render,ready,go:mount};
})(window);
