from Encoder import Encoder
from networking.Listener import Listener
from networking.IP_Parser import IP_Parser
from networking.Network_utils import Network_utils
from Global.Global_consts import Global_consts
from src.Routing.RoutingTable import RoutingTable

class Node():

    def __init__(self, socket=None, id=None):
        self.encoder = Encoder()
        self.socket = socket or Network_utils.get_default_udp_socket()
        id = id or self.__generate_random_id()
        parser = IP_Parser()
        self.table = RoutingTable(id, parser.get_default_IP())

    def __generate_random_id(self):
        return self.encoder.generate_random_id()

    def start_network(self):
        self.listener = Listener(self.socket, self.table)
        self.listener.listen()
