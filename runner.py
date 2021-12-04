#import sys
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')
#import numpy
import re
import urllib.request
import argparse



# get user input from gui

import paper


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
    # create papers and add all papers to an array!
    #call dataframe and give back dataframe instead of idList. this needs an array of papers(not just ids)
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

    def access_pubmed():  # Willi
        url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' \
              f'{args.keyword}&retmax={args.numberOfPapers}'

        website = urllib.request.urlopen(url).read().decode('utf-8')
        idList = re.findall(r'(?<=<Id>)\d{8}(?=</Id>)', website)
        idList = list(map(int, idList))
        paperList =[]
        for pubmedId in idList:
            paperList.append(paper.Paper(pubmedId))
        print(paperList)


    #def sort_and_cutoff(unsorted_papers):  # Merit & Franzi
    #    return sorted_papers  # list
    #    # return list to gui (the first 20?)

    access_pubmed()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()



