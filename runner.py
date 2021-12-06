#import sys
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')
#import numpy
import re
import urllib.request
import argparse
import paper
import arguments
import dataframe


def pubmed(keyword, num):
    #todo testing: use different constructor for paper
    #return dataframe.testing_for_html
    print("runnning pubmed")

    # set keyword in arguments class
    arguments.set_searchTerm(keyword)

    # calling pubmed-API via a url. for more info see: https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=' \
          f'{keyword}&retmax={num}&usehistory=y'
    website = urllib.request.urlopen(url).read().decode('utf-8')

    queryKey = re.search(r'(?<=<QueryKey>)\d+(?=<\/QueryKey>)', website).group()
    webEnv = re.search(r'(?<=<WebEnv>)[\w\W]*(?=<\/WebEnv>)', website).group()

    # calling pubmed-API via a url. for more info see: https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key={queryKey}&WebEnv' \
          f'={webEnv}&rettype=medline&retmax={num}'
    website = urllib.request.urlopen(url).read().decode('utf-8')
    website = website.strip('\n')
    medlineList = website.split('\n\n')
    website = ''

    paperList = []
    while len(medlineList) > 0:
        paperObject = paper.Paper(medlineList[0])
        if paperObject.status:
            paperList.append(paperObject)
        del medlineList[0]
    #sort papers by their score
    sortedList = sorted(paperList, key=lambda paper: paper.score, reverse=True);

    #return dataframe.create_df(paperList)
    return dataframe.create_df(sortedList)


# stuff to run always here such as class/def
def main():
    # argument parser for testing
    parser = argparse.ArgumentParser(description='Fetching and ranking pubmed papers',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k', '--keyword',
                        type=str,
                        help='keyword to be included in paper abstract',
                        default='cancer',
                        metavar='')
    parser.add_argument('-n', '--numberOfPapers',
                        type=int,
                        help='maximum number of papers to be searched',
                        default=100,
                        metavar='')
    args = parser.parse_args()
    arguments.set_searchTerm(args.keyword)

    paperList = pubmed(args.keyword, args.numberOfPapers)
    print(len(paperList))


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()