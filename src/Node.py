__author__ = 'mike'

from Encoder import Encoder

class Node():

    def __init__(self, id=None):
        self.encoder = Encoder()
        self.id = id or self.__generate_random_id()

    def __generate_random_id(self):
        return self.encoder.generate_random_id()
