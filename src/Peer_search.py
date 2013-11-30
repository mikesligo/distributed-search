__author__ = 'mike'

from Parser import Parser
from Node import Node
from src.networking.IP_Parser import IP_Parser

class Peer_search():

    def __init__(self):
        self.node = None
        self.socket = None
        self.parser = Parser()

    def init(self, udp_socket):
        args = self.parser.get_parsed_args()
        self.socket = udp_socket
        self.node = Node(udp_socket, args.id, args.ip)
        if args.boot:
            self.node.start_network()

    def join_network(self, bootstrap_node_ip_addr):
        ip_parer = IP_Parser()
        self.node.join_network(ip_parer.parse(bootstrap_node_ip_addr))

    def leave_network(self, network_id):
        pass

    def index_page(self, url, unique_words):
        pass

    def search(self, words):
        pass