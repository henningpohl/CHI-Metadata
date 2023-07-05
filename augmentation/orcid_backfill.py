import os
import pandas as pd
from augment import augment_papers_with

if __name__ == '__main__':
    idmap = pd.read_csv('acmid_to_orcid_map.csv', dtype=str)    
    idmap = pd.Series(idmap['orcid'].values, index=idmap['acmid']).to_dict()
    
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
