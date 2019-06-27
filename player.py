class Player(object):
    def __init__(self, name):
        self.name = name
        self.teams = []

    def register_player_in_team(self, team):
        self.teams.append(team)
