import os
import json

def check_for_email_protection():
    basedir = os.path.join('..', 'cache', 'papers')

    n = 0
    for fn in os.listdir(basedir):
        with open(os.path.join(basedir, fn), 'r', encoding='utf') as f:
            data = f.read()
            if '[email&#160;protected]' in data:
                n = n + 1
                print(fn)
    print(n)


def check_for_missing_institutions():
    n = 0
    basedir = os.path.join('..', 'data', 'papers')
    for folder in os.listdir(basedir):
        for fn in os.listdir(os.path.join(basedir, folder)):
            fn = os.path.join(basedir, folder, fn)
            with open(fn, 'r', encoding='utf8') as f:
                data = json.load(f)
                for author in data['authors']:
                    if author['institution'] == 'missing':
                        n = n + 1
                        print(data['year'], data['doi'], author['name'])
    print(n)


if __name__ == '__main__':
    #check_for_email_protection()
    check_for_missing_institutions()
