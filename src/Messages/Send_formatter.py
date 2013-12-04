import json

class Send_formatter(object):

    def __init__(self, table):
        self.table = table

    def send_routing_info(self, node_id, gateway_node_id):
        print "Sending ROUTING_INFO"
        message = {}
        message["type"] = "ROUTING_INFO"
        message["gateway_id"] = gateway_node_id
        message["node_id"] = node_id
        message["ip_address"] = str(self.table.node_ip)
        message["route_table"] = self.table.get_routing_table_json()
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def send_joining_network(self):
        print "Sending JOINING_NETWORK"
        message = {}
        message["type"] = "JOINING_NETWORK"
        message["node_id"] = self.table.node_id
        message["ip_address"] = str(self.table.node_ip)
        jsoned_msg = json.dumps(message)
        return jsoned_msg

    def send_joining_network_relay(self, node_id):
        print "Sending JOINING_NETWORK_RELAY"
        message = {}
        message["type"] = "JOINING_NETWORK_RELAY"
        message["node_id"] = node_id
        message["gateway_id"] = self.table.node_id
        jsoned_msg = json.dumps(message)
        return jsoned_msg
