import pandas as pd
import numpy as np
import paper as p


def create_df(paperList):
    print(paperList)
    paper_lists = []
    for paper in paperList:
        paper_lists.append(paper.list)

    # table should ba an array of all the papers lists that are being returned
    my_data = pd.DataFrame(data=paper_lists, index=None, columns=["title", "author", "year", "score", "DOI"])
    print(my_data)
    return my_data


def testing_for_html():
    p1 = p.Paper("paper1", "merit", "2001", "01")
    p2 = p.Paper("paper2", "merit", "2001", "02")

    paper_lists = np.array([p1.list])
    paper_lists = np.append(paper_lists, [p2.list], axis=0)

    # need to safe in single list:
    # numpy_data = np.array([p1.list, ["paper2", "merit", "2002", "008"]])
    numpy_data = paper_lists
    data = pd.DataFrame(data=numpy_data, index=None, columns=["title", "author", "year", "DOI"])
    return data

#for testing only
"""p1 = p.Paper("paper1", "merit", "2001", "01")
p2 = p.Paper("paper2", "merit", "2001", "02")

#paper_lists = np.array([p1.list])
#paper_lists = np.append(paper_lists, [p2.list], axis=0)

papers = []
papers.append(p1)
papers.append(p2)

paper_lists = []
paper_lists.append(p1.list)
paper_lists.append(p2.list)


create_df(papers)
"""