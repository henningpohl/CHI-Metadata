import json

with open('CHI2015.json', 'r', encoding='utf8') as f:
    data = json.load(f)

for key in data:
    info = data[key]
    title = info['title']

    if 'award' not in info:
        continue
    
    if info['award']:
        print(f'2015,"{title}",Best Paper')
    if info['hm']:
        print(f'2015,"{title}",Honorable Mention')
    

