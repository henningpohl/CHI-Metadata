import os
import json
import cache
import parse
import pandas as pd

def get_paper_data(year, doi):
    folder = os.path.join('..', 'data', 'papers')
    if not os.path.exists(folder):
        os.mkdir(folder)
    
    folder = os.path.join(folder, str(year))
    if not os.path.exists(folder):
        os.mkdir(folder)
    
    fn = os.path.join(folder, doi.replace('/', '+') + '.json')
    if os.path.exists(fn):
        return

    print(f'Processing {doi} from CHI {year}')
    paper_content = cache.get_paper(doi)
    paper_data = parse.process_paper(paper_content)
    with open(fn, 'w', encoding='utf-8') as f:
        json.dump(paper_data, f, indent=2)
        

if __name__ == '__main__':
    papers = pd.read_csv(os.path.join('..', 'data', 'chipapers.csv'))
    for _, row in papers.iterrows():
        get_paper_data(row['year'], row['doi'])
