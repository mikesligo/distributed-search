from src.networking.Network_utils import Network_utils

def send_joining_network():
    socket = Network_utils.get_test_udp_socket()
    data = '''{
    "type": "JOINING_NETWORK",
    "node_id": "42",
    "ip_address": "199.1.5.2:3434"
}'''
    socket.sendto(data, Network_utils.get_default_server_addr())

if __name__ == '__main__':
    send_joining_network()