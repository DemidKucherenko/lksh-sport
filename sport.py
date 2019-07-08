# -*- coding: utf-8 -*-
from enum import Enum


class SportType(Enum):
    TEAM = 0
    TABLE = 1


TYPE_MAP = {"TEAM": SportType.TEAM, "TABLE": SportType.TABLE}


class Sport(object):
    def __init__(self, name, time, type, filename):
        self.name = name
        self.time = time
        assert type in TYPE_MAP, "bad type of sport " + name
        self.type = TYPE_MAP[type]
        self.filename = filename
        self.name2team = {}

    def register_team(self, team):
        self.name2team[team.name] = team
