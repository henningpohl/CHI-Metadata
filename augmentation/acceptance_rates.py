import os
import re
import json
import sys
sys.path.append(os.path.join('..', 'scraping'))
import cache
from datetime import datetime
from bs4 import BeautifulSoup
from augment import augment_conference
import pandas as pd

def fix_year(text):
    m = re.match(r"CHI ['’](\d+)", text.strip())
    dt = datetime.strptime(m.group(1), '%y')
    if(dt.year > 2050):
        return dt.year - 100
    else:
        return dt.year

def parse_acceptance_rate(text):
    m = re.match(r"(\d+)/(\d+) = (\d+(?:.\d+)?)%", text.strip())
    return int(m.group(1)), int(m.group(2)), float(m.group(3))

def scrape_acceptance_rates():
    url = 'https://sigchi.org/conferences/conference-history/CHI/'
    content = cache.get_page('CHI-History', url)
    soup = BeautifulSoup(content, 'html.parser')

    table = soup.select_one('table.listing')
    data = []
    for row in table.select('tbody tr'):
        year = fix_year(row.select_one('td[data-mtr-content="Archive"]').text)
        pubs = row.select('td[data-mtr-content="Publications"] a')
        accepted, submitted, rate = parse_acceptance_rate(row.select_one('td[data-mtr-content~="Acceptance"]').text)

        data.append({
            'Year': year,
            'Submitted': submitted,
            'Accepted': accepted,
            'AcceptanceRate': rate
        })
    return data

def get_acceptance_rates():
    if os.path.exists('acceptance_rates.csv'):
        return pd.read_csv('acceptance_rates.csv')

    data = scrape_acceptance_rates()
    data = pd.DataFrame(data)
    data.to_csv('acceptance_rates.csv', index=False)
    return data

def augment_acceptance_rates():
    data = get_acceptance_rates()
    
    for row in data.itertuples():
        fields = {
            'submitted papers': row.Submitted,
            'accepted papers': row.Accepted,
            'acceptance rate': row.AcceptanceRate
        }
        augment_conference('CHI', str(int(row.Year)), fields)
        print('Added acceptance rate data for CHI %d' % row.Year)      

    
if __name__ == '__main__':
    augment_acceptance_rates()
