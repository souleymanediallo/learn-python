import utils


class SportTeam:
    number_of_teams = 0
    fine_amount = 50_000

    def __init__(self, name, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.total_fines = 0
        SportTeam.number_of_teams += 1

    @classmethod
    def from_string(cls, stats_as_string):
        name, wins, losses = stats_as_string.split("-")
        return cls(name, wins, losses)

    @classmethod
    def from_file(cls, stats_as_file):
        with open(stats_as_file, "r") as f:
            name, wins, losses = f.readline().strip().split("-")
            return cls(name, int(wins), int(losses))

    def get_fined(self):
        self.total_fines += self.fine_amount

    def stats(self):
        return f"{self.name} has {utils.pluralize(self.wins, 'victoire')} and {utils.pluralize(self.losses, 'defaite')}"

    @classmethod
    def set_fine_amount(cls, amount):
        cls.fine_amount = amount
