import os
import json

def file_iter(basedir):
    for year in os.listdir(basedir):
        folder = os.path.join(basedir, year)
        for fn in os.listdir(folder):
            if fn.endswith('.json'):
                doi, _ = os.path.splitext(fn)
                doi = doi.replace('+', '/')
                yield (year, doi, os.path.join(folder, fn))

def paper_iter():
    for year, doi, file_path in file_iter(os.path.join('..', 'data', 'papers')):
        with open(file_path, 'r', encoding='utf-8') as f:
            yield (year, doi, json.load(f))
