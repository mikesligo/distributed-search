__author__ = 'mike'

from IP_struct import IP
from Global.Global_consts import Global_consts

class IP_Parser():

    def __init__(self):
        self.ip = None
        self.port = None

    def parse(self, to_parse):
        if to_parse is None:
            return self.get_default_IP()

        ip = IP()
        split = to_parse.split(":")
        ip.set_ip(split[0])

        if len(split) == 1:
            ip.set_port(self.__get_default_port())
        elif len(split) == 2:
            ip.set_port(split[1])
        else:
            raise Exception("Was not able to parse IP")
        return ip

    def __get_default_port(self):
        return Global_consts.default_port

    def __get_default_ip_addr(self):
        return Global_consts.default_ip

    def get_default_IP(self):
        ip = IP()
        ip.ip = self.__get_default_ip_addr()
        ip.port = self.__get_default_port()
        return ip
