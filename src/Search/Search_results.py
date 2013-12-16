class Search_results(object):

    def __init__(self):
        self.results = {}

    def load_results_from_response(self, word, responses):
        if not responses:
            return
        for response in responses:
            url = response["url"]
            rank = response["rank"]
            self.results[word] = {url:rank}
