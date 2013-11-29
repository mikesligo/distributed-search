__author__ = 'mike'

from Parser import Parser
from Node import Node

class Peer_search():

    def __init__(self):
        self.node = None
        self.socket = None

    def init(self, udp_socket):
        parser = Parser()
        args = parser.get_parsed_args()
        self.node = Node(udp_socket, id=args.id)
        if args.boot:
            self.node.start_network()

    def join_network(self, bootstrap_node_ip_addr):
        pass

    def leave_network(self, network_id):
        pass

    def index_page(self, url, unique_words):
        pass

    def search(self, words):
        pass