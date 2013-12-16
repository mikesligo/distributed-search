import json
from Send_formatter import Send_formatter
from src.networking.IP_Parser import IP_Parser
from Exceptions.Table_lookup_failed_exception import Table_lookup_failed_exception
from src.Encoder import Encoder
from src.Search.Search_results import Search_results
from src.Search.Database import Database
import threading

class Message_handler(object):

    def __init__(self, table, socket):
        self.parser = IP_Parser()
        self.table = table
        self.socket = socket
        self.__send_formatter = Send_formatter(self.table)
        self.__encoder = Encoder()
        self.__db = Database()
        self.setup_lock_event = threading.Event()

    def handle(self, data, sender_addr):
        message = json.loads(data)
        message_type = message["type"]

        if not self.__valid_message(message_type):
            print "Warning - Malformed message received"
            return

        print "Received message - " + message_type + " from " + str(sender_addr[0]) + ":" + str(sender_addr[1])
        print message

        if message_type == "JOINING_NETWORK":
            self.__handle_joining_network(message, sender_addr)
        if message_type == "ROUTING_INFO":
            self.setup_lock_event.set()
            self.__handle_routing_info(message, sender_addr)
        if message_type == "JOINING_NETWORK_RELAY":
            self.__handle_joining_network_relay(message)
        if message_type == "SEARCH_RESPONSE":
            self.__handle_search_response(message)
        if message_type == "SEARCH":
            self.__handle_search(message)
        if message_type == "INDEX":
            self.__handle_index(message)

    def __valid_message(self, message_type):
        return message_type

    def join_network(self, bootstrap_ip):
        to_send = self.__send_formatter.send_joining_network()
        self.send_message(to_send, bootstrap_ip.get_ip_pair())

    def __handle_routing_info(self, message, sender_addr):
        self.table.load_routing_info(message["route_table"])
        if self.__sender_is_gateway(message, sender_addr):
            self.table.add_routing_info(message["gateway_id"], message["ip_address"])
        self.__forward_routing_info_if_necessary(message)

    def __sender_is_gateway(self, message, sender_addr):
        msg_ip = str(message["ip_address"])
        parsed_sender_addr = str(self.parser.parse_from_tuple(sender_addr))
        return msg_ip == parsed_sender_addr

    def __forward_routing_info_if_necessary(self, message):
        node_id = message["node_id"]
        gateway_id = message["gateway_id"]

        if not self.__id_is_me(node_id):
            if self.__id_is_me(gateway_id):
                ip = self.__normalise_ip_to_pair(node_id)
                jsoned = json.dumps(message)
                self.send_message(jsoned, ip)
            else:
                print "Error - Expecting to forward routing info but I am not gateway"
                return

    def __id_is_me(self, node_id):
        return int(node_id) == int(self.table.node_id)

    def __handle_joining_network_relay(self, message):
        gateway_id = message["gateway_id"]
        node_id = message["node_id"]

        if self.__id_is_me(node_id):
            return
        self.__forward_message_to_closest_node(message, node_id)

        if not self.__id_is_me(gateway_id):
            new_known_ip = self.table.get_ip_of_node(gateway_id)
            self.table.add_routing_info(node_id, new_known_ip)

        to_send = self.__send_formatter.send_routing_info(node_id, gateway_id)
        self.send_to_node_id(to_send, gateway_id)

    def send_to_node_id(self, message, node_id):
        ip = self.__normalise_ip_to_pair(node_id)
        self.send_message(message, ip)

    def __handle_joining_network(self, message, sender_addr):
        node_id = message["node_id"]
        node_ip = message["ip_address"]

        to_send_forward = self.__send_formatter.send_joining_network_relay(node_id)
        self.__forward_message_to_closest_node(to_send_forward, node_id)

        to_send = self.__send_formatter.send_routing_info(node_id, self.table.node_id)
        self.table.add_routing_info(node_id, node_ip)
        self.send_message(to_send, sender_addr)

    def send_message(self, message, sender_addr):
        sender_ip = str(sender_addr[0])
        sender_port = str(sender_addr[1])
        loaded = json.loads(message)
        print "Sending " + loaded["type"] + " to " + sender_ip + ":" + sender_port
        print message
        self.socket.sendto(message, sender_addr)

    def __normalise_ip_to_pair(self, node_id):
        try:
            node_ip = self.table.get_ip_of_node(node_id)
        except KeyError:
            print "----------- Error - Could not find ip of node " + str(node_id)
            raise Table_lookup_failed_exception("Could not find ip for id " + str(node_id))
        normalised_ip = self.parser.parse(node_ip).get_ip_pair()
        return normalised_ip

    def search(self, words):
        for word in words:
            hash_of_word = self.__encoder.get_hash_of_word(word)
            print "Hash is " + str(hash_of_word)
            closest_node = self.table.get_closest_node_id(hash_of_word)
            if closest_node:
                message = self.__send_formatter.search(word, closest_node)
                ip = self.__normalise_ip_to_pair(closest_node)
                self.send_message(message, ip)
            #TODO what if I am the node with the info
        #TODO handle pings

    def __handle_search(self, message):
        word = message["word"]
        target_node_id = message["sender_id"]
        results = self.__db.get_results(word)
        message = self.__send_formatter.search_response(word, target_node_id, results)

        self.__forward_message_to_closest_node(message, target_node_id)

    def __handle_search_response(self, message):
        node_id = message["node_id"]

        if self.__id_is_me(node_id):
            word = message["word"]
            responses = message["response"]
            search_result = Search_results()
            search_result.load_results_from_response(word, responses)
            return search_result
        else:
            self.__forward_message_to_closest_node(message, node_id)

    def __handle_index(self, message):
        target_id = message["target_id"]
        if self.__id_is_me(target_id):
            self.__send_ack(target_id)
            word = message["keyword"]
            urls = message["link"]

            # TODO add indexing code, the following is wrong

            self.__db.index_results(word, urls)
        else:
            self.__forward_message_to_closest_node(message, target_id)

    def __send_ack(self, target_id):
        message = self.__send_formatter.ack(target_id)
        ip = self.__normalise_ip_to_pair(target_id)
        self.send_message(message, ip)

    def __forward_message_to_closest_node(self, message, node_id):
        if type(message) is dict:
            message = json.dumps(message)
        closest_node = self.table.get_closest_node_id(node_id)
        if closest_node:
            self.__send_message(message, closest_node)

    def __send_message(self, message, node_id):
        ip = self.__normalise_ip_to_pair(node_id)
        self.send_message(message, ip)
