# -*- coding: utf-8 -*-
from player import Player
from sport import *
from team import Team
from event import Event
from utils import *

players = []
sports = []
teams = []
events = []

name2sport = {}


def load_players():
    f = open('configs/players.txt', encoding='utf-8')
    cnt = 1
    for name in f:
        name = remove_bad_symbol(name)
        players.append(Player(name.strip(), cnt))
        cnt += 1


def load_sports():
    f = open('configs/sports.txt', encoding='utf-8')
    for sport in f:
        s = sport.split()
        if len(s) == 3:
            assert s[2] == "TABLE"
            s.append("")
        sports.append(Sport(s[0], int(s[1]), s[2], s[3]))
        name2sport[s[0]] = sports[-1]


def find_player(players, name, info):
    for player in players:
        if player.name == name:
            return player
    assert False, "Can't find player " + name + " from " + info


def register_player_in_team(player, team):
    player.register_player_in_team(team)
    team.register_player_in_team(player)


def load_teams_from_file(sport):
    f = open("configs/" + sport.filename, encoding='utf-8')
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
            sport.register_team(teams[-1])
            status = False
        else:
            name = remove_bad_symbol(line.strip())
            player = find_player(players, name, "file " + sport.filename + " line " + str(line_number))
            register_player_in_team(player, teams[-1])


def load_current_schedule():
    f = open('configs/schedule-ready.txt', encoding='utf-8')
    sport = None
    time = 0
    read_names = False
    new_players = []
    line_number = 0
    for line in f:
        line_number += 1
        line = line.strip()
        if is_sport_name(line, sports):
            if read_names:
                events.append(Event.construct_from_players(time, sport, new_players))
            read_names = False
            assert name2sport.get(line) is not None
            sport = name2sport[line]
            continue

        if is_time(line):
            assert sport.type == SportType.TABLE
            time = convert_start_time(line)
            read_names = True
            continue

        if read_names:
            new_players.append(find_player(players, line, "file " + sport.filename + " line " + str(line_number)))
            continue

        assert is_time(line[0:5]), "problem in line " + str(line_number)
        assert sport.type == SportType.TEAM

        st = line[5:].split("-")
        assert (len(st) == 2), str(line_number)
        st[0] = st[0].strip()
        st[1] = st[1].strip()
        start_time = convert_start_time(line[0:5])
        assert sport.name2team[st[0]] is not None
        assert sport.name2team[st[1]] is not None
        events.append(Event.construct_from_teams(start_time, sport, sport.name2team[st[0]], sport.name2team[st[1]]))

    if read_names:
        assert len(new_players) > 0
        events.append(Event.construct_from_players(time, sport, new_players))


def load_data():
    load_players()
    load_sports()

    for sport in sports:
        if sport.type is SportType.TEAM:
            load_teams_from_file(sport)
        elif sport.type is SportType.TABLE:
            pass
        else:
            assert False, sport.type

    return players, sports, teams


def load_schedule():
    load_current_schedule()
    return events
