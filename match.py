from random import random

from player import Player

class Match():
    def __init__(self, player1, player2, legs_to_win):
        self.player1 = player1
        self.player2 = player2
        self.legs_to_win = legs_to_win

        self.winner = None
        self.player1_legs = 0
        self.player2_legs = 0

    def __repr__(self):
        return f"{self.player1} {self.player1_legs}:{self.player2_legs} {self.player2}"

    def _play_leg(self):
        if random() >= 0.5:
            self.player1_legs += 1 
        else:
            self.player2_legs += 1

        self._check_if_finished()

    def _check_if_finished(self):
        if self.player1_legs == self.legs_to_win:
            self.winner = self.player1
        elif self.player2_legs == self.legs_to_win:
            self.winner = self.player2

    def simulate(self):
        while not isinstance(self.winner, Player):
            self._play_leg()
        return self.winner
