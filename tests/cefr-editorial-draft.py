#!/usr/bin/env python3
"""QA for draft-only bilingual A1 entries. Structural, NOT semantic certification."""
import json,re,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STARTER=ROOT/'draft/A1-EDITORIAL-STARTER.json'
CANDIDATES=ROOT/'draft/UNVERIFIED_CEFR_CANDIDATES.json'
draft=json.loads(STARTER.read_text('utf8'))
candidates=json.loads(CANDIDATES.read_text('utf8'))
assert draft['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
assert candidates['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
entries=draft['entries']
oxford=json.loads((ROOT/'draft/A1-OXFORD-LEVEL-SAMPLE-CHECKS.json').read_text('utf8'))
assert oxford['verified_scope']=='ENGLISH CEFR LEVEL AND PART OF SPEECH ONLY'
assert oxford['semantic_burmese_reviewed'] is False
assert oxford['pronunciation_reviewed'] is False
assert len(oxford['checks'])==10
lookups={x['word']:x for x in entries}
for check in oxford['checks']:
    match=lookups[check['word']]
    assert match['part_of_speech']==check['part_of_speech'],check['word']
    assert match['level']==check['level']=='A1',check['word']
    assert check['result']=='SOURCE_LEVEL_MATCH_OBSERVED'
    assert check['source_url'].startswith('https://www.oxfordlearnersdictionaries.')
assert len(entries)==227, f'Expected current hand-authored starter count 227, got {len(entries)}'
assert len({e['word'] for e in entries})==len(entries)
full=candidates['entries']
assert len(full)==5000
assert len({e['word'] for e in full})==5000
first500={e['word']:e for e in full[:500]}
assert len(first500)==500
myanmar=re.compile('[\u1000-\u109f\uaa60-\uaa7f]')
for e in entries:
    word=e['word']
    assert e['level']=='A1',word
    assert word in first500,'Curated A1 word missing or assigned too high: '+word
    other=first500[word]
    assert other['editorial_status']=='HAND_AUTHORED_PENDING_SECOND_REVIEW',word
    assert other['editorial_english_definition_draft']==e['english_definition'],word
    assert other['editorial_burmese_meaning_draft']==e['burmese_meaning'],word
    assert other['editorial_example_sentence_draft']==e['example_sentence'],word
    assert isinstance(e['part_of_speech'],str) and len(e['part_of_speech'])>=3,word
    assert len(e['english_definition'])>=8,word
    assert myanmar.search(e['burmese_meaning']),word
    assert unicodedata.normalize('NFC',e['burmese_meaning'])==e['burmese_meaning'],word
    example=e['example_sentence']
    assert example and example[0].isupper() and example[-1] in '.?!',word
    assert len(example)<=160,word
    assert all(e[x] is False for x in ('reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation')),word
    assert e['status']=='DRAFT_PENDING_INDEPENDENT_REVIEW',word
    assert e['source_level_reference'].startswith('https://'),word
    # This check is only a rough heuristic; morphology and contextual sense still
    # need human checking. We never mark anything verified based on this test.
    pattern=re.compile(r'\b'+re.escape(word)+r'\b',re.I)
    if not pattern.search(example):print('REQUIRES HUMAN MORPHOLOGY CHECK:',word,example)
for word in ['a','an','be','he','i','it']:
    entry=first500[word]
    assert entry['editorial_english_definition_draft'] != entry['english_definition_draft'] or not entry['english_definition_draft'],word
assert 'cefr-vocabulary-data.js' not in (str(CANDIDATES)+str(STARTER))
production=(ROOT/'cefr-vocabulary-data.js').read_text('utf8')
assert 'UNVERIFIED_DRAFT_DO_NOT_PUBLISH' in production
assert 'entries:[]' in production
print(f'PASS: {len(entries)} author-written A1 bilingual examples structurally valid, integrated in 5000 unverified corpus')
print('CAUTION: Meaning, naturalness, level, pronunciation and independent translation review still PENDING')
