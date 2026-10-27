#!/usr/bin/env python3
"""Batch72 five-way nonpublishing structural and candidate-risk audit. Never approves words."""
import argparse,collections,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'draft'
COUNTS={"A2":8,"B1":8,"B2":9,"C1":15}
def load(name):return json.loads((D/name).read_text(encoding="utf-8"))
def prior_index():
    files=[D/'A1-EDITORIAL-STARTER.json',*sorted(D.glob('A1-EXPANSION-BATCH*.json')),D/'A2-C1-EDITORIAL-STARTER.json',*sorted(D.glob('A2-C1-EDITORIAL-BATCH*.json')),*sorted(D.glob('A2-C1-RETIER-EDITORIAL-BATCH*.json')),*[p for p in sorted(D.glob('A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json')) if 'BATCH72' not in p.name]]
    prior=collections.defaultdict(list)
    for p in files:
        for r in json.loads(p.read_text(encoding="utf-8"))['entries']:
            prior[r['word'].casefold()].append(p.name)
    return prior
def run(level):
    d=load('A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH72.json')
    t=load('A2-C1-SOURCE-RECOVERY-REVIEW-TASKS-BATCH72.json')
    q=load('A2-C1-SOURCE-RECOVERY-QUARANTINE-BATCH72.json')
    E,T,Q=d['entries'],t['entries'],q['records']
    assert d['release_status']=='UNVERIFIED_SOURCE_RECOVERY_DO_NOT_PUBLISH'
    assert t['release_status']=='UNVERIFIED_REVIEW_TASKS_DO_NOT_PUBLISH' and t['source_pages_not_yet_checked'] is True
    assert q['release_status']=='REVERSIBLE_EDITORIAL_QUARANTINE_NOT_APPROVED_DO_NOT_PUBLISH'
    assert len(E)==len(T)==len(Q)==40
    assert collections.Counter(e['proposed_level'] for e in E)==COUNTS
    assert d['counts_by_proposed_level']==COUNTS
    assert len({e['word'].casefold() for e in E})==40
    assert {e['word'] for e in E}=={x['word'] for x in T}=={x['word'] for x in Q}
    task={x['word']:x for x in T};hold={x['word']:x for x in Q}
    prior=prior_index()
    pool={x['word'].casefold():x for x in load('UNVERIFIED_CEFR_CANDIDATES.json')['entries']}
    triage=load('BATCH70-CANDIDATE-TRIAGE.json')
    screened={(x['proposed_level'],x['word']):x for x in triage['records']}
    extra=load('BATCH72-EXTRA-CANDIDATE-TRIAGE.json')
    assert extra['screened']==len(extra['records']) and extra['screened']==extra['clear_only']+extra['quarantined']
    assert all(x['independently_checked'] is False for x in extra['records'])
    extra_screened={(x['level'],x['word']):x for x in extra['records']}
    problems=[];selected=0;previous_clear=0;new_unscreened=0
    for e in E:
        if level!='ALL' and e['proposed_level']!=level:continue
        selected+=1;w=e['word'];x=task[w];h=hold[w]
        screening=screened.get((e['proposed_level'],w))
        if screening:
            if screening['mechanical_preflight']!='CLEAR_ONLY_NOT_APPROVED':problems.append({'word':w,'issue':'BATCH70_PREFLIGHT_QUARANTINE'})
            else:previous_clear+=1
        else:
            extra_record=extra_screened.get((e['proposed_level'],w))
            if not extra_record or extra_record['mechanical_status']!='CLEAR_ONLY_NOT_APPROVED':
                problems.append({'word':w,'issue':'NOT_CLEAR_IN_OBSERVED_BATCH72_PREFLIGHT'})
            else: new_unscreened+=1
        assert re.fullmatch('[a-z]{3,}',w),w
        assert e['part_of_speech'] in ('noun','verb','adjective','adverb','plural noun'),w
        assert len(e['english_definition'])>=30,w
        assert re.search('[\\u1000-\\u109f]',e['burmese_meaning']),w
        s=e['example_sentence']
        assert len(s)>=35 and s[0].isupper() and s[-1] in '.?!',w
        assert re.search(r'(?<![a-z])'+re.escape(w)+r'(?![a-z])',s.casefold()),w
        assert e['editorial_hold'] is True and e['release_approved'] is False,w
        assert e['status']=='REVERSIBLE_QUARANTINE_PENDING_INDEPENDENT_EVIDENCE',w
        assert len(e['editorial_hold_reasons'])==3,w
        assert all(e[k] is False for k in ('reviewed_english','reviewed_burmese','reviewed_example','reviewed_level','reviewed_pronunciation')),w
        assert all(e[k]=='' for k in ('source_english','source_burmese','source_level')),w
        assert x['editorial_hold'] is True and x['release_approved'] is False,w
        for k in ('english_definition_review','burmese_review','example_review','cefr_review'):
            assert x[k]['completed'] is False and x[k]['reviewer'] is None and x[k]['observed_evidence'] is None,w
        assert x['english_definition_review']['source_observed'] is False,w
        assert all(v is False for v in x['audio_review'].values()),w
        assert h['reason_codes']==e['editorial_hold_reasons'] and h['hold_reversible'] is True,w
        assert h['independently_approved'] is False and h['release_approved'] is False,w
        if w.casefold() in prior:problems.append({'word':w,'issue':'PRIOR_AUTHORED_COLLISION','files':prior[w.casefold()]})
        p=pool.get(w.casefold())
        if p and p.get('level')!=e['proposed_level']:problems.append({'word':w,'issue':'UNVERIFIED_POOL_TIER_DISAGREEMENT','pool_level':p.get('level')})
        if p and re.search(r'\b(?:surname|given name|capital of|city in|genus|species|trademark)\b',str(p.get('english_definition_draft','')),re.I):
            problems.append({'word':w,'issue':'SUSPECT_WORDNET_SENSE'})
    if level=='ALL':
        files=[D/'A1-EDITORIAL-STARTER.json',*sorted(D.glob('A1-EXPANSION-BATCH*.json')),D/'A2-C1-EDITORIAL-STARTER.json',*sorted(D.glob('A2-C1-EDITORIAL-BATCH*.json')),*sorted(D.glob('A2-C1-RETIER-EDITORIAL-BATCH*.json')),*sorted(D.glob('A2-C1-SOURCE-RECOVERY-EDITORIAL-BATCH*.json'))]
        unique=collections.defaultdict(set); occurrences=collections.Counter(); unlevelled=[]
        for p in files:
            for row in json.loads(p.read_text(encoding='utf-8'))['entries']:
                w=row['word'].casefold();lvl=row.get('proposed_level') or row.get('level') or ('A1' if p.name.startswith('A1-') else None)
                if lvl not in ('A1','A2','B1','B2','C1'):unlevelled.append((p.name,w,lvl));continue
                unique[lvl].add(w);occurrences[w]+=1
        assert not unlevelled,unlevelled[:10]
        distinct=set().union(*unique.values())
        staged_counts={lvl:len(unique[lvl]) for lvl in ('A1','A2','B1','B2','C1')}
        cross_tier=sum(1 for w in distinct if sum(w in s for s in unique.values())>1)
        print('BATCH72 STAGED DISTINCT HEADWORDS',len(distinct),'PER_LEVEL',json.dumps(staged_counts),'CROSS_LEVEL',cross_tier,'REPEATED_OCCURRENCES',sum(v-1 for v in occurrences.values()))
        assert 'UNVERIFIED_DRAFT_DO_NOT_PUBLISH' in (ROOT/'cefr-vocabulary-data.js').read_text(encoding='utf-8')
        assert re.search(r'entries:\s*\[\s*\]',(ROOT/'cefr-vocabulary-data.js').read_text(encoding='utf-8'))
        (ROOT/'batch72-triage-results.json').write_text(json.dumps({'batch':72,'drafts':40,'by_level':COUNTS,'batch70_mechanically_clear_only':previous_clear,'new_batch72_mechanically_clear_only':new_unscreened,'independently_approved':0,'audio_generated':0,'problems':problems,'staged_distinct_headwords':len(distinct),'staged_per_level_unique_headwords':staged_counts,'cross_level_wordforms':cross_tier,'repeated_occurrences':sum(v-1 for v in occurrences.values())},ensure_ascii=False,indent=2)+'\\n',encoding='utf-8')
    print('BATCH72',level,'structurally checked',selected,'earlier-preflight-clear-only',previous_clear,'new-batch72-preflight-clear-only',new_unscreened,'cross-corpus problems',json.dumps(problems,ensure_ascii=False))
    assert not problems,'Cross-corpus problems require repair; all drafts stay held'
    print('PASS: structural-only. All quarantined. No independent approval, audio or publication.')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--level',choices=[*COUNTS,'ALL'],required=True)
    run(p.parse_args().level)
