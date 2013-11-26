__author__ = 'mike'

import argparse

class Parser():

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--boot', type=int, default=0, help="Start network with defined id")

    def parse_args(self):
        return self.parser.parse_args()
