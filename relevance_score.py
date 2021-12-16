## compute relevance score
#Filter options

#Journal
#NunCitations


# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html

import re


def compute_score(searchTerm, paperTitle, paperAbstract):
    abstractScore = len(re.findall(searchTerm, paperAbstract, re.IGNORECASE))
    multiplier = compute_multiplier(searchTerm, paperTitle)
    return abstractScore * multiplier

def compute_multiplier(searchTerm, paperTitle):
    normalMultiplier = 1
    wordsInTitle = len(re.findall(searchTerm, paperTitle, re.IGNORECASE))

    if(wordsInTitle > 0):
        return wordsInTitle * 10
    else:
        return normalMultiplier