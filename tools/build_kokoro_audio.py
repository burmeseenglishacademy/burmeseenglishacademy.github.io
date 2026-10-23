#!/usr/bin/env python3
"""Generate British MP3 files locally with Kokoro, with resumable verification."""
import argparse
import hashlib
import json
import pathlib
import shutil
import subprocess
import tempfile

VOICES=('bm_george','bf_emma')
def audio_ok(p):
    if not p.is_file() or p.stat().st_size<500:return False
    proc=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)],capture_output=True,text=True)
    try:return proc.returncode==0 and float(proc.stdout.strip())>=0.12
    except (ValueError,TypeError):return False

def synthesize(pipe,text,voice,target):
    import numpy as np
    import soundfile as sf
    segments=[]
    for _,_,a in pipe(text,voice=voice,speed=1.0,split_pattern=r'\n+'):
        array=a.detach().cpu().numpy() if hasattr(a,'detach') else np.asarray(a)
        if array.ndim!=1 or len(array)==0:raise RuntimeError('Invalid synthesizer audio')
        segments.append(array.astype('float32',copy=False))
    if not segments:raise RuntimeError('Empty synthesizer response')
    target.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='bea-audio-') as d:
        wav=pathlib.Path(d)/'voice.wav'
        mp3=pathlib.Path(d)/'voice.mp3'
        sf.write(wav,np.concatenate(segments),24000)
        subprocess.run(['ffmpeg','-nostdin','-loglevel','error','-y','-i',str(wav),'-ac','1','-ar','24000','-b:a','64k',str(mp3)],check=True)
        if not audio_ok(mp3):raise RuntimeError('Bad MP3 after conversion')
        shutil.copy2(mp3,target)

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--catalogue',required=True,type=pathlib.Path)
    p.add_argument('--root',required=True,type=pathlib.Path)
    p.add_argument('--voice',choices=VOICES+('all',),default='all')
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--limit',type=int,default=0)
    p.add_argument('--manifest-only',action='store_true')
    args=p.parse_args()
    cat=json.loads(args.catalogue.read_text('utf8'))
    entries=cat['entries']
    if cat['recording_goal']!=2*len(entries) or cat['source_counts']!={'lessons':54,'ielts_words':1000}:raise RuntimeError('Invalid catalogue')
    if len({e['id'] for e in entries})!=len(entries):raise RuntimeError('Duplicate file id')
    for e in entries:
        actual=hashlib.sha256(e['text'].encode('utf8')).hexdigest()[:24]
        if actual!=e['id']:raise RuntimeError('Text checksum mismatch')
    voices=VOICES if args.voice=='all' else (args.voice,)
    if not args.manifest_only:
        from kokoro import KPipeline
        pipe=KPipeline(lang_code='b')
        work=entries[args.start:args.start+args.limit if args.limit else None]
        for pos,e in enumerate(work,args.start):
            for voice in voices:
                out=args.root/f'audio/{voice}/{e["id"]}.mp3'
                if audio_ok(out):continue
                print(f'[{pos+1}/{len(entries)}] {voice}: {e["id"]}',flush=True)
                synthesize(pipe,' '.join(e['text'].split()),voice,out)
    clips={}
    for e in entries:
        available={}
        for voice in VOICES:
            rel=f'audio/{voice}/{e["id"]}.mp3'
            if audio_ok(args.root/rel):available[voice]=rel
        if available:clips[e['text']]=available
    manifest={'schema':1,'model':'hexgrad/Kokoro-82M','clips':clips}
    (args.root/'audio-manifest.js').write_text('/* Kokoro audio manifest */\nwindow.BEA_AUDIO_MANIFEST='+json.dumps(manifest,ensure_ascii=False,separators=(',',':'))+';\n','utf8')
    recorded=sum(len(v) for v in clips.values())
    print(f'Valid recordings: {recorded}/{cat["recording_goal"]}')
    if not args.manifest_only and args.limit==0 and recorded<cat['recording_goal']:raise RuntimeError('Not ready for publication: recordings incomplete')

if __name__=='__main__':main()
