import os
import json
import pandas as pd
from augment import augment_papers_with

def iter_papers():
    basedir = os.path.join('..', 'data', 'papers')
    for folder in os.listdir(basedir):
        folder = os.path.join(basedir, folder)
        for fn in os.listdir(folder):
            with open(os.path.join(folder, fn), 'r', encoding='utf8') as f:
                yield json.load(f)

def iter_authors():
    for paper in iter_papers():
        for author in paper['authors']:
            yield {
                'acmid': author['acmid'],
                'orcid': author['orcid']}

def get_mapping():
    if os.path.exists('acmid_to_orcid_map.csv'):
        data = pd.read_csv('acmid_to_orcid_map.csv', dtype=str)
    else:
        data = dict()
        for author in iter_authors():
            if author['orcid'] == 'missing':
                continue
            if author['acmid'] == 'missing':
                continue

            if author['acmid'] not in data:
                data[author['acmid']] = author['orcid']
            elif data[author['acmid']] != author['orcid']:
                print('conflicting orcid for acmid', author['acmid'])
                print(data[author['acmid']])
                print(author['orcid'])

        # manual handling of a few cases with
        # conflicting/wrong orcids in the dataset
        data['81328490974'] = '0000-0003-3873-6366'
        data['99659261679'] = '0000-0001-9382-6466'
        data['99658640651'] = '0000-0002-9425-0881'
        data['99659162915'] = 'missing'
        data['81551198756'] = 'missing'
        #data[''] = ''

        data = pd.DataFrame.from_dict(data, orient='index').reset_index()
        data.columns = ['acmid', 'orcid']
        data.to_csv('acmid_to_orcid_map.csv', index=False)

    return pd.Series(data['orcid'].values, index=data['acmid']).to_dict()
            

if __name__ == '__main__':
    idmap = get_mapping()

    def update_paper(data):       
        changes = 0
        for i, adata in enumerate(data['authors']):          
            if adata['acmid'] not in idmap:
                continue

            new_orcid = idmap[adata['acmid']]
            if adata['orcid'] != new_orcid:
                adata['orcid'] = new_orcid
                print('changed', data['doi'])
                changes = changes + 1
        return changes, data
        
    augment_papers_with(update_paper)
