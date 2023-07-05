import os
import json

def iter_conferences(basedir):
    for fn in os.listdir(basedir):
        fn = os.path.join(basedir, fn)    
        with open(fn, 'r', encoding='utf-8') as f:
            yield json.load(f)

for conf in iter_conferences(os.path.join('..', 'data', 'conferences')):  
    if 'accepted papers' not in conf:
        print('skipping', conf['year'])
        continue
    
    have = len(conf['papers'])
    need = conf['accepted papers']
    diff = abs(have - need)

    if diff == 0:
        print('CHI', conf['year'], 'on point')
    else:
        print('CHI', conf['year'], f'{have} instead of {need} -> {diff} off')
    
