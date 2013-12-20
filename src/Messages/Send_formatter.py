import json

class Send_formatter(object):

    def __init__(self, table):
        self.table = table

    def send_routing_info(self, node_id, gateway_node_id):
        message = {}
        message["type"] = "ROUTING_INFO"
        message["gateway_id"] = gateway_node_id
        message["node_id"] = node_id
        message["ip_address"] = str(self.table.node_ip)
        message["route_table"] = self.table.get_routing_table_json()
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def send_joining_network(self):
        message = {}
        message["type"] = "JOINING_NETWORK"
        message["node_id"] = self.table.node_id
        message["ip_address"] = str(self.table.node_ip)
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def send_joining_network_relay(self, node_id):
        message = {}
        message["type"] = "JOINING_NETWORK_RELAY"
        message["node_id"] = node_id
        message["gateway_id"] = self.table.node_id
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def search(self, word, node_id):
        message = {}
        message["type"] = "SEARCH"
        message["word"] = word
        message["node_id"] = node_id
        message["sender_id"] = str(self.table.node_id)
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def search_response(self, word, node_id, results):
        message = {}
        message["type"] = "SEARCH_RESPONSE"
        message["word"] = word
        message["node_id"] = node_id
        message["sender_id"] = str(self.table.node_id)
        message["response"] = results
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def ack(self, node_id):
        message = {}
        message["type"] = "ACK"
        message["node_id"] = node_id
        message["ip_address"] = str(self.table.node_ip)
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def index(self, target_id, keyword, link):
        message = {}
        message["type"] = "INDEX"
        message["target_id"] = str(target_id)
        message["sender_id"] = str(self.table.node_id)
        message["keyword"] = keyword
        message["link"] = [link]
        jsoned_msg = json.dumps(message)
        return jsoned_msg
