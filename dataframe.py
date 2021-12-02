import pandas as pd
import numpy as np
import paper as p

def create_df(table):
    # table should ba an array of all the papers lists that are being returned
    my_data = pd.DataFrame(data=table, index=None, columns=["title", "auther", "year", "DOI"])

    # get in html form:
    html_table = my_data.to_html()

p1 = p.Paper("paper1", "merit", "001", "2001", 0, 1)
p2 = p.Paper("paper2", "merit", "002", "2001", 0, 1)

paper_lists = np.array([p1.list])
print(paper_lists[0])

paper_lists = np.append(paper_lists, [p2.list], axis=0)
print(paper_lists)
print("\n")


#need to safe in single list:
#numpy_data = np.array([p1.list, ["paper2", "merit", "2002", "008"]])
numpy_data = paper_lists
data = pd.DataFrame(data=numpy_data, index=None, columns=["title", "author", "year", "DOI"])
print(data)