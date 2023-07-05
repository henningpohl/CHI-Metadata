import os
from download import grab_paper_with_retries, grab_conference, grab_series, grab_page

def __get_fn(cachetype, cacheid):
    if not os.path.exists(os.path.join('..', 'cache')):
        os.mkdir(os.path.join('..', 'cache'))
    cachedir = os.path.join('..', 'cache', cachetype)
    if not os.path.exists(cachedir):
        os.mkdir(cachedir)
    return os.path.join(cachedir, cacheid)
    
def has_resource(cachetype, cacheid):
    fn = __get_fn(cachetype, cacheid)
    return os.path.exists(fn)

def get_resource(cachetype, cacheid):
    fn = __get_fn(cachetype, cacheid)
    if os.path.exists(fn):
        with open(fn, 'r', encoding='utf8') as f:
            return f.read()
    else:
        return None

def write_resource(cachetype, cacheid, data):
    fn = __get_fn(cachetype, cacheid)
    with open(fn, 'w', encoding='utf8') as f:
        f.write(data)

def resolve_paper(doi):
    cacheid = doi.replace('/', '+') + '.html'
    url = f'https://dl.acm.org/doi/{doi}'
    return ('papers', cacheid, url)

def get_paper(doi):
    cachetype, cacheid, url = resolve_paper(doi)

    data = get_resource('papers', cacheid)
    if data is None:
        data = grab_paper_with_retries(url)
        write_resource(cachetype, cacheid, data)
    return data 

def get_conference(year, doi):
    cacheid = f'CHI{year}.html'
    url = f'https://dl.acm.org/doi/proceedings/{doi}'

    data = get_resource('conferences', cacheid)
    if data is None:
        data = grab_conference(url)
        write_resource('conferences', cacheid, data)
    return data

def get_series(name, url):
    cacheid = f'{name}.html'
    data = get_resource('series', cacheid)
    if data is None:
        data = grab_series(url)
        write_resource('series', cacheid, data)
    return data

def get_page(identifier, url):
    cacheid = f'{identifier}.html'
    data = get_resource('pages', cacheid)
    if data is None:
        data = grab_page(url)
        write_resource('pages', cacheid, data)
    return data
    

if __name__ == '__main__':
    a = get_paper('10.1145/3290605.3300648')
    b = get_conference(2007, '10.1145/1240624')
    c = get_series('CHI', 'https://dl.acm.org/conference/chi/proceedings')
    d = get_page('CHI-History', 'https://sigchi.org/conferences/conference-history/CHI/')
