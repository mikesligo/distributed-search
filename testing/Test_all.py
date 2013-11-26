__author__ = 'mike'

import unittest
from src.Search_result import SearchResult
from src.Peer_search import Peer_search
from src.Node import Node
from src.Encoder import Encoder

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
