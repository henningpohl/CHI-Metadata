from augment import augment_paper_author, remove_paper_author, add_paper_author, augment_paper_pages


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

# not actually a paper so removed now
#add_paper_author(
#    1992,
#    '10.1145/142750.150712',
#    dict(acmid='81341496917', name='Jared M. Spool', institution='User Interface Engineering'))
#  
#add_paper_author(
#    1992,
#    '10.1145/142750.150712',
#    dict(acmid='81100424369', name='Bill Verplank', institution='IDEO'))

augment_paper_pages(1993, '10.1145/169059.169072', '55')
augment_paper_pages(1993, '10.1145/169059.169074', '56')
augment_paper_pages(1993, '10.1145/169059.169120', '144')
augment_paper_pages(1993, '10.1145/169059.169199', '248')
augment_paper_pages(1993, '10.1145/169059.169233', '303')
augment_paper_pages(1993, '10.1145/169059.169459', '514')
augment_paper_pages(1993, '10.1145/169059.169467', '515')
augment_paper_pages(1993, '10.1145/169059.169488', '518')
augment_paper_pages(1993, '10.1145/169059.169494', '519')
augment_paper_pages(1993, '10.1145/169059.169506', '521')
augment_paper_pages(1993, '10.1145/169059.169517', '524')
augment_paper_pages(1993, '10.1145/169059.169528', '531')
augment_paper_pages(1993, '10.1145/169059.280187', '535')
augment_paper_pages(1996, '10.1145/238386.238446', '111-117')
augment_paper_pages(1996, '10.1145/238386.238585', '399-405')
augment_paper_pages(1996, '10.1145/238386.238587', '406-412')
augment_paper_pages(1996, '10.1145/238386.238599', '436-441')
augment_paper_pages(1996, '10.1145/238386.238608', '466-472')
augment_paper_pages(2007, '10.1145/1240624.1240807', '1205-1214')
