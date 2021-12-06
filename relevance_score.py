## compute relevance score
#Filter options

#Journal
#NunCitations
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