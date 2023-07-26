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

def to_page_count(page_range):
    if len(page_range) == 0:
        return -1
    if '-' not in page_range:
        return 1

    try:
        a, b = page_range.split('-')
        return int(b) - int(a) + 1
    except:
        return -1

awards = []
authors = []
info = []

for paper in paper_iter():
    info.append({
        'year': paper['year'],
        'doi': paper['doi'],
        'published': paper['published'],
        'page_range': paper['pages'],
        'page_count': to_page_count(paper['pages'])
    })
   
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

info = pd.DataFrame(info)
info.to_csv('paperinfos.csv', index=False)
print(len(info), 'paper infos collected')

        
awards = pd.DataFrame(awards)
awards.to_csv('awards.csv', index=False)
print(len(awards), 'awards collected')

authors = pd.DataFrame(authors)
authors.to_csv('paperauthors.csv', index=False)
print(len(authors), 'author items collected')
