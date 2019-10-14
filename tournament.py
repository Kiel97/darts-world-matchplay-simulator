from random import choice, shuffle
from math import log2

from match import Match
from player_generator import PlayerGenerator
from seed import Seed

class Tournament():

    bracket = {}

    def __init__(self, players=32, year=2137):
        self.gen = PlayerGenerator()
        self.MATCH_LENGTH = (10, 13, 16, 17, 18)
        self.SEEDS_PRIORITY = tuple(Seed.generate(players//2))
        self.ROUNDS_NAMES = ("Final", "Semi Finals", "Quarter Finals", "Round ")
        self.year = year
        self.players = players

    def simulate(self):
        print(f"Simulating World Matchplay {self.year} ...")

        self.get_players(self.players)
        self.present_competitors()

        shuffle(self.qualifiers)

        self.rounds = self.get_round_names()
        print(self.rounds)

        self.bracket["Round 1"] = self.draw_1st_round_matches()
        self.bracket["Round 2"] = self.simulate_round(self.bracket["Round 1"], self.MATCH_LENGTH[1])
        self.bracket["Quarter Finals"] = self.simulate_round(self.bracket["Round 2"], self.MATCH_LENGTH[2])
        self.bracket["Semi Finals"] = self.simulate_round(self.bracket["Quarter Finals"], self.MATCH_LENGTH[3])
        self.bracket["Final"] = self.simulate_round(self.bracket["Semi Finals"], self.MATCH_LENGTH[4])
        self.bracket["Winner"] = self.simulate_round(self.bracket["Final"], self.MATCH_LENGTH[4])

        self.show_round_results(self.bracket["Round 1"])
        self.show_round_results(self.bracket["Round 2"], "Second round")
        self.show_round_results(self.bracket["Quarter Finals"], "Quarter finals")
        self.show_round_results(self.bracket["Semi Finals"], "Semi finals")
        self.show_round_results(self.bracket["Final"], "Final")
        print(f"{self.bracket['Winner']} wins World Matchplay {self.year}! Congratulations!")

    def get_players(self, players=32):
        self.seeds = self.gen.generate_players(players//2, seed=True)
        self.qualifiers = self.gen.generate_players(players//2)

    def present_competitors(self):
        print("Seeds:")
        for player in self.seeds:
            print(player)
        print("\nQualifiers:")
        for player in self.qualifiers:
            print(player)
        print("")
    
    def get_round_names(self):
        self.rounds_amount = int(log2(self.players))
        rounds_names = []
        for i in range(self.rounds_amount):
            if i <= 2:
                rounds_names.append(self.ROUNDS_NAMES[i])
            else:
                rounds_names.append(self.ROUNDS_NAMES[3] + str(self.rounds_amount - i))
        rounds_names.reverse()
        return rounds_names

    def draw_1st_round_matches(self):
        draws = []

        q = self.qualifiers[:]
        for iseed in self.SEEDS_PRIORITY:
            p1 = self.seeds[iseed-1]
            p2 = choice(q)
            draws.append(Match(p1, p2, self.MATCH_LENGTH[0]))
            q.remove(p2)

        return draws

    def simulate_round(self, game_round, next_len):
        winners = []
        current_round = game_round[:]
        next_round = []

        for match in current_round:
            match.simulate()
            winner = match.has_winner()
            winners.append(winner)

        if len(winners) >= 2:
            for i in range(0, len(winners), 2):
                next_round.append(Match(winners[i], winners[i+1], next_len))
        else:
            next_round = winners[0]

        return next_round

    def show_round_results(self, game_round, title="First round"):
        print(f"{title} results:")
        for match in game_round:
            print(match)
        print("")
