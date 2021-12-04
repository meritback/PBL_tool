import pandas as pd
import numpy as np
import paper as p


def create_df(table):
    # table should ba an array of all the papers lists that are being returned
    my_data = pd.DataFrame(data=table, index=None, columns=["title", "auther", "year", "DOI"])

    # get in html form:
    html_table = my_data.to_html()

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

p1 = p.Paper("paper1", "merit", "2001", "01")
p2 = p.Paper("paper2", "merit", "2001", "02")

paper_lists = np.array([p1.list])
paper_lists = np.append(paper_lists, [p2.list], axis=0)

# need to safe in single list:
# numpy_data = np.array([p1.list, ["paper2", "merit", "2002", "008"]])
numpy_data = paper_lists
data = pd.DataFrame(data=numpy_data, index=None, columns=["title", "author", "year", "DOI"])
print(data)
