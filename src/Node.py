from src.networking import IP_Parser

__author__ = 'mike'

from Encoder import Encoder
from networking.Listener import Listener
from networking.IP_Parser import IP_Parser
from networking.Network_utils import Network_utils

class Node():

    def __init__(self, socket=None, id=None):
        self.encoder = Encoder()
        self.id = id or self.__generate_random_id()
        self.socket = socket or Network_utils.get_default_udp_socket()

    def __generate_random_id(self):
        return self.encoder.generate_random_id()

    def start_network(self):
        self.listener = Listener(self.socket)
        self.listener.listen()
