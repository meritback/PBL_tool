import relevance_score as r
#MERIT

class Paper:

    def __init__(self, title, authors, id, year, count_abstract, count_title):
        self.title = title
        self.authors = authors
        self.id = id
        self.year = year
        self.count_abstract = count_abstract
        self.count_title = count_title
        self.score = None

    def set_score(self, filter_options):
        self.score = r.compute_score(self, filter_options)
