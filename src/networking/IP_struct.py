__author__ = 'mike'

from Exceptions.Invalid_IP_exception import Invalid_IP_exception

class IP():

    def __init__(self, ip=None, port=None):
        self.ip = ip
        self.port = port

    def set_ip(self, ip):
        if not len(ip.split(".")) == 4:
            raise Invalid_IP_exception("Not all ip digits found")
        if ip is None or "":
            raise Invalid_IP_exception("Attempted to parse empty string as ip")
        self.ip = ip

    def set_port(self, port):
        if not port:
            raise Invalid_IP_exception("Attempted to parse empty string as port")
        self.port = int(port)
