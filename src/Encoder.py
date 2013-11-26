__author__ = 'mike'

import random

class Encoder():

    def __init__(self):
        pass

    def generate_random_id(self):
        return random.randint(0, 2**32)
