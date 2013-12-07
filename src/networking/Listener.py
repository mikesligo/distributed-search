from src.networking.IP_Parser import IP_Parser
from Exceptions.Table_lookup_failed_exception import Table_lookup_failed_exception

class Listener():

    def __init__(self, message_handler):
        self.message_handler = message_handler

    def listen(self):
        print "Listening..."
        while True:
            recv_data, addr = self.message_handler.socket.recvfrom(2048)
            print "Received data..."
            try:
                self.message_handler.handle(recv_data, addr)
            except Table_lookup_failed_exception as e:
                print str(e)
