
class RoutingTable(object):

    def __init__(self, node_id, node_ip):
        self.__table = {}
        self.node_id = node_id
        self.node_ip = node_ip

    def add_routing_info(self, id, ip):
        self.__table[id] = ip
