from random import choice

from player import Player


class PlayerGenerator():
    def __init__(self):
        self.names = self.load_names_from_file()
        self.surs = self.load_surs_from_file()

    def load_names_from_file(self):
        with open("first-names.txt", 'r') as file:
            names = [name.strip() for name in file.readlines()]
        return names

    def load_surs_from_file(self):
        with open("last-names.txt", 'r') as file:
            surs = [sur.strip() for sur in file.readlines()]
        return surs

    def generate_players(self, amount=1, seed=False):
        if not seed:
            return [self._generate() for i in range(amount)]
        else:
            return [self._generate(i+1) for i in range(amount)]

    def _generate(self, seed=None):
        return Player(choice(self.names), choice(self.surs), seed)
