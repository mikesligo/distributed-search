class Database(object):

    def __init__(self):
        # schema: {word: [{url:rank}]}
        self.__db = {}

    def get_results(self, word):
        return [result for result in self.__db[word]]

    def index_result(self, word, url):
        result = self.__db[word]

        for entry in result:
            if entry["url"] == url:
                entry["rank"] = entry["rank"] + 1
                return

        result.append({"url":url, "rank":1})