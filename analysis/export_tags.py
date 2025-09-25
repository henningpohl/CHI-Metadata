import os
import gzip
import json
from data import paper_iter

def abstract_iter():
    for year, doi, paper in paper_iter():        
        yield {
            'year': year,
            'doi': doi,
            'title': paper['title'],
            'tags': paper['tags']
        }

data = list(abstract_iter())
with gzip.open('tags.json.gzip', 'wt', encoding='utf8') as f:
    json.dump(data, f)
    
