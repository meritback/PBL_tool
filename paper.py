import urllib.request
import relevance_score as r
import numpy as np
import re
import runner


class Paper:
    def __init__(self, medlineFile):
        # some pubmed IDs don't seem to work with the api, therefore we need to catch this error
        if not medlineFile.startswith('id:'):
            self.id = re.search(r'(?<=PMID- )\d+(?=\n)', medlineFile).group()
            self.title = re.search(r'(?<=TI  - )[\s\S]*?(?=[.?]\n\S)', medlineFile).group().replace('\n      ', ' ') + '.'
            self.authors = re.findall(r'(?<=FAU - )[\s\S]*?(?=\n)', medlineFile)
            self.publishDate = re.search(r'(?<=EDAT- )[\s\S]*?(?= )', medlineFile).group()
            self.keywords = re.findall(r'(?<=OT  - )[\s\S]*?(?=\n)', medlineFile)

            regexAbstract = re.search(r'(?<=AB  - )[\s\S]*?(?=[.?]\n\S)', medlineFile)
            # some abstracts are not available
            if regexAbstract is not None:
                abstract = regexAbstract.group().replace('\n      ', ' ') + '.'
            else:
                abstract = ''
            self.score = None

# keyword can be accessed with runner.keyword

    def set_score(self, filter_options):
        self.score = r.compute_score(self, filter_options)
