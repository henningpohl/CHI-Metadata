import os
import difflib
import pandas as pd
from augment import augment_paper_award

papers = pd.read_csv(os.path.join('..', 'data', 'chipapers.csv'))
awards = pd.read_csv('awards.csv', comment='#')

papers['title'] = papers['title'].str.lower()

for row in awards.itertuples():
    candidates = papers[papers['year'] == row.year].copy()
    title = row.title.lower()

    def match(entry):
        return difflib.SequenceMatcher(a=title, b=entry).ratio()

    candidates['match'] = candidates['title'].apply(match)

    idx = candidates['match'].idxmax()
    score = candidates.loc[idx, 'match']
    doi = candidates.loc[idx, 'doi']

    if score < 0.9:
        print("WARNING: couldn't match paper award")
        print('Year:', row.year)
        print('Title:', title)
        print('Best Match Score:', score, 'DOI:', doi)
        print(candidates.loc[idx, 'title'])
        print()
    else:
        augment_paper_award(row.year, doi, [row.award])
    

