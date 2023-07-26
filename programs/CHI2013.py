from bs4 import BeautifulSoup

with open('CHI2013.html', 'r', encoding='utf8') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

for paper in soup.select('li.presentation'):
    best = paper.select_one('span.best')
    hm = paper.select_one('span.honorable')
    title = paper.select_one('span.title').text
    
    if best is not None:
        print(f'2013,"{title}",Best Paper')
    if hm is not None:
        print(f'2013,"{title}",Honorable Mention')
    
