# -*- coding: utf-8 -*-
SPORT_TYPES = ['TEAM', 'TABLE']


class Sport(object):
    def __init__(self, name, time, type, filename):
        self.name = name
        self.time = time
        self.type = type
        self.filename = filename
        self.name2team = {}
        assert type in SPORT_TYPES, "bad type of sport " + name

    def register_team(self, team):
        self.name2team[team.name] = team
