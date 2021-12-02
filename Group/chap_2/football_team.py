from Group.chap_2.sport_team import SportTeam


class FootBallTeam(SportTeam):
    def stats(self):
        return "[FOOTBALL] STATS : " + super().stats()


foot_ball = FootBallTeam("Marseille", 34, 5)
print(foot_ball.stats())