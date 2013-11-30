from src.networking.IP_Parser import IP_Parser

class Listener():

    def __init__(self, message_handler):
        self.message_handler = message_handler

    def listen(self):
        print "Listening..."
        while True:
            recv_data, addr = self.message_handler.socket.recvfrom(2048)
            print "Received data..."
            self.message_handler.handle(recv_data, addr)