import random

class Encoder():

    def generate_random_id(self):
        return random.randint(0, 2**32)

    def get_hash_of_word(self, word):
        hash = 0
        for char in word:
            hash = hash*31 + int(ord(char))
        overflowed = hash % 2**32
        return overflowed
