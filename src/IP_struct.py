__author__ = 'mike'

from Exceptions.Invalid_IP_exception import Invalid_IP_exception

class IP():

    def __init__(self):
        self.ip = None
        self.port = None

    def set_ip(self, ip):
        if not len(ip.split(".")) == 4:
            raise Invalid_IP_exception("Not all ip digits found")
        if ip is None or "":
            raise Invalid_IP_exception("Attempted to parse empty string as ip")
        self.ip = ip

    def set_port(self, port):
        if port is None or "":
            raise Invalid_IP_exception("Attempted to parse empty string as port")
        self.port = int(port)

