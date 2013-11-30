import json
from Message_sender import Mesaage_sender

class Message_handler(object):

    def __init__(self, table, addr):
        self.table = table
        self.sender_addr = addr
        self.send_handler = Mesaage_sender()

    def handle(self, data):
        message = json.loads(data)
        type = message["type"]
        if not type:
            print "Warning - Malformed message received"
            return
        if type == "JOINING_NETWORK":
            self.handle_joining_network(message)

    def handle_joining_network(self, message):
        print "Received message - JOINING_NETWORK"
        self.table.add_routing_info(message["node_id"], message["ip_address"])
        self.send_handler.send_routing_info()
        # reply with routing_info
        # possibly forward joinig_network_relay to node with numerically closer id
