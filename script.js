const TRACKS = [["A1","Beginner Foundations","အခြေခံစတင်လေ့လာမှု","A1"],["A2","Elementary Life English","နေ့စဉ်ဘဝ အင်္ဂလိပ်စာ","A2"],["B1","Independent English","အလယ်အလတ် အင်္ဂလိပ်စာ","B1"],["B2","Confident Communication","အဆင့်မြင့်အလယ်ပိုင်း","B2"],["C1","Advanced Communication","အဆင့်မြင့်အင်္ဂလိပ်စာ","C1"],["IELTS Bridge","IELTS Foundations","IELTS အခြေခံပြင်ဆင်မှု","IELTS"],["IELTS Academic","IELTS Academic","IELTS Academic လေ့ကျင့်မှု","IELTS"],["IELTS General","IELTS General Training","IELTS General Training လေ့ကျင့်မှု","IELTS"]];
/* Lesson content is loaded from content.js before this application script. */
'use strict';
/* All learning content lives in this local JS file. No accounts, APIs, frameworks or tracking. */
const SKILLS=['Reading','Listening','Speaking','Writing','Grammar','Vocabulary'];
const TABS=[['overview','Overview'],['reading','📖 Reading'],['listening','🎧 Listening'],['speaking','🎙 Speaking'],['writing','✍ Writing'],['grammar','🧩 Grammar'],['vocab','🗂 Vocabulary'],['quiz','✅ Quiz']];
const MAX_ID=LESSONS.length;
const E=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const toWords=s=>String(s||'').trim().match(/[\p{L}\p{N}]+(?:['’\-][\p{L}\p{N}]+)*/gu)||[];
const countWords=s=>toWords(s).length;
const norm=s=>String(s).toLowerCase().normalize('NFKC').replace(/[’]/g,"'").replace(/[^\p{L}\p{N}' ]/gu,' ').replace(/\s+/g,' ').trim();
const today=()=>{let d=new Date();return [d.getFullYear(),String(d.getMonth()+1).padStart(2,'0'),String(d.getDate()).padStart(2,'0')].join('-')};
const tr=(id)=>LESSONS.find(l=>l.id===Number(id));
const defaultState=()=>({speed:1,activeMock:null});
function loadState(){return defaultState()} // Fresh, in-memory practice only; never read historical progress
let wordBankQuery='',wordBankTopic='all',wordBankPage=0,wordBankExact=false;
let state=loadState();let timerHandle=null,timerEndsAt=0,timerRemain=0,recorder=null,recordedChunks=[],recordedAudioURL=null,recogniser=null;let recordingStream=null,recordDeletePending=false,recordingGeneration=0;let activeFlash=null;let searchQuery='',filterLevel='all';let gymQuestions=[],gymLevel='all';
function save(){} // Intentional: no learner progress, drafts, or preferences are persisted.
function recordVisit(){} // No visit logs.
function markSkill(){} // No completion tracking.

function toast(message){let el=document.getElementById('toast');el.textContent=message;el.classList.add('show');clearTimeout(toast._t);toast._t=setTimeout(()=>el.classList.remove('show'),3500)}
function percent(n,d){return Math.round((n/(d||1))*100)}
function levelLessons(level){return LESSONS.filter(l=>l.level===level)}
function updateAside(){
 const tracks=document.getElementById('sideTracks');
 if(tracks)tracks.innerHTML=TRACKS.map(([id,label])=>`<a href="#courses/${encodeURIComponent(id)}" data-track="${E(id)}"><span>${E(label)}</span><span>${levelLessons(id).length} lessons</span></a>`).join('');
}
function route(){clearRecordingSession(false);let hash=decodeURIComponent(location.hash.replace(/^#/,''))||'home';let parts=hash.split('/');let top=parts[0];clearLessonTimer();if(!top)top='home';
 const app=document.getElementById('app');
 try{
  if(top==='home')app.innerHTML=renderHome();
  else if(top==='courses')app.innerHTML=renderCourses(parts[1]||'all');
  else if(top==='lesson') {let l=tr(parts[1]);app.innerHTML=l?renderLesson(l,parts[2]||'overview'):renderCourses('all')}
  else if(top==='review')app.innerHTML=renderReview();
  else if(top==='gym')app.innerHTML=renderGym(parts[1]||'all');
  else if(top==='ielts')app.innerHTML=renderIELTS();
  else if(top==='ielts-vocabulary')app.innerHTML=renderIELTSVocabulary();
  else if(top==='mock')app.innerHTML=renderMock(parts[1]);
  else if(top==='guide')app.innerHTML=renderGuide();
  else if(top==='updates')app.innerHTML=renderUpdates();
  else app.innerHTML=renderHome();
 }catch(e){console.error(e);app.innerHTML=`<div class="panel"><h2>Something went wrong</h2><p>Please reload this page. Practice entries are not saved and will be cleared.</p><code>${E(e.message)}</code></div>`}
 document.querySelectorAll('.toplinks a').forEach(a=>a.classList.toggle('active',a.dataset.nav=== (top==='lesson'?'courses':top==='mock'?'ielts':top)));
 document.querySelectorAll('.side-tracks a').forEach(a=>a.classList.toggle('active',a.dataset.track===parts[1]));
 document.querySelector('.toplinks').classList.remove('open');document.getElementById('menuToggle').setAttribute('aria-expanded','false');
 updateAside();window.scrollTo(0,0);if(top==='mock')startMockClock();}
function renderUpdates(){let entries=Array.isArray(SITE_META.history)?SITE_META.history:[];
 return `<div class="page"><div class="eyebrow">ACADEMY RELEASE HISTORY</div><h1>What's new in Burmese English Academy?</h1><p class="muted">Version ${E(SITE_META.version)} · Updated ${E(SITE_META.updated)} · ${MAX_ID} guided lessons</p><div class="notice"><strong>Our commitment:</strong> The learning materials are free. New lesson content and corrections will appear here when published.</div><div class="cards" style="display:block">${entries.map(entry=>`<article class="panel" style="margin:16px 0"><span class="level-pill">Version ${E(entry.version)}</span> <span class="muted">${E(entry.date)}</span><h2>${E(entry.title||'Website update')}</h2><p style="white-space:pre-line">${E(entry.notes||'Improvements and lesson updates.')}</p></article>`).join('')}</div><div class="panel"><h2>For learners | သင်ယူသူများအတွက်</h2><p>You do not need to download the website again to see newly published lessons. Just refresh this page while online.</p><p class="mm">သင်ခန်းစာအသစ် တင်ထားရင် Website ကို Refresh လုပ်ပြီး ကြည့်နိုင်ပါတယ်။</p><p class="note-small">This edition does not store scores or lesson progress. Choose any lesson next time and keep your own notes.</p></div></div>`;}
function renderHome(){
 const lead=LESSONS[0];
 return `<div class="page home-page">
  <section class="hero hero-new" aria-labelledby="heroTitle">
    <div class="hero-copy">
      <div class="eyebrow hero-eyebrow"><span class="pulse-dot"></span> FREE FOR EVERY LEARNER · အခမဲ့</div>
      <h1 id="heroTitle">A little English.<br><em>A lot of possibility.</em></h1>
      <p class="hero-lede">Every word takes you somewhere. Explore ${MAX_ID} bite-sized lessons, with English explanations and Burmese support. No login, no pressure, no tracking.</p>
      <p class="mm hero-mm" lang="my">ကိုယ့်အဆင့်နဲ့ ကိုက်ညီတဲ့ သင်ခန်းစာကို ရွေးပြီး လွတ်လပ်စွာ လေ့လာပါ။ အကောင့်ဖွင့်ရန် မလိုပါ။ သင်ယူမှုမှတ်တမ်းကို Website မှ မသိမ်းပါ။</p>
      <div class="hero-actions"><a href="#courses" class="btn light">Explore lessons <span aria-hidden="true">↗</span></a><a href="#lesson/${lead.id}/overview" class="btn ghost">Start Lesson 01 →</a></div>
      <div class="hero-proof"><span>✦ 54 guided lessons</span><span>✦ British voices</span><span>✦ No accounts</span></div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <div class="orbit orbit-one"></div><div class="orbit orbit-two"></div>
      <span class="hero-spark spark-one">✦</span><span class="hero-spark spark-two">✳</span>
      <div class="art-note art-note-main"><span class="art-note-label">WORD OF THE DAY</span><strong>Grow.</strong><small>/ɡrəʊ/</small><span class="art-note-mm">တိုးတက်ပါ</span></div>
      <div class="art-note art-note-small"><span>HELLO!</span><strong>မင်္ဂလာပါ</strong></div>
      <div class="art-bubble art-bubble-one">a</div><div class="art-bubble art-bubble-two">A</div>
    </div>
  </section>
  <section class="metrics" aria-label="Academy at a glance">
    <div class="metric"><strong class="value">${MAX_ID}</strong><span class="label">Guided lessons</span></div>
    <div class="metric"><strong class="value">8</strong><span class="label">Learning pathways</span></div>
    <div class="metric"><strong class="value">6</strong><span class="label">Practice skills</span></div>
    <div class="metric"><strong class="value">Free</strong><span class="label">Always, for everyone</span></div>
  </section>
  <section class="word-bank-teaser"><div><span class="eyebrow">NEW · IELTS VOCABULARY</span><h2>1,000 words. A world of ideas.</h2><p>English definitions, Burmese meanings and real usage examples across 20 useful topics. Hear every word, search freely, and learn without tracking.</p><a href="#ielts-vocabulary" class="btn primary">Explore the word bank ↗</a></div><div class="word-bank-teaser-art" aria-hidden="true"><span>1,000</span><small>WORDS TO DISCOVER</small></div></section>
  <section class="privacy-promise" aria-label="Our privacy promise"><span class="privacy-promise-icon">✳</span><div><strong>Learning belongs to you. Not a database.</strong><p>No account, saved scores or completion history. Pick up at any lesson next time. <span lang="my">ဘယ်သင်ခန်းစာရောက်ခဲ့လဲ ကိုယ်တိုင်မှတ်သားနိုင်ပါတယ်။</span></p></div><a href="privacy.html">Our privacy promise ↗</a></section>
  <div class="section-head"><div><span class="eyebrow">FIND YOUR PATH</span><h2>Where will English take you?</h2><p>Pick any level. Every lesson is open.</p></div><a href="#courses">All ${MAX_ID} lessons ↗</a></div>
  <section class="cards level-cards">${TRACKS.map(([id,label,mm],i)=>trackCard(id,label,mm,i)).join('')}</section>
  <section class="welcome-work home-extras">
    <article class="panel editorial-panel"><span class="eyebrow">YOUR DAILY ROUTINE</span><h2>Just 25 minutes. Big difference.</h2><ol class="flow-steps"><li><span class="step-num">05</span><span>Learn five useful phrases</span></li><li><span class="step-num">08</span><span>Read and listen for meaning</span></li><li><span class="step-num">07</span><span>Speak and write your own words</span></li><li><span class="step-num">05</span><span>Check your answers and retry</span></li></ol><a href="#guide" class="text-arrow">Find your study rhythm →</a></article>
    <article class="panel editorial-panel accent-panel"><span class="eyebrow">IELTS CORNER</span><h2>Make practice feel possible.</h2><p>Academic and General Training mini-checks, guided writing and speaking prompts. Honest feedback, no made-up band scores.</p><div class="toolbar-actions"><a href="#ielts" class="btn primary">Enter IELTS Lab →</a><a href="#ielts-vocabulary" class="btn outline">Explore 1,000 IELTS Words ↗</a></div></article>
  </section>
  <div class="section-head"><div><span class="eyebrow">SIX WAYS TO LEARN</span><h2>Practice your whole voice.</h2></div></div>
  <div class="skill-showcase">${[['📖','Reading'],['🎧','Listening'],['🎙','Speaking'],['✍','Writing'],['🧩','Grammar'],['🗂','Vocabulary']].map(([ico,n])=>`<div class="skill-show"><span>${ico}</span><strong>${n}</strong></div>`).join('')}</div>
  <div class="footnote-honest">Courses and IELTS-style exercises are self-study materials, not official certification or guaranteed scores. Learn freely and be curious.</div>
 </div>`;
}
function trackCard(id,label,mm,index){
 const ls=levelLessons(id);
 return `<article class="card track-card tier-${index}"><div class="tier-top"><span class="level-pill">${E(id)}</span><span class="tier-icon" aria-hidden="true">${['✷','✳','✦','❋','✺','◎','◈','✧'][index]}</span></div><h3>${E(label)}</h3><p class="mm">${E(mm)}</p><div class="card-bottom"><span class="track-count">${ls.length} lessons · no tracking</span><a href="#courses/${encodeURIComponent(id)}" class="btn soft sm">Explore ↗</a></div></article>`;
}
function renderCourses(level){filterLevel=level==='all'?'all':TRACKS.some(t=>t[0]===level)?level:'all';const all=LESSONS.filter(l=>(filterLevel==='all'||l.level===filterLevel)&&(`${l.title} ${l.myanmarTitle} ${l.summary} ${l.level}`).toLowerCase().includes(searchQuery.toLowerCase()));
 return `<div class="page"><div class="eyebrow">THE FULL LEARNING PATHWAY</div><h1>Explore ${MAX_ID} lessons.</h1><p class="muted">Use the level filter or search. All lessons are unlocked; follow the order for a stronger foundation.</p><div class="toolbar"><input id="courseSearch" class="search" type="search" autocomplete="off" placeholder="Search lessons, topics…" value="${E(searchQuery)}" aria-label="Search lessons"><select class="filter" id="levelSelect" aria-label="Filter course level"><option value="all">All levels</option>${TRACKS.map(t=>`<option value="${E(t[0])}" ${filterLevel===t[0]?'selected':''}>${E(t[0])} — ${E(t[1])}</option>`).join('')}</select></div><div id="courseMatches" class="lesson-list">${all.length?all.map(lessonTile).join(''):'<p class="empty">No lessons match your search. Try a different keyword.</p>'}</div><div class="notice" style="margin-top:23px">A level label describes the intended complexity of the practice material; completing a short module is not proof of CEFR proficiency.</div></div>`}
function lessonTile(l){return `<a class="lesson-item" href="#lesson/${l.id}/overview"><span class="lesson-index">${String(l.id).padStart(2,'0')}</span><div class="lesson-info"><span class="lesson-level">${E(l.level)}</span><h3>${E(l.title)}</h3><p class="mm">${E(l.myanmarTitle)}</p><p>${E(l.summary)}</p><span class="lesson-state">Open lesson →</span></div></a>`}
function skillPills(){return ''} // No learner completion states.
function renderLesson(l,tab){if(!TABS.some(t=>t[0]===tab))tab='overview';let cur=TABS.find(t=>t[0]===tab)?.[1]||'Overview';let ix=l.id-1;
 return `<div class="page skill-area"><div class="breadcrumb"><a href="#courses/${encodeURIComponent(l.level)}">${E(l.level)} lessons</a> › Lesson ${l.id} › ${E(cur)}</div><header class="lesson-header"><div class="lesson-meta"><span class="level-pill">${E(l.level)}</span><span class="tag">LESSON ${String(l.id).padStart(2,'0')} OF ${MAX_ID}</span></div><h1>${E(l.title)}</h1><p class="mm mm-soft">${E(l.myanmarTitle)}</p><p>${E(l.focus||l.summary)}</p><span class="session-note">Open practice · no progress saved</span></header><nav class="skills-tabs" aria-label="Lesson activities">${TABS.map(([key,label])=>`<a href="#lesson/${l.id}/${key}" ${tab===key?'aria-current="page"':''}>${E(label)}</a>`).join('')}</nav><section class="skill-card">${renderSkill(l,tab)}</section><div class="flex-bottom"><a class="btn outline" href="#lesson/${Math.max(1,l.id-1)}/overview" ${l.id===1?'style="visibility:hidden"':''}>← Previous lesson</a><a class="btn primary" href="#lesson/${Math.min(MAX_ID,l.id+1)}/overview">${l.id===MAX_ID?'Review final lesson':'Next lesson →'}</a></div></div>`}
function skillHead(name,my,description){return `<div class="eyebrow">${E(name.toUpperCase())} PRACTICE</div><h2>${E(name)} <span class="mm mm-soft">| ${E(my)}</span></h2><p class="skill-lede">${E(description)}</p>`}
function renderSkill(l,tab){if(tab==='overview')return renderOverview(l);if(tab==='reading')return renderReading(l);if(tab==='listening')return renderListening(l);if(tab==='speaking')return renderSpeaking(l);if(tab==='writing')return renderWriting(l);if(tab==='grammar')return renderGrammar(l);if(tab==='vocab')return renderVocab(l);return renderQuiz(l)}
function renderOverview(l){return `${skillHead('Lesson overview','လေ့လာမည့်အကြောင်းအရာ','A guided lesson includes six practice stations. Work through them, then complete the five-question checkpoint.')}
 <div class="sample-grid">${[['📖','Reading','Read for main ideas and details.'],['🎧','Listening','Hear a British George or Emma synthetic voice recording.'],['🎙','Speaking','Record or practise aloud and self-reflect.'],['✍','Writing','Write a response and check your task coverage.'],['🧩','Grammar','Apply one targeted language rule.'],['🗂','Vocabulary','Learn and revisit useful English.']].map(([icon,note,desc])=>`<div class="tiny-panel"><h4>${icon} ${note}</h4><p>${desc}</p></div>`).join('')}</div><div class="mini-divider"></div><h3>Today’s communication goal</h3><p>${E(l.focus||l.summary)}</p><h3>Grammar focus</h3><p><strong>${E(l.grammarLabel||'Useful expressions')}</strong></p><p class="mm">${E(l.explain)}</p><div class="toolbar-actions"><a class="btn primary" href="#lesson/${l.id}/reading">Begin with reading →</a><a class="btn outline" href="#lesson/${l.id}/quiz">Jump to quiz</a></div><p class="note-small">Your answers are checked on this page only. No lesson completion is saved.</p>`}
function qHtml(q,name,index){return `<fieldset class="quiz-q"><legend class="q-title">${index+1}. ${E(q.q)}</legend>${q.options.map((v,i)=>`<label class="choice"><input type="radio" name="${E(name)}" value="${i}"><span>${E(v)}</span></label>`).join('')}<div class="feedback" data-feedback="${E(name)}" aria-live="polite"></div></fieldset>`}
function renderReading(l){let isOld=l.id<=18;return `${skillHead('Reading','စာဖတ်ခြင်း','Read for meaning, then answer two questions without guessing. The original A1–A2 lessons use short dialogue texts; later lessons use longer passages.')}
 <div class="study-text" lang="en">${E(l.reading)}</div><div class="toolbar-actions"><button class="btn soft sm" data-action="say" data-text="reading" type="button">🔊 Listen to the passage</button><button class="btn outline sm" data-action="say" data-text="slow-reading" type="button">🐢 Slow playback</button></div><h3 class="divider-large">Reading checkpoint</h3><p class="muted">Choose answers based on the text. After checking, read the explanation for each question.</p><div id="readingQuestions">${l.readingQuestions.map((q,i)=>qHtml(q,'rd'+i,i)).join('')}</div><button type="button" class="btn primary" data-action="reading-check">Check reading answers</button><div class="statline" style="margin-top:10px">${isOld?'Short foundational dialogue practice':'Original reading passage practice'} · Scores here are for learning, not an official test.</div>`}
function renderListening(l){let q=l.audioQuestion;return `${skillHead('Listening','နားထောင်ခြင်း','Play the short recording. Listen for the answer, then try to write the dictated sentence before revealing the transcript.')}
 <div class="rec-box"><h3>🎧 Audio exercise</h3><p class="muted">Choose George (British male) or Emma (British female) with the Voices button.</p><div class="toolbar-actions"><button class="btn primary" type="button" data-action="say" data-text="audio">▶ Play audio</button><button class="btn outline" type="button" data-action="say" data-text="slow-audio">🐢 Play slowly</button><button class="btn soft" type="button" data-action="say-stop">■ Stop</button><button class="btn outline" type="button" data-action="voice-open">🔊 Choose voice</button></div><label for="speedControl">Playback speed</label><select id="speedControl" class="filter" style="min-width:145px;max-width:225px;margin:8px 0"><option value="0.75" ${state.speed===.75?'selected':''}>Slow (0.75x)</option><option value="0.85" ${state.speed===.85?'selected':''}>Learning (0.85x)</option><option value="1" ${state.speed===1?'selected':''}>Natural pace (1.0x) · recommended</option></select></div>
 <h3>Comprehension question</h3>${qHtml(q,'listening-q',0)}<h3>Dictation challenge</h3><p class="muted">Type the first sentence that you hear. This is a word-matching exercise, not an accent or IELTS score.</p><label for="dictInput" class="small">Your dictated sentence</label><textarea id="dictInput" class="input-text dictation" placeholder="Listen, then type the first sentence…" spellcheck="false"></textarea><div class="toolbar-actions"><button class="btn primary" data-action="listening-check" type="button">Check listening</button><button class="btn outline" data-action="listen-reveal" type="button">Reveal full transcript</button></div><div id="dictFeedback" aria-live="polite"></div><div id="listenTranscript" class="listen-text" hidden><strong>Recording transcript:</strong><p>${E(l.audio)}</p><strong>Dictation target:</strong> ${E(l.dictation)}</div><p class="note-small">Audio uses prerecorded synthetic British George and Emma voices, not a real IELTS examiner. An internet connection is needed to load these recordings from the Academy.</p>`}
function renderSpeaking(l){return `${skillHead('Speaking','စကားပြောခြင်း','Speak in your own words. Record yourself if your browser allows microphone access, then listen and reflect. No artificial band score is assigned.')}
 <ol class="hint-list">${l.speak.map(s=>`<li>${E(s)}</li>`).join('')}</ol><div class="rec-box"><h3>🎙 Speaking recorder</h3><p class="muted">Optional: your browser may ask permission to use the microphone. Audio stays in this page and is not uploaded.</p><div class="toolbar-actions"><button class="btn primary" type="button" data-action="record-start">● Start recording</button><button class="btn outline" type="button" data-action="record-stop">■ Stop recording</button><button class="btn outline" type="button" data-action="record-delete">✕ Delete recording</button></div><p id="recordStatus" class="statline">Ready. You can also speak without recording.</p><div id="recordPlayback"></div><p class="note-small">Privacy test build: Speech-to-text is disabled because browser services may send spoken audio to third parties. Recording stays within this page session unless you download it. Leaving the Speaking page clears app-managed recording memory.</p></div>
 <h3>Speaking reflection <span class="mm mm-soft">| ကိုယ်တိုင်ပြန်လည်သုံးသပ်မှု</span></h3><div class="check-row"><input id="sp1" type="checkbox"><label for="sp1">I answered the prompt and gave at least one specific example.</label></div><div class="check-row"><input id="sp2" type="checkbox"><label for="sp2">I spoke at a steady pace and corrected unclear words.</label></div><div class="check-row"><input id="sp3" type="checkbox"><label for="sp3">I listened to my recording or repeated my answer aloud.</label></div><div class="toolbar-actions"><button class="btn primary" data-action="speaking-check" type="button">Check my speaking practice</button><button class="btn outline" data-action="say" data-text="audio" type="button">Listen to sample audio</button></div><div id="speakFeedback" aria-live="polite"></div>`}
function renderWriting(l){let min=l.minWords||60,content='',task=l.table;let writingType=(l.level.startsWith('IELTS')?'Exam-style practice':'Guided free writing');let minutes=l.minutes||0;
 return `${skillHead('Writing','စာရေးခြင်း','Write your own answer in this page, then revise it with the checklist. Your draft is never saved by the Academy; copy it yourself before leaving.')}
 <div class="sample"><div class="split"><strong>${E(writingType)}</strong><span class="tag">Target ${min}+ words</span></div><p style="margin:10px 0">${E(l.write)}</p></div>
 ${task?`<div class="table-wrap"><table class="data-table"><caption>${E(task.title)} · illustrative exercise data</caption><thead><tr>${task.headers.map(s=>`<th scope="col">${E(s)}</th>`).join('')}</tr></thead><tbody>${task.rows.map(row=>`<tr>${row.map(v=>`<td>${E(v)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`:''}
 ${minutes?`<div class="toolbar-actions"><span class="timer" id="lessonTimer">${minutes}:00</span><button type="button" class="btn outline sm" data-action="timer-start" data-minutes="${minutes}">Start ${minutes}-minute timer</button><button type="button" class="btn outline sm" data-action="timer-pause">Pause</button><button type="button" class="btn outline sm" data-action="timer-reset" data-minutes="${minutes}">Reset</button></div>`:''}
 <label for="writingText" style="display:block;margin:15px 0 7px;font-weight:750">Your writing <span class="mm mm-soft">| သင်ရေးသားချက်</span></label><textarea id="writingText" autocomplete="off" class="writing-box" placeholder="Write your response here. Try to answer every part of the task…">${E(content)}</textarea><div class="split writing-count"><span id="wordCount">${countWords(content)} words written · target ${min}+</span><span id="draftStatus">Temporary on this page · not saved</span></div>
 <div class="mini-divider"></div><h3>Self-review: check these four areas</h3>${['I answered every part of the question and used relevant ideas.','I organised my response into clear, connected paragraphs.','I checked word choice and avoided unnecessary repetition.','I reviewed grammar, spelling and punctuation.'].map((s,i)=>`<label class="check-row"><input type="checkbox" class="write-check" value="${i}"> ${E(s)}</label>`).join('')}
 <div class="toolbar-actions"><button type="button" class="btn primary" data-action="writing-check">Check my draft</button><button type="button" class="btn soft" data-action="writing-coach">Find simple improvements</button></div><div id="writingCoach" aria-live="polite"></div><div id="writingFeedback" aria-live="polite"></div>
 ${l.level.startsWith('IELTS')?'<p class="w-note">An official IELTS Writing band requires human-style assessment against task response/achievement, coherence and cohesion, lexical resource, and grammar. This website does not pretend to grade your essay automatically.</p>':''}`}
function renderGrammar(l){let q=l.quiz.find(q=>q.skill==='Grammar')||l.quiz[3];return `${skillHead('Grammar','သဒ္ဒါ','Understand the rule, compare examples and check one targeted question.')}
 <div class="sample"><h3>${E(l.grammarLabel||'Useful grammar')}</h3><p class="mm">${E(l.explain)}</p></div><h3 style="margin-top:23px">Apply the rule</h3>${qHtml(q,'grammar-q',0)}<button class="btn primary" type="button" data-action="grammar-check">Check grammar</button><p class="note-small">Review the rule, change your answer and try again. One question is practice, not proof of full grammar mastery.</p>`}
function cardId(l,i){return `${l.id}:${i}`}
function renderVocab(l){return `${skillHead('Vocabulary','ဝေါဟာရ','Listen, reveal the Burmese meaning, and try making your own sentences. No scores or review schedule are stored.')}
 <div class="vocab-grid">${l.words.map(([word,mm,example],i)=>`<article class="vocab-tile"><div><span class="tag">WORD ${i+1}</span><h3>${E(word)}</h3><div id="vocabMeaning${i}" hidden><p class="mm mm-soft">${E(mm)}</p><p>${E(example)}</p></div></div><div class="vocab-actions"><button type="button" class="btn outline sm" data-action="vocab-flip" data-idx="${i}">Reveal meaning</button><button type="button" class="btn soft sm" data-action="vocab-audio" data-idx="${i}" aria-label="Play pronunciation for word ${i+1}">🔊 Listen</button></div></article>`).join('')}</div><div class="toolbar-actions"><a class="btn soft" href="#review">Browse word practice →</a></div><p class="note-small">Your learning is yours: jot down words you want to revisit another day.</p>`}
function renderQuiz(l){return `${skillHead('Lesson checkpoint','သင်ခန်းစာစစ်ဆေးမှု','Five quick questions with instant feedback. Nothing is saved, and you can retry freely.')}
 <div class="notice">The quiz checks selected concepts on this page only. Speaking and writing are not automatically graded.</div><div id="quizArea">${l.quiz.map((q,i)=>qHtml(q,'quiz'+i,i)).join('')}</div><div class="toolbar-actions"><button type="button" class="btn primary" data-action="quiz-submit">Check my answers</button><button type="button" class="btn outline" data-action="quiz-retry">Try again</button></div><div id="quizResult" aria-live="polite"></div>`}
/* IELTS VOCABULARY · 1,000 terms in a static locally served script, no tracking. */
const WORD_BANK_PAGE_SIZE=24;
function getWordBankEntries(){return typeof IELTS_VOCAB_BANK!=='undefined'&&Array.isArray(IELTS_VOCAB_BANK.entries)?IELTS_VOCAB_BANK.entries:[]}
function filteredWordBank(){
 const query=wordBankQuery.trim().toLocaleLowerCase();
 return getWordBankEntries().map((entry,index)=>({entry,index})).filter(({entry})=>{
  if(wordBankTopic!=='all'&&String(entry[4])!==wordBankTopic)return false;
  if(!query)return true;
  if(wordBankExact)return entry[0].toLocaleLowerCase()===query;
  return [entry[0],entry[1],entry[2],entry[3]].some(value=>String(value).toLocaleLowerCase().includes(query));
 });
}
function wordBankCard({entry,index}){
 const [word,meaning,burmese,example,topicId]=entry;
 const topics=typeof IELTS_VOCAB_BANK!=='undefined'?IELTS_VOCAB_BANK.topics:[];
 return `<article class="word-bank-card"><div class="word-bank-card-top"><span class="word-bank-number">${String(index+1).padStart(4,'0')} / 1000</span><span class="word-bank-tag">${E(topics[topicId]||'Academic')}</span></div>
 <div class="word-bank-head"><h3>${E(word)}</h3><button type="button" class="word-bank-sound" data-action="word-bank-say" data-idx="${index}" aria-label="Hear pronunciation of ${E(word)}">🔊 <span>Listen</span></button></div>
 <div class="word-bank-definition" id="wordDef${index}"><p class="word-bank-label">MEANING · အဓိပ္ပာယ်</p><p class="word-bank-english">${E(meaning)}</p><p class="word-bank-burmese" lang="my">${E(burmese)}</p>
 <p class="word-bank-label">USAGE · အသုံးပြုပုံ</p><blockquote class="word-bank-example">${E(example)}</blockquote></div>
 <div class="word-bank-card-actions"><button class="btn outline sm" type="button" data-action="word-bank-example" data-idx="${index}">▶ Read example</button><button class="word-bank-cover" type="button" data-action="word-bank-cover" data-idx="${index}" aria-controls="wordDef${index}" aria-expanded="true">Hide meaning</button></div></article>`;
}
function wordBankResultMarkup(){
 const filtered=filteredWordBank();const maxPage=Math.max(0,Math.ceil(filtered.length/WORD_BANK_PAGE_SIZE)-1);
 wordBankPage=Math.max(0,Math.min(wordBankPage,maxPage));
 const first=wordBankPage*WORD_BANK_PAGE_SIZE,last=Math.min(filtered.length,first+WORD_BANK_PAGE_SIZE);
 const cards=filtered.slice(first,last).map(wordBankCard).join('');
 return `<div class="word-bank-resultbar"><strong>${filtered.length.toLocaleString('en-GB')} of 1,000 words</strong><span>${filtered.length?`Showing ${first+1}–${last}`:'Try a different word or topic'}</span></div>
 ${filtered.length?`<div class="word-bank-grid">${cards}</div><nav class="word-bank-pagination" aria-label="Vocabulary pages"><button type="button" class="btn outline" data-action="word-bank-prev" ${wordBankPage===0?'disabled':''}>← Previous</button><span>Page ${wordBankPage+1} of ${maxPage+1}</span><button type="button" class="btn outline" data-action="word-bank-next" ${wordBankPage>=maxPage?'disabled':''}>Next →</button></nav>`:
 `<div class="word-bank-empty"><h2>No matches found</h2><p>Try another spelling, remove the topic filter or search for a meaning in English or Burmese.</p><button type="button" data-action="word-bank-reset" class="btn primary">Show all 1,000 words</button></div>`}`;
}
function updateWordBankResults(scroll=false){const target=document.getElementById('wordBankResults');if(!target)return;target.innerHTML=wordBankResultMarkup();if(scroll){document.getElementById('wordBankFilters')?.scrollIntoView({behavior:'auto',block:'start'});}}
function renderIELTSVocabulary(){
 const entries=getWordBankEntries(),topics=typeof IELTS_VOCAB_BANK==='undefined'?[]:IELTS_VOCAB_BANK.topics;
 return `<div class="page word-bank-page"><a class="back-link" href="#ielts">← Back to IELTS Lab</a>
 <section class="word-bank-hero"><div class="word-bank-hero-text"><span class="eyebrow">IELTS VOCABULARY · ENGLISH + မြန်မာ</span><h1>1,000 words.<br><em>More ways to say it.</em></h1><p>From science to society, learn useful academic and everyday vocabulary with clear meanings, Burmese support and natural example sentences.</p><p class="word-bank-hero-mm" lang="my">အကြောင်းအရာ ၂၀ မျိုးခွဲထားတဲ့ ဝေါဟာရ ၁,၀၀၀ ကို အဓိပ္ပာယ်၊ မြန်မာဘာသာနဲ့ အသုံးချဝါကျတွေနဲ့ လေ့လာပါ။</p><div class="word-bank-facts"><span>✦ 1,000 entries</span><span>✦ 20 topics</span><span>✦ British voice</span><span>✦ No tracking</span></div></div><div class="word-bank-hero-number" aria-hidden="true"><strong>1000</strong><span>WORDS / စကားလုံးများ</span></div></section>
 <div class="word-bank-help"><strong>How to learn:</strong> Search by a word or meaning, choose a topic, press 🔊 to hear pronunciation, and try saying the example aloud. Use the top <strong>Voices</strong> button to change the British voice. Your search, study actions and word history are <strong>not saved</strong>. <span lang="my">သင်ယူခဲ့သည့် စကားလုံးမှတ်တမ်းကို မသိမ်းပါ။</span></div>
 <section class="word-bank-controls" id="wordBankFilters" aria-label="Vocabulary filters"><div class="word-bank-search-field"><label for="ieltsVocabSearch">Search vocabulary · ရှာဖွေရန်</label><input id="ieltsVocabSearch" class="search" type="search" autocomplete="off" spellcheck="false" placeholder="Try sustainability, စီးပွားရေး, example…" value="${E(wordBankQuery)}"></div><div class="word-bank-topic-field"><label for="ieltsVocabTopic">Topic · အကြောင်းအရာ</label><select id="ieltsVocabTopic" class="filter"><option value="all">All 20 topics · 1,000 words</option>${topics.map((topic,i)=>`<option value="${i}" ${wordBankTopic===String(i)?'selected':''}>${E(topic)} · 50</option>`).join('')}</select></div><button class="btn soft word-bank-surprise" type="button" data-action="word-bank-surprise">✦ Surprise me</button></section>
 <div id="wordBankResults" aria-live="polite">${wordBankResultMarkup()}</div>
 <section class="word-bank-bottom-note"><h2>Words are a starting point, not a band score.</h2><p>This is an independently curated learning bank, <strong>not an official IELTS vocabulary list or an IELTS-endorsed product</strong>. Learning 1,000 words cannot guarantee a test result. Practise accurate meaning, natural collocations and use in full sentences.</p><p class="mm" lang="my">IELTS စာမေးပွဲက တရားဝင် ထုတ်ပြန်ထားတဲ့ စကားလုံးစာရင်း မဟုတ်ပါ။ စာလုံးတွေကို အဓိပ္ပာယ်နားလည်ပြီး ဝါကျထဲမှာ သဘာဝကျကျ အသုံးချလေ့ကျင့်ပါ။</p></section>
 </div>`;
}

function renderReview(){return `<div class="page"><span class="eyebrow">WORD PLAY · ပြန်လည်လေ့ကျင့်ခြင်း</span><h1>Pick a word. Make it yours.</h1><p class="muted">No scheduled reminders, ratings or saved review history. Choose any lesson to revisit its vocabulary whenever you like.</p><div class="review-hero"><span class="eyebrow">ANY DAY, ANY WORD</span><h2>A word is a tiny adventure.</h2><p>Say it. Try it. Remember it your way.</p><a class="btn light" href="#lesson/1/vocab">Try Lesson 01 words →</a> <a class="btn ghost" href="#ielts-vocabulary">Explore 1,000 IELTS words ↗</a></div><div class="section-head"><div><span class="eyebrow">PICK A LESSON</span><h2>Word practice library</h2></div></div><div class="lesson-list">${LESSONS.map(l=>`<a class="lesson-item" href="#lesson/${l.id}/vocab"><span class="lesson-index">${String(l.id).padStart(2,'0')}</span><div class="lesson-info"><span class="lesson-level">${E(l.level)}</span><h3>${E(l.title)}</h3><p class="mm">${E(l.myanmarTitle)}</p><span class="lesson-state">5 words · practise now →</span></div></a>`).join('')}</div></div>`}
function refreshReview(){document.getElementById('app').innerHTML=renderReview()}

function gymPick(level){let pool=LESSONS.filter(l=>level==='all'||l.level===level).map(l=>({ ...l.quiz.find(q=>q.skill==='Grammar'),lesson:l.id,topic:l.title})).filter(x=>x.q);
 for(let i=pool.length-1;i>0;i--){let j=Math.floor(Math.random()*(i+1));[pool[i],pool[j]]=[pool[j],pool[i]]}return pool.slice(0,Math.min(10,pool.length))}
function renderGym(level){gymLevel=TRACKS.some(t=>t[0]===level)?level:'all';if(!gymQuestions.length)gymQuestions=gymPick(gymLevel);return `<div class="page"><span class="eyebrow">EXTRA PRACTICE • သဒ္ဒါထပ်လေ့ကျင့်ခြင်း</span><h1>Grammar Gym</h1><p class="muted">Ten mixed questions with explanations, drawn from 54 grammar patterns across the course. Change the level to target one stage. Repeat with a fresh set to practise retrieval.</p><div class="toolbar"><select class="filter" id="gymLevel" aria-label="Grammar level"><option value="all">Mixed — all levels</option>${TRACKS.map(x=>`<option value="${E(x[0])}" ${gymLevel===x[0]?'selected':''}>${E(x[0])} — ${E(x[1])}</option>`).join('')}</select><button class="btn outline" type="button" data-action="gym-new">↻ New question set</button></div><div id="gymArea">${gymQuestions.map((q,i)=>`<div class="mock-question"><p class="statline">From Lesson ${q.lesson}: ${E(q.topic)}</p>${qHtml(q,'gym'+i,i)}</div>`).join('')}</div><div class="toolbar-actions"><button class="btn primary" type="button" data-action="gym-check">Check my answers</button></div><div id="gymResult" aria-live="polite"></div><p class="note-small">One short question cannot validate mastery of a grammar topic. If you missed one, revisit the related lesson and create three original examples.</p></div>`}
function renderGymInPlace(){document.getElementById('app').innerHTML=renderGym(gymLevel)}
function checkGym(){let result=scoreQuestions(gymQuestions,'gym');let el=document.getElementById('gymResult');if(result.missing){el.innerHTML=`<div class="result-banner fail">Answer all ${gymQuestions.length} questions first. ${result.missing} missing.</div>`;return}el.innerHTML=`<div class="result-banner">${result.score}/${gymQuestions.length} answered correctly. Review each explanation and try a fresh set.</div>`;toast('Grammar practice checked.')}

function renderIELTS(){return `<div class="page"><span class="eyebrow">IELTS PRACTICE STUDIO</span><h1>Prepare with the right test.</h1><p>Choose Academic or General Training. The two tests share listening and speaking formats, but their reading content and Writing Task 1 requirements differ.</p><div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(270px,1fr))"><article class="panel"><span class="level-pill purple">IELTS Academic</span><h2>University and academic contexts</h2><p>Academic-style passages, chart/process description and essay tasks.</p><div class="toolbar-actions"><a href="#courses/IELTS%20Academic" class="btn primary">6 guided lessons</a><button class="btn outline" data-action="mock-start" data-type="IELTS Academic">20-minute mini check</button></div></article><article class="panel"><span class="level-pill purple">IELTS General Training</span><h2>Everyday and workplace contexts</h2><p>General-style passages, formal/informal letters and essay tasks.</p><div class="toolbar-actions"><a href="#courses/IELTS%20General" class="btn primary">6 guided lessons</a><button class="btn outline" data-action="mock-start" data-type="IELTS General">20-minute mini check</button></div></article></div>
 <div class="panel ielts-vocab-cta"><div><span class="eyebrow">IELTS VOCABULARY</span><h2>1,000 words for curious minds</h2><p>20 topics · simple meanings in English and Burmese · original example sentences · British voice practice. Search by word or topic, without creating an account.</p></div><a class="btn primary" href="#ielts-vocabulary">Open the vocabulary bank →</a></div>
 <div class="panel"><h2>Writing task reminder</h2><div class="sample-grid"><div class="tiny-panel"><h4>Academic Task 1</h4><p>Describe visual information such as a graph, table or process. At least 150 words; about 20 minutes.</p></div><div class="tiny-panel"><h4>General Training Task 1</h4><p>Write a letter responding to a situation. At least 150 words; about 20 minutes.</p></div><div class="tiny-panel"><h4>Task 2 (both)</h4><p>Write an essay responding to an argument or problem. At least 250 words; about 40 minutes.</p></div><div class="tiny-panel"><h4>Speaking (both)</h4><p>Practice personal questions, a long turn and deeper discussion. Genuine scoring requires skilled human assessment.</p></div></div><p class="note-small" style="margin-top:17px">Official guidance: <a href="https://ielts.org/take-a-test/test-types/ielts-academic-test/ielts-academic-format-writing" target="_blank" rel="noopener noreferrer">Academic writing</a> · <a href="https://ielts.org/take-a-test/test-types/ielts-general-training-test/ielts-general-training-format-writing" target="_blank" rel="noopener noreferrer">General Training writing</a>. These links require internet.</p></div>
 <div class="notice amber"><strong>About the mini checks:</strong> These are original 12-question, 20-minute reading-and-listening practice sets, <em>not</em> full-length IELTS mock examinations. Browser-generated audio does not replicate the actual listening test. Objective scores are not IELTS bands.</div></div>`}
function renderMock(type){if(type!=='IELTS Academic'&&type!=='IELTS General')return renderIELTS();if(!state.activeMock||state.activeMock.type!==type)return `<div class="page"><h1>${E(type)} mini check</h1><p>This check has twelve original objective questions and a 20-minute timer. It is not a full IELTS mock examination.</p><button class="btn primary" data-action="mock-start" data-type="${E(type)}">Begin practice check</button></div>`;
 let mock=state.activeMock,ls=levelLessons(type),elapsed=Math.floor((Date.now()-mock.startedAt)/1000),remaining=Math.max(0,1200-elapsed);
 return `<div class="page"><a class="back-link" href="#ielts">← Back to IELTS Lab</a><span class="eyebrow">ORIGINAL TIMED PRACTICE • NOT A FULL IELTS EXAM</span><h1>${E(type)} · 12 questions</h1><p class="muted">Read each short text for its reading item. For listening items, click Play audio and answer from what you hear. The transcript is not shown during the exercise.</p>
 <div id="mockItems">${ls.map((l,k)=>`<section class="panel"><span class="level-pill">SECTION ${k+1}</span><h3>${E(l.title)}</h3><h4>Reading passage</h4><p>${E(l.reading)}</p>${qHtml(l.quiz[0],'mock'+(k*2),k*2)}<div class="mini-divider"></div><h4>Listening item</h4><button type="button" class="btn soft sm" data-action="mock-audio" data-lesson="${l.id}">🔊 Play section ${k+1} recording</button>${qHtml(l.quiz[2],'mock'+(k*2+1),k*2+1)}</section>`).join('')}</div><div class="mock-tools"><div><span class="timer" id="mockTimer">${Math.floor(remaining/60).toString().padStart(2,'0')}:${(remaining%60).toString().padStart(2,'0')}</span><span class="note-small"> · 20-minute recommended limit</span></div><button type="button" class="btn primary" data-action="mock-submit">Submit 12 answers</button></div><div id="mockResult" aria-live="polite"></div></div>`}
function renderGuide(){return `<div class="page"><span class="eyebrow">YOUR STUDY HANDBOOK</span><h1>Make it your own.</h1><p class="muted mm">သင်ခန်းစာအားလုံးကို လွတ်လပ်စွာ ရွေးချယ်လေ့လာနိုင်ပါတယ်။ Website က သင့်ရဲ့ သင်ယူမှုမှတ်တမ်းကို မသိမ်းပါ။</p>
 <div class="cards">${[['01','Pick any lesson','You are free to start at the level that suits you.'],['02','Practise in small steps','Read, listen, speak, write and check your own answers.'],['03','Keep a personal note','If you want to continue tomorrow, note your last lesson number yourself.'],['04','Return when ready','Open any lesson again. There are no streaks, accounts or completion scores.'],['05','Be mindful of drafts','Writing is temporary; copy it before moving away from the page.'],['06','Stay in control','Clear this session and previous-version browser data whenever you like.']].map(([no,title,desc])=>`<article class="card"><span class="level-pill">${no}</span><h3>${E(title)}</h3><p>${E(desc)}</p></article>`).join('')}</div>
 <div class="panel"><h2>Learning roadmap</h2><p><strong>A1–A2:</strong> daily phrases and useful grammar. <strong>B1–B2:</strong> conversations, explanations and practical work English. <strong>C1:</strong> critical reading and nuanced communication. <strong>IELTS:</strong> independent practice for Academic and General Training, not official examinations.</p></div>
 <div class="panel"><h2>Voices are yours to choose</h2><p>Open <strong>🔊 Voices</strong> for British Male/Female options available on your device. Preferences last only during the open page and reset after refresh.</p><button class="btn outline" type="button" data-action="voice-open">Choose a voice</button></div>
 <div class="panel"><h2>Privacy & old saved data</h2><p>This edition never saves learning progress. If you used an earlier Academy version, old local browser entries may remain until you clear them. Clear your session and those old entries with the button below.</p><p class="mm">ယခင် Version က Browser ထဲ သိမ်းခဲ့တဲ့ Data တွေကို ဖျက်ချင်ရင် အောက်ကခလုတ်ကို သုံးနိုင်ပါတယ်။</p><div class="toolbar-actions"><button type="button" class="btn danger" data-action="clear-session">Clear session & old saved data</button><a href="privacy.html" class="btn outline">Read privacy notice</a></div></div>
 <div class="notice amber"><strong>Important:</strong> Refreshing or leaving the page clears practice entries. Browser speech voices may rely on device or vendor services. All IELTS-style exercises are original learning approximations and do not provide an official IELTS band score.</div></div>`}
function getPicked(name){let v=document.querySelector(`input[name="${name}"]:checked`);return v===null?null:Number(v.value)}
function paintAnswer(name,q,v){let box=document.querySelector(`[data-feedback="${name}"]`);if(!box)return;let correct=(v===q.a),answer=q.options[q.a];box.innerHTML=`<div class="answer ${correct?'':'bad'}"><strong>${correct?'✓ Correct':'✗ Not quite'}.</strong> ${E(q.why)}<br><span class="note-small">Answer: ${E(answer)}</span></div>`;return correct}
function scoreQuestions(list,prefix){let score=0,missing=0;list.forEach((q,i)=>{let name=prefix+i,v=getPicked(name);if(v===null){let target=document.querySelector(`[data-feedback="${name}"]`);if(target)target.innerHTML='<div class="answer bad">Choose an answer first.</div>';missing++;return}if(paintAnswer(name,q,v))score++});return {score,missing}}
function checkReading(){let l=currentLesson();if(!l)return;let r=scoreQuestions(l.readingQuestions,'rd');if(r.missing===0){markSkill(l,'Reading');toast(`Reading checked: ${r.score}/2. Review any mistakes.`)}else toast('Please answer both reading questions.')}
function checkGrammar(){let l=currentLesson(),q=l.quiz.find(q=>q.skill==='Grammar');let v=getPicked('grammar-q');if(v===null){toast('Choose a grammar answer first.');return}paintAnswer('grammar-q',q,v);markSkill(l,'Grammar');toast('Grammar checked. Review the rule and retry if needed.')}
function checkListening(){let l=currentLesson(),v=getPicked('listening-q'),dict=document.getElementById('dictInput').value;if(v===null||!norm(dict)){toast('Answer the listening question and type the dictation.');return}paintAnswer('listening-q',l.audioQuestion,v);let a=norm(l.dictation).split(' '),b=norm(dict).split(' '),matched=0;let dp=Array.from({length:b.length+1},()=>0);for(let i=1;i<=a.length;i++){let next=[0];for(let j=1;j<=b.length;j++)next[j]=a[i-1]===b[j-1]?dp[j-1]+1:Math.max(dp[j],next[j-1]);dp=next}matched=dp[b.length];let pct=percent(matched,Math.max(a.length,b.length));document.getElementById('dictFeedback').innerHTML=`<div class="answer"><strong>Dictation word match: about ${pct}%</strong><p>Expected: ${E(l.dictation)}</p><p>This is an approximate word comparison, not an official listening score. Notice any missing, extra or changed words.</p></div>`;document.getElementById('listenTranscript').hidden=false;markSkill(l,'Listening');toast('Listening checked. Nothing has been saved.')}
function checkQuiz(){
 let l=currentLesson();if(!l)return;let r=scoreQuestions(l.quiz,'quiz');let el=document.getElementById('quizResult');
 if(r.missing){el.innerHTML=`<div class="result-banner fail">Answer all five questions first. ${r.missing} still unanswered.</div>`;return}
 el.innerHTML=`<div class="result-banner ${r.score>=4?'':'fail'}">${r.score}/5 · ${r.score>=4?'Great work!':'Review the feedback and try again.'}</div><p class="note-small">This result is visible only on this page. No quiz history, score or lesson completion is saved.</p>`;
 toast(`Quiz result: ${r.score}/5 · not saved`)
}
function currentLesson(){let parts=decodeURIComponent(location.hash.replace(/^#/,'' )).split('/');return parts[0]==='lesson'?tr(parts[1]):null}
/* Voice selection is temporary in this tab: no persistent browser storage. */
let voicePreferences={gender:'male',voiceId:''};
function saveVoicePreferences(){} // Selection is lost on refresh by design.

// UK ONLY: Do not expose, select, or fall back to US/AU/other English voices.
// Web Speech voices are supplied by the visitor's browser, not by this website.
function voiceIsBritish(v){return /^en[-_]GB(?:$|[-_])/i.test(String(v?.lang||''))}
function voiceGenderHint(v){
 const n=String(v?.name||'');
 if(/\b(ryan|george|daniel|david|james|oliver|guy|mark|alfie|thomas|arthur|brian|harry|fred|male|man)\b/i.test(n))return 'male';
 if(/\b(sonia|libby|hazel|kate|susan|emily|charlotte|emma|olivia|amy|jenny|serena|maisie|martha|female|woman)\b/i.test(n))return 'female';
 // Browser APIs do not expose a reliable gender property; these are name-only hints.
 return '';
}
function voiceIsNatural(v){return /\b(natural|neural|premium|enhanced|high.quality)\b/i.test(String(v?.name||''))}
function voiceId(v){return [v.voiceURI||'',v.name||'',v.lang||''].join('||')}
function voiceQualityScore(v){
 // Advertised neural/natural voices usually sound more human than basic system voices,
 // but these labels are not a quality guarantee and not present on every platform.
 const n=String(v?.name||'');
 return (voiceIsNatural(v)?100:0)+(v.localService===false?8:0)+(v.default?1:0);
}
function britishVoices(){
 if(!('speechSynthesis'in window))return [];
 return (speechSynthesis.getVoices()||[]).filter(voiceIsBritish).slice().sort((a,b)=>
   voiceQualityScore(b)-voiceQualityScore(a)||String(a.name||'').localeCompare(String(b.name||'')));
}
function resolveVoice(){
 const voices=britishVoices();
 const chosen=voices.find(v=>voicePreferences.voiceId===voiceId(v))||null;
 const byGender=voices.filter(v=>voiceGenderHint(v)===voicePreferences.gender);
 const unknown=voices.filter(v=>!voiceGenderHint(v));
 const voice=chosen||byGender[0]||unknown[0]||voices[0]||null;
 return {voice,voices,manual:!!chosen,exactGender:!!voice&&voiceGenderHint(voice)===voicePreferences.gender};
}
function refreshVoicePanel(){
 const gender=document.getElementById('voiceGender'),pick=document.getElementById('voiceChoice'),status=document.getElementById('voiceStatus');
 if(!gender||!pick||!status)return;
 gender.value=voicePreferences.gender;
 const selected=resolveVoice();
 let choices='<option value="">Automatic — best available UK '+voicePreferences.gender+' voice</option>';
 for(const v of selected.voices){
  const hint=voiceGenderHint(v);
  let desc='British English (en-GB)';
  if(voiceIsNatural(v))desc+=' · Natural/Neural labelled';
  if(hint)desc+=' · '+hint+' (name hint)';
  choices+='<option value="'+E(voiceId(v))+'">'+E(v.name)+' — '+E(desc)+'</option>';
 }
 pick.innerHTML=choices;
 pick.value=selected.voices.some(v=>voiceId(v)===voicePreferences.voiceId)?voicePreferences.voiceId:'';
 pick.disabled=!selected.voices.length;
 document.getElementById('voicePreview').disabled=!selected.voices.length;
 if(!('speechSynthesis'in window)){
   status.textContent='Your browser does not support text-to-speech. Please try a recent Microsoft Edge or Chrome.';
 }else if(!selected.voice){
   status.textContent='No British (en-GB) voice is available in this browser. We will NOT substitute US English. Try Microsoft Edge with UK voices enabled, or install an English (United Kingdom) voice in your device settings.';
 }else{
   let note=selected.exactGender?'':'The browser cannot verify the requested male/female voice; listen to the preview. ';
   let quality=voiceIsNatural(selected.voice)?' · labelled Natural/Neural':' · standard device voice';
   status.textContent=note+'Playing only British English: '+selected.voice.name+quality+'. For a more human-sounding voice, use an available UK Natural voice (often in Microsoft Edge).';
 }
}
function playSpeech(text,slow=false,preview=false){
 if(!('speechSynthesis'in window)){toast('Text-to-speech is not supported by this browser.');return}
 const selected=resolveVoice();
 if(!selected.voice){refreshVoicePanel();toast('A British English (en-GB) voice is required. No US accent fallback.');return}
 const synth=window.speechSynthesis;
 synth.cancel();
 const utterance=new SpeechSynthesisUtterance(String(text??''));
 utterance.voice=selected.voice;
 utterance.lang='en-GB';
 // The browser's normal rate preserves a voice's own prosody better than 0.85x playback.
 utterance.rate=preview?1:(slow?Math.max(.65,state.speed-.22):state.speed);
 utterance.pitch=1;
 synth.speak(utterance);
}
function playFor(action){let l=currentLesson();if(!l)return;let which=action?.dataset.text||'audio';if(which.endsWith('reading'))playSpeech(l.reading,which.startsWith('slow'));else playSpeech(l.audio,which.startsWith('slow'))}
function showWritingStatus(){
 const l=currentLesson(),area=document.getElementById('writingText');if(!l||!area)return;
 const words=countWords(area.value);
 document.getElementById('wordCount').textContent=`${words} words written · target ${l.minWords||60}+`;
 document.getElementById('draftStatus').textContent='Not saved · copy before leaving';
}
function coachWriting(){let l=currentLesson();if(!l)return;showWritingStatus();let s=document.getElementById('writingText')?.value||'',output=document.getElementById('writingCoach');if(!s.trim()){output.innerHTML='<div class="answer bad">Write a few sentences first to receive basic pattern suggestions.</div>';return}
 let rules=[[/\bi am agree\b/i,'Use “I agree”, not “I am agree”.'],[/\b(?:more better|more easier|more faster)\b/i,'Avoid double comparatives: better, easier or faster.'],[/\bdid(?: not|n[’\']t) went\b/i,'After did/did not, use the base form “go”.'],[/\b(?:he|she) don[’\']t\b/i,'For he/she, use “doesn’t” instead of “don’t”.'],[/\b(?:informations|advices|equipments)\b/i,'Information, advice and equipment are normally uncountable nouns.'],[/\bdiscuss about\b/i,'Usually say “discuss the topic”, without “about”.'],[/\blook forward to hear\b/i,'After “look forward to”, use -ing: “hearing”.'],[/\b(?:he|she) go to\b/i,'Check present simple: “he/she goes” for a usual activity.'],[/\bpeople is\b/i,'Use “people are” for the plural.'],[/\b(?:I|we) has\b/i,'Use “I/we have” in standard present tense.'],[/\b(?:it|he|she) have been\b/i,'Check agreement: “it/he/she has been”.'],[/\b(?:an university|a apple|an book)\b/i,'Check a/an by sound: “a university”, “an apple”, “a book”.']];
 let notes=rules.filter(([re])=>re.test(s)).map(([,msg])=>msg);let wc=countWords(s),paras=s.split(/\n\s*\n/g).filter(x=>x.trim()).length;
 if(l.level.startsWith('IELTS')&&wc>=150&&paras<=1)notes.push('Your answer appears to have one paragraph. Consider whether separate introduction, body and conclusion paragraphs would help.');
 if(!/[.!?]\s*$/.test(s.trim()))notes.push('Check that the final sentence ends with suitable punctuation.');
 let wordCount=new Map();toWords(s).forEach(w=>{w=w.toLowerCase();if(['very','good','bad','thing','things','important'].includes(w))wordCount.set(w,(wordCount.get(w)||0)+1)});for(let [w,n] of wordCount)if(n>=4)notes.push(`You repeated “${w}” ${n} times. Consider more precise wording where appropriate.`);
 if(!notes.length)notes.push('No common patterns were detected by these limited checks. Reread your answer and ask a teacher to check accuracy, coherence and task response.');
 output.innerHTML=`<div class="sample" style="margin-top:15px"><strong>Writing coach · basic pattern hints</strong><p class="note-small">${wc} words · ${paras} paragraph(s). These simple pattern checks can miss errors or raise false positives.</p><ul class="hint-list">${notes.slice(0,7).map(n=>`<li>${E(n)}</li>`).join('')}</ul></div>`}
function checkWriting(){
 let l=currentLesson();if(!l)return;showWritingStatus();let words=countWords(document.getElementById('writingText')?.value||''),target=l.minWords||60,checked=document.querySelectorAll('.write-check:checked').length;
 let box=document.getElementById('writingFeedback');
 if(words<target){box.innerHTML=`<div class="answer bad">${words} words so far. Target: ${target}+. Nothing is saved; copy your work before leaving.</div>`;return}
 if(checked<4){box.innerHTML=`<div class="answer bad">Complete the four self-review checks first (${checked}/4). Nothing is saved.</div>`;return}
 box.innerHTML='<div class="answer"><strong>✓ Practice checked.</strong> You met the word target and completed the self-review list. This response is not saved or officially graded.</div>';
 toast('Writing checked · not saved.');
}
function addDays(n){let d=new Date();d.setDate(d.getDate()+n);return [d.getFullYear(),String(d.getMonth()+1).padStart(2,'0'),String(d.getDate()).padStart(2,'0')].join('-')}
function rateCard(){} // No spaced repetition history or ratings are recorded.
let writerSecondsLeft=0;
function clearLessonTimer(){if(timerHandle){clearInterval(timerHandle);timerHandle=null}}
function formatSeconds(n){return `${String(Math.floor(n/60)).padStart(2,'0')}:${String(Math.max(0,n)%60).padStart(2,'0')}`}
function timerStart(n){let el=document.getElementById('lessonTimer');if(!el)return;if(!writerSecondsLeft)writerSecondsLeft=n*60;clearLessonTimer();timerEndsAt=Date.now()+writerSecondsLeft*1000;timerHandle=setInterval(()=>{writerSecondsLeft=Math.max(0,Math.ceil((timerEndsAt-Date.now())/1000));if(el)el.textContent=formatSeconds(writerSecondsLeft);if(writerSecondsLeft<=0){clearLessonTimer();toast('Writing time finished. You can still revise your answer.')}},500)}
function timerPause(){if(!timerHandle)return;writerSecondsLeft=Math.max(0,Math.ceil((timerEndsAt-Date.now())/1000));clearLessonTimer()}
function timerReset(n){clearLessonTimer();writerSecondsLeft=n*60;let el=document.getElementById('lessonTimer');if(el)el.textContent=formatSeconds(writerSecondsLeft)}
function downloadText(filename,body,mime='text/plain'){let url=URL.createObjectURL(new Blob([body],{type:mime})),a=document.createElement('a');a.href=url;a.download=filename;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000)}
function clearRecordingSession(updateMessage=true){
 recordingGeneration++;recordDeletePending=true;
 try{if(recorder&&recorder.state==='recording')recorder.stop()}catch(e){}
 if(recordingStream){try{recordingStream.getTracks().forEach(track=>track.stop())}catch(e){} recordingStream=null}
 if(recogniser){try{recogniser.abort()}catch(e){} recogniser=null}
 if(recordedAudioURL){try{URL.revokeObjectURL(recordedAudioURL)}catch(e){} recordedAudioURL=null}
 recordedChunks=[]; recorder=null;
 const target=document.getElementById('recordPlayback');if(target)target.replaceChildren();
 const status=document.getElementById('recordStatus');if(status){status.classList.remove('recording');if(updateMessage)status.textContent='Recording deleted from this browser session.'}
}
async function startRecord(){
 const status=document.getElementById('recordStatus');if(!status)return;
 if(!navigator.mediaDevices?.getUserMedia||typeof MediaRecorder==='undefined'){
  status.textContent='Microphone recording is unavailable. Practise aloud instead.';return;
 }
 clearRecordingSession(false);recordDeletePending=false;const sessionGeneration=recordingGeneration;
 try{
  const stream=await navigator.mediaDevices.getUserMedia({audio:true});
  if(recordDeletePending||sessionGeneration!==recordingGeneration||!document.getElementById('recordStatus')){stream.getTracks().forEach(t=>t.stop());return}
  recordingStream=stream;
  const media=new MediaRecorder(stream);recorder=media;recordedChunks=[];
  media.ondataavailable=e=>{if(!recordDeletePending&&e.data.size)recordedChunks.push(e.data)};
  media.onstop=()=>{
   stream.getTracks().forEach(t=>t.stop());if(recordingStream===stream)recordingStream=null;
   if(recordDeletePending||recorder!==media)return;
   const blob=new Blob(recordedChunks,{type:media.mimeType||'audio/webm'});
   recordedAudioURL=URL.createObjectURL(blob);
   const parent=document.getElementById('recordPlayback');
   if(parent)parent.innerHTML=`<audio controls src="${E(recordedAudioURL)}" style="width:100%;margin-top:12px"></audio><p class="note-small">Only in this page session. Delete it or leave Speaking to clear it. No Academy audio uploads.</p>`;
   const current=document.getElementById('recordStatus');if(current)current.textContent='Recording stopped. Listen back or delete it.';
  };
  media.start();status.textContent='● Recording… Stop or delete when finished.';status.classList.add('recording');
 }catch(e){if(recordingStream){recordingStream.getTracks().forEach(t=>t.stop());recordingStream=null}status.textContent='Microphone unavailable or permission denied. You can practise without recording.'}
}
function stopRecord(){if(recorder&&recorder.state==='recording')recorder.stop();const el=document.getElementById('recordStatus');if(el)el.classList.remove('recording')}
function speechRecognize(){const el=document.getElementById('recordStatus');if(el)el.textContent='Speech-to-text is disabled in the privacy-test build to prevent unverified third-party audio processing.'}
function speakingCheck(){let l=currentLesson();if(!l)return;let all=[...document.querySelectorAll('#sp1,#sp2,#sp3')].every(x=>x.checked);let el=document.getElementById('speakFeedback');if(!all){el.innerHTML='<div class="answer bad">Complete the three self-reflection checks after genuine speaking practice.</div>';return}markSkill(l,'Speaking');el.innerHTML='<div class="answer">✓ Speaking self-review complete on this page only. An examiner or teacher is needed for reliable proficiency feedback.</div>';toast('Speaking practice checked · not saved.')}
function mockStart(type){if(!['IELTS Academic','IELTS General'].includes(type))return;state.activeMock={type,startedAt:Date.now()};save();location.hash='#mock/'+encodeURIComponent(type);route()}
let mockClock=null;
function startMockClock(){if(mockClock)clearInterval(mockClock);let el=document.getElementById('mockTimer');if(!el||!state.activeMock)return;const tick=()=>{let el=document.getElementById('mockTimer');if(!el){clearInterval(mockClock);mockClock=null;return}let rem=Math.max(0,1200-Math.floor((Date.now()-state.activeMock.startedAt)/1000));el.textContent=formatSeconds(rem);if(rem===0){clearInterval(mockClock);mockClock=null;toast('20 minutes elapsed. Submit when ready; late submissions are labelled.')}};tick();mockClock=setInterval(tick,1000)}
function submitMock(){if(!state.activeMock)return;let type=state.activeMock.type,ls=levelLessons(type).slice(0,6),questions=ls.flatMap(l=>[l.quiz[0],l.quiz[2]]);let r=scoreQuestions(questions,'mock');if(r.missing){toast(`Please complete all questions (${r.missing} unanswered).`);return}let elapsed=Math.floor((Date.now()-state.activeMock.startedAt)/1000),late=elapsed>1200;state.activeMock=null;save();if(mockClock)clearInterval(mockClock);document.querySelector('.mock-tools').innerHTML=`<strong>Practice check complete · ${r.score}/12 · ${late?'Over the 20-minute target':'Within the 20-minute target'}</strong><a class="btn primary" href="#ielts">Back to IELTS Lab</a>`;document.getElementById('mockResult').innerHTML=`<div class="result-banner">${r.score} of 12 original questions correct. Review feedback above. This is <strong>not an IELTS band score</strong>.</div>`;toast('Mini check finished · not saved.')}
function clearPracticeSession(){
 if(!confirm('Clear current practice and remove saved data from older Burmese English Academy versions on this browser? This cannot be undone.'))return;
 clearRecordingSession(false);clearLessonTimer();
 if('speechSynthesis' in window)window.speechSynthesis.cancel();
 const keys=['bea-complete-v1','bea-unit1-progress-v1','bea-voice-settings-v1','bea-privacy-ack-v1','bea-beta-privacy-ack-v1','bea-policy-ack-v1'];
 for(const storageName of ['localStorage','sessionStorage']){
  try{const storage=window[storageName];for(const k of keys)storage.removeItem(k)}catch(e){}
 }
 state=defaultState();voicePreferences={gender:'male',voiceId:''};
 gymQuestions=[];activeFlash=null;searchQuery='';filterLevel='all';
 if(mockClock){clearInterval(mockClock);mockClock=null}
 try{history.replaceState(null,'',location.pathname+location.search+'#home')}catch(e){location.hash='#home'}
 route();refreshVoicePanel();toast('Session cleared. Old Academy browser data removed where accessible.');
}

document.addEventListener('click',async function(ev){let node=ev.target.closest('[data-action]');if(!node)return;let action=node.dataset.action;if(!action)return;ev.preventDefault();const l=currentLesson();
 switch(action){
 case 'reading-check':checkReading();break;
 case 'grammar-check':checkGrammar();break;
 case 'listening-check':checkListening();break;
 case 'listen-reveal':document.getElementById('listenTranscript').hidden=false;break;
 case 'quiz-submit':checkQuiz();break;
 case 'quiz-retry':if(l)document.getElementById('app').innerHTML=renderLesson(l,'quiz');break;
 case 'say':playFor(node);break;
 case 'say-stop':if('speechSynthesis'in window)window.speechSynthesis.cancel();break;
 case 'voice-open':document.getElementById('voiceSettingsToggle').click();document.getElementById('voiceSettingsPanel').scrollIntoView({behavior:'smooth',block:'start'});break;
 case 'vocab-audio':if(l)playSpeech(l.words[Number(node.dataset.idx)]?.[0]);break;
 case 'vocab-flip':{let id=Number(node.dataset.idx),el=document.getElementById('vocabMeaning'+id);if(el){el.hidden=!el.hidden;node.textContent=el.hidden?'Reveal':'Hide'}}break;
 
 case 'writing-check':checkWriting();break;
 case 'writing-coach':coachWriting();break;

 case 'timer-start':timerStart(Number(node.dataset.minutes));break;
 case 'timer-pause':timerPause();break;
 case 'timer-reset':timerReset(Number(node.dataset.minutes));break;
 case 'record-start':await startRecord();break;
 case 'record-stop':stopRecord();break;
 case 'record-delete':clearRecordingSession();break;

 case 'speech-recognize':speechRecognize();break; // deliberately disabled in privacy beta
 case 'speaking-check':speakingCheck();break;
 case 'flash-flip':{let el=document.getElementById('flashBack');el.hidden=!el.hidden;node.textContent=el.hidden?'Reveal meaning':'Hide meaning'}break;
 case 'flash-audio':if(activeFlash)playSpeech(activeFlash.word);break;

 case 'gym-new':gymQuestions=[];renderGymInPlace();break;
 case 'gym-check':checkGym();break;
 case 'mock-start':mockStart(node.dataset.type);break;
 case 'mock-audio':{let item=tr(node.dataset.lesson);if(item)playSpeech(item.audio)}break;
 case 'mock-submit':submitMock();break;


 case 'word-bank-say':{let e=getWordBankEntries()[Number(node.dataset.idx)];if(e)playSpeech(e[0]);}break;
 case 'word-bank-example':{let e=getWordBankEntries()[Number(node.dataset.idx)];if(e)playSpeech(e[3]);}break;
 case 'word-bank-cover':{let el=document.getElementById('wordDef'+node.dataset.idx);if(el){el.hidden=!el.hidden;node.textContent=el.hidden?'Reveal meaning':'Hide meaning';node.setAttribute('aria-expanded',String(!el.hidden));}}break;
 case 'word-bank-prev':wordBankPage=Math.max(0,wordBankPage-1);updateWordBankResults(true);break;
 case 'word-bank-next':wordBankPage++;updateWordBankResults(true);break;
 case 'word-bank-reset':wordBankQuery='';wordBankTopic='all';wordBankPage=0;wordBankExact=false;document.getElementById('ieltsVocabSearch').value='';document.getElementById('ieltsVocabTopic').value='all';updateWordBankResults();break;
 case 'word-bank-surprise':{let entries=getWordBankEntries();if(entries.length){let e=entries[Math.floor(Math.random()*entries.length)];wordBankQuery=e[0];wordBankTopic='all';wordBankPage=0;wordBankExact=true;document.getElementById('ieltsVocabSearch').value=wordBankQuery;document.getElementById('ieltsVocabTopic').value='all';updateWordBankResults();}}break;
 case 'clear-session':clearPracticeSession();break;
 }
});
document.addEventListener('input',e=>{
 if(e.target.id==='ieltsVocabSearch'){wordBankQuery=e.target.value;wordBankPage=0;wordBankExact=false;updateWordBankResults();}
 if(e.target.id==='writingText')showWritingStatus();
 if(e.target.id==='courseSearch'){
  searchQuery=e.target.value;let list=LESSONS.filter(l=>(filterLevel==='all'||l.level===filterLevel)&&(`${l.title} ${l.myanmarTitle} ${l.summary} ${l.level}`).toLowerCase().includes(searchQuery.toLowerCase()));let box=document.getElementById('courseMatches');if(box)box.innerHTML=list.length?list.map(lessonTile).join(''):'<p class="empty">No lessons found. Try a different topic.</p>';
 }
});
document.addEventListener('change',e=>{
 if(e.target.id==='ieltsVocabTopic'){wordBankTopic=e.target.value;wordBankPage=0;wordBankExact=false;updateWordBankResults();}
 if(e.target.id==='levelSelect'){filterLevel=e.target.value;location.hash='#courses/'+encodeURIComponent(filterLevel);route()}
 if(e.target.id==='gymLevel'){gymLevel=e.target.value;gymQuestions=[];renderGymInPlace()}
 if(e.target.id==='speedControl'){state.speed=Number(e.target.value);toast('Speed changed for this page only.')}
 if(e.target.id==='importFile')importProgress(e.target.files[0]);
});
/* Voice selection controls stay usable between lesson changes. */
document.getElementById('voiceSettingsToggle').addEventListener('click',()=>{
 const panel=document.getElementById('voiceSettingsPanel');
 panel.hidden=!panel.hidden;
 document.getElementById('voiceSettingsToggle').setAttribute('aria-expanded',String(!panel.hidden));
 if(!panel.hidden){refreshVoicePanel();document.getElementById('voiceGender').focus()}
});
document.getElementById('voiceGender').addEventListener('change',e=>{
 voicePreferences.gender=e.target.value==='female'?'female':'male';
 voicePreferences.voiceId='';
 saveVoicePreferences();refreshVoicePanel();
});
document.getElementById('voiceChoice').addEventListener('change',e=>{
 voicePreferences.voiceId=e.target.value;saveVoicePreferences();refreshVoicePanel();
});
document.getElementById('voicePreview').addEventListener('click',()=>playSpeech('Good morning! Welcome to Burmese English Academy. Let us practise clear British English together.',false,true));
document.getElementById('voiceStop').addEventListener('click',()=>{if('speechSynthesis'in window)speechSynthesis.cancel()});
document.addEventListener('keydown',e=>{
 if(e.key==='Escape'&&!document.getElementById('voiceSettingsPanel').hidden){
  document.getElementById('voiceSettingsPanel').hidden=true;
  document.getElementById('voiceSettingsToggle').setAttribute('aria-expanded','false');
  document.getElementById('voiceSettingsToggle').focus();
 }
});
document.getElementById('menuToggle').addEventListener('click',()=>{let nav=document.querySelector('.toplinks'),open=nav.classList.toggle('open');document.getElementById('menuToggle').setAttribute('aria-expanded',String(open))});
window.addEventListener('hashchange',route);
window.addEventListener('pagehide',()=>{clearRecordingSession(false);if('speechSynthesis'in window)window.speechSynthesis.cancel()});
if('speechSynthesis'in window){window.speechSynthesis.getVoices();window.speechSynthesis.addEventListener('voiceschanged',refreshVoicePanel)}
route();
const versionNode=document.getElementById('siteVersion');if(versionNode)versionNode.textContent='v'+SITE_META.version;

refreshVoicePanel();
