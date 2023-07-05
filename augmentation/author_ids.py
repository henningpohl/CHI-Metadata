import pandas as pd
from augment import augment_paper_author

def iter_fixes():
    data = pd.read_csv('author_id_fixes.csv')
    for row in data.itertuples():
        yield row

if __name__ == '__main__':
    for fix in iter_fixes():      
        augment_paper_author(
            fix.year,
            fix.doi,
            dict(name=fix.name),
            dict(acmid=fix.acmid, orcid=fix.orcid))
        print(f'Updated info for {fix.name}') 
