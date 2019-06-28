# -*- coding: utf-8 -*-
class Event(object):
    def __init__(self, time, sport, team1, team2):
        self.start_time = time
        self.sport = sport
        assert sport == team1.sport and sport == team2.sport
        self.players = []
        for player1 in team1.players:
            self.players.append(player1)
            player1.add_event_for_player(self)
        for player2 in team2.players:
            self.players.append(player2)
            player2.add_event_for_player(self)



def is_intersecting(event1, event2):
    return (event1.start_time >= event2.start_time + event2.sport.time) or (event2.start_time >= event1.start_time + event1.sport.time)
