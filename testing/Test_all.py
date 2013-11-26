__author__ = 'mike'

import unittest
from src.Search_result import SearchResult
from src.Peer_search import Peer_search
from src.Skeleton import Skeleton

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
