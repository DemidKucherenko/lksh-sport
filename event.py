# -*- coding: utf-8 -*-
from utils import convert_to_time
from sport import *


class Event(object):
    def __init__(self, time, sport, players):
        self.start_time = time
        self.sport = sport
        self.players = players
        for player in players:
            player.add_event_for_player(self)

    @classmethod
    def construct_from_players(cls, time, sport, players):
        assert sport.type is SportType.TABLE
        return cls(time, sport, players)

    @classmethod
    def construct_from_teams(cls, time, sport, team1, team2):
        assert sport.type is SportType.TEAM
        assert sport == team1.sport and sport == team2.sport
        players = []
        for player1 in team1.players:
            players.append(player1)
        for player2 in team2.players:
            players.append(player2)
        return cls(time, sport, players)

    def str(self):
        return "[" + convert_to_time(self.start_time) + " " + self.sport.name + "]"


def is_intersecting(event1, event2):
    return (event1.start_time < event2.start_time + event2.sport.time) and (event2.start_time < event1.start_time
                                                                            + event1.sport.time)
