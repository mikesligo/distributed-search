class Mesaage_sender(object):

    def __init__(self, table):
        self.table = table

    def send_routing_info(self, node_id):
        gateway_id = self.table.node_id
        ip_address = self.table.node_ip
