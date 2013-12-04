import json
from Send_formatter import Send_formatter
from src.networking.IP_Parser import IP_Parser

class Message_handler(object):

    def __init__(self, table, socket):
        self.parser = IP_Parser()
        self.table = table
        self.socket = socket
        self.send_formatter = Send_formatter(self.table)

    def handle(self, data, sender_addr):
        message = json.loads(data)
        message_type = message["type"]
        if not message_type:
            print "Warning - Malformed message received"
            return

        print "Received message - " + message_type + " from " + str(sender_addr[0]) + ":" + str(sender_addr[1])
        print message

        if message_type == "JOINING_NETWORK":
            self.handle_joining_network(message, sender_addr)
        if message_type == "ROUTING_INFO":
            self.handle_routing_info(message, sender_addr)
        if message_type == "JOINING_NETWORK_RELAY":
            self.handle_joining_network_relay(message)

    def join_network(self, bootstrap_ip):
        to_send = self.send_formatter.send_joining_network()
        self.send_message(to_send, bootstrap_ip.get_ip_pair())

    def handle_routing_info(self, message, sender_addr):
        self.table.load_routing_info(message["route_table"])
        if self.__sender_is_gateway(message, sender_addr):
            self.table.add_routing_info(message["gateway_id"], message["ip_address"])
        self.__forward_routing_info_if_necessary(message)

    def __sender_is_gateway(self, message, sender_addr):
        msg_ip = str(message["ip_address"])
        parsed_sender_addr = str(self.parser.parse_from_tuple(sender_addr))
        return msg_ip == parsed_sender_addr

    def __forward_routing_info_if_necessary(self, message):
        node_id = int(message["node_id"])
        gateway_id = message["gateway_id"]

        if node_id != int(self.table.node_id):
            if gateway_id == int(self.table.node_id):
                ip = self.table.get_ip_of_node(node_id)
                ip_normalised = self.parser.parse(ip).get_ip_pair()
                jsoned = json.dumps(message)
                self.send_message(jsoned, ip_normalised)
            else:
                print "Error - Expecting to forward routing info but I am not gateway"
                return


    def handle_joining_network_relay(self, message):
        gateway_id = message["gateway_id"]
        node_id = message["node_id"]

        closest_node = self.table.get_ip_of_node_closest_to_id(node_id)
        if closest_node:
            self.forward_joining_network_relay(message, closest_node)

        to_send = self.send_formatter.send_routing_info(node_id, gateway_id)
        self.send_to_node_id(to_send, gateway_id)

    def send_to_node_id(self, message, node_id):
        try:
            node_ip = self.table.get_ip_of_node(node_id)
        except KeyError:
            print "Error - Could not find ip of node " + str(node_id)
            return
        normalised_ip = self.parser.parse(node_ip).get_ip_pair()
        self.send_message(message, normalised_ip)

    def handle_joining_network(self, message, sender_addr):
        node_id = message["node_id"]
        node_ip = message["ip_address"]

        closest_node = self.table.get_ip_of_node_closest_to_id(node_id)
        if closest_node:
            self.send_initial_joining_network_relay(node_id, closest_node)

        to_send = self.send_formatter.send_routing_info(node_id, self.table.node_id)
        self.table.add_routing_info(node_id, node_ip)
        self.send_message(to_send, sender_addr)

    def forward_joining_network_relay(self, message, closest_node):
        normalised_ip = self.parser.parse(closest_node["ip_address"]).get_ip_pair()
        self.send_message(message, normalised_ip)

    def send_initial_joining_network_relay(self, node_id, closest_node):
        to_send = self.send_formatter.send_joining_network_relay(node_id)
        self.forward_joining_network_relay(to_send, closest_node)

    def send_message(self, message, sender_addr):
        sender_ip = sender_addr[0]
        sender_port = str(sender_addr[1])
        loaded = json.loads(message)
        print "Sending " + loaded["type"] + " to " + sender_ip + ":" + sender_port
        print message
        self.socket.sendto(message, sender_addr)
