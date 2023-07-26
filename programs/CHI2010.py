from bs4 import BeautifulSoup

with open('CHI2010.html', 'r', encoding='utf8') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

best_papers = set()
honorable_mentions = set()

for paper in soup.select('div.title'):
    title = paper.text.strip()
    best = paper.select_one('img[alt="Best Paper"]')
    hm = paper.select_one('img[alt="Honorable Mention"]')

    if best != None:
        best_papers.add(title)
    if hm != None:
        honorable_mentions.add(title)

for paper in best_papers:
    print(f'2010,"{paper}",Best Paper')
for paper in honorable_mentions:
    print(f'2010,"{paper}",Honorable Mention')

