from random import choice, shuffle

from match import Match
from player_generator import PlayerGenerator


class Tournament():

    def __init__(self, year=2137):
        self.gen = PlayerGenerator()
        self.MATCH_LENGTH = (10, 13, 16, 17, 18)
        self.SEEDS_PRIORITY = (1, 16, 8, 9, 5, 12, 4, 13, 2, 15, 7, 10, 6,
                               11, 3, 14)
        self.year = year

    def simulate(self):
        print(f"Simulating World Matchplay {self.year} ...")

        self.get_players()
        self.present_players()

        shuffle(self.qualifiers)

        self.first_round = self.draw_matches()
        self.second_round = self.simulate_round(self.first_round, self.MATCH_LENGTH[1])
        self.quarter_finals = self.simulate_round(self.second_round, self.MATCH_LENGTH[2])
        self.semi_finals = self.simulate_round(self.quarter_finals, self.MATCH_LENGTH[3])
        self.final = self.simulate_round(self.semi_finals, self.MATCH_LENGTH[4])
        self.winner = self.simulate_round(self.final, self.MATCH_LENGTH[4])

        self.show_round_results(self.first_round)
        self.show_round_results(self.second_round, "Second round")
        self.show_round_results(self.quarter_finals, "Quarter finals")
        self.show_round_results(self.semi_finals, "Semi finals")
        self.show_round_results(self.final, "Final")
        print(f"{self.winner} wins World Matchplay {self.year}! Congratulations!")

    def get_players(self, players=32):
        self.seeds = self.gen.generate_players(players//2, seed=True)
        self.qualifiers = self.gen.generate_players(players//2)

    def present_players(self):
        print("Seeds:")
        for player in self.seeds:
            print(player)
        print("\nQualifiers:")
        for player in self.qualifiers:
            print(player)
        print("")
    
    def draw_matches(self):
        first_round = []

        q = self.qualifiers[:]
        for iseed in self.SEEDS_PRIORITY:
            p1 = self.seeds[iseed-1]
            p2 = choice(q)
            first_round.append(Match(p1, p2, self.MATCH_LENGTH[0]))
            q.remove(p2)

        return first_round

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
