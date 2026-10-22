/* Optional erasure of legacy data left by earlier Academy versions.
   No tracking, cookie, or browser storage is written by this script. */
(function(){
 'use strict';
 const legacy=['bea-complete-v1','bea-unit1-progress-v1','bea-voice-settings-v1','bea-privacy-ack-v1','bea-beta-privacy-ack-v1','bea-policy-ack-v1'];
 const button=document.getElementById('removeOldData');
 const result=document.getElementById('deleteResult');
 if(!button)return;
 button.addEventListener('click',()=>{
  if(!window.confirm('Remove Burmese English Academy data left by older versions in this browser? This cannot be undone.'))return;
  let removed=0,blocked=0;
  for(const storageName of ['localStorage','sessionStorage']){
   try{const storage=window[storageName];for(const key of legacy){if(storage.getItem(key)!==null)removed++;storage.removeItem(key)}}catch(_e){blocked++}
  }
  result.textContent=blocked?'Tried to clear old Academy data; browser storage access was restricted. You may also clear site data in browser settings.':`Cleared ${removed} old Academy entries in this browser. Reload the learning website to clear any open practice session.`;
  result.hidden=false;
 });
})();
