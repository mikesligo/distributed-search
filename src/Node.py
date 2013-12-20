from Encoder import Encoder
from networking.Listener import Listener
from networking.IP_Parser import IP_Parser
from src.Routing.RoutingTable import RoutingTable
from src.Messages.Message_handler import Message_handler

class Node():

    def __init__(self, socket, id, ip):
        self.__encoder = Encoder()
        self.socket = socket
        id = id or self.__generate_random_id()
        parser = IP_Parser()
        if ip:
            self.ip = parser.parse(ip)
        else:
            self.ip = parser.get_default_IP()
        self.table = RoutingTable(id, self.ip)
        self.message_handler = Message_handler(self.table, self.socket)


    def __generate_random_id(self):
        return self.__encoder.generate_random_id()

    def start_network(self):
        self.message_handler.setup_lock_event.set()
        self.listener = Listener(self.message_handler)
        self.listener.listen()

    def join_network(self, bootstrap_ip):
        self.message_handler.join_network(bootstrap_ip)
        self.listener = Listener(self.message_handler)
        self.listener.listen()

    def search(self, words):
        self.listener.message_handler.search(words)

    def index_words_from_url(self, url, unique_words):
        for word in set(unique_words):
            self.message_handler.index(word, url)