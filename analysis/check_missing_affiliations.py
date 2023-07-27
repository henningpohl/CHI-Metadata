import pandas as pd
from data import paper_iter

missing = []
for year, doi, paper in paper_iter():
    for author in paper['authors']:
        if author['institution'] == 'missing':
            missing.append({
                'year': paper['year'],
                'doi': paper['doi'],
                'acmid': author['acmid'],
                'name': author['name'],
                'affiliation': ''
                })
missing = pd.DataFrame(missing)
missing.to_csv('affiliation_fixes.csv', index=False)
print(missing)
