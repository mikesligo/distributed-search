__author__ = 'mike'

from Encoder import Encoder
from networking.Listener import Listener
from IP_Parser import IP_Parser

class Node():

    def __init__(self, id=None, boot=False, ip=None):
        self.encoder = Encoder()
        self.id = id or self.__generate_random_id()
        self.boot = boot
        parser = IP_Parser()
        self.IP = ip or parser.get_default_IP()
        if self.boot:
            self.__start_network()

    def __generate_random_id(self):
        return self.encoder.generate_random_id()

    def __start_network(self):
        self.listener = Listener(self.IP)
