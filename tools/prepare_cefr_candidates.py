#!/usr/bin/env python3
"""Prepare a CEFR *candidate* list without publishing unreviewed translations.

Sources:
- wordfreq: usage frequency, CC BY-SA 4.0 frequency data.
- NLTK Princeton WordNet: lexical sense & gloss, WordNet license.
Ranking is an editorial starting point, NOT an official CEFR classification.
Output deliberately marks all rows pending human sense/translation review.
"""
import argparse, collections, json, re
from pathlib import Path

TARGETS={'A1':500,'A2':700,'B1':1000,'B2':1300,'C1':1500}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,default=Path('draft/cefr-candidates.json'))
    ap.add_argument('--starter',type=Path,default=Path('draft/A1-EDITORIAL-STARTER.json'))
    opts=ap.parse_args()
    from wordfreq import top_n_list, zipf_frequency
    from nltk.corpus import wordnet as wn

    # This is a ranked shortlist, not a redistribution of Oxford / Cambridge wordlists.
    ranked=top_n_list('en',55000,wordlist='best')
    required=['a','an','be','i','you','we','the','this','that','he','she','it','my','your',
              'yes','no','please','hello','goodbye','thank','water','food','home',
              'family','mother','father','school','teacher','student','book','read']
    starter={}
    if opts.starter.is_file():
        review=json.loads(opts.starter.read_text('utf8'))
        if review.get('release_status')!='UNVERIFIED_DRAFT_DO_NOT_PUBLISH':
            raise RuntimeError('Editorial starter must remain explicitly unverified')
        starter={row['word']:row for row in review['entries']}
        if len(starter)!=len(review['entries']):raise RuntimeError('Duplicate editorial words')
        if len(starter)>TARGETS['A1']:raise RuntimeError('A1 starter exceeds approved 500 quota')
    ordered=list(dict.fromkeys(list(starter)+required+ranked))
    # Function words and pronouns must not inherit chemical-symbol or acronym synsets.
    function_words={'a','an','be','i','you','we','the','this','that','he','she','it','my','your',
                    'yes','no','please','hello','goodbye'}
    entries=[]
    for term in ordered:
        term=term.lower().strip()
        if not re.fullmatch(r"[a-z]+(?:'[a-z]+)?",term) or len(term)>25:continue
        if any(t['word']==term for t in []):pass
        senses=[] if term in function_words else wn.synsets(term.replace("'",""))
        if not senses and term not in required:continue
        # Prefer headwords/lemmas rather than machine-derived tense/plural forms.
        if term not in required and wn.morphy(term) not in (None,term):continue
        # POS of the first available synset is provisional; common words may be polysemous.
        pos=senses[0].pos() if senses else 'other'
        gloss=senses[0].definition() if senses else ''
        if not gloss and term not in required:continue
        entry={
            'word':term,
            'level':'',
            'part_of_speech':pos,
            'english_definition_draft':gloss,
            'burmese_meaning':'',
            'example_sentence':'',
            'lexical_sense_id':senses[0].name() if senses else '',
            'sense_selection_status':'UNREVIEWED_PROVISIONAL',
            'zipf_frequency':round(zipf_frequency(term,'en'),2),
            'reference':'Princeton WordNet 3.0 / wordfreq',
            'reviewed_english':False,'reviewed_burmese':False,
            'reviewed_example':False,'reviewed_level':False,'reviewed_pronunciation':False,
            'candidate_status':'UNREVIEWED_PROVISIONAL',
        }
        if term in starter:
            for key in ('part_of_speech','english_definition','burmese_meaning','example_sentence'):
                entry['editorial_'+key+'_draft']=starter[term][key]
            entry['editorial_status']='HAND_AUTHORED_PENDING_SECOND_REVIEW'
            entry['draft_display_word']='I' if term=='i' else term
        entries.append(entry)
        if len(entries)>=sum(TARGETS.values()):break
    if len(entries)!=5000:raise RuntimeError(f'Only found {len(entries)} of 5000 candidates')
    offset=0
    for level,count in TARGETS.items():
        for row in entries[offset:offset+count]:row['level']=level
        offset+=count
    assert len({x['word'] for x in entries})==5000
    assert all(row['word'] in {x['word'] for x in entries[:TARGETS['A1']]} for row in starter.values())
    print('Editorial A1 drafts merged:',len(starter),'(none independently reviewed)')
    # Explicitly prohibited from live publication until all bilingual content is reviewed.
    payload={'schema':1,'release_status':'UNVERIFIED_DRAFT_DO_NOT_PUBLISH',
        'tier_method':'frequency-based rough planning tiers; not formal CEFR assignments',
        'sources':['https://github.com/rspeer/wordfreq',
                   'https://wordnet.princeton.edu/license-and-commercial-use',
                   'https://wordnet.burmese.sg/'],
        'targets':TARGETS,'entries':entries}
    opts.out.parent.mkdir(parents=True,exist_ok=True)
    opts.out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n','utf-8')
    print('GENERATED 5000 unique English sense CANDIDATES; 0 Burmese glosses verified')
    print('These are NOT suitable for live learners until full semantic reviews and audio.')
    print('Level targets:',dict(collections.Counter(x['level'] for x in entries)))
if __name__=='__main__':main()
