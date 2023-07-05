import os
import pandas as pd

def available_papers(basedir):
    for folder in os.listdir(basedir):
        folder = os.path.join(basedir, folder)
        if not os.path.isdir(folder):
            continue
        for file in os.listdir(folder):
            if not file.endswith('.json'):
                continue
            doi = file.removesuffix('.json').replace('+', '/')
            yield doi

have = list(available_papers(os.path.join('..', 'data', 'papers')))
have = pd.DataFrame({'doi': have, 'have': True})
need = pd.read_csv(os.path.join('..', 'data', 'chipapers.csv'))
need['need'] = True

data = pd.merge(have, need, on='doi', how='outer')
data.drop(columns='title', inplace=True)
data['need'] = data['need'].fillna(False)
data['have'] = data['have'].fillna(False)

print("Papers needed but not scraped yet:")
print(data[data['have'] == False].to_string(index=False))
print()
print("Papers available but that shouldn't be there:")
print(data[data['need'] == False].to_string(index=False))

