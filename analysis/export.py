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

authors = []
for paper in paper_iter():
    for author in paper['authors']:
        authors.append({
            'year': paper['year'],
            'doi': paper['doi'],
            'acmid': author['acmid'],
            'orcid': author['orcid'],
            'name': author['name'],
            'institution': author['institution']
        })

authors = pd.DataFrame(authors)
authors.to_csv('paperauthors.csv', index=False)
print(len(authors), 'author items collected')
    
