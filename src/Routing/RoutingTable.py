import math
import json

class RoutingTable(object):

    def __init__(self, node_id, node_ip):
        self.__table = {}
        self.node_id = int(node_id)
        self.node_ip = node_ip
        print "ID: " + str(node_id)
        print "IP: " + str(node_ip)

    def add_routing_info(self, id, ip):
        if int(self.node_id) != int(id):
            self.__table[int(id)] = ip

    def get_routing_table_json(self):
        return [{"node_id":entry, "ip_address":str(self.__table[entry])} for entry in self.__table.keys() if entry != self.node_id]

    def get_ip_of_node_closest_to_id(self, node_id): # I'm allowed 1 hacky method
        if not any(self.__table):
            return None
        node_id = int(node_id)
        if self.node_id == node_id:
            return None
        sorted_ids = sorted(self.__table.keys())

        closest = 0
        for i in sorted_ids:
            if abs(node_id-i) < abs(node_id-closest):
                closest = i

        if abs(node_id-self.node_id) <= abs(node_id-closest):
            return None

        if closest not in sorted_ids:
            return None

        return {"node_id":closest, "ip_address": self.__table[closest]}

    def load_routing_info(self, list_of_info):
        for entry in list_of_info:
            self.add_routing_info(entry["node_id"], entry["ip_address"])

    def get_ip_of_node(self, node_id):
        return self.__table[node_id]

    def remove_node_from_table(self, node_id):
        del(self.__table[node_id])
