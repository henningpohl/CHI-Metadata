# CHI-Metadata Repository



## Running the Scraping and Processing

1) First run the conference scraper (`/scraping/scrape_conferences.py`) that gathers the CHI conference pages from the ACM DL. Afterwards you should have a JSON file with links to each conference, one json per conference with the list of papers, and a csv file of all the papers found across these conferences.
2) Run `/scraping/scrape_papers.py` to download the ACM DL pages for each of the papers and extract the metadata from them. You should now have one folder per year under `/data/papers` with one json file per paper. Files are named after the paper DOIs, with '/' replaced by ' +'.
3) Some scraping might have gone wrong, run `/scraping/fixes.py` to redo some of them. Right now this only looks for email handle replacement (i.e., removing all text with an @ inside it, email or not) from the ACM CDN.
4) Apply the data augmentation and fixing scripts from the `/augmentation` folder:
    1) `/augmentation/acceptance_rates.py` pull acceptance rates from the SIGCHI page (note that the numbers there and on the ACM DL do not always agree 🤷‍) and adds this info to the conference data files.
    2) `/augmentation/author_id_fixer.py` applies a set of manual corrections to author information, per `/augmentation/author_id_fixes.csv`
    3) `/augmentation/orcid_backfill.py` finds orcid ids from the full set of papers and adds them to earlier papers of the authors. Some manual overrides are defined in the script as well.
    4) `/augmentation/other_fixes.py` are some random corrections that did not fit in elsewhere, such as removing wrong authors.
	5) `/augmentation/add_awards.py` fills in award information for CHI 2010-2015, where this information is not listed on the paper pages.
