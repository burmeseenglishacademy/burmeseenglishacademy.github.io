/* Same-origin prerecorded Kokoro playback. No fetch, storage or analytics. */
(function(root){
 'use strict';
 function createPlayer({manifest,createAudio,report}){
  let current=null,generation=0;
  function stop(){generation++;if(current){current.pause();current.removeAttribute('src');current.load();current=null;}}
  function play(text,gender,rate){
   stop();
   const token=generation,voice=gender==='female'?'bf_emma':'bm_george';
   const path=manifest.clips?.[String(text??'').trim()]?.[voice];
   if(!path||!/^audio\/(bm_george|bf_emma)\/[a-f0-9]{24}\.mp3$/.test(path)){
    report('This recording is not available yet. Choose a device voice in Advanced, or try another passage.');return false;
   }
   const audio=createAudio();current=audio;
   audio.preload='none';audio.src=path;audio.playbackRate=Math.min(1.5,Math.max(.5,Number(rate)||1));audio.preservesPitch=true;
   const fail=()=>{if(token!==generation)return;stop();report('Audio could not play. Check your connection and tap Play again.');};
   audio.onerror=fail;
   audio.onended=()=>{if(token===generation)stop();};
   // Synchronous play() in the click handler retains Safari user activation.
   try{const pending=audio.play();if(pending?.catch)pending.catch(error=>{
    if(token!==generation)return;
    if(error?.name==='NotAllowedError'){stop();report('Tap Play again to allow audio in Safari.');}else fail();
   });}catch(error){fail();}
   return true;
  }
  return {play,stop};
 }
 root.BEAAudio={createPlayer};
})(typeof window==='undefined'?globalThis:window);
