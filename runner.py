import paper as p
import re
import urllib.request
import argparse



# get user input from gui
def pubmed(keyword, num):
    parser = argparse.ArgumentParser(description='Fetching and ranking pubmed papers',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k', '--keyword',
                        type=str,
                        help='keyword to be included in paper abstract',
                        default=keyword,
                        metavar='')
    parser.add_argument('-n', '--numberOfPapers',
                        type=int,
                        help='maximum number of papers to be searched',
                        default=num,
                        metavar='')
    args = parser.parse_args()

    # testing
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' \
          f'{args.keyword}&retmax={args.numberOfPapers}'

    website = urllib.request.urlopen(url).read().decode('utf-8')
    idList = re.findall(r'(?<=<Id>)\d{8}(?=</Id>)', website)
    idList = list(map(int, idList))
    return idList


# stuff to run always here such as class/def
def main():
    # argument parser for testing
    parser = argparse.ArgumentParser(description='Fetching and ranking pubmed papers',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k', '--keyword',
                        type=str,
                        help='keyword to be included in paper abstract',
                        default='bioinformatics',
                        metavar='')
    parser.add_argument('-n', '--numberOfPapers',
                        type=int,
                        help='maximum number of papers to be searched',
                        default=100,
                        metavar='')
    args = parser.parse_args()

    # testing
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' \
          f'{args.keyword}&retmax={args.numberOfPapers}'

    website = urllib.request.urlopen(url).read().decode('utf-8')
    idList = re.findall(r'(?<=<Id>)\d{8}(?=</Id>)', website)
    idList = list(map(int, idList))
    print(idList)
    print(len(idList))

    def access_pubmed():  # Willi
        # each paper as instance of paper class
        # call scanning function
        # all_papers = [paper1, paper2]
        i = 0
        # scanned_papers  # p.Paper[] #list of papers
        # for paper in all_papers:
        #     scanned_papers[i] = scanner(paper)
        #     i += 1
        # parse to get sorted
        # sorted_papers = sort_and_cutoff(scanned_papers)
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

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()



