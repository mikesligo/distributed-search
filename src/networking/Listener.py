from src.Messages.Message_handler import Message_handler
from src.networking.IP_Parser import IP_Parser

class Listener():

    def __init__(self, socket, table):
        self.socket = socket
        self.table = table
        self.message_handler = Message_handler(self.table, self.socket)

    def listen(self):
        print "Listening..."
        while True:
            recv_data, addr = self.socket.recvfrom(2048)
            print "Received data..."
            self.message_handler.handle(recv_data, addr)