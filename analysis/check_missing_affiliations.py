import os
import json
import pandas as pd

def file_iter(basedir):
    for year in os.listdir(basedir):
        folder = os.path.join(basedir, year)
        for fn in os.listdir(folder):
            if fn.endswith('.json'):
                yield os.path.join(folder, fn)

def paper_iter():
    for paper in file_iter(os.path.join('..', 'data', 'papers')):
        with open(paper, 'r', encoding='utf-8') as f:
            yield json.load(f)

missing = []
for paper in paper_iter():
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
