#!/usr/bin/env python3
"""Fail-closed release gate for bilingual CEFR learning content.
Run before any recording creation or GitHub Pages publication. "Reviewed" flags
must represent actual human checks; no automated producer may set them.
"""
import argparse,collections,hashlib,json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlparse
TARGETS={'A1':500,'A2':700,'B1':1000,'B2':1300,'C1':1500}
MYANMAR=re.compile('[\\u1000-\\u109f\\uaa60-\\uaa7f]')
ASCII_WORD=re.compile(r"^[a-z][a-z'-]{0,35}$")
REVIEW_FIELDS=('reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation')
SOURCE_FIELDS=('source_english','source_burmese','source_level')

def source_url_is_specific(url):
    """Heuristic provenance check, never proof of linguistic correctness."""
    if not isinstance(url,str) or not url.startswith('https://'):
        return False
    p=urlparse(url)
    host=(p.hostname or '').lower()
    path=p.path.strip('/').lower()
    if not host or p.username or p.password or host in ('example.org','www.example.org','example.com','www.example.com'):
        return False
    if path in ('','about/wordlists/oxford3000-5000','dictionary','english','about'):
        return False
    if host.endswith('oxfordlearnersdictionaries.com') and path.startswith('about/wordlists/'):
        return False
    if len([segment for segment in path.split('/') if segment])<2:
        return False
    return True
def normalize(s):return ' '.join(str(s).strip().split())
def validate(data,root=None,verify_audio=False):
    errors=[]
    def fail(s):errors.append(s)
    if not isinstance(data,dict):return ['File is not a JSON object']
    entries=data.get('entries')
    if not isinstance(entries,list) or len(entries)!=5000:fail('Exactly 5000 entries required')
    if data.get('targets')!=TARGETS:fail('Level quotas differ from approved 500/700/1000/1300/1500')
    if data.get('release_status')!='VERIFIED_FOR_RELEASE':fail('Release status is not VERIFIED_FOR_RELEASE')
    if not isinstance(entries,list):return errors
    seen=set();counts=collections.Counter()
    texts=set()
    for n,row in enumerate(entries):
        if not isinstance(row,dict):fail(f'{n}: entry not an object');continue
        word=normalize(row.get('word','')).lower()
        if not ASCII_WORD.fullmatch(word):fail(f'{n}: noncanonical English word')
        if word in seen:fail(f'{n}: duplicate headword {word}')
        seen.add(word)
        level=row.get('level')
        if level not in TARGETS:fail(f'{n}: invalid level {level}')
        else:counts[level]+=1
        for field in ('english_definition','burmese_meaning','example_sentence','part_of_speech'):
            if not isinstance(row.get(field),str) or not normalize(row[field]):fail(f'{n}: missing {field}')
        if not MYANMAR.search(str(row.get('burmese_meaning',''))):fail(f'{n}: Burmese script required')
        if len(str(row.get('english_definition','')))>300 or len(str(row.get('example_sentence','')))>350:
            fail(f'{n}: overly long definition/example')
        if len(str(row.get('burmese_meaning','')))>250:fail(f'{n}: overly long Burmese gloss')
        if 'english_definition' in row and 'burmese_meaning' in row and normalize(row.get('english_definition',''))==normalize(row.get('burmese_meaning','')):
            fail(f'{n}: unchanged translation')
        if not any(t in str(row.get('example_sentence','')).lower().split() for t in
                   [word,word+'s',word+'ed',word+'ing',word+'es']) and not row.get('example_word_form_reviewed'):
            fail(f'{n}: example needs headword or manually approved inflected form')
        for field in REVIEW_FIELDS:
            if row.get(field) is not True:fail(f'{n}: {field} not independently verified')
        for field in SOURCE_FIELDS:
            ref=row.get(field)
            if not source_url_is_specific(ref):
                fail(f'{n}: missing or generic non-word-specific reference URL in {field}')
        texts.add(word);texts.add(normalize(row.get('example_sentence','')))
    if counts!=collections.Counter(TARGETS):fail(f'Level quota mismatch: {counts}')
    if not verify_audio or root is None:return errors
    manifest_path=root/'audio-manifest.js'
    if not manifest_path.is_file():return errors+['Audio manifest absent']
    s=manifest_path.read_text('utf8');start=s.index('{');end=s.rfind('}')
    m=json.loads(s[start:end+1]);clips=m.get('clips',{})
    for text in texts:
        md5=hashlib.sha256(text.encode('utf8')).hexdigest()[:24]
        voices=clips.get(text,{})
        for voice in ('bm_george','bf_emma'):
            target=f'audio/{voice}/{md5}.mp3'
            if voices.get(voice)!=target:fail(f'Missing or wrong {voice}: {text[:32]}')
            else:
                p=root/target
                if not p.is_file() or p.stat().st_size<500:fail(f'Missing MP3: {target}')
                else:
                    q=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(p)],capture_output=True,text=True)
                    try:
                        if q.returncode!=0 or float(q.stdout.strip())<0.12:fail(f'Invalid MP3: {target}')
                    except ValueError:fail(f'Invalid MP3 duration: {target}')
    return errors
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('dataset',type=Path)
    ap.add_argument('--root',type=Path)
    ap.add_argument('--audio',action='store_true')
    args=ap.parse_args()
    data=json.loads(args.dataset.read_text('utf8'))
    issues=validate(data,args.root,args.audio)
    if issues:
        for msg in issues[:35]:print('BLOCK:',msg,file=sys.stderr)
        print(f'NOT RELEASE READY: {len(issues)} defects (first 35 shown)',file=sys.stderr)
        raise SystemExit(1)
    print('PASS: 5000 records satisfy structural reference/review checks' + (' and MP3 existence/decoding' if args.audio else '; AUDIO NOT CHECKED, NOT RELEASE APPROVED'))
if __name__=='__main__':main()
