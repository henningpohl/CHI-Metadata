import os
import pandas as pd

data = pd.read_csv('exclude_list.csv')
duplicates = data.groupby('doi').size()
if len(duplicates[duplicates > 1]) > 0:
    print('duplicated exclusions:')
    print(duplicates[duplicates > 1])
    print()
excluded = set(data['doi'])
print(len(excluded), 'papers excluded')

basedir = os.path.join('..', 'data', 'papers')
for folder in os.listdir(basedir):
    folder = os.path.join(basedir, folder)
    for fn in os.listdir(folder):
        doi = os.path.splitext(os.path.basename(fn))[0]
        doi = doi.replace('+', '/')
        if doi in excluded:
            print('deleting', fn)
            os.remove(os.path.join(folder, fn))

chipapers = set(pd.read_csv(os.path.join('..', 'data', 'chipapers.csv'))['doi'])
for doi in excluded:
    if doi in chipapers:
        print(doi, 'should not be in chipapers.csv')

print('done')
        

