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

awards = []
authors = []
for paper in paper_iter():
    for badge in paper['badges']:
        awards.append({
            'year': paper['year'],
            'doi': paper['doi'],
            'award': badge
        })
    for author in paper['authors']:
        authors.append({
            'year': paper['year'],
            'doi': paper['doi'],
            'acmid': author['acmid'],
            'orcid': author['orcid'],
            'name': author['name'],
            'institution': author['institution']
        })
awards = pd.DataFrame(awards)
awards.to_csv('awards.csv', index=False)
print(len(awards), 'awards collected')

authors = pd.DataFrame(authors)
authors.to_csv('paperauthors.csv', index=False)
print(len(authors), 'author items collected')
