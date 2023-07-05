from augment import augment_paper_author


# Only partial name on paper and wrong acmid
# https://scholar.google.com/citations?hl=en&user=oJdqdYoAAAAJ
# https://engineering.tamu.edu/mechanical/profiles/vinayak.html
augment_paper_author(
    2017,
    '10.1145/3025453.3025825',
    dict(name='Vinayak -'),
    dict(acmid='99659451839', name='Vinayak Krishnamurthy'))




