from Global.Global_consts import Global_consts
import socket

class Network_utils():

    @staticmethod
    def get_default_udp_socket():
        host = Global_consts.default_ip
        port = Global_consts.default_port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(3.0)
        s.bind((host,port))
        return s

    @staticmethod
    def get_test_udp_socket():
        host = Global_consts.default_ip
        port = 1234
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(3.0)
        s.bind((host,port))
        return s