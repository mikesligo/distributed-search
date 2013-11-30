class RoutingTable(object):

    def __init__(self, node_id, node_ip):
        self.__table = {}
        self.node_id = node_id
        self.node_ip = node_ip

    def add_routing_info(self, id, ip):
        self.__table[id] = ip

    def get_routing_table_json(self):
        return [{entry:str(self.__table[entry])} for entry in self.__table.keys()]
