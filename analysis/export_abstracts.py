import os
import gzip
import json
from data import paper_iter

def abstract_iter():
    for year, doi, paper in paper_iter():
        abstract = paper['abstract'].strip()
        if abstract == 'No abstract available.':
            abstract = ''
        
        yield {
            'year': year,
            'doi': doi,
            'title': paper['title'],
            'abstract': abstract
        }

data = list(abstract_iter())
with gzip.open('abstracts.json.gzip', 'wt', encoding='utf8') as f:
    json.dump(data, f)
    
