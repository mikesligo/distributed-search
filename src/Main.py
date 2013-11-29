__author__ = 'mike'

from Peer_search import Peer_search
from networking.Network_utils import Network_utils

def main():
    peer_search = Peer_search()
    peer_search.init(Network_utils.get_default_udp_socket())

if __name__=='__main__':
    main()