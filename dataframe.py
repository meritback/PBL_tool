import pandas as pd
import numpy as np
import paper as p


def create_df(paperList):
    print(paperList)
    paper_lists = []
    for paper in paperList:
        paper_lists.append(paper.list)

    # table should ba an array of all the papers lists that are being returned
    my_data = pd.DataFrame(data=paper_lists, index=None, columns=["title", "author", "date", "score", "ID"])
    #my_data = pd.DataFrame(data=paper_lists, index=None, columns=["title", "author", "date", "score", "Pubmed ID"])
    print(my_data)
    return my_data