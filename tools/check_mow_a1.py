#!/usr/bin/env python3
"""Reference-only 100-entry A1 alignment against CC BY 4.0 Myanmar Open Wordnet.
IMPORTANT: semantic overlap != translation validation. No publication.
"""
import collections,json,pathlib
from nltk.corpus import wordnet as wn

root=pathlib.Path('.')
draft=json.loads((root/'draft/A1-EDITORIAL-STARTER.json').read_text('utf8'))
candidates=json.loads((root/'draft/UNVERIFIED_CEFR_CANDIDATES.json').read_text('utf8'))
assert draft['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
assert candidates['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
candidate_by_word={x['word']:x for x in candidates['entries']}
tab=root/'scratch/mow-0.1.3-mya_20171005165336.tab'
assert tab.stat().st_size>10000
lemmas=collections.defaultdict(set)
for line in tab.read_text('utf8').splitlines():
    if line.startswith('#'):continue
    cols=line.split('\t')
    if len(cols)==3 and cols[1]=='mya:lemma':
        lemmas[cols[0]].add(cols[2])
output=[]
for entry in draft['entries']:
    word=entry['word']
    source=candidate_by_word.get(word, {})
    if not source:print('WARNING: candidate missing for',word)
    sense_id=source.get('lexical_sense_id','')
    synsets=[]
    if sense_id:
        try:
            synset=wn.synset(sense_id)
            synsets=[synset]
        except (ValueError,KeyError):pass
    suggestions=[]
    for synset in synsets:
        sid=f'{synset.offset():08d}-{synset.pos()}'
        hits=sorted(lemmas[sid])
        if hits:suggestions.append({'synset_id':sid,'terms':hits})
    output.append({
       'word':word,
       'source_synset_provisional':sense_id,
       'mow_matches_at_this_synset':suggestions,
       'english_definition_draft':entry['english_definition'],
       'burmese_translation_draft':entry['burmese_meaning'],
       'crosscheck_status':'WEAK_SENSE_CANDIDATES_NOT_TRANSLATION_APPROVAL',
       'reviewed_burmese':False,
    })
destination=root/'draft/A1-MOW-WEAK-CROSSCHECK.json'
destination.write_text(json.dumps({
  'license':'CC BY 4.0',
  'source':'https://github.com/myanmaropenwordnet/mow',
  'warning':'MOW suggestions alone do not verify translation, word sense, orthography, or CEFR level',
  'total':len(output),'entries':output
 },ensure_ascii=False,indent=2),'utf8')
print('A1 entries',len(output),'with any MOW alignment',sum(bool(x['mow_matches_at_this_synset']) for x in output))
print('All translations remain unverified')
