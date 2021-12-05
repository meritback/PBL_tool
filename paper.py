import urllib.request
import relevance_score as r
import numpy as np
import arguments
import re

# MERIT

class Paper:
    #one init needs to be outcommented: for testing purpose only
    """def __init__(self, name, author, year, id):
        self.id = id
        self.name = name
        self.authors = author
        self.publishDate = year
        self.score = None
        self.list = np.array([self.name, self.authors, self.publishDate, self.id])"""


    def __init__(self, medlineFile):
        # some pubmed IDs don't seem to work with the api, therefore we need to catch this error
        if not medlineFile.startswith('id:'):
            # attribute for checking if the paper can be properly created
            self.status = True

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

            searchTerm = arguments.searchTerm
            self.score = r.compute_score(searchTerm, self.title, abstract)

            #todo new
            self.list = np.array([self.title, self.authors[0], self.publishDate, self.id])
        else:
            self.status = False


    def set_score(self, filter_options):
            self.score = r.compute_score(self, filter_options)


