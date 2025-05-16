from augment import augment_paper_author
import pandas as pd

def fix_affiliations():
    fixes = pd.read_csv('affiliation_fixes.csv')
    for row in fixes.itertuples():
        augment_paper_author(
            row.year,
            row.doi,
            {'acmid': str(row.acmid)},
            {'institution': row.affiliation})


if __name__ == '__main__':
    fix_affiliations()


        
