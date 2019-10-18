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

        self.extended = False
        self.max_legs = legs_to_win + 3

    def __repr__(self):
        return f"{self.player1} {self.player1_legs}:{self.player2_legs} {self.player2}"

    def _play_leg(self):
        if random() >= 0.5:
            self.player1_legs += 1 
        else:
            self.player2_legs += 1

        if not self.extended and self.player1_legs == self.legs_to_win-1 and self.player2_legs == self.legs_to_win-1:
            self.extended = True

        self._check_if_finished()

    def _check_if_finished(self):
        if not self.extended:
            if self.player1_legs == self.legs_to_win:
                self.winner = self.player1
            elif self.player2_legs == self.legs_to_win:
                self.winner = self.player2
        else:
            if self.player1_legs == self.player2_legs+2 or self.player1_legs == self.max_legs:
                self.winner = self.player1
            elif self.player2_legs == self.player1_legs+2 or self.player2_legs == self.max_legs:
                self.winner = self.player2

    def simulate(self):
        while not isinstance(self.winner, Player):
            self._play_leg()
        return self.winner
