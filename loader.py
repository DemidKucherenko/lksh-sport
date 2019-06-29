# -*- coding: utf-8 -*-
from player import Player
from sport import Sport
from team import Team
from event import Event
from utils import *

players = []
sports = []
teams = []
events = []

name2sport = {}


def load_players():
    f = open('players.txt', encoding='utf-8')
    cnt = 1
    for name in f:
        name = remove_bad_symbol(name)
        players.append(Player(name.strip(), cnt))
        cnt += 1


def load_sports():
    f = open('sports.txt', encoding='utf-8')
    for sport in f:
        s = sport.split()
        sports.append(Sport(s[0], int(s[1]), s[2], s[3]))
        name2sport[s[0]] = sports[len(sports) - 1]


def find_player(players, name, info):
    for player in players:
        if player.name == name:
            return player
    assert False, "Can't find player " + name + " from " + info


def register_player_in_team(player, team):
    player.register_player_in_team(team)
    team.register_player_in_team(player)


def load_teams_from_file(sport):
    f = open(sport.filename, encoding='utf-8')
    status = True
    line_number = 0
    for line in f:
        line = line.strip()
        line_number += 1
        if line.strip() == "":
            status = True
            continue
        if status:
            teams.append(Team(line.strip(), sport))
            sport.register_team(teams[len(teams) - 1])
            status = False
        else:
            name = remove_bad_symbol(line.strip())
            player = find_player(players, name, "file " + sport.filename + " line " + str(line_number))
            register_player_in_team(player, teams[len(teams) - 1])


def load_current_schedule():
    f = open('schedule.txt', encoding='utf-8')
    first_line = True
    sport = None
    for line in f:
        s = line.split()
        if first_line:
            assert(len(s) == 1)
            first_line = False
        if len(s) == 1:
            assert name2sport.get(s[0]) is not None
            sport = name2sport[s[0]]
            continue
        start_time = convert_start_time(s[0])
        assert sport.name2team[s[1]] is not None
        assert sport.name2team[s[2]] is not None
        events.append(Event(start_time, sport, sport.name2team[s[1]], sport.name2team[s[2]]))


def load_data():
    load_players()
    load_sports()

    for sport in sports:
        load_teams_from_file(sport)

    return (players, sports, teams)


def check_schedule():
    load_current_schedule()
    return events
