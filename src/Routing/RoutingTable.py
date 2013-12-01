import math
import json

class RoutingTable(object):

    def __init__(self, node_id, node_ip):
        self.__table = {}
        self.node_id = node_id
        self.node_ip = node_ip

    def add_routing_info(self, id, ip):
        self.__table[int(id)] = ip

    def get_routing_table_json(self):
        return [{"node_id":entry, "ip_address":str(self.__table[entry])} for entry in self.__table.keys()]

    def get_ip_of_node_closest_to_id(self, node_id):
        node_id = int(node_id)
        if self.node_id == node_id:
            return self.node_ip
        sorted_ids = sorted(self.__table.keys())

        closest = 0
        for i in sorted_ids:
            if abs(node_id-i) < abs(node_id-closest):
                closest = i

        return self.__table[closest]

    def load_routing_info(self, list_of_info):
        #[self.add_routing_info(entry.keys(), entry[entry.keys()]) for entry in list_of_info]
        for entry in list_of_info:
            self.add_routing_info(entry["node_id"], entry["ip_address"])
        pass
