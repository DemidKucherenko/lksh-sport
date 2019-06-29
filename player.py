# -*- coding: utf-8 -*-
class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.teams = []
        self.events = []

    def register_player_in_team(self, team):
        self.teams.append(team)

    def add_event_for_player(self, event):
        self.events.append(event)
