from IP_struct import IP
from Global.Global_consts import Global_consts

class IP_Parser():

    def parse(self, to_parse):
        if to_parse is None:
            return self.get_default_IP()

        split = to_parse.split(":")
        ip = split[0]

        if len(split) == 1:
            return IP(ip, self.__get_default_port())
        if len(split) == 2:
            return IP(ip, split[1])
        raise Exception("Was not able to parse IP")

    def parse_from_tuple(self, tuple):
        return IP(tuple[0], tuple[1])

    def __get_default_port(self):
        return Global_consts.default_port

    def __get_default_ip_addr(self):
        return Global_consts.default_ip

    def get_default_IP(self):
        ip = IP()
        ip.ip = self.__get_default_ip_addr()
        ip.port = self.__get_default_port()
        return ip
