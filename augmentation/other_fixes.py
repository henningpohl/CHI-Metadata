from augment import augment_paper_author, remove_paper_author, add_paper_author, augment_paper

def apply_other_fixes():

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

    augment_paper_author(
        2014,
        '10.1145/2556288.2556957',
        dict(name='Soroush Vosoughi'),
        dict(acmid='99660786853', img='/pb-assets/icons/DOs/default-profile-1543932446943.svg'))

    augment_paper_author(
        1988,
        '10.1145/57167.57192',
        dict(name='R. Guidon', acmid='81332502415'),
        dict(acmid='81329489045', name=''))

    # Some missing authors
    add_paper_author(
        1989,
        '10.1145/67449.67494',
        dict(acmid='81100021992', name='Robert A. Gargan Jr', institution='Lockheed Missiles and Space Co, Menlo Park, CA'))
    add_paper_author(
        1989,
        '10.1145/67449.67494',
        dict(acmid='81100510774', name='Jon L. Schlossberg', institution='Lockheed Missiles and Space Co, Menlo Park, CA'))
    add_paper_author(
        1989,
        '10.1145/67449.67494',
        dict(acmid='81542462256', name='Sherman W. Tyler', institution='Lockheed Missiles and Space Co, Menlo Park, CA'))

    # skipped because no info found for that author
    #add_paper_author(
    #    1988,
    #    '10.1145/57167.57173,
    #    dict(acmid='???', name='Antonio Romero', institution='Princeton Univ., Princeton, NJ'))

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

    augment_paper(1993, '10.1145/169059.169072', {'pages': '55'})
    augment_paper(1993, '10.1145/169059.169233', {'pages': '303'})
    augment_paper(1993, '10.1145/169059.169459', {'pages': '514'})
    augment_paper(1993, '10.1145/169059.169467', {'pages': '515'})
    augment_paper(1993, '10.1145/169059.169488', {'pages': '518'})
    augment_paper(1993, '10.1145/169059.169494', {'pages': '519'})
    augment_paper(1993, '10.1145/169059.169506', {'pages': '521'})
    augment_paper(1993, '10.1145/169059.169517', {'pages': '524'})
    augment_paper(1993, '10.1145/169059.169528', {'pages': '531'})
    augment_paper(1993, '10.1145/169059.280187', {'pages': '535'})
    augment_paper(1996, '10.1145/238386.238446', {'pages': '111-117'})
    augment_paper(1996, '10.1145/238386.238585', {'pages': '399-405'})
    augment_paper(1996, '10.1145/238386.238587', {'pages': '406-412'})
    augment_paper(1996, '10.1145/238386.238599', {'pages': '436-441'})
    augment_paper(1996, '10.1145/238386.238608', {'pages': '466-472'})
    augment_paper(2007, '10.1145/1240624.1240807', {'pages': '1205-1214'})

    # All the CHI 1987 papers are supposedly published in May 1986
    augment_paper(1987, '10.1145/29933.275623', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275624', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275625', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275626', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275627', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275628', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275630', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275631', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275632', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275633', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275635', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275636', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275637', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275638', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275639', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275640', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275642', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275643', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275644', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275645', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275646', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275647', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275649', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275650', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275651', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275653', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275654', {'year': 1987})
    augment_paper(1987, '10.1145/29933.275837', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30852', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30853', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30854', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30855', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30856', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30857', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30858', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30859', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30860', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30861', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30862', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30863', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30864', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30865', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30866', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30867', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30868', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30869', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30870', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30871', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30872', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30873', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30874', {'year': 1987})
    augment_paper(1987, '10.1145/29933.30875', {'year': 1987})

if __name__ == '__main__':
    apply_other_fixes()
