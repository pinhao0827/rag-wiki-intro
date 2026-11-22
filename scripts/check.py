"""Re-run structural and retrieval checks with Python 3 standard library only."""
from pathlib import Path
from datetime import datetime, timezone
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'content.json').read_text(encoding='utf-8'))
def retrieve(query,version):
    scores=[]
    for c in D['concepts']:
        terms=c['keywords'] if version==1 else [t for t in c['keywords'] if t.isascii()]
        score=sum(len(t) for t in terms if t.lower() in query.lower())
        if score:scores.append((score,c['id']))
    return max(scores,default=(0,None))[1]
checks=[]
def test(name,ok):checks.append({'name':name,'passed':bool(ok)})
sids={s['id'] for s in D['sources']};kids={c['id'] for c in D['concepts']}
test('at least five sources',len(sids)>=5)
test('8-15 slides',8<=len(D['slides'])<=15)
for c in D['concepts']:
    test(c['id']+' valid references',bool(c['sources']) and set(c['sources'])<=sids and set(c['links'])<=kids)
for p in D['slides']:
    test(p['id']+' valid wiki mapping',bool(p['concepts']) and set(p['concepts'])<=kids and set(p['sources'])<=sids)
    allowed=set().union(*(set(c['sources']) for c in D['concepts'] if c['id'] in p['concepts']))
    test(p['id']+' sources available in wiki',set(p['sources'])<=allowed)
for md in (ROOT/'wiki').rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',md.read_text(encoding='utf-8')):
        if not target.startswith(('https://','http://','#')):test(str(md.relative_to(ROOT))+' '+target,(md.parent/target).is_file())
trials=[]
for version in (0,1):
    rows=[dict(t,actual=retrieve(t['q'],version),passed=retrieve(t['q'],version)==t['expected']) for t in D['queries']]
    trials.append({'version':version,'hits':sum(t['passed'] for t in rows),'total':len(rows),'cases':rows})
test('v1 fixed query set',trials[1]['hits']==trials[1]['total'])
page=(ROOT/'index.html').read_text(encoding='utf-8')
embedded=json.loads(re.search(r'<script id="project-data" type="application/json">(.*?)</script>',page,re.S).group(1))
for key in ('title','sources','concepts','queries','slides'):test('embedded '+key+' matches content',embedded[key]==D[key])
result={'timestamp':datetime.now(timezone.utc).isoformat(),'checks':checks,'trials':trials,'passed':sum(t['passed'] for t in checks),'total':len(checks),'note':'Recheck does not re-download raw source PDFs or replace the original run record.'}
(ROOT/'records/recheck.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(f"Checks: {result['passed']}/{result['total']}")
for t in trials:print(f"Retrieval v{t['version']}: {t['hits']}/{t['total']}")
sys.exit(0 if all(t['passed'] for t in checks) else 1)
