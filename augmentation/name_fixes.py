from augment import augment_paper_author
import pandas as pd

def fix_names():
    fixes = pd.read_csv('name_fixes.csv')
    for row in fixes.itertuples():
        augment_paper_author(
            row.year,
            row.doi,
            {'acmid': str(row.acmid)},
            {'name': row.newName})

if __name__ == '__main__':
    fix_names()
