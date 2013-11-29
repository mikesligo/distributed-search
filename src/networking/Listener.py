import logging

class Listener():

    def __init__(self, socket):
        self.socket = socket

    def listen(self):
        logging.info("Listening...")
        while True:
            recv_data, addr = self.socket.recvfrom(2048)
            print recv_data

    def echo(self):
        logging.info("Echoing...")
        recv_data, addr = self.socket.recvfrom(2048)
        self.socket.sendto(recv_data, addr)
