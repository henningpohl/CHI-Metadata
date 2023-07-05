import os
import json

def __load(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        return json.load(f)

def __save(fn, data):
    with open(fn, 'w', encoding='utf-8') as f:
        return json.dump(data, f, indent=2)

def augment_papers_with(fun):
    processed = 0
    basedir = os.path.join('..', 'data', 'papers')
    for year in os.listdir(basedir):
        folder = os.path.join(basedir, year)
        for paper in os.listdir(folder):
            if paper.endswith('.json'):
                fn = os.path.join(folder, paper)
                data = __load(fn)
                changes, data = fun(data)
                if changes > 0:
                    __save(fn, data)
                processed = processed + 1
    print(f'Processed {processed} papers')

def augment_conference(name, year, fields):
    fn = os.path.join('..', 'data', 'conferences', f'{name}-{year}.json')

    data = __load(fn)
    changes = 0
    for key, value in fields.items():
        if key in data:
            if value is None:
                del data[key]
                changes = changes + 1
            elif data[key] != value:
                data[key] = value
                changes = changes + 1
        elif value is not None:
            data[key] = value
            changes = changes + 1
          
    if changes > 0:
        __save(fn, data)

def augment_paper_author(year, doi, author, fields):
    doi = doi.replace('/', '+')
    fn = os.path.join('..', 'data', 'papers', str(year), f'{doi}.json')
    data = __load(fn)

    changes = 0
    for i, adata in enumerate(data['authors']):
        if 'name' in author and author['name'] == adata['name']:
            pass
        elif 'acmid' in author and author['acmid'] == adata['acmid']:
            pass
        elif 'orcid' in author and author['orcid'] == adata['orcid']:
            pass
        else:
            continue
        for key, value in fields.items():
            if key in adata:
                if value is None:
                    del adata[key]
                    changes = changes + 1
                elif adata[key] != value:
                    adata[key] = value
                    changes = changes + 1
            elif value is not None:
                adata[key] = value
                changes = changes + 1
        
    if changes > 0:
        __save(fn, data)
  
if __name__ == '__main__':
    #augment_conference('CHI', 2023, dict(test='test'))
    #augment_conference('CHI', 2023, dict(test=None))
    augment_paper_author(2023, '10.1145/3544548.3581566', dict(name='Xiang "Anthony" Chen'), dict(test='test'))
    augment_paper_author(2023, '10.1145/3544548.3581566', dict(name='Xiang "Anthony" Chen'), dict(test=None))
