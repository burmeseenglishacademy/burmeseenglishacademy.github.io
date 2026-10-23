#!/usr/bin/env python3
"""A1 500-word draft diagnostics, not bilingual proofreading.
Creates a machine-generated exception list for targeted human editing.
"""
import collections,json,re,unicodedata
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'draft/A1-EDITORIAL-STARTER.json'
data=json.loads(p.read_text('utf8'))
items=data['entries']
assert data['release_status']=='UNVERIFIED_DRAFT_DO_NOT_PUBLISH'
assert len(items)==500
seen=set();issues=[];warnings=[];human_review=[]
def problem(kind,row,msg):
    issues.append({'word':row['word'],'category':kind,'detail':msg})
def caution(kind,row,msg):
    warnings.append({'word':row['word'],'category':kind,'detail':msg})
for row in items:
    word=row['word']
    if word in seen:problem('duplicate',row,'Repeated headword')
    seen.add(word)
    if not re.fullmatch(r"[a-z]+(?:'[a-z]+)?",word):problem('headword',row,'Invalid canonical headword')
    if row['level']!='A1':problem('level',row,'Unexpected stage')
    if row['status']!='DRAFT_PENDING_INDEPENDENT_REVIEW':problem('status',row,'Premature approval')
    if any(row.get(x)!=False for x in ('reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation')):
        problem('review_status',row,'Flag must remain false until independently examined')
    en=row['english_definition'];my=row['burmese_meaning'];ex=row['example_sentence']
    if not 8<=len(en)<=300:problem('definition',row,'Missing/overlong')
    if not re.search('[\u1000-\u109F\uAA60-\uAA7F]',my):problem('burmese',row,'No Burmese Unicode')
    if not 1<=len(my)<=250:problem('burmese',row,'Missing/overlong')
    if not re.fullmatch(r'.{8,200}[.?!]',ex,re.S):problem('example',row,'Sentence punctuation/length')
    if ex[0].isalpha() and not ex[0].isupper():problem('example',row,'First letter must be uppercase')
    if any('<' in field or '>' in field for field in (en,my,ex)):problem('html',row,'Unescaped markup is prohibited')
    if any(unicodedata.normalize('NFC',field)!=field for field in (en,my,ex)):problem('unicode',row,'Noncanonical Unicode text')
    if len(ex.split())>26:caution('example_complexity',row,'More than 26 tokens for A1')
    if len(en.split())>30:caution('definition_complexity',row,'More than 30 tokens in gloss')
    # Heuristic: irregular plural/tense and functional words are exempt from exact token match.
    expanded=re.findall(r"[a-z]+(?:'[a-z]+)?",ex.lower())
    forms={word,word+'s',word+'es',word+'ed',word+'ing'}
    if word.endswith('e'):forms|={word[:-1]+'ing',word+'d'}
    if word.endswith('y'):forms|={word[:-1]+'ies'}
    special={'be':['am','is','are','was','were'],'i':['i'],"trousers":['trousers'],
             'foot':['foot','feet'],'child':['child','children'],'people':['people'],
             'man':['man','men'],'woman':['woman','women'],'read':['read'],
             'speak':['speak','speaks','spoke'],'do':['do','does','did']}
    forms.update(special.get(word,[]))
    if not forms.intersection(expanded):caution('example_word_form',row,'Headword or regular variant not found; check morphology manually')
    human_review.append({'word':word,'english_sense':'PENDING','burmese_meaning':'PENDING',
       'example_grammar':'PENDING','cefr_level':'PROVISIONAL','george_emma_audio':'NOT_GENERATED_OR_APPROVED'})
assert len(seen)==500
output={'status':'EDITORIAL_REPORT_NOT_LANGUAGE_CERTIFICATION',
        'draft_entries':500,'unique_headwords':500,
        'machine_detected_errors':issues,'manual_review_priority':warnings,
        'independent_burmese_approved':0,
        'individual_review_queue':human_review}
dest=root/'draft/A1-500-REVIEW-QUEUE.json'
dest.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n','utf8')
print('Draft A1 500 structural issues:',len(issues),'warnings requiring manual reading:',len(warnings))
for item in warnings[:30]:print('REVIEW',item['word'],item['category'],item['detail'])
if issues:
    for item in issues[:25]:print('FAIL',item)
    raise SystemExit(1)
print('PASS structural checks; ZERO independently approved Burmese glosses')
