import pandas as pd
from data import paper_iter

initials_cases = []
for year, doi, paper in paper_iter():
    for author in paper['authors']:
        parts = author['name'].split(' ')
        # just initials first name
        if len(parts) == 2 and len(parts[0]) == 2 and '.' in parts[0]:
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

