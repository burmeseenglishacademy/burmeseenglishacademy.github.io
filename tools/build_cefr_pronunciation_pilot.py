#!/usr/bin/env python3
"""Temporary British Kokoro pilot for unreviewed A1 pronunciation, never deployed.
Technical decoding is not a substitute for human listening/lexical review.
"""
import hashlib,json,pathlib,subprocess,sys
sys.path.insert(0,str(pathlib.Path(__file__).parent))
from build_kokoro_audio import VOICES,synthesize,audio_ok

ROOT=pathlib.Path('.')
SOURCE=ROOT/'draft/A1-EDITORIAL-STARTER.json'
DATA=json.loads(SOURCE.read_text('utf8'))
assert DATA['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
WORDS=('a','an','i','he','water','school','book','apple','mother','can')
entries={e['word']:e for e in DATA['entries']}
assert all(word in entries for word in WORDS)
from kokoro import KPipeline
pipe=KPipeline(lang_code='b')
outroot=ROOT/'scratch/cefr-pronunciation-pilot'
results=[]
for word in WORDS:
    e=entries[word]
    for kind,text in [('word',e.get('display_word',e['word'])),('example',e['example_sentence'])]:
        h=hashlib.sha256(text.encode('utf8')).hexdigest()[:24]
        for voice in VOICES:
            dest=outroot/voice/f'{h}.mp3'
            synthesize(pipe,text,voice,dest)
            assert audio_ok(dest)
            info=json.loads(subprocess.check_output([
                'ffprobe','-v','error','-show_entries','format=duration',
                '-of','json',str(dest)],text=True))
            length=float(info['format']['duration'])
            assert length>.12
            results.append({'word':word,'kind':kind,'spoken_text':text,'voice':voice,
                'relative_path':str(dest),'seconds':round(length,3),
                'bytes':dest.stat().st_size,
                'listening_review':'NOT_PERFORMED'})
report={
  'state':'TECHNICAL_PILOT_ONLY_NEVER_PUBLISH',
  'warning':'Audio quality, pronunciation and semantics NOT independently verified',
  'words':len(WORDS),'recordings':len(results),
  'total_bytes':sum(x['bytes'] for x in results),
  'recordings_detail':results,
}
outroot.mkdir(parents=True,exist_ok=True)
(outroot/'technical-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8')
print('PASS',report['recordings'],'MP3 pilot samples; technical integrity only')
print('Words:',', '.join(WORDS))
print('Audio bytes:',report['total_bytes'])
print('NO audio has been published to production')
