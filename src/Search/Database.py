class Database(object):

    def __init__(self):
        # schema: {word: [{url:rank}]}
        self.__db = {}

    def get_results(self, word):
        if word not in self.__db.keys():
            return None
        return [result for result in self.__db[word]]

    def index_results(self, word, urls):
        # TODO make urls a set perhaps, need to only index once per page, not once per time on page
        for url in urls:
            self.__index_result(word, url)

    def __index_result(self, word, url):
        result = self.__db[word]

        for entry in result:
            if entry["url"] == url:
                entry["rank"] = entry["rank"] + 1
                return

        result.append({"url":url, "rank":1})

