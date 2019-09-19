class Player():
    def __init__(self, name, sur, seed=None):
        self.name = name
        self.sur = sur
        self.seed = seed

    def __repr__(self):
        self.prefix = ""
        if self.seed:
            self.prefix = f"(#{self.seed}) "

        return f"{self.prefix}{self.name} {self.sur}"
