from Group.chap_2.basket_team import BasketTeam
from Group.chap_2.football_team import FootBallTeam


team_1 = BasketTeam("Golden State Warrios", 12, 39)
team_2 = FootBallTeam("Los Angles Lakers", 40, 10)

with open("milwaukee.txt") as file:
    name, wins, losses = file.readline().strip().split("-")
    team_4 = BasketTeam(name, int(wins), int(losses))
    print(team_4.stats())

# team_4 = BasketBallTeam.from_file('milwaukee.txt')
# print(team_4.stats())

# team_1.set_fine_amount(80_000)
# print(team_1.fine_amount)

# print(team_1.total_fines)
# team_1.get_fined()
# team_1.get_fined()
# print(team_1.total_fines)

# print(BasketBallTeam.fine_amount)
# print(team_1.fine_amount)
# print(team_2.fine_amount)
# print(team_1.fine_amount)
# print(team_1.get_fined())


