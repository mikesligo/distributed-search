__author__ = 'mike'

from Exceptions.Invalid_IP_exception import Invalid_IP_exception

class IP():

    def __init__(self, ip=None, port=None):
        self.ip = ip
        self.port = port

    def __str__(self):
        return str(self.ip) + ":" + str(self.port)

    def get_ip_pair(self):
        return (self.ip, int(self.port))