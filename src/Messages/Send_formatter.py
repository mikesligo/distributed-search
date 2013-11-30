import json

class Send_formatter(object):

    def __init__(self, table):
        self.table = table

    def send_routing_info(self, node_id):
        message = {}
        message["type"] = "ROUTING_INFO"
        message["gateway_id"] = self.table.node_id
        message["node_id"] = node_id
        message["ip_address"] = str(self.table.node_ip)
        message["table"] = self.table.get_routing_table_json()
        jsoned_msg = json.dumps(message)
        return jsoned_msg
