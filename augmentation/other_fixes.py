from augment import augment_paper_author, remove_paper_author, add_paper_author


# Only partial name on paper and wrong acmid
# https://scholar.google.com/citations?hl=en&user=oJdqdYoAAAAJ
# https://engineering.tamu.edu/mechanical/profiles/vinayak.html
augment_paper_author(
    2017,
    '10.1145/3025453.3025825',
    dict(name='Vinayak -'),
    dict(acmid='99659451839', name='Vinayak Krishnamurthy'))

remove_paper_author(
    1992,
    '10.1145/142750.142832',
    dict(acmid='81332505988'))

add_paper_author(
    1992,
    '10.1145/142750.150712',
    dict(acmid='81341496917', name='Jared M. Spool', institution='User Interface Engineering'))
    
add_paper_author(
    1992,
    '10.1145/142750.150712',
    dict(acmid='81100424369', name='Bill Verplank', institution='IDEO'))
