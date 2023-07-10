import os
import pandas as pd

excluded = set(pd.read_csv('exclude_list.csv')['doi'])

basedir = os.path.join('..', 'data', 'papers')
for folder in os.listdir(basedir):
    folder = os.path.join(basedir, folder)
    for fn in os.listdir(folder):
        doi = os.path.splitext(os.path.basename(fn))[0]
        doi = doi.replace('+', '/')
        if doi in excluded:
            print('deleting', fn)
            os.remove(os.path.join(folder, fn))

chipapers = pd.read_csv(os.path.join('..', 'data', 'chipapers.csv'))
for doi in excluded:
    if doi in chipapers['doi']:
        print(doi, 'should not be in chipapers.csv')

print('done')
        

