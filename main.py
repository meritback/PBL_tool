import paper as p
import re
import urllib.request


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# get user input from gui

# testing
test_keyword = 'cancer'
test_amount = 100
url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={test_keyword}&retmax={test_amount}'
website = urllib.request.urlopen(url).read().decode('utf-8')
print(website)
list = re.findall(r'(?<=<Id>)\d{8}(?=</Id>)', website)
print(list)

def access_pubmed():  # Willi
    # each paper as instance of paper class
    # call scanning function
    #all_papers = [paper1, paper2]
    i = 0
    #scanned_papers  # p.Paper[] #list of papers
    # for paper in all_papers:
    #     scanned_papers[i] = scanner(paper)
    #     i += 1
    # parse to get sorted
    #sorted_papers = sort_and_cutoff(scanned_papers)
    # return sorted_papers


def scanner(paper):  # Merit & Franzi
    # with regex as well
    abstract
    title = "my_title"
    authors = "my_authors"
    id = 0
    year = 2021
    # call count matches for each section
    count_title = count_matches(title)
    count_abstract = count_matches(abstract)
    paper = p.Paper(title=title, authors=authors, id=id, year=year, count_abstract=count_abstract,
                    count_title=count_title)
    return paper


def count_matches(String):  # Berkem
    matches = 0
    # parse abstract and title
    # use regex
    countTitle
    countAbstract
    # call compute relevance score
    # set instance variable of paper's variable "relevance score"
    return matches


def sort_and_cutoff(unsorted_papers):  # Merit & Franzi
    return sorted_papers  # list
    # return list to gui (the first 20?)


sorted_papers = access_pubmed()
