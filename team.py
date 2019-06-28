# -*- coding: utf-8 -*-
class Team(object):
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport
        self.players = []

    def register_player_in_team(self, player):
        self.players.append(player)
