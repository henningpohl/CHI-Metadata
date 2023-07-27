from data import paper_iter

for year, doi, paper in paper_iter():
    if int(year) != int(paper['year']):
        print(year, '!=', paper['year'], doi)
