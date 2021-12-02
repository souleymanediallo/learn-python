def pluralize(total, singular, plural=None):
    assert isinstance(total, int) and total >= 0, "Le total doit être une valeur entière positive."

    if plural is None:
        plural = singular + "s"

    string = singular if total <= 1 else plural

    return f"{total} {string}"


r = pluralize(2, "evenemnts", "evements")
print(r)


def get_basketball_team_stats(team_name, wins, losses):
    return f"[BASKETBALL] STATS : {team_name} : {pluralize(wins, 'vitorire')}, {pluralize(losses, 'defaites')}"


def get_football_team_stats(team_name, wins, losses):
    return f"[FOOTBALL] STATS : {team_name}, {pluralize(wins, 'victoire')}, {pluralize(losses, 'defaite')}"


if __name__ == '__main__':
    # Basketball TEAMS
    print(get_football_team_stats("Golden State Warrioes", 12, 39))
    print(get_basketball_team_stats("Los Angeles Lakers", 37, 11))

    raptors_stats = "Toronto Raptors-36-14"
    data = raptors_stats.split("-")
    print(get_basketball_team_stats(data[0], int(data[1]), int(data[2])))

    with open("milwaukee.txt", "r") as file:
        data = file.readline().strip().split("-")
        print(get_basketball_team_stats(data[0], int(data[1]), int(data[2])))


