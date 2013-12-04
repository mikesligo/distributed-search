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

        print "Received message - " + message_type

        if message_type == "JOINING_NETWORK":
            self.handle_joining_network(message, sender_addr)
        if message_type == "ROUTING_INFO":
            self.handle_routing_info(message, sender_addr)
        if message_type == "JOINING_NETWORK_RELAY":
            self.handle_joining_network_relay(message)

    def join_network(self, bootstrap_ip):
        to_send = self.send_formatter.send_joining_network()
        self.socket.sendto(to_send, bootstrap_ip.get_ip_pair())

    def handle_routing_info(self, message, sender_addr):
        self.table.load_routing_info(message["route_table"])
        self.table.add_routing_info(message["gateway_id"], message["ip_address"])

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
        self.socket.sendto(message, normalised_ip)

    def handle_joining_network(self, message, sender_addr):
        node_id = message["node_id"]
        node_ip = message["ip_address"]

        closest_node = self.table.get_ip_of_node_closest_to_id(node_id)
        if closest_node:
            self.send_joining_network_relay(node_id, closest_node)

        self.table.add_routing_info(node_id, node_ip)
        to_send = self.send_formatter.send_routing_info(node_id, self.table.node_id)
        self.socket.sendto(to_send, sender_addr)

    def forward_joining_network_relay(self, message, closest_node):
        normalised_ip = self.parser.parse(closest_node["ip_address"]).get_ip_pair()
        self.socket.sendto(message, normalised_ip)

    def send_joining_network_relay(self, node_id, closest_node):
        to_send = self.send_formatter.send_joining_network_relay(node_id)
        self.forward_joining_network_relay(to_send, closest_node)
