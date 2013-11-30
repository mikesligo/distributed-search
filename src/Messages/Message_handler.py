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
        type = message["type"]
        if not type:
            print "Warning - Malformed message received"
            return

        if type == "JOINING_NETWORK":
            self.handle_joining_network(message, sender_addr)

    def join_network(self, bootstrap_ip):
        to_send = self.send_formatter.send_joining_network()
        self.socket.sendto(to_send, bootstrap_ip.get_ip_pair())

    def handle_joining_network(self, message, sender_addr):
        print "Received message - JOINING_NETWORK"
        self.table.add_routing_info(message["node_id"], message["ip_address"])
        self.table.add_routing_info(23, message["ip_address"])
        to_send = self.send_formatter.send_routing_info(message["node_id"])
        self.socket.sendto(to_send, sender_addr)

        # possibly forward joinig_network_relay to node with numerically closer id
