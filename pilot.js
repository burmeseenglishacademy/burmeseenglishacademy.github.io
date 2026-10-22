'use strict';
const pilotStatus=document.getElementById('pilot-status');
const pilotPlayer=BEAAudio.createPlayer({manifest:window.BEA_AUDIO_MANIFEST,createAudio:()=>new Audio(),report:message=>{pilotStatus.textContent=message;}});
document.addEventListener('click',event=>{const button=event.target.closest('[data-sample]');if(!button)return;const sample=BEA_PILOT.entries[Number(button.dataset.sample)];if(!sample)return;pilotStatus.textContent=(button.dataset.gender==='female'?'Emma':'George')+' · '+sample.category;pilotPlayer.play(sample.text,button.dataset.gender,Number(document.getElementById('pilot-rate').value));});
document.getElementById('pilot-stop').addEventListener('click',()=>{pilotPlayer.stop();pilotStatus.textContent='Stopped.';});
window.addEventListener('pagehide',()=>pilotPlayer.stop());
