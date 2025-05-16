import pandas as pd
from data import paper_iter

initials_cases = []
for year, doi, paper in paper_iter():
    for author in paper['authors']:
        parts = author['name'].split(' ')
        # just initials first name
        initials_only = len([p for p in parts if '.' in p])
        
        if len(parts) - initials_only < 2:
            initials_cases.append({
                'year': paper['year'],
                'doi': paper['doi'],
                'acmid': author['acmid'],
                'name': author['name'],
                'newName': 'TODO'
            })
initials_cases = pd.DataFrame(initials_cases)
initials_cases.sort_values('acmid', inplace=True)
initials_cases.to_csv('name_fixes.csv', index=False)
print(initials_cases) 

