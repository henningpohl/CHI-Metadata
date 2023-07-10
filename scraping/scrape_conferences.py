import os
import json
import cache
import parse
import pandas as pd

def get_chi_list():
    fn = os.path.join('..', 'data', 'CHI.json')
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            return json.load(f)

    series_data = cache.get_series('CHI', 'https://dl.acm.org/conference/chi/proceedings')
    data = parse.process_series(series_data)
    data = [row for row in data if row['year'] > 1981]
    
    with open(fn, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    return data

def get_conference_data(year, doi, exclude=[]):
    fn = os.path.join('..', 'data', 'conferences', f'CHI-{year}.json')
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf-8') as f:
            return json.load(f)

    conf_data = cache.get_conference(year, doi)
    data = parse.process_conference(conf_data)
    data['papers'] = [p for p in data['papers'] if p['doi'] not in exclude]
    
    with open(fn, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    return data

if __name__ == '__main__':
    import pandas as pd
    exclude = set(pd.read_csv('exclude_list.csv')['doi'])
    
    series = get_chi_list()   
    papers = []
    for conference in series:
        data = get_conference_data(conference['year'], conference['doi'], exclude)
        for paper in data['papers']:
            papers.append({'year': conference['year'], 'doi': paper['doi'], 'title': paper['title']})

    fn = os.path.join('..', 'data', 'chipapers.csv')
    papers = pd.DataFrame(papers)
    papers.to_csv(fn, index=False, encoding='utf-8')

    
    
