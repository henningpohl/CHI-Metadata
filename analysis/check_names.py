import pandas as pd
from data import paper_iter

cases = []
for year, doi, paper in paper_iter():
    for author in paper['authors']:
        parts = author['name'].split(' ')
        # just initials first name
        initials_only = len([p for p in parts if '.' in p])

        # The 1% shortest ones
        if len(author['name']) < 8:
            cases.append({
                'year': paper['year'],
                'doi': paper['doi'],
                'acmid': str(author['acmid']),
                'name': author['name'],
                'newName': 'TODO'
            })
        # The 1% longest ones
        elif len(author['name']) > 24:
            cases.append({
                'year': paper['year'],
                'doi': paper['doi'],
                'acmid': str(author['acmid']),
                'name': author['name'],
                'newName': 'TODO'
            })
        # Initials only ones
        elif len(parts) - initials_only < 2:
            cases.append({
                'year': paper['year'],
                'doi': paper['doi'],
                'acmid': str(author['acmid']),
                'name': author['name'],
                'newName': 'TODO'
            })
cases = pd.DataFrame(cases)
cases.sort_values('acmid', inplace=True)
cases.to_csv('name_fixes.csv', index=False)
print(cases) 

