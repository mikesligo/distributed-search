from src.Parser import Parser

from Peer_search import Peer_search
from src.networking.Network_utils import Network_utils
from src.networking.IP_Parser import IP_Parser

def main():
    parser = Parser()
    args = parser.get_parsed_args()
    ip_parser = IP_Parser()
    node_ip = ip_parser.parse(args.ip)
    peer_search = Peer_search()
    peer_search.init(Network_utils.get_udp_socket(node_ip.ip, int(node_ip.port)))
    peer_search.join_network(args.bootstrap)
    peer_search.index_page("reddit.com", ["reddit", "frontpage", "of", "the", "internet"])
    peer_search.index_page("reddit.com", ["reddit", "cats", "lots", "of", "cats"])
    peer_search.index_page("reddit.com", ["reddit", "hackernews", "internet", "of", "cats"])
    peer_search.index_page("news.ycombinator.com", ["reddit", "hackernews", "internet", "of", "cats"])
    peer_search.index_page("google.com", ["reddit", "frontpage", "of", "the", "internet"])

if __name__=='__main__':
    main()