/* Optional prerecorded audio, falling back to the current UK-only Web Speech voice. */
(function(root){
 'use strict';
 if(!root.BEAAudio||!root.BEA_AUDIO_MANIFEST||typeof root.playSpeech!=='function')return;
 const manifest=root.BEA_AUDIO_MANIFEST;
 const preview='Good morning! Welcome to Burmese English Academy. Let us practise clear British English together.';
 const originalSpeak=root.playSpeech,originalRefresh=root.refreshVoicePanel;
 const player=root.BEAAudio.createPlayer({
  manifest,
  createAudio:()=>new Audio(),
  report:msg=>{if(typeof root.toast==='function')root.toast(msg);else console.warn(msg);}
 });
 const gender=()=>voicePreferences.gender==='female'?'female':'male';
 const has=(text,g)=>Boolean(manifest.clips?.[String(text??'').trim()]?.[g==='female'?'bf_emma':'bm_george']);
 root.playSpeech=function(text,slow=false,previewMode=false){
  const g=gender();
  if(!voicePreferences.voiceId&&has(text,g)){
   if('speechSynthesis'in root)root.speechSynthesis.cancel();
   const rate=previewMode?1:(slow?Math.max(.65,state.speed-.22):state.speed);
   return player.play(String(text).trim(),g,rate);
  }
  player.stop();
  return originalSpeak(text,slow,previewMode);
 };
 root.refreshVoicePanel=function(){
  originalRefresh();
  const btn=document.getElementById('voicePreview'),status=document.getElementById('voiceStatus'),select=document.getElementById('voiceChoice');
  if(btn&&has(preview,gender())&&!voicePreferences.voiceId)btn.disabled=false;
  if(status&&has(preview,gender())&&!voicePreferences.voiceId)status.textContent='Selected '+(gender()==='female'?'Emma, British female':'George, British male')+' prerecorded audio. Missing recordings use British-only device speech.';
  if(select?.options?.length)select.options[0].textContent='Automatic — prefer George/Emma recordings';
 };
 document.addEventListener('click',event=>{
  const node=event.target.closest('[data-action]');
  if(node&&['say-stop','clear-session'].includes(node.dataset.action))player.stop();
 },true);
 document.getElementById('voiceStop')?.addEventListener('click',()=>player.stop());
 root.addEventListener('hashchange',()=>player.stop());
 root.addEventListener('pagehide',()=>player.stop());
 root.refreshVoicePanel();
})(window);
