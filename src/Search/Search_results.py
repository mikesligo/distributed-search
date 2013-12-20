class Search_results(object):

    def __init__(self, word, responses):
        self.word = word
        self.results = []
        for response in responses:
            url = response["url"]
            rank = response["rank"]
            self.results.append({"url":url, "rank": rank})