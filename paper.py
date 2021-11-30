import urllib.request
import relevance_score as r
import numpy as np
import re

# MERIT

class Paper:
    def __init__(self, pubmedId):

        # url for pubmed file. see https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch for more info
        url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pubmedId}&retmode=text&rettype=medline'
        website = urllib.request.urlopen(url).read().decode('utf-8')

        self.id = pubmedId
        self.title = re.search(r'(?<=TI  - )[\s\S]*?(?=\.\n\S)', website).group().replace('\n      ', ' ') + '.'
        self.authors = re.findall('(?<=FAU - )[\s\S]*?(?=\n)', website)
        self.publishDate = re.search('(?<=EDAT- )[\s\S]*?(?= )', website).group()

        abstract = re.search(r'(?<=AB  - )[\s\S]*?(?=\.\n\S)', website).group().replace('\n      ', ' ') + '.'
        self.list = self.list = np.array([self.title, self.authors, self.year, self.id])
        self.score = None


    def set_score(self, filter_options):
        self.score = r.compute_score(self, filter_options)

