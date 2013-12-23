

from Parser import Parser
from Node import Node
from src.networking.IP_Parser import IP_Parser
import threading

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
            t = threading.Thread(target=self.node.start_network, args=())
            t.start()

    def join_network(self, bootstrap_node_ip_addr):
        args = self.parser.get_parsed_args()
        if not args.boot:
            t = threading.Thread(target=self.__join_network, args=(bootstrap_node_ip_addr,))
            t.start()

    def __join_network(self, bootstrap_node_ip_addr):
        ip_parer = IP_Parser()
        self.node.join_network(ip_parer.parse(bootstrap_node_ip_addr))

    def leave_network(self, network_id):
        pass

    def index_page(self, url, unique_words):
        self.node.message_handler.setup_lock_event.wait(None)
        self.node.index_words_from_url(url, unique_words)

    def search(self, words):
        self.node.message_handler.setup_lock_event.wait(None)
        print "Thread unlocked..."
        self.node.search(words)
