from bs4 import BeautifulSoup

with open('CHI2012.html', 'r', encoding='utf8') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

for paper in soup.select('div.submissionDetails'):
    best = paper.select_one('img.best')
    hm = paper.select_one('img.nominee')
    title = paper.select_one('a.title').text
    paper_type = paper.select_one('span.type').text

    if 'Study' in paper_type:
        continue
    
    if best is not None:
        print(f'2012,"{title}",Best Paper')
    if hm is not None:
        print(f'2012,"{title}",Honorable Mention')
    
