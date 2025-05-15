import re
from datetime import datetime
from bs4 import BeautifulSoup

def parse_year(name):
    m = re.match(r".+ '(\d+):.+", name)
    dt = datetime.strptime(m.group(1), '%y')
    if(dt.year > 2050):
        return dt.year - 100
    else:
        return dt.year

def get_prop(x, prop, default=''):
    if x is None:
        return default
    try:
        return x[prop]
    except:
        return default

def acm_to_iso_date(text):
    return datetime.strptime(text, '%d %B %Y').date().isoformat()

def try_get_doi(refelement):
    acmlinks = refelement.select('a[href^="/doi/"]')
    if len(acmlinks) == 0:
        return ''
    return acmlinks[0]['href'].removeprefix('/doi/')

def process_paper(content):
    soup = BeautifulSoup(content, 'html.parser')

    doi = soup.select_one('a.issue-item__doi').text.removeprefix('https://doi.org/')
    
    title = soup.select_one('h1.citation__title').text.strip()
    abstract = soup.select_one('div.abstractInFull')
    if abstract == None:
        abstract = ''
    else:
        abstract = abstract.text.strip()
        
    published = datetime.strptime(soup.select_one('span.CitationCoverDate').text, '%d %B %Y').date()
    proctitle = soup.select_one('h2.parent-item__title').text.strip()

    pages = soup.select_one('div.parent-item div.pageRange')
    if pages == None:
        pages = ''
    else:
        pages = pages.text.removeprefix('Pages ').strip()
    pages = pages.replace('\u2013', '-') # en dash to hyphen

    badges = soup.select_one('span.badges')
    if badges == None:
        badges = []
    else:
        badges = [x.text for x in badges.select('a div')]    

    authors = []
    for author in soup.select('.loa > .loa__item'):
        name = author.select_one('.loa__author-name > span').text.strip()
        img = author.select_one('.loa__author-name img')
        if img == None:
            img = ''
        else:
            img = img['src']

        institution = list(author.select_one('.loa_author_inst').stripped_strings)
        if len(institution) == 0:
            institution = 'missing'
        else:
            institution = institution[0]
        
        profile = author.select_one('.author-info__body a[href^="/profile/"]')
        if profile == None:
            profile = 'missing'
        else:
            profile = profile['href'].removeprefix('/profile/')

        orcid = author.select_one('p.orcid-account a')
        if orcid == None:
            orcid = 'missing'
        else:
            orcid = orcid['href'].removeprefix('https://orcid.org/')
        
        authors.append({
            'name': name,
            'institution': institution,
            'img': img,
            'acmid': profile,
            'orcid': orcid
        })
    

    references = []
    ref_sec = soup.select_one('div h2#sec-ref')
    if ref_sec != None:
        for reference in ref_sec.parent.find_next('ol').select('li.references__item'):
            content = reference.select_one('span.references__note').contents
            content = [x for x in content if x.name == None][0]
            references.append({   
                'text': content,
                'doi': try_get_doi(reference)
            })
        

    return {
        'doi': doi,
        'title': title,
        'published': published.isoformat(),
        'proctitle': proctitle,
        'pages': pages,
        'year': published.year,
        'badges': badges,
        'abstract': abstract,
        'authors': authors,
        'references': references
    }

def parse_chairs(block):
    chairs = []
    current_group = 'Undefined'
    for row in block.select('li'):
        if 'label' in row.get_attribute_list('class'):
            current_group = row.text.strip().removesuffix(':').removesuffix('s').lower()
        elif '(Less)' in row.text:
            continue
        else:
            person = {
                'name': row.select_one('a span').text,
                'role': current_group,
                'acmid': row.select_one('a')['href'].removeprefix('/profile/'),
                'img': get_prop(row.select_one('img.author-picture'), 'src'),
                'institution': row.select_one('span.loa_author_inst').text
            }
            if 'default-profile' in person['img']:
                person['img'] = ''
            chairs.append(person)
    return chairs


def process_conference(content):
    soup = BeautifulSoup(content, 'html.parser')

    conf = {
        'title': soup.select_one('div.left-bordered-title').text.strip(),
        'year': int(soup.select_one('div.coverDate').text),
        'doi': soup.select_one('div.overlay-cover-wrapper a')['href'].removeprefix('/doi/proceedings/'),
        'chairs': []
    }

    for meta in soup.select('div.item-meta-row'):
        label = meta.select_one('div.item-meta-row__label')
        if label is None:
            conf['chairs'] = parse_chairs(meta)
        elif 'ISBN' in label.text:
            conf['isbn'] = meta.select_one('div.pages-info').text.strip()
        elif 'Published' in label.text:
            conf['published'] = acm_to_iso_date(meta.select_one('div.pages-info').text.strip())

    conf['papers'] = []
    skipped = set()
    for section in soup.select('div.sections div.rlist div.toc__section'):
        heading = section.select_one('a.section__title')
        if heading is None:
            heading = ''
        else:
            heading = heading.text.strip()
        
        for paper in section.select('div.issue-item-container'):
            papertype = paper.select_one('div.issue-heading').text
            if papertype not in ['Article', 'research-article', 'short-paper', 'note', 'tutorial']:
                skipped.add(papertype)
                continue

            title = paper.select_one('div.issue-item__content h5.issue-item__title').text
            conf['papers'].append({
                'doi': paper.select_one('div.issue-item__content h5.issue-item__title a')['href'].removeprefix('/doi/'),
                'title': title,
                'session': heading,
                'papertype': papertype,
                'badges': paper.select_one('div.badges').text
            })
    if len(skipped) > 1:
        print('Skipped', ', '.join(skipped))

    return conf

def process_series(content):
    soup = BeautifulSoup(content, 'html.parser')

    results = []
    for conf in soup.select('ul.conference__proceedings__container li.conference__proceedings div.conference__title'):
        links = conf.select('a')
        link = [l for l in links if 'proceedings' in l.text.lower()][0] # goes wrong for 1981, but we remove that one anyway
        results.append({
            'name': link.text,
            'year': parse_year(link.text),
            'url': 'https://dl.acm.org' + link['href'],
            'doi': link['href'].removeprefix('/doi/proceedings/')
        })        
    return results


if __name__ == '__main__':
    #with open('../cache/conferences/CHI2005.html', 'r', encoding='utf8') as f:
    #    process_conference(f.read())
    #with open('../cache/series/CHI.html', 'r', encoding='utf8') as f:
    #     process_series(f.read())
    #with open('../cache/papers/10.1145+3544548.3581258.html', 'r', encoding='utf8') as f:
    #    print(process_paper(f.read())['authors'])
    #with open('../cache/papers/10.1145+3025453.3026015.html', 'r', encoding='utf8') as f:
    #    print(process_paper(f.read())['authors'])
    with open('../cache/papers/10.1145+3544548.3581196.html', 'r', encoding='utf8') as f:
        print(process_paper(f.read())['badges'])
