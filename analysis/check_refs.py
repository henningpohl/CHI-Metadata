import os
import pandas as pd
from data import paper_iter

def load(fn='references.csv'):
    if os.path.exists(fn):
        return pd.read_csv(fn)
    
    refs = []
    for year, doi, paper in paper_iter():
        refs.append({
            'year': year,
            'doi': doi,
            'references': len(paper['references']),
            'with_doi': len([x for x in paper['references'] if x['doi'] != ''])
        })
        
    refs = pd.DataFrame(refs)
    refs.to_csv(fn, index=False)
    return refs

refs = load()
print(refs[refs['references'] > 200])
print()
print(refs[refs['references'] < 5])
print()
print(refs.groupby('references').size())
print()
refs['none'] = refs['references'] == 0
print(refs.groupby(['year', 'none']).size())

print(refs['references'].sum())
print(refs['with_doi'].sum())
