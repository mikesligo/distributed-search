class Database(object):

    def __init__(self):
        # schema: {word: [{url:rank}]}
        self.__db = {}

    def get_results(self, word):
        if word not in self.__db.keys():
            return None
        return [result for result in self.__db[word]]

    def index_results(self, word, urls):
        for url in urls:
            self.__index_result(word, url)

    def __index_result(self, word, url):
        if word not in self.__db.keys():
            self.__db[word] = [{"url":url, "rank": 1}]
        else:
            for entry in self.__db[word]:
                if entry["url"] == url:
                    entry["rank"] = entry["rank"] + 1
                    return
            self.__db[word].append({"url":url,"rank":1})