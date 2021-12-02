from Group.chap_2.sport_team import SportTeam


class BasketTeam(SportTeam):
    def stats(self):
        return "[BASKETBALL] STATS : " + super().stats()


basket = BasketTeam("Paris", 34, 67)

print(basket.stats())
