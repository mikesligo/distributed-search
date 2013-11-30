__author__ = 'mike'

import argparse
from Args import Args

class Parser():

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--boot', type=int, default=0, help="Start network with defined id")
        self.parser.add_argument('--bootstrap', default=None, help="Start network with defined id")
        self.parser.add_argument('--id', default=None, help="Start network with defined id")
        self.parser.add_argument('--ip', default="127.0.0.1:8767", help="Start network with defined id")
        self.args = Args()

    def get_parsed_args(self):
        parsed = self.parser.parse_args()
        self.args.id = parsed.boot or parsed.id
        self.args.boot = True if parsed.boot else False
        self.args.bootstrap = parsed.bootstrap
        self.args.ip = parsed.ip
        return self.args
