from bs4 import BeautifulSoup

with open('CHI2011.html', 'r', encoding='utf8') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

def parse_section(id, kind):   
    for tag in soup.select_one(id).next_siblings:
        if tag.name == 'h3':
            return
        if tag.name != 'p':
            continue
        title = tag.select_one('b').text
        print(f'2011,"{title}",{kind}')

parse_section('h3#bestpapers', 'Best Paper')
parse_section('h3#bestnotes', 'Best Paper')
parse_section('h3#hmpapers', 'Honorable Mention')
parse_section('h3#hmnotes', 'Honorable Mention')
