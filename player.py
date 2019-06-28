# -*- coding: utf-8 -*-
from event import is_intersecting


class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.teams = []
        self.events = []

    def register_player_in_team(self, team):
        self.teams.append(team)

    def add_event_for_player(self, event):
        for cur in self.events:
            assert not is_intersecting(cur, event), "player " + self.name + " with id="
        self.events.append(event)
