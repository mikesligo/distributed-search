from src.networking import IP_Parser

__author__ = 'mike'

import unittest
from src.Search_result import SearchResult
from src.Peer_search import Peer_search
from src.Node import Node
from src.Encoder import Encoder
from src.networking.IP_Parser import IP_Parser
from Exceptions.Invalid_IP_exception import Invalid_IP_exception
from Global.Global_consts import Global_consts

class Test_start_node_as_boot(unittest.TestCase):

    def setUp(self):
        self.node = Node()

    def test_default_ip_set_up(self):
        self.assertEqual(self.node.IP.ip, Global_consts.default_ip, "Default ip not set")
        self.assertEqual(self.node.IP.port, Global_consts.default_port, "Default port not set")

    def test_node_accepting_connections(self):
        pass

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

    def test_default_ip_for_node(self):
        self.assertEqual(self.node.IP.ip, Global_consts.default_ip, "Default ip not set")
        self.assertEqual(self.node.IP.port, Global_consts.default_port, "Default port not set")

class Test_Node_attributes_passed_and_set(unittest.TestCase):

    def setUp(self):
        self.test_id = 12345
        self.node = Node(id=self.test_id)

    def test_check_id_generated(self):
        self.assertTrue(self.node.id == self.test_id)

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
