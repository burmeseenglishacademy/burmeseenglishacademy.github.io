#!/usr/bin/env python3
"""Fail-closed release gate for bilingual CEFR learning content.
Run before any recording creation or GitHub Pages publication. "Reviewed" flags
must represent actual human checks; no automated producer may set them.
"""
import argparse,collections,hashlib,json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlparse
TARGETS={'A1':200,'A2':200,'B1':200,'B2':200,'C1':200}
MYANMAR=re.compile('[\\u1000-\\u109f\\uaa60-\\uaa7f]')
ASCII_WORD=re.compile(r"^[a-z][a-z'-]{0,35}$")
REVIEW_FIELDS=('reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation')
SOURCE_FIELDS=('source_english','source_burmese','source_level')
# Non-independent inflected forms must not inflate a 200-distinct-lexeme quota.
# The four A1 be/do forms and good/bad comparisons already have held cards.
# Additional plural forms of existing A1 man/woman/child/foot lemmas are
# future-manifest guards, not current held cards. They may be taught as grammar.
# Do NOT automatically ban little/less/least (size vs quantity POS/sense)
# or person/people (plural vs collective senses): require human sense review.
NON_LEXICAL_INFLECTIONS={'is':'be','are':'be','does':'do','did':'do',
                         'better':'good','worst':'bad',
                         'men':'man','women':'woman','children':'child','feet':'foot'}

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
# A plausible URL is not a source-to-headword match. For the release CEFR
# reference require a publisher dictionary *entry* for this exact headword.
# This remains a structural URL check: the separate independent-human ledger
# must still establish a directly observed, exact-sense CEFR label.
PUBLISHER_DICTIONARY_HOSTS=frozenset((
    'dictionary.cambridge.org','oxfordlearnersdictionaries.com',
    'www.oxfordlearnersdictionaries.com'))

def publisher_headword_url_matches(url, word):
    if not source_url_is_specific(url) or not isinstance(word,str) or not word:
        return False
    from urllib.parse import unquote
    p=urlparse(url)
    host=(p.hostname or '').lower()
    segments=[unquote(s).casefold() for s in p.path.strip('/').split('/')]
    if len(segments)!=3:
        return False
    if host=='dictionary.cambridge.org':
        if segments[:2]!=['dictionary','english']:
            return False
    elif host in ('oxfordlearnersdictionaries.com','www.oxfordlearnersdictionaries.com'):
        if segments[:2]!=['definition','english']:
            return False
    else:
        return False
    # Oxford distinguishes homograph entries with _1, _2 etc. The suffix
    # cannot be used to swap the actual lemma or hide a generic list page.
    return bool(re.fullmatch(re.escape(word.casefold())+r'(?:_[1-9][0-9]*)?',segments[-1]))

def normalize(s):return ' '.join(str(s).strip().split())
def example_has_headword_or_regular_form(word, sentence):
    """Punctuation-aware *structural* token check, NOT grammatical approval.
    Irregular or genuinely unusual forms require a separately reviewed override.
    """
    tokens=set(re.findall(r"[a-z]+(?:[-'][a-z]+)*", sentence.lower()))
    forms={word, word+'s', word+'es', word+'ed', word+'ing'}
    if word.endswith('e') and len(word)>1:
        forms.update((word+'d', word[:-1]+'ing'))
    if len(word)>=3 and word[-1] not in 'aeiouwxy' and word[-2] in 'aeiou' and word[-3] not in 'aeiou':
        forms.update((word+word[-1]+'ed', word+word[-1]+'ing'))
    if word.endswith('y') and len(word)>1 and word[-2] not in 'aeiou':
        forms.add(word[:-1]+'ies')
    return any(form in tokens for form in forms)

def audio_collision_risks(recordings):
    """Detect copied audio where the intended speech/voice must differ.

    Identical same-voice single-word homophones may be legitimate and are
    left for actual human listening. Byte-identical recordings across George
    and Emma are always suspicious, even when attached to DIFFERENT words.
    Distinct multiword utterances (including TWO-word phrases) must not
    share the same recording within one voice. This is only a mechanical
    guard, never proof of correct pronunciation or real listening.
    """
    seen = {}
    collisions = []
    for text, voice, digest in recordings:
        current = (text, voice)
        for previous in seen.get(digest, []):
            old_text, old_voice = previous
            incompatible = (voice != old_voice
                            or (text != old_text
                                and (len(text.split()) >= 2 or len(old_text.split()) >= 2)))
            if incompatible:
                collisions.append((previous, current))
        seen.setdefault(digest, []).append(current)
    return collisions

def validate(data,root=None,verify_audio=False):
    errors=[]
    def fail(s):errors.append(s)
    if not isinstance(data,dict):return ['File is not a JSON object']
    entries=data.get('entries')
    if not isinstance(entries,list) or len(entries)!=1000:fail('Exactly 1000 entries required')
    if data.get('targets')!=TARGETS:fail('Level quotas differ from approved 200/200/200/200/200')
    if data.get('release_status')!='VERIFIED_FOR_RELEASE':fail('Release status is not VERIFIED_FOR_RELEASE')
    if not isinstance(entries,list):return errors
    seen=set();counts=collections.Counter()
    texts=set()
    for n,row in enumerate(entries):
        if not isinstance(row,dict):fail(f'{n}: entry not an object');continue
        word=normalize(row.get('word','')).lower()
        if not ASCII_WORD.fullmatch(word):fail(f'{n}: noncanonical English word')
        # The English first-person singular pronoun is obligatorily capitalised.
        # The provisional shortlist currently has lowercase 'i'; never silently
        # promote that unreviewed spelling into a release manifest.
        if word == 'i' and row.get('word') != 'I':
            fail(f'{n}: first-person singular pronoun must be displayed as capital I')
        if word in NON_LEXICAL_INFLECTIONS:
            fail(f'{n}: {word} is a grammatical form of {NON_LEXICAL_INFLECTIONS[word]}; do not count as a separate lexical headword')
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
        if not example_has_headword_or_regular_form(word,str(row.get('example_sentence',''))) and row.get('example_word_form_reviewed') is not True:
            fail(f'{n}: example needs a standalone headword, regular inflection or independently approved irregular form')
        for field in REVIEW_FIELDS:
            if row.get(field) is not True:fail(f'{n}: {field} not independently verified')
        for field in SOURCE_FIELDS:
            ref=row.get(field)
            if not source_url_is_specific(ref):
                fail(f'{n}: missing or generic non-word-specific reference URL in {field}')
            elif field == 'source_level' and not publisher_headword_url_matches(ref,word):
                fail(f'{n}: source_level must bind to same-headword publisher dictionary entry (not independent CEFR proof)')
            elif (urlparse(ref).hostname or '').lower() in PUBLISHER_DICTIONARY_HOSTS and not publisher_headword_url_matches(ref,word):
                fail(f'{n}: {field} publisher dictionary URL does not match headword {word}')
        texts.add(word);texts.add(normalize(row.get('example_sentence','')))
    if counts!=collections.Counter(TARGETS):fail(f'Level quota mismatch: {counts}')
    if verify_audio and root is None:return errors+['Audio verification requested without a root directory']
    if not verify_audio:return errors
    manifest_path=root/'audio-manifest.js'
    if not manifest_path.is_file():return errors+['Audio manifest absent']
    s=manifest_path.read_text('utf8');start=s.index('{');end=s.rfind('}')
    m=json.loads(s[start:end+1]);clips=m.get('clips',{})
    audio_recordings=[]
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
                        if q.returncode!=0 or float(q.stdout.strip())<0.12:
                            fail(f'Invalid MP3: {target}')
                        else:
                            audio_recordings.append((text,voice,hashlib.sha256(p.read_bytes()).hexdigest()))
                    except ValueError:fail(f'Invalid MP3 duration: {target}')
    for earlier, later in audio_collision_risks(audio_recordings):
        fail(f'Identical MP3 bytes reused across incompatible voice/text pairs: {earlier!r} vs {later!r}')
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
    print('PASS: 1000 records satisfy structural reference/review checks' + (' and MP3 existence/decoding' if args.audio else '; AUDIO NOT CHECKED, NOT RELEASE APPROVED'))
if __name__=='__main__':main()
