import os
import json
import cache
import download
import parse
import time

def redo(doi):
    cachetype, cacheid, url = cache.resolve_paper(doi)
    try:
        paper_content = download.grab_page_selenium(url)
        cache.write_resource(cachetype, cacheid, paper_content)
        print('downloaded', doi)

        paper_data = parse.process_paper(paper_content)
        fn = os.path.join(
            '..',
            'data',
            'papers',
            str(paper_data['year']),
            doi.replace('/', '+') + '.json')
        with open(fn, 'w', encoding='utf-8') as f:
            json.dump(paper_data, f, indent=2)
        print('processed', doi)
        
        time.sleep(10)
    except Exception as e: 
        print(e)
        print('Waiting 5 min before retrying...')
        time.sleep(60 * 5)

basedir = os.path.join('..', 'cache', 'papers')
for fn in os.listdir(basedir):
    with open(os.path.join(basedir, fn), 'r', encoding='utf') as f:
        data = f.read()
        if '[email&#160;protected]' in data:
            doi = fn.replace('+', '/').removesuffix('.html')
            redo(doi)


