from math import log2, ceil

class Seed:

    def generate(self, players=16):
        iters = ceil(log2(players))
        seeds = [1]
        for i in range(iters):
            seeds = Seed.seed_bracket(seeds)
        
        return seeds


    def seed_bracket(bracket):
        out = []
        for n in bracket:
            out.append(n)
            out.append(2*len(bracket)+1-n)
        return out