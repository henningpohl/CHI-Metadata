import os
import pandas as pd

papers = pd.read_csv(os.path.join('..', 'data', 'chipapers.csv'))

print(papers.groupby('year')['doi'].count())
print(len(papers), 'overall')
