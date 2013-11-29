import unittest

import threading

from src.Search_result import SearchResult
from src.Peer_search import Peer_search
from src.Node import Node
from src.Encoder import Encoder
from src.networking.IP_Parser import IP_Parser
from src.networking.Listener import Listener
from src.networking.Network_utils import Network_utils
from Exceptions.Invalid_IP_exception import Invalid_IP_exception
from Exceptions.TimeoutError import TimeoutError
from Global.Global_consts import Global_consts

class Test_listener_works_as_echo_server(unittest.TestCase):

    def setUp(self):
        self.socket = Network_utils.get_default_udp_socket()
        self.client_sock = Network_utils.get_test_udp_socket()
        self.listener = Listener(self.socket)

    def test_listener_echo_server(self):
        listen_thread = threading.Thread(target=self.listener.echo(), args=())
        send_data = "ping"
        self.client_sock.sendto(send_data)
        data, server = self.client_sock.recvfrom(4096)
        self.assertEqual(send_data, data)

    def tearDown(self):
        self.socket.close()
        self.client_sock.close()

class Test_start_node_as_boot(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    def test_node_accepting_connections(self):
        pass

    def tearDown(self):
        self.node.socket.close()

class Test_IP_Parser_parse_method_valid_inputs(unittest.TestCase):

    def setUp(self):
        self.parser = IP_Parser()

    def test_valid_ip_addr(self):
        str = "127.2.2.1:1234"
        ip = self.parser.parse(str)
        self.assertEqual(ip.ip, "127.2.2.1", "Did not parse valid ip correctly")
        self.assertEqual(ip.port, 1234, "Did not parse valid port correctly")

    def test_no_port_given(self):
        str = "127.2.2.1"
        ip = self.parser.parse(str)
        self.assertEqual(ip.ip, "127.2.2.1", "Did not parse valid ip correctly")
        self.assertEqual(ip.port, Global_consts.default_port, "Did not parse valid port correctly")

class Test_IP_Parser_parse_method_edge_cases(unittest.TestCase):

    def setUp(self):
        self.parser = IP_Parser()

    def test_invalid_ip_addr(self):
        str = "127.2.1:1234"
        try:
            ip = self.parser.parse(str)
        except Invalid_IP_exception:
            return
        self.fail("Did not recognise invalid IP")

    def test_invalid_port(self):
        str = "127.2.1.1:"
        try:
            ip = self.parser.parse(str)
        except Invalid_IP_exception:
            return
        self.fail("Did not recognise invalid Port")

class Test_encoder_generate_random_id(unittest.TestCase):

    def setUp(self):
        self.encoder = Encoder()

    def test_random_id(self):
        self.assertNotEquals(self.encoder.generate_random_id(), None, "Encoder not generating random id")
        self.assertNotEquals(self.encoder.generate_random_id(), 0, "Encoder not generating random id")

class Test_Node_default_attributes(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    def test_check_id_generated(self):
        self.assertTrue(self.node.id)
        self.assertTrue(self.node.socket)

    def tearDown(self):
        self.node.socket.close()

class Test_Node_attributes_passed_and_set(unittest.TestCase):

    def setUp(self):
        self.test_id = 12345
        self.node = Node(id=self.test_id)

    def test_check_id_generated(self):
        self.assertTrue(self.node.id == self.test_id)

    def tearDown(self):
        self.node.socket.close()

class Test_search_result_conforms_to_interface(unittest.TestCase):

    def setUp(self):
        self.search = SearchResult()

    def test_class_attributes(self):
        self.assertTrue("words" in self.search.__dict__, "words attribute not defined")
        self.assertTrue("url" in self.search.__dict__, "words attribute not defined")
        self.assertTrue("frequency" in self.search.__dict__, "words attribute not defined")

class Test_Peer_search_has_interface_methods(unittest.TestCase):

    def setUp(self):
        self.search = Peer_search()

    def test_methods_exist(self):
        self.assertTrue("init" in dir(self.search), "Could not find interface method for peersearch")
        self.assertTrue("join_network" in dir(self.search), "Could not find interface method for peersearch")
        self.assertTrue("leave_network" in dir(self.search), "Could not find interface method for peersearch")
        self.assertTrue("index_page" in dir(self.search), "Could not find interface method for peersearch")
        self.assertTrue("search" in dir(self.search), "Could not find interface method for peersearch")
