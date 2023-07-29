import pandas as pd
from augment import augment_paper_author, augment_papers_with

def apply_fixes():
    data = pd.read_csv('author_id_fixes.csv')
    for row in data.itertuples():
        augment_paper_author(
            fix.year,
            fix.doi,
            dict(name=fix.name),
            dict(acmid=fix.acmid, orcid=fix.orcid))
        print(f'Updated info for {fix.name}')

# Hacky fixes for acmids that were remapped later on
def recode_acmids():
    recodes = pd.read_csv('acmid_updates.csv')
    code_map = {str(x.old_id): str(x.new_id) for x in recodes.itertuples()}
    
    def recode_ids(data):
        changes = 0
        for author in data['authors']:
            if author['acmid'] in code_map:
                changes = changes + 1
                author['acmid'] = code_map[author['acmid']]
                print('changed', data['doi'])
        return (changes, data)
    augment_papers_with(recode_ids)
        
if __name__ == '__main__':
    apply_fixes()
    recode_acmids()


    
    
